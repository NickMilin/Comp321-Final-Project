import subprocess
import glob
import os

# Path to compiled Java class
JAVA_CLASS = "submissions/accepted/solution"  # do not include .class

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

    # Run the Java solution
    try:
        result = subprocess.run(
            ["java", "-cp", "submissions/accepted", JAVA_CLASS],
            stdin=open(infile, "r"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=120  # longer timeout for Java
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
