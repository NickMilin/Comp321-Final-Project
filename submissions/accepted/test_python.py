import subprocess
import glob
import os

# Path to your Python solution
PYTHON_SOL = "submissions/accepted/solution.py"

# Path to secret test cases
SECRET_DIR = "data/secret"

# Find all secret .in files
input_files = sorted(glob.glob(os.path.join(SECRET_DIR, "secret*.in")))

all_passed = True

for infile in input_files:
    ansfile = infile.replace(".in", ".ans")
    if not os.path.exists(ansfile):
        print(f"Skipping {infile}: no .ans file found")
        continue

    # Run the Python solution
    try:
        result = subprocess.run(
            ["python3", PYTHON_SOL],
            stdin=open(infile, "r"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=60
        )
    except subprocess.TimeoutExpired:
        print(f"{infile}: Timeout!")
        all_passed = False
        continue

    expected = open(ansfile).read().strip()
    actual = result.stdout.strip()

    if actual == expected:
        print(f"{infile}: ✅ Passed")
    else:
        print(f"{infile}: ❌ Failed")
        print(f"Expected:\n{expected[:200]}{'...' if len(expected) > 200 else ''}")
        print(f"Got:\n{actual[:200]}{'...' if len(actual) > 200 else ''}")
        all_passed = False

if all_passed:
    print("\nAll secret test cases passed!")
else:
    print("\nSome secret test cases failed.")
