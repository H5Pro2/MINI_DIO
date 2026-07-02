from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mini_world import build_senses_world_relative, build_sensory_profile, load_candles


DEFAULT_WORLDS = {
    "SOL_2023_NEG": "data/kontrolliert_2023_negative_stress_10k_5m_SOLUSDT.csv",
    "SOL_2024_SIDE": "data/kontrolliert_2024_moderate_sideways_10k_5m_SOLUSDT.csv",
    "SOL_2025_STRESS": "data/kontrolliert_2025_stress_10k_5m_SOLUSDT.csv",
    "SOL_2026_STABLE": "data/kontrolliert_2026_stable_reife_10k_5m_SOLUSDT.csv",
    "BTC_2024_5M": "data/kontrolliert_btc_2024_5m_10k_BTCUSDT.csv",
    "DOGE_2025_5M": "data/kontrolliert_doge_2025_5m_10k_DOGEUSDT.csv",
    "XRP_2025_5M": "data/kontrolliert_xrp_2025_5m_10k_XRPUSDT.csv",
    "PAXG_2024_5M": "data/kontrolliert_paxg_2024_5m_10k_PAXGUSDT.csv",
    "DESYNC": "data/synthetic_mcm_desync_axes_8500_5m.csv",
    "VISUAL_STABLE_HEARING_CHAOTIC": "data/synthetic_mcm_visual_stable_hearing_chaotic_5m.csv",
    "VISUAL_CHAOTIC_HEARING_STABLE": "data/synthetic_mcm_visual_chaotic_hearing_stable_5m.csv",
}

DETAIL_INPUTS = [
    ("100", 100, "docs/befunde/1305_WELTLAGEN_FOLGEMEMORY_BLOCK100_DETAILS.csv"),
    ("200", 200, "docs/befunde/1303_WELTLAGEN_FOLGEMEMORY_MEHRWELTEN_DETAILS.csv"),
    ("400", 400, "docs/befunde/1306_WELTLAGEN_FOLGEMEMORY_BLOCK400_DETAILS.csv"),
]


def _parse_world(value: str) -> tuple[str, str]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("world must be LABEL=PATH")
    label, path = value.split("=", 1)
    return label, path


def _parse_detail(value: str) -> tuple[str, int, Path]:
    parts = value.split("=", 2)
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("detail must be SCALE=BLOCK_SIZE=PATH")
    return parts[0], int(parts[1]), Path(parts[2])


def _float(value: object) -> float:
    try:
        out = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if out != out else out


def _load_target_sequences(path: Path, profile: str) -> set[str]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return {
            str(row["worldlage_sequence"])
            for row in csv.DictReader(handle)
            if str(row.get("multiscale_profile", "")) == profile
        }


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _raw_window_profile(candles: list[dict], profile: dict, start: int, end: int, *, window: int) -> dict[str, float]:
    end = min(end, len(candles))
    start = max(0, min(start, end))
    if end <= start:
        return {
            "price_move_pct": 0.0,
            "avg_abs_body_pct": 0.0,
            "avg_range_pct": 0.0,
            "avg_volume": 0.0,
            "avg_auditory": 0.0,
            "avg_visual_sharpness": 0.0,
            "avg_field_pressure": 0.0,
            "avg_form_flow": 0.0,
            "avg_energy_shift": 0.0,
        }
    first_open = _float(candles[start].get("open"))
    last_close = _float(candles[end - 1].get("close"))
    price_move_pct = ((last_close - first_open) / first_open) * 100.0 if abs(first_open) > 1e-12 else 0.0
    bodies: list[float] = []
    ranges: list[float] = []
    volumes: list[float] = []
    auditory: list[float] = []
    visual: list[float] = []
    pressure: list[float] = []
    form_flow: list[float] = []
    energy_shift: list[float] = []
    for index in range(start, end):
        candle = candles[index]
        open_price = _float(candle.get("open"))
        close = _float(candle.get("close"))
        high = _float(candle.get("high"))
        low = _float(candle.get("low"))
        base = max(abs(open_price), 1e-12)
        bodies.append(abs(close - open_price) / base * 100.0)
        ranges.append(abs(high - low) / base * 100.0)
        volumes.append(_float(candle.get("volume")))
        senses = build_senses_world_relative(candles, index, window=window, profile=profile)
        hoeren = dict(senses.get("hoeren", {}) or {})
        sehen = dict(senses.get("sehen", {}) or {})
        state = dict(senses.get("perception_regulation_state", {}) or {})
        auditory.append(abs(_float(hoeren.get("energy_tone"))) + abs(_float(hoeren.get("energy_shift"))))
        visual.append(_float(state.get("visual_sharpness")))
        pressure.append(_float(state.get("adapted_field_intake_pressure", state.get("raw_field_intake_pressure", 0.0))))
        form_flow.append(_float(sehen.get("form_flow")))
        energy_shift.append(_float(hoeren.get("energy_shift")))
    return {
        "price_move_pct": round(price_move_pct, 6),
        "avg_abs_body_pct": round(_avg(bodies), 6),
        "avg_range_pct": round(_avg(ranges), 6),
        "avg_volume": round(_avg(volumes), 6),
        "avg_auditory": round(_avg(auditory), 6),
        "avg_visual_sharpness": round(_avg(visual), 6),
        "avg_field_pressure": round(_avg(pressure), 6),
        "avg_form_flow": round(_avg(form_flow), 6),
        "avg_energy_shift": round(_avg(energy_shift), 6),
    }


def _classify_raw(profile: dict[str, float]) -> str:
    auditory = abs(profile["avg_auditory"])
    pressure = profile["avg_field_pressure"]
    move = abs(profile["price_move_pct"])
    range_pct = profile["avg_range_pct"]
    if auditory >= 0.50 or pressure >= 0.22:
        return "laute_oder_druckvolle_rohwelt"
    if move >= 3.0 or range_pct >= 1.0:
        return "bewegungsreiche_rohwelt"
    if profile["avg_visual_sharpness"] >= 0.72 and pressure <= 0.16:
        return "scharf_ruhige_rohwelt"
    return "gemischte_rohwelt"


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(rows: list[dict[str, object]], summary: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Mehrskalige Weltlagen-Folgen Rohweltfenster",
        "",
        "Diese Diagnose liest skalenabhaengige Weltlagen-Folgen gegen konkrete Rohweltfenster zurueck.",
        "",
        "Ziel:",
        "",
        "```text",
        "Welche Weltbewegung macht eine kurze neutrale Lage",
        "zu einer laenger beruhigenden Feldphase?",
        "```",
        "",
        "## Verdichtung nach Folge und Skala",
        "",
        "| Lagefolge | Skala | Fenster | Rohklasse | Bewegung % | Range % | Hoeren | Sicht | Felddruck |",
        "|---|---:|---:|---|---:|---:|---:|---:|---:|",
    ]
    for row in summary[:40]:
        lines.append(
            "| {base_sequence} | {scale} | {count} | {dominant_raw_class} | {avg_price_move_pct:.4f} | {avg_range_pct:.4f} | {avg_auditory:.4f} | {avg_visual_sharpness:.4f} | {avg_field_pressure:.4f} |".format(
                **row
            )
        )
    lines.extend(
        [
            "",
            "## Bewertung",
            "",
            "Skalenabhaengige Folgen sind nicht beliebig.",
            "",
            "Sie treten dort auf, wo Rohwelt, Hoeren, Sicht und Felddruck ueber Zeit anders getragen werden als im kurzen Einzelblock.",
            "",
            "Damit wird der Unterschied zwischen kurzer Lagebewegung und laengerer Feldphase konkreter ruecklesbar.",
            "",
            "Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung und kein Gate.",
            "",
            "Wie es weitergeht: Als naechstes sollten die Rohklassen der skalenabhaengigen Folgen mit stabil neutralen und stabil beruhigenden Folgen verglichen werden.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--world", action="append", type=_parse_world)
    parser.add_argument("--detail", action="append", type=_parse_detail)
    parser.add_argument("--target", default="docs/befunde/1308_WELTLAGEN_FOLGEMEMORY_MEHRSKALIG.csv")
    parser.add_argument("--profile", default="skalenabhaengig_neutral_beruhigend")
    parser.add_argument("--window", type=int, default=5)
    parser.add_argument("--out", default="docs/befunde/1309_WELTLAGEN_MEHRSKALIG_ROHWELTFENSTER.md")
    parser.add_argument("--csv-out", default="docs/befunde/1309_WELTLAGEN_MEHRSKALIG_ROHWELTFENSTER.csv")
    parser.add_argument("--summary-out", default="docs/befunde/1309_WELTLAGEN_MEHRSKALIG_ROHWELTFENSTER_SUMMARY.csv")
    args = parser.parse_args()

    worlds = {label: Path(path) for label, path in (args.world or DEFAULT_WORLDS.items())}
    details = args.detail or DETAIL_INPUTS
    targets = _load_target_sequences(Path(args.target), args.profile)
    candle_cache: dict[str, list[dict]] = {}
    profile_cache: dict[str, dict] = {}
    rows: list[dict[str, object]] = []

    for scale, block_size, detail_path in details:
        with Path(detail_path).open("r", encoding="utf-8", newline="") as handle:
            for detail in csv.DictReader(handle):
                sequence = str(detail.get("base_sequence", ""))
                if sequence not in targets:
                    continue
                world = str(detail.get("world", ""))
                if world not in worlds:
                    continue
                if world not in candle_cache:
                    candle_cache[world] = load_candles(worlds[world])
                    profile_cache[world] = build_sensory_profile(candle_cache[world], window=args.window)
                block_index = int(float(detail.get("block_index", 0) or 0))
                start = block_index * block_size
                end = start + block_size
                raw = _raw_window_profile(candle_cache[world], profile_cache[world], start, end, window=args.window)
                rows.append(
                    {
                        "world": world,
                        "scale": scale,
                        "block_index": block_index,
                        "base_sequence": sequence,
                        "raw_class": _classify_raw(raw),
                        **raw,
                        "passive_only": 1,
                        "influences_action": 0,
                    }
                )

    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["base_sequence"]), str(row["scale"]))].append(row)

    summary: list[dict[str, object]] = []
    for (sequence, scale), group in grouped.items():
        class_counts: dict[str, int] = defaultdict(int)
        for row in group:
            class_counts[str(row["raw_class"])] += 1
        dominant = sorted(class_counts.items(), key=lambda item: (-item[1], item[0]))[0][0]
        summary.append(
            {
                "base_sequence": sequence,
                "scale": scale,
                "count": len(group),
                "dominant_raw_class": dominant,
                "raw_class_counts": ";".join(f"{key}:{value}" for key, value in sorted(class_counts.items(), key=lambda item: (-item[1], item[0]))),
                "avg_price_move_pct": round(_avg([_float(row["price_move_pct"]) for row in group]), 6),
                "avg_abs_body_pct": round(_avg([_float(row["avg_abs_body_pct"]) for row in group]), 6),
                "avg_range_pct": round(_avg([_float(row["avg_range_pct"]) for row in group]), 6),
                "avg_auditory": round(_avg([_float(row["avg_auditory"]) for row in group]), 6),
                "avg_visual_sharpness": round(_avg([_float(row["avg_visual_sharpness"]) for row in group]), 6),
                "avg_field_pressure": round(_avg([_float(row["avg_field_pressure"]) for row in group]), 6),
            }
        )
    summary.sort(key=lambda row: (-int(row["count"]), str(row["base_sequence"]), str(row["scale"])))
    if not rows or not summary:
        raise RuntimeError("no raw windows generated")
    _write_csv(rows, Path(args.csv_out))
    _write_csv(summary, Path(args.summary_out))
    _write_markdown(rows, summary, Path(args.out))
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.summary_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
