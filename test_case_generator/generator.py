#!/usr/bin/env python3

import random
import sys
import subprocess


def generate_test_case(n, m, q, filename, max_value=1000000, max_accidents=10):
    """
    Generate a single test case and write to files.

    Args:
        n: Number of highway sections (1 <= n <= 2,000,000)
        m: Number of beautification projects (1 <= m <= 2,000,000)
        q: Number of traffic scenarios (1 <= q <= 20,000)
        filename: Base filename (without extension)
        max_value: Maximum absolute value for scenic value changes
        max_accidents: Maximum number of accidents per scenario (1 <= K <= 10)
    """
    # Generate beautification projects
    projects = []
    for _ in range(m):
        left = random.randint(1, n)
        right = random.randint(left, n)
        v = random.randint(-max_value, max_value)
        projects.append((left, right, v))

    # Generate traffic scenarios
    scenarios = []
    for _ in range(q):
        k = random.randint(1, min(max_accidents, n))
        accidents = sorted(random.sample(range(1, n + 1), k))
        scenarios.append(accidents)

    # Write input file
    with open(f"{filename}.in", "w") as f:
        f.write(f"{n} {m}\n")
        for left, right, v in projects:
            f.write(f"{left} {right} {v}\n")
        f.write(f"{q}\n")
        for accidents in scenarios:
            k = len(accidents)
            f.write(f"{k} " + " ".join(map(str, accidents)) + "\n")

    # Compute answers
    with open(f"{filename}.in", "r") as f:
        input_data = f.read()
    result = subprocess.run(
        ["python", "submissions/accepted/solution.py"],
        capture_output=True,
        text=True,
        input=input_data,
    )
    answers = result.stdout

    # Write answer file
    with open(f"{filename}.ans", "w") as f:
        f.write(answers)


def main():
    # Default parameters
    n = 100
    m = 50
    q = 10
    filename = "test_case_generator/test"

    # Parse command line arguments if provided
    if len(sys.argv) >= 5:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        q = int(sys.argv[3])
        filename = sys.argv[4]
    elif len(sys.argv) >= 4:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        q = int(sys.argv[3])

    # Validate constraints
    assert 1 <= n <= 2000000, "N must be between 1 and 2,000,000"
    assert 1 <= m <= 2000000, "M must be between 1 and 2,000,000"
    assert 1 <= q <= 20000, "Q must be between 1 and 20,000"

    # Set random seed for reproducibility (can be overridden)
    seed = random.randint(0, 10**9) if len(sys.argv) < 6 else int(sys.argv[5])
    random.seed(seed)

    generate_test_case(n, m, q, filename)
    print(f"Generated {filename}.in and {filename}.ans")


if __name__ == "__main__":
    main()
