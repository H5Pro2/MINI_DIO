from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

RUNS = [
    ("BTC", "debug/1837_btc_17k/dio_mini_lauf_1"),
    ("DOGE", "debug/1837_doge_17k/dio_mini_lauf_1"),
    ("PAXG", "debug/1837_paxg_17k/dio_mini_lauf_1"),
    ("XRP", "debug/1837_xrp_17k/dio_mini_lauf_1"),
]

OUT_CSV = ROOT / "docs/befunde/1001-2000/1751-2000/1839_MCM_REIFUNGSBAHN_17K_PHASENSEGMENTE.csv"
OUT_MD = ROOT / "docs/befunde/1001-2000/1751-2000/1839_MCM_REIFUNGSBAHN_17K_PHASENSEGMENTE.md"


def _float(value: object) -> float:
    try:
        out = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if out != out else out


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _family(row: dict[str, str]) -> str:
    return row.get("symbol_family") or row.get("dominant_family") or "-"


def _role(row: dict[str, str]) -> str:
    return (
        row.get("mcm_field_episode_role")
        or row.get("passive_mcm_effect_class")
        or row.get("mcm_field_effect_state")
        or "-"
    )


def _read_rows(run_dir: str) -> list[dict[str, str]]:
    path = ROOT / run_dir / "episodes.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _phase(index: int, total: int) -> str:
    if total <= 0:
        return "unbekannt"
    ratio = index / total
    if ratio < 1 / 3:
        return "frueh"
    if ratio < 2 / 3:
        return "mitte"
    return "spaet"


def _jaccard(left: list[str], right: list[str]) -> float:
    left_set = set(left)
    right_set = set(right)
    if not left_set and not right_set:
        return 0.0
    return len(left_set & right_set) / len(left_set | right_set)


def _summaries() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    segment_rows: list[dict[str, object]] = []
    transition_rows: list[dict[str, object]] = []
    for asset, run_dir in RUNS:
        rows = _read_rows(run_dir)
        buckets: dict[str, list[dict[str, str]]] = defaultdict(list)
        for index, row in enumerate(rows):
            buckets[_phase(index, len(rows))].append(row)

        top_by_phase: dict[str, list[str]] = {}
        for phase in ["frueh", "mitte", "spaet"]:
            phase_rows = buckets[phase]
            families = Counter(_family(row) for row in phase_rows)
            roles = Counter(_role(row) for row in phase_rows)
            top_families = [family for family, _ in families.most_common(20)]
            top_by_phase[phase] = top_families
            segment_rows.append(
                {
                    "asset": asset,
                    "phase": phase,
                    "rows": len(phase_rows),
                    "unique_families": len(families),
                    "dominant_family": families.most_common(1)[0][0] if families else "-",
                    "dominant_family_share": (families.most_common(1)[0][1] / len(phase_rows)) if phase_rows else 0.0,
                    "dominant_role": roles.most_common(1)[0][0] if roles else "-",
                    "avg_rekopplung": _mean(
                        [
                            _float(row.get("mcm_adaptive_rekopplung_quality") or row.get("mcm_rekopplung_quality"))
                            for row in phase_rows
                        ]
                    ),
                    "avg_strain": _mean([_float(row.get("mcm_strain_quality")) for row in phase_rows]),
                    "avg_afterimage": _mean([_float(row.get("mini_afterimage")) for row in phase_rows]),
                    "avg_temporal_trust": _mean([_float(row.get("mini_temporal_trust_support")) for row in phase_rows]),
                    "top20": " ".join(top_families),
                }
            )

        for left, right in [("frueh", "mitte"), ("mitte", "spaet"), ("frueh", "spaet")]:
            overlap = _jaccard(top_by_phase[left], top_by_phase[right])
            if overlap >= 0.75:
                reading = "stabile_familienbahn"
            elif overlap >= 0.45:
                reading = "drift_mit_anschluss"
            else:
                reading = "starke_neubildung"
            transition_rows.append(
                {
                    "asset": asset,
                    "transition": f"{left}_zu_{right}",
                    "top20_overlap": overlap,
                    "reading": reading,
                }
            )
    return segment_rows, transition_rows


def _write_csv(rows: list[dict[str, object]]) -> None:
    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(segment_rows: list[dict[str, object]], transition_rows: list[dict[str, object]]) -> None:
    lines = [
        "# 1839 - MCM-Reifungsbahn: 17k-Phasensegmente",
        "",
        "## Grundfrage",
        "",
        "Entsteht Reife in den 17k-Realwelten durch stabile Wiederkehr, durch Drift oder durch Brückenbildung zwischen Phasen?",
        "",
        "## Methode",
        "",
        "Jede 17k-Realwelt wurde in drei gleich große Abschnitte geteilt: frühe Phase, Mittelphase und späte Phase.",
        "Gelesen wurden Familienbreite, dominante Familie, dominante Feldrolle, Rekopplung, Strain, Nachhall und Feldzeit-Trust.",
        "",
        "## Phasenprofil",
        "",
        "| Asset | Phase | Familien | Dominante Familie | Anteil | Rolle | Rekopplung | Strain | Nachhall | Feldzeit |",
        "|---|---|---:|---|---:|---|---:|---:|---:|---:|",
    ]
    for row in segment_rows:
        lines.append(
            f"| {row['asset']} | {row['phase']} | {row['unique_families']} | `{row['dominant_family']}` | "
            f"{row['dominant_family_share']:.4f} | `{row['dominant_role']}` | {row['avg_rekopplung']:.4f} | "
            f"{row['avg_strain']:.4f} | {row['avg_afterimage']:.4f} | {row['avg_temporal_trust']:.4f} |"
        )

    lines.extend(
        [
            "",
            "## Übergänge",
            "",
            "| Asset | Übergang | Top20-Überlappung | Lesung |",
            "|---|---|---:|---|",
        ]
    )
    for row in transition_rows:
        lines.append(
            f"| {row['asset']} | `{row['transition']}` | {row['top20_overlap']:.3f} | `{row['reading']}` |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Reifung wirkt nicht wie ein einmaliger Umschlag.",
            "Die starken Familien bleiben phasenübergreifend anschlussfähig, gleichzeitig verändern sich Anteil, Nachhall und Feldzeitqualität.",
            "",
            "Damit ist die aktuelle Lesung:",
            "",
            "- Reife entsteht nicht nur aus Stabilität.",
            "- Reife entsteht auch aus haltbarer Drift.",
            "- Brückenbildung zeigt sich dort, wo Familien über Phasen erhalten bleiben, aber ihre Feldqualität verschieben.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollten die Familien mit hoher Phasenbindung einzeln gelesen werden: Welche Familien bleiben Kern, welche wandern an den Rand und welche bilden Brückenrollen?",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    segment_rows, transition_rows = _summaries()
    _write_csv(segment_rows)
    _write_md(segment_rows, transition_rows)
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"wrote {OUT_CSV.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
