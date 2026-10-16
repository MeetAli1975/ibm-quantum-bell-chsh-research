import math

measurements = {
    "AB0": {"00": 409, "11": 427, "10": 110, "01": 78},
    "AB1": {"00": 453, "11": 410, "10": 91, "01": 70},
    "A1B0": {"00": 441, "11": 415, "10": 92, "01": 76},
    "A1B1": {"00": 102, "11": 73, "10": 422, "01": 427},
}

expectations = {}

for name, counts in measurements.items():
    shots = sum(counts.values())
    expectation = (
        counts["00"] + counts["11"]
        - counts["01"] - counts["10"]
    ) / shots
    expectations[name] = expectation
    print(f"{name}: {expectation:.6f} ({shots} shots)")

chsh = (
    expectations["AB0"]
    + expectations["AB1"]
    + expectations["A1B0"]
    - expectations["A1B1"]
)

standard_error = math.sqrt(
    sum((1 - value**2) / 1024 for value in expectations.values())
)

print(f"\nCHSH: {chsh:.6f}")
print(f"Standard error: {standard_error:.6f}")
print(f"Standard errors above classical bound: {(chsh - 2) / standard_error:.2f}")
print(
    "Approximate 95% confidence interval:",
    f"({chsh - 1.96 * standard_error:.6f}, "
    f"{chsh + 1.96 * standard_error:.6f})"
)
