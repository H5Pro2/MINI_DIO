from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


def _read_rows(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    if not text.strip():
        return []
    sample = text[:4096]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",;")
    except csv.Error:
        dialect = csv.excel
    return list(csv.DictReader(text.splitlines(), dialect=dialect))


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _float(row: dict[str, str], key: str) -> float:
    try:
        return float(row.get(key, "0") or 0.0)
    except ValueError:
        return 0.0


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _counter_text(counter: Counter[str], limit: int = 8) -> str:
    if not counter:
        return "-"
    return " | ".join(f"{key}:{value}" for key, value in counter.most_common(limit))


def _classify(row: dict[str, str]) -> str:
    side = row.get("side", "-")
    mode = row.get("mode", "-")
    phase = row.get("phase_hint", "-")
    movement = row.get("dominant_movement", "-")
    ret = _float(row, "return_pct")
    rng = _float(row, "range_pct")
    pressure = _float(row, "pressure_abs")

    if mode == "rekopplung_nach_abverkauf":
        return "last_rebound_rekopplung"
    if side == "bull" and "expansion" in mode:
        return "bull_expansion"
    if side == "bull" and "bruch" in mode and ret < 0:
        return "bull_open_bruch_risk"
    if side == "selloff" and "rekopplung" in mode:
        return "falling_rekopplung"
    if side == "selloff" and "bruch" in mode:
        return "falling_bruch"
    if "rekopplung" in movement and pressure <= 0.06:
        return "quiet_rekopplung"
    if rng >= 40:
        return "wide_transition"
    if "offen" in phase:
        return "open_transition"
    return "mixed_axis_state"


def _summarize(rows: list[dict[str, str]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    annotated: list[dict[str, object]] = []
    for row in rows:
        reading = _classify(row)
        annotated.append(
            {
                "reading": reading,
                "side": row.get("side", "-"),
                "mode": row.get("mode", "-"),
                "world": row.get("world", "-"),
                "pair": row.get("pair", "-"),
                "phase_hint": row.get("phase_hint", "-"),
                "chart_zone": row.get("chart_zone", "-"),
                "dominant_movement": row.get("dominant_movement", "-"),
                "return_pct": _float(row, "return_pct"),
                "range_pct": _float(row, "range_pct"),
                "pressure_abs": _float(row, "pressure_abs"),
                "rekopplung_abs": _float(row, "rekopplung_abs"),
                "direction_pair": row.get("pair", "-"),
                "passive_only": 1,
                "read_by_mini_dio": 0,
                "influences_action": 0,
                "is_gate": 0,
                "is_motoric": 0,
                "is_entry_signal": 0,
                "is_direction_signal": 0,
            }
        )

    groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in annotated:
        groups[str(row["reading"])].append(row)

    summary: list[dict[str, object]] = []
    for reading, items in sorted(groups.items()):
        summary.append(
            {
                "reading": reading,
                "count": len(items),
                "sides": _counter_text(Counter(str(item["side"]) for item in items)),
                "modes": _counter_text(Counter(str(item["mode"]) for item in items)),
                "phase_hints": _counter_text(Counter(str(item["phase_hint"]) for item in items)),
                "movement_types": _counter_text(Counter(str(item["dominant_movement"]) for item in items)),
                "avg_return_pct": round(_mean([float(item["return_pct"]) for item in items]), 6),
                "avg_range_pct": round(_mean([float(item["range_pct"]) for item in items]), 6),
                "avg_pressure_abs": round(_mean([float(item["pressure_abs"]) for item in items]), 6),
                "avg_rekopplung_abs": round(_mean([float(item["rekopplung_abs"]) for item in items]), 6),
            }
        )
    return annotated, summary


def _write_md(path: Path, details: list[dict[str, object]], summary: list[dict[str, object]]) -> None:
    lines = [
        "# 1022 - Achse 183drjy<->1t5bcxp: Rollenqualitaet-Kippmerkmale",
        "",
        "Passive Isolation der gemeinsamen Achse aus Bull- und Selloff-Familien.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Diagnose",
        "- keine Handlung",
        "- kein Gate",
        "- keine Strategie",
        "- keine harte Regelableitung",
        "",
        "## Verdichtete Lesarten",
        "",
        "| Lesart | Count | Seiten | Modi | Phasen | Bewegung | Return % | Range % | Druck | Rekopplung |",
        "|---|---:|---|---|---|---|---:|---:|---:|---:|",
    ]
    for row in summary:
        lines.append(
            f"| `{row['reading']}` | {row['count']} | `{row['sides']}` | `{row['modes']}` | "
            f"`{row['phase_hints']}` | `{row['movement_types']}` | {row['avg_return_pct']} | "
            f"{row['avg_range_pct']} | {row['avg_pressure_abs']} | {row['avg_rekopplung_abs']} |"
        )

    lines.extend(
        [
            "",
            "## Einzelbelege",
            "",
            "| Lesart | Seite | Modus | Welt | Paar | Phase | Bewegung | Return % | Range % | Druck | Rekopplung |",
            "|---|---|---|---|---|---|---|---:|---:|---:|---:|",
        ]
    )
    for row in details:
        lines.append(
            f"| `{row['reading']}` | {row['side']} | `{row['mode']}` | `{row['world']}` | "
            f"`{row['pair']}` | `{row['phase_hint']}` | `{row['dominant_movement']}` | "
            f"{row['return_pct']} | {row['range_pct']} | {row['pressure_abs']} | {row['rekopplung_abs']} |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Achse `183drjy<->1t5bcxp` ist kein einzelner Bedeutungszustand.",
            "Sie traegt mehrere Rollenqualitaeten: Bull-Expansion, fallende Rekopplung, fallender Bruch und Erholung nach Abverkauf.",
            "",
            "Der Kippunterschied liegt in der Weltphase:",
            "",
            "- Bull-Expansion: hoeherer positiver Fortsetzungsanteil, meist groessere Range und mehr Druck.",
            "- Fallende Rekopplung: wiederkehrender Rekopplungsuebergang unter negativer Bewegung.",
            "- Bruch: dieselbe Achse bleibt sichtbar, aber die Bewegung liest sich als Umordnung oder Belastung.",
            "- Erholung nach Abverkauf: Sonderlage mit sehr hoher Range und positiver Bewegung nach vorheriger negativer Last.",
            "",
            "## Schluss",
            "",
            "Die gemeinsame Achse wirkt wie ein Feldkanal, der verschiedene Weltphasen tragen kann.",
            "Mini-DIOs MCM-Lesung sollte deshalb nicht nach Richtung, sondern nach Rollenqualitaet gelesen werden:",
            "Welche Art von Kopplung entsteht an derselben Achse unter welcher Weltspannung?",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese Achse gegen echte Chartsegmente geplottet werden: gleiche Achse, vier Lesarten, direkte Sicht auf die Weltfenster.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--details", required=True, type=Path)
    parser.add_argument("--out-details", required=True, type=Path)
    parser.add_argument("--out-summary", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    args = parser.parse_args()

    rows = [row for row in _read_rows(args.details) if row.get("axis") == "183drjy<->1t5bcxp"]
    details, summary = _summarize(rows)
    _write_csv(args.out_details, details)
    _write_csv(args.out_summary, summary)
    _write_md(args.out_md, details, summary)
    print(f"axis_rows={len(rows)}")
    print(f"readings={len(summary)}")
    print(f"wrote {args.out_md}")


if __name__ == "__main__":
    main()
