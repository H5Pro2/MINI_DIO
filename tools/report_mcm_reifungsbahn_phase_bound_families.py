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

OUT_CSV = ROOT / "docs/befunde/1840_MCM_REIFUNGSBAHN_PHASENGEBUNDENE_FAMILIEN.csv"
OUT_MD = ROOT / "docs/befunde/1840_MCM_REIFUNGSBAHN_PHASENGEBUNDENE_FAMILIEN.md"


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


def _phase(index: int, total: int) -> str:
    ratio = index / total if total else 0.0
    if ratio < 1 / 3:
        return "frueh"
    if ratio < 2 / 3:
        return "mitte"
    return "spaet"


def _read_rows(run_dir: str) -> list[dict[str, str]]:
    path = ROOT / run_dir / "episodes.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _classify(row: dict[str, object]) -> str:
    presence = int(row["phase_presence"])
    share_delta = _float(row["share_spaet"]) - _float(row["share_frueh"])
    after_delta = _float(row["afterimage_spaet"]) - _float(row["afterimage_frueh"])
    temporal_delta = _float(row["temporal_spaet"]) - _float(row["temporal_frueh"])
    strain_delta = _float(row["strain_spaet"]) - _float(row["strain_frueh"])

    if presence == 3 and after_delta > 0.18 and temporal_delta > 0.10 and abs(share_delta) < 0.03:
        return "kernfamilie_mit_feldzeitverdichtung"
    if presence == 3 and share_delta > 0.012 and after_delta > 0.12:
        return "brueckenfamilie_wird_staerker"
    if presence == 3 and share_delta < -0.012 and after_delta > 0.12:
        return "fruehe_familie_mit_nachhallrest"
    if presence == 2 and after_delta > 0.12:
        return "phasenbruecke_lokal"
    if strain_delta > 0.025:
        return "randnahe_spannungszunahme"
    return "anschlussfaehige_oberflaeche"


def _rows() -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for asset, run_dir in RUNS:
        rows = _read_rows(run_dir)
        buckets: dict[str, dict[str, list[dict[str, str]]]] = defaultdict(lambda: defaultdict(list))
        phase_totals = Counter()
        for index, row in enumerate(rows):
            phase = _phase(index, len(rows))
            family = _family(row)
            buckets[family][phase].append(row)
            phase_totals[phase] += 1

        total_counts = Counter(_family(row) for row in rows)
        for family, count in total_counts.most_common(36):
            phase_rows = {phase: buckets[family].get(phase, []) for phase in ["frueh", "mitte", "spaet"]}
            phase_presence = sum(1 for values in phase_rows.values() if values)
            row: dict[str, object] = {
                "asset": asset,
                "family": family,
                "total_count": count,
                "phase_presence": phase_presence,
                "dominant_role": Counter(_role(item) for phase in phase_rows.values() for item in phase).most_common(1)[0][0],
            }
            for phase in ["frueh", "mitte", "spaet"]:
                values = phase_rows[phase]
                row[f"count_{phase}"] = len(values)
                row[f"share_{phase}"] = len(values) / phase_totals[phase] if phase_totals[phase] else 0.0
                row[f"rekopplung_{phase}"] = _mean(
                    [
                        _float(item.get("mcm_adaptive_rekopplung_quality") or item.get("mcm_rekopplung_quality"))
                        for item in values
                    ]
                )
                row[f"strain_{phase}"] = _mean([_float(item.get("mcm_strain_quality")) for item in values])
                row[f"afterimage_{phase}"] = _mean([_float(item.get("mini_afterimage")) for item in values])
                row[f"temporal_{phase}"] = _mean([_float(item.get("mini_temporal_trust_support")) for item in values])
            row["share_delta_spaet_frueh"] = _float(row["share_spaet"]) - _float(row["share_frueh"])
            row["afterimage_delta_spaet_frueh"] = _float(row["afterimage_spaet"]) - _float(row["afterimage_frueh"])
            row["temporal_delta_spaet_frueh"] = _float(row["temporal_spaet"]) - _float(row["temporal_frueh"])
            row["strain_delta_spaet_frueh"] = _float(row["strain_spaet"]) - _float(row["strain_frueh"])
            row["family_reading"] = _classify(row)
            output.append(row)
    return output


def _write_csv(rows: list[dict[str, object]]) -> None:
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(rows: list[dict[str, object]]) -> None:
    reading_counts = Counter(str(row["family_reading"]) for row in rows)
    lines = [
        "# 1840 - MCM-Reifungsbahn: phasengebundene Familien",
        "",
        "## Grundfrage",
        "",
        "Welche Familien tragen die Reifung ueber die 17k-Phasen hinweg: Kern, Bruecke, Rand oder nur Oberflaeche?",
        "",
        "## Methode",
        "",
        "Die staerksten Familien jeder 17k-Realwelt wurden ueber Frueh-, Mittel- und Spaetphase gelesen.",
        "Bewertet wurden Phasenpraesenz, Anteilverschiebung, Rekopplung, Strain, Nachhall und Feldzeit-Trust.",
        "",
        "## Rollenverteilung",
        "",
    ]
    for key, count in reading_counts.most_common():
        lines.append(f"- `{key}`: {count}")

    lines.extend(
        [
            "",
            "## Staerkste phasengebundene Familien",
            "",
            "| Asset | Familie | Lesung | Rolle | Praesenz | Anteil frueh | Anteil mitte | Anteil spaet | Nachhall-Delta | Feldzeit-Delta | Strain-Delta |",
            "|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    priority = {
        "kernfamilie_mit_feldzeitverdichtung": 0,
        "brueckenfamilie_wird_staerker": 1,
        "fruehe_familie_mit_nachhallrest": 2,
        "phasenbruecke_lokal": 3,
        "randnahe_spannungszunahme": 4,
        "anschlussfaehige_oberflaeche": 5,
    }
    selected = sorted(
        rows,
        key=lambda row: (
            priority.get(str(row["family_reading"]), 99),
            -int(row["phase_presence"]),
            -int(row["total_count"]),
        ),
    )[:40]
    for row in selected:
        lines.append(
            f"| {row['asset']} | `{row['family']}` | `{row['family_reading']}` | `{row['dominant_role']}` | "
            f"{row['phase_presence']} | {_float(row['share_frueh']):.4f} | {_float(row['share_mitte']):.4f} | "
            f"{_float(row['share_spaet']):.4f} | {_float(row['afterimage_delta_spaet_frueh']):.4f} | "
            f"{_float(row['temporal_delta_spaet_frueh']):.4f} | {_float(row['strain_delta_spaet_frueh']):.4f} |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die phasenstabilen Familien sind keine festen Woerter.",
            "Sie wirken eher wie Feldrollen, die ueber Weltzeit Anschluss behalten und dabei ihre Qualitaet verschieben.",
            "",
            "Wichtig ist die Trennung:",
            "",
            "- Kernfamilien bleiben praesent und verdichten Nachhall/Feldzeit.",
            "- Brueckenfamilien werden spaeter staerker oder verbinden lokale Phasen.",
            "- Fruehe Familien koennen als Nachhallrest erhalten bleiben.",
            "- Randnaehe ist nicht der Normalfall, sondern eine eigene Spannungslesung.",
            "",
            "## Organische Erweiterungsrichtung",
            "",
            "Aus diesem Befund folgt noch keine Handlungsschicht.",
            "Eine sinnvolle organische Erweiterung waere eine passive `Feldrollen-Memory`: Familien speichern nicht nur Haeufigkeit, sondern ihre Reifungsbewegung ueber Phasen.",
            "Das wuerde MINI_DIO erlauben, Feldintelligenz nicht als Regel, sondern als gewachsene Rollenkenntnis zu tragen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte geprueft werden, ob eine passive Feldrollen-Memory aus diesen Bewegungsprofilen aufgebaut werden kann, ohne Handlung oder harte Gates einzufuehren.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    rows = _rows()
    _write_csv(rows)
    _write_md(rows)
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"wrote {OUT_CSV.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
