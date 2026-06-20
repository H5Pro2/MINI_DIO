from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from statistics import fmean


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "332_PREVIEW_FAMILIEN_NACHBARSCHAFT_DIAGNOSE.md"
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


def _fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"


def _mean(values: list[float]) -> float:
    return fmean(values) if values else 0.0


def _load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    return sorted(rows, key=lambda row: int(_float(row.get("tick"))))


def _role(row: dict[str, str]) -> str:
    effect_class = str(row.get("passive_mcm_effect_class", "-") or "-")
    awareness = str(row.get("passive_inner_effect_awareness_state", "-") or "-")
    if effect_class == "stabil" or awareness == "inner_effect_stable":
        return "zentrum_stabil"
    if effect_class in {"kippend", "gespannt"}:
        return "spannungsrand_kippnaehe"
    if effect_class in {"tragend_unruhig", "diffus"}:
        return "offene_variante"
    return "unbestimmt"


def _axes(row: dict[str, str]) -> dict[str, float]:
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

    distance = max(0.0, min(1.0, (visual_gap + hearing_gap + max(0.0, 1.0 - contact_alignment)) / 3.0))
    focus = max(0.0, min(1.0, ((visual_contact + auditory_contact + contact_alignment) / 3.0) * (1.0 - distance * 0.35)))
    loudness = max(0.0, min(1.0, (hearing_tone + hearing_shift) / 2.0))
    sharpness = max(0.0, min(1.0, (form_stability + max(0.0, 1.0 - form_change)) / 2.0))
    pressure = max(0.0, min(1.0, (contact_pressure + strain + max(0.0, 1.0 - rekopplung)) / 3.0))
    relaxation = max(0.0, min(1.0, (rekopplung + contact_alignment + max(0.0, 1.0 - strain)) / 3.0))
    return {
        "focus": focus,
        "distance": distance,
        "loudness": loudness,
        "sharpness": sharpness,
        "pressure": pressure,
        "relaxation": relaxation,
        "rekopplung": rekopplung,
        "strain": strain,
    }


def _dominant(counter: Counter[str]) -> str:
    if not counter:
        return "-"
    value, count = counter.most_common(1)[0]
    total = sum(counter.values())
    return f"{value} ({count}/{total})"


def _summarize_world(asset: str, timeframe: str, episodes_path: Path, targets: set[str]) -> list[dict[str, object]]:
    rows = _load_rows(episodes_path)
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)

    for idx, row in enumerate(rows):
        preview = row.get("mcm_field_episode_preview_symbol", "-") or "-"
        if preview not in targets:
            continue
        prev_row = rows[idx - 1] if idx > 0 else None
        next_row = rows[idx + 1] if idx + 1 < len(rows) else None
        current_axes = _axes(row)
        prev_axes = _axes(prev_row) if prev_row is not None else {}
        next_axes = _axes(next_row) if next_row is not None else {}
        grouped[preview].append(
            {
                "prev_preview": prev_row.get("mcm_field_episode_preview_symbol", "-") if prev_row else "-",
                "next_preview": next_row.get("mcm_field_episode_preview_symbol", "-") if next_row else "-",
                "current_role": _role(row),
                "prev_role": _role(prev_row) if prev_row else "-",
                "next_role": _role(next_row) if next_row else "-",
                "focus_delta_prev": current_axes.get("focus", 0.0) - prev_axes.get("focus", current_axes.get("focus", 0.0)),
                "focus_delta_next": next_axes.get("focus", current_axes.get("focus", 0.0)) - current_axes.get("focus", 0.0),
                "pressure_delta_prev": current_axes.get("pressure", 0.0) - prev_axes.get("pressure", current_axes.get("pressure", 0.0)),
                "pressure_delta_next": next_axes.get("pressure", current_axes.get("pressure", 0.0)) - current_axes.get("pressure", 0.0),
                "sharpness_delta_prev": current_axes.get("sharpness", 0.0) - prev_axes.get("sharpness", current_axes.get("sharpness", 0.0)),
                "sharpness_delta_next": next_axes.get("sharpness", current_axes.get("sharpness", 0.0)) - current_axes.get("sharpness", 0.0),
                "rekopplung_delta_next": next_axes.get("rekopplung", current_axes.get("rekopplung", 0.0)) - current_axes.get("rekopplung", 0.0),
            }
        )

    result: list[dict[str, object]] = []
    for preview in sorted(targets):
        items = grouped.get(preview, [])
        prev_counter = Counter(str(item["prev_preview"]) for item in items if str(item["prev_preview"]) != "-")
        next_counter = Counter(str(item["next_preview"]) for item in items if str(item["next_preview"]) != "-")
        role_counter = Counter(str(item["current_role"]) for item in items)
        result.append(
            {
                "asset": asset,
                "timeframe": timeframe,
                "preview": preview,
                "count": len(items),
                "dominant_prev": _dominant(prev_counter),
                "dominant_next": _dominant(next_counter),
                "dominant_role": _dominant(role_counter),
                "prev_self_share": prev_counter.get(preview, 0) / max(1, sum(prev_counter.values())),
                "next_self_share": next_counter.get(preview, 0) / max(1, sum(next_counter.values())),
                "focus_delta_prev": _mean([float(item["focus_delta_prev"]) for item in items]),
                "focus_delta_next": _mean([float(item["focus_delta_next"]) for item in items]),
                "pressure_delta_prev": _mean([float(item["pressure_delta_prev"]) for item in items]),
                "pressure_delta_next": _mean([float(item["pressure_delta_next"]) for item in items]),
                "sharpness_delta_prev": _mean([float(item["sharpness_delta_prev"]) for item in items]),
                "sharpness_delta_next": _mean([float(item["sharpness_delta_next"]) for item in items]),
                "rekopplung_delta_next": _mean([float(item["rekopplung_delta_next"]) for item in items]),
            }
        )
    return result


def _write_csv(rows: list[dict[str, object]], out_path: Path) -> None:
    fields = [
        "asset",
        "timeframe",
        "preview",
        "count",
        "dominant_prev",
        "dominant_next",
        "dominant_role",
        "prev_self_share",
        "next_self_share",
        "focus_delta_prev",
        "focus_delta_next",
        "pressure_delta_prev",
        "pressure_delta_next",
        "sharpness_delta_prev",
        "sharpness_delta_next",
        "rekopplung_delta_next",
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

    result: list[dict[str, object]] = []
    for preview, items in grouped.items():
        total = sum(int(item["count"]) for item in items)
        prev_counts: Counter[str] = Counter()
        next_counts: Counter[str] = Counter()
        role_counts: Counter[str] = Counter()
        for item in items:
            prev_name = str(item["dominant_prev"]).split(" (", 1)[0]
            next_name = str(item["dominant_next"]).split(" (", 1)[0]
            role_name = str(item["dominant_role"]).split(" (", 1)[0]
            if prev_name != "-":
                prev_counts[prev_name] += int(item["count"])
            if next_name != "-":
                next_counts[next_name] += int(item["count"])
            if role_name != "-":
                role_counts[role_name] += int(item["count"])
        result.append(
            {
                "preview": preview,
                "count": total,
                "dominant_prev": _dominant(prev_counts),
                "dominant_next": _dominant(next_counts),
                "dominant_role": _dominant(role_counts),
                "prev_self_share": _mean([float(item["prev_self_share"]) for item in items]),
                "next_self_share": _mean([float(item["next_self_share"]) for item in items]),
                "focus_delta_prev": sum(float(item["focus_delta_prev"]) * int(item["count"]) for item in items) / max(1, total),
                "focus_delta_next": sum(float(item["focus_delta_next"]) * int(item["count"]) for item in items) / max(1, total),
                "pressure_delta_prev": sum(float(item["pressure_delta_prev"]) * int(item["count"]) for item in items) / max(1, total),
                "pressure_delta_next": sum(float(item["pressure_delta_next"]) * int(item["count"]) for item in items) / max(1, total),
                "sharpness_delta_prev": sum(float(item["sharpness_delta_prev"]) * int(item["count"]) for item in items) / max(1, total),
                "sharpness_delta_next": sum(float(item["sharpness_delta_next"]) * int(item["count"]) for item in items) / max(1, total),
                "rekopplung_delta_next": sum(float(item["rekopplung_delta_next"]) * int(item["count"]) for item in items) / max(1, total),
            }
        )
    return sorted(result, key=lambda row: str(row["preview"]))


def _write_md(rows: list[dict[str, object]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    _write_csv(rows, out_path)
    aggregated = _aggregate(rows)

    lines = [
        "# Preview-Familien Nachbarschaft Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft, welche MCM-Preview-Familien direkt vor und nach zentralen Familien liegen.",
        "Sie bleibt passiv: keine Handlung, kein Gate, kein Entry-Signal.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Unterscheiden sich Familien eher durch Nachbarschaft als durch grobe Regulationsklasse?",
        "2. Unterpruefung: dominante Vor-/Nach-Familie, Selbstnaehte und lokale Achsendeltas.",
        "3. Folgeschritt: stabile Uebergangspaare gegen weitere Welten pruefen.",
        "",
        "## Aggregat",
        "",
        "| MCM-Preview | Anzahl | Rolle | Davor | Danach | Selbst davor | Selbst danach | dFokus vorher | dFokus nachher | dDruck vorher | dDruck nachher | dSchaerfe vorher | dSchaerfe nachher | dRekopplung nachher |",
        "|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in aggregated:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["preview"]),
                    str(row["count"]),
                    str(row["dominant_role"]),
                    str(row["dominant_prev"]),
                    str(row["dominant_next"]),
                    _fmt(float(row["prev_self_share"])),
                    _fmt(float(row["next_self_share"])),
                    _fmt(float(row["focus_delta_prev"])),
                    _fmt(float(row["focus_delta_next"])),
                    _fmt(float(row["pressure_delta_prev"])),
                    _fmt(float(row["pressure_delta_next"])),
                    _fmt(float(row["sharpness_delta_prev"])),
                    _fmt(float(row["sharpness_delta_next"])),
                    _fmt(float(row["rekopplung_delta_next"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Asset-/Timeframe-Matrix",
            "",
            "| Asset | Timeframe | MCM-Preview | Anzahl | Davor | Danach | Selbst davor | Selbst danach | dDruck nachher | dSchaerfe nachher |",
            "|---|---|---|---:|---|---|---:|---:|---:|---:|",
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
                    str(row["dominant_prev"]),
                    str(row["dominant_next"]),
                    _fmt(float(row["prev_self_share"])),
                    _fmt(float(row["next_self_share"])),
                    _fmt(float(row["pressure_delta_next"])),
                    _fmt(float(row["sharpness_delta_next"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Nachbarschaftspruefung zeigt, ob eine Familie eher als durchlaufende Grundnaehe oder als Uebergangsknoten wirkt.",
            "",
            "Hohe Selbstanteile vor und nach einer Familie sprechen fuer eine laengere Insel oder stabile Feldzone. Niedrigere Selbstanteile und klare Fremd-Nachbarn sprechen fuer Bruecken- oder Uebergangsfunktion.",
            "",
            "Die Achsendeltas sind absichtlich klein gelesen. Entscheidend ist nicht ein einzelner Sprung, sondern ob Druck, Schaerfe oder Rekopplung wiederholt beim Eintritt oder Austritt der Familie kippen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes werden aus dieser Matrix stabile Uebergangspaare extrahiert, also wiederkehrende Folgen wie Familie A -> Familie B mit aehnlicher Feldwirkung.",
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
