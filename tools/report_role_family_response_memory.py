from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mcm_role_family_response_memory import (
    MCMRoleFamilyResponseMemory,
    ResponseEvidenceSource,
)


BEFUNDE = ROOT / "docs" / "befunde" / "2001-3000"
DEFAULT_FAMILY_MEMORY = BEFUNDE / "2069_PASSIVE_ROLLENFAMILIEN_MEMORY.csv"
DEFAULT_OUT_PREFIX = BEFUNDE / "2082_PASSIVE_FAMILIEN_KOMPONENTEN_ANTWORT_MEMORY"
DEFAULT_OUT_JSON = ROOT / "memory" / "passive_role_family_response_memory.json"


def _resolve(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _fmt(value: object, digits: int = 3) -> str:
    return f"{_safe_float(value):.{digits}f}"


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _sources(
    summary_2079: Path,
    summary_2080: Path,
    summary_2081: Path,
) -> list[ResponseEvidenceSource]:
    return [
        ResponseEvidenceSource(
            evidence_id="2079_2025_1h15m_matched_pseudo",
            summary_path=summary_2079,
            world_year_profile="2025",
            timeframe_profile="1h;15m",
            asset_profile="BTC;SOL",
            overall_real_worlds=12,
            subgroup_real_worlds=6,
        ),
        ResponseEvidenceSource(
            evidence_id="2080_2024_1h15m_matched_pseudo",
            summary_path=summary_2080,
            world_year_profile="2024",
            timeframe_profile="1h;15m",
            asset_profile="BTC;SOL",
            overall_real_worlds=12,
            subgroup_real_worlds=6,
        ),
        ResponseEvidenceSource(
            evidence_id="2081_2024_2025_30m_holdout",
            summary_path=summary_2081,
            world_year_profile="2024;2025",
            timeframe_profile="30m",
            asset_profile="BTC;SOL",
            overall_real_worlds=12,
            subgroup_real_worlds=6,
        ),
    ]


def _aggregate(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["role_family"]), str(row["component"]))].append(row)
    out: list[dict[str, object]] = []
    for (role_family, component), items in sorted(grouped.items()):
        out.append(
            {
                "role_family": role_family,
                "component": component,
                "response_symbol": items[0]["response_symbol"],
                "observations": len(items),
                "evidence_sources": len({str(row["evidence_id"]) for row in items}),
                "context_groups": len(
                    {
                        (
                            str(row["world_year_profile"]),
                            str(row["timeframe_profile"]),
                            str(row["asset_profile"]),
                            str(row["context_group"]),
                        )
                        for row in items
                    }
                ),
                "mean_delta_continuity": sum(
                    _safe_float(row["delta_continuity"]) for row in items
                )
                / len(items),
                "mean_delta_event_share": sum(
                    _safe_float(row["delta_event_share"]) for row in items
                )
                / len(items),
                "mean_delta_member_coverage": sum(
                    _safe_float(row["delta_member_coverage"]) for row in items
                )
                / len(items),
                "mean_percentile_continuity": sum(
                    _safe_float(row["percentile_continuity"]) for row in items
                )
                / len(items),
                "mean_percentile_event_share": sum(
                    _safe_float(row["percentile_event_share"]) for row in items
                )
                / len(items),
                "mean_percentile_member_coverage": sum(
                    _safe_float(row["percentile_member_coverage"]) for row in items
                )
                / len(items),
            }
        )
    return out


def _write_markdown(
    path: Path,
    memory: MCMRoleFamilyResponseMemory,
    aggregate: list[dict[str, object]],
    sources: list[ResponseEvidenceSource],
    order_stable: bool,
    duplicate_rejected: bool,
) -> None:
    profile = memory.quality_profile()
    lines = [
        "# 2082 - Passive Familien-Komponenten-Antwort-Memory",
        "",
        "## Zweck",
        "",
        "Befund 2081 begründet erstmals eine kleine organische Erweiterung der passiven Memory. Diese Schicht bewahrt kontinuierliche Reaktionen von Rollenfamilien auf Komponenten-Phasenänderungen samt Weltkontext und Abstand zu gematchten Pseudo-Familien.",
        "",
        "Die Memory speichert keine abgeleiteten Antwortklassen, keine Bestätigung, keine Bedeutung und keine Vorhersage. Sie verändert weder Wahrnehmung noch Handlung. Eine Familien-Komponenten-Antwort bleibt dieselbe Identität; neue Kontexte erzeugen zusätzliche numerische Beobachtungen.",
        "",
        "## Numerisches Memory-Profil",
        "",
        f"- Beobachtungen: `{profile['records']}`",
        f"- stabile Familien-Komponenten-Identitäten: `{profile['response_identities']}`",
        f"- eindeutige Beobachtungssymbole: `{profile['observation_identities']}`",
        f"- Rollenfamilien: `{profile['families']}`",
        f"- Komponenten: `{profile['components']}`",
        f"- Evidenzquellen: `{profile['evidence_sources']}`",
        f"- unterschiedliche Kontexte: `{profile['contexts']}`",
        f"- quellenreihenfolgenstabil: `{int(order_stable)}`",
        f"- doppelte Beobachtung abgewiesen: `{int(duplicate_rejected)}`",
        f"- passiv: `{profile['passive_only']}`",
        f"- handlungswirksam: `{profile['influences_action']}`",
        f"- Gate: `{profile['is_gate']}`",
        f"- Richtungssignal: `{profile['is_direction_signal']}`",
        "",
        "## Evidenzquellen",
        "",
        "| Evidenz | Jahre | Zeitebenen | Assets | Summary |",
        "|---|---|---|---|---|",
    ]
    for source in sources:
        lines.append(
            f"| `{source.evidence_id}` | `{source.world_year_profile}` | "
            f"`{source.timeframe_profile}` | `{source.asset_profile}` | "
            f"`{source.summary_path.resolve().relative_to(ROOT).as_posix()}` |"
        )

    lines.extend(
        [
            "",
            "## Antwortidentitäten",
            "",
            "Alle Werte sind arithmetische Übersichten der gespeicherten Einzelbeobachtungen. Sie sind keine Memory-Klassen.",
            "",
            "| Familie | Komponente | Antwortsymbol | Beobachtungen | Quellen | Kontexte | Δ Kontinuität | Δ Ereignisanteil | Δ Abdeckung | Perzentile K/E/A |",
            "|---|---|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in aggregate:
        lines.append(
            f"| `{row['role_family']}` | `{row['component']}` | `{row['response_symbol']}` | "
            f"{row['observations']} | {row['evidence_sources']} | {row['context_groups']} | "
            f"{_fmt(row['mean_delta_continuity'])} | "
            f"{_fmt(row['mean_delta_event_share'], 4)} | "
            f"{_fmt(row['mean_delta_member_coverage'])} | "
            f"{_fmt(row['mean_percentile_continuity'])}/"
            f"{_fmt(row['mean_percentile_event_share'])}/"
            f"{_fmt(row['mean_percentile_member_coverage'])} |"
        )

    lines.extend(
        [
            "",
            "## Organische Erweiterung",
            "",
            "Die Erweiterung ist generisch: Jede Rollenfamilie und jede gemessene Komponente kann Beobachtungen erhalten. `rf_05` wird weder im Memory-Modul noch in der DIO-Syntax bevorzugt. Dass seine Volumenreaktion derzeit stark trägt, bleibt Inhalt der gespeicherten Evidenz und keine programmierte Eigenschaft.",
            "",
            "Neue Erfahrung wird als zusätzliche Beobachtung mit eigener Herkunft, Weltlage und numerischem Antwortvektor angefügt. Die stabile Antwortidentität verbindet diese Beobachtungen, ohne sie in eine feste Bedeutung zu verdichten.",
            "",
            "## Technische Grenze",
            "",
            "`read_by_mini_dio`, `influences_action`, `is_gate`, `is_motoric`, `is_entry_signal` und `is_direction_signal` bleiben `0`. Die lokale JSON-Memory ist experimenteller Zustand und bleibt durch die bestehende Repository-Grenze ungetrackt; die reproduzierbare CSV-Projektion und der Generator sind dokumentiert.",
            "",
            "Die Memory enthält bewusst keine Felder für Antwortklasse, Bestätigung, Bedeutung oder Vorhersage. Eine spätere passive Rücklesung müsste erneut fachlich begründet werden und darf nicht stillschweigend aus dieser Speicherung entstehen.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Schreibt passive numerische Familien-Komponenten-Antworten."
    )
    parser.add_argument("--family-memory", default=str(DEFAULT_FAMILY_MEMORY))
    parser.add_argument(
        "--summary-2079",
        default=str(BEFUNDE / "2079_ROLLENFAMILIEN_GEMATCHE_PSEUDOFAMILIEN.summary.csv"),
    )
    parser.add_argument(
        "--summary-2080",
        default=str(BEFUNDE / "2080_RF08_SIGN_GEMATCHTER_CROSSYEAR_KONTRAST.summary.csv"),
    )
    parser.add_argument(
        "--summary-2081",
        default=str(BEFUNDE / "2081_RF08_SIGN_RF05_VOLUME_30M_HOLDOUT.summary.csv"),
    )
    parser.add_argument("--out-prefix", default=str(DEFAULT_OUT_PREFIX))
    parser.add_argument("--out-json", default=str(DEFAULT_OUT_JSON))
    args = parser.parse_args()

    family_memory = _resolve(args.family_memory)
    sources = _sources(
        _resolve(args.summary_2079),
        _resolve(args.summary_2080),
        _resolve(args.summary_2081),
    )
    out_prefix = _resolve(args.out_prefix)
    out_json = _resolve(args.out_json)

    memory = MCMRoleFamilyResponseMemory.from_sources(
        family_memory,
        sources,
        ROOT,
    )
    errors = memory.validate()
    if errors:
        raise ValueError(";".join(errors))
    reversed_memory = MCMRoleFamilyResponseMemory.from_sources(
        family_memory,
        list(reversed(sources)),
        ROOT,
    )
    order_stable = memory.to_rows() == reversed_memory.to_rows()
    if not order_stable:
        raise ValueError("Memory hängt von der Reihenfolge der Evidenzquellen ab")
    records_before_duplicate = len(memory.records)
    duplicate_rejected = not memory.append(memory.records[0])
    duplicate_rejected = duplicate_rejected and len(memory.records) == records_before_duplicate
    if not duplicate_rejected:
        raise ValueError("Doppelte Beobachtung wurde in die Memory aufgenommen")

    rows = memory.to_rows()
    aggregate = _aggregate(rows)
    memory.write_csv(out_prefix.with_suffix(".csv"))
    memory.write_json(out_json)
    _write_csv(out_prefix.with_suffix(".summary.csv"), aggregate)
    _write_markdown(
        out_prefix.with_suffix(".md"),
        memory,
        aggregate,
        sources,
        order_stable,
        duplicate_rejected,
    )

    print(f"records={len(rows)}")
    print(f"response_identities={memory.quality_profile()['response_identities']}")
    print(f"aggregate_rows={len(aggregate)}")
    print(f"validation_errors={len(errors)}")
    print(f"order_stable={order_stable}")
    print(f"duplicate_rejected={duplicate_rejected}")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
