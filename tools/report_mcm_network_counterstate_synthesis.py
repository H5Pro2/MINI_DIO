from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
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


def _profile(label: str, rows: list[dict[str, str]]) -> dict[str, object]:
    count = len(rows)
    rekopplung = [_safe_float(row.get("edge_rekopplung_delta_avg")) for row in rows]
    strain = [_safe_float(row.get("edge_strain_delta_avg")) for row in rows]
    neighbors = [_safe_int(row.get("neighbor_count")) for row in rows]
    edge_count = [_safe_int(row.get("edge_count")) for row in rows]
    causes = Counter(str(row.get("cause_reading", "") or "-") for row in rows)
    return {
        **PASSIVE_FLAGS,
        "state_label": label,
        "nodes": count,
        "avg_neighbor_count": round(sum(neighbors) / max(1, count), 6),
        "edge_count_total": sum(edge_count),
        "avg_edge_count": round(sum(edge_count) / max(1, count), 6),
        "avg_rekopplung_delta": round(sum(rekopplung) / max(1, count), 6),
        "avg_strain_delta": round(sum(strain) / max(1, count), 6),
        "dominant_cause": causes.most_common(1)[0][0] if causes else "-",
        "cause_profile": " | ".join(f"{key}:{value}" for key, value in causes.most_common()),
    }


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, object]]) -> None:
    by_label = {str(row["state_label"]): row for row in rows}
    frag = by_label.get("netz_fragmentiert_belastet", {})
    rek = by_label.get("netz_rekoppelnd_verbunden", {})
    lines = [
        "# MCM-Rolennetzwerk: Gegenzustand-Synthese",
        "",
        "## Zweck",
        "",
        "Diese Datei fuehrt die Ruecklesungen von belasteter Fragmentierung und ruhiger Rekopplung zusammen.",
        "Sie haelt den beobachteten Gegenzustand der sichtbaren Netzwerkverbindung fest.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Synthese",
        "- keine Handlung",
        "- kein Gate",
        "- keine Richtung",
        "- keine Strategie",
        "",
        "## Vergleich",
        "",
        "| Zustand | Knoten | Kanten gesamt | Durchschnitt Nachbarn | Durchschnitt Rekopplung-Delta | Durchschnitt Strain-Delta | Dominante Lesung |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['state_label']}` | {row['nodes']} | {row['edge_count_total']} | {row['avg_neighbor_count']} | {row['avg_rekopplung_delta']} | {row['avg_strain_delta']} | `{row['dominant_cause']}` |"
        )

    lines.extend(
        [
            "",
            "## Mechanischer Satz",
            "",
            "Die Ruecklesung zeigt einen klaren Gegenzustand:",
            "",
            "```text",
            "Belastete Fragmentierung:",
            "Knoten bleibt sichtbar.",
            "Nachbarschaft bleibt vorhanden.",
            "Rekopplung faellt.",
            "Strain steigt.",
            "",
            "Ruhige Rekopplung:",
            "Knoten bleibt sichtbar.",
            "Nachbarschaft bleibt vorhanden.",
            "Rekopplung steigt.",
            "Strain faellt.",
            "```",
            "",
            "Arbeitsableitung:",
            "",
            "```text",
            "Belastung und Rekopplung sind Gegenzustaende derselben sichtbaren Netzwerkverbindung.",
            "```",
            "",
            "## Interpretation",
            "",
            "Das MCM-Feld scheint eine Verbindung nicht nur als vorhanden oder nicht vorhanden zu lesen.",
            "Es liest auch die Qualitaet der Verbindung: tragend, entlastend, belastet, offen oder fragmentiert.",
            "",
            "Damit wird die MCM-Feldmechanik funktional konkreter:",
            "",
            "```text",
            "Netzwerk bleibt sichtbar.",
            "Feldqualitaet entscheidet, ob es rekoppelt oder belastet fragmentiert.",
            "```",
            "",
            "## Zahlenkern",
            "",
            f"- Fragmentierung: `{frag.get('dominant_cause', '-')}` bei `{frag.get('nodes', 0)}` Knoten, Rekopplung-Delta `{frag.get('avg_rekopplung_delta', 0)}`, Strain-Delta `{frag.get('avg_strain_delta', 0)}`.",
            f"- Rekopplung: `{rek.get('dominant_cause', '-')}` bei `{rek.get('nodes', 0)}` Knoten, Rekopplung-Delta `{rek.get('avg_rekopplung_delta', 0)}`, Strain-Delta `{rek.get('avg_strain_delta', 0)}`.",
            "",
            "## Grenze",
            "",
            "Diese Synthese beschreibt eine passive Feldmechanik.",
            "Sie ist keine Handlungsnaehe und kein Beweisabschluss.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte geprueft werden, ob derselbe Gegenzustand auch in neuen Weltgruppen reproduzierbar bleibt.",
            "Erst dann kann daraus eine robuste MCM-Feldmechanik-These formuliert werden.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fragmented", required=True, type=Path)
    parser.add_argument("--recoupled", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    rows = [
        _profile("netz_fragmentiert_belastet", _load_csv(args.fragmented)),
        _profile("netz_rekoppelnd_verbunden", _load_csv(args.recoupled)),
    ]
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print("states=2")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
