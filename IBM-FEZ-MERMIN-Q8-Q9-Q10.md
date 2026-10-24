# IBM Quantum — Three-Qubit Mermin Inequality Hardware Experiment

**Experiment date:** October 18, 2026, 00:38:48 EDT  
**Backend:** ibm_fez  
**Job ID:** dba4qlvi0auc7391h0t0  
**Status:** DONE

## Objective

Prepare a three-qubit GHZ state on real IBM Quantum hardware and
evaluate the Mermin inequality using four measurement settings.

Compare the experimental Mermin parameter with the classical
local-hidden-variable bound of 2 and the ideal quantum maximum of 4.

## Configuration

- Processor: IBM Fez
- Physical qubits: 8, 9, 10
- Primitive: Qiskit Runtime Sampler
- Measurement settings: XXX, XYY, YXY, YYX
- Shots per setting: 1024
- Total shots: 4096

The circuit prepares the GHZ state using a Hadamard gate followed
by two CNOT gates:

    H(0)
    CX(0, 1)
    CX(1, 2)

X measurements use a Hadamard basis rotation.
Y measurements use S-dagger followed by Hadamard.

The original implementation is preserved in `mermin_run.py`.

## Hardware Measurements

| Observable | Expectation | Ideal | Shots |
|------------|------------:|------:|------:|
| XXX | +0.900391 | +1 | 1024 |
| XYY | -0.894531 | -1 | 1024 |
| YXY | -0.867188 | -1 | 1024 |
| YYX | -0.892578 | -1 | 1024 |

The complete measured bitstring counts are preserved in:

`mermin_ibm_fez_q8-q9-q10_recovered.json`

The data was recovered from the completed IBM Quantum job and
independently reprocessed using the original experiment code.

## Mermin Calculation

The Mermin parameter is defined as:

    M = <XXX> - <XYY> - <YXY> - <YYX>

Experimental result:

    M = 3.554688

Statistical standard error:

    SE = 0.028648

Standard errors above the classical bound:

    (M - 2) / SE = 54.27

Approximate 95% confidence interval:

    [3.498538, 3.610837]

Reference bounds:

- Local-hidden-variable bound: |M| <= 2
- Ideal quantum GHZ maximum: |M| = 4

The standard error was estimated from independent measurement
samples using:

    SE = sqrt(sum((1 - E_i^2) / N_i))

where E_i is the measured expectation value and N_i is the
number of shots for measurement setting i.

## Comparison

| Reference | Mermin parameter |
|-----------|-----------------:|
| Classical bound | 2 |
| IBM Fez experiment | 3.554688 |
| Ideal quantum GHZ maximum | 4 |

The observed result exceeds the classical bound by 1.554688.

## Scientific Interpretation

The hardware measurements demonstrate a strong violation of the
three-qubit Mermin inequality under the standard experimental
and statistical assumptions.

The result is consistent with nonclassical correlations produced
by a GHZ state.

The reported statistical uncertainty accounts for finite-shot
sampling but not systematic hardware errors.

This experiment is not a loophole-free Bell test. In particular,
the measurement implementation and hardware architecture do not
establish spacelike separation or close all relevant experimental
loopholes.

Consequently, the result should be interpreted as a controlled
quantum-computing demonstration of a Mermin inequality violation,
not as a loophole-free demonstration of Bell nonlocality.

## Reproducibility

Original experimental implementation:

`mermin_run.py`

Recovered hardware measurements:

`mermin_ibm_fez_q8-q9-q10_recovered.json`

IBM Quantum job:

`dba4qlvi0auc7391h0t0`

To reproduce the numerical analysis without submitting a new job,
load the recovered JSON and pass its four measurement-count
dictionaries to the `report()` function in `mermin_run.py`.

The locally recovered data was validated against that function.
The calculation reproduced:

    M = 3.554688
    SE = 0.028648

No additional QPU execution was required during recovery
and validation.

## Research Conclusion

A three-qubit GHZ experiment was successfully executed on IBM Fez
using physical qubits 8, 9, and 10.

The measured Mermin parameter of 3.554688 exceeds the classical
bound of 2 and approaches the ideal quantum maximum of 4.

The original hardware measurements have been recovered, preserved,
and validated independently of the IBM Quantum execution service.
