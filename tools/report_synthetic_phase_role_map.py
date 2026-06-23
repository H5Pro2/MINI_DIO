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


def _phase_for_tick(tick: int, phases: tuple[tuple[str, int], ...]) -> str:
    index = max(0, tick - 1)
    offset = 0
    for name, length in phases:
        if index < offset + length:
            return name
        offset += length
    return phases[-1][0]


def _scale_phases(phases: tuple[tuple[str, int], ...], phase_scale: float) -> tuple[tuple[str, int], ...]:
    scale = max(0.05, float(phase_scale or 1.0))
    return tuple((name, max(1, int(round(length * scale)))) for name, length in phases)


def _order_phases(phases: tuple[tuple[str, int], ...], phase_order: str) -> tuple[tuple[str, int], ...]:
    if not str(phase_order or "").strip():
        return phases
    phase_by_name = {name: phase for phase in phases for name in [phase[0]]}
    ordered_names = [item.strip() for item in str(phase_order).split(",") if item.strip()]
    missing = [name for name in ordered_names if name not in phase_by_name]
    if missing:
        raise ValueError(f"unknown phase names: {', '.join(missing)}")
    if len(set(ordered_names)) != len(ordered_names):
        raise ValueError("phase-order contains duplicate phase names")
    remaining = [phase for phase in phases if phase[0] not in set(ordered_names)]
    return tuple(phase_by_name[name] for name in ordered_names) + tuple(remaining)


def _override_phase_lengths(phases: tuple[tuple[str, int], ...], phase_lengths: str) -> tuple[tuple[str, int], ...]:
    if not str(phase_lengths or "").strip():
        return phases
    overrides: dict[str, int] = {}
    for item in str(phase_lengths).split(","):
        if not item.strip():
            continue
        if "=" not in item:
            raise ValueError("phase-lengths entries must use name=length")
        name, raw_length = item.split("=", 1)
        name = name.strip()
        if not name:
            raise ValueError("phase-lengths contains an empty phase name")
        overrides[name] = max(1, int(float(raw_length.strip())))
    known = {phase[0] for phase in phases}
    missing = [name for name in overrides if name not in known]
    if missing:
        raise ValueError(f"unknown phase names: {', '.join(missing)}")
    return tuple((name, overrides.get(name, length)) for name, length in phases)


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


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def build_report(
    episodes_csv: Path,
    preset: str,
    phase_scale: float = 1.0,
    phase_order: str = "",
    phase_lengths: str = "",
) -> tuple[list[dict[str, object]], dict[str, Counter]]:
    phases = _override_phase_lengths(_order_phases(_scale_phases(PRESETS[preset], phase_scale), phase_order), phase_lengths)
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    with episodes_csv.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            tick = int(float(row.get("tick", "0") or 0))
            grouped[_phase_for_tick(tick, phases)].append(row)

    phase_rows: list[dict[str, object]] = []
    phase_roles: dict[str, Counter] = {}
    for name, _length in phases:
        rows = grouped.get(name, [])
        roles = Counter(_role(row) for row in rows)
        phase_roles[name] = roles
        total = max(1, len(rows))
        phase_rows.append(
            {
                "phase": name,
                "episodes": len(rows),
                "zentrum": round(roles["zentrum_stabil"] / total, 6),
                "offen": round(roles["offene_variante"] / total, 6),
                "rand_kipp": round(roles["spannungsrand_kippnaehe"] / total, 6),
                "rekopplungsnaehe": round(roles["rekopplungsnaehe"] / total, 6),
                "rekopplung": round(_avg([_float(row, "mcm_rekopplung_quality") for row in rows]), 6),
                "carry": round(_avg([_float(row, "mcm_carry_quality") for row in rows]), 6),
                "strain": round(_avg([_float(row, "mcm_strain_quality") for row in rows]), 6),
                "raw_field_intake": round(_avg([_float(row, "perception_raw_field_intake_pressure") for row in rows]), 6),
                "auditory_loudness": round(_avg([_float(row, "perception_auditory_loudness") for row in rows]), 6),
                "visual_sharpness": round(_avg([_float(row, "perception_visual_sharpness") for row in rows]), 6),
            }
        )
    return phase_rows, phase_roles


def write_outputs(phase_rows: list[dict[str, object]], phase_roles: dict[str, Counter], out: Path, csv_out: Path, title: str) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    csv_out.parent.mkdir(parents=True, exist_ok=True)
    with csv_out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(phase_rows[0].keys()))
        writer.writeheader()
        writer.writerows(phase_rows)

    lines: list[str] = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append("Passive Diagnose: synthetische Weltphase gegen entstehende MCM-Rolle. Die Phasen sind nur Auswertungshilfe, keine Runtime-Regel.")
    lines.append("")
    lines.append("## Phasenmatrix")
    lines.append("")
    lines.append("| Phase | Episoden | Zentrum | Offen | Rand/Kipp | Rekopplungsnähe | Rekopplung | Carry | Strain | Feldinput | Lautheit | Schärfe |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for row in phase_rows:
        lines.append(
            "| {phase} | {episodes} | {zentrum:.4f} | {offen:.4f} | {rand_kipp:.4f} | {rekopplungsnaehe:.4f} | {rekopplung:.4f} | {carry:.4f} | {strain:.4f} | {raw_field_intake:.4f} | {auditory_loudness:.4f} | {visual_sharpness:.4f} |".format(
                **row
            )
        )
    lines.append("")
    lines.append("## Rollenverteilung")
    for phase, roles in phase_roles.items():
        parts = ", ".join(f"{key}={value}" for key, value in roles.most_common())
        lines.append(f"- `{phase}`: {parts}")
    lines.append("")
    lines.append("## Befund")
    lines.append("Die Diagnose zeigt, ob die synthetisch gesetzten Weltphasen unterschiedliche Innenfeldrollen auslösen oder ob das Feld sie trotz Bruchstruktur zentrumsnah integriert.")
    lines.append("")
    lines.append("Wie es weitergeht: Die Phasenmatrix sollte gegen harmonische und Bruch-/Randwelt verglichen werden, um zu prüfen, ob die Rollenverschiebung wirklich phasengebunden ist.")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--episodes", required=True)
    parser.add_argument("--preset", choices=sorted(PRESETS), required=True)
    parser.add_argument(
        "--phase-scale",
        type=float,
        default=1.0,
        help="Scale phase lengths to match synthetically compacted or stretched worlds.",
    )
    parser.add_argument(
        "--phase-order",
        default="",
        help="Optional comma-separated phase order. Missing phases keep their original order after the listed phases.",
    )
    parser.add_argument(
        "--phase-lengths",
        default="",
        help="Optional comma-separated length overrides, for example rekopplung=1400,randflackern=700.",
    )
    parser.add_argument("--out", required=True)
    parser.add_argument("--csv-out", required=True)
    parser.add_argument("--title", default="Synthetische Phasenrollen")
    args = parser.parse_args()

    phase_rows, phase_roles = build_report(
        Path(args.episodes),
        args.preset,
        args.phase_scale,
        args.phase_order,
        args.phase_lengths,
    )
    write_outputs(phase_rows, phase_roles, Path(args.out), Path(args.csv_out), args.title)
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
