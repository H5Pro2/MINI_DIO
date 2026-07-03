from __future__ import annotations

import csv
import sys
from pathlib import Path
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.report_mcm_hoerbarer_shift_rawworld_loupe import _resolve_world
from tools.report_mcm_hoerbarer_shift_symbol_coupling import EPISODE_MAP, _basename, _float


CENTER_INPUT = ROOT / "docs" / "befunde" / "1358_HOERBARER_SCHMALER_SHIFT_ERWEITERTE_ROLLELESUNG.csv"
CANDIDATE_INPUT = ROOT / "docs" / "befunde" / "1349_HOERBARER_SCHMALER_SHIFT_MULTI_HOLDOUT.csv"
OUT_CSV = ROOT / "docs" / "befunde" / "1367_ZENTRUM_NEGATIVKONTROLLE_AUSWAHL.csv"
OUT_MD = ROOT / "docs" / "befunde" / "1367_ZENTRUM_NEGATIVKONTROLLE_AUSWAHL.md"


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


def _control_type(sequence: str) -> str | None:
    if sequence == "ruhig_zentrumsnah->lauter_feldkontakt":
        return None
    if sequence.endswith("->lauter_feldkontakt"):
        return "same_target_not_center_origin"
    if sequence.startswith("ruhig_zentrumsnah->"):
        return "same_origin_not_loud_contact"
    return None


def build_report(per_type: int = 12) -> None:
    center_rows = [
        row
        for row in _read(CENTER_INPUT)
        if row.get("phase_role") in {"zentrumskontakt_mit_hoeranstieg", "zentrumskontakt_wird_aktiviert"}
    ]
    if not center_rows:
        raise RuntimeError("no center rows")

    ref_hearing = mean(_float(row.get("during_hoeren")) for row in center_rows)
    ref_pressure = mean(_float(row.get("during_druck")) for row in center_rows)
    ref_range = mean(_float(row.get("during_range")) for row in center_rows)

    candidates_by_type: dict[str, list[dict[str, str]]] = {
        "same_target_not_center_origin": [],
        "same_origin_not_loud_contact": [],
    }

    for row in _read(CANDIDATE_INPUT):
        sequence = row.get("base_sequence", "")
        control_type = _control_type(sequence)
        if control_type is None:
            continue
        if not _has_episode_mapping(row.get("world", "")):
            continue

        hearing = _float(row.get("avg_auditory"))
        pressure = _float(row.get("avg_field_pressure"))
        range_pct = _float(row.get("avg_range_pct"))
        distance = (
            abs(hearing - ref_hearing)
            + (abs(pressure - ref_pressure) * 4.0)
            + (abs(range_pct - ref_range) * 0.35)
        )
        out = dict(row)
        out["center_control_type"] = control_type
        out["center_similarity_distance"] = f"{distance:.6f}"
        out["center_reference_hearing"] = f"{ref_hearing:.6f}"
        out["center_reference_pressure"] = f"{ref_pressure:.6f}"
        out["center_reference_range"] = f"{ref_range:.6f}"
        candidates_by_type[control_type].append(out)

    selected: list[dict[str, str]] = []
    for control_type, candidates in candidates_by_type.items():
        candidates.sort(key=lambda row: (_float(row["center_similarity_distance"]), -_float(row.get("score"))))
        seen: set[tuple[str, str, str, str]] = set()
        for row in candidates:
            key = (row.get("world", ""), row.get("scale", ""), row.get("block_index", ""), row.get("base_sequence", ""))
            if key in seen:
                continue
            seen.add(key)
            selected.append(row)
            if len(seen) >= per_type:
                break

    if not selected:
        raise RuntimeError("no center negative controls selected")

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(selected[0].keys()))
        writer.writeheader()
        writer.writerows(selected)

    counts: dict[str, int] = {}
    sequences: dict[str, int] = {}
    for row in selected:
        counts[row["center_control_type"]] = counts.get(row["center_control_type"], 0) + 1
        sequences[row["base_sequence"]] = sequences.get(row["base_sequence"], 0) + 1

    lines = [
        "# 1367 - Zentrumskontakt: Negativkontrolle Auswahl",
        "",
        "## Zweck",
        "",
        "Diese Auswahl prueft den Zentrumskontakt gegen zwei Gegenproben:",
        "",
        "- gleicher Zielkontakt `->lauter_feldkontakt`, aber ohne zentrumsnahen Ausgang",
        "- gleicher zentrumsnaher Ausgang, aber ohne Zielkontakt `->lauter_feldkontakt`",
        "",
        "Damit wird geprueft, ob der Zentrumskontakt aus der vollen Lagefolge `ruhig_zentrumsnah->lauter_feldkontakt` entsteht.",
        "",
        "## Referenz",
        "",
        f"- Zentrumfenster: `{len(center_rows)}`",
        f"- Referenz Hoeren: `{ref_hearing:.6f}`",
        f"- Referenz Druck: `{ref_pressure:.6f}`",
        f"- Referenz Range: `{ref_range:.6f}`",
        "",
        "## Auswahl",
        "",
        f"- Kontrollfenster: `{len(selected)}`",
        f"- Kontrolltypen: {sorted(counts.items())}",
        f"- Lagefolgen: {sorted(sequences.items())}",
        "",
        "## Wie es weitergeht",
        "",
        "Als naechstes wird diese Auswahl durch Rohwelt-, Rollen- und Nachhallpipeline gelesen.",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build_report()
