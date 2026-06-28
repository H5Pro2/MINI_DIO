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
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _top(counter: Counter[str], limit: int = 4) -> str:
    return " | ".join(f"{key}:{value}" for key, value in counter.most_common(limit))


def _condition_reading(row: dict[str, object]) -> str:
    state = str(row.get("network_state", "") or "")
    avg_rekopplung = _safe_float(row.get("avg_rekopplung"))
    avg_strain = _safe_float(row.get("avg_strain"))
    avg_neighbors = _safe_float(row.get("avg_neighbor_count"))
    dominant_movement = str(row.get("top_movement_quality", "") or "")
    dominant_stability = str(row.get("top_stability_quality", "") or "")
    dominant_drift = str(row.get("top_drift_quality", "") or "")

    if state == "netz_zentrum_mit_anschluss":
        return "Zentrumsnaehe entsteht, wenn Kern-/Zentrumsqualitaet mit Anschlussnachbarschaft zusammen sichtbar wird."
    if state == "netz_rekoppelnd_verbunden":
        return "Rekopplung entsteht, wenn Feldanschluss und Entlastung gemeinsam staerker wirken als Strain."
    if state == "netz_driftend_getragen":
        return "Drift bleibt getragen, wenn Rollenbewegung sichtbar ist, aber Rekopplung Strain nicht klar unterliegt."
    if state == "netz_fragmentiert_belastet":
        return "Fragmentierung wird belastet, wenn Strain und Aussen-/Brueckenriss trotz sichtbarer Kernnaehe hoch bleiben."
    if state == "netz_offen_verbunden":
        return "Offene Verbindung zeigt Anschluss ohne klare Zentrums- oder Rekopplungsbindung."
    if state == "netz_rekoppelnd_einzeln":
        return "Einzelrekopplung zeigt Entlastung ohne tragendes Nachbarschaftsnetz."
    if avg_rekopplung >= avg_strain and avg_neighbors > 0:
        return "Bedingung wirkt allgemein rekoppelnd und vernetzt."
    if "drift" in dominant_drift or "drifting" in dominant_movement:
        return "Bedingung wirkt allgemein driftend."
    if "core" in dominant_stability:
        return "Bedingung wirkt allgemein zentrumsnah."
    return "Bedingung bleibt offen."


def build_condition_rows(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[str(row.get("network_state", "") or "-")].append(row)

    output: list[dict[str, object]] = []
    for state, items in sorted(groups.items(), key=lambda item: len(item[1]), reverse=True):
        count = len(items)
        observations = sum(_safe_int(item.get("observations")) for item in items)
        worlds = sum(_safe_int(item.get("worlds")) for item in items)
        neighbors = [_safe_int(item.get("neighbor_count")) for item in items]
        rekopplung = [_safe_float(item.get("avg_rekopplung")) for item in items]
        strain = [_safe_float(item.get("avg_strain")) for item in items]
        row = {
            **PASSIVE_FLAGS,
            "network_state": state,
            "nodes": count,
            "observations_total": observations,
            "worlds_total": worlds,
            "avg_neighbor_count": round(sum(neighbors) / max(1, count), 6),
            "avg_rekopplung": round(sum(rekopplung) / max(1, count), 6),
            "avg_strain": round(sum(strain) / max(1, count), 6),
            "top_roles": _top(Counter(str(item.get("dominant_role", "") or "-") for item in items)),
            "top_movement_quality": _top(Counter(str(item.get("dominant_movement_quality", "") or "-") for item in items)),
            "top_shift_quality": _top(Counter(str(item.get("dominant_shift_quality", "") or "-") for item in items)),
            "top_stability_quality": _top(Counter(str(item.get("dominant_stability_quality", "") or "-") for item in items)),
            "top_drift_quality": _top(Counter(str(item.get("dominant_drift_quality", "") or "-") for item in items)),
        }
        row["condition_reading"] = _condition_reading(row)
        output.append(row)
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


def _write_md(path: Path, rows: list[dict[str, object]]) -> None:
    lines = [
        "# MCM-Rolennetzwerk: Bedingungsdiagnose",
        "",
        "## Zweck",
        "",
        "Diese Datei prueft passiv, welche gemeinsamen Bedingungen hinter den Netzwerkzustaenden der `dio_net_*` Feldkarte liegen.",
        "Sie beschreibt keine Handlung, kein Gate und keine Strategie.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Diagnose",
        "- keine Entry-Wirkung",
        "- keine Richtungsvorgabe",
        "- keine Motorik",
        "",
        "## Bedingungsmatrix",
        "",
        "| Zustand | Knoten | Durchschnitt Nachbarn | Durchschnitt Rekopplung | Durchschnitt Strain | Top Bewegung | Top Stabilitaet | Top Drift | Lesung |",
        "|---|---:|---:|---:|---:|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['network_state']}` | {row['nodes']} | {row['avg_neighbor_count']} | {row['avg_rekopplung']} | {row['avg_strain']} | `{row['top_movement_quality']}` | `{row['top_stability_quality']}` | `{row['top_drift_quality']}` | {row['condition_reading']} |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Die Netzwerkzustaende wirken nicht zufaellig gleichartig.",
            "Sie unterscheiden sich durch Kombinationen aus Nachbarschaft, Rekopplung, Strain, Rollenbewegung, Stabilitaet und Drift.",
            "",
            "Damit wird die naechste MCM-Arbeitsfrage konkreter:",
            "",
            "```text",
            "Welche Feldbedingungen lassen eine Bedeutung stabil bleiben, wandern, rekoppeln oder fragmentieren?",
            "```",
            "",
            "## Grenze",
            "",
            "Diese Diagnose bleibt beschreibend.",
            "Sie darf keine harte Regel und keine Handlungsnaehe erzeugen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte eine einzelne Klasse, vorzugsweise `netz_fragmentiert_belastet`, gegen ihre Weltsegmente zurueckgelegt werden.",
            "Dann wird sichtbar, ob Fragmentierung durch Weltbruch, Nachbarschaftsriss oder innere Strain-Lage getragen wird.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--network", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    rows = build_condition_rows(_load_csv(args.network))
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"states={len(rows)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
