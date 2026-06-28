from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


PASSIVE_FLAGS = {
    "passive_only": 1,
    "read_by_mini_dio": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
}


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


def _load_csv(path: Path) -> list[dict[str, str]]:
    path = Path(path)
    if not path.exists() or path.stat().st_size <= 0:
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _short_node(value: object) -> str:
    text = str(value or "").strip()
    if text.startswith("dio_mcm_episode_"):
        return text.replace("dio_mcm_episode_", "", 1)
    return text


def _top(counter: Counter[str], limit: int = 5) -> str:
    return " | ".join(f"{key}:{value}" for key, value in counter.most_common(limit))


def _fragmentation_cause(row: dict[str, object]) -> str:
    rekopplung_delta = _safe_float(row.get("edge_rekopplung_delta_avg"))
    strain_delta = _safe_float(row.get("edge_strain_delta_avg"))
    neighbor_count = _safe_int(row.get("neighbor_count"))
    top_phase = str(row.get("top_exit_phases", "") or "")
    top_nonbridge = str(row.get("top_nonbridge_classes", "") or "")

    if strain_delta > 0.0 and rekopplung_delta < 0.0:
        if "aussen" in str(row.get("top_edge_kinds", "") or ""):
            return "fragmentierung_durch_aussen_brueckenriss"
        return "fragmentierung_durch_strain_ueber_rekopplung"
    if "rand" in top_nonbridge:
        return "fragmentierung_durch_randspannung"
    if "offen" in top_nonbridge:
        return "fragmentierung_durch_offene_oberflaeche"
    if neighbor_count >= 5 and "belast" in top_phase:
        return "fragmentierung_durch_dichte_belastete_nachbarschaft"
    if neighbor_count >= 5:
        return "fragmentierung_trotz_dichter_nachbarschaft"
    return "fragmentierung_offen"


def _cause_reading_for_state(row: dict[str, object], target_state: str) -> str:
    if target_state == "netz_fragmentiert_belastet":
        return _fragmentation_cause(row)

    rekopplung_delta = _safe_float(row.get("edge_rekopplung_delta_avg"))
    strain_delta = _safe_float(row.get("edge_strain_delta_avg"))
    neighbor_count = _safe_int(row.get("neighbor_count"))
    top_phase = str(row.get("top_exit_phases", "") or "")
    top_nonbridge = str(row.get("top_nonbridge_classes", "") or "")

    if target_state == "netz_rekoppelnd_verbunden":
        if rekopplung_delta > 0.0 and strain_delta < 0.0:
            return "rekopplung_durch_entlastende_bruecke"
        if "rekoppelnder" in top_phase:
            return "rekopplung_durch_phasenwechsel"
        if "rekopplung" in top_nonbridge:
            return "rekopplung_durch_nichtbruecken_rueckbindung"
        if neighbor_count > 0:
            return "rekopplung_durch_nachbarschaft"
        return "rekopplung_offen"

    if rekopplung_delta > strain_delta:
        return "netzlage_rekoppelnd"
    if strain_delta > rekopplung_delta:
        return "netzlage_belastet"
    if neighbor_count > 0:
        return "netzlage_verbunden"
    return "netzlage_offen"


def _title_for_state(target_state: str) -> str:
    if target_state == "netz_fragmentiert_belastet":
        return "MCM-Rolennetzwerk: Fragmentierungs-Ruecklesung"
    if target_state == "netz_rekoppelnd_verbunden":
        return "MCM-Rolennetzwerk: Rekopplungs-Ruecklesung"
    return "MCM-Rolennetzwerk: Zustands-Ruecklesung"


def _purpose_for_state(target_state: str) -> str:
    if target_state == "netz_fragmentiert_belastet":
        return "Diese Datei legt die Klasse `netz_fragmentiert_belastet` passiv auf Brueckenkanten, Austrittsphasen und Nicht-Bruecken-Rollen zurueck."
    if target_state == "netz_rekoppelnd_verbunden":
        return "Diese Datei legt die Klasse `netz_rekoppelnd_verbunden` passiv auf Brueckenkanten, Austrittsphasen und Nicht-Bruecken-Rollen zurueck."
    return f"Diese Datei legt die Klasse `{target_state}` passiv auf Brueckenkanten, Austrittsphasen und Nicht-Bruecken-Rollen zurueck."


def _interpretation_lines(target_state: str) -> list[str]:
    if target_state == "netz_fragmentiert_belastet":
        return [
            "Belastete Fragmentierung ist in dieser Ruecklesung keine einfache Leere.",
            "Sie entsteht dort, wo Knoten sichtbar und oft sogar stark vernetzt bleiben, aber Rekopplung in den Kanten faellt und Strain steigt.",
            "",
            "Das spricht fuer eine belastete Netzwerksituation:",
            "",
            "```text",
            "Knoten bleibt da.",
            "Nachbarschaft bleibt da.",
            "Aber die Verbindung traegt nicht ruhig genug.",
            "Das Feld fragmentiert belastet statt zu verschwinden.",
            "```",
        ]
    if target_state == "netz_rekoppelnd_verbunden":
        return [
            "Rekoppelnde Verbindung ist in dieser Ruecklesung keine blosse Verbindung.",
            "Sie entsteht dort, wo Bruecken- und Aussenkanten Entlastung tragen: Rekopplung steigt, Strain faellt.",
            "",
            "Das spricht fuer eine entlastende Netzwerksituation:",
            "",
            "```text",
            "Knoten bleibt sichtbar.",
            "Nachbarschaft wirkt mit.",
            "Die Verbindung traegt ruhig genug.",
            "Das Feld rekoppelt verbunden statt belastet zu fragmentieren.",
            "```",
        ]
    return [
        f"`{target_state}` ist in dieser Ruecklesung keine isolierte Einzelzahl.",
        "Die Lage entsteht als Kombination aus Knoten, Nachbarschaft, Kantenphase, Rekopplung und Strain.",
    ]


def build_rows(
    *,
    network_rows: list[dict[str, str]],
    bridge_rows: list[dict[str, str]],
    nonbridge_rows: list[dict[str, str]],
    target_state: str,
) -> list[dict[str, object]]:
    fragmented = {
        str(row.get("node", "") or ""): row
        for row in network_rows
        if row.get("network_state") == target_state
    }
    edge_map: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in bridge_rows:
        source = _short_node(row.get("source", ""))
        target = _short_node(row.get("target", ""))
        if source in fragmented:
            edge_map[source].append(row)
        if target in fragmented:
            edge_map[target].append(row)

    nonbridge_map: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in nonbridge_rows:
        token = _short_node(row.get("short_token", "") or row.get("token", ""))
        if token in fragmented:
            nonbridge_map[token].append(row)

    output: list[dict[str, object]] = []
    for node, net in fragmented.items():
        edges = edge_map.get(node, [])
        nonbridges = nonbridge_map.get(node, [])
        edge_count = sum(_safe_int(row.get("count")) for row in edges)
        edge_worlds = sum(_safe_int(row.get("worlds")) for row in edges)
        rekopplung_delta = [_safe_float(row.get("exit_rekopplung_delta_avg")) for row in edges]
        strain_delta = [_safe_float(row.get("exit_strain_delta_avg")) for row in edges]
        row = {
            **PASSIVE_FLAGS,
            "node": node,
            "network_symbol": net.get("network_symbol", ""),
            "network_state": net.get("network_state", ""),
            "dominant_role": net.get("dominant_role", ""),
            "dominant_stability_quality": net.get("dominant_stability_quality", ""),
            "dominant_drift_quality": net.get("dominant_drift_quality", ""),
            "network_observations": _safe_int(net.get("observations")),
            "network_worlds": _safe_int(net.get("worlds")),
            "neighbor_count": _safe_int(net.get("neighbor_count")),
            "network_avg_rekopplung": _safe_float(net.get("avg_rekopplung")),
            "network_avg_strain": _safe_float(net.get("avg_strain")),
            "edge_rows": len(edges),
            "edge_count": edge_count,
            "edge_worlds": edge_worlds,
            "edge_rekopplung_delta_avg": round(sum(rekopplung_delta) / max(1, len(rekopplung_delta)), 6),
            "edge_strain_delta_avg": round(sum(strain_delta) / max(1, len(strain_delta)), 6),
            "top_edge_kinds": _top(Counter(str(item.get("edge_kind", "") or "-") for item in edges)),
            "top_exit_phases": _top(Counter(str(item.get("exit_phase", "") or "-") for item in edges)),
            "top_nonbridge_classes": _top(Counter(str(item.get("nonbridge_class", "") or "-") for item in nonbridges)),
            "top_condensation_zones": _top(Counter(str(item.get("condensation_zone", "") or "-") for item in nonbridges)),
        }
        row["cause_reading"] = _cause_reading_for_state(row, target_state)
        output.append(row)

    output.sort(key=lambda item: (_safe_int(item.get("edge_count")), _safe_int(item.get("network_observations"))), reverse=True)
    return output


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, object]], target_state: str) -> None:
    cause_counts = Counter(str(row.get("cause_reading", "") or "-") for row in rows)
    lines = [
        f"# {_title_for_state(target_state)}",
        "",
        "## Zweck",
        "",
        _purpose_for_state(target_state),
        "Sie prueft, welche Kanten-, Phasen- und Rollenbedingungen diese Netzwerklage tragen.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Ruecklesung",
        "- keine Handlung",
        "- kein Gate",
        "- keine Richtung",
        "- keine Strategie",
        "",
        "## Ursachenlesung",
        "",
    ]
    for key, count in cause_counts.most_common():
        lines.append(f"- `{key}`: {count}")

    lines.extend(
        [
            "",
            "## Staerkste Knoten",
            "",
            "| Knoten | Lesung | Nachbarn | Kanten | Rekopplung-Delta | Strain-Delta | Kantenarten | Austrittsphasen | Nicht-Bruecken |",
            "|---|---|---:|---:|---:|---:|---|---|---|",
        ]
    )
    for row in rows[:32]:
        lines.append(
            f"| `{row['node']}` | `{row['cause_reading']}` | {row['neighbor_count']} | {row['edge_count']} | {row['edge_rekopplung_delta_avg']} | {row['edge_strain_delta_avg']} | `{row['top_edge_kinds']}` | `{row['top_exit_phases']}` | `{row['top_nonbridge_classes']}` |"
        )

    lines.extend(["", "## Interpretation", ""])
    lines.extend(_interpretation_lines(target_state))
    lines.extend(
        [
            "",
            "## Grenze",
            "",
            "Diese Lesung beschreibt nur Feldbedingungen.",
            "Sie erzeugt keine Handlung und keine Regel.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollten die Ruecklesungen von `netz_fragmentiert_belastet` und `netz_rekoppelnd_verbunden` direkt verglichen werden.",
            "Dann wird sichtbar, welche Feldbedingungen Belastung von Rekopplung unterscheiden.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--network", required=True, type=Path)
    parser.add_argument("--target-state", default="netz_fragmentiert_belastet")
    parser.add_argument("--bridge-network", action="append", default=[])
    parser.add_argument("--nonbridge", action="append", default=[])
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    bridge_rows: list[dict[str, str]] = []
    for path in args.bridge_network:
        bridge_rows.extend(_load_csv(Path(path)))
    nonbridge_rows: list[dict[str, str]] = []
    for path in args.nonbridge:
        nonbridge_rows.extend(_load_csv(Path(path)))

    rows = build_rows(
        network_rows=_load_csv(args.network),
        bridge_rows=bridge_rows,
        nonbridge_rows=nonbridge_rows,
        target_state=args.target_state,
    )
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows, args.target_state)
    print(f"target_state={args.target_state}")
    print(f"nodes={len(rows)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
