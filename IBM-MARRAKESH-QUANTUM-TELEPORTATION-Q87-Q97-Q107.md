# Quantum Teleportation on IBM Marrakesh

**Experiment date:** October 17, 2026
**Processor:** IBM Marrakesh (156 physical qubits)
**Physical qubits:** 87, 97, 107
**IBM Quantum job ID:** `db9f8apgv2cc73e5dt20`
**Execution status:** DONE
**Shots:** 1,024

## Research Objective

Investigate measurement-based quantum teleportation of the
|+> state using entanglement, Bell-basis measurements,
and classical feed-forward on real IBM quantum hardware.

## Experimental Configuration

- Input state: |+>
- Input qubit: Q87
- Intermediate qubit: Q97
- Receiving qubit: Q107
- Entangling operations: 2 CZ gates after compilation
- Conditional operations: 2
- Compiled circuit depth: 18
- Measurement basis for receiver: X
- Qiskit Runtime primitive: SamplerV2

## Hardware Calibration

| Qubit | T1 (us) | T2 (us) | Readout error |
|---|---:|---:|---:|
| Q87 | 158.57 | 132.86 | 0.708% |
| Q97 | 238.71 | 59.64 | 0.403% |
| Q107 | 185.32 | 188.94 | 0.476% |

Calibration values reflect the measurements retrieved
during experiment preparation.

## Verification

The ideal AerSimulator returned the expected receiving-qubit
measurement in 4,096 of 4,096 shots.

The compiled circuit passed local IBM ISA validation.

The real-hardware experiment completed successfully.

## Hardware Measurement Counts

Qiskit displays the three-bit classical register in the order
c[2] c[1] c[0]. The leftmost bit is the receiver's X-basis
verification measurement.

| Bitstring | Counts |
|---|---:|
| 000 | 237 |
| 001 | 257 |
| 010 | 229 |
| 011 | 212 |
| 100 | 17 |
| 101 | 39 |
| 110 | 12 |
| 111 | 21 |
| **Total** | **1,024** |

## Experimental Result

Expected receiver outcome (c[2] = 0):

935 / 1,024 = **91.30859375%**

Unexpected receiver outcome (c[2] = 1):

89 / 1,024 = **8.69140625%**

Ideal simulator verification success: 100%.

Real-hardware verification success: **91.3086%**.

## Scientific Interpretation

The experiment demonstrates successful execution of a
three-qubit teleportation circuit with mid-circuit
measurements and classical feed-forward on IBM Marrakesh.

The observed result is consistent with successful
reconstruction of the prepared |+> state in the X basis.

The measured 91.3086% is a single-state verification
success rate, not complete quantum teleportation fidelity.

The experiment does not establish arbitrary-state
teleportation fidelity, process fidelity, or a
loophole-free demonstration.

Further experiments using multiple input states and
appropriate controls are required for broader
characterization.

## Reproducibility

IBM Quantum job ID:

`db9f8apgv2cc73e5dt20`

Backend:

`ibm_marrakesh`

Physical qubits:

`87, 97, 107`

Qiskit Runtime:

`SamplerV2`

Shots:

`1024`

No IBM credentials or access tokens are included.
