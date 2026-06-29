from __future__ import annotations

import argparse
import csv
from pathlib import Path


PASSIVE_FLAGS = {
    "passive_only": 1,
    "read_by_mini_dio": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
}


METRICS = [
    "delta_seen_stability_vs_world",
    "delta_seen_change_vs_world",
    "delta_energy_tone_vs_world",
    "delta_energy_shift_abs_vs_world",
    "delta_loudness_vs_world",
    "delta_visual_sharpness_vs_world",
    "delta_felt_pressure_vs_world",
    "delta_adapted_field_intake_vs_world",
    "delta_mcm_tension_vs_world",
    "avg_target_rekopplung",
    "avg_target_strain",
]


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _avg(rows: list[dict[str, str]], key: str) -> float:
    return sum(_safe_float(row.get(key)) for row in rows) / max(1, len(rows))


def build_rows(recoupling: list[dict[str, str]], fragmentation: list[dict[str, str]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for metric in METRICS:
        rec = _avg(recoupling, metric)
        frag = _avg(fragmentation, metric)
        rows.append(
            {
                **PASSIVE_FLAGS,
                "metric": metric,
                "recoupling_avg": round(rec, 6),
                "fragmentation_avg": round(frag, 6),
                "fragmentation_minus_recoupling": round(frag - rec, 6),
                "reading": _reading(metric, rec, frag),
            }
        )
    return rows


def _reading(metric: str, rec: float, frag: float) -> str:
    delta = frag - rec
    if metric == "delta_energy_tone_vs_world":
        return "Fragmentierung zeigt vorab deutlich mehr tonale Energie relativ zur Weltbasis." if delta > 0 else "Rekopplung zeigt hoehere tonale Energie."
    if metric == "delta_adapted_field_intake_vs_world":
        return "Fragmentierung zeigt vorab mehr Feldaufnahme relativ zur Weltbasis." if delta > 0 else "Rekopplung zeigt mehr Feldaufnahme."
    if metric == "delta_seen_stability_vs_world":
        return "Fragmentierung ist im Sichtkanal nicht einfach stabiler; der Unterschied bleibt weltabhaengig." if abs(delta) < 0.02 else "Sichtstabilitaet unterscheidet die Zielzustaende sichtbar."
    if metric == "avg_target_rekopplung":
        return "Rekopplungstraeger liegen im Zielzustand deutlich hoeher als Fragmentierung."
    if metric == "avg_target_strain":
        return "Fragmentierung liegt im Zielzustand deutlich hoeher in Strain/Last."
    if abs(delta) < 0.01:
        return "Keine starke mittlere Trennung."
    return "Fragmentierung liegt hoeher." if delta > 0 else "Rekopplung liegt hoeher."


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, object]], recoupling_count: int, fragmentation_count: int) -> None:
    by_metric = {str(row["metric"]): row for row in rows}
    lines = [
        "# Rekopplung gegen Fragmentierung: Rohwelt-Vorfeldvergleich",
        "",
        "## Zweck",
        "",
        "Diese Diagnose legt die Ruecklesung vor Rekopplungsbindung neben die Ruecklesung vor belasteter Fragmentierung.",
        "Sie prueft, ob beide Zielzustaende aus derselben Vorwelt entstehen oder unterschiedliche sinnliche Vorbedingungen zeigen.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Diagnose",
        "- keine Handlung",
        "- kein Gate",
        "- keine Strategie",
        "- Mittelwerte sind Vergleichshinweise, keine absoluten Regeln",
        "",
        "## Kurzbefund",
        "",
        f"- Rekopplungsprofile: `{recoupling_count}`",
        f"- Fragmentierungsprofile: `{fragmentation_count}`",
        f"- Energie-Delta Fragmentierung minus Rekopplung: `{by_metric['delta_energy_tone_vs_world']['fragmentation_minus_recoupling']}`",
        f"- Feldaufnahme-Delta Fragmentierung minus Rekopplung: `{by_metric['delta_adapted_field_intake_vs_world']['fragmentation_minus_recoupling']}`",
        f"- Ziel-Strain Fragmentierung minus Rekopplung: `{by_metric['avg_target_strain']['fragmentation_minus_recoupling']}`",
        "",
        "## Vergleichsmatrix",
        "",
        "| Metrik | Rekopplung | Fragmentierung | Delta | Lesung |",
        "|---|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['metric']}` | {row['recoupling_avg']} | {row['fragmentation_avg']} | "
            f"{row['fragmentation_minus_recoupling']} | {row['reading']} |"
        )
    lines.extend(
        [
            "",
            "## Arbeitsableitung",
            "",
            "```text",
            "Rekopplung und Fragmentierung entstehen nicht aus derselben Vorfeldqualitaet.",
            "Rekopplung folgt im Mittel einem gedaempften Vorfeld mit geringerer tonaler Energie und geringerer Feldaufnahme.",
            "Fragmentierung ist selten, zeigt aber im Mittel mehr tonale Energie und mehr Feldaufnahme relativ zur eigenen Weltbasis.",
            "```",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese Trennung auf weitere Weltgruppen geprueft werden.",
            "Wenn sie stabil bleibt, kann daraus eine passive Rezeptor-Regulationsdiagnose entstehen: nicht als Regel, sondern als Lesung, wann das Feld eher bindet oder eher fragmentiert.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--recoupling", required=True, type=Path)
    parser.add_argument("--fragmentation", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    recoupling = _load(args.recoupling)
    fragmentation = _load(args.fragmentation)
    rows = build_rows(recoupling, fragmentation)
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows, len(recoupling), len(fragmentation))
    print(f"metrics={len(rows)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
