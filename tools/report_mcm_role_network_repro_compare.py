from __future__ import annotations

import argparse
import csv
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
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _index(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {str(row.get("network_state", "") or "-"): row for row in rows}


def _reading(state: str, early_nodes: int, late_nodes: int) -> str:
    delta = late_nodes - early_nodes
    if state == "netz_zentrum_getragen" and late_nodes > 0:
        return "Spaete Gruppe bildet zusaetzliche getragene Zentrumsqualitaet."
    if state == "netz_fragmentiert_belastet" and delta < 0:
        return "Belastete Fragmentierung nimmt in der spaeten Gruppe ab."
    if state == "netz_driftend_getragen" and delta > 0:
        return "Getragene Drift nimmt zu und wirkt als Folgereifung statt Zerfall."
    if state == "netz_rekoppelnd_verbunden" and abs(delta) <= 3:
        return "Rekoppelnde Verbindung bleibt ueber beide Gruppen stabil sichtbar."
    if state == "netz_offen_verbunden" and delta < 0:
        return "Offene Verbindung bleibt sichtbar, wird aber weniger dominant."
    if state == "netz_rekoppelnd_einzeln" and delta > 0:
        return "Einzelrekopplung nimmt zu; Teile loesen sich aus dichter Verbindung."
    if delta > 0:
        return "Zustand nimmt in der spaeten Gruppe zu."
    if delta < 0:
        return "Zustand nimmt in der spaeten Gruppe ab."
    return "Zustand bleibt in der Knotenzahl stabil."


def build_rows(early_rows: list[dict[str, str]], late_rows: list[dict[str, str]]) -> list[dict[str, object]]:
    early = _index(early_rows)
    late = _index(late_rows)
    states = sorted(set(early) | set(late))
    output: list[dict[str, object]] = []
    for state in states:
        e = early.get(state, {})
        l = late.get(state, {})
        early_nodes = _safe_int(e.get("nodes"))
        late_nodes = _safe_int(l.get("nodes"))
        output.append(
            {
                **PASSIVE_FLAGS,
                "network_state": state,
                "early_nodes": early_nodes,
                "late_nodes": late_nodes,
                "node_delta_late_minus_early": late_nodes - early_nodes,
                "early_avg_neighbors": _safe_float(e.get("avg_neighbor_count")),
                "late_avg_neighbors": _safe_float(l.get("avg_neighbor_count")),
                "early_avg_rekopplung": _safe_float(e.get("avg_rekopplung")),
                "late_avg_rekopplung": _safe_float(l.get("avg_rekopplung")),
                "early_avg_strain": _safe_float(e.get("avg_strain")),
                "late_avg_strain": _safe_float(l.get("avg_strain")),
                "reading": _reading(state, early_nodes, late_nodes),
            }
        )
    return output


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, object]]) -> None:
    lines = [
        "# MCM-Rolennetzwerk: Reproduktionsvergleich",
        "",
        "## Zweck",
        "",
        "Diese Datei vergleicht die passive Rolennetzwerk-Lesung zwischen frueher und spaeter Weltgruppe.",
        "Sie prueft, ob dieselbe Feldmechanik wiederkehrt, driftet oder neue Zentrumsqualitaet bildet.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Diagnose",
        "- keine Handlung",
        "- kein Gate",
        "- keine Strategie",
        "",
        "## Vergleich",
        "",
        "| Zustand | Frueh | Spaet | Delta | Frueh Rekopplung | Spaet Rekopplung | Frueh Strain | Spaet Strain | Lesung |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in sorted(rows, key=lambda item: abs(int(item["node_delta_late_minus_early"])), reverse=True):
        lines.append(
            f"| `{row['network_state']}` | {row['early_nodes']} | {row['late_nodes']} | {row['node_delta_late_minus_early']} | "
            f"{row['early_avg_rekopplung']:.6f} | {row['late_avg_rekopplung']:.6f} | "
            f"{row['early_avg_strain']:.6f} | {row['late_avg_strain']:.6f} | {row['reading']} |"
        )

    lines.extend(
        [
            "",
            "## Kernbefund",
            "",
            "Die spaete Gruppe erzeugt keine voellig andere Topologie.",
            "Sie verschiebt die Gewichtung innerhalb derselben Feldfamilie:",
            "",
            "- weniger `netz_fragmentiert_belastet`",
            "- mehr `netz_driftend_getragen`",
            "- weiterhin stabile `netz_rekoppelnd_verbunden`",
            "- erstmals `netz_zentrum_getragen` als kleine zusaetzliche Zentrumsqualitaet",
            "",
            "## Arbeitsableitung",
            "",
            "```text",
            "Das Rolennetzwerk reproduziert sich nicht als starre Kopie.",
            "Es bleibt in der Grundtopologie aehnlich, verschiebt aber Last, Drift und Zentrumsnaehe je nach Weltgruppe.",
            "```",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die spaete Zentrumsqualitaet gegen ihre Rohwelt und Sensorik zurueckgelesen werden.",
            "Wenn sie nicht zufaellig ist, zeigt sie, wann aus Rekopplung eine getragene Mitte wird.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--early", required=True, type=Path)
    parser.add_argument("--late", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    rows = build_rows(_load_csv(args.early), _load_csv(args.late))
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"states={len(rows)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
