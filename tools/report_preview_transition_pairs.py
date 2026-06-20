from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from statistics import fmean


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "334_PREVIEW_UEBERGANGSPAARE_DIAGNOSE.md"


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


def _dominant(values: list[str]) -> str:
    cleaned = [value for value in values if value and value != "-"]
    if not cleaned:
        return "-"
    value, count = Counter(cleaned).most_common(1)[0]
    return f"{value} ({count}/{len(cleaned)})"


def _collect_world(asset: str, timeframe: str, episodes_path: Path) -> list[dict[str, object]]:
    rows = _load_rows(episodes_path)
    transitions: list[dict[str, object]] = []
    for idx in range(1, len(rows)):
        prev_row = rows[idx - 1]
        cur_row = rows[idx]
        from_preview = _preview(prev_row)
        to_preview = _preview(cur_row)
        if from_preview == to_preview:
            continue
        prev_axes = _axes(prev_row)
        cur_axes = _axes(cur_row)
        transitions.append(
            {
                "asset": asset,
                "timeframe": timeframe,
                "from_preview": from_preview,
                "to_preview": to_preview,
                "pair": f"{from_preview}->{to_preview}",
                "from_role": _role(prev_row),
                "to_role": _role(cur_row),
                "pressure_delta": cur_axes["pressure"] - prev_axes["pressure"],
                "sharpness_delta": cur_axes["sharpness"] - prev_axes["sharpness"],
                "focus_delta": cur_axes["focus"] - prev_axes["focus"],
                "rekopplung_delta": cur_axes["rekopplung"] - prev_axes["rekopplung"],
                "loudness_delta": cur_axes["loudness"] - prev_axes["loudness"],
            }
        )
    return transitions


def _summarize(transitions: list[dict[str, object]], top_n: int) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for item in transitions:
        grouped[str(item["pair"])].append(item)

    pair_rows: list[dict[str, object]] = []
    for pair, items in sorted(grouped.items(), key=lambda entry: len(entry[1]), reverse=True)[:top_n]:
        pair_rows.append(
            {
                "pair": pair,
                "count": len(items),
                "worlds": len({f"{item['asset']}_{item['timeframe']}" for item in items}),
                "dominant_world": _dominant([f"{item['asset']}_{item['timeframe']}" for item in items]),
                "dominant_role_shift": _dominant([f"{item['from_role']}->{item['to_role']}" for item in items]),
                "pressure_delta": _mean([float(item["pressure_delta"]) for item in items]),
                "sharpness_delta": _mean([float(item["sharpness_delta"]) for item in items]),
                "focus_delta": _mean([float(item["focus_delta"]) for item in items]),
                "rekopplung_delta": _mean([float(item["rekopplung_delta"]) for item in items]),
                "loudness_delta": _mean([float(item["loudness_delta"]) for item in items]),
            }
        )

    world_grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for item in transitions:
        world_grouped[(str(item["asset"]), str(item["timeframe"]))].append(item)
    world_rows: list[dict[str, object]] = []
    for (asset, timeframe), items in sorted(world_grouped.items()):
        world_rows.append(
            {
                "asset": asset,
                "timeframe": timeframe,
                "transition_count": len(items),
                "top_pair": _dominant([str(item["pair"]) for item in items]),
                "pressure_delta": _mean([float(item["pressure_delta"]) for item in items]),
                "sharpness_delta": _mean([float(item["sharpness_delta"]) for item in items]),
                "rekopplung_delta": _mean([float(item["rekopplung_delta"]) for item in items]),
            }
        )
    return pair_rows, world_rows


def _write_csv(pair_rows: list[dict[str, object]], world_rows: list[dict[str, object]], out_path: Path) -> None:
    pair_path = out_path.with_suffix(".csv")
    pair_fields = [
        "pair",
        "count",
        "worlds",
        "dominant_world",
        "dominant_role_shift",
        "pressure_delta",
        "sharpness_delta",
        "focus_delta",
        "rekopplung_delta",
        "loudness_delta",
    ]
    pair_path.parent.mkdir(parents=True, exist_ok=True)
    with pair_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=pair_fields)
        writer.writeheader()
        for row in pair_rows:
            writer.writerow(
                {
                    key: _fmt(float(row[key]), 6) if isinstance(row.get(key), float) else row.get(key, "")
                    for key in pair_fields
                }
            )

    world_path = out_path.with_name(out_path.stem + "_worlds.csv")
    world_fields = ["asset", "timeframe", "transition_count", "top_pair", "pressure_delta", "sharpness_delta", "rekopplung_delta"]
    with world_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=world_fields)
        writer.writeheader()
        for row in world_rows:
            writer.writerow(
                {
                    key: _fmt(float(row[key]), 6) if isinstance(row.get(key), float) else row.get(key, "")
                    for key in world_fields
                }
            )


def _write_md(pair_rows: list[dict[str, object]], world_rows: list[dict[str, object]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    _write_csv(pair_rows, world_rows, out_path)

    lines = [
        "# Preview-Uebergangspaare Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose extrahiert konkrete Wechselpaare zwischen MCM-Preview-Familien.",
        "Selbstfortsetzung wird ausgeblendet. Die Diagnose bleibt passiv.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Welche wiederkehrenden Feldbewegungen entstehen zwischen Preview-Familien?",
        "2. Unterpruefung: konkrete Paare und Achsendeltas ueber Assets/Timeframes vergleichen.",
        "3. Folgeschritt: stabile Paare gegen weitere Welten und laengere Laeufe pruefen.",
        "",
        "## Top-Uebergangspaare",
        "",
        "| Paar | Anzahl | Welten | Dominante Welt | Rollenwechsel | dDruck | dSchaerfe | dFokus | dRekopplung | dLautheit |",
        "|---|---:|---:|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in pair_rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["pair"]),
                    str(row["count"]),
                    str(row["worlds"]),
                    str(row["dominant_world"]),
                    str(row["dominant_role_shift"]),
                    _fmt(float(row["pressure_delta"])),
                    _fmt(float(row["sharpness_delta"])),
                    _fmt(float(row["focus_delta"])),
                    _fmt(float(row["rekopplung_delta"])),
                    _fmt(float(row["loudness_delta"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Weltuebersicht",
            "",
            "| Asset | Timeframe | Uebergaenge | Top-Paar | dDruck | dSchaerfe | dRekopplung |",
            "|---|---|---:|---|---:|---:|---:|",
        ]
    )
    for row in world_rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["asset"]),
                    str(row["timeframe"]),
                    str(row["transition_count"]),
                    str(row["top_pair"]),
                    _fmt(float(row["pressure_delta"])),
                    _fmt(float(row["sharpness_delta"])),
                    _fmt(float(row["rekopplung_delta"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Uebergangspaare zeigen die ersten passiven Feldbewegungen zwischen Bedeutungsinseln.",
            "Sie sind nicht als Handlung zu lesen, sondern als Bewegung der Innenfeld-Syntax.",
            "",
            "Wenn ein Paar ueber mehrere Welten wiederkehrt, ist es staerker als eine lokale Einzelkante.",
            "Wenn ein Paar nur in einer Welt dominiert, ist es eher asset- oder timeframe-spezifisch.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes werden die stabilsten Paare fachlich klassifiziert: Grundinsel-Wechsel, Rekopplungsbogen oder Randuebergang.",
            "",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--world", action="append", nargs=3, metavar=("ASSET", "TIMEFRAME", "EPISODES_CSV"), required=True)
    parser.add_argument("--top-n", type=int, default=20)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    transitions: list[dict[str, object]] = []
    for asset, timeframe, path_text in args.world:
        transitions.extend(_collect_world(asset, timeframe, _resolve(path_text)))

    pair_rows, world_rows = _summarize(transitions, args.top_n)
    out = args.out if args.out.is_absolute() else ROOT / args.out
    _write_md(pair_rows, world_rows, out)
    print(f"wrote {out}")
    print(f"wrote {out.with_suffix('.csv')}")
    print(f"wrote {out.with_name(out.stem + '_worlds.csv')}")


if __name__ == "__main__":
    main()
