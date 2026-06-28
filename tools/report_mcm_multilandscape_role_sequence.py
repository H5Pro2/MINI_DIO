from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


CLASS_RANK = {
    "-": 0,
    "schwacher_anschluss": 1,
    "schwacher_brueckenpfad": 1,
    "lokaler_anschlussanker": 2,
    "starker_anschlussanker": 3,
    "brueckenkern": 4,
}


def _read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def _int(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def _float(value: str) -> float:
    try:
        return float(value or 0.0)
    except ValueError:
        return 0.0


def _short(token: str) -> str:
    return token.replace("dio_mcm_episode_", "")


def _load_landscape(label: str, path: Path) -> dict[str, dict[str, str]]:
    rows = _read(path)
    out: dict[str, dict[str, str]] = {}
    for row in rows:
        token = row.get("token", "")
        if not token:
            continue
        out[token] = {
            "class": row.get("anchor_class", "-") or "-",
            "weight": row.get("total_weight", "0") or "0",
            "duration": row.get("weighted_duration", "0") or "0",
            "world_span": row.get("max_world_span", "0") or "0",
            "path_class": row.get("path_class", "-") or "-",
            "movement": row.get("movement", "-") or "-",
            "label": label,
        }
    return out


def _trend(classes: list[str]) -> str:
    ranks = [CLASS_RANK.get(value, 0) for value in classes]
    nonzero = [rank for rank in ranks if rank > 0]
    if not nonzero:
        return "nicht_sichtbar"
    if all(ranks[index] <= ranks[index + 1] for index in range(len(ranks) - 1)) and ranks[0] < ranks[-1]:
        return "aufsteigende_verdichtung"
    if all(ranks[index] >= ranks[index + 1] for index in range(len(ranks) - 1)) and ranks[0] > ranks[-1]:
        return "absteigende_entlastung"
    if max(ranks) >= 4 and ranks[-1] >= 3:
        return "kernnah_gehalten"
    if len(set(ranks)) > 1:
        return "rollendrift"
    return "stabile_rolle"


def _rows(landscapes: list[tuple[str, dict[str, dict[str, str]]]]) -> list[dict[str, str]]:
    tokens = sorted({token for _, landscape in landscapes for token in landscape})
    out: list[dict[str, str]] = []
    for token in tokens:
        classes: list[str] = []
        weights: list[int] = []
        durations: list[float] = []
        world_spans: list[int] = []
        row: dict[str, str] = {"token": token, "short_token": _short(token)}
        for label, landscape in landscapes:
            data = landscape.get(token, {})
            cls = data.get("class", "-")
            weight = _int(data.get("weight", "0"))
            duration = _float(data.get("duration", "0"))
            world_span = _int(data.get("world_span", "0"))
            classes.append(cls)
            weights.append(weight)
            durations.append(duration)
            world_spans.append(world_span)
            row[f"{label}_class"] = cls
            row[f"{label}_weight"] = str(weight)
            row[f"{label}_duration"] = f"{duration:.6f}"
            row[f"{label}_world_span"] = str(world_span)
        row["class_sequence"] = " -> ".join(classes)
        row["weight_sequence"] = " -> ".join(str(value) for value in weights)
        row["duration_sequence"] = " -> ".join(f"{value:.2f}" for value in durations)
        row["world_span_sequence"] = " -> ".join(str(value) for value in world_spans)
        row["trend"] = _trend(classes)
        row["max_rank"] = str(max(CLASS_RANK.get(value, 0) for value in classes))
        row["weight_delta_total"] = str(weights[-1] - weights[0])
        out.append(row)
    out.sort(key=lambda row: (-_int(row["max_rank"]), row["trend"], row["short_token"]))
    return out


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _top(rows: list[dict[str, str]], trend: str, limit: int = 12) -> list[dict[str, str]]:
    return [row for row in rows if row["trend"] == trend][:limit]


def _table(rows: list[dict[str, str]]) -> list[str]:
    lines = [
        "| Token | Klassenfolge | Gewichtfolge | Weltspanne | Trend |",
        "|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['short_token']}` | {row['class_sequence']} | {row['weight_sequence']} | {row['world_span_sequence']} | {row['trend']} |"
        )
    return lines


def _write_md(path: Path, rows: list[dict[str, str]]) -> None:
    counts = Counter(row["trend"] for row in rows)
    lines: list[str] = []
    lines.append("# MCM-Mehrlandschaft Rollenfolge")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append("Diese Diagnose vergleicht drei Anschlussanker-Landschaften als Folge: 894, 901 und 911.")
    lines.append("Ziel ist zu pruefen, ob Rollenreife und Rollendrift als Verlauf sichtbar werden.")
    lines.append("")
    lines.append("## Trendprofil")
    lines.append("")
    lines.append("| Trend | Anzahl |")
    lines.append("|---|---:|")
    for trend, count in counts.most_common():
        lines.append(f"| {trend} | {count} |")
    lines.append("")
    lines.append("## Kernnah Gehalten")
    lines.append("")
    lines.extend(_table(_top(rows, "kernnah_gehalten")))
    lines.append("")
    lines.append("## Aufsteigende Verdichtung")
    lines.append("")
    lines.extend(_table(_top(rows, "aufsteigende_verdichtung")))
    lines.append("")
    lines.append("## Rollendrift")
    lines.append("")
    lines.extend(_table(_top(rows, "rollendrift")))
    lines.append("")
    lines.append("## Absteigende Entlastung")
    lines.append("")
    lines.extend(_table(_top(rows, "absteigende_entlastung")))
    lines.append("")
    lines.append("## Befund")
    lines.append("")
    lines.append("Die dritte Landschaft zeigt, dass Rollen nicht nur einmalig kippen.")
    lines.append("Einige Tokens bleiben kernnah oder verdichten weiter, andere driften oder entlasten sich.")
    lines.append("Damit wird Rollenreife als dynamischer Verlauf sichtbarer: nicht feste Leiter, sondern feldabhaengige Rollenbewegung.")
    lines.append("")
    lines.append("Besonders relevant:")
    lines.append("")
    lines.append("- `0b7nep9` bleibt nach dem Rollenwechsel kernnah.")
    lines.append("- `0ykar6i` faellt nicht auf schwach zurueck, sondern bleibt als starker Anschlussanker in der Naehe des Kernraums.")
    lines.append("- `1jx2k4i` bleibt ebenfalls stark/kernnah.")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    lines.append("Als naechstes sollte die Rollenfolge in eine semantische Memory-Regel uebersetzt werden: nicht harte Klassen speichern, sondern Rollenbewegung, Stabilitaet und Driftqualitaet.")
    path.write_text("\n".join(lines), encoding="utf-8")


def _parse_landscapes(items: list[str]) -> list[tuple[str, Path]]:
    parsed: list[tuple[str, Path]] = []
    for item in items:
        if "=" not in item:
            raise SystemExit(f"landscape must be LABEL=PATH, got {item}")
        label, raw_path = item.split("=", 1)
        parsed.append((label, Path(raw_path)))
    return parsed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--landscape", action="append", required=True)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    landscapes = [(label, _load_landscape(label, path)) for label, path in _parse_landscapes(args.landscape)]
    rows = _rows(landscapes)
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
