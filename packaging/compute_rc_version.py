import subprocess
from pathlib import Path

# TODO: consolidate with the code in build_conda.py
THIS_PATH = Path(__file__).resolve()
code_version = (THIS_PATH.parents[1] / "version.txt").read_text().strip()
num_commits = subprocess.check_output(["git", "rev-list", "--count", "HEAD"], text=True).strip()
# increment patch
last_part = code_version.rindex(".") + 1
code_version = version[:last_part] + str(1 + int(version[last_part:]))

print(f"{code_version}rc{num_commits}", end = "")
