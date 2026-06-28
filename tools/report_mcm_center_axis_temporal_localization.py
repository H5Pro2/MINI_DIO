from __future__ import annotations

import argparse
import csv
import statistics
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable


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


def _row_text(row: dict[str, str]) -> str:
    return " ".join(str(value or "") for value in row.values())


def _float(row: dict[str, str], *keys: str) -> float | None:
    for key in keys:
        value = row.get(key)
        if value in (None, ""):
            continue
        try:
            return float(str(value).replace(",", "."))
        except ValueError:
            continue
    return None


def _tick(row: dict[str, str]) -> float | None:
    return _float(row, "event_tick", "start_tick", "tick", "start", "index")


def _world(row: dict[str, str], fallback: str) -> str:
    for key in ("world", "source_world", "dataset", "source_debug"):
        value = str(row.get(key, "") or "").strip()
        if value:
            return value
    return fallback


def _phase(tick: float, min_tick: float, max_tick: float) -> str:
    if max_tick <= min_tick:
        return "punktuell"
    position = (tick - min_tick) / (max_tick - min_tick)
    if position < 0.25:
        return "frueh"
    if position < 0.50:
        return "frueh_mitte"
    if position < 0.75:
        return "spaet_mitte"
    return "spaet"


def _axis_hits(rows_by_source: Iterable[tuple[str, dict[str, str]]], a: str, b: str) -> list[dict[str, object]]:
    hits: list[dict[str, object]] = []
    for source_name, row in rows_by_source:
        text = _row_text(row)
        if a not in text and b not in text:
            continue
        tick = _tick(row)
        if tick is None:
            continue
        pair_hit = (
            (a in text and b in text)
            or f"{a}->{b}" in text
            or f"{b}->{a}" in text
            or f"{a}<->{b}" in text
            or f"{b}<->{a}" in text
        )
        hits.append(
            {
                "source": source_name,
                "world": _world(row, source_name),
                "tick": tick,
                "pair_hit": pair_hit,
                "effect": str(row.get("dominant_effect", "") or row.get("switch_class", "") or "-"),
                "post_state": str(row.get("post_state", "") or row.get("after_class", "") or "-"),
                "strain": _float(row, "avg_strain", "strain"),
                "rekopplung": _float(row, "avg_rekopplung", "rekopplung"),
                "pressure_delta": _float(row, "pressure_delta", "avg_pressure_delta"),
                "rekopplung_delta": _float(row, "rekopplung_delta", "avg_rekopplung_delta"),
            }
        )
    return hits


def _fmt_counter(counter: Counter[str], limit: int = 5) -> str:
    if not counter:
        return "-"
    return " | ".join(f"{key}:{value}" for key, value in counter.most_common(limit))


def _avg(values: Iterable[float | None]) -> float:
    cleaned = [value for value in values if value is not None]
    return sum(cleaned) / len(cleaned) if cleaned else 0.0


def _summarize_axis(axis: str, hits: list[dict[str, object]]) -> list[dict[str, object]]:
    by_world: dict[str, list[dict[str, object]]] = defaultdict(list)
    for hit in hits:
        by_world[str(hit["world"])].append(hit)

    rows: list[dict[str, object]] = []
    for world, world_hits in sorted(by_world.items(), key=lambda item: (-len(item[1]), item[0])):
        ticks = [float(hit["tick"]) for hit in world_hits]
        min_tick = min(ticks)
        max_tick = max(ticks)
        phases = Counter(_phase(tick, min_tick, max_tick) for tick in ticks)
        pair_hits = sum(1 for hit in world_hits if bool(hit["pair_hit"]))

        if len(ticks) >= 4:
            quartiles = statistics.quantiles(ticks, n=4, method="inclusive")
            q1, q2, q3 = quartiles[0], statistics.median(ticks), quartiles[2]
        else:
            q1 = q2 = q3 = statistics.median(ticks)

        densest_phase, densest_count = phases.most_common(1)[0]
        if pair_hits > 0 and densest_count >= max(3, len(world_hits) * 0.30):
            reading = "zeitlich_lokalisierte_achse"
        elif pair_hits > 0:
            reading = "breit_verteilte_achse"
        else:
            reading = "knoten_naehe_ohne_paarverdichtung"

        rows.append(
            {
                "axis": axis,
                "world": world,
                "events": len(world_hits),
                "pair_events": pair_hits,
                "tick_min": round(min_tick, 3),
                "tick_q1": round(q1, 3),
                "tick_median": round(q2, 3),
                "tick_q3": round(q3, 3),
                "tick_max": round(max_tick, 3),
                "phase_profile": _fmt_counter(phases),
                "dominant_effects": _fmt_counter(Counter(str(hit["effect"]) for hit in world_hits)),
                "post_states": _fmt_counter(Counter(str(hit["post_state"]) for hit in world_hits)),
                "avg_rekopplung": round(_avg(hit["rekopplung"] for hit in world_hits), 6),
                "avg_strain": round(_avg(hit["strain"] for hit in world_hits), 6),
                "avg_pressure_delta": round(_avg(hit["pressure_delta"] for hit in world_hits), 6),
                "avg_rekopplung_delta": round(_avg(hit["rekopplung_delta"] for hit in world_hits), 6),
                "reading": reading,
            }
        )
    return rows


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else [
        "axis",
        "world",
        "events",
        "pair_events",
        "reading",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# MCM-Zentrumsachse: zeitliche Lokalisierung",
        "",
        "## Zweck",
        "",
        "Diese Datei liest, in welchen Weltphasen eine reziproke Zentrumsachse gehauft erscheint.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Ruecklesung",
        "- keine Handlung",
        "- kein Gate",
        "- keine Strategie",
        "",
        "## Weltphasen",
        "",
        "| Achse | Welt | Events | Paar-Events | Tickbereich | Phasen | Rekopplung | Strain | Lesung |",
        "|---|---|---:|---:|---|---|---:|---:|---|",
    ]
    for row in rows:
        tick_range = f"{row['tick_min']} / {row['tick_q1']} / {row['tick_median']} / {row['tick_q3']} / {row['tick_max']}"
        lines.append(
            f"| `{row['axis']}` | `{row['world']}` | {row['events']} | {row['pair_events']} | "
            f"`{tick_range}` | `{row['phase_profile']}` | {row['avg_rekopplung']} | {row['avg_strain']} | `{row['reading']}` |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Eine weltlich getragene Achse ist staerker, wenn sie nicht nur insgesamt haeufig erscheint,",
            "sondern in bestimmten Weltphasen verdichtet oder wiederholt als Paarereignis lesbar wird.",
            "",
            "Arbeitsableitung:",
            "",
            "```text",
            "Zentrumsqualitaet kann als zeitlich lokalisierte Feldachse erscheinen:",
            "nicht nur ein Punkt im Bedeutungsraum, sondern eine wiederkehrende Lage ueber Weltphasen.",
            "```",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte geprueft werden, ob diese zeitlichen Achsenlagen mit Topologie-Rollenwechseln zusammenfallen.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--axis", action="append", required=True, help="Format: a<->b")
    parser.add_argument("--event-file", action="append", required=True)
    parser.add_argument("--out-md", required=True)
    parser.add_argument("--out-csv", required=True)
    args = parser.parse_args()

    rows_by_source: list[tuple[str, dict[str, str]]] = []
    for filename in args.event_file:
        path = Path(filename)
        for row in _read_rows(path):
            rows_by_source.append((path.name, row))

    output_rows: list[dict[str, object]] = []
    for axis in args.axis:
        if "<->" not in axis:
            raise SystemExit(f"axis must use <->: {axis}")
        a, b = [part.strip() for part in axis.split("<->", 1)]
        output_rows.extend(_summarize_axis(axis, _axis_hits(rows_by_source, a, b)))

    _write_csv(Path(args.out_csv), output_rows)
    _write_md(Path(args.out_md), output_rows)
    print(f"axes={len(args.axis)}")
    print(f"rows={len(output_rows)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
