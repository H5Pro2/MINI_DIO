from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


def _float(row: dict[str, str], key: str) -> float:
    try:
        return float(row.get(key, "") or 0.0)
    except ValueError:
        return 0.0


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = int(round((len(ordered) - 1) * q))
    return ordered[max(0, min(len(ordered) - 1, index))]


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


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _metrics(rows: list[dict[str, str]], prefix: str = "") -> dict[str, float]:
    raw = _avg([_float(row, "perception_raw_field_intake_pressure") for row in rows])
    adapted = _avg([_float(row, "perception_adapted_field_intake_pressure") for row in rows])
    loudness = _avg([_float(row, "perception_auditory_loudness") for row in rows])
    sharpness = _avg([_float(row, "perception_visual_sharpness") for row in rows])
    blur = _avg([_float(row, "perception_visual_blur") for row in rows])
    pressure = _avg([_float(row, "perception_felt_pressure") for row in rows])
    relaxation = _avg([_float(row, "perception_felt_relaxation") for row in rows])
    tension = _avg([_float(row, "mcm_feldwirkung_mcm_tension") for row in rows])
    coherence = _avg([_float(row, "mcm_feldwirkung_mcm_coherence") for row in rows])
    asymmetry = _avg([_float(row, "mcm_feldwirkung_mcm_asymmetry") for row in rows])
    reduction = max(0.0, raw - adapted)
    ratio = adapted / raw if raw > 1e-9 else 0.0
    return {
        f"{prefix}auditory_loudness": round(loudness, 6),
        f"{prefix}visual_sharpness": round(sharpness, 6),
        f"{prefix}visual_blur": round(blur, 6),
        f"{prefix}raw_field_intake": round(raw, 6),
        f"{prefix}adapted_field_intake": round(adapted, 6),
        f"{prefix}intake_reduction": round(reduction, 6),
        f"{prefix}adaptation_ratio": round(ratio, 6),
        f"{prefix}felt_pressure": round(pressure, 6),
        f"{prefix}felt_relaxation": round(relaxation, 6),
        f"{prefix}mcm_tension": round(tension, 6),
        f"{prefix}mcm_coherence": round(coherence, 6),
        f"{prefix}mcm_asymmetry": round(asymmetry, 6),
    }


def _summarize(label: str, path: Path) -> dict[str, object]:
    rows = _load(path)
    roles = Counter(_role(row) for row in rows)
    total = max(1, len(rows))
    raw_values = [_float(row, "perception_raw_field_intake_pressure") for row in rows]
    high_threshold = _percentile(raw_values, 0.90)
    high_rows = [row for row in rows if _float(row, "perception_raw_field_intake_pressure") >= high_threshold]
    high_roles = Counter(_role(row) for row in high_rows)
    high_total = max(1, len(high_rows))
    out: dict[str, object] = {
        "world": label,
        "episodes": len(rows),
        "highload_episodes": len(high_rows),
        "highload_threshold": round(high_threshold, 6),
        "zentrum": round(roles["zentrum_stabil"] / total, 6),
        "offen": round(roles["offene_variante"] / total, 6),
        "rand_kipp": round(roles["spannungsrand_kippnaehe"] / total, 6),
        "rekopplungsnaehe": round(roles["rekopplungsnaehe"] / total, 6),
        "high_zentrum": round(high_roles["zentrum_stabil"] / high_total, 6),
        "high_offen": round(high_roles["offene_variante"] / high_total, 6),
        "high_rand_kipp": round(high_roles["spannungsrand_kippnaehe"] / high_total, 6),
        "high_rekopplungsnaehe": round(high_roles["rekopplungsnaehe"] / high_total, 6),
    }
    out.update(_metrics(rows))
    out.update(_metrics(high_rows, prefix="high_"))
    return out


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
        "Passive Diagnose: echte Weltfolgen gegen Rezeptorachsen und hoechste Rohfeldaufnahme-Fenster.",
        "",
        "## Weltmatrix",
        "",
        "| Welt | Episoden | Zentrum | Offen | Rand/Kipp | Lautheit | Schaerfe | Rohfeld | Adaptfeld | Reduktion | Ratio | High-Offen | High-Rand/Kipp | High-Lautheit | High-Rohfeld | High-Reduktion |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {world} | {episodes} | {zentrum:.4f} | {offen:.4f} | {rand_kipp:.4f} | {auditory_loudness:.4f} | {visual_sharpness:.4f} | {raw_field_intake:.4f} | {adapted_field_intake:.4f} | {intake_reduction:.4f} | {adaptation_ratio:.4f} | {high_offen:.4f} | {high_rand_kipp:.4f} | {high_auditory_loudness:.4f} | {high_raw_field_intake:.4f} | {high_intake_reduction:.4f} |".format(
                **row
            )
        )

    strongest_high_open = max(rows, key=lambda row: float(row["high_offen"]))
    strongest_high_rand = max(rows, key=lambda row: float(row["high_rand_kipp"]))
    strongest_reduction = max(rows, key=lambda row: float(row["high_intake_reduction"]))
    strongest_loudness = max(rows, key=lambda row: float(row["high_auditory_loudness"]))

    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"- Staerkste offene Variante im Hochlastfenster: `{strongest_high_open['world']}` mit `{float(strongest_high_open['high_offen']):.4f}`.",
            f"- Staerkste Rand/Kipp-Naehe im Hochlastfenster: `{strongest_high_rand['world']}` mit `{float(strongest_high_rand['high_rand_kipp']):.4f}`.",
            f"- Staerkste auditive Hochlast: `{strongest_loudness['world']}` mit `{float(strongest_loudness['high_auditory_loudness']):.4f}`.",
            f"- Staerkste Adaptionsreduktion im Hochlastfenster: `{strongest_reduction['world']}` mit `{float(strongest_reduction['high_intake_reduction']):.4f}`.",
            "",
            "## Ableitung",
            "",
            "Die echte Weltpruefung trennt zwei Fragen: Wie klingt und wirkt die Welt insgesamt, und was passiert in den lautesten/rohesten Feldaufnahme-Fenstern?",
            "",
            "Wenn Hochlastfenster offen oder randnaher werden, aber die adaptierte Feldaufnahme unter der Rohaufnahme bleibt, spricht das fuer dieselbe organische Aufnahmegrenze wie in den synthetischen Welten.",
            "",
            "Wie es weitergeht: Die Weltmatrix sollte gegen die synthetische Limit-Synthese gelesen werden. Danach kann entschieden werden, ob die Rezeptoradaptation stabil genug als Kernmechanik dokumentiert ist.",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _parse_world(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("world must be LABEL=PATH")
    label, path = value.split("=", 1)
    return label, Path(path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--world", action="append", required=True, type=_parse_world)
    parser.add_argument("--out", required=True)
    parser.add_argument("--csv-out", required=True)
    parser.add_argument("--title", default="Rezeptorachsen-Weltvergleich")
    args = parser.parse_args()

    rows = [_summarize(label, path) for label, path in args.world]
    _write_csv(rows, Path(args.csv_out))
    _write_markdown(rows, Path(args.out), args.title)
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
