from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PHASES = {
    "vorlauf": lambda rel: rel < 0,
    "ereignis": lambda rel: rel == 0,
    "nachlauf": lambda rel: rel > 0,
}


def _float(value: object) -> float:
    try:
        out = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if out != out else out


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _report_title(path: Path, fallback: str) -> str:
    stem = path.stem
    if "_" in stem and stem.split("_", 1)[0].isdigit():
        number, rest = stem.split("_", 1)
        return f"{number} - {rest.replace('_', ' ').title()}"
    return fallback


def _dominant(rows: list[dict[str, str]], key: str) -> str:
    counter = Counter(str(row.get(key) or "-") for row in rows)
    return counter.most_common(1)[0][0] if counter else "-"


def _classify(pattern: str, phase_rows: dict[str, list[dict[str, str]]]) -> str:
    event = phase_rows.get("ereignis", [])
    after = phase_rows.get("nachlauf", [])
    event_field = _dominant(event, "field_label")
    after_field = _dominant(after, "field_label")
    event_rec = _mean([_float(row.get("mcm_rekopplung_quality")) for row in event])
    event_strain = _mean([_float(row.get("mcm_strain_quality")) for row in event])
    after_tension = _mean([_float(row.get("mcm_feldwirkung_mcm_tension")) for row in after])
    if pattern == "tragende_verarbeitung" and event_field == "rekoppelt" and event_rec >= 0.72:
        return "rekopplungspunkt_mit_nachhallpruefung"
    if pattern == "kippnaehe" and event_field == "offen" and after_field != "rekoppelt":
        return "offene_kippnaehe_mit_nachlaufspannung"
    if event_strain >= 0.18 or after_tension >= 0.16:
        return "spannungsnahe_folge"
    return "gemischte_feldfolge"


def _write_md(path: Path, source: str, rows: list[dict[str, object]], family: str) -> None:
    lines = [
        f"# {_report_title(path, f'{family} Feldfolgen-Signatur')}",
        "",
        "## Grundfrage",
        "",
        "Die Prüfung verdichtet Tickfenster zu einer kompakten Feldfolgen-Signatur.",
        "",
        "Gelesen werden Vorlauf, Ereignis und Nachlauf getrennt. Die Diagnose bleibt passiv.",
        "",
        f"Quelle: `{source}`",
        "",
        "## Signatur",
        "",
        "| Muster | Phase | Zeilen | Visual | Ton | Feld | Spannung | Rekopplung | Strain | Raw Intake | Adapt Intake | Lesung |",
        "|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['pattern']}` | `{row['phase']}` | {row['rows']} | `{row['visual']}` | `{row['tone']}` | "
            f"`{row['field']}` | {row['avg_tension']} | {row['avg_rekopplung']} | {row['avg_strain']} | "
            f"{row['avg_raw_intake']} | {row['avg_adapted_intake']} | `{row['sequence_reading']}` |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"`{family}` zeigt in den geprüften Fenstern die folgenden Feldfolgen:",
            "",
            "- tragende Verarbeitung: Vorlauf offen/wechselnd, Ereignis rekoppelt, Nachlauf prüft weiter zwischen offen, rekoppelt und belastet.",
            "- Kippnähe: Ereignis bleibt offen, der Nachlauf trägt eher offene Spannung als stabile Rekopplung.",
            "",
            f"Damit ist `{family}` nicht einfach ein einzelnes Symbol. Die konkrete Lesart entsteht aus Feldfolge, Weltfenster und Nachbarschaft.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte diese Signatur mit der bisherigen Rollentaxonomie verglichen werden.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="reports/dio_0l7p_bridge_tick_windows.csv")
    parser.add_argument("--family", default="dio_0l7p")
    parser.add_argument("--out-csv", default="reports/dio_0l7p_bridge_tick_window_signature.csv")
    parser.add_argument("--out-md", default="docs/befunde/1802_DIO_0L7P_FELDFOLGEN_SIGNATUR.md")
    args = parser.parse_args()

    source_path = ROOT / args.source
    source_rows = _read_csv(source_path)
    grouped: dict[str, dict[str, list[dict[str, str]]]] = defaultdict(lambda: defaultdict(list))
    for row in source_rows:
        pattern = str(row.get("event_pattern") or "-")
        rel = int(_float(row.get("relative_pos")))
        for phase, predicate in PHASES.items():
            if predicate(rel):
                grouped[pattern][phase].append(row)
                break

    out_rows: list[dict[str, object]] = []
    for pattern, phase_rows in sorted(grouped.items()):
        sequence_reading = _classify(pattern, phase_rows)
        for phase in ["vorlauf", "ereignis", "nachlauf"]:
            rows = phase_rows.get(phase, [])
            out_rows.append(
                {
                    "family": args.family,
                    "pattern": pattern,
                    "phase": phase,
                    "rows": len(rows),
                    "visual": _dominant(rows, "visual_label"),
                    "tone": _dominant(rows, "tone_label"),
                    "field": _dominant(rows, "field_label"),
                    "avg_tension": round(_mean([_float(row.get("mcm_feldwirkung_mcm_tension")) for row in rows]), 6),
                    "avg_rekopplung": round(_mean([_float(row.get("mcm_rekopplung_quality")) for row in rows]), 6),
                    "avg_strain": round(_mean([_float(row.get("mcm_strain_quality")) for row in rows]), 6),
                    "avg_raw_intake": round(_mean([_float(row.get("perception_raw_field_intake_pressure")) for row in rows]), 6),
                    "avg_adapted_intake": round(
                        _mean([_float(row.get("perception_adapted_field_intake_pressure")) for row in rows]), 6
                    ),
                    "sequence_reading": sequence_reading,
                }
            )

    _write_csv(ROOT / args.out_csv, out_rows)
    _write_md(ROOT / args.out_md, args.source, out_rows, args.family)
    print({"patterns": len(grouped), "out": args.out_md})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
