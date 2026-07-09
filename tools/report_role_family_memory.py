from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mcm_role_family_memory import MCMRoleFamilyMemory
from reports.role_family_research_reading import read_family, reading_profile


def _resolve(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _write_markdown(path: Path, memory: MCMRoleFamilyMemory) -> None:
    rows = memory.to_rows()
    profile = memory.quality_profile()
    report_profile = reading_profile(rows)
    lines = [
        "# 2069 - Passive Rollenfamilien-Memory",
        "",
        "## Zweck",
        "",
        "Diese Erweiterung ueberfuehrt die Befunde 2066 bis 2068 in eine passive Rollenfamilien-Memory.",
        "",
        "Die Memory speichert nur Familienidentitaet, Herkunft und kontinuierliche Erfahrungswerte. Benannte Lesungen werden ausschliesslich in diesem Report erzeugt und nicht in die Memory geschrieben.",
        "",
        "Die Memory bleibt passiv. Sie erzeugt keine Handlung, keine Richtung, kein Gate und keinen motorischen Impuls.",
        "",
        "## Numerisches Memory-Profil",
        "",
        f"- gespeicherte Rollenfamilien: `{profile['records']}`",
        f"- gespeicherte Mitglieder: `{profile['total_members']}`",
        f"- mit interner Kohaesionsevidenz: `{profile['with_cohesion_evidence']}`",
        f"- mit alter Folgeweltruecklesung: `{profile['with_legacy_follow_evidence']}`",
        f"- mit gleicher Symbolbasis: `{profile['with_same_basis_follow_evidence']}`",
        f"- interne Ereignisse: `{profile['cohesion_events']}`",
        f"- alte Ruecklesungsereignisse: `{profile['legacy_follow_events']}`",
        "",
        "## Gespeicherte Evidenz",
        "",
        "| family_symbol | evidence_symbol | role_family | Mitglieder | Evidenzschichten | Ereignisse intern | Konzentration | Labelnaehe | alt gefunden | alte Abdeckung |",
        "|---|---|---|---:|---|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['family_symbol']} | {row['evidence_symbol']} | {row['role_family']} | "
            f"{row['members']} | {row['evidence_layers']} | {row['cohesion_total_events']} | "
            f"{_safe_float(row['cohesion_event_concentration']):.3f} | "
            f"{_safe_float(row['cohesion_mean_label_jaccard']):.3f} | "
            f"{row['legacy_found_members']} | {_safe_float(row['legacy_member_coverage']):.3f} |"
        )
    lines.extend(
        [
            "",
            "## Report-Lesung",
            "",
            "Diese Begriffe sind eine ausserhalb der Memory erzeugte Forschungssicht auf die Messwerte.",
            "",
            f"- Folgeweltlesungen: `{report_profile['follow']}`",
            f"- Tragelesungen: `{report_profile['carry']}`",
            f"- Anschlusslesungen: `{report_profile['connection']}`",
            f"- Driftlesungen: `{report_profile['drift']}`",
            "",
            "| role_family | alte Ruecklesung | Tragelesung | Anschlusslesung | Driftlesung | Hinweis |",
            "|---|---|---|---|---|---|",
        ]
    )
    for row in rows:
        reading = read_family(row)
        lines.append(
            f"| {row['role_family']} | {reading['legacy_follow_reading']} | "
            f"{reading['carry_reading']} | {reading['connection_reading']} | "
            f"{reading['drift_reading']} | {reading['note']} |"
        )
    lines.extend(
        [
            "",
            "## Symbolbasis",
            "",
            "`family_symbol` bleibt an die Mitgliedschaft gebunden. `evidence_symbol` veraendert sich, wenn neue numerische Erfahrung hinzukommt.",
            "",
            "| role_family | member_symbols | found_member_symbols |",
            "|---|---|---|",
        ]
    )
    for row in rows:
        lines.append(
            f"| {row['role_family']} | {row['member_symbols'] or '-'} | "
            f"{row['found_member_symbols'] or '-'} |"
        )
    lines.extend(
        [
            "",
            "## Grenze",
            "",
            "Die CSV- und JSON-Memory enthalten keine festen Bedeutungs-, Anschluss- oder Driftklassen. Die Report-Lesung darf nicht als Regel, Strategie, Entry-Signal, Richtungsvorgabe oder Handlungsgate verwendet werden.",
            "",
            "Wie es weitergeht: Neue Folgeweltmessungen sollten als weitere numerische Evidenzschichten aufgenommen werden. Erst die Reports lesen daraus vorlaeufige Muster.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Schreibt numerische Rollenfamilien-Evidenz aus 2066/2068.")
    parser.add_argument("--cohesion", default="docs/befunde/2066_REALVERSTAERKTE_ROLLENFAMILIEN_KOHAESION.summary.csv")
    parser.add_argument("--connected", default="docs/befunde/2068_ANSCHLUSSFAEHIGE_ROLLENFAMILIEN_IN_FOLGEWELTEN.summary.csv")
    parser.add_argument("--out-csv", default="docs/befunde/2069_PASSIVE_ROLLENFAMILIEN_MEMORY.csv")
    parser.add_argument("--out-json", default="memory/passive_role_family_memory.json")
    parser.add_argument("--out-md", default="docs/befunde/2069_PASSIVE_ROLLENFAMILIEN_MEMORY.md")
    args = parser.parse_args()

    memory = MCMRoleFamilyMemory.from_csvs(_resolve(args.cohesion), _resolve(args.connected))
    memory.write_csv(_resolve(args.out_csv))
    memory.write_json(_resolve(args.out_json))
    _write_markdown(_resolve(args.out_md), memory)
    print(f"records={len(memory.records)}")
    print(f"wrote={args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
