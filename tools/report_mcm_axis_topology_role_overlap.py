from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


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


def _short(value: str) -> str:
    return str(value or "").replace("dio_mcm_episode_", "").strip()


def _pair_parts(pair: str) -> tuple[str, str] | None:
    pair = str(pair or "")
    if "->" not in pair:
        return None
    left, right = pair.split("->", 1)
    return _short(left), _short(right)


def _axis_parts(axis: str) -> tuple[str, str]:
    if "<->" not in axis:
        raise SystemExit(f"axis must use <->: {axis}")
    left, right = axis.split("<->", 1)
    return _short(left), _short(right)


def _counter_text(counter: Counter[str], limit: int = 6) -> str:
    if not counter:
        return "-"
    return " | ".join(f"{key}:{value}" for key, value in counter.most_common(limit))


def _node_profile(network_rows: list[dict[str, str]], node: str) -> dict[str, str]:
    for row in network_rows:
        row_node = _short(row.get("node", "") or row.get("token", "") or row.get("short_token", ""))
        if row_node == node:
            return {
                "network_state": row.get("network_state", "") or row.get("nonbridge_class", "-"),
                "dominant_role": row.get("dominant_role", "-"),
                "dominant_movement_quality": row.get("dominant_movement_quality", "") or row.get("condensation_zone", "-"),
                "dominant_shift_quality": row.get("dominant_shift_quality", "") or row.get("reading", "-"),
                "observations": row.get("observations", "0"),
                "worlds": row.get("worlds", "0"),
                "neighbor_count": row.get("neighbor_count", "0"),
                "avg_rekopplung": row.get("avg_rekopplung", "0"),
                "avg_strain": row.get("avg_strain", "0"),
            }
    return {
        "network_state": "-",
        "dominant_role": "-",
        "dominant_movement_quality": "-",
        "dominant_shift_quality": "-",
        "observations": "0",
        "worlds": "0",
        "neighbor_count": "0",
        "avg_rekopplung": "0",
        "avg_strain": "0",
    }


def _load_movement_rows(paths: list[Path]) -> list[tuple[str, dict[str, str]]]:
    rows: list[tuple[str, dict[str, str]]] = []
    for path in paths:
        for row in _read_rows(path):
            rows.append((path.name, row))
    return rows


def _summarize_axis(
    axis: str,
    temporal_rows: list[dict[str, str]],
    movement_rows: list[tuple[str, dict[str, str]]],
    network_rows: list[dict[str, str]],
) -> dict[str, object]:
    a, b = _axis_parts(axis)
    axis_temporal = [row for row in temporal_rows if row.get("axis") == axis]
    localized = [row for row in axis_temporal if row.get("reading") == "zeitlich_lokalisierte_achse"]
    temporal_worlds = Counter(row.get("world", "-") for row in axis_temporal)
    localized_worlds = Counter(row.get("world", "-") for row in localized)
    pair_events = sum(int(float(row.get("pair_events") or 0)) for row in axis_temporal)

    direct_roles: Counter[str] = Counter()
    direct_effects: Counter[str] = Counter()
    direct_sources: Counter[str] = Counter()
    adjacent_roles: Counter[str] = Counter()
    adjacent_effects: Counter[str] = Counter()
    adjacent_sources: Counter[str] = Counter()
    direct_hits = 0
    adjacent_hits = 0

    for source, row in movement_rows:
        parts = _pair_parts(row.get("pair", ""))
        if not parts:
            continue
        left, right = parts
        role = row.get("dominant_role_shift") or row.get("role_shift_profile") or row.get("movement_effect") or "-"
        effect = row.get("movement_effect") or "-"
        if {left, right} == {a, b}:
            direct_hits += 1
            direct_roles[role] += int(float(row.get("total_count") or 1))
            direct_effects[effect] += int(float(row.get("total_count") or 1))
            direct_sources[source] += 1
        elif left in {a, b} or right in {a, b}:
            adjacent_hits += 1
            adjacent_roles[role] += int(float(row.get("total_count") or 1))
            adjacent_effects[effect] += int(float(row.get("total_count") or 1))
            adjacent_sources[source] += 1

    profile_a = _node_profile(network_rows, a)
    profile_b = _node_profile(network_rows, b)

    if direct_hits and localized:
        reading = "achse_hat_rollenwechsel_und_zeitlage"
    elif adjacent_hits and localized:
        reading = "zeitachse_mit_angrenzender_rollenbewegung"
    elif localized:
        reading = "zeitachse_ohne_topologische_paarspur"
    elif adjacent_hits:
        reading = "breite_naehe_mit_angrenzender_rollenbewegung"
    else:
        reading = "breite_naehe_ohne_rollenwechselbeleg"

    return {
        "axis": axis,
        "temporal_worlds": _counter_text(temporal_worlds),
        "localized_worlds": _counter_text(localized_worlds),
        "temporal_rows": len(axis_temporal),
        "localized_rows": len(localized),
        "pair_events": pair_events,
        "direct_topology_hits": direct_hits,
        "adjacent_topology_hits": adjacent_hits,
        "direct_role_shifts": _counter_text(direct_roles),
        "direct_effects": _counter_text(direct_effects),
        "direct_sources": _counter_text(direct_sources),
        "adjacent_role_shifts": _counter_text(adjacent_roles),
        "adjacent_effects": _counter_text(adjacent_effects),
        "adjacent_sources": _counter_text(adjacent_sources),
        "node_a": a,
        "node_a_network_state": profile_a["network_state"],
        "node_a_role": profile_a["dominant_role"],
        "node_a_shift": profile_a["dominant_shift_quality"],
        "node_a_observations": profile_a["observations"],
        "node_b": b,
        "node_b_network_state": profile_b["network_state"],
        "node_b_role": profile_b["dominant_role"],
        "node_b_shift": profile_b["dominant_shift_quality"],
        "node_b_observations": profile_b["observations"],
        "reading": reading,
    }


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, object]]) -> None:
    lines = [
        "# MCM-Zentrumsachse und Topologie-Rollenwechsel",
        "",
        "## Zweck",
        "",
        "Diese Datei legt zeitlich lokalisierte Zentrumsachsen gegen Topologie-Rollenbewegungen.",
        "Unterschieden wird direkte Achsenpaar-Spur und angrenzende Rollenbewegung der beteiligten Knoten.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Ruecklesung",
        "- keine Handlung",
        "- kein Gate",
        "- keine Strategie",
        "",
        "## Achsenvergleich",
        "",
        "| Achse | Zeitlagen | Paar-Events | direkte Topologie | angrenzende Topologie | Knotenrollen | Lesung |",
        "|---|---:|---:|---:|---:|---|---|",
    ]
    for row in rows:
        node_roles = (
            f"{row['node_a']}={row['node_a_network_state']} / "
            f"{row['node_b']}={row['node_b_network_state']}"
        )
        lines.append(
            f"| `{row['axis']}` | {row['localized_rows']} | {row['pair_events']} | "
            f"{row['direct_topology_hits']} | {row['adjacent_topology_hits']} | `{node_roles}` | `{row['reading']}` |"
        )

    lines.extend(
        [
            "",
            "## Detailprofile",
            "",
        ]
    )
    for row in rows:
        lines.extend(
            [
                f"### `{row['axis']}`",
                "",
                f"- Zeitlich lokalisierte Welten: `{row['localized_worlds']}`",
                f"- Direkte Rollenwechsel: `{row['direct_role_shifts']}`",
                f"- Direkte Effekte: `{row['direct_effects']}`",
                f"- Angrenzende Rollenwechsel: `{row['adjacent_role_shifts']}`",
                f"- Angrenzende Effekte: `{row['adjacent_effects']}`",
                f"- Knoten A: `{row['node_a']}` / `{row['node_a_network_state']}` / `{row['node_a_role']}` / Beobachtungen {row['node_a_observations']}",
                f"- Knoten B: `{row['node_b']}` / `{row['node_b_network_state']}` / `{row['node_b_role']}` / Beobachtungen {row['node_b_observations']}",
                "",
            ]
        )

    lines.extend(
        [
            "## Befund",
            "",
            "Wenn eine Achse zeitlich lokalisiert ist, aber kaum direkte Topologie-Paarspur besitzt,",
            "dann ist sie eher als Feldlage mit angrenzender Rollenbewegung zu lesen, nicht als starre Kante.",
            "",
            "Arbeitsableitung:",
            "",
            "```text",
            "Zentrumsachsen koennen zeitlich auftreten, waehrend die Topologie ihren Ausdruck",
            "ueber Rollenbewegungen der beteiligten Knoten oder ihrer Nachbarschaft zeigt.",
            "```",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die staerkste Achse lokal segmentiert werden: Welche konkreten Kontaktsegmente erzeugen die Rollennaehe?",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--axis", action="append", required=True)
    parser.add_argument("--temporal", required=True, type=Path)
    parser.add_argument("--network", required=True, type=Path)
    parser.add_argument("--movement-file", action="append", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    temporal_rows = _read_rows(args.temporal)
    network_rows = _read_rows(args.network)
    movement_rows = _load_movement_rows(args.movement_file)
    rows = [_summarize_axis(axis, temporal_rows, movement_rows, network_rows) for axis in args.axis]
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"axes={len(rows)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
