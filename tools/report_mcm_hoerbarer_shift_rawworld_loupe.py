from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mini_world import build_sensory_profile, load_candles
from tools.report_worldlage_multiscale_raw_windows import _classify_raw, _raw_window_profile


WORLD_FILES = {
    "BTC_2024_5M": "data/kontrolliert_btc_2024_5m_10k_BTCUSDT.csv",
    "BTC_2025_5M": "data/kontrolliert_btc_2025_5m_10k_BTCUSDT.csv",
    "DOGE_2024_5M": "data/kontrolliert_doge_2024_5m_10k_DOGEUSDT.csv",
    "DOGE_2025_5M": "data/kontrolliert_doge_2025_5m_10k_DOGEUSDT.csv",
    "PAXG_2024_5M": "data/kontrolliert_paxg_2024_5m_10k_PAXGUSDT.csv",
    "PAXG_2025_5M": "data/kontrolliert_paxg_2025_5m_10k_PAXGUSDT.csv",
    "SOL_2023_ALT_A_FOLLOW": "data/kontrolliert_2023_altseq_a_follow_10k_5m_SOLUSDT.csv",
    "SOL_2023_NEG_STRESS": "data/kontrolliert_2023_negative_stress_10k_5m_SOLUSDT.csv",
    "SOL_2023_POS_EXP": "data/kontrolliert_2023_positive_expansion_10k_5m_SOLUSDT.csv",
    "SOL_2024_ALT_A_FOLLOW": "data/kontrolliert_2024_altseq_a_follow_10k_5m_SOLUSDT.csv",
    "SOL_2024_NEG_STRESS": "data/kontrolliert_2024_negative_stress_10k_5m_SOLUSDT.csv",
    "SOL_2024_POS": "data/kontrolliert_2024_positive_stress_10k_5m_SOLUSDT.csv",
    "SOL_2024_SIDE": "data/kontrolliert_2024_moderate_sideways_10k_5m_SOLUSDT.csv",
    "SOL_2025_ALT_A_FOLLOW": "data/kontrolliert_2025_altseq_a_follow_10k_5m_SOLUSDT.csv",
    "SOL_2025_REC": "data/kontrolliert_2025_positive_recovery_10k_5m_SOLUSDT.csv",
    "SOL_2025_STRESS": "data/kontrolliert_2025_stress_10k_5m_SOLUSDT.csv",
    "XRP_2024_5M": "data/kontrolliert_xrp_2024_5m_10k_XRPUSDT.csv",
    "XRP_2025_5M": "data/kontrolliert_xrp_2025_5m_10k_XRPUSDT.csv",
}


def _float(value: object) -> float:
    try:
        out = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if out != out else out


def _resolve_world(label: str) -> Path | None:
    candidates = [label]
    if label.endswith("_CONTRAST"):
        candidates.append(label[: -len("_CONTRAST")])
    for candidate in candidates:
        path = WORLD_FILES.get(candidate)
        if path:
            return ROOT / path
    return None


def _selected_rows(path: Path, per_asset: int, min_score: float) -> tuple[list[dict[str, str]], list[str]]:
    rows = list(csv.DictReader(path.open("r", encoding="utf-8", newline="")))
    rows.sort(key=lambda row: -_float(row.get("score")))
    selected: list[dict[str, str]] = []
    counts: dict[str, int] = {}
    unresolved: list[str] = []
    for row in rows:
        if _float(row.get("score")) < min_score:
            continue
        asset = str(row.get("asset") or "-")
        if counts.get(asset, 0) >= per_asset:
            continue
        world = str(row.get("world") or "")
        if _resolve_world(world) is None:
            unresolved.append(world)
            continue
        selected.append(row)
        counts[asset] = counts.get(asset, 0) + 1
    return selected, sorted(set(unresolved))


def _phase_profile(candles: list[dict], profile: dict, start: int, end: int, *, window: int) -> dict[str, float | str]:
    raw = _raw_window_profile(candles, profile, start, end, window=window)
    return {
        "raw_class": _classify_raw(raw),
        **raw,
    }


def _row_profiles(source: dict[str, str], *, radius: int, window: int) -> dict[str, object]:
    world = str(source.get("world") or "")
    path = _resolve_world(world)
    if path is None:
        raise RuntimeError(f"unresolved world: {world}")
    candles = load_candles(path)
    profile = build_sensory_profile(candles, window=window)
    scale = int(float(source.get("scale") or 0))
    block_index = int(float(source.get("block_index") or 0))
    start = block_index * scale
    end = start + scale
    pre = _phase_profile(candles, profile, start - radius, start, window=window)
    during = _phase_profile(candles, profile, start, end, window=window)
    post = _phase_profile(candles, profile, end, end + radius, window=window)
    return {
        "holdout_group": source.get("holdout_group", "-"),
        "asset": source.get("asset", "-"),
        "world": world,
        "source_file": str(path.relative_to(ROOT)),
        "scale": scale,
        "block_index": block_index,
        "start_tick": start,
        "end_tick": end,
        "base_sequence": source.get("base_sequence", "-"),
        "candidate_score": round(_float(source.get("score")), 6),
        "pre_raw_class": pre["raw_class"],
        "during_raw_class": during["raw_class"],
        "post_raw_class": post["raw_class"],
        "pre_move_pct": pre["price_move_pct"],
        "during_move_pct": during["price_move_pct"],
        "post_move_pct": post["price_move_pct"],
        "pre_range": pre["avg_range_pct"],
        "during_range": during["avg_range_pct"],
        "post_range": post["avg_range_pct"],
        "pre_hoeren": pre["avg_auditory"],
        "during_hoeren": during["avg_auditory"],
        "post_hoeren": post["avg_auditory"],
        "pre_sicht": pre["avg_visual_sharpness"],
        "during_sicht": during["avg_visual_sharpness"],
        "post_sicht": post["avg_visual_sharpness"],
        "pre_druck": pre["avg_field_pressure"],
        "during_druck": during["avg_field_pressure"],
        "post_druck": post["avg_field_pressure"],
        "range_narrows_vs_pre": int(float(during["avg_range_pct"]) < float(pre["avg_range_pct"])),
        "hearing_rises_vs_pre": int(float(during["avg_auditory"]) > float(pre["avg_auditory"])),
        "pressure_rises_vs_pre": int(float(during["avg_field_pressure"]) > float(pre["avg_field_pressure"])),
        "passive_only": 1,
        "influences_action": 0,
    }


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(rows: list[dict[str, object]], unresolved: list[str], path: Path) -> None:
    narrowed = sum(int(row["range_narrows_vs_pre"]) for row in rows)
    hearing = sum(int(row["hearing_rises_vs_pre"]) for row in rows)
    pressure = sum(int(row["pressure_rises_vs_pre"]) for row in rows)
    lines = [
        "# Hoerbarer schmaler Shift - Rohweltlupe",
        "",
        "Diese Diagnose liest starke Mikrofenster gegen konkrete Rohweltabschnitte zurueck.",
        "",
        "Gelesen wird passiv:",
        "",
        "- Vorfenster",
        "- Trefferfenster",
        "- Folgefenster",
        "",
        "Die Diagnose erzeugt keine Handlung, keine Richtung und kein Gate.",
        "",
        "## Verdichtung",
        "",
        f"- gelesene Fenster: `{len(rows)}`",
        f"- Trefferfenster enger als Vorfenster: `{narrowed}`",
        f"- Hoeren steigt gegen Vorfenster: `{hearing}`",
        f"- Felddruck steigt gegen Vorfenster: `{pressure}`",
        "",
    ]
    if unresolved:
        lines.extend(["Nicht aufgeloeste Weltlabels:", ""])
        for item in unresolved:
            lines.append(f"- `{item}`")
        lines.append("")
    lines.extend(
        [
            "## Fenster",
            "",
            "| Asset | Welt | Ticks | Sequenz | Klasse vor -> waehrend -> nach | Range | Hoeren | Druck |",
            "|---|---|---:|---|---|---|---|---|",
        ]
    )
    for row in rows:
        lines.append(
            "| {asset} | {world} | {start_tick}-{end_tick} | `{base_sequence}` | `{pre_raw_class}` -> `{during_raw_class}` -> `{post_raw_class}` | {pre_range:.4f}->{during_range:.4f}->{post_range:.4f} | {pre_hoeren:.4f}->{during_hoeren:.4f}->{post_hoeren:.4f} | {pre_druck:.4f}->{during_druck:.4f}->{post_druck:.4f} |".format(
                **row
            )
        )
    lines.extend(
        [
            "",
            "## Bewertung",
            "",
            "Die Mikrophase wird hier als konkrete Weltphase gelesen, nicht als abstrakte Symbolrolle.",
            "",
            "Wenn Range enger wird und Hoeren/Felddruck steigen, liegt eine plausible komprimierte Sinnesphase vor: weniger aeussere Ausdehnung, aber mehr innere Ton-/Druckwirkung.",
            "",
            "Wie es weitergeht: Als naechstes sollte geprueft werden, ob diese komprimierte Sinnesphase spaeter im Bedeutungsnetz als Bruecke, Randnaehe oder Zentrumskontakt erscheint.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="docs/befunde/1349_HOERBARER_SCHMALER_SHIFT_MULTI_HOLDOUT.csv")
    parser.add_argument("--per-asset", type=int, default=4)
    parser.add_argument("--min-score", type=float, default=0.25)
    parser.add_argument("--radius", type=int, default=100)
    parser.add_argument("--window", type=int, default=5)
    parser.add_argument("--out", default="docs/befunde/1350_HOERBARER_SCHMALER_SHIFT_ROHWELTLUPE.md")
    parser.add_argument("--csv-out", default="docs/befunde/1350_HOERBARER_SCHMALER_SHIFT_ROHWELTLUPE.csv")
    args = parser.parse_args()

    selected, unresolved = _selected_rows(Path(args.input), args.per_asset, args.min_score)
    rows = [_row_profiles(row, radius=args.radius, window=args.window) for row in selected]
    if not rows:
        raise RuntimeError("no resolvable rows selected")
    _write_csv(rows, Path(args.csv_out))
    _write_markdown(rows, unresolved, Path(args.out))
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
