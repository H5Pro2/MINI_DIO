from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


PRESETS: dict[str, tuple[tuple[str, int], ...]] = {
    "harmonic": (
        ("ruhig", 900),
        ("expansion", 900),
        ("unruhe", 900),
        ("kippnaehe", 900),
        ("rekopplung", 900),
        ("ruhe_rueckkehr", 900),
    ),
    "bruch_rand": (
        ("ruhig_vorlast", 700),
        ("oeffnung", 700),
        ("bruch_impuls", 700),
        ("randflackern", 700),
        ("gegenpol", 700),
        ("rekopplung", 700),
        ("ruhe_nachhall", 700),
        ("zweiter_kippimpuls", 500),
        ("zweite_rekopplung", 400),
    ),
    "rand_dominanz": (
        ("ruhig_basis", 600),
        ("druckaufbau", 600),
        ("laute_randphase", 800),
        ("asymmetrischer_bruch", 700),
        ("gegenzerrung", 700),
        ("ueberreizter_nachhall", 700),
        ("rekopplungsversuch", 700),
        ("ruhe_restspannung", 600),
        ("zweiter_randstoss", 600),
        ("schluss_rekopplung", 600),
    ),
}


def _float(row: dict[str, str], key: str) -> float:
    try:
        return float(row.get(key, "") or 0.0)
    except ValueError:
        return 0.0


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _phase_for_tick(tick: int, phases: tuple[tuple[str, int], ...]) -> str:
    index = max(0, tick - 1)
    offset = 0
    for name, length in phases:
        if index < offset + length:
            return name
        offset += length
    return phases[-1][0]


def _role(row: dict[str, str]) -> str:
    rec = _float(row, "mcm_rekopplung_quality")
    carry = _float(row, "mcm_carry_quality")
    strain = _float(row, "mcm_strain_quality")
    pressure = _float(row, "mcm_feldwirkung_mcm_tension") or _float(row, "perception_adapted_field_intake_pressure")
    if rec >= 0.704 and carry >= 0.533 and pressure <= 0.425 and strain <= 0.18:
        return "zentrum_stabil"
    if pressure >= 0.438 or strain >= 0.25:
        return "spannungsrand_kippnaehe"
    if rec < 0.702 and carry < 0.533:
        return "offene_variante"
    return "rekopplungsnaehe"


def _phase_rows(episodes_csv: Path, preset: str) -> list[dict[str, object]]:
    phases = PRESETS[preset]
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    with episodes_csv.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            tick = int(float(row.get("tick", "0") or 0))
            grouped[_phase_for_tick(tick, phases)].append(row)

    output: list[dict[str, object]] = []
    for phase, _length in phases:
        rows = grouped.get(phase, [])
        roles = Counter(_role(row) for row in rows)
        total = max(1, len(rows))

        raw_intake = _avg([_float(row, "perception_raw_field_intake_pressure") for row in rows])
        adapted_intake = _avg([_float(row, "perception_adapted_field_intake_pressure") for row in rows])
        damping = _avg([_float(row, "perception_regulation_damping") for row in rows])
        adaptation = _avg([_float(row, "perception_adaptation_potential") for row in rows])
        loudness = _avg([_float(row, "perception_auditory_loudness") for row in rows])
        softening = _avg([_float(row, "perception_auditory_softening") for row in rows])
        auditory_stim = _avg([_float(row, "rezeptor_auditory_stimulation") for row in rows])
        visual_salience = _avg([_float(row, "rezeptor_visual_form_salience") for row in rows])
        visual_sharpness = _avg([_float(row, "perception_visual_sharpness") for row in rows])
        visual_blur = _avg([_float(row, "perception_visual_blur") for row in rows])
        felt_pressure = _avg([_float(row, "perception_felt_pressure") for row in rows])
        felt_relaxation = _avg([_float(row, "perception_felt_relaxation") for row in rows])
        mcm_tension = _avg([_float(row, "mcm_feldwirkung_mcm_tension") for row in rows])
        mcm_coherence = _avg([_float(row, "mcm_feldwirkung_mcm_coherence") for row in rows])
        mcm_asymmetry = _avg([_float(row, "mcm_feldwirkung_mcm_asymmetry") for row in rows])

        intake_reduction = max(0.0, raw_intake - adapted_intake)
        adaptation_ratio = adapted_intake / raw_intake if raw_intake > 1e-9 else 0.0
        auditory_to_field_gap = max(0.0, loudness - raw_intake)
        visual_loss = visual_blur

        axis_values = {
            "hoeren": loudness + auditory_stim + auditory_to_field_gap,
            "sehen": visual_salience + visual_loss,
            "feldinput": raw_intake + adapted_intake + intake_reduction + damping + adaptation,
            "druck": felt_pressure + mcm_tension + mcm_asymmetry - (felt_relaxation * 0.20),
        }
        strongest_axis = max(axis_values.items(), key=lambda item: item[1])[0]
        limiting_axis = "adaptation" if intake_reduction > 0.01 or adaptation_ratio < 0.92 else "gering"

        output.append(
            {
                "phase": phase,
                "episodes": len(rows),
                "zentrum": round(roles["zentrum_stabil"] / total, 6),
                "offen": round(roles["offene_variante"] / total, 6),
                "rand_kipp": round(roles["spannungsrand_kippnaehe"] / total, 6),
                "rekopplungsnaehe": round(roles["rekopplungsnaehe"] / total, 6),
                "auditory_loudness": round(loudness, 6),
                "auditory_softening": round(softening, 6),
                "auditory_stimulation": round(auditory_stim, 6),
                "visual_salience": round(visual_salience, 6),
                "visual_sharpness": round(visual_sharpness, 6),
                "visual_blur": round(visual_blur, 6),
                "raw_field_intake": round(raw_intake, 6),
                "adapted_field_intake": round(adapted_intake, 6),
                "intake_reduction": round(intake_reduction, 6),
                "adaptation_ratio": round(adaptation_ratio, 6),
                "regulation_damping": round(damping, 6),
                "adaptation_potential": round(adaptation, 6),
                "felt_pressure": round(felt_pressure, 6),
                "felt_relaxation": round(felt_relaxation, 6),
                "mcm_tension": round(mcm_tension, 6),
                "mcm_coherence": round(mcm_coherence, 6),
                "mcm_asymmetry": round(mcm_asymmetry, 6),
                "auditory_to_field_gap": round(auditory_to_field_gap, 6),
                "hoeren_score": round(axis_values["hoeren"], 6),
                "sehen_score": round(axis_values["sehen"], 6),
                "feldinput_score": round(axis_values["feldinput"], 6),
                "druck_score": round(axis_values["druck"], 6),
                "strongest_axis": strongest_axis,
                "limiting_axis": limiting_axis,
            }
        )
    return output


def _write_csv(rows: list[dict[str, object]], csv_out: Path) -> None:
    csv_out.parent.mkdir(parents=True, exist_ok=True)
    with csv_out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(rows: list[dict[str, object]], out: Path, title: str) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = [
        f"# {title}",
        "",
        "Passive Differenzdiagnose: Welche Rezeptorachse traegt Randlast, und wo wird sie vor dem MCM-Feld begrenzt?",
        "",
        "Die Diagnose ist kein Gate und keine Runtime-Regel. Sie liest nur vorhandene Episodenspuren.",
        "",
        "## Phasenmatrix",
        "",
        "| Phase | Episoden | Zentrum | Offen | Rand/Kipp | Lautheit | Schaerfe | Rohfeld | Adaptfeld | Reduktion | Ratio | Druck | MCM-Spannung | staerkste Achse | Begrenzung |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for row in rows:
        lines.append(
            "| {phase} | {episodes} | {zentrum:.4f} | {offen:.4f} | {rand_kipp:.4f} | {auditory_loudness:.4f} | {visual_sharpness:.4f} | {raw_field_intake:.4f} | {adapted_field_intake:.4f} | {intake_reduction:.4f} | {adaptation_ratio:.4f} | {felt_pressure:.4f} | {mcm_tension:.4f} | {strongest_axis} | {limiting_axis} |".format(
                **row
            )
        )

    highest_rand = max(rows, key=lambda row: float(row["rand_kipp"]))
    highest_open = max(rows, key=lambda row: float(row["offen"]))
    highest_loud = max(rows, key=lambda row: float(row["auditory_loudness"]))
    strongest_reduction = max(rows, key=lambda row: float(row["intake_reduction"]))
    lowest_sharpness = min(rows, key=lambda row: float(row["visual_sharpness"]))

    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"- Staerkste lokale Rand/Kipp-Naehe: `{highest_rand['phase']}` mit `{float(highest_rand['rand_kipp']):.4f}`.",
            f"- Staerkste offene Variante: `{highest_open['phase']}` mit `{float(highest_open['offen']):.4f}`.",
            f"- Staerkste auditive Lautheit: `{highest_loud['phase']}` mit `{float(highest_loud['auditory_loudness']):.4f}`.",
            f"- Staerkste rezeptorische Reduktion: `{strongest_reduction['phase']}` mit `{float(strongest_reduction['intake_reduction']):.4f}`.",
            f"- Niedrigste visuelle Schaerfe: `{lowest_sharpness['phase']}` mit `{float(lowest_sharpness['visual_sharpness']):.4f}`.",
            "",
            "## Ableitung",
            "",
            "Rand-/Oeffnungslast entsteht in den geprueften synthetischen Welten nicht als reine MCM-Entgleisung. Sie steigt lokal dort, wo auditive Lautheit, Rohfeldaufnahme und fallende visuelle Schaerfe zusammenkommen.",
            "",
            "Die Begrenzung liegt bisher vor allem in der rezeptorischen Adaptation: Rohfeldaufnahme wird in adaptierte Feldaufnahme uebersetzt, und die Randphase bleibt deshalb lokal statt global kollabierend.",
            "",
            "Damit wirkt die Rezeptorschicht nicht nur als Vorfilter, sondern als organische Aufnahmegrenze: Sie laesst Weltspannung ins Feld, aber nicht als ungebremste Rohdatenflut.",
            "",
            "Wie es weitergeht: Als naechstes sollte dieselbe Achsendiagnose gegen Bruch/Rand und Harmonie laufen, damit klar wird, ob die Begrenzung spezifisch fuer Randdominanz ist oder eine allgemeine MINI_DIO-Aufnahmeeigenschaft.",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--episodes", required=True)
    parser.add_argument("--preset", choices=sorted(PRESETS), required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--csv-out", required=True)
    parser.add_argument("--title", default="Synthetische Rezeptorachsen-Limitdiagnose")
    args = parser.parse_args()

    rows = _phase_rows(Path(args.episodes), args.preset)
    _write_csv(rows, Path(args.csv_out))
    _write_markdown(rows, Path(args.out), args.title)
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
