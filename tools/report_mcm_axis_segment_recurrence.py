from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


PASSIVE_FLAGS = {
    "passive_only": 1,
    "read_by_mini_dio": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
}


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def _avg(rows: list[dict[str, str]], key: str) -> float:
    values: list[float] = []
    for row in rows:
        try:
            values.append(float(row.get(key) or 0.0))
        except ValueError:
            continue
    return sum(values) / len(values) if values else 0.0


def _top(counter: Counter[str], limit: int = 6) -> str:
    return " | ".join(f"{key}:{value}" for key, value in counter.most_common(limit)) or "-"


def _signature(row: dict[str, str]) -> str:
    return " / ".join(
        [
            row.get("effect", "-") or "-",
            row.get("before_class", "-") or "-",
            row.get("switch_class", "-") or "-",
            row.get("after_class", "-") or "-",
            row.get("segment_reading", "-") or "-",
        ]
    )


def _reading(world_count: int, count: int, reading_profile: Counter[str]) -> str:
    if world_count >= 3 and count >= 5 and reading_profile.get("paarsegment_rekoppelnd", 0) >= count * 0.6:
        return "wiederkehrend_rekoppelnd"
    if world_count >= 2 and count >= 3:
        return "wiederkehrend_offen"
    if count >= 2:
        return "lokal_wiederholt"
    return "situationssegment"


def _build(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    pair_rows = [row for row in rows if str(row.get("match_kind", "")).startswith("paar")]
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in pair_rows:
        groups[_signature(row)].append(row)

    out: list[dict[str, object]] = []
    for signature, group in groups.items():
        worlds = Counter(row.get("world", "-") or "-" for row in group)
        sources = Counter(row.get("source", "-") or "-" for row in group)
        readings = Counter(row.get("segment_reading", "-") or "-" for row in group)
        ticks = Counter(f"{row.get('world', '-') or '-'}:{row.get('tick', '-') or '-'}" for row in group)
        world_count = len(worlds)
        out.append(
            {
                **PASSIVE_FLAGS,
                "signature": signature,
                "count": len(group),
                "world_count": world_count,
                "worlds": _top(worlds),
                "sources": _top(sources),
                "segment_readings": _top(readings),
                "sample_ticks": _top(ticks, limit=10),
                "avg_pressure_delta": round(_avg(group, "pressure_delta"), 6),
                "avg_rekopplung_delta": round(_avg(group, "rekopplung_delta"), 6),
                "recurrence_reading": _reading(world_count, len(group), readings),
            }
        )
    out.sort(key=lambda row: (-int(row["count"]), -int(row["world_count"]), str(row["signature"])))
    return out


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else [*PASSIVE_FLAGS.keys(), "signature", "count"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, object]]) -> None:
    state_counts = Counter(str(row["recurrence_reading"]) for row in rows)
    lines = [
        "# MCM-Zentrumsachse: Kontaktsegment-Wiederkehr",
        "",
        "## Zweck",
        "",
        "Diese Datei prueft, welche lokalen Achsen-Kontaktsegmente wiederkehren und welche nur situationsbedingt auftreten.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Ruecklesung",
        "- keine Handlung",
        "- kein Gate",
        "- keine Strategie",
        "",
        "## Wiederkehrstatus",
        "",
        "| Status | Anzahl |",
        "|---|---:|",
    ]
    for state, count in state_counts.most_common():
        lines.append(f"| `{state}` | {count} |")

    lines.extend(
        [
            "",
            "## Signaturen",
            "",
            "| Signatur | Anzahl | Welten | Pressure Delta | Rekopplung Delta | Lesung |",
            "|---|---:|---:|---:|---:|---|",
        ]
    )
    for row in rows:
        lines.append(
            f"| `{row['signature']}` | {row['count']} | {row['world_count']} | "
            f"{row['avg_pressure_delta']} | {row['avg_rekopplung_delta']} | `{row['recurrence_reading']}` |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Wiederkehrende Kontaktsegmente sind keine neuen Regeln.",
            "Sie markieren nur, welche lokale Achsenberuehrung in mehreren Welten erneut als Feldwirkung erscheint.",
            "",
            "Arbeitsableitung:",
            "",
            "```text",
            "Aus einer lokalen Achsenberuehrung wird erst dann eine tragendere Bedeutungsnaehe,",
            "wenn aehnliche Kontaktqualitaet ueber mehrere Weltlagen erneut erscheint.",
            "```",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die staerkste wiederkehrende Signatur gegen Nachbarschaft und Feldmitte gelesen werden.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--segments", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    rows = _build(_read_rows(args.segments))
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"signatures={len(rows)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
