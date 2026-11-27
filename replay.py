"""Replay the exact verification certificates. Run with Python 3.12 and SymPy 1.14."""

from hashlib import sha256
from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent


def run(script, *args):
    result = subprocess.run(
        [sys.executable, "-E", "-B", str(HERE / script), *map(str, args)],
        cwd=HERE, stdout=subprocess.PIPE, text=True, check=True,
    )
    return result.stdout


def require_same(actual, expected, label):
    if actual != expected:
        raise ValueError(f"Replayed output differs from the archived {label}")


def verify_hashes(manifest, folder):
    for record in manifest.read_text(encoding="utf-8").splitlines():
        expected, relative = record.split(maxsplit=1)
        actual = sha256((folder / relative).read_bytes()).hexdigest()
        require_same(actual, expected, relative)


def main():
    verify_hashes(HERE / "verification/FROZEN.sha256", HERE)
    for script in ("switching/check_switching.py", "switching/check_extensions.py",
                   "verification/switching_controls.py", "verification/check_lean_inputs.py"):
        print(run(script).strip(), flush=True)



if __name__ == "__main__":
    main()
