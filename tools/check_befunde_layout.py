from __future__ import annotations

import re
from pathlib import Path

from befunde_paths import befunde_root

from befunde_paths import befund_relative_path


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = befunde_root(ROOT)
MAX_DIRECTORY_ENTRIES = 999
FLAT_REFERENCE = re.compile(
    r"docs/befunde/\d[^/\s)`'\"]*\.(?:csv|json|md|txt|wav)(?=[\s)`'\"#]|$)"
)
MARKDOWN_LINK = re.compile(r"\]\((?P<target>[^)\s]+)\)")
IGNORED_PARTS = {".git", ".venv", "__pycache__", "debug"}


def main() -> int:
    errors: list[str] = []
    files = [path for path in BEFUNDE.rglob("*") if path.is_file()]
    links_checked = 0

    for directory in [BEFUNDE, *(path for path in BEFUNDE.rglob("*") if path.is_dir())]:
        entries = sum(1 for _ in directory.iterdir())
        if entries > MAX_DIRECTORY_ENTRIES:
            errors.append(f"zu_viele_eintraege={directory.relative_to(ROOT)} count={entries}")

    for path in files:
        expected = BEFUNDE / befund_relative_path(path.name)
        if path != expected:
            errors.append(
                f"falsch_abgelegt={path.relative_to(ROOT)} expected={expected.relative_to(ROOT)}"
            )

    reference_paths = [path for path in ROOT.iterdir() if path.is_file()]
    for directory_name in ("DIO_BAUPLAN", "docs", "mini_dio", "reports", "tools"):
        directory = ROOT / directory_name
        if directory.is_dir():
            reference_paths.extend(path for path in directory.rglob("*") if path.is_file())

    for path in reference_paths:
        if not path.is_file() or path.suffix.lower() not in {".md", ".py", ".json", ".txt"}:
            continue
        relative_parts = path.relative_to(ROOT).parts
        if any(part in IGNORED_PARTS for part in relative_parts) or relative_parts[:2] == (
            "data",
            "generated",
        ):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if FLAT_REFERENCE.search(text):
            errors.append(f"flacher_befundpfad={path.relative_to(ROOT)}")

    for source in (ROOT / "docs").rglob("*.md"):
        text = source.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(text):
            target = match.group("target").split("#", 1)[0]
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            target_path = Path(target)
            if not re.match(r"^\d", target_path.name):
                continue
            if target_path.suffix.lower() not in {".csv", ".json", ".md"}:
                continue
            links_checked += 1
            if not (source.parent / target_path).is_file():
                errors.append(f"toter_befundlink={source.relative_to(ROOT)} target={target}")

    print(
        f"befunde_checked={len(files)} links_checked={links_checked} "
        f"layout_errors={len(errors)}"
    )
    for error in errors:
        print(f"ERROR {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
