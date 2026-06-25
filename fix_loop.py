"""
The "make the tests pass" loop — cross-platform Python version.

Same shape as fix_loop.ps1:
    run pytest (deterministic gate) -> green? stop -> else feed failures to Amp.

Usage:  python fix_loop.py
"""
import subprocess
import sys

MAX_STEPS = 6


def run_tests() -> tuple[int, str]:
    p = subprocess.run(
        [sys.executable, "-m", "pytest", "-q"],
        capture_output=True, text=True,
    )
    return p.returncode, p.stdout + p.stderr


def amp_fix(test_output: str) -> None:
    prompt = (
        "The pytest suite in this folder is failing. Output:\n\n"
        f"{test_output}\n\n"
        "Fix the bugs in textstats.py so every test passes. Edit ONLY "
        "textstats.py. Do NOT change test_textstats.py. Make the smallest "
        "correct change per bug."
    )
    subprocess.run(["amp", "-x", prompt, "--dangerously-allow-all"], check=True)


def main() -> int:
    for i in range(1, MAX_STEPS + 1):
        print(f"\n[loop] test pass {i}/{MAX_STEPS}", file=sys.stderr)
        code, out = run_tests()
        print(out)
        if code == 0:
            print(f"[loop] all tests green after {i - 1} fix step(s).", file=sys.stderr)
            return 0
        amp_fix(out)
    print(f"[loop] still failing after {MAX_STEPS} passes.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
