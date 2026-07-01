from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt


def _float(row: dict[str, str], key: str) -> float:
    try:
        value = float(row.get(key, "") or 0.0)
    except ValueError:
        return 0.0
    return 0.0 if value != value else value


def _int(row: dict[str, str], key: str) -> int:
    try:
        return int(float(row.get(key, "") or 0))
    except ValueError:
        return 0


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _parse_world(value: str) -> tuple[str, Path]:
    parts = value.split("=")
    if len(parts) != 2:
        raise argparse.ArgumentTypeError("world must be LABEL=DATA_CSV")
    return parts[0], Path(parts[1])


def _select_examples(events: list[dict[str, str]], role: str, per_role: int) -> list[dict[str, str]]:
    rows = [row for row in events if row.get("role") == role]
    return sorted(rows, key=lambda row: _float(row, "raw_field_intake"), reverse=True)[:per_role]


def _plot_one(row: dict[str, str], candles: list[dict[str, str]], out_dir: Path, radius: int) -> Path:
    world = row["world"]
    role = row["role"]
    tick = _int(row, "tick")
    index = max(0, min(len(candles) - 1, tick - 1))
    start = max(0, index - radius)
    end = min(len(candles), index + radius + 1)
    window = candles[start:end]
    xs = list(range(start + 1, end + 1))
    closes = [_float(item, "close") for item in window]
    highs = [_float(item, "high") for item in window]
    lows = [_float(item, "low") for item in window]
    opens = [_float(item, "open") for item in window]

    fig, ax = plt.subplots(figsize=(9.5, 4.2))
    ax.set_facecolor("#11161d")
    fig.patch.set_facecolor("#0b0f14")
    ax.grid(True, color="#253140", alpha=0.45, linewidth=0.8)

    for x, open_value, close_value, high_value, low_value in zip(xs, opens, closes, highs, lows):
        color = "#37c47a" if close_value >= open_value else "#d65a5a"
        ax.vlines(x, low_value, high_value, color="#6d7890", linewidth=1.0, alpha=0.85)
        ax.vlines(x, open_value, close_value, color=color, linewidth=4.0, alpha=0.85)

    ax.axvline(tick, color="#f6b04b", linewidth=1.6, alpha=0.9)
    ax.plot(xs, closes, color="#7aa6ff", linewidth=1.1, alpha=0.6)
    ax.set_title(
        f"{world} | {role} | tick {tick} | raw {_float(row, 'raw_field_intake'):.3f} | rek {_float(row, 'rekopplung'):.3f}",
        color="#d8e5ff",
        fontsize=10,
    )
    ax.tick_params(colors="#8fa0bd")
    for spine in ax.spines.values():
        spine.set_color("#2a3545")

    safe_role = role.replace("/", "_")
    out_path = out_dir / f"1213_{world}_{safe_role}_tick_{tick}.png"
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


def _write_md(image_rows: list[dict[str, str]], out: Path) -> None:
    lines = [
        "# Befund 1213 - Chartfenster der realen Hochlastrollen",
        "",
        "## Grundfrage",
        "",
        "Sind Hochlast-Offenheit und Hochlast-Randnaehe auch in der sichtbaren Weltform unterscheidbar?",
        "",
        "Die Bilder zeigen passive Chartfenster um die staerksten Hochlast-Ereignisse. Die orange Linie markiert den Ereignis-Tick.",
        "",
    ]
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in image_rows:
        grouped[row["role"]].append(row)
    for role, rows in grouped.items():
        lines.extend([f"## {role}", ""])
        for item in rows:
            image_path = item["image"].replace("\\", "/")
            lines.extend(
                [
                    f"- `{item['world']}` Tick `{item['tick']}`: Rohfeld `{float(item['raw_field_intake']):.4f}`, Rekopplung `{float(item['rekopplung']):.4f}`, Strain `{float(item['strain']):.4f}`",
                    f"![{item['world']} {item['role']} Tick {item['tick']}](../bilder/{Path(image_path).name})",
                    "",
                ]
            )

    lines.extend(
        [
            "## Ableitung",
            "",
            "Die Chartfenster sind keine Strategieauswertung. Sie dienen nur dazu, Feldrollen an sichtbare Weltform zurueckzubinden.",
            "",
            "Wie es weitergeht: Die Bildfenster sollten gegen Sinneswerte gelesen werden: Offenheit als Uebergangsraum, Rand/Kipp als hohe Aufnahme plus schwache Rekopplung.",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--events", required=True)
    parser.add_argument("--world", action="append", required=True, type=_parse_world)
    parser.add_argument("--out", required=True)
    parser.add_argument("--image-dir", required=True)
    parser.add_argument("--per-role", type=int, default=3)
    parser.add_argument("--radius", type=int, default=30)
    args = parser.parse_args()

    events = _load(Path(args.events))
    worlds = {label: _load(path) for label, path in args.world}
    image_dir = Path(args.image_dir)
    image_dir.mkdir(parents=True, exist_ok=True)

    selected = []
    for role in ["offene_variante", "spannungsrand_kippnaehe"]:
        selected.extend(_select_examples(events, role, args.per_role))

    image_rows: list[dict[str, str]] = []
    for row in selected:
        world = row["world"]
        if world not in worlds:
            continue
        path = _plot_one(row, worlds[world], image_dir, args.radius)
        item = dict(row)
        item["image"] = str(path)
        image_rows.append(item)

    _write_md(image_rows, Path(args.out))
    print(f"wrote {args.out}")
    print(f"wrote {len(image_rows)} images to {image_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
