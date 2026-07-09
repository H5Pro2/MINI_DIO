from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from statistics import fmean


ROOT = Path(__file__).resolve().parents[1]


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"


def _mean(values: list[float]) -> float:
    return fmean(values) if values else 0.0


def _summaries(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    grouped["ALLE"] = rows
    for row in rows:
        grouped[row.get("family", "-")].append(row)
    out: list[dict[str, object]] = []
    for family, items in grouped.items():
        pre_range = _mean([_float(row.get("pre_raw_range_pct")) for row in items])
        pre_hearing = _mean([_float(row.get("pre_hearing_gap")) for row in items])
        pre_tension = _mean([_float(row.get("pre_mcm_tension")) for row in items])
        open_range = _mean([_float(row.get("open_raw_range_pct")) for row in items])
        open_hearing = _mean([_float(row.get("open_hearing_gap")) for row in items])
        open_tension = _mean([_float(row.get("open_mcm_tension")) for row in items])
        out.append(
            {
                "family": family,
                "windows": len(items),
                "pre_range": pre_range,
                "pre_hearing": pre_hearing,
                "pre_tension": pre_tension,
                "open_range": open_range,
                "open_hearing": open_hearing,
                "open_tension": open_tension,
                "range_delta_open_minus_pre": open_range - pre_range,
                "hearing_delta_open_minus_pre": open_hearing - pre_hearing,
                "tension_delta_open_minus_pre": open_tension - pre_tension,
            }
        )
    return sorted(out, key=lambda row: str(row["family"]))


def _write_csv(rows: list[dict[str, object]], out_path: Path) -> None:
    csv_path = out_path.with_suffix(".csv")
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0].keys()) if rows else []
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        if not fields:
            return
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: _fmt(value, 6) if isinstance(value, float) else value for key, value in row.items()})


def _write_md(rows: list[dict[str, object]], out_path: Path) -> None:
    _write_csv(rows, out_path)
    title_prefix = out_path.stem.split("_", 1)[0]
    title = f"# {title_prefix} - Oeffnungs-Vorform der Ziel-Familien" if title_prefix.isdigit() else "# Oeffnungs-Vorform der Ziel-Familien"
    lines = [
        title,
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose verdichtet die Rohweltfenster aus 1701 zu einer Oeffnungs-Vorform.",
        "Sie bleibt passiv: keine Handlung, kein Gate, keine Richtung.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Gibt es eine gemeinsame Vorform vor erneuter Milieu-Oeffnung?",
        "2. Unterpruefung: Vorfenster und Oeffnungsfamilie aggregiert vergleichen.",
        "3. Folgeschritt: Diese Vorform gegen weitere Welten und laengere Fenster pruefen.",
        "",
        "## Aggregat",
        "",
        "| Familie | Fenster | Vor Range | Vor Hoeren | Vor Spannung | Open Range | Open Hoeren | Open Spannung | Delta Hoeren | Delta Spannung |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["family"]),
                    str(row["windows"]),
                    _fmt(float(row["pre_range"])),
                    _fmt(float(row["pre_hearing"])),
                    _fmt(float(row["pre_tension"])),
                    _fmt(float(row["open_range"])),
                    _fmt(float(row["open_hearing"])),
                    _fmt(float(row["open_tension"])),
                    _fmt(float(row["hearing_delta_open_minus_pre"])),
                    _fmt(float(row["tension_delta_open_minus_pre"])),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Die robuste Oeffnung zeigt in dieser Pruefung keine harte neue Weltlast.",
            "Vor der Oeffnung liegen Hoeren-Gap und Feldspannung moderat hoeher; in der Oeffnungsfamilie selbst fallen beide ab.",
            "",
            "Vorlaeufige Arbeitslesung:",
            "",
            "```text",
            "milieu_oeffnet_nach_entlastung:",
            "  moderate Vorlast",
            "  danach geringerer Hoer-Gap",
            "  danach geringere Feldspannung",
            "  gleiche Familienbewegung in mehreren Welten",
            "```",
            "",
            "Das spricht eher fuer eine Rekopplungs-/Entlastungsbewegung als fuer ein reines Stress- oder Rangeereignis.",
            "",
            "## Grenze",
            "",
            "Die Stichprobe ist klein. `dio_0ly7` und `dio_01hu` sind robuste Kandidaten, aber noch keine feste Bedeutungsdefinition.",
            "",
        ]
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Aggregiert robuste Ziel-Familien zu einer Oeffnungs-Vorform.")
    parser.add_argument("--raw-window-csv", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()
    rows = _summaries(_load_csv(_resolve(args.raw_window_csv)))
    _write_md(rows, _resolve(args.out_md))
    print({"out_md": str(_resolve(args.out_md)), "rows": len(rows)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
