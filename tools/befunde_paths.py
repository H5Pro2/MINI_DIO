from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Iterator


_NUMBER = re.compile(r"^(\d+)")
_RANGES = (
    (100, 500, ("100-1000", "100-500")),
    (501, 1000, ("100-1000", "501-1000")),
    (1001, 1500, ("1001-2000", "1001-1500")),
    (1501, 1750, ("1001-2000", "1501-1750")),
    (1751, 2000, ("1001-2000", "1751-2000")),
    (2001, 3000, ("2001-3000",)),
)


def befund_relative_path(name: str | os.PathLike[str]) -> Path:
    """Return the stable repository-relative location for a finding file."""
    path = Path(name)
    if len(path.parts) != 1:
        return path

    match = _NUMBER.match(path.name)
    if match is None:
        return path

    number = int(match.group(1))
    for lower, upper, parts in _RANGES:
        if lower <= number <= upper:
            return Path(*parts, path.name)
    raise ValueError(f"Befundnummer ausserhalb der Ablagestruktur: {path.name}")


def befund_path(repo_root: str | os.PathLike[str], name: str | os.PathLike[str]) -> Path:
    return Path(repo_root) / "docs" / "befunde" / befund_relative_path(name)


class BefundeRoot(os.PathLike[str]):
    """Path-compatible root that routes numbered findings into their range."""

    def __init__(self, repo_root: str | os.PathLike[str]) -> None:
        self.path = Path(repo_root) / "docs" / "befunde"

    def __fspath__(self) -> str:
        return os.fspath(self.path)

    def __str__(self) -> str:
        return str(self.path)

    def __truediv__(self, name: str | os.PathLike[str]) -> Path:
        return self.path / befund_relative_path(name)

    def glob(self, pattern: str) -> Iterator[Path]:
        # Historical tools searched the former flat directory with glob().
        return self.path.rglob(pattern)

    def rglob(self, pattern: str) -> Iterator[Path]:
        return self.path.rglob(pattern)

    def __getattr__(self, name: str) -> object:
        return getattr(self.path, name)


def befunde_root(repo_root: str | os.PathLike[str]) -> BefundeRoot:
    return BefundeRoot(repo_root)
