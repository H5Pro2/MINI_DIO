from __future__ import annotations

import csv
import sys
from pathlib import Path

from befunde_paths import befunde_root
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.report_mcm_hoerbarer_shift_rawworld_loupe import _resolve_world
from tools.report_mcm_hoerbarer_shift_symbol_coupling import EPISODE_MAP, _basename, _float


BRIDGE_INPUT = befunde_root(ROOT) / "1358_HOERBARER_SCHMALER_SHIFT_ERWEITERTE_ROLLELESUNG.csv"
CANDIDATE_INPUT = befunde_root(ROOT) / "1349_HOERBARER_SCHMALER_SHIFT_MULTI_HOLDOUT.csv"
OUT_CSV = befunde_root(ROOT) / "1361_BRUECKE_NEGATIVKONTROLLE_AUSWAHL.csv"
OUT_MD = befunde_root(ROOT) / "1361_BRUECKE_NEGATIVKONTROLLE_AUSWAHL.md"


def _read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _source_basename(world: str) -> str | None:
    path = _resolve_world(world)
    if path is None:
        return None
    return _basename(str(path))


def _has_episode_mapping(world: str) -> bool:
    basename = _source_basename(world)
    return bool(basename and basename in EPISODE_MAP)


def build_report(limit: int = 20) -> None:
    bridge_rows = [
        row
        for row in _read(BRIDGE_INPUT)
        if row.get("phase_role") == "brueckenuebergang_zum_lauten_kontakt"
    ]
    if not bridge_rows:
        raise RuntimeError("no bridge rows")

    bridge_hearing = mean(_float(row.get("during_hoeren")) for row in bridge_rows)
    bridge_pressure = mean(_float(row.get("during_druck")) for row in bridge_rows)
    bridge_range = mean(_float(row.get("during_range")) for row in bridge_rows)

    selected: list[dict[str, str]] = []
    candidates = []
    for row in _read(CANDIDATE_INPUT):
        sequence = row.get("base_sequence", "")
        if sequence.endswith("->lauter_feldkontakt"):
            continue
        if not _has_episode_mapping(row.get("world", "")):
            continue
        hearing = _float(row.get("avg_auditory"))
        pressure = _float(row.get("avg_field_pressure"))
        range_pct = _float(row.get("avg_range_pct"))
        distance = (
            abs(hearing - bridge_hearing)
            + (abs(pressure - bridge_pressure) * 4.0)
            + (abs(range_pct - bridge_range) * 0.35)
        )
        out = dict(row)
        out["bridge_similarity_distance"] = f"{distance:.6f}"
        out["bridge_reference_hearing"] = f"{bridge_hearing:.6f}"
        out["bridge_reference_pressure"] = f"{bridge_pressure:.6f}"
        out["bridge_reference_range"] = f"{bridge_range:.6f}"
        candidates.append(out)

    candidates.sort(key=lambda row: (_float(row["bridge_similarity_distance"]), -_float(row.get("score"))))
    seen: set[tuple[str, str, str, str]] = set()
    for row in candidates:
        key = (row.get("world", ""), row.get("scale", ""), row.get("block_index", ""), row.get("base_sequence", ""))
        if key in seen:
            continue
        seen.add(key)
        selected.append(row)
        if len(selected) >= limit:
            break

    if not selected:
        raise RuntimeError("no negative controls selected")

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(selected[0].keys()))
        writer.writeheader()
        writer.writerows(selected)

    sequences: dict[str, int] = {}
    assets: dict[str, int] = {}
    for row in selected:
        sequences[row["base_sequence"]] = sequences.get(row["base_sequence"], 0) + 1
        assets[row["asset"]] = assets.get(row["asset"], 0) + 1

    lines = [
        "# 1361 - Brueckenfunktion: Negativkontrolle Auswahl",
        "",
        "## Zweck",
        "",
        "Diese Auswahl sucht Fenster mit aehnlicher Hoer-/Druckstaerke wie die Brueckenfenster aus `1358`, aber ohne Lagefolge `->lauter_feldkontakt`.",
        "Damit wird geprueft, ob die Bruecken-Nachhallfunktion aus der Lagefolge entsteht oder nur aus starker Sinnesaktivierung.",
        "",
        "## Referenz",
        "",
        f"- Brueckenfenster: `{len(bridge_rows)}`",
        f"- Referenz Hoeren: `{bridge_hearing:.6f}`",
        f"- Referenz Druck: `{bridge_pressure:.6f}`",
        f"- Referenz Range: `{bridge_range:.6f}`",
        "",
        "## Auswahl",
        "",
        f"- Kontrollfenster: `{len(selected)}`",
        f"- Assets: {sorted(assets.items())}",
        f"- Lagefolgen: {sorted(sequences.items())}",
        "",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build_report()
