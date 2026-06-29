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


AXES = {
    "delta_energy_tone_vs_world": ("hoeren", "tonale_energie"),
    "delta_energy_shift_abs_vs_world": ("hoeren", "tonaler_wechsel"),
    "delta_loudness_vs_world": ("hoeren", "lautheit"),
    "delta_seen_stability_vs_world": ("sehen", "formstabilitaet"),
    "delta_seen_change_vs_world": ("sehen", "formwechsel"),
    "delta_visual_sharpness_vs_world": ("sehen", "schaerfe"),
    "delta_felt_pressure_vs_world": ("fuehlen", "druck"),
    "delta_adapted_field_intake_vs_world": ("rezeptor", "feldaufnahme"),
    "delta_mcm_tension_vs_world": ("mcm_feld", "feldspannung"),
}


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _load(path: Path) -> dict[str, dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return {str(row.get("metric") or ""): row for row in csv.DictReader(handle)}


def _classify(values: list[float]) -> tuple[str, str]:
    signs = [1 if value > 0 else -1 if value < 0 else 0 for value in values]
    abs_values = [abs(value) for value in values]
    if all(sign > 0 for sign in signs) and min(abs_values) >= 0.02:
        return "fragmentierungsnaehe_stabil", "Achse liegt in beiden Gruppen klar hoeher vor Fragmentierung."
    if all(sign < 0 for sign in signs) and min(abs_values) >= 0.02:
        return "bindungsnaehe_stabil", "Achse liegt in beiden Gruppen klar hoeher vor Rekopplung."
    if all(sign > 0 for sign in signs):
        return "fragmentierungsnaehe_schwach", "Achse zeigt gleiche Richtung, aber mindestens eine Gruppe ist schwach."
    if all(sign < 0 for sign in signs):
        return "bindungsnaehe_schwach", "Achse zeigt gleiche Richtung, aber mindestens eine Gruppe ist schwach."
    return "weltabhaengig_oder_widerspruechlich", "Achse kippt zwischen Weltgruppen oder ist nicht stabil trennend."


def build_rows(group1: dict[str, dict[str, str]], group2: dict[str, dict[str, str]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for metric, (sense_axis, receptor_axis) in AXES.items():
        g1 = _safe_float(group1.get(metric, {}).get("fragmentation_minus_recoupling"))
        g2 = _safe_float(group2.get(metric, {}).get("fragmentation_minus_recoupling"))
        regulation_class, reading = _classify([g1, g2])
        rows.append(
            {
                **PASSIVE_FLAGS,
                "sense_axis": sense_axis,
                "receptor_axis": receptor_axis,
                "metric": metric,
                "group1_delta_fragmentation_minus_recoupling": round(g1, 6),
                "group2_delta_fragmentation_minus_recoupling": round(g2, 6),
                "mean_delta": round((g1 + g2) / 2.0, 6),
                "regulation_reading": regulation_class,
                "reading": reading,
            }
        )
    return rows


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, object]]) -> None:
    lines = [
        "# Passive Rezeptor-Regulationskarte",
        "",
        "## Zweck",
        "",
        "Diese Datei verdichtet die Rohwelt-Ruecklesungen zu einer passiven Rezeptor-Regulationskarte.",
        "Sie liest, welche Sinnesachsen eher Bindungsnaehe oder Fragmentierungsnaehe anzeigen.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Lesekarte",
        "- keine Handlung",
        "- kein Gate",
        "- keine Strategie",
        "- keine harte Regulation",
        "",
        "## Karte",
        "",
        "| Sinnesachse | Rezeptorachse | Metrik | Gruppe 1 Delta | Gruppe 2 Delta | Mittel | Leseklasse | Deutung |",
        "|---|---|---|---:|---:|---:|---|---|",
    ]
    for row in sorted(rows, key=lambda item: abs(float(item["mean_delta"])), reverse=True):
        lines.append(
            f"| `{row['sense_axis']}` | `{row['receptor_axis']}` | `{row['metric']}` | "
            f"{row['group1_delta_fragmentation_minus_recoupling']} | "
            f"{row['group2_delta_fragmentation_minus_recoupling']} | {row['mean_delta']} | "
            f"`{row['regulation_reading']}` | {row['reading']} |"
        )

    stable_fragment = [row for row in rows if row["regulation_reading"] == "fragmentierungsnaehe_stabil"]
    weak_fragment = [row for row in rows if row["regulation_reading"] == "fragmentierungsnaehe_schwach"]
    weak_binding = [row for row in rows if row["regulation_reading"] == "bindungsnaehe_schwach"]
    unstable = [row for row in rows if row["regulation_reading"] == "weltabhaengig_oder_widerspruechlich"]

    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"- Stabile Fragmentierungsnaehe: `{', '.join(str(row['receptor_axis']) for row in stable_fragment) or '-'}`",
            f"- Schwache Fragmentierungsnaehe: `{', '.join(str(row['receptor_axis']) for row in weak_fragment) or '-'}`",
            f"- Schwache Bindungsnaehe: `{', '.join(str(row['receptor_axis']) for row in weak_binding) or '-'}`",
            f"- Weltabhaengig / nicht stabil: `{', '.join(str(row['receptor_axis']) for row in unstable) or '-'}`",
            "",
            "## Arbeitsableitung",
            "",
            "```text",
            "Die bisher robusteste passive Regulationsachse liegt im Hoeren:",
            "tonale Energie zeigt in beiden Weltgruppen Fragmentierungsnaehe.",
            "Andere Achsen bleiben wichtig, aber kontextabhaengiger.",
            "```",
            "",
            "Das ist keine Steuerung.",
            "Es ist eine Lesung darueber, welche Aufnahmeform das Feld spaeter eher bindet oder belastet.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese Karte gegen weitere Sinnes-/Feldrollen gelegt werden.",
            "Ziel: pruefen, ob tonale Energie wirklich als fruehe Fragmentierungsnaehe wirkt oder nur in den bisher geprueften Welten dominant war.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--group1", required=True, type=Path)
    parser.add_argument("--group2", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    rows = build_rows(_load(args.group1), _load(args.group2))
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"axes={len(rows)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
