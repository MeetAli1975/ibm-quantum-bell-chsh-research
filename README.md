# IBM Quantum — Bell Entanglement & CHSH Experiment

Date: October 16, 2026
Platform: Apple Silicon macOS
Quantum provider: IBM Quantum
Quantum processor: ibm_marrakesh
Processor family: Heron r2
Processor capacity: 156 physical qubits
Selected physical qubits: 53 and 54

## Research Objective

Prepare an entangled Bell state, characterize its correlations
in complementary measurement bases, and experimentally evaluate
the CHSH Bell inequality on real IBM quantum hardware.

## Software Environment

Python environment: ~/quantum_env
Qiskit: 2.5.0
Qiskit IBM Runtime: 0.47.0
Qiskit Aer: 0.17.2

## IBM Quantum Account

Portal:
https://quantum.cloud.ibm.com/

Instance: open-instance
Account plan: Open Plan trial at experiment time

Authentication:
IBM Quantum API credentials are configured locally through
QiskitRuntimeService.

SECURITY:
Never include IBM API tokens, passwords, or private keys in
research documentation or Git repositories.

## Experiment 1 — Bell State, Z Basis

Job ID: db8qg5heukqs73ar4qdg
Backend: ibm_marrakesh
Shots: 1024

00: 521
11: 489
10: 13
01: 1

Z correlation: 98.6328125%
ZZ expectation: 0.97265625

## Experiment 2 — Bell State, X Basis

Job ID: db8qj29eukqs73ar50pg
Backend: ibm_marrakesh
Shots: 1024

00: 491
11: 506
10: 19
01: 8

X correlation: 97.36328125%
XX expectation: 0.947265625

## Bell-State Fidelity Analysis

Estimated fidelity lower bound: 95.99609375%
Estimated standard error: 0.618 percentage points
Approximate 95% lower confidence bound: 94.784%

These estimates assume consistent state preparation across
measurement settings. Statistical confidence calculations
are approximate.

## Experiment 3 — Four-Setting CHSH

Job ID: db8qnmdckpjs73b1ho20
Backend: ibm_marrakesh
Physical qubits: 53, 54
Shots per setting: 1024
Total shots: 4096

Hardware execution time: 2.674505703 seconds

Measurement settings:

AB0: A=Z, B=(Z+X)/sqrt(2)
AB1: A=Z, B=(Z-X)/sqrt(2)
A1B0: A=X, B=(Z+X)/sqrt(2)
A1B1: A=X, B=(Z-X)/sqrt(2)

Measured outcomes:

AB0:
00=409, 11=427, 10=110, 01=78
Correlation: 0.6328125

AB1:
00=453, 11=410, 10=91, 01=70
Correlation: 0.685546875

A1B0:
00=441, 11=415, 10=92, 01=76
Correlation: 0.671875

A1B1:
00=102, 11=73, 10=422, 01=427
Correlation: -0.658203125

## Final CHSH Results

CHSH = AB0 + AB1 + A1B0 - A1B1

Measured CHSH: 2.6484375
Classical CHSH bound: 2.0
Ideal quantum maximum: 2.828427125

Estimated standard error: 0.046822
Standard errors above classical bound: 13.85

Approximate 95% confidence interval:
2.556666 to 2.740209

## Scientific Interpretation

The measured CHSH value exceeds the classical bound.

The experiment demonstrates a CHSH violation under the
assumptions of the implemented measurement protocol.

This is not a loophole-free Bell test.

The confidence interval accounts approximately for finite-shot
statistical uncertainty, not all hardware systematic errors.

## Reproducibility

Quantum state:

|Phi+> = (|00> + |11>) / sqrt(2)

Preparation:

1. Initialize two qubits in |00>.
2. Apply Hadamard to qubit 0.
3. Apply CX from qubit 0 to qubit 1.
4. Rotate measurement bases for each CHSH setting.
5. Measure both qubits.
6. Repeat 1024 shots per setting.

Circuit compilation:

transpile(
    circuit,
    backend,
    initial_layout=[53,54],
    optimization_level=3
)

Each CHSH circuit compiled with:
- Depth: 8
- CZ gates: 1
- Measurements: 2

Execution:
Qiskit Runtime SamplerV2

Four circuits submitted in one hardware job.

## Operational Notes

IBM Quantum execution time is distinct from local terminal
execution time and queue waiting time.

Existing completed jobs can be retrieved without submitting
new hardware experiments.

Hardware calibration and queue conditions may change over time.

## Additional Historical Hardware Jobs

Earlier completed experiments were also performed on
ibm_fez and ibm_kingston.

Their recorded job IDs:

db3i5hcvf2bc73ct7bng
db3iefo4qg6s73c0qdh0

These jobs are separate from the October 16 CHSH experiment.

## Research Conclusion

Four-setting CHSH measurements were successfully completed
on IBM Marrakesh using physical qubits 53 and 54.

Measured CHSH: 2.6484375

The result provides strong experimental evidence of quantum
correlations exceeding the classical CHSH bound.

All primary IBM job IDs and measurement counts are preserved
for subsequent verification.
