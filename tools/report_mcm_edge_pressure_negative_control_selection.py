from __future__ import annotations

import csv
import sys
from pathlib import Path

from befunde_paths import befunde_root
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.report_mcm_hoerbarer_shift_symbol_coupling import _float


ROLE_INPUT = befunde_root(ROOT) / "1358_HOERBARER_SCHMALER_SHIFT_ERWEITERTE_ROLLELESUNG.csv"
RAW_INPUT = befunde_root(ROOT) / "1357_HOERBARER_SCHMALER_SHIFT_ERWEITERTE_ROHWELTLUPE.csv"
OUT_CSV = befunde_root(ROOT) / "1373_RANDDRUCK_NEGATIVKONTROLLE_AUSWAHL.csv"
OUT_MD = befunde_root(ROOT) / "1373_RANDDRUCK_NEGATIVKONTROLLE_AUSWAHL.md"


def _read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _control_type(row: dict[str, str]) -> str | None:
    sequence = row.get("base_sequence", "")
    raw_class = row.get("during_raw_class", "")
    is_edge = sequence == "lauter_feldkontakt->lauter_feldkontakt" and raw_class == "laute_oder_druckvolle_rohwelt"
    if is_edge:
        return None
    if sequence == "lauter_feldkontakt->lauter_feldkontakt":
        return "same_loud_contact_not_raw_loud"
    if raw_class == "laute_oder_druckvolle_rohwelt":
        return "same_raw_loud_not_loud_contact_loop"
    return None


def build_report() -> None:
    edge_rows = [row for row in _read(ROLE_INPUT) if row.get("phase_role") == "randnaher_kontaktdruck"]
    if not edge_rows:
        raise RuntimeError("no edge pressure rows")

    ref_hearing = mean(_float(row.get("during_hoeren")) for row in edge_rows)
    ref_pressure = mean(_float(row.get("during_druck")) for row in edge_rows)
    ref_range = mean(_float(row.get("during_range")) for row in edge_rows)

    selected: list[dict[str, str]] = []
    for row in _read(RAW_INPUT):
        control_type = _control_type(row)
        if control_type is None:
            continue
        hearing = _float(row.get("during_hoeren"))
        pressure = _float(row.get("during_druck"))
        range_pct = _float(row.get("during_range"))
        distance = (
            abs(hearing - ref_hearing)
            + (abs(pressure - ref_pressure) * 4.0)
            + (abs(range_pct - ref_range) * 0.35)
        )
        out = dict(row)
        out["edge_control_type"] = control_type
        out["edge_similarity_distance"] = f"{distance:.6f}"
        out["edge_reference_hearing"] = f"{ref_hearing:.6f}"
        out["edge_reference_pressure"] = f"{ref_pressure:.6f}"
        out["edge_reference_range"] = f"{ref_range:.6f}"
        selected.append(out)

    selected.sort(key=lambda row: _float(row["edge_similarity_distance"]))
    if not selected:
        raise RuntimeError("no edge pressure negative controls selected")

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(selected[0].keys()))
        writer.writeheader()
        writer.writerows(selected)

    counts: dict[str, int] = {}
    sequences: dict[str, int] = {}
    raw_classes: dict[str, int] = {}
    for row in selected:
        counts[row["edge_control_type"]] = counts.get(row["edge_control_type"], 0) + 1
        sequences[row["base_sequence"]] = sequences.get(row["base_sequence"], 0) + 1
        raw_classes[row["during_raw_class"]] = raw_classes.get(row["during_raw_class"], 0) + 1

    lines = [
        "# 1373 - Randdruck: Negativkontrolle Auswahl",
        "",
        "## Zweck",
        "",
        "Diese Auswahl prueft randnahen Kontaktdruck gegen zwei Gegenproben:",
        "",
        "- gleicher fortgesetzter lauter Kontakt, aber ohne laute/druckvolle Rohweltklasse",
        "- gleiche laute/druckvolle Rohweltklasse, aber ohne fortgesetzten lauten Kontakt",
        "",
        "Damit wird geprueft, ob Randdruck aus der vollen Kopplung `lauter_feldkontakt->lauter_feldkontakt` plus `laute_oder_druckvolle_rohwelt` entsteht.",
        "",
        "## Referenz",
        "",
        f"- Randdruckfenster: `{len(edge_rows)}`",
        f"- Referenz Hoeren: `{ref_hearing:.6f}`",
        f"- Referenz Druck: `{ref_pressure:.6f}`",
        f"- Referenz Range: `{ref_range:.6f}`",
        "",
        "## Auswahl",
        "",
        f"- Kontrollfenster: `{len(selected)}`",
        f"- Kontrolltypen: {sorted(counts.items())}",
        f"- Lagefolgen: {sorted(sequences.items())}",
        f"- Rohweltklassen: {sorted(raw_classes.items())}",
        "",
        "## Wie es weitergeht",
        "",
        "Als naechstes wird diese Auswahl durch Rollen- und Nachhallpipeline gelesen.",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build_report()
