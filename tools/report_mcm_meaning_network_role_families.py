from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
IN_CSV = ROOT / "docs" / "befunde" / "1393_BEDEUTUNGSNETZ_ROHWELT_RUECKLESUNG.csv"
OUT_CSV = ROOT / "docs" / "befunde" / "1394_BEDEUTUNGSNETZ_FELDROLLEN_FAMILIEN.csv"
OUT_MD = ROOT / "docs" / "befunde" / "1394_BEDEUTUNGSNETZ_FELDROLLEN_FAMILIEN.md"


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def _avg(rows: list[dict[str, str]], key: str) -> float:
    values: list[float] = []
    for row in rows:
        try:
            values.append(float(row.get(key, "0") or 0.0))
        except ValueError:
            values.append(0.0)
    return mean(values) if values else 0.0


def _role_family(rows: list[dict[str, str]]) -> str:
    tensions = Counter(row["world_tension_class"] for row in rows)
    directions = Counter(row["raw_direction"] for row in rows)
    follow = Counter(row["follow_state"] for row in rows)
    avg_range = _avg(rows, "raw_range_pct")
    avg_tone_shift = abs(_avg(rows, "hoeren_energy_shift"))
    avg_field_tension = _avg(rows, "mcm_feldwirkung_mcm_tension")

    if follow.get("starker_knoten_taucht_wieder_auf", 0) >= 3 and avg_range >= 4.0:
        return "gerichtete_spannungsrolle"
    if tensions.get("ruhige_feinspannung", 0) >= max(1, len(rows) * 0.70) and avg_field_tension <= 0.02:
        return "ruhige_feldnaehe"
    if avg_range >= 4.5:
        return "weite_weltspannungsnaehe"
    if directions.get("steigend", 0) >= max(1, len(rows) * 0.65) and avg_tone_shift <= 0.002:
        return "leise_gerichtete_nahe"
    if follow.get("neue_nachbarschaft_zu_altem_knoten", 0) >= max(1, len(rows) * 0.65):
        return "offene_nachbarschaftsrolle"
    return "gemischte_feldrolle"


def main() -> None:
    rows = _read_rows(IN_CSV)
    by_node: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_node[row["old_node"]].append(row)

    out_rows: list[dict[str, str]] = []
    for node, node_rows in sorted(by_node.items()):
        tensions = Counter(row["world_tension_class"] for row in node_rows)
        directions = Counter(row["raw_direction"] for row in node_rows)
        follow = Counter(row["follow_state"] for row in node_rows)
        worlds = Counter(row["world"] for row in node_rows)
        out_rows.append(
            {
                "old_node": node,
                "old_state": node_rows[0].get("old_state", ""),
                "role_family": _role_family(node_rows),
                "windows": str(len(node_rows)),
                "world_count": str(len(worlds)),
                "avg_raw_range_pct": f"{_avg(node_rows, 'raw_range_pct'):.6f}",
                "avg_raw_net_pct": f"{_avg(node_rows, 'raw_net_pct'):.6f}",
                "avg_hearing_shift": f"{_avg(node_rows, 'hoeren_energy_shift'):.6f}",
                "avg_field_tension": f"{_avg(node_rows, 'mcm_feldwirkung_mcm_tension'):.6f}",
                "tensions": " | ".join(f"{key}:{value}" for key, value in tensions.most_common()),
                "directions": " | ".join(f"{key}:{value}" for key, value in directions.most_common()),
                "follow_states": " | ".join(f"{key}:{value}" for key, value in follow.most_common()),
                "worlds": " | ".join(f"{key}:{value}" for key, value in worlds.most_common()),
            }
        )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    family_counts = Counter(row["role_family"] for row in out_rows)
    lines = [
        "# 1394 - Bedeutungsnetz Feldrollen-Familien",
        "",
        "## Zweck",
        "",
        "Diese Diagnose verdichtet starke Bedeutungsnetz-Knoten aus der Rohwelt-Ruecklesung zu passiven Feldrollen-Familien.",
        "",
        "Sie beschreibt keine Handlung. Sie zeigt nur, welche Art von Welt- und Feldnaehe ein Knoten ueber Folgewelten traegt.",
        "",
        "## Befund",
        "",
        f"- untersuchte starke Knoten: `{len(out_rows)}`",
        f"- Feldrollen-Familien: `{', '.join(f'{key}:{value}' for key, value in family_counts.most_common())}`",
        "",
        "## Rollen",
        "",
        *[
            f"- `{row['old_node']}` -> `{row['role_family']}`: Fenster `{row['windows']}`, Welten `{row['world_count']}`, Range `{row['avg_raw_range_pct']}`, Feldspannung `{row['avg_field_tension']}`"
            for row in sorted(out_rows, key=lambda item: int(item["windows"]), reverse=True)
        ],
        "",
        "## Lesung",
        "",
        "Die starken Knoten bilden keine einheitliche Klasse.",
        "Sie trennen sich in ruhige Feldnaehe, offene Nachbarschaft und gerichtete Spannungsnaehe.",
        "Damit entsteht aus dem Bedeutungsnetz eine erste passive Rollenordnung: gleiche Weltnaehe kann je nach Feldkontakt anders getragen werden.",
        "",
        "## Wie es weitergeht",
        "",
        "Als naechstes sollte geprueft werden, ob diese Feldrollen-Familien bei einer weiteren neuen Welt stabil bleiben oder ob eine Familie in zwei Unterrollen zerfaellt.",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
