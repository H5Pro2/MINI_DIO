from __future__ import annotations

import py_compile
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def compile_python_files() -> int:
    files = (
        list((ROOT / "mini_dio").glob("*.py"))
        + list((ROOT / "reports").glob("*.py"))
        + list((ROOT / "tools").glob("*.py"))
    )
    errors: list[tuple[Path, str]] = []
    for path in files:
        try:
            py_compile.compile(str(path), doraise=True)
        except Exception as exc:  # pragma: no cover - diagnostic script
            errors.append((path, repr(exc)))

    print(f"compile_checked={len(files)} compile_errors={len(errors)}")
    for path, error in errors:
        print(f"ERROR {path.relative_to(ROOT)}")
        print(error)
    return len(errors)


def check_runner_help() -> int:
    result = subprocess.run(
        [sys.executable, "-m", "mini_dio.run_mini", "--help"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    print(f"runner_help_exit={result.returncode}")
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
    return 0 if result.returncode == 0 else 1


def main() -> int:
    errors = 0
    errors += compile_python_files()
    errors += check_runner_help()
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
