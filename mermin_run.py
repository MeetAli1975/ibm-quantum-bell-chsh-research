#!/usr/bin/env python3
"""Mermin inequality on a 3-qubit GHZ state: simulator, chain finder, or IBM hardware.

Usage (run with ~/quantum_env/bin/python):
  mermin_run.py sim                      ideal local simulator, never contacts IBM
  mermin_run.py chains ibm_fez           read-only: best 3-qubit chains on a backend
  mermin_run.py submit ibm_fez A B C     submits after you type YES (B is the middle qubit)

State: GHZ = (|000> + |111>) / sqrt(2)
  M = <XXX> - <XYY> - <YXY> - <YYX>
  classical (local hidden variable) bound |M| <= 2, quantum maximum 4
"""
import json
import math
import sys
import time

from qiskit import QuantumCircuit

SHOTS = 1024
# name: (measurement bases for qubits 0,1,2, sign of the term in M)
SETTINGS = {
    "XXX": ("XXX", +1),
    "XYY": ("XYY", -1),
    "YXY": ("YXY", -1),
    "YYX": ("YYX", -1),
}


def build_circuits():
    circuits = []
    for name, (bases, _) in SETTINGS.items():
        qc = QuantumCircuit(3, 3, name=name)
        qc.h(0)
        qc.cx(0, 1)
        qc.cx(1, 2)
        for q, basis in enumerate(bases):
            if basis == "Y":
                qc.sdg(q)
            qc.h(q)
        qc.measure([0, 1, 2], [0, 1, 2])
        circuits.append(qc)
    return circuits


def parity_expectation(counts):
    total = sum(counts.values())
    signed = sum(
        n * (-1) ** bin(int(k.replace(" ", ""), 2)).count("1")
        for k, n in counts.items()
    )
    return signed / total, total


def report(all_counts):
    exp, shots = {}, {}
    for (name, (_, sign)), counts in zip(SETTINGS.items(), all_counts):
        exp[name], shots[name] = parity_expectation(counts)
        print(f"<{name}> = {exp[name]:+.6f}  (ideal {sign:+d}, {shots[name]} shots)")
    m = sum(sign * exp[name] for name, (_, sign) in SETTINGS.items())
    se = math.sqrt(sum((1 - exp[k] ** 2) / shots[k] for k in exp))
    print(f"\nMermin M: {m:.6f}  (classical bound 2, quantum maximum 4)")
    print(f"Standard error: {se:.6f}")
    if se > 0:
        print(f"Standard errors above classical bound 2: {(m - 2) / se:.2f}")
    else:
        print("Standard errors above classical bound 2: n/a (zero statistical error)")
    print(f"Approximate 95% CI: ({m - 1.96 * se:.6f}, {m + 1.96 * se:.6f})")
    return m, se, exp


def find_chains(backend):
    """Return (chains sorted best-first, dict of coupler errors)."""
    target = backend.target
    cz = target["cz"]
    meas = target["measure"]

    def ro(q):
        props = meas.get((q,))
        return (props.error or 0.0) if props else 0.0

    err = {}
    for (a, b), props in cz.items():
        key = tuple(sorted((a, b)))
        e = props.error if props and props.error is not None else 1.0
        err[key] = min(e, err.get(key, 1.0))

    nbrs = {}
    for a, b in err:
        nbrs.setdefault(a, []).append(b)
        nbrs.setdefault(b, []).append(a)

    chains = []
    for mid, ns in nbrs.items():
        for i in range(len(ns)):
            for j in range(i + 1, len(ns)):
                a, c = ns[i], ns[j]
                e1 = err[tuple(sorted((a, mid)))]
                e2 = err[tuple(sorted((mid, c)))]
                score = e1 + e2 + ro(a) + ro(mid) + ro(c)
                chains.append((score, a, mid, c, e1, e2))
    return sorted(chains), err


def compile_circuits(backend, layout):
    from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

    pm = generate_preset_pass_manager(
        backend=backend, optimization_level=3, initial_layout=layout
    )
    return pm.run(build_circuits())


def run_sim():
    from qiskit import transpile
    from qiskit_aer import AerSimulator

    sim = AerSimulator()
    circs = transpile(build_circuits(), sim)
    result = sim.run(circs, shots=SHOTS).result()
    report([result.get_counts(i) for i in range(len(circs))])


def run_chains(backend_name):
    from qiskit_ibm_runtime import QiskitRuntimeService

    backend = QiskitRuntimeService().backend(backend_name)
    chains, _ = find_chains(backend)
    print(f"Best 3-qubit chains on {backend_name} (A, middle B, C; lower score is better):")
    for score, a, mid, c, e1, e2 in chains[:8]:
        print(f"  chain {a},{mid},{c}  cz_errors={e1:.4f}/{e2:.4f}  score={score:.4f}")


def run_submit(backend_name, a, b, c):
    from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2

    backend = QiskitRuntimeService().backend(backend_name)
    _, err = find_chains(backend)
    if tuple(sorted((a, b))) not in err or tuple(sorted((b, c))) not in err:
        print(f"Qubits {a},{b},{c} are not a connected chain (B must touch A and C). Nothing submitted.")
        return

    isa = compile_circuits(backend, [a, b, c])
    for circ in isa:
        print(f"{circ.name}: depth={circ.depth()} ops={dict(circ.count_ops())}")

    print(
        f"\nReady to submit 4 circuits x {SHOTS} shots to {backend_name} "
        f"on qubits {a},{b},{c} (about 3-4 s of QPU time)."
    )
    if input("Type YES to submit, anything else cancels: ").strip() != "YES":
        print("Cancelled. Nothing was submitted.")
        return

    job = SamplerV2(mode=backend).run(isa, shots=SHOTS)
    print("Job ID:", job.job_id(), "(save this)")
    result = job.result()
    all_counts = [pub.data.c.get_counts() for pub in result]
    m, se, exp = report(all_counts)

    out = {
        "job_id": job.job_id(),
        "backend": backend_name,
        "qubits": [a, b, c],
        "shots_per_setting": SHOTS,
        "counts": dict(zip(SETTINGS, all_counts)),
        "mermin_M": m,
        "standard_error": se,
    }
    fname = f"mermin_{backend_name}_q{a}-q{b}-q{c}_{time.strftime('%Y%m%d-%H%M%S')}.json"
    with open(fname, "w") as f:
        json.dump(out, f, indent=2)
    print("Saved:", fname)


def main(argv):
    if len(argv) >= 2 and argv[1] == "sim":
        run_sim()
    elif len(argv) == 3 and argv[1] == "chains":
        run_chains(argv[2])
    elif len(argv) == 6 and argv[1] == "submit":
        run_submit(argv[2], int(argv[3]), int(argv[4]), int(argv[5]))
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv)
