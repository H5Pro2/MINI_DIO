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


def _read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _find(rows: list[dict[str, str]], key: str, value: str) -> dict[str, str]:
    for row in rows:
        if row.get(key) == value:
            return row
    return {}


def _comparison_row(label: str, bull: dict[str, str], selloff: dict[str, str], reading: str) -> dict[str, object]:
    bull_range = _safe_float(bull.get("avg_range_pct"))
    sell_range = _safe_float(selloff.get("avg_range_pct"))
    bull_pressure = _safe_float(bull.get("avg_pressure_abs"))
    sell_pressure = _safe_float(selloff.get("avg_pressure_abs"))
    bull_rekopplung = _safe_float(bull.get("avg_rekopplung_abs"))
    sell_rekopplung = _safe_float(selloff.get("avg_rekopplung_abs"))
    return {
        "comparison": label,
        "bull_mode": bull.get("mode", "-"),
        "selloff_mode": selloff.get("mode", "-"),
        "bull_count": bull.get("count", "0"),
        "selloff_count": selloff.get("count", "0"),
        "bull_return_pct": bull.get("avg_return_pct", "0"),
        "selloff_return_pct": selloff.get("avg_return_pct", "0"),
        "bull_range_pct": bull.get("avg_range_pct", "0"),
        "selloff_range_pct": selloff.get("avg_range_pct", "0"),
        "range_delta_bull_minus_selloff": round(bull_range - sell_range, 6),
        "bull_pressure_abs": bull.get("avg_pressure_abs", "0"),
        "selloff_pressure_abs": selloff.get("avg_pressure_abs", "0"),
        "pressure_delta_bull_minus_selloff": round(bull_pressure - sell_pressure, 6),
        "bull_rekopplung_abs": bull.get("avg_rekopplung_abs", "0"),
        "selloff_rekopplung_abs": selloff.get("avg_rekopplung_abs", "0"),
        "rekopplung_delta_bull_minus_selloff": round(bull_rekopplung - sell_rekopplung, 6),
        "reading": reading,
        **PASSIVE_FLAGS,
    }


def build_rows(bull_modes: Path, selloff_modes: Path, bull_phases: Path, selloff_phases: Path) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    bull = _read(bull_modes)
    sell = _read(selloff_modes)
    comparisons = [
        _comparison_row(
            "tragende_expansion_vs_fallende_rekopplung",
            _find(bull, "mode", "getragene_expansion"),
            _find(sell, "mode", "abverkauf_mit_rekopplung"),
            "Bull-Seite zeigt tragende Expansion mit hoeherer Range und hoeherem Druck; Selloff-Seite zeigt fallende Rekopplung als engeren Rekopplungsmodus.",
        ),
        _comparison_row(
            "steigender_bruch_vs_fallender_bruch",
            _find(bull, "mode", "gerichtete_bewegung_mit_bruch"),
            _find(sell, "mode", "abverkauf_mit_bruch"),
            "Bruch existiert auf beiden Seiten, aber fallender Bruch ist staerker negativ und wirkt nachlaufend belasteter.",
        ),
        _comparison_row(
            "steigende_rekopplung_vs_fallende_rekopplung",
            _find(bull, "mode", "gerichtete_bewegung_mit_rekopplung"),
            _find(sell, "mode", "abverkauf_mit_rekopplung"),
            "Rekopplung existiert beidseitig; fallende Rekopplung ist haeufiger, steigende Rekopplung zeigt kleinere Range und offenere Anschlussqualitaet.",
        ),
        _comparison_row(
            "bull_expansion_vs_erholung_nach_abverkauf",
            _find(bull, "mode", "getragene_expansion"),
            _find(sell, "mode", "rekopplung_nach_abverkauf"),
            "Beide koennen stark positiv sein, aber Erholung nach Abverkauf traegt deutlich groessere Range und vorherige negative Last.",
        ),
    ]

    phase_summary: list[dict[str, object]] = []
    for side, path in (("bull", bull_phases), ("selloff", selloff_phases)):
        for row in _read(path):
            phase_summary.append(
                {
                    "side": side,
                    "phase": row.get("phase_hint", "-"),
                    "count": row.get("count", "0"),
                    "modes": row.get("modes", "-"),
                    "avg_return_pct": row.get("avg_return_pct", "0"),
                    "avg_range_pct": row.get("avg_range_pct", "0"),
                    "avg_before_pct": row.get("avg_before_pct", "0"),
                    "avg_after_pct": row.get("avg_after_pct", "0"),
                    "avg_pressure_abs": row.get("avg_pressure_abs", "0"),
                    "avg_rekopplung_abs": row.get("avg_rekopplung_abs", "0"),
                    **PASSIVE_FLAGS,
                }
            )
    return comparisons, phase_summary


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames: list[str] = []
    for row in rows:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _clean(value: object) -> str:
    return str(value).replace("|", "<br>")


def _write_md(path: Path, comparisons: list[dict[str, object]], phases: list[dict[str, object]]) -> None:
    lines = [
        f"# {path.stem.split('_', 1)[0]} - Bull/Selloff-Familienvergleich",
        "",
        "Passiver Vergleich zwischen Bull-/Rekopplung-Familie und Abverkauf-/Rekopplung-Familie.",
        "",
        "## Direktvergleich",
        "",
        "| Vergleich | Bull | Selloff | Bull Count | Selloff Count | Bull Return % | Selloff Return % | Range Delta | Druck Delta | Rekopplung Delta | Lesung |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in comparisons:
        clean = {key: _clean(value) for key, value in row.items()}
        lines.append(
            "| {comparison} | {bull_mode} | {selloff_mode} | {bull_count} | {selloff_count} | {bull_return_pct} | {selloff_return_pct} | {range_delta_bull_minus_selloff} | {pressure_delta_bull_minus_selloff} | {rekopplung_delta_bull_minus_selloff} | {reading} |".format(
                **clean
            )
        )
    lines.extend(
        [
            "",
            "## Phasen nebeneinander",
            "",
            "| Seite | Phase | Count | Modi | Return % | Range % | Vorher % | Nachher % | Druck | Rekopplung |",
            "|---|---|---:|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in phases:
        clean = {key: _clean(value) for key, value in row.items()}
        lines.append(
            "| {side} | {phase} | {count} | {modes} | {avg_return_pct} | {avg_range_pct} | {avg_before_pct} | {avg_after_pct} | {avg_pressure_abs} | {avg_rekopplung_abs} |".format(
                **clean
            )
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Bull- und Selloff-Seite sind nicht symmetrisch gespiegelt. Beide besitzen Bruch und Rekopplung, aber die Feldqualitaet unterscheidet sich.",
            "",
            "- Bull-Seite: tragende Expansion ist der staerkste Modus; sie traegt hoeheren Druck und groessere positive Fortsetzung.",
            "- Selloff-Seite: fallende Rekopplung ist der stabilere Grundmodus; sie ist weniger expansive Richtung als Rueckbindung unter fallender Last.",
            "- Erholung nach Abverkauf ist kein normales Bull-Fenster, sondern eine Sonderform: positive Bewegung nach vorheriger negativer Last mit sehr hoher Range.",
            "",
            "## Schluss",
            "",
            "Das MCM-Feld liest Bewegungsfamilien asymmetrisch. Aufwaertsbewegung wird eher als Expansion/Fortsetzung differenziert, Abverkauf eher als Bruch/Rekopplung/Erholung nach Belastung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese Asymmetrie gegen Topologie-Rollen gelesen werden: Liegen Bull-Fortsetzung und Selloff-Rekopplung an unterschiedlichen Rollenorten im MCM-Feld?",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bull-modes", required=True, type=Path)
    parser.add_argument("--selloff-modes", required=True, type=Path)
    parser.add_argument("--bull-phases", required=True, type=Path)
    parser.add_argument("--selloff-phases", required=True, type=Path)
    parser.add_argument("--out-comparison", required=True, type=Path)
    parser.add_argument("--out-phases", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    args = parser.parse_args()

    comparisons, phases = build_rows(args.bull_modes, args.selloff_modes, args.bull_phases, args.selloff_phases)
    _write_csv(args.out_comparison, comparisons)
    _write_csv(args.out_phases, phases)
    _write_md(args.out_md, comparisons, phases)
    print(f"comparisons={len(comparisons)}")
    print(f"phases={len(phases)}")
    print(f"wrote {args.out_md}")


if __name__ == "__main__":
    main()
