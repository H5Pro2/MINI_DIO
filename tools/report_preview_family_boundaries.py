from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from statistics import fmean


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "333_PREVIEW_FAMILIEN_BOUNDARY_DIAGNOSE.md"
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


def _preview(row: dict[str, str] | None) -> str:
    if row is None:
        return "-"
    return row.get("mcm_field_episode_preview_symbol", "-") or "-"


def _role(row: dict[str, str] | None) -> str:
    if row is None:
        return "-"
    effect_class = str(row.get("passive_mcm_effect_class", "-") or "-")
    awareness = str(row.get("passive_inner_effect_awareness_state", "-") or "-")
    if effect_class == "stabil" or awareness == "inner_effect_stable":
        return "zentrum_stabil"
    if effect_class in {"kippend", "gespannt"}:
        return "spannungsrand_kippnaehe"
    if effect_class in {"tragend_unruhig", "diffus"}:
        return "offene_variante"
    return "unbestimmt"


def _axes(row: dict[str, str] | None) -> dict[str, float]:
    if row is None:
        return {}
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
    transitions: dict[str, list[dict[str, object]]] = defaultdict(list)

    for idx in range(1, len(rows)):
        prev_row = rows[idx - 1]
        cur_row = rows[idx]
        prev_preview = _preview(prev_row)
        cur_preview = _preview(cur_row)
        if prev_preview == cur_preview:
            continue

        prev_axes = _axes(prev_row)
        cur_axes = _axes(cur_row)

        if cur_preview in targets:
            transitions[cur_preview].append(
                {
                    "direction": "entry",
                    "other": prev_preview,
                    "from_role": _role(prev_row),
                    "to_role": _role(cur_row),
                    "focus_delta": cur_axes["focus"] - prev_axes["focus"],
                    "pressure_delta": cur_axes["pressure"] - prev_axes["pressure"],
                    "sharpness_delta": cur_axes["sharpness"] - prev_axes["sharpness"],
                    "rekopplung_delta": cur_axes["rekopplung"] - prev_axes["rekopplung"],
                }
            )
        if prev_preview in targets:
            transitions[prev_preview].append(
                {
                    "direction": "exit",
                    "other": cur_preview,
                    "from_role": _role(prev_row),
                    "to_role": _role(cur_row),
                    "focus_delta": cur_axes["focus"] - prev_axes["focus"],
                    "pressure_delta": cur_axes["pressure"] - prev_axes["pressure"],
                    "sharpness_delta": cur_axes["sharpness"] - prev_axes["sharpness"],
                    "rekopplung_delta": cur_axes["rekopplung"] - prev_axes["rekopplung"],
                }
            )

    result: list[dict[str, object]] = []
    for preview in sorted(targets):
        items = transitions.get(preview, [])
        entries = [item for item in items if item["direction"] == "entry"]
        exits = [item for item in items if item["direction"] == "exit"]
        result.append(
            {
                "asset": asset,
                "timeframe": timeframe,
                "preview": preview,
                "boundary_count": len(items),
                "entry_count": len(entries),
                "exit_count": len(exits),
                "dominant_entry_from": _dominant(Counter(str(item["other"]) for item in entries if item["other"] != "-")),
                "dominant_exit_to": _dominant(Counter(str(item["other"]) for item in exits if item["other"] != "-")),
                "dominant_entry_role": _dominant(Counter(f"{item['from_role']}->{item['to_role']}" for item in entries)),
                "dominant_exit_role": _dominant(Counter(f"{item['from_role']}->{item['to_role']}" for item in exits)),
                "entry_pressure_delta": _mean([float(item["pressure_delta"]) for item in entries]),
                "exit_pressure_delta": _mean([float(item["pressure_delta"]) for item in exits]),
                "entry_sharpness_delta": _mean([float(item["sharpness_delta"]) for item in entries]),
                "exit_sharpness_delta": _mean([float(item["sharpness_delta"]) for item in exits]),
                "entry_rekopplung_delta": _mean([float(item["rekopplung_delta"]) for item in entries]),
                "exit_rekopplung_delta": _mean([float(item["rekopplung_delta"]) for item in exits]),
            }
        )
    return result


def _write_csv(rows: list[dict[str, object]], out_path: Path) -> None:
    fields = [
        "asset",
        "timeframe",
        "preview",
        "boundary_count",
        "entry_count",
        "exit_count",
        "dominant_entry_from",
        "dominant_exit_to",
        "dominant_entry_role",
        "dominant_exit_role",
        "entry_pressure_delta",
        "exit_pressure_delta",
        "entry_sharpness_delta",
        "exit_sharpness_delta",
        "entry_rekopplung_delta",
        "exit_rekopplung_delta",
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
        grouped[str(row["preview"])].append(row)

    result: list[dict[str, object]] = []
    for preview, items in grouped.items():
        total_boundaries = sum(int(item["boundary_count"]) for item in items)
        total_entries = sum(int(item["entry_count"]) for item in items)
        total_exits = sum(int(item["exit_count"]) for item in items)
        entry_from = Counter()
        exit_to = Counter()
        for item in items:
            source = str(item["dominant_entry_from"]).split(" (", 1)[0]
            target = str(item["dominant_exit_to"]).split(" (", 1)[0]
            if source != "-":
                entry_from[source] += int(item["entry_count"])
            if target != "-":
                exit_to[target] += int(item["exit_count"])
        result.append(
            {
                "preview": preview,
                "boundary_count": total_boundaries,
                "entry_count": total_entries,
                "exit_count": total_exits,
                "dominant_entry_from": _dominant(entry_from),
                "dominant_exit_to": _dominant(exit_to),
                "entry_pressure_delta": sum(float(item["entry_pressure_delta"]) * int(item["entry_count"]) for item in items) / max(1, total_entries),
                "exit_pressure_delta": sum(float(item["exit_pressure_delta"]) * int(item["exit_count"]) for item in items) / max(1, total_exits),
                "entry_sharpness_delta": sum(float(item["entry_sharpness_delta"]) * int(item["entry_count"]) for item in items) / max(1, total_entries),
                "exit_sharpness_delta": sum(float(item["exit_sharpness_delta"]) * int(item["exit_count"]) for item in items) / max(1, total_exits),
                "entry_rekopplung_delta": sum(float(item["entry_rekopplung_delta"]) * int(item["entry_count"]) for item in items) / max(1, total_entries),
                "exit_rekopplung_delta": sum(float(item["exit_rekopplung_delta"]) * int(item["exit_count"]) for item in items) / max(1, total_exits),
            }
        )
    return sorted(result, key=lambda row: str(row["preview"]))


def _write_md(rows: list[dict[str, object]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    _write_csv(rows, out_path)
    aggregated = _aggregate(rows)

    lines = [
        "# Preview-Familien Boundary Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest nur echte Wechselkanten zwischen MCM-Preview-Familien.",
        "Selbstfortsetzung wird bewusst ausgeblendet.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Welche Familien bilden echte Uebergangskanten?",
        "2. Unterpruefung: Eintritt/Austritt und Achsendeltas ohne Selbstfortsetzung.",
        "3. Folgeschritt: stabile Uebergangspaare als passive Feldbewegung pruefen.",
        "",
        "## Aggregat",
        "",
        "| MCM-Preview | Boundaries | Entries | Exits | Eintritt von | Austritt zu | dDruck Eintritt | dDruck Austritt | dSchaerfe Eintritt | dSchaerfe Austritt | dRekopplung Eintritt | dRekopplung Austritt |",
        "|---|---:|---:|---:|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in aggregated:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["preview"]),
                    str(row["boundary_count"]),
                    str(row["entry_count"]),
                    str(row["exit_count"]),
                    str(row["dominant_entry_from"]),
                    str(row["dominant_exit_to"]),
                    _fmt(float(row["entry_pressure_delta"])),
                    _fmt(float(row["exit_pressure_delta"])),
                    _fmt(float(row["entry_sharpness_delta"])),
                    _fmt(float(row["exit_sharpness_delta"])),
                    _fmt(float(row["entry_rekopplung_delta"])),
                    _fmt(float(row["exit_rekopplung_delta"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Detailmatrix",
            "",
            "| Asset | Timeframe | MCM-Preview | Boundaries | Eintritt von | Austritt zu | dDruck Eintritt | dDruck Austritt | dSchaerfe Eintritt | dSchaerfe Austritt |",
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
                    str(row["boundary_count"]),
                    str(row["dominant_entry_from"]),
                    str(row["dominant_exit_to"]),
                    _fmt(float(row["entry_pressure_delta"])),
                    _fmt(float(row["exit_pressure_delta"])),
                    _fmt(float(row["entry_sharpness_delta"])),
                    _fmt(float(row["exit_sharpness_delta"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Boundary-Diagnose trennt stabile Insel von echter Kante. Dadurch wird sichtbar, ob eine Familie nur lange bei sich bleibt oder ob sie wiederkehrende Uebergaenge zu anderen Familien bildet.",
            "",
            "Kleine Achsendeltas sind hier nicht automatisch unwichtig. Wenn sie an echten Kanten wiederholt gleichgerichtet auftreten, koennen sie eine passive Feldbewegung anzeigen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes werden die haeufigsten konkreten Uebergangspaare extrahiert, nicht nur Eintritt/Austritt pro Ziel-Familie.",
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
