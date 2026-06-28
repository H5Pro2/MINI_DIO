from __future__ import annotations

import argparse
import csv
from pathlib import Path

import matplotlib.pyplot as plt


def _read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


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


def _slice(rows: list[dict[str, str]], start: int, end: int) -> tuple[int, list[dict[str, str]]]:
    start = max(0, start)
    end = min(len(rows) - 1, end)
    return start, rows[start : end + 1]


def _safe_name(value: str) -> str:
    allowed = []
    for char in value:
        if char.isalnum() or char in ("_", "-"):
            allowed.append(char)
        else:
            allowed.append("_")
    return "".join(allowed).strip("_")


def _plot_window(row: dict[str, str], root: Path, out_dir: Path, pad: int) -> Path:
    data_path = root / row["data_file"]
    candles = _read(data_path)
    tick_min = _safe_int(row["tick_min"])
    tick_max = _safe_int(row["tick_max"])
    start, window = _slice(candles, tick_min - pad, tick_max + pad)
    xs = list(range(start, start + len(window)))
    closes = [_safe_float(item.get("close")) for item in window]
    highs = [_safe_float(item.get("high")) for item in window]
    lows = [_safe_float(item.get("low")) for item in window]

    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=150)
    ax.plot(xs, closes, color="#5d8fd8", linewidth=1.8, label="Close")
    ax.fill_between(xs, lows, highs, color="#5d8fd8", alpha=0.12, label="High-Low")
    ax.axvspan(tick_min, tick_max, color="#ff9f43", alpha=0.22, label="MCM-Achsenfenster")
    ax.axvline(_safe_int(row["tick_mid"]), color="#ff6b6b", linewidth=1.2, linestyle="--", label="Schwerpunkt")
    ax.set_title(f"{row['world']} | {row['pair']} | {row['chart_zone']}")
    ax.set_xlabel("Tick")
    ax.set_ylabel("Preis")
    ax.grid(True, alpha=0.18)
    ax.legend(loc="best", fontsize=8)
    fig.tight_layout()

    file_name = "1011_" + _safe_name(f"{row['world']}_{row['pair']}_{row['tick_min']}_{row['tick_max']}") + ".png"
    out_path = out_dir / file_name
    out_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path)
    plt.close(fig)
    return out_path


def write_md(rows: list[dict[str, str]], image_paths: list[Path], out_md: Path) -> None:
    lines = [
        "# 1011 - Aktive Achsen als Chartgrafik",
        "",
        "Passive Visualisierung ausgewaehlter MCM-Achsenfenster gegen den OHLCV-Chart.",
        "",
        "Die orange Flaeche markiert das MCM-Achsenfenster. Die rote Linie markiert den Schwerpunkt innerhalb dieses Fensters.",
        "",
    ]
    for row, image_path in zip(rows, image_paths):
        lines.extend(
            [
                f"## {row['world']} - `{row['pair']}`",
                "",
                f"- Ticks: `{row['tick_min']}-{row['tick_max']}`",
                f"- Chartzone: `{row['chart_zone']}`",
                f"- MCM-Bewegung: `{row['dominant_movement']}`",
                "",
                f"![{row['world']} {row['pair']}]({image_path.as_posix()})",
                "",
            ]
        )
    lines.extend(
        [
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte aus diesen Bildern eine Chartzonen-Typologie abgeleitet werden: Rekopplung nach Bruch, Druckfenster, Konsolidierung mit Spannung und getragene Expansion.",
            "",
        ]
    )
    out_md.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--windows", required=True, type=Path)
    parser.add_argument("--root", default=".", type=Path)
    parser.add_argument("--out-dir", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--pad", type=int, default=48)
    args = parser.parse_args()

    rows = _read(args.windows)
    rows.sort(key=lambda row: (_safe_float(row.get("mcm_pressure_abs")) + _safe_float(row.get("mcm_rekopplung_abs"))), reverse=True)
    selected = rows[: args.limit]
    image_paths = [_plot_window(row, args.root, args.out_dir, args.pad) for row in selected]
    write_md(selected, image_paths, args.out_md)
    print(f"images={len(image_paths)}")
    print(f"wrote {args.out_md}")


if __name__ == "__main__":
    main()
