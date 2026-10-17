# Four-State Quantum Teleportation on IBM Marrakesh

**Experiment date:** October 17, 2026

**Processor:** IBM Marrakesh (156 physical qubits)

**Physical qubits:** 87, 97, 107

**IBM Quantum job ID:** `db9fd80c77vs7381c9t0`

**Execution status:** DONE

**Reported QPU usage:** 3 seconds

## Research Objective

Investigate quantum teleportation performance across four
prepared input states using entanglement, mid-circuit
measurements, and classical feed-forward on real IBM hardware.

## Experimental Configuration

- Input qubit: Q87
- Intermediate qubit: Q97
- Receiving qubit: Q107
- Quantum states: |0>, |1>, |+>, |->
- Verification bases: Z and X
- Entangling operations: 2 CZ gates per compiled circuit
- Conditional operations: 2 per circuit
- Circuit depths: 15 (Z states), 18 (X states)
- Qiskit Runtime primitive: SamplerV2
- Circuits: 4
- Shots per circuit: 1,024
- Total shots: 4,096

All four circuits passed local IBM ISA validation.

Ideal AerSimulator verification succeeded in 4,096
of 4,096 shots for each input state.

## Real-Hardware Measurement Counts

Bitstrings are displayed as c[2] c[1] c[0].

The leftmost bit represents the receiving qubit's
verification measurement.

| Bitstring | \|0> | \|1> | \|+> | \|-> |
|---|---:|---:|---:|---:|
| 000 | 251 | 26 | 270 | 24 |
| 001 | 252 | 19 | 229 | 18 |
| 010 | 211 | 15 | 249 | 14 |
| 011 | 241 | 15 | 232 | 12 |
| 100 | 17 | 219 | 16 | 257 |
| 101 | 21 | 242 | 7 | 232 |
| 110 | 13 | 260 | 9 | 237 |
| 111 | 18 | 228 | 12 | 230 |
| **Total** | **1024** | **1024** | **1024** | **1024** |

## Verification Results

| State | Expected c[2] | Successful shots | Success rate |
|---|---:|---:|---:|
| \|0> | 0 | 955/1024 | 93.2617% |
| \|1> | 1 | 949/1024 | 92.6758% |
| \|+> | 0 | 980/1024 | 95.7031% |
| \|-> | 1 | 956/1024 | 93.3594% |
| **Combined** | — | **3840/4096** | **93.7500%** |

Z-basis combined verification: 1904/2048 = 92.96875%.

X-basis combined verification: 1936/2048 = 94.53125%.

Observed X-minus-Z difference: 1.5625 percentage points.

## Previous Experiment Comparison

Earlier single-state |+> experiment:

- Job ID: `db9f8apgv2cc73e5dt20`
- Verification: 935/1024 = 91.3086%

Current four-state experiment, |+> component:

- Job ID: `db9fd80c77vs7381c9t0`
- Verification: 980/1024 = 95.7031%

Observed difference: approximately 4.39 percentage points.

This difference does not by itself establish a change in
hardware quality or protocol performance.

## Scientific Interpretation

All four tested input states produced verification
success rates exceeding 92% on IBM Marrakesh.

The results are consistent with successful reconstruction
of the prepared states using a teleportation protocol
with measurement-based classical feed-forward.

The combined 93.75% represents an average single-state
verification success rate across four equally sampled
input states. It is not quantum process fidelity.

These measurements do not constitute full process
tomography or establish arbitrary-state teleportation
fidelity. Additional input states, including Y-basis
states, and appropriate controls would strengthen
the experimental characterization.

Hardware calibration drift, gate errors, measurement
errors, and statistical fluctuations may influence
the observed results.

## Reproducibility

IBM Quantum job ID: `db9fd80c77vs7381c9t0`

Backend: `ibm_marrakesh`

Physical qubits: `87, 97, 107`

Runtime primitive: `SamplerV2`

Shots per circuit: `1024`

State order: `|0>, |1>, |+>, |->`

No IBM credentials or access tokens are included.
