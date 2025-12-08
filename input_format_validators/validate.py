#!/usr/bin/env python3

import sys


def validate_input():
    try:
        lines = sys.stdin.read().split("\n")

        # Remove final empty line if input ends with newline
        if lines and lines[-1] == "":
            lines = lines[:-1]

        line_idx = 0

        # First line: N and M
        if line_idx >= len(lines):
            sys.stderr.write("Error: Missing first line with N and M\n")
            return 1

        first_line = lines[line_idx].strip().split()
        if len(first_line) != 2:
            sys.stderr.write(
                "Error: First line must contain exactly 2 integers (N and M)\n"
            )
            return 1

        try:
            N = int(first_line[0])
            M = int(first_line[1])
        except ValueError:
            sys.stderr.write("Error: N and M must be integers\n")
            return 1

        # Validate constraints: 1 <= N <= 2,000,000, 1 <= M <= 2,000,000
        if not (1 <= N <= 2000000):
            sys.stderr.write(f"Error: N must be between 1 and 2,000,000, got {N}\n")
            return 1
        if not (1 <= M <= 2000000):
            sys.stderr.write(f"Error: M must be between 1 and 2,000,000, got {M}\n")
            return 1

        line_idx += 1

        # Next M lines: beautification projects (L, R, V)
        for i in range(M):
            if line_idx >= len(lines):
                sys.stderr.write(
                    f"Error: Missing beautification project line {i + 1}\n"
                )
                return 1

            project_line = lines[line_idx].strip().split()
            if len(project_line) != 3:
                sys.stderr.write(
                    f"Error: Beautification project line {i + 1} must contain exactly 3 integers (L, R, V)\n"
                )
                return 1

            try:
                L = int(project_line[0])
                R = int(project_line[1])
                V = int(project_line[2])
            except ValueError:
                sys.stderr.write(
                    f"Error: Beautification project line {i + 1} must contain integers\n"
                )
                return 1

            # Validate constraints: 1 <= L <= R <= N
            if not (1 <= L <= N):
                sys.stderr.write(f"Error: L must be between 1 and {N}, got {L}\n")
                return 1
            if not (1 <= R <= N):
                sys.stderr.write(f"Error: R must be between 1 and {N}, got {R}\n")
                return 1
            if L > R:
                sys.stderr.write(f"Error: L must be <= R, got L={L}, R={R}\n")
                return 1

            # Validate constraint: -1,000,000 <= V <= 1,000,000
            if not (-1000000 <= V <= 1000000):
                sys.stderr.write(f"Error: V must be between -1,000,000 and 1,000,000, got {V}\n")
                return 1

            line_idx += 1

        # Next line: Q (number of scenarios)
        if line_idx >= len(lines):
            sys.stderr.write("Error: Missing line with Q (number of scenarios)\n")
            return 1

        q_line = lines[line_idx].strip().split()
        if len(q_line) != 1:
            sys.stderr.write("Error: Q line must contain exactly 1 integer\n")
            return 1

        try:
            Q = int(q_line[0])
        except ValueError:
            sys.stderr.write("Error: Q must be an integer\n")
            return 1

        # Validate constraint: 1 <= Q <= 20,000
        if not (1 <= Q <= 20000):
            sys.stderr.write(f"Error: Q must be between 1 and 20,000, got {Q}\n")
            return 1

        line_idx += 1

        # Next Q lines: traffic scenarios
        for i in range(Q):
            if line_idx >= len(lines):
                sys.stderr.write(f"Error: Missing traffic scenario line {i + 1}\n")
                return 1

            scenario_line = lines[line_idx].strip()

            if scenario_line == "":
                sys.stderr.write(
                    f"Error: Scenario {i + 1} line cannot be empty (must have K and accident locations)\n"
                )
                return 1

            parts = scenario_line.split()

            # First integer should be K
            if len(parts) < 1:
                sys.stderr.write(
                    f"Error: Scenario {i + 1} must contain K (number of accidents)\n"
                )
                return 1

            try:
                K = int(parts[0])
            except ValueError:
                sys.stderr.write(
                    f"Error: Scenario {i + 1} K must be an integer\n"
                )
                return 1

            # Validate constraint: 1 <= K <= 10
            if not (1 <= K <= 10):
                sys.stderr.write(
                    f"Error: K must be between 1 and 10, got {K}\n"
                )
                return 1

            # Check that we have exactly K accident locations after K
            if len(parts) != K + 1:
                sys.stderr.write(
                    f"Error: Scenario {i + 1} declares K={K} but has {len(parts) - 1} accident locations\n"
                )
                return 1

            accidents = parts[1:]
            accident_set = set()
            for j, accident_str in enumerate(accidents):
                try:
                    a = int(accident_str)
                except ValueError:
                    sys.stderr.write(
                        f"Error: Scenario {i + 1} contains non-integer accident location\n"
                    )
                    return 1

                # Validate constraint: 1 <= a_i <= N
                if not (1 <= a <= N):
                    sys.stderr.write(
                        f"Error: Accident location must be between 1 and {N}, got {a}\n"
                    )
                    return 1

                # Check for duplicate accidents (problem says "K distinct integers")
                if a in accident_set:
                    sys.stderr.write(
                        f"Error: Scenario {i + 1} contains duplicate accident at location {a}\n"
                    )
                    return 1
                accident_set.add(a)

            line_idx += 1

        # Check for extra lines
        if line_idx < len(lines):
            # Allow trailing empty lines
            remaining = lines[line_idx:]
            for line in remaining:
                if line.strip() != "":
                    sys.stderr.write(
                        "Error: Extra non-empty lines found after expected input\n"
                    )
                    return 1

        # All validations passed
        return 42

    except Exception as e:
        sys.stderr.write(f"Error: Unexpected exception during validation: {e}\n")
        return 1


if __name__ == "__main__":
    exit_code = validate_input()
    sys.exit(exit_code)
