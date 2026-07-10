from __future__ import annotations

import csv
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools import run_mcm_neighborhood_offline_consolidation as runner


PREFIX = "2083_EXAKTE_DELTA_KONSOLIDIERUNG_MCM_NACHBARSCHAFT"
FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
VERBOSE_PREFIX = "2082_PASSIVE_OFFLINE_KONSOLIDIERUNG_MCM_NACHBARSCHAFT"


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def _history_digest(rows: list[dict[str, str]]) -> str:
    fields = list(rows[0])
    payload = "\n".join(
        "|".join(str(row.get(field, "")) for field in fields) for row in rows
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _compare_reconstruction() -> list[dict[str, object]]:
    compact_path = FINDING_DIR / f"{PREFIX}.histories.csv"
    verbose_path = FINDING_DIR / f"{VERBOSE_PREFIX}.histories.csv"
    compact = _read_csv(compact_path)
    verbose = _read_csv(verbose_path)
    rows = []
    for sequence in ("forward", "reverse"):
        compact_sequence = [row for row in compact if row["sequence"] == sequence]
        verbose_sequence = [row for row in verbose if row["sequence"] == sequence]
        compact_digest = _history_digest(compact_sequence)
        verbose_digest = _history_digest(verbose_sequence)
        rows.append(
            {
                "sequence": sequence,
                "compact_reconstructed_entries": len(compact_sequence),
                "2082_verbose_entries": len(verbose_sequence),
                "compact_reconstructed_sha256": compact_digest,
                "2082_verbose_sha256": verbose_digest,
                "exact_reconstruction": int(
                    compact_sequence == verbose_sequence
                    and compact_digest == verbose_digest
                ),
            }
        )
    compact_path.unlink()
    return rows


def _enrich_summary() -> None:
    compact_path = FINDING_DIR / f"{PREFIX}.summary.csv"
    verbose_path = FINDING_DIR / f"{VERBOSE_PREFIX}.summary.csv"
    compact = _read_csv(compact_path)
    verbose = {row["sequence"]: row for row in _read_csv(verbose_path)}
    rows = []
    for row in compact:
        sequence = row["sequence"]
        compact_size = int(row["memory_size_bytes"])
        verbose_size = int(verbose[sequence]["memory_size_bytes"])
        baseline = int(row["2081_baseline_memory_size_bytes"])
        compact_overhead = compact_size - baseline
        verbose_overhead = verbose_size - baseline
        row.update(
            {
                "2082_verbose_memory_size_bytes": verbose_size,
                "saved_vs_2082_bytes": verbose_size - compact_size,
                "saved_vs_2082_percent": ((verbose_size - compact_size) / verbose_size)
                * 100.0,
                "removed_2082_overhead_percent": (
                    (verbose_overhead - compact_overhead) / max(1, verbose_overhead)
                )
                * 100.0,
            }
        )
        rows.append(row)
    _write_csv(compact_path, rows)


def main() -> int:
    runner.RUN_ID = "2083"
    runner.GENERATED_DIR = ROOT / "data" / "generated" / "2083_mcm_neighborhood_delta"
    runner.DEBUG_ROOT = ROOT / "debug" / "2083_mcm_neighborhood_delta"
    runner.PREFIX = PREFIX
    result = runner.main()
    reconstruction = _compare_reconstruction()
    _write_csv(FINDING_DIR / f"{PREFIX}.reconstruction.csv", reconstruction)
    _enrich_summary()
    if not all(int(row["exact_reconstruction"]) == 1 for row in reconstruction):
        raise RuntimeError("compact histories do not reconstruct the 2082 histories exactly")
    print(f"reconstruction_rows={len(reconstruction)}")
    return result


if __name__ == "__main__":
    raise SystemExit(main())
