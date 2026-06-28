from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt


def _read_rows(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    if not text.strip():
        return []
    sample = text[:4096]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",;")
    except csv.Error:
        dialect = csv.excel
    return list(csv.DictReader(text.splitlines(), dialect=dialect))


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _safe_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _safe_name(value: str) -> str:
    chars = []
    for char in str(value):
        if char.isalnum() or char in ("_", "-"):
            chars.append(char)
        else:
            chars.append("_")
    return "".join(chars).strip("_")


def _key(row: dict[str, str], mode_key: str = "mode") -> tuple[str, str, str]:
    return (
        str(row.get("world", "")),
        str(row.get("pair", "")),
        str(row.get(mode_key, "")),
    )


def _load_source_lookup(paths: list[Path]) -> dict[tuple[str, str, str], dict[str, str]]:
    lookup: dict[tuple[str, str, str], dict[str, str]] = {}
    for path in paths:
        for row in _read_rows(path):
            lookup[_key(row, mode_key="typology")] = row
    return lookup


def _join_details(
    axis_rows: list[dict[str, str]],
    source_lookup: dict[tuple[str, str, str], dict[str, str]],
) -> list[dict[str, str]]:
    joined: list[dict[str, str]] = []
    for row in axis_rows:
        source = source_lookup.get(_key(row, mode_key="mode"))
        if not source:
            continue
        merged = dict(row)
        for key in ("data_file", "tick_min", "tick_mid", "tick_max", "events", "before_return_pct", "after_return_pct"):
            merged[key] = source.get(key, "")
        joined.append(merged)
    return joined


def _pick_representatives(rows: list[dict[str, str]], limit_per_reading: int) -> list[dict[str, str]]:
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[row.get("reading", "-")].append(row)
    selected: list[dict[str, str]] = []
    for reading in sorted(groups):
        items = sorted(
            groups[reading],
            key=lambda row: (
                _safe_float(row.get("range_pct")),
                abs(_safe_float(row.get("return_pct"))),
                _safe_float(row.get("pressure_abs")),
            ),
            reverse=True,
        )
        selected.extend(items[:limit_per_reading])
    return selected


def _slice(rows: list[dict[str, str]], start: int, end: int) -> tuple[int, list[dict[str, str]]]:
    start = max(0, start)
    end = min(len(rows) - 1, end)
    return start, rows[start : end + 1]


def _plot(row: dict[str, str], root: Path, out_dir: Path, pad: int) -> Path:
    data_path = root / row["data_file"]
    candles = _read_rows(data_path)
    tick_min = _safe_int(row.get("tick_min"))
    tick_mid = _safe_int(row.get("tick_mid"))
    tick_max = _safe_int(row.get("tick_max"))
    start, window = _slice(candles, tick_min - pad, tick_max + pad)
    xs = list(range(start, start + len(window)))
    closes = [_safe_float(item.get("close")) for item in window]
    highs = [_safe_float(item.get("high")) for item in window]
    lows = [_safe_float(item.get("low")) for item in window]

    fig, ax = plt.subplots(figsize=(11.2, 5.2), dpi=150)
    ax.plot(xs, closes, color="#74a7ff", linewidth=1.6, label="Close")
    ax.fill_between(xs, lows, highs, color="#74a7ff", alpha=0.13, label="High-Low")
    ax.axvspan(tick_min, tick_max, color="#ff9f43", alpha=0.20, label="Achsenfenster")
    ax.axvline(tick_mid, color="#ff5c5c", linewidth=1.1, linestyle="--", label="Schwerpunkt")
    title = (
        f"{row['reading']} | {row['world']} | {row['pair']}\n"
        f"{row['mode']} / {row['phase_hint']} / {row['dominant_movement']}"
    )
    ax.set_title(title, fontsize=10)
    ax.set_xlabel("Tick")
    ax.set_ylabel("Preis")
    ax.grid(True, alpha=0.18)
    ax.legend(loc="best", fontsize=8)
    fig.tight_layout()

    out_dir.mkdir(parents=True, exist_ok=True)
    file_name = "1023_" + _safe_name(f"{row['reading']}_{row['world']}_{row['pair']}_{tick_min}_{tick_max}") + ".png"
    out_path = out_dir / file_name
    fig.savefig(out_path)
    plt.close(fig)
    return out_path


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, plotted: list[dict[str, object]]) -> None:
    lines = [
        "# 1023 - Achse 183drjy<->1t5bcxp als Chartfenster",
        "",
        "Passive Visualisierung der gemeinsamen Achse in mehreren Rollenqualitaeten.",
        "",
        "Orange markiert das MCM-Achsenfenster. Rot markiert den Schwerpunkt des Fensters.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Visualisierung",
        "- keine Handlung",
        "- kein Gate",
        "- keine Strategie",
        "- keine Richtungsvorgabe",
        "",
    ]
    for item in plotted:
        lines.extend(
            [
                f"## `{item['reading']}` - {item['world']}",
                "",
                f"- Paar: `{item['pair']}`",
                f"- Modus: `{item['mode']}`",
                f"- Phase: `{item['phase_hint']}`",
                f"- Bewegung: `{item['dominant_movement']}`",
                f"- Return: `{item['return_pct']}`",
                f"- Range: `{item['range_pct']}`",
                f"- Druck: `{item['pressure_abs']}`",
                f"- Rekopplung: `{item['rekopplung_abs']}`",
                "",
                f"![{item['reading']} {item['world']}]({Path(str(item['image_path'])).as_posix()})",
                "",
            ]
        )

    lines.extend(
        [
            "## Befund",
            "",
            "Die Bilder zeigen dieselbe Achse nicht als festen Verlauf, sondern als wiederkehrenden Feldkanal in unterschiedlichen Weltphasen.",
            "Die sichtbare Weltform unterscheidet sich deutlich zwischen Expansion, Rekopplung, Bruch und Erholung nach Last.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte aus den Bildern eine knappe visuelle Typologie abgeleitet werden: Welche sichtbaren Weltformen korrespondieren mit welcher Rollenqualitaet?",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--axis-details", required=True, type=Path)
    parser.add_argument("--source-detail", action="append", required=True, type=Path)
    parser.add_argument("--root", default=".", type=Path)
    parser.add_argument("--out-dir", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--limit-per-reading", type=int, default=1)
    parser.add_argument("--pad", type=int, default=64)
    args = parser.parse_args()

    axis_rows = _read_rows(args.axis_details)
    source_lookup = _load_source_lookup(args.source_detail)
    joined = _join_details(axis_rows, source_lookup)
    selected = _pick_representatives(joined, args.limit_per_reading)

    plotted: list[dict[str, object]] = []
    for row in selected:
        image_path = _plot(row, args.root, args.out_dir, args.pad)
        plotted.append({**row, "image_path": str(image_path)})

    _write_csv(args.out_csv, plotted)
    _write_md(args.out_md, plotted)
    print(f"joined={len(joined)}")
    print(f"images={len(plotted)}")
    print(f"wrote {args.out_md}")


if __name__ == "__main__":
    main()
