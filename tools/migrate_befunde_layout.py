from __future__ import annotations

import argparse
import hashlib
import os
import re
from pathlib import Path

from befunde_paths import befund_relative_path


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = ROOT / "docs" / "befunde"
PYTHON_ROOT_EXPRESSION = 'ROOT / "docs" / "befunde"'
PYTHON_ROUTED_EXPRESSION = "befunde_root(ROOT)"
PYTHON_IMPORT = "from befunde_paths import befunde_root"
TEXT_EXTENSIONS = {
    ".bat",
    ".csv",
    ".json",
    ".md",
    ".ps1",
    ".py",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}
IGNORED_PARTS = {".git", ".venv", "__pycache__", "debug"}
REPO_PATH = re.compile(r"docs/befunde/(?P<name>\d[A-Za-z0-9_.-]+)")
MARKDOWN_LINK = re.compile(r"(?P<prefix>!?\[[^\]]*\]\()(?P<target>[^)\s]+)(?P<suffix>\))")


def _digest(path: Path) -> str:
    result = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            result.update(chunk)
    return result.hexdigest()


def _inventory() -> dict[str, str]:
    inventory: dict[str, str] = {}
    for path in BEFUNDE.rglob("*"):
        if not path.is_file():
            continue
        if path.name in inventory:
            raise RuntimeError(f"Doppelter Befunddateiname: {path.name}")
        inventory[path.name] = _digest(path)
    return inventory


def _move_findings() -> int:
    moved = 0
    for source in sorted((path for path in BEFUNDE.rglob("*") if path.is_file()), key=str):
        destination = BEFUNDE / befund_relative_path(source.name)
        if source == destination:
            continue
        if BEFUNDE.resolve() not in destination.resolve().parents:
            raise RuntimeError(f"Ziel ausserhalb von docs/befunde: {destination}")
        if destination.exists():
            raise RuntimeError(f"Befundziel existiert bereits: {destination}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        source.replace(destination)
        moved += 1
    return moved


def _add_python_import(text: str, path: Path) -> str:
    if PYTHON_IMPORT in text:
        return text
    marker = "from pathlib import Path"
    if marker not in text:
        raise RuntimeError(f"Kein pathlib-Import fuer Pfadmigration: {path}")
    return text.replace(marker, f"{marker}\n\n{PYTHON_IMPORT}", 1)


def _rewrite_python_roots() -> int:
    changed = 0
    excluded = {Path(__file__).name, "befunde_paths.py"}
    for path in sorted((ROOT / "tools").glob("*.py")):
        if path.name in excluded:
            continue
        text = path.read_text(encoding="utf-8")
        if PYTHON_ROOT_EXPRESSION not in text:
            continue
        updated = text.replace(PYTHON_ROOT_EXPRESSION, PYTHON_ROUTED_EXPRESSION)
        updated = _add_python_import(updated, path)
        path.write_text(updated, encoding="utf-8")
        changed += 1
    return changed


def _markdown_target(source: Path, target: str) -> str:
    fragment = ""
    if "#" in target:
        target, fragment = target.split("#", 1)
        fragment = f"#{fragment}"

    normalized = target.replace("\\", "/")
    if normalized.startswith(("http://", "https://", "mailto:", "#")):
        return f"{target}{fragment}"

    current = (source.parent / normalized).resolve()
    if current.is_file():
        return f"{target}{fragment}"

    target_path = Path(normalized)
    target_name = target_path.name
    if re.match(r"^\d", target_name) and (
        "befunde" in target_path.parts
        or (BEFUNDE in source.parents and len(target_path.parts) == 1)
    ):
        destination = BEFUNDE / befund_relative_path(target_name)
        if destination.is_file():
            relative = os.path.relpath(destination, source.parent).replace("\\", "/")
            return f"{relative}{fragment}"

    if BEFUNDE in source.parents:
        old_destination = (BEFUNDE / normalized).resolve()
        if old_destination.is_file():
            relative = os.path.relpath(old_destination, source.parent).replace("\\", "/")
            return f"{relative}{fragment}"

    if target_path.parts and target_path.parts[0] in {
        "DIO_BAUPLAN",
        "data",
        "docs",
        "reports",
        "tools",
    }:
        root_destination = (ROOT / normalized).resolve()
        if root_destination.is_file():
            relative = os.path.relpath(root_destination, source.parent).replace("\\", "/")
            return f"{relative}{fragment}"

    return f"{target}{fragment}"


def _rewrite_text_references() -> tuple[int, int]:
    changed_files = 0
    changed_paths = 0
    paths = [path for path in ROOT.iterdir() if path.is_file()]
    for directory_name in (
        "DIO_BAUPLAN",
        "data_builder",
        "docs",
        "mini_dio",
        "reports",
        "tests",
        "tools",
    ):
        directory = ROOT / directory_name
        if directory.is_dir():
            paths.extend(path for path in directory.rglob("*") if path.is_file())

    for path in sorted(paths, key=str):
        if not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        relative_parts = path.relative_to(ROOT).parts
        if (
            any(part in IGNORED_PARTS for part in relative_parts)
            or relative_parts[:2] == ("data", "generated")
            or path.name in {Path(__file__).name, "befunde_paths.py"}
        ):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        original = text
        if path.suffix.lower() == ".md":
            text = MARKDOWN_LINK.sub(
                lambda match: (
                    f"{match.group('prefix')}"
                    f"{_markdown_target(path, match.group('target'))}"
                    f"{match.group('suffix')}"
                ),
                text,
            )

        def replace_repo_path(match: re.Match[str]) -> str:
            nonlocal changed_paths
            name = match.group("name")
            if name in {"100-1000", "1001-2000", "2001-3000"}:
                return match.group(0)
            changed_paths += 1
            return f"docs/befunde/{befund_relative_path(name).as_posix()}"

        text = REPO_PATH.sub(replace_repo_path, text)
        if text != original:
            path.write_text(text, encoding="utf-8")
            changed_files += 1
    return changed_files, changed_paths


def main() -> int:
    parser = argparse.ArgumentParser(description="Migriert Befunde in GitHub-taugliche Nummernbereiche.")
    parser.parse_args()

    before = _inventory()
    moved = _move_findings()
    after_move = _inventory()
    if before != after_move:
        raise RuntimeError("Dateibestand oder Befundinhalte haben sich beim Verschieben veraendert.")

    python_files = _rewrite_python_roots()
    reference_files, reference_paths = _rewrite_text_references()
    after = _inventory()

    print(f"befunde={len(after)} moved={moved}")
    print(f"python_files={python_files}")
    print(f"reference_files={reference_files} reference_paths={reference_paths}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
