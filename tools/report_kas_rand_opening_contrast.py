from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


NUMERIC_KEYS = [
    "zentrum",
    "offen",
    "rand_kipp",
    "rekopplungsnaehe",
    "avg_raw_field",
    "max_raw_field",
    "avg_adapted_field",
    "avg_reduction",
    "avg_loudness",
    "max_loudness",
    "avg_visual_sharpness",
    "avg_visual_blur",
    "avg_mcm_tension",
    "avg_mcm_coherence",
    "avg_mcm_asymmetry",
    "avg_strain",
    "avg_rekopplung",
    "price_drift",
    "abs_price_drift",
    "max_range_pct",
    "avg_range_pct",
    "direction_change_ratio",
]


def _float(row: dict[str, str], key: str) -> float:
    try:
        return float(row.get(key, "") or 0.0)
    except ValueError:
        return 0.0


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _class_summary(class_name: str, rows: list[dict[str, str]]) -> dict[str, object]:
    family_counts = Counter(row.get("dominant_family", "-") or "-" for row in rows)
    out: dict[str, object] = {
        "segment_class": class_name,
        "segments": len(rows),
        "families": len(family_counts),
        "top_family": family_counts.most_common(1)[0][0] if family_counts else "-",
        "top_family_count": family_counts.most_common(1)[0][1] if family_counts else 0,
    }
    for key in NUMERIC_KEYS:
        out[key] = round(_avg([_float(row, key) for row in rows]), 6)
    return out


def _write_csv(rows: list[dict[str, object]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _delta(a: dict[str, object], b: dict[str, object], key: str) -> float:
    return float(a.get(key, 0.0) or 0.0) - float(b.get(key, 0.0) or 0.0)


def _write_markdown(rows: list[dict[str, object]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    by_class = {str(row["segment_class"]): row for row in rows}
    rand = by_class.get("reale_randphase", {})
    opening = by_class.get("reale_oeffnungsphase", {})
    mixed = by_class.get("gemischter_uebergang", {})

    focus_keys = [
        "rand_kipp",
        "offen",
        "zentrum",
        "avg_raw_field",
        "avg_loudness",
        "avg_visual_blur",
        "avg_visual_sharpness",
        "avg_mcm_tension",
        "avg_strain",
        "avg_rekopplung",
        "abs_price_drift",
        "max_range_pct",
        "direction_change_ratio",
    ]

    lines = [
        "# KAS Randnaehe Gegen Normale Oeffnung",
        "",
        "## Zweck",
        "",
        "Diese Diagnose trennt innerhalb der KAS-Referenzwelt echte Rand/Kipp-Naehe von normaler offener Wahrnehmung.",
        "Sie ist passiv und erzeugt keine Runtime-Regel.",
        "",
        "## Klassenvergleich",
        "",
        "| Klasse | Segmente | Familien | Top-Familie | Zentrum | Offen | Rand | Rohfeld avg | Lautheit avg | Unschaerfe avg | MCM-Spannung | Strain | Rekopplung | Drift abs | Range max | Wechsel |",
        "|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {segment_class} | {segments} | {families} | {top_family} ({top_family_count}) | {zentrum:.4f} | {offen:.4f} | {rand_kipp:.4f} | {avg_raw_field:.4f} | {avg_loudness:.4f} | {avg_visual_blur:.4f} | {avg_mcm_tension:.4f} | {avg_strain:.4f} | {avg_rekopplung:.4f} | {abs_price_drift:.4f} | {max_range_pct:.4f} | {direction_change_ratio:.4f} |".format(
                **row
            )
        )

    lines.extend(["", "## Mechanischer Kontrast", ""])
    if rand and opening:
        lines.extend(
            [
                "Gegenueber normaler Oeffnung zeigt echte KAS-Randnaehe:",
                "",
                f"- Rand/Kipp-Anteil: `{_delta(rand, opening, 'rand_kipp'):+.4f}`",
                f"- Offen-Anteil: `{_delta(rand, opening, 'offen'):+.4f}`",
                f"- Zentrum-Anteil: `{_delta(rand, opening, 'zentrum'):+.4f}`",
                f"- Rohfeldaufnahme: `{_delta(rand, opening, 'avg_raw_field'):+.4f}`",
                f"- Lautheit: `{_delta(rand, opening, 'avg_loudness'):+.4f}`",
                f"- visuelle Unschaerfe: `{_delta(rand, opening, 'avg_visual_blur'):+.4f}`",
                f"- MCM-Spannung: `{_delta(rand, opening, 'avg_mcm_tension'):+.4f}`",
                f"- Strain: `{_delta(rand, opening, 'avg_strain'):+.4f}`",
                f"- Rekopplung: `{_delta(rand, opening, 'avg_rekopplung'):+.4f}`",
                f"- absolute Drift: `{_delta(rand, opening, 'abs_price_drift'):+.4f}`",
                f"- maximale Range: `{_delta(rand, opening, 'max_range_pct'):+.4f}`",
                f"- Richtungswechsel: `{_delta(rand, opening, 'direction_change_ratio'):+.4f}`",
                "",
            ]
        )

    lines.extend(
        [
            "## Befund",
            "",
            "Normale Oeffnung ist in KAS haeufig. Echte Randnaehe ist selten, aber deutlich.",
            "Der Unterschied liegt nicht in einem einzelnen Wert, sondern in einer Kopplung aus Feldoeffnung, erhoehter Rohfeldaufnahme, hoher Lautheit, geringerer Schaerfe und realer Weltbewegung.",
            "",
            "Fuer die Mechanik bedeutet das: MINI_DIO sollte Oeffnung nicht automatisch als Gefahr lesen. Erst wenn Oeffnung mit Rand/Kipp-Naehe, Rohfeldlast und Rekopplungsverlust zusammenfaellt, entsteht eine belastete Feldlage.",
            "",
            "## Konsequenz Fuer MINI_DIO",
            "",
            "- Rezeptorische Wahrnehmung bleibt vor dem Feld.",
            "- Das MCM-Feld bewertet keine Einzelachse isoliert.",
            "- Randnaehe ist ein Feldzustand aus Zusammenwirkung, kein harter Sensorwert.",
            "- Fuer ein spaeteres DIO-Handlungssystem ist diese Trennung zentral: offene Wahrnehmung darf beobachtbar bleiben, ohne sofort als Blockade oder Aktion gelesen zu werden.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese KAS-Kontrastsignatur gegen PAXG geprueft werden. Ziel: verstehen, warum PAXG trotz Hochlast weniger echte Randnaehe ausbildet.",
        ]
    )

    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--segments", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--csv-out", required=True)
    args = parser.parse_args()

    rows = _load(Path(args.segments))
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row.get("segment_class", "-") or "-"].append(row)

    order = ["reale_randphase", "reale_oeffnungsphase", "gemischter_uebergang", "rekopplung_umfeld"]
    summaries = [_class_summary(name, grouped[name]) for name in order if grouped.get(name)]
    _write_csv(summaries, Path(args.csv_out))
    _write_markdown(summaries, Path(args.out))
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
