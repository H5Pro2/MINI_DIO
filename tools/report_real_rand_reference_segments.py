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


def _timestamp(row: dict[str, str]) -> int:
    return int(float(row.get("timestamp_ms", "0") or 0))


def _tick(row: dict[str, str]) -> int:
    return int(float(row.get("tick", "0") or 0))


def _segments(rows: list[dict[str, str]], raw_threshold: float, context: int) -> list[list[dict[str, str]]]:
    focus_indices = [
        idx
        for idx, row in enumerate(rows)
        if _float(row, "perception_raw_field_intake_pressure") >= raw_threshold and _role(row) != "zentrum_stabil"
    ]
    if not focus_indices:
        return []

    grouped: list[list[int]] = []
    current: list[int] = [focus_indices[0]]
    for idx in focus_indices[1:]:
        if idx - current[-1] <= 1:
            current.append(idx)
        else:
            grouped.append(current)
            current = [idx]
    grouped.append(current)

    output: list[list[dict[str, str]]] = []
    for indices in grouped:
        start = max(0, indices[0] - context)
        end = min(len(rows) - 1, indices[-1] + context)
        output.append(rows[start : end + 1])
    return output


def _candle_features(candles: list[dict[str, str]]) -> dict[str, float]:
    if not candles:
        return {
            "price_drift": 0.0,
            "abs_price_drift": 0.0,
            "max_range_pct": 0.0,
            "avg_range_pct": 0.0,
            "avg_volume": 0.0,
            "max_volume": 0.0,
            "direction_change_ratio": 0.0,
        }
    closes = [_float(row, "close") for row in candles]
    ranges = [
        ((_float(row, "high") - _float(row, "low")) / max(1e-12, _float(row, "close")))
        for row in candles
    ]
    volumes = [_float(row, "volume") for row in candles]
    returns = [
        (closes[idx] - closes[idx - 1]) / max(1e-12, closes[idx - 1])
        for idx in range(1, len(closes))
    ]
    direction_changes = sum(1 for idx in range(1, len(returns)) if returns[idx] * returns[idx - 1] < 0)
    drift = (closes[-1] - closes[0]) / max(1e-12, closes[0])
    return {
        "price_drift": drift,
        "abs_price_drift": abs(drift),
        "max_range_pct": max(ranges) if ranges else 0.0,
        "avg_range_pct": _avg(ranges),
        "avg_volume": _avg(volumes),
        "max_volume": max(volumes) if volumes else 0.0,
        "direction_change_ratio": direction_changes / max(1, len(returns) - 1),
    }


def _summarize_segment(index: int, rows: list[dict[str, str]], candle_by_ts: dict[int, dict[str, str]]) -> dict[str, object]:
    roles = Counter(_role(row) for row in rows)
    total = max(1, len(rows))
    candles = [candle_by_ts[_timestamp(row)] for row in rows if _timestamp(row) in candle_by_ts]
    candle = _candle_features(candles)
    families = Counter(row.get("symbol_family", "-") or "-" for row in rows)
    previews = Counter(row.get("mcm_field_episode_preview_symbol", "-") or "-" for row in rows)

    out: dict[str, object] = {
        "segment": index,
        "start_tick": _tick(rows[0]),
        "end_tick": _tick(rows[-1]),
        "episodes": len(rows),
        "zentrum": round(roles["zentrum_stabil"] / total, 6),
        "offen": round(roles["offene_variante"] / total, 6),
        "rand_kipp": round(roles["spannungsrand_kippnaehe"] / total, 6),
        "rekopplungsnaehe": round(roles["rekopplungsnaehe"] / total, 6),
        "avg_raw_field": round(_avg([_float(row, "perception_raw_field_intake_pressure") for row in rows]), 6),
        "max_raw_field": round(max(_float(row, "perception_raw_field_intake_pressure") for row in rows), 6),
        "avg_adapted_field": round(_avg([_float(row, "perception_adapted_field_intake_pressure") for row in rows]), 6),
        "avg_reduction": round(
            _avg(
                [
                    max(
                        0.0,
                        _float(row, "perception_raw_field_intake_pressure")
                        - _float(row, "perception_adapted_field_intake_pressure"),
                    )
                    for row in rows
                ]
            ),
            6,
        ),
        "avg_loudness": round(_avg([_float(row, "perception_auditory_loudness") for row in rows]), 6),
        "max_loudness": round(max(_float(row, "perception_auditory_loudness") for row in rows), 6),
        "avg_visual_sharpness": round(_avg([_float(row, "perception_visual_sharpness") for row in rows]), 6),
        "avg_visual_blur": round(_avg([_float(row, "perception_visual_blur") for row in rows]), 6),
        "avg_mcm_tension": round(_avg([_float(row, "mcm_feldwirkung_mcm_tension") for row in rows]), 6),
        "avg_mcm_coherence": round(_avg([_float(row, "mcm_feldwirkung_mcm_coherence") for row in rows]), 6),
        "avg_mcm_asymmetry": round(_avg([_float(row, "mcm_feldwirkung_mcm_asymmetry") for row in rows]), 6),
        "avg_strain": round(_avg([_float(row, "mcm_strain_quality") for row in rows]), 6),
        "avg_rekopplung": round(_avg([_float(row, "mcm_rekopplung_quality") for row in rows]), 6),
        "dominant_family": families.most_common(1)[0][0] if families else "-",
        "dominant_preview": previews.most_common(1)[0][0] if previews else "-",
    }
    out.update({key: round(value, 6) for key, value in candle.items()})
    return out


def _classify(row: dict[str, object]) -> str:
    if float(row["rand_kipp"]) >= 0.12:
        return "reale_randphase"
    if float(row["offen"]) >= 0.60:
        return "reale_oeffnungsphase"
    if float(row["zentrum"]) >= 0.70:
        return "rekopplung_umfeld"
    return "gemischter_uebergang"


def _write_csv(rows: list[dict[str, object]], csv_out: Path) -> None:
    csv_out.parent.mkdir(parents=True, exist_ok=True)
    with csv_out.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = list(rows[0].keys())
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(rows: list[dict[str, object]], out: Path, raw_threshold: float) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    strongest_rand = max(rows, key=lambda row: float(row["rand_kipp"]))
    strongest_open = max(rows, key=lambda row: float(row["offen"]))
    strongest_loud = max(rows, key=lambda row: float(row["max_loudness"]))
    strongest_range = max(rows, key=lambda row: float(row["max_range_pct"]))

    lines: list[str] = [
        "# KAS Als Reale Randreferenz: Segmentlupe",
        "",
        "## Zweck",
        "",
        "Diese Diagnose isoliert die realen KAS-Hochlastabschnitte aus dem MINI_DIO-Episodenlauf.",
        "Sie verbindet Rollenanteile, Rezeptorachsen, MCM-Feldwirkung und Rohweltmerkmale.",
        "",
        "Die Diagnose ist passiv: kein Gate, keine Handlung, keine Runtime-Regel.",
        "",
        f"Hochlastschwelle Rohfeldaufnahme: `{raw_threshold:.6f}`.",
        "",
        "## Segmentmatrix",
        "",
        "| Segment | Klasse | Ticks | Episoden | Zentrum | Offen | Rand | Rohfeld max | Lautheit max | Schärfe avg | Drift | Range max | Richtungswechsel | Familie |",
        "|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            "| {segment} | {segment_class} | {start_tick}-{end_tick} | {episodes} | {zentrum:.4f} | {offen:.4f} | {rand_kipp:.4f} | {max_raw_field:.4f} | {max_loudness:.4f} | {avg_visual_sharpness:.4f} | {price_drift:.4f} | {max_range_pct:.4f} | {direction_change_ratio:.4f} | {dominant_family} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"- Staerkste Rand/Kipp-Naehe: Segment `{strongest_rand['segment']}` mit `{float(strongest_rand['rand_kipp']):.4f}`.",
            f"- Staerkste Oeffnung: Segment `{strongest_open['segment']}` mit `{float(strongest_open['offen']):.4f}`.",
            f"- Staerkste Lautheit: Segment `{strongest_loud['segment']}` mit `{float(strongest_loud['max_loudness']):.4f}`.",
            f"- Staerkste Kerzen-Range: Segment `{strongest_range['segment']}` mit `{float(strongest_range['max_range_pct']):.4f}`.",
            "",
            "## Einordnung",
            "",
            "KAS wird nicht als dauerhaft randnah gelesen. Die Randnaehe entsteht in lokalen Segmenten, in denen Rohfeldaufnahme, Lautheit, visuelle Unschaerfe und Richtungswechsel zusammenfallen.",
            "",
            "Damit ist KAS als reale Randreferenz nuetzlich: Es zeigt, dass echte Weltabschnitte staerker randnah werden koennen als die bisherige synthetische Randdominanz, ohne dass das Gesamtfeld kollabiert.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte aus den staerksten KAS-Randsegmenten eine synthetische Gegenwelt gebaut werden. Ziel ist zu pruefen, ob eine real inspirierte synthetische Welt dieselbe Randnaehe reproduzieren kann.",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--episodes", required=True)
    parser.add_argument("--world-data", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--csv-out", required=True)
    parser.add_argument("--context", type=int, default=4)
    args = parser.parse_args()

    rows = sorted(_load(Path(args.episodes)), key=_tick)
    candles = _load(Path(args.world_data))
    candle_by_ts = {_timestamp(row): row for row in candles}
    raw_threshold = _percentile([_float(row, "perception_raw_field_intake_pressure") for row in rows], 0.90)
    segments = _segments(rows, raw_threshold=raw_threshold, context=args.context)
    summaries = [_summarize_segment(index + 1, segment, candle_by_ts) for index, segment in enumerate(segments)]
    for summary in summaries:
        summary["segment_class"] = _classify(summary)
    summaries = sorted(summaries, key=lambda row: (float(row["rand_kipp"]), float(row["offen"])), reverse=True)
    _write_csv(summaries, Path(args.csv_out))
    _write_markdown(summaries, Path(args.out), raw_threshold)
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
