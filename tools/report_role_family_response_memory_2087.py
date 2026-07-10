from __future__ import annotations

import argparse
from pathlib import Path

try:
    from tools.report_role_family_response_memory import (
        BEFUNDE,
        DEFAULT_FAMILY_MEMORY,
        DEFAULT_OUT_JSON,
        _aggregate,
        _fmt,
        _resolve,
        _sources,
        _write_csv,
    )
except ModuleNotFoundError:
    from report_role_family_response_memory import (
        BEFUNDE,
        DEFAULT_FAMILY_MEMORY,
        DEFAULT_OUT_JSON,
        _aggregate,
        _fmt,
        _resolve,
        _sources,
        _write_csv,
    )

from mini_dio.mcm_role_family_response_memory import (
    MCMRoleFamilyResponseMemory,
    ResponseEvidenceSource,
)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT_PREFIX = BEFUNDE / "2087_PASSIVE_ANTWORT_MEMORY_WIDERSPRUCHSREIFUNG"
RF05_VOLUME = ("rf_05", "volume")


def _base_sources() -> list[ResponseEvidenceSource]:
    sources = _sources(
        BEFUNDE / "2079_ROLLENFAMILIEN_GEMATCHE_PSEUDOFAMILIEN.summary.csv",
        BEFUNDE / "2080_RF08_SIGN_GEMATCHTER_CROSSYEAR_KONTRAST.summary.csv",
        BEFUNDE / "2081_RF08_SIGN_RF05_VOLUME_30M_HOLDOUT.summary.csv",
    )
    sources.append(
        ResponseEvidenceSource(
            evidence_id="2083_2024_2025_5m_rf05_volume_holdout",
            summary_path=BEFUNDE / "2083_RF05_VOLUME_5M_MEMORY_REIFUNG.summary.csv",
            world_year_profile="2024;2025",
            timeframe_profile="5m",
            asset_profile="BTC;SOL",
            overall_real_worlds=12,
            subgroup_real_worlds=6,
        )
    )
    return sources


def _new_source(summary_2086: Path) -> ResponseEvidenceSource:
    return ResponseEvidenceSource(
        evidence_id="2086_2024_2025_5m_orientation_holdout",
        summary_path=summary_2086,
        world_year_profile="2024;2025",
        timeframe_profile="5m",
        asset_profile="BTC;SOL",
        overall_real_worlds=12,
        subgroup_real_worlds=6,
    )


def _rf05_volume(
    aggregate: list[dict[str, object]],
) -> dict[str, object]:
    return next(
        row
        for row in aggregate
        if (str(row["role_family"]), str(row["component"])) == RF05_VOLUME
    )


def _write_markdown(
    path: Path,
    before: MCMRoleFamilyResponseMemory,
    after: MCMRoleFamilyResponseMemory,
    before_aggregate: list[dict[str, object]],
    after_aggregate: list[dict[str, object]],
    new_observations: list[dict[str, object]],
    order_stable: bool,
    duplicate_rejected: bool,
) -> None:
    before_profile = before.quality_profile()
    after_profile = after.quality_profile()
    previous = _rf05_volume(before_aggregate)
    current = _rf05_volume(after_aggregate)
    lines = [
        "# 2087 - Passive Antwort-Memory mit widersprechender Erfahrung",
        "",
        "## Zweck",
        "",
        "Befund 2086 widerlegt die positive Kreuzorientierung aus 2085 und begrenzt die Volumenphasenantwort auf einen steigenden Familienereignisanteil bei sinkender Kontinuität und Mitgliederbreite. Diese unabhängige Erfahrung wird vollständig und ohne sprachliche Antwortklasse an dieselbe passive Familien-Komponenten-Identität angehängt.",
        "",
        "Die Memory speichert ausschließlich Herkunft, Kontext, numerischen Antwortvektor und Abstand zu gematchten Pseudo-Familien. `verstaerkt`, `gemischt`, Erwartung, Bestätigung und Widerlegung sind Berichtssprache und keine Memory-Felder.",
        "",
        "## Reifungsprofil",
        "",
        f"- Beobachtungen vorher/nachher: `{before_profile['records']}/{after_profile['records']}`",
        f"- Antwortidentitäten vorher/nachher: `{before_profile['response_identities']}/{after_profile['response_identities']}`",
        f"- eindeutige Beobachtungssymbole: `{after_profile['observation_identities']}`",
        f"- Evidenzquellen vorher/nachher: `{before_profile['evidence_sources']}/{after_profile['evidence_sources']}`",
        f"- Kontexte vorher/nachher: `{before_profile['contexts']}/{after_profile['contexts']}`",
        f"- neue Beobachtungen: `{len(new_observations)}`",
        f"- quellenreihenfolgenstabil: `{int(order_stable)}`",
        f"- doppelte Beobachtung abgewiesen: `{int(duplicate_rejected)}`",
        f"- passiv/handlungswirksam: `{after_profile['passive_only']}/{after_profile['influences_action']}`",
        "",
        "## rf_05:volume vor und nach 2086",
        "",
        "| Zustand | Antwortsymbol | Beobachtungen | Quellen | Δ Kontinuität | Δ Ereignisanteil | Δ Abdeckung | Perzentile K/E/A |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
        f"| vorher | `{previous['response_symbol']}` | {previous['observations']} | {previous['evidence_sources']} | {_fmt(previous['mean_delta_continuity'])} | {_fmt(previous['mean_delta_event_share'], 4)} | {_fmt(previous['mean_delta_member_coverage'])} | {_fmt(previous['mean_percentile_continuity'])}/{_fmt(previous['mean_percentile_event_share'])}/{_fmt(previous['mean_percentile_member_coverage'])} |",
        f"| nachher | `{current['response_symbol']}` | {current['observations']} | {current['evidence_sources']} | {_fmt(current['mean_delta_continuity'])} | {_fmt(current['mean_delta_event_share'], 4)} | {_fmt(current['mean_delta_member_coverage'])} | {_fmt(current['mean_percentile_continuity'])}/{_fmt(current['mean_percentile_event_share'])}/{_fmt(current['mean_percentile_member_coverage'])} |",
        "",
        "## Neue numerische Beobachtungen",
        "",
        "| Kontext | Beobachtungssymbol | Δ Kontinuität | Δ Ereignisanteil | Δ Abdeckung | Perzentile K/E/A |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for row in new_observations:
        lines.append(
            f"| `{row['context_group']}` | `{row['observation_symbol']}` | "
            f"{_fmt(row['delta_continuity'])} | {_fmt(row['delta_event_share'], 4)} | "
            f"{_fmt(row['delta_member_coverage'])} | "
            f"{_fmt(row['percentile_continuity'])}/"
            f"{_fmt(row['percentile_event_share'])}/"
            f"{_fmt(row['percentile_member_coverage'])} |"
        )
    lines.extend(
        [
            "",
            "## Organische Bedeutung",
            "",
            "Die stabile Antwortidentität bleibt bestehen, während ihr Erfahrungsraum eine gegenläufige Feldlage aufnimmt. Dadurch wird frühere Evidenz weder überschrieben noch zur Wahrheit erklärt. Die numerische Mitte darf sich mit neuer Erfahrung verschieben, ohne dass MINI_DIO eine feste Antwortklasse erhält.",
            "",
            "Die Kontextzahl wächst nicht, weil 2086 dieselben Jahr-, Zeitebenen-, Asset- und Gruppendimensionen wie 2083 verwendet. Neu sind Evidenzherkunft und Antwortwerte. Genau diese Trennung verhindert, dass gleiche Kontextbezeichnungen mit gleicher Erfahrung verwechselt werden.",
            "",
            "## Technische Grenze",
            "",
            "`read_by_mini_dio`, `influences_action`, `is_gate`, `is_motoric`, `is_entry_signal` und `is_direction_signal` bleiben `0`. Es entsteht weder eine Kreuzkopplungsidentität noch eine Ereignisanteil-Regel. Die lokale JSON-Memory bleibt ungetrackt; CSV-Projektion und Generator sind reproduzierbar.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Reift die passive Antwort-Memory mit Befund 2086."
    )
    parser.add_argument("--family-memory", default=str(DEFAULT_FAMILY_MEMORY))
    parser.add_argument(
        "--summary-2086",
        default=str(BEFUNDE / "2086_RF05_VOLUME_ORIENTIERUNGS_HOLDOUT.summary.csv"),
    )
    parser.add_argument("--out-prefix", default=str(DEFAULT_OUT_PREFIX))
    parser.add_argument("--out-json", default=str(DEFAULT_OUT_JSON))
    args = parser.parse_args()

    family_memory = _resolve(args.family_memory)
    out_prefix = _resolve(args.out_prefix)
    out_json = _resolve(args.out_json)
    base_sources = _base_sources()
    all_sources = [*base_sources, _new_source(_resolve(args.summary_2086))]

    before = MCMRoleFamilyResponseMemory.from_sources(
        family_memory, base_sources, ROOT
    )
    after = MCMRoleFamilyResponseMemory.from_sources(
        family_memory, all_sources, ROOT
    )
    errors = after.validate()
    if errors:
        raise ValueError(";".join(errors))
    reversed_memory = MCMRoleFamilyResponseMemory.from_sources(
        family_memory, list(reversed(all_sources)), ROOT
    )
    order_stable = after.to_rows() == reversed_memory.to_rows()
    if not order_stable:
        raise ValueError("Memory hängt von der Reihenfolge der Evidenzquellen ab")

    before_symbols = {str(row["observation_symbol"]) for row in before.to_rows()}
    new_observations = [
        row
        for row in after.to_rows()
        if str(row["observation_symbol"]) not in before_symbols
    ]
    if len(new_observations) != 5:
        raise ValueError(f"Erwartet wurden 5 neue Beobachtungen, gefunden {len(new_observations)}")
    if any(
        row["evidence_id"] != "2086_2024_2025_5m_orientation_holdout"
        for row in new_observations
    ):
        raise ValueError("Neue Beobachtungen stammen nicht ausschließlich aus 2086")
    if after.quality_profile()["response_identities"] != before.quality_profile()[
        "response_identities"
    ]:
        raise ValueError("Die Reifung hat neue Antwortidentitäten erzeugt")

    before_aggregate = _aggregate(before.to_rows())
    after_aggregate = _aggregate(after.to_rows())
    previous = _rf05_volume(before_aggregate)
    current = _rf05_volume(after_aggregate)
    if current["response_symbol"] != previous["response_symbol"]:
        raise ValueError("rf_05:volume hat seine Antwortidentität gewechselt")

    records_before_duplicate = len(after.records)
    duplicate_rejected = not after.append(after.records[0])
    duplicate_rejected = duplicate_rejected and len(after.records) == records_before_duplicate
    if not duplicate_rejected:
        raise ValueError("Doppelte Beobachtung wurde in die Memory aufgenommen")

    after.write_csv(out_prefix.with_suffix(".csv"))
    after.write_json(out_json)
    _write_csv(out_prefix.with_suffix(".summary.csv"), after_aggregate)
    _write_markdown(
        out_prefix.with_suffix(".md"),
        before,
        after,
        before_aggregate,
        after_aggregate,
        new_observations,
        order_stable,
        duplicate_rejected,
    )

    print(f"records_before={len(before.records)}")
    print(f"records_after={len(after.records)}")
    print(f"new_observations={len(new_observations)}")
    print(f"response_identities={after.quality_profile()['response_identities']}")
    print(f"rf05_volume_response_symbol={current['response_symbol']}")
    print(f"rf05_volume_observations={current['observations']}")
    print(f"validation_errors={len(errors)}")
    print(f"order_stable={order_stable}")
    print(f"duplicate_rejected={duplicate_rejected}")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
