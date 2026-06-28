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


def _int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _short(token: str) -> str:
    return token.replace("dio_mcm_episode_", "")


def _parts(value: object) -> list[str]:
    text = str(value or "").strip()
    if not text:
        return []
    return [part.strip() for part in text.split("->")]


def _rank(cls: str) -> int:
    return CLASS_RANK.get(cls, 0)


def _landscape_by_short(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for row in rows:
        short = row.get("short_token") or _short(row.get("token", ""))
        if short:
            out[short] = row
    return out


def _reading(memory: dict[str, str], current: dict[str, str] | None) -> dict[str, str]:
    short = memory.get("short_token", "")
    classes = _parts(memory.get("class_sequence", ""))
    last_class = classes[-1] if classes else "-"
    last_rank = _rank(last_class)
    max_rank = max((_rank(cls) for cls in classes), default=0)
    current_class = (current or {}).get("anchor_class", "-") or "-"
    current_rank = _rank(current_class)
    trend = memory.get("role_movement_quality", "")
    stability = memory.get("stability_quality", "")
    drift = memory.get("drift_quality", "")

    if current is None:
        read_state = "nicht_wiedergefunden"
    elif trend == "role_core_near_retained":
        read_state = "kernnaehe_gehalten" if current_rank >= 3 else "kernnaehe_verloren"
    elif trend == "role_condensing":
        if current_rank >= max(1, max_rank):
            read_state = "verdichtung_gehalten"
        elif current_rank > last_rank:
            read_state = "weiter_verdichtet"
        elif current_rank == last_rank:
            read_state = "verdichtung_stabil"
        else:
            read_state = "verdichtung_entlastet_oder_driftet"
    elif trend == "role_drifting":
        read_state = "drift_bestaetigt" if current_rank != last_rank else "drift_beruhigt"
    elif trend == "role_releasing":
        read_state = "entlastung_bestaetigt" if current_rank <= last_rank else "rekopplung_gegen_entlastung"
    elif trend == "role_stable":
        read_state = "stabil_bestaetigt" if current_rank == last_rank else "stabilitaet_gebrochen"
    else:
        read_state = "offen_gelesen"

    return {
        "role_symbol": memory.get("role_symbol", ""),
        "short_token": short,
        "memory_trend": trend,
        "memory_stability": stability,
        "memory_drift": drift,
        "memory_class_sequence": memory.get("class_sequence", ""),
        "memory_last_class": last_class,
        "memory_max_rank": str(max_rank),
        "current_class": current_class,
        "current_weight": (current or {}).get("total_weight", "0"),
        "current_world_span": (current or {}).get("max_world_span", "0"),
        "current_duration": f"{_float((current or {}).get('weighted_duration', '0')):.6f}",
        "read_state": read_state,
        "rank_delta_from_last": str(current_rank - last_rank),
        "rank_delta_from_max": str(current_rank - max_rank),
    }


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _table(rows: list[dict[str, str]], limit: int = 18) -> list[str]:
    lines = [
        "| Symbol | Token | Memory | Aktuell | Lesung | Rangdelta |",
        "|---|---|---|---|---|---:|",
    ]
    for row in rows[:limit]:
        lines.append(
            f"| `{row['role_symbol']}` | `{row['short_token']}` | {row['memory_trend']} / {row['memory_stability']} | {row['current_class']} | {row['read_state']} | {row['rank_delta_from_last']} |"
        )
    return lines


def _write_md(path: Path, rows: list[dict[str, str]], *, memory_label: str, landscape_label: str) -> None:
    counts = Counter(row["read_state"] for row in rows)
    trend_counts = Counter(row["memory_trend"] for row in rows)
    lines: list[str] = []
    lines.append("# MCM-Rollenbewegungs-Memory Lesung")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append(f"Diese Diagnose liest passive Rollenbewegungs-Memory aus `{memory_label}` gegen die Folgelandschaft `{landscape_label}`.")
    lines.append("Geprueft wird, ob `dio_role_*` stabil bleibt, weiter verdichtet, entlastet oder driftet.")
    lines.append("")
    lines.append("## Profil")
    lines.append("")
    lines.append(f"- Gelesene Rollen-Symbole: `{len(rows)}`")
    lines.append("")
    lines.append("### Lesestatus")
    lines.append("")
    lines.append("| Status | Anzahl |")
    lines.append("|---|---:|")
    for name, count in counts.most_common():
        lines.append(f"| {name} | {count} |")
    lines.append("")
    lines.append("### Memory-Trends")
    lines.append("")
    lines.append("| Trend | Anzahl |")
    lines.append("|---|---:|")
    for name, count in trend_counts.most_common():
        lines.append(f"| {name} | {count} |")
    lines.append("")
    lines.append("## Starke Bestaetigungen / Bewegungen")
    lines.append("")
    priority = sorted(
        rows,
        key=lambda row: (
            row["read_state"] not in {"verdichtung_gehalten", "kernnaehe_gehalten", "stabil_bestaetigt", "weiter_verdichtet"},
            -_int(row["current_weight"]),
            row["short_token"],
        ),
    )
    lines.extend(_table(priority))
    lines.append("")
    lines.append("## Befund")
    lines.append("")
    lines.append("Die Rollenbewegungs-Memory kann gegen eine Folgelandschaft gelesen werden, ohne daraus Handlung abzuleiten.")
    lines.append("Relevant ist nicht, ob ein Token dieselbe Klasse behaelt, sondern ob die gespeicherte Bewegungsqualitaet getragen bleibt.")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    lines.append("Als naechstes sollte die Lesung mit einer wirklich neuen vierten Landschaft wiederholt werden. Dann kann geprueft werden, ob `dio_role_*` generalisiert oder nur die bisherige Weltfolge beschreibt.")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--memory", required=True, type=Path)
    parser.add_argument("--landscape", required=True, type=Path)
    parser.add_argument("--memory-label", default="memory")
    parser.add_argument("--landscape-label", default="landscape")
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    memory_rows = _read(args.memory)
    current = _landscape_by_short(_read(args.landscape))
    rows = [_reading(row, current.get(row.get("short_token", ""))) for row in memory_rows]
    rows.sort(key=lambda row: (row["read_state"], row["short_token"]))
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows, memory_label=args.memory_label, landscape_label=args.landscape_label)
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
