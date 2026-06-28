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


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _short(value: str) -> str:
    return str(value or "").replace("dio_mcm_episode_", "").strip()


def _axis_key_from_pair(pair: str) -> str:
    pair = str(pair or "")
    if "->" not in pair:
        return "-"
    left, right = pair.split("->", 1)
    return "<->".join(sorted([_short(left), _short(right)]))


def _counter_text(counter: Counter[str], limit: int = 8) -> str:
    if not counter:
        return "-"
    return " | ".join(f"{key}:{value}" for key, value in counter.most_common(limit))


def _float(row: dict[str, str], key: str) -> float:
    try:
        return float(row.get(key, "0") or 0.0)
    except ValueError:
        return 0.0


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _load_topology(axis_rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    topology: dict[str, dict[str, str]] = {}
    for row in axis_rows:
        axis = row.get("axis", "")
        if not axis:
            continue
        topology[axis] = row
    return topology


def _annotate_family_rows(
    rows: list[dict[str, str]],
    side: str,
    topology_by_axis: dict[str, dict[str, str]],
) -> list[dict[str, object]]:
    annotated: list[dict[str, object]] = []
    for row in rows:
        axis = _axis_key_from_pair(row.get("pair", ""))
        topo = topology_by_axis.get(axis, {})
        annotated.append(
            {
                "side": side,
                "source": row.get("source", "-"),
                "world": row.get("world", "-"),
                "pair": row.get("pair", "-"),
                "axis": axis,
                "mode": row.get("mode", "-"),
                "phase_hint": row.get("phase_hint", "-"),
                "chart_zone": row.get("chart_zone", "-"),
                "dominant_movement": row.get("dominant_movement", "-"),
                "return_pct": _float(row, "main_return_pct"),
                "range_pct": _float(row, "main_range_pct"),
                "pressure_abs": _float(row, "pressure_delta_abs_avg"),
                "rekopplung_abs": _float(row, "rekopplung_delta_abs_avg"),
                "topology_reading": topo.get("reading", "keine_topologie_achse"),
                "node_a_state": topo.get("node_a_network_state", "-"),
                "node_a_role": topo.get("node_a_role", "-"),
                "node_a_shift": topo.get("node_a_shift", "-"),
                "node_b_state": topo.get("node_b_network_state", "-"),
                "node_b_role": topo.get("node_b_role", "-"),
                "node_b_shift": topo.get("node_b_shift", "-"),
                "adjacent_role_shifts": topo.get("adjacent_role_shifts", "-"),
                "adjacent_effects": topo.get("adjacent_effects", "-"),
                "direct_topology_hits": topo.get("direct_topology_hits", "0"),
                "adjacent_topology_hits": topo.get("adjacent_topology_hits", "0"),
                "passive_only": 1,
                "read_by_mini_dio": 0,
                "influences_action": 0,
                "is_gate": 0,
                "is_motoric": 0,
                "is_entry_signal": 0,
                "is_direction_signal": 0,
            }
        )
    return annotated


def _summarize(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    groups: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        groups[(str(row["side"]), str(row["mode"]))].append(row)

    summary: list[dict[str, object]] = []
    for (side, mode), items in sorted(groups.items()):
        topology = Counter(str(item["topology_reading"]) for item in items)
        axes = Counter(str(item["axis"]) for item in items)
        phases = Counter(str(item["phase_hint"]) for item in items)
        movements = Counter(str(item["dominant_movement"]) for item in items)
        node_states = Counter(
            f"{item['node_a_state']}<->{item['node_b_state']}" for item in items
        )
        summary.append(
            {
                "side": side,
                "mode": mode,
                "count": len(items),
                "avg_return_pct": round(_mean([float(item["return_pct"]) for item in items]), 6),
                "avg_range_pct": round(_mean([float(item["range_pct"]) for item in items]), 6),
                "avg_pressure_abs": round(_mean([float(item["pressure_abs"]) for item in items]), 6),
                "avg_rekopplung_abs": round(_mean([float(item["rekopplung_abs"]) for item in items]), 6),
                "topology_readings": _counter_text(topology),
                "axes": _counter_text(axes),
                "phase_hints": _counter_text(phases),
                "movement_types": _counter_text(movements),
                "node_state_pairs": _counter_text(node_states),
            }
        )
    return summary


def _write_md(
    path: Path,
    annotated: list[dict[str, object]],
    summary: list[dict[str, object]],
) -> None:
    lines = [
        "# 1021 - Bull/Selloff gegen Topologie-Rollen",
        "",
        "Passive Gegenlesung der Bull-/Abverkauf-Familien gegen vorhandene MCM-Topologie-Rollen.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Diagnose",
        "- keine Handlung",
        "- kein Gate",
        "- keine Strategie",
        "- keine nachtraegliche Topologie-Vorgabe",
        "",
        "## Rollenverdichtung",
        "",
        "| Seite | Modus | Count | Return % | Range % | Druck | Rekopplung | Topologie-Lesung | Achsen | Knotenstatus |",
        "|---|---|---:|---:|---:|---:|---:|---|---|---|",
    ]
    for row in summary:
        lines.append(
            f"| {row['side']} | `{row['mode']}` | {row['count']} | "
            f"{row['avg_return_pct']} | {row['avg_range_pct']} | "
            f"{row['avg_pressure_abs']} | {row['avg_rekopplung_abs']} | "
            f"`{row['topology_readings']}` | `{row['axes']}` | `{row['node_state_pairs']}` |"
        )

    lines.extend(
        [
            "",
            "## Einzelbelege",
            "",
            "| Seite | Modus | Welt | Paar | Phase | Bewegung | Return % | Topologie | Knotenrollen |",
            "|---|---|---|---|---|---|---:|---|---|",
        ]
    )
    for row in annotated:
        roles = f"{row['node_a_role']} / {row['node_b_role']}"
        lines.append(
            f"| {row['side']} | `{row['mode']}` | `{row['world']}` | `{row['pair']}` | "
            f"`{row['phase_hint']}` | `{row['dominant_movement']}` | {row['return_pct']} | "
            f"`{row['topology_reading']}` | `{roles}` |"
        )

    bull = [row for row in summary if row["side"] == "bull"]
    selloff = [row for row in summary if row["side"] == "selloff"]
    bull_axes = Counter()
    selloff_axes = Counter()
    for row in annotated:
        if row["side"] == "bull":
            bull_axes[str(row["axis"])] += 1
        elif row["side"] == "selloff":
            selloff_axes[str(row["axis"])] += 1

    shared_axes = sorted(set(bull_axes) & set(selloff_axes))
    bull_only = sorted(set(bull_axes) - set(selloff_axes))
    selloff_only = sorted(set(selloff_axes) - set(bull_axes))

    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"- Bull-Modi: {len(bull)}",
            f"- Selloff-Modi: {len(selloff)}",
            f"- Gemeinsame Achsen: `{', '.join(shared_axes) if shared_axes else '-'}`",
            f"- Nur Bull-Achsen: `{', '.join(bull_only) if bull_only else '-'}`",
            f"- Nur Selloff-Achsen: `{', '.join(selloff_only) if selloff_only else '-'}`",
            "",
            "Die gleiche oder aehnliche Achse kann unterschiedliche Bewegungsqualitaeten tragen.",
            "Damit wirkt die Topologie nicht als starres Richtungsschema, sondern als Feldort,",
            "an dem Bewegung je nach Weltphase anders gelesen wird.",
            "",
            "## Schluss",
            "",
            "Bull-/Selloff-Asymmetrie liegt nicht nur in der Rohbewegung, sondern in der Kombination aus Achse,",
            "Rollennaehe, Rekopplung, Druck und vorheriger Last. Das passt zur bisherigen Lesung:",
            "MCM-Feldrollen sind Bedeutungsorte, keine fixen Handelsrichtungen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte eine einzelne gemeinsame Achse isoliert werden: Wann liest sie Bull-Fortsetzung, wann Selloff-Rekopplung, und welche Weltmerkmale kippen die Rollenqualitaet?",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bull-details", required=True, type=Path)
    parser.add_argument("--selloff-details", required=True, type=Path)
    parser.add_argument("--topology", required=True, type=Path)
    parser.add_argument("--out-details", required=True, type=Path)
    parser.add_argument("--out-summary", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    args = parser.parse_args()

    topology = _load_topology(_read_rows(args.topology))
    annotated = []
    annotated.extend(_annotate_family_rows(_read_rows(args.bull_details), "bull", topology))
    annotated.extend(_annotate_family_rows(_read_rows(args.selloff_details), "selloff", topology))
    summary = _summarize(annotated)

    _write_csv(args.out_details, annotated)
    _write_csv(args.out_summary, summary)
    _write_md(args.out_md, annotated, summary)
    print(f"details={len(annotated)}")
    print(f"summary={len(summary)}")
    print(f"wrote {args.out_md}")


if __name__ == "__main__":
    main()
