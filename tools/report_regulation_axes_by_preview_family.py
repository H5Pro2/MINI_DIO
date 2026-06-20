from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from statistics import fmean


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "331_PREVIEW_FAMILIEN_REGULATIONSACHSEN_PROFIL.md"
DEFAULT_TARGETS = [
    "dio_mcm_episode_1t5bcxp",
    "dio_mcm_episode_0y50lf3",
    "dio_mcm_episode_183drjy",
]


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    if result != result:
        return 0.0
    return result


def _clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def _mean(values: list[float]) -> float:
    return fmean(values) if values else 0.0


def _fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"


def _load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _row_axes(row: dict[str, str]) -> dict[str, float]:
    visual_gap = _float(row.get("mcm_visual_field_gap"))
    hearing_gap = _float(row.get("mcm_hearing_field_gap"))
    contact_alignment = _float(row.get("rezeptor_contact_alignment"))
    visual_contact = _float(row.get("rezeptor_visual_contact"))
    auditory_contact = _float(row.get("rezeptor_auditory_contact"))

    hearing_tone = abs(_float(row.get("hoeren_energy_tone")))
    hearing_shift = abs(_float(row.get("hoeren_energy_shift")))

    form_stability = _float(row.get("sehen_form_stability"))
    form_change = abs(_float(row.get("sehen_form_change")))

    contact_pressure = _float(row.get("rezeptor_contact_pressure"))
    strain = _float(row.get("mcm_strain_quality"))
    rekopplung = _float(row.get("mcm_rekopplung_quality"))

    distance = _clamp((visual_gap + hearing_gap + max(0.0, 1.0 - contact_alignment)) / 3.0)
    focus = _clamp(((visual_contact + auditory_contact + contact_alignment) / 3.0) * (1.0 - (distance * 0.35)))
    loudness = _clamp((hearing_tone + hearing_shift) / 2.0)
    sharpness = _clamp((form_stability + max(0.0, 1.0 - form_change)) / 2.0)
    pressure = _clamp((contact_pressure + strain + max(0.0, 1.0 - rekopplung)) / 3.0)
    relaxation = _clamp((rekopplung + contact_alignment + max(0.0, 1.0 - strain)) / 3.0)

    return {
        "focus": focus,
        "distance": distance,
        "loudness": loudness,
        "quietness": _clamp(1.0 - loudness),
        "sharpness": sharpness,
        "blur": _clamp(1.0 - sharpness),
        "pressure": pressure,
        "relaxation": relaxation,
        "rekopplung": rekopplung,
        "strain": strain,
        "contact_alignment": contact_alignment,
        "visual_gap": visual_gap,
        "hearing_gap": hearing_gap,
    }


def _axis_label(summary: dict[str, float]) -> str:
    focus_part = "nah" if summary["focus"] >= summary["distance"] else "abstand"
    sound_part = "laut" if summary["loudness"] >= summary["quietness"] else "leise"
    visual_part = "scharf" if summary["sharpness"] >= summary["blur"] else "unscharf"
    field_part = "entspannend" if summary["relaxation"] >= summary["pressure"] else "druckvoll"
    return f"{focus_part}_{sound_part}_{visual_part}_{field_part}"


def _summarize_group(asset: str, timeframe: str, preview: str, rows: list[dict[str, str]]) -> dict[str, object]:
    axes = [_row_axes(row) for row in rows]
    summary = {
        "asset": asset,
        "timeframe": timeframe,
        "preview": preview,
        "count": len(rows),
        "focus": _mean([item["focus"] for item in axes]),
        "distance": _mean([item["distance"] for item in axes]),
        "loudness": _mean([item["loudness"] for item in axes]),
        "quietness": _mean([item["quietness"] for item in axes]),
        "sharpness": _mean([item["sharpness"] for item in axes]),
        "blur": _mean([item["blur"] for item in axes]),
        "pressure": _mean([item["pressure"] for item in axes]),
        "relaxation": _mean([item["relaxation"] for item in axes]),
        "rekopplung": _mean([item["rekopplung"] for item in axes]),
        "strain": _mean([item["strain"] for item in axes]),
        "contact_alignment": _mean([item["contact_alignment"] for item in axes]),
        "visual_gap": _mean([item["visual_gap"] for item in axes]),
        "hearing_gap": _mean([item["hearing_gap"] for item in axes]),
    }
    summary["regulation_profile"] = _axis_label(summary)
    return summary


def _summarize_world(asset: str, timeframe: str, episodes_path: Path, targets: set[str]) -> list[dict[str, object]]:
    rows = _load_rows(episodes_path)
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        preview = row.get("mcm_field_episode_preview_symbol", "-") or "-"
        if preview in targets:
            grouped[preview].append(row)

    summaries: list[dict[str, object]] = []
    for preview in sorted(targets):
        items = grouped.get(preview, [])
        if not items:
            summaries.append(
                {
                    "asset": asset,
                    "timeframe": timeframe,
                    "preview": preview,
                    "count": 0,
                    "focus": 0.0,
                    "distance": 0.0,
                    "loudness": 0.0,
                    "quietness": 0.0,
                    "sharpness": 0.0,
                    "blur": 0.0,
                    "pressure": 0.0,
                    "relaxation": 0.0,
                    "rekopplung": 0.0,
                    "strain": 0.0,
                    "contact_alignment": 0.0,
                    "visual_gap": 0.0,
                    "hearing_gap": 0.0,
                    "regulation_profile": "nicht_gesehen",
                }
            )
            continue
        summaries.append(_summarize_group(asset, timeframe, preview, items))
    return summaries


def _write_csv(rows: list[dict[str, object]], out_path: Path) -> None:
    fields = [
        "asset",
        "timeframe",
        "preview",
        "count",
        "regulation_profile",
        "focus",
        "distance",
        "loudness",
        "quietness",
        "sharpness",
        "blur",
        "pressure",
        "relaxation",
        "rekopplung",
        "strain",
        "contact_alignment",
        "visual_gap",
        "hearing_gap",
    ]
    csv_path = out_path.with_suffix(".csv")
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    key: _fmt(float(row[key]), 6) if isinstance(row.get(key), float) else row.get(key, "")
                    for key in fields
                }
            )


def _aggregate(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        if int(row["count"]) > 0:
            grouped[str(row["preview"])].append(row)

    aggregated: list[dict[str, object]] = []
    for preview, items in grouped.items():
        total_count = sum(int(item["count"]) for item in items)
        result = {"preview": preview, "count": total_count}
        for key in ["focus", "distance", "loudness", "quietness", "sharpness", "blur", "pressure", "relaxation", "rekopplung", "strain"]:
            result[key] = sum(float(item[key]) * int(item["count"]) for item in items) / max(1, total_count)
        result["regulation_profile"] = _axis_label(result)  # type: ignore[arg-type]
        aggregated.append(result)
    return sorted(aggregated, key=lambda item: str(item["preview"]))


def _write_md(rows: list[dict[str, object]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    _write_csv(rows, out_path)
    aggregated = _aggregate(rows)

    lines = [
        "# Preview-Familien Regulationsachsen Profil",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest passive Regulationsachsen fuer zentrale MCM-Preview-Familien.",
        "Sie prueft nicht Handlung, sondern Wahrnehmungs-Einstellung.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Tragen MCM-Preview-Familien unterschiedliche Wahrnehmungs-Einstellungen?",
        "2. Unterpruefung: Fokus/Abstand, lauter/leiser, scharf/unscharf und Druck/Entspannung je Familie vergleichen.",
        "3. Folgeschritt: Nachbarschaften der Familien pruefen.",
        "",
        "## Achsenableitung",
        "",
        "- Fokus/Abstand: Rezeptorkontakt, Kontaktpassung und Sinnes-Feld-Gaps.",
        "- Lauter/Leiser: Hoerenergie und Hoerverschiebung.",
        "- Scharf/Unscharf: Formstabilitaet gegen Formwechsel.",
        "- Druck/Entspannung: Kontaktdruck, Strain, Rekopplung und Kontaktpassung.",
        "",
        "Diese Ableitung ist diagnostisch. Sie ist keine Runtime-Regel.",
        "",
        "## Familien-Aggregat",
        "",
        "| MCM-Preview | Anzahl | Profil | Fokus | Abstand | Laut | Leise | Scharf | Unscharf | Druck | Entspannung | Rekopplung | Strain |",
        "|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in aggregated:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["preview"]),
                    str(row["count"]),
                    str(row["regulation_profile"]),
                    _fmt(float(row["focus"])),
                    _fmt(float(row["distance"])),
                    _fmt(float(row["loudness"])),
                    _fmt(float(row["quietness"])),
                    _fmt(float(row["sharpness"])),
                    _fmt(float(row["blur"])),
                    _fmt(float(row["pressure"])),
                    _fmt(float(row["relaxation"])),
                    _fmt(float(row["rekopplung"])),
                    _fmt(float(row["strain"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Asset-/Timeframe-Matrix",
            "",
            "| Asset | Timeframe | MCM-Preview | Anzahl | Profil | Fokus | Abstand | Laut | Scharf | Druck | Entspannung |",
            "|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["asset"]),
                    str(row["timeframe"]),
                    str(row["preview"]),
                    str(row["count"]),
                    str(row["regulation_profile"]),
                    _fmt(float(row["focus"])),
                    _fmt(float(row["distance"])),
                    _fmt(float(row["loudness"])),
                    _fmt(float(row["sharpness"])),
                    _fmt(float(row["pressure"])),
                    _fmt(float(row["relaxation"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die drei geprueften MCM-Preview-Familien liegen nicht in voellig getrennten Regulationswelten. Sie teilen eine stark rekoppelnde Grundlage, unterscheiden sich aber in Schwerpunkt und Streuung.",
            "",
            "`dio_mcm_episode_1t5bcxp` traegt die breiteste und haeufigste Grundfamilie. Sie wirkt in dieser Diagnose ueberwiegend nah, leise, scharf und entspannend.",
            "",
            "`dio_mcm_episode_0y50lf3` und `dio_mcm_episode_183drjy` wirken ebenfalls rekoppelnd, koennen aber je nach Asset/Timeframe andere Gewichte aufnehmen. Genau diese Unterschiede sind fuer die naechste Nachbarschaftspruefung relevant.",
            "",
            "Wichtig: Die Profile beschreiben Aufnahmequalitaet. Sie sind keine Befehle und keine Regeln.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes werden die Nachbarschaften der drei Familien geprueft: Welche Familien liegen davor und danach, und kippt dabei Fokus, Druck oder Schaerfe?",
            "",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--world", action="append", nargs=3, metavar=("ASSET", "TIMEFRAME", "EPISODES_CSV"), required=True)
    parser.add_argument("--target", action="append", default=[])
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    targets = set(args.target or DEFAULT_TARGETS)
    rows: list[dict[str, object]] = []
    for asset, timeframe, path_text in args.world:
        rows.extend(_summarize_world(asset, timeframe, _resolve(path_text), targets))

    out = args.out if args.out.is_absolute() else ROOT / args.out
    _write_md(rows, out)
    print(f"wrote {out}")
    print(f"wrote {out.with_suffix('.csv')}")


if __name__ == "__main__":
    main()
