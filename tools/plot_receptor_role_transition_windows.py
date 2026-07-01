from __future__ import annotations

import argparse
import csv
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


def _plot(row: dict[str, str], candles: list[dict[str, str]], image_dir: Path, radius: int) -> Path:
    world = row["world"]
    transition = row["transition"]
    tick = _int(row, "start_tick")
    index = max(0, min(len(candles) - 1, tick - 1))
    start = max(0, index - radius)
    end = min(len(candles), index + radius + 1)
    window = candles[start:end]
    xs = list(range(start + 1, end + 1))
    opens = [_float(item, "open") for item in window]
    highs = [_float(item, "high") for item in window]
    lows = [_float(item, "low") for item in window]
    closes = [_float(item, "close") for item in window]

    fig, ax = plt.subplots(figsize=(9.5, 4.2))
    fig.patch.set_facecolor("#0b0f14")
    ax.set_facecolor("#11161d")
    ax.grid(True, color="#253140", alpha=0.45, linewidth=0.8)
    for x, open_value, close_value, high_value, low_value in zip(xs, opens, closes, highs, lows):
        color = "#37c47a" if close_value >= open_value else "#d65a5a"
        ax.vlines(x, low_value, high_value, color="#6d7890", linewidth=1.0, alpha=0.85)
        ax.vlines(x, open_value, close_value, color=color, linewidth=4.0, alpha=0.85)
    ax.plot(xs, closes, color="#7aa6ff", linewidth=1.1, alpha=0.6)
    ax.axvline(tick, color="#f6b04b", linewidth=1.8, alpha=0.95)
    ax.set_title(
        f"{world} | {transition} | tick {tick} | raw {_float(row, 'current_raw_field_intake'):.3f} | rek {_float(row, 'current_rekopplung'):.3f}",
        color="#d8e5ff",
        fontsize=10,
    )
    ax.tick_params(colors="#8fa0bd")
    for spine in ax.spines.values():
        spine.set_color("#2a3545")
    safe_transition = transition.replace("->", "_to_").replace("/", "_")
    path = image_dir / f"1216_{world}_{safe_transition}_tick_{tick}.png"
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


def _write_md(rows: list[dict[str, str]], out: Path) -> None:
    lines = [
        "# Befund 1216 - Direkte Rollenuebergang-Chartfenster",
        "",
        "## Grundfrage",
        "",
        "Wie sehen die direkten Uebergaenge `Offen -> Rand` und `Rand -> Offen` in der Rohwelt aus?",
        "",
        "Die orange Linie markiert den Starttick der neuen Rolle.",
        "",
    ]
    for transition in ["offene_variante->spannungsrand_kippnaehe", "spannungsrand_kippnaehe->offene_variante"]:
        lines.extend([f"## {transition}", ""])
        for row in [item for item in rows if item["transition"] == transition]:
            image_name = Path(row["image"]).name
            lines.extend(
                [
                    f"- `{row['world']}` Tick `{row['start_tick']}`: vorherige Dauer `{row['previous_duration']}`, aktuelle Dauer `{row['current_duration']}`, Rohfeld `{float(row['current_raw_field_intake']):.4f}`, Rekopplung `{float(row['current_rekopplung']):.4f}`, Strain `{float(row['current_strain']):.4f}`",
                    f"![{row['world']} {transition} Tick {row['start_tick']}](../bilder/{image_name})",
                    "",
                ]
            )
    lines.extend(
        [
            "## Ableitung",
            "",
            "Diese Bilder dienen der passiven Feldphasen-Lesung. Sie pruefen, ob Offenheit eine Vorphase von Rand/Kipp ist oder ob Rand/Kipp als direkter Impulszustand erscheint.",
            "",
            "Wie es weitergeht: Die Bilder sollten gegen die Segmentwerte gelesen werden. Danach kann die Feldphasen-Mechanik als Vorraum/Pendelbewegung dokumentiert werden.",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--transitions", required=True)
    parser.add_argument("--world", action="append", required=True, type=_parse_world)
    parser.add_argument("--out", required=True)
    parser.add_argument("--image-dir", required=True)
    parser.add_argument("--per-transition", type=int, default=4)
    parser.add_argument("--radius", type=int, default=35)
    args = parser.parse_args()

    transitions = _load(Path(args.transitions))
    worlds = {label: _load(path) for label, path in args.world}
    image_dir = Path(args.image_dir)
    image_dir.mkdir(parents=True, exist_ok=True)

    selected: list[dict[str, str]] = []
    for transition in ["offene_variante->spannungsrand_kippnaehe", "spannungsrand_kippnaehe->offene_variante"]:
        rows = [row for row in transitions if row.get("transition") == transition]
        rows = sorted(rows, key=lambda row: _float(row, "current_raw_field_intake"), reverse=True)[: args.per_transition]
        selected.extend(rows)

    image_rows: list[dict[str, str]] = []
    for row in selected:
        candles = worlds.get(row["world"])
        if not candles:
            continue
        path = _plot(row, candles, image_dir, args.radius)
        item = dict(row)
        item["image"] = str(path)
        image_rows.append(item)
    _write_md(image_rows, Path(args.out))
    print(f"wrote {args.out}")
    print(f"wrote {len(image_rows)} images to {image_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
