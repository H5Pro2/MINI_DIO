from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.run_research_chain import run_chain
from tools.report_world_relative_topology_matrix import _load_rows, _summarize_world


def _path(path_text: str) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _float(row: dict, key: str) -> float:
    try:
        return float(row.get(key) or 0.0)
    except Exception:
        return 0.0


def _read_rows(path: Path) -> tuple[list[str], list[dict]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def _write_rows(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _window_metrics(rows: list[dict], start: int, size: int) -> dict[str, float]:
    window = rows[start : start + size]
    closes = [_float(row, "close") for row in window]
    highs = [_float(row, "high") for row in window]
    lows = [_float(row, "low") for row in window]
    volumes = [_float(row, "volume") for row in window]

    signed_returns = [
        (closes[index] - closes[index - 1]) / closes[index - 1]
        for index in range(1, len(closes))
        if closes[index - 1]
    ]
    returns = [abs(value) for value in signed_returns]
    ranges = [(high - low) / close for high, low, close in zip(highs, lows, closes) if close]
    direction_changes = sum(
        1
        for index in range(2, len(closes))
        if (closes[index] - closes[index - 1]) * (closes[index - 1] - closes[index - 2]) < 0
    )
    drift = ((closes[-1] - closes[0]) / closes[0]) if len(closes) >= 2 and closes[0] else 0.0
    max_drawdown = 0.0
    peak = closes[0] if closes else 0.0
    for close in closes:
        peak = max(peak, close)
        if peak:
            max_drawdown = max(max_drawdown, (peak - close) / peak)

    avg_abs_return = sum(returns) / max(1, len(returns))
    max_abs_return = max(returns) if returns else 0.0
    avg_range = sum(ranges) / max(1, len(ranges))
    mean_signed = sum(signed_returns) / max(1, len(signed_returns))
    return_volatility = (
        sum((value - mean_signed) ** 2 for value in signed_returns) / max(1, len(signed_returns))
    ) ** 0.5
    avg_volume = sum(volumes) / max(1, len(volumes))

    quiet_score = (
        avg_abs_return * 42.0
        + max_abs_return * 8.0
        + avg_range * 24.0
        + return_volatility * 32.0
        + abs(drift) * 0.7
        + max_drawdown * 1.1
        + (direction_changes / max(1, size)) * 0.5
    )
    return {
        "start": float(start),
        "end": float(start + size),
        "avg_abs_return": avg_abs_return,
        "max_abs_return": max_abs_return,
        "avg_range": avg_range,
        "return_volatility": return_volatility,
        "drift": drift,
        "max_drawdown": max_drawdown,
        "direction_changes": float(direction_changes),
        "avg_volume": avg_volume,
        "quiet_score": quiet_score,
    }


def _non_overlapping_candidates(
    metrics: list[dict[str, float]],
    window_size: int,
    limit: int,
) -> list[dict[str, float]]:
    selected: list[dict[str, float]] = []
    for item in sorted(metrics, key=lambda row: row["quiet_score"]):
        start = int(item["start"])
        end = int(item["end"])
        overlaps = False
        for existing in selected:
            existing_start = int(existing["start"])
            existing_end = int(existing["end"])
            overlap = max(0, min(end, existing_end) - max(start, existing_start))
            if overlap >= int(window_size * 0.35):
                overlaps = True
                break
        if not overlaps:
            selected.append(item)
        if len(selected) >= limit:
            break
    return selected


def _field_quiet_score(summary: dict[str, object]) -> float:
    center = float(summary.get("center_share", 0.0) or 0.0)
    open_share = float(summary.get("open_share", 0.0) or 0.0)
    rand = float(summary.get("rand_share", 0.0) or 0.0)
    rekopplung = float(summary.get("avg_rekopplung", 0.0) or 0.0)
    carry = float(summary.get("avg_carry", 0.0) or 0.0)
    strain = float(summary.get("avg_strain", 0.0) or 0.0)
    return (center * 0.35) + (rekopplung * 0.22) + (carry * 0.18) - (open_share * 0.16) - (rand * 0.22) - (strain * 0.18)


def _write_csv_report(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "rank",
        "label",
        "data_path",
        "start",
        "end",
        "raw_quiet_score",
        "field_quiet_score",
        "topology_state",
        "center_share",
        "open_share",
        "rand_share",
        "rekopplung_overlay_share",
        "avg_rekopplung",
        "avg_carry",
        "avg_strain",
        "avg_sensory",
        "unique_symbols",
        "episode_memory_written",
        "top_symbol_overlap",
        "top_family_overlap",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(rows: list[dict[str, object]], path: Path, source: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    best = rows[0] if rows else {}
    lines = [
        "# Feldruhige Fensterselektion",
        "",
        "## Zweck",
        "",
        "Diese Diagnose korrigiert die reine Rohwelt-Quiet-Extraktion.",
        "",
        "Rohweltlich ruhig bedeutet nicht automatisch innenfeldruhig. Deshalb werden mehrere rohweltlich ruhige Kandidaten passiv durch MINI_DIO gelesen und danach nach Feldruhe sortiert.",
        "",
        "## Quelle",
        "",
        f"- Quelle: `{source.relative_to(ROOT) if source.is_relative_to(ROOT) else source}`",
        "",
        "## Methode",
        "",
        "1. Rohweltlich ruhige Fenster suchen.",
        "2. Ueberlappende Kandidaten reduzieren.",
        "3. Jeden Kandidaten passiv durch MINI_DIO laufen lassen.",
        "4. Topologie aus den Episoden lesen.",
        "5. Relativ nach Feldruhe sortieren.",
        "",
        "Die Sortierung ist Diagnose, keine Runtime-Regel.",
        "",
        "## Kandidaten",
        "",
        "| Rang | Kandidat | Start | Ende | Rohquiet | Feldquiet | Topologie | Zentrum | Offen | Rand | Rekopplung | Carry | Strain | Syntax | Memory |",
        "|---:|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {rank} | {label} | {start:.0f} | {end:.0f} | {raw_quiet_score:.4f} | {field_quiet_score:.4f} | {topology_state} | {center_share:.4f} | {open_share:.4f} | {rand_share:.4f} | {avg_rekopplung:.4f} | {avg_carry:.4f} | {avg_strain:.4f} | {unique_symbols} | {episode_memory_written} |".format(
                **row
            )
        )
    lines.extend(["", "## Befund", ""])
    if best:
        lines.extend(
            [
                f"- Feldruhigster Kandidat: `{best['label']}`",
                f"- Rohweltlicher Start/Ende: `{best['start']:.0f}` / `{best['end']:.0f}`",
                f"- Topologie: `{best['topology_state']}`",
                f"- Zentrum: `{best['center_share']:.4f}`",
                f"- Offen: `{best['open_share']:.4f}`",
                f"- Rand/Kipp: `{best['rand_share']:.4f}`",
                "",
                "Der Befund trennt die Ebenen:",
                "",
                "```text",
                "Rohweltliche Ruhe = Eigenschaft des Aussenfensters.",
                "Feldruhe = Eigenschaft der MCM-Innenreaktion.",
                "```",
            ]
        )
    lines.extend(
        [
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte der feldruhigste Kandidat direkt gegen das reale Bruchfenster verglichen werden. Ziel: nicht Rohruhe gegen Rohstress, sondern Feldruhe gegen Feldbruch innerhalb derselben Quelle.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Waehlt ruhige Fenster nach rohweltlicher Ruhe und MCM-Feldruhe.")
    parser.add_argument("--source", required=True)
    parser.add_argument("--window-size", type=int, default=2000)
    parser.add_argument("--step", type=int, default=250)
    parser.add_argument("--candidates", type=int, default=5)
    parser.add_argument("--label-prefix", default="field_quiet_candidate")
    parser.add_argument("--data-dir", default="data/field_quiet_candidates")
    parser.add_argument("--debug-root", default="debug/field_quiet_candidates")
    parser.add_argument("--memory-dir", default="bot_memory/field_quiet_candidates")
    parser.add_argument("--out", required=True)
    parser.add_argument("--csv-out", required=True)
    args = parser.parse_args()

    source = _path(args.source)
    fieldnames, rows = _read_rows(source)
    if len(rows) < args.window_size:
        raise ValueError(f"source has only {len(rows)} rows, need {args.window_size}")

    metrics: list[dict[str, float]] = []
    max_start = len(rows) - args.window_size
    for start in range(0, max_start + 1, max(1, args.step)):
        metrics.append(_window_metrics(rows, start, args.window_size))
    if metrics[-1]["start"] != float(max_start):
        metrics.append(_window_metrics(rows, max_start, args.window_size))

    selected = _non_overlapping_candidates(metrics, args.window_size, args.candidates)
    report_rows: list[dict[str, object]] = []
    data_dir = _path(args.data_dir)
    debug_root = _path(args.debug_root)
    memory_dir = _path(args.memory_dir)
    source_stem = source.stem.lower()

    for index, candidate in enumerate(selected, start=1):
        label = f"{args.label_prefix}_{index:02d}"
        window_path = data_dir / f"{source_stem}_{label}_{args.window_size}.csv"
        start = int(candidate["start"])
        _write_rows(window_path, fieldnames, rows[start : start + args.window_size])

        candidate_debug = debug_root / label
        candidate_memory = memory_dir / f"{label}.json"
        chain_out = ROOT / "docs" / "befunde" / f"{label.upper()}_FORSCHUNGSKETTE.md"
        summary = run_chain(window_path, candidate_debug, candidate_memory, chain_out)

        episodes_path = candidate_debug / "dio_mini_lauf_1" / "episodes.csv"
        _, topology = _summarize_world(label.upper(), _load_rows(episodes_path))
        field_score = _field_quiet_score(topology)
        report_rows.append(
            {
                "rank": 0,
                "label": label.upper(),
                "data_path": str(window_path.relative_to(ROOT) if window_path.is_relative_to(ROOT) else window_path),
                "start": candidate["start"],
                "end": candidate["end"],
                "raw_quiet_score": candidate["quiet_score"],
                "field_quiet_score": field_score,
                "topology_state": topology["topology_state"],
                "center_share": topology["center_share"],
                "open_share": topology["open_share"],
                "rand_share": topology["rand_share"],
                "rekopplung_overlay_share": topology["rekopplung_overlay_share"],
                "avg_rekopplung": topology["avg_rekopplung"],
                "avg_carry": topology["avg_carry"],
                "avg_strain": topology["avg_strain"],
                "avg_sensory": topology["avg_sensory"],
                "unique_symbols": int((summary.get("unique_symbols") or [0, 0])[1]),
                "episode_memory_written": int((summary.get("episode_memory_written") or [0, 0])[1]),
                "top_symbol_overlap": float((summary.get("top_symbol_overlap") or {}).get("ratio", 0.0)),
                "top_family_overlap": float((summary.get("top_family_overlap") or {}).get("ratio", 0.0)),
            }
        )

    report_rows.sort(key=lambda row: float(row["field_quiet_score"]), reverse=True)
    for index, row in enumerate(report_rows, start=1):
        row["rank"] = index

    out = _path(args.out)
    csv_out = _path(args.csv_out)
    _write_csv_report(report_rows, csv_out)
    _write_markdown(report_rows, out, source)
    print(json.dumps({"out": str(out), "csv_out": str(csv_out), "candidates": report_rows}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
