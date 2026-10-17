# IBM Quantum — CHSH Hardware Experiment

Date: October 16, 2026
Processor: ibm_marrakesh
Physical qubits: 135, 139
Job ID: db9ese7i0auc7390huv0
Execution status: DONE

## Objective

Evaluate the CHSH Bell inequality using entangled qubits
on real IBM superconducting quantum hardware.

## Configuration

Qiskit Runtime: SamplerV2
Shots per setting: 1024
Total shots: 4096
Circuit optimization level: 1
Circuit depth: 8
Two-qubit gates per circuit: 1

Selected physical qubit pair: 135, 139
Reported CZ gate error: 0.1226%

## Hardware Measurements

| Setting | 00 | 11 | 01 | 10 | Correlation |
|---|---:|---:|---:|---:|---:|
| AB | 443 | 431 | 74 | 76 | +0.70703125 |
| AB_prime | 415 | 429 | 87 | 93 | +0.6484375 |
| A_primeB | 439 | 399 | 94 | 92 | +0.63671875 |
| A_primeB_prime | 84 | 63 | 435 | 442 | -0.712890625 |

## CHSH Calculation

S = |E(AB) + E(AB_prime) + E(A_primeB) - E(A_primeB_prime)|

Measured S: 2.705078125
Classical bound: 2.0
Ideal quantum maximum: 2.828427125

Result: CHSH inequality violated.

## Comparison

Earlier hardware experiment:
Physical qubits: 53, 54
CHSH: 2.6484375
Job ID: db8qnmdckpjs73b1ho20

Current hardware experiment:
Physical qubits: 135, 139
CHSH: 2.705078125
Job ID: db9ese7i0auc7390huv0

Observed CHSH difference: +0.056640625

The observed difference alone does not establish statistically
significant superiority of either physical qubit pair.

## Scientific Interpretation

The measured correlations exceed the classical CHSH bound
under the assumptions of the implemented measurement protocol.

This is a quantum-computing demonstration, not a loophole-free
Bell experiment.

## Reproducibility

Bell-state preparation:
H on logical qubit 0, followed by CX(0, 1).

Measurement settings:
AB: A=Z, B=(Z+X)/sqrt(2)
AB_prime: A=Z, B=(Z-X)/sqrt(2)
A_primeB: A=X, B=(Z+X)/sqrt(2)
A_primeB_prime: A=X, B=(Z-X)/sqrt(2)

Circuit compilation:
generate_preset_pass_manager(
    backend=backend,
    optimization_level=1,
    initial_layout=[135, 139]
)

Four circuits were submitted together using SamplerV2.

IBM Quantum job results can be retrieved using the recorded
job ID without submitting another hardware experiment.

No API credentials are stored in this research record.
