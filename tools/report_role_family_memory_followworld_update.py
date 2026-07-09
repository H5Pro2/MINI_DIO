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
    same_basis = [row for row in rows if row["has_same_basis_follow_evidence"]]
    open_rows = [row for row in rows if not row["has_same_basis_follow_evidence"]]
    lines = [
        "# 2071 - Passive Rollenfamilien-Evidenz mit Folgeweltkontinuitaet und Rollendrift",
        "",
        "## Zweck",
        "",
        "Diese Erweiterung koppelt die neuen Folgeweltmessungen aus 2070 in die passive Rollenfamilien-Memory zurueck.",
        "",
        "Die Memory speichert nur Identitaet, Evidenzherkunft und kontinuierliche Messwerte. Familienanschluss, Stabilitaet und Reorganisation werden erst in diesem Report als vorlaeufige Forschungssprache gelesen.",
        "",
        "Die Erweiterung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung, kein Gate und keinen motorischen Impuls.",
        "",
        "## Numerisches Memory-Profil",
        "",
        f"- gespeicherte Rollenfamilien: `{profile['records']}`",
        f"- gespeicherte Mitglieder: `{profile['total_members']}`",
        f"- mit alter Folgeweltruecklesung: `{profile['with_legacy_follow_evidence']}`",
        f"- mit gleicher Symbolbasis: `{profile['with_same_basis_follow_evidence']}`",
        f"- Ereignisse auf gleicher Symbolbasis: `{profile['same_basis_follow_events']}`",
        f"- mittlere lokale Mitgliederabdeckung: `{_safe_float(profile['mean_same_basis_member_coverage']):.3f}`",
        f"- mittlere Mitgliedsverteilungsdrift: `{_safe_float(profile['mean_member_distribution_drift']):.3f}`",
        "",
        "## Gespeicherte Evidenz",
        "",
        "| family_symbol | evidence_symbol | role_family | Evidenzschichten | global gefunden | Weltpraesenz | ganze Familie | mittlere Abdeckung | Ereignisbalance | Verteilungsdrift |",
        "|---|---|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['family_symbol']} | {row['evidence_symbol']} | {row['role_family']} | "
            f"{row['evidence_layers']} | {row['same_basis_global_found_members']}/{row['members']} | "
            f"{_safe_float(row['same_basis_world_presence_ratio']):.3f} | "
            f"{_safe_float(row['same_basis_whole_family_ratio']):.3f} | "
            f"{_safe_float(row['same_basis_mean_member_coverage']):.3f} | "
            f"{_safe_float(row['same_basis_family_event_balance']):.3f} | "
            f"{_safe_float(row['member_distribution_drift']):.3f} |"
        )
    lines.extend(
        [
            "",
            "## Report-Lesung",
            "",
            "Die folgenden Begriffe werden aus den Messwerten abgeleitet, aber nicht in CSV oder JSON der Memory gespeichert.",
            "",
            f"- Folgeweltlesungen: `{report_profile['follow']}`",
            f"- innere Rollenlesungen: `{report_profile['internal_role']}`",
            f"- Tragelesungen: `{report_profile['carry']}`",
            f"- Anschlusslesungen: `{report_profile['connection']}`",
            f"- Driftlesungen: `{report_profile['drift']}`",
            "",
            "| role_family | Folgeweltlesung | Kontinuitaet | innere Rollenlesung | Tragelesung | Anschlusslesung | Driftlesung |",
            "|---|---|---:|---|---|---|---|",
        ]
    )
    for row in rows:
        reading = read_family(row)
        lines.append(
            f"| {row['role_family']} | {reading['follow_reading']} | "
            f"{_safe_float(reading['continuity_score']):.3f} | "
            f"{reading['internal_role_reading']} | {reading['carry_reading']} | "
            f"{reading['connection_reading']} | {reading['drift_reading']} |"
        )
    lines.extend(
        [
            "",
            "## Gleiche Symbolbasis",
            "",
            "| role_family | alt gefunden | neue Welten | ganze Familie | mittlere Abdeckung | Ereignisse | Drift | Dominanzbewegung |",
            "|---|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in same_basis:
        reading = read_family(row)
        lines.append(
            f"| {row['role_family']} | {row['legacy_found_members']}/{row['members']} | "
            f"{row['same_basis_worlds_present']}/{row['same_basis_worlds']} | "
            f"{row['same_basis_whole_family_worlds']}/{row['same_basis_worlds']} | "
            f"{_safe_float(row['same_basis_mean_member_coverage']):.3f} | "
            f"{row['same_basis_total_follow_events']} | "
            f"{_safe_float(row['member_distribution_drift']):.3f} | "
            f"{reading['source_dominant_member']}->{reading['follow_dominant_member']} |"
        )
    lines.extend(
        [
            "",
            "## Feldzeit der neuen Evidenz",
            "",
            "| role_family | Rekopplung spaet | Strain spaet | Nachhall-Delta | Feldzeit-Delta | Phasenbreite | Ereignisprofil |",
            "|---|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in same_basis:
        lines.append(
            f"| {row['role_family']} | {_safe_float(row['same_basis_mean_rekopplung_spaet']):.3f} | "
            f"{_safe_float(row['same_basis_mean_strain_spaet']):.3f} | "
            f"{_safe_float(row['same_basis_mean_afterimage_delta']):.3f} | "
            f"{_safe_float(row['same_basis_mean_temporal_delta']):.3f} | "
            f"{_safe_float(row['same_basis_mean_phase_complete_ratio']):.3f} | "
            f"{row['same_basis_member_event_profile'] or '-'} |"
        )
    lines.extend(
        [
            "",
            "## Noch offene Familien",
            "",
            "| role_family | Mitglieder | interne Ereignisse | Konzentration | Labelnaehe | vorhandene Schichten |",
            "|---|---:|---:|---:|---:|---|",
        ]
    )
    for row in open_rows:
        lines.append(
            f"| {row['role_family']} | {row['members']} | {row['cohesion_total_events']} | "
            f"{_safe_float(row['cohesion_event_concentration']):.3f} | "
            f"{_safe_float(row['cohesion_mean_label_jaccard']):.3f} | {row['evidence_layers']} |"
        )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Die Messwerte von `rf_07` zeigen dichte Folgeweltpraesenz, volle lokale Abdeckung und sehr geringe Mitgliedsverteilungsdrift.",
            "",
            "Bei `rf_21` bleibt die Familienabdeckung hoch, waehrend die Mitgliedsverteilung deutlich kippt. Der Report nennt das innere Reorganisation; die Memory speichert nur die zugrunde liegenden Profile und den Driftwert.",
            "",
            "`rf_05` wurde mit allen acht Mitgliedern wiedergefunden, erscheint lokal aber meist verteilt. Auch hier speichert die Memory keinen festen Familientyp, sondern Abdeckung, Balance, Phasenbreite und Drift.",
            "",
            "## Grenze",
            "",
            "Die numerische Memory enthaelt keine festen Bedeutungs-, Anschluss- oder Driftklassen und keine gewichtete Kontinuitaetszahl. Die Report-Lesung bleibt vorlaeufig, passiv und nicht handlungswirksam.",
            "",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Koppelt 2070 als numerische Evidenz in die Rollenfamilien-Memory.")
    parser.add_argument("--cohesion", default="docs/befunde/2001-3000/2066_REALVERSTAERKTE_ROLLENFAMILIEN_KOHAESION.summary.csv")
    parser.add_argument("--legacy-follow", default="docs/befunde/2001-3000/2068_ANSCHLUSSFAEHIGE_ROLLENFAMILIEN_IN_FOLGEWELTEN.summary.csv")
    parser.add_argument("--same-basis", default="docs/befunde/2001-3000/2070_ROLLENFAMILIEN_GLEICHE_SYMBOLBASIS_FOLGEWELTEN.summary.csv")
    parser.add_argument("--out-csv", default="docs/befunde/2001-3000/2071_PASSIVE_ROLLENFAMILIEN_MEMORY_FOLGEWELTDRIFT.csv")
    parser.add_argument("--out-json", default="memory/passive_role_family_memory_followworld.json")
    parser.add_argument("--out-md", default="docs/befunde/2001-3000/2071_PASSIVE_ROLLENFAMILIEN_MEMORY_FOLGEWELTDRIFT.md")
    args = parser.parse_args()

    memory = MCMRoleFamilyMemory.from_csvs(
        _resolve(args.cohesion),
        _resolve(args.legacy_follow),
        _resolve(args.same_basis),
    )
    memory.write_csv(_resolve(args.out_csv))
    memory.write_json(_resolve(args.out_json))
    _write_markdown(_resolve(args.out_md), memory)
    print(f"records={len(memory.records)}")
    print(f"same_basis_records={sum(record.has_same_basis_follow_evidence for record in memory.records)}")
    print(f"wrote={args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
