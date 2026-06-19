from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

from report_harmonic_sol5m_reference import DEFAULT_SUMMARIES
from report_harmonic_sol5m_reference import _avg
from report_harmonic_sol5m_reference import _fmt
from report_harmonic_sol5m_reference import _row as harmonic_row
from report_recoupling_quality import _resolve


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "222_ORGANISCHER_ADAPTIONSWEG_DIAGNOSE.md"


def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def _adaptation_axis(row: dict, reference: dict) -> dict:
    recoupling_need = _clamp((reference["rekopplung"] - row["rekopplung"]) * 8.0)
    field_need = _clamp((row["field_load"] - reference["field_load"]) * 3.0)
    memory_need = _clamp((row["memory_load"] - reference["memory_load"]) * 3.0)
    duration_need = _clamp((row["duration_load"] - reference["duration_load"]) * 3.5)
    afterimage_need = _clamp((row["afterimage"] - reference["afterimage"]) * 2.0)
    stimulus_rebase_need = _clamp(abs(row["adapted_load"] - reference["adapted_load"]) * 1.8)
    overbinding_need = _clamp(row["overbinding_risk"] - reference["overbinding_risk"])

    total_need = _clamp(
        (recoupling_need * 0.24)
        + (field_need * 0.20)
        + (memory_need * 0.20)
        + (duration_need * 0.16)
        + (afterimage_need * 0.08)
        + (stimulus_rebase_need * 0.06)
        + (overbinding_need * 0.06)
    )

    strongest = max(
        [
            ("rekopplung_vertiefen", recoupling_need),
            ("feldabstand_bilden", field_need),
            ("memory_leichter_tragen", memory_need),
            ("dauerlast_abbauen", duration_need),
            ("nachhall_loesbar_machen", afterimage_need),
            ("reizbasis_neu_einpendeln", stimulus_rebase_need),
        ],
        key=lambda item: item[1],
    )[0]

    return {
        "recoupling_need": recoupling_need,
        "field_need": field_need,
        "memory_need": memory_need,
        "duration_need": duration_need,
        "afterimage_need": afterimage_need,
        "stimulus_rebase_need": stimulus_rebase_need,
        "overbinding_need": overbinding_need,
        "total_need": total_need,
        "dominant_path": strongest,
    }


def _reference_profile(rows: list[dict]) -> dict:
    reference_rows = [row for row in rows if row["group"] == "referenz"]
    return {
        "rekopplung": _avg(reference_rows, "rekopplung"),
        "field_load": _avg(reference_rows, "field_load"),
        "memory_load": _avg(reference_rows, "memory_load"),
        "duration_load": _avg(reference_rows, "duration_load"),
        "afterimage": _avg(reference_rows, "afterimage"),
        "adapted_load": _avg(reference_rows, "adapted_load"),
        "overbinding_risk": _avg(reference_rows, "overbinding_risk"),
        "harmonic_index": _avg(reference_rows, "harmonic_index"),
    }


def _write_markdown(rows: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    reference = _reference_profile(rows)
    enriched = []
    for row in rows:
        if row["group"] == "referenz":
            continue
        enriched.append({**row, **_adaptation_axis(row, reference)})

    enriched = sorted(enriched, key=lambda row: row["total_need"], reverse=True)

    lines = [
        "# Organischer Adaptionsweg - Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest, welche Anpassungsrichtung eine schwerere Welt im Vergleich zum harmonischen SOL-5m-Referenzprofil benoetigt.",
        "Sie erzeugt keine Regel, kein Gate und keine Handlung.",
        "",
        "Hierarchie der Pruefung:",
        "",
        "1. Grundfrage: Welche Anpassungsfaehigkeit wuerde ein MCM-Feld organisch entwickeln, um eine schwerere Welt tragbarer zu lesen?",
        "2. Unterpruefung: Rekopplung, Feldlast, Memorylast, Dauerlast, Nachhall und Reizbasis gegen SOL 5m legen.",
        "3. Folgeschritt: Die staerksten Anpassungsachsen als passive Feldhygiene beschreiben.",
        "",
        "## Referenzprofil SOL 5m",
        "",
        f"- Rekopplung: `{_fmt(reference['rekopplung'], 6)}`",
        f"- Feldlast: `{_fmt(reference['field_load'], 4)}`",
        f"- Memorylast: `{_fmt(reference['memory_load'], 4)}`",
        f"- Dauerlast: `{_fmt(reference['duration_load'], 4)}`",
        f"- Nachhall: `{_fmt(reference['afterimage'], 4)}`",
        f"- Adaptierte Last: `{_fmt(reference['adapted_load'], 4)}`",
        f"- Ueberbindung: `{_fmt(reference['overbinding_risk'], 4)}`",
        "",
        "## Adaptionsachsen",
        "",
        "| Welt | Rolle | dominante Achse | Bedarf gesamt | Rekopplung | Feldabstand | Memory leichter | Dauerlast | Nachhall | Reizbasis | Ueberbindung |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in enriched:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["name"],
                    row["role"],
                    row["dominant_path"],
                    _fmt(row["total_need"], 4),
                    _fmt(row["recoupling_need"], 4),
                    _fmt(row["field_need"], 4),
                    _fmt(row["memory_need"], 4),
                    _fmt(row["duration_need"], 4),
                    _fmt(row["afterimage_need"], 4),
                    _fmt(row["stimulus_rebase_need"], 4),
                    _fmt(row["overbinding_need"], 4),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Lesart",
            "",
            "- `rekopplung_vertiefen`: Die Welt braucht bessere Rueckkehr in das Feldzentrum.",
            "- `feldabstand_bilden`: Die Welt wirkt zu direkt als Feldlast und braucht mehr Loesbarkeit.",
            "- `memory_leichter_tragen`: Episodenspuren schreiben zu schwer in die Bedeutungsbildung.",
            "- `dauerlast_abbauen`: Die Welt bleibt ueber Zeit zu stark im Feld.",
            "- `nachhall_loesbar_machen`: Restwirkung bleibt zu stark haengen.",
            "- `reizbasis_neu_einpendeln`: Die sensorische Basis passt noch nicht zur Welt.",
            "",
            "## Vorlaeufiger Befund",
            "",
            "Die bisherigen schweren Welten brauchen nicht alle dieselbe Anpassung.",
            "SOL 1h liegt vor allem bei Feldlast, Memorylast und Dauerlast weit weg vom SOL-5m-Profil.",
            "Lokale Stresssegmente koennen aehnlich schwer wirken, aber mit anderen Mischungen aus Feldlast, Nachhall und Reizbasis.",
            "",
            "Damit entsteht eine organische Sicht:",
            "",
            "Ein Organismus passt nicht nur Lautstaerke an.",
            "Er entwickelt unterschiedliche Arten, Weltwirkung wieder loesbar, tragbar und rekoppelbar zu machen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes wird ein Befund geschrieben.",
            "Dort wird festgehalten, welche Anpassungsachsen fuer MINI_DIO als passive Feldhygiene am wichtigsten sind.",
        ]
    )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Liest passive Adaptionsachsen gegen SOL 5m als Referenzprofil.")
    parser.add_argument("--summary", nargs=3, action="append", metavar=("NAME", "PATH", "GROUP"))
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    specs = args.summary or DEFAULT_SUMMARIES
    rows = [harmonic_row(name, path_text, group) for name, path_text, group in specs]
    _write_markdown(rows, _resolve(args.out))


if __name__ == "__main__":
    main()
