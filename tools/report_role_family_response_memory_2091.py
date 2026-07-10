from __future__ import annotations

import argparse
import csv
from pathlib import Path

try:
    from tools.report_role_family_response_memory import (
        BEFUNDE,
        DEFAULT_FAMILY_MEMORY,
        DEFAULT_OUT_JSON,
        _aggregate,
        _fmt,
        _resolve,
        _write_csv,
    )
    from tools.report_role_family_response_memory_2087 import (
        _base_sources,
        _new_source,
    )
except ModuleNotFoundError:
    from report_role_family_response_memory import (
        BEFUNDE,
        DEFAULT_FAMILY_MEMORY,
        DEFAULT_OUT_JSON,
        _aggregate,
        _fmt,
        _resolve,
        _write_csv,
    )
    from report_role_family_response_memory_2087 import (
        _base_sources,
        _new_source,
    )

from mini_dio.mcm_role_family_response_memory import (
    MCMRoleFamilyResponseMemory,
    ResponseEvidenceSource,
)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MEMORY_2087 = BEFUNDE / "2087_PASSIVE_ANTWORT_MEMORY_WIDERSPRUCHSREIFUNG.csv"
DEFAULT_SUMMARY_2089 = BEFUNDE / "2089_ALLE_ROLLENFAMILIEN_VOLUME_EVIDENZBALANCE.summary.csv"
DEFAULT_SUMMARY_2090 = BEFUNDE / "2090_ALLE_ROLLENFAMILIEN_VOLUME_30M_TRANSFER.summary.csv"
DEFAULT_OUT_PREFIX = BEFUNDE / "2091_PASSIVE_VOLUME_ANTWORT_MEMORY_EVIDENZBALANCE"
ROLE_FAMILIES = ("rf_05", "rf_06", "rf_07", "rf_08", "rf_10", "rf_13", "rf_17", "rf_21")


def _load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _source_path(prefix: Path, label: str) -> Path:
    return Path(f"{prefix}.source_{label}.csv")


def _filter_sources(
    summary_2089: Path,
    summary_2090: Path,
) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    rows_2089 = _load_csv(summary_2089)
    rows_2090 = _load_csv(summary_2090)
    source_2083 = [
        row
        for row in rows_2089
        if row["holdout_id"] == "2083_5m_windows"
        and row["role_family"] != "rf_05"
    ]
    source_2086 = [
        row
        for row in rows_2089
        if row["holdout_id"] == "2086_5m_windows"
        and row["role_family"] != "rf_05"
    ]
    source_2090 = [
        row
        for row in rows_2090
        if row["role_family"] not in {"rf_05", "rf_08"}
    ]
    return source_2083, source_2086, source_2090


def _additional_sources(
    source_2083: Path,
    source_2086: Path,
    source_2090: Path,
) -> list[ResponseEvidenceSource]:
    return [
        ResponseEvidenceSource(
            evidence_id="2089_2083_5m_other_families_volume",
            summary_path=source_2083,
            world_year_profile="2024;2025",
            timeframe_profile="5m",
            asset_profile="BTC;SOL",
            overall_real_worlds=12,
            subgroup_real_worlds=6,
        ),
        ResponseEvidenceSource(
            evidence_id="2089_2086_5m_other_families_volume",
            summary_path=source_2086,
            world_year_profile="2024;2025",
            timeframe_profile="5m",
            asset_profile="BTC;SOL",
            overall_real_worlds=12,
            subgroup_real_worlds=6,
        ),
        ResponseEvidenceSource(
            evidence_id="2090_2081_30m_other_families_volume",
            summary_path=source_2090,
            world_year_profile="2024;2025",
            timeframe_profile="30m",
            asset_profile="BTC;SOL",
            overall_real_worlds=12,
            subgroup_real_worlds=6,
        ),
    ]


def _volume_rows(
    aggregate: list[dict[str, object]],
) -> dict[str, dict[str, object]]:
    return {
        str(row["role_family"]): row
        for row in aggregate
        if row["component"] == "volume"
    }


def _write_markdown(
    path: Path,
    before: MCMRoleFamilyResponseMemory,
    after: MCMRoleFamilyResponseMemory,
    before_aggregate: list[dict[str, object]],
    after_aggregate: list[dict[str, object]],
    new_observations: list[dict[str, object]],
    source_paths: list[Path],
    source_counts: list[int],
    order_stable: bool,
    duplicate_rejected: bool,
) -> None:
    before_profile = before.quality_profile()
    after_profile = after.quality_profile()
    previous = _volume_rows(before_aggregate)
    current = _volume_rows(after_aggregate)
    new_by_family = {
        role_family: sum(
            row["role_family"] == role_family for row in new_observations
        )
        for role_family in ROLE_FAMILIES
    }
    lines = [
        "# 2091 - Passive Volumen-Antwort-Memory mit balancierter Evidenz",
        "",
        "## Zweck",
        "",
        "Befunde 2089 und 2090 gleichen die Volumenphasenevidenz aller acht Rollenfamilien über zwei 5m-Holdouts und einen 30m-Transfer an. Diese numerischen Beobachtungen werden nun provenancegetreu in die passive Antwort-Memory aufgenommen.",
        "",
        "Bereits gespeicherte `rf_05`-Beobachtungen aus 2083 und 2086 sowie `rf_05`- und `rf_08`-Beobachtungen aus 2081 werden ausdrücklich nicht unter neuen Evidenznamen wiederholt. Die Quellsichten enthalten ausschließlich bisher fehlende Familien.",
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
        "## Provenienzquellen",
        "",
        "| Quellsicht | neue Zeilen | ausgeschlossene bereits gespeicherte Familien |",
        "|---|---:|---|",
        f"| `{source_paths[0].resolve().relative_to(ROOT).as_posix()}` | {source_counts[0]} | `rf_05` |",
        f"| `{source_paths[1].resolve().relative_to(ROOT).as_posix()}` | {source_counts[1]} | `rf_05` |",
        f"| `{source_paths[2].resolve().relative_to(ROOT).as_posix()}` | {source_counts[2]} | `rf_05;rf_08` |",
        "",
        "## Volumenidentitäten vor und nach der Balance",
        "",
        "| Familie | vorher Beobachtungen/Quellen | neu | nachher Beobachtungen/Quellen | Δ Ereignisanteil-Mittel | Ereignisanteil-Perzentil |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for role_family in ROLE_FAMILIES:
        old = previous[role_family]
        new = current[role_family]
        lines.append(
            f"| `{role_family}` | {old['observations']}/{old['evidence_sources']} | "
            f"{new_by_family[role_family]} | "
            f"{new['observations']}/{new['evidence_sources']} | "
            f"{_fmt(new['mean_delta_event_share'], 4)} | "
            f"{_fmt(new['mean_percentile_event_share'])} |"
        )
    lines.extend(
        [
            "",
            "## Organische Bedeutung",
            "",
            "Alle acht Volumenidentitäten besitzen nun dieselbe Beobachtungs- und Quellentiefe. Positive, negative und driftende Ereignisrichtungen werden als numerische Erfahrung nebeneinander bewahrt. Die Balance erzeugt weder eine Rangordnung noch eine feste Familieneigenschaft.",
            "",
            "Die 100 neuen Beobachtungen erweitern vorhandene Identitäten; sie erzeugen keine neue Antwortidentität. Gleiche Weltkontexte bleiben unterscheidbar über Evidenzherkunft und Beobachtungssymbol.",
            "",
            "## Technische Grenze",
            "",
            "Die Memory speichert keine Richtungsklasse, Replikationsmarke, Bedeutung oder Vorhersage. `read_by_mini_dio`, `influences_action`, `is_gate`, `is_motoric`, `is_entry_signal` und `is_direction_signal` bleiben `0`. Die lokale JSON-Memory bleibt ungetrackt.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Balanciert passive Volumen-Antwort-Evidenz über alle Familien."
    )
    parser.add_argument("--family-memory", default=str(DEFAULT_FAMILY_MEMORY))
    parser.add_argument("--memory-2087", default=str(DEFAULT_MEMORY_2087))
    parser.add_argument("--summary-2089", default=str(DEFAULT_SUMMARY_2089))
    parser.add_argument("--summary-2090", default=str(DEFAULT_SUMMARY_2090))
    parser.add_argument("--out-prefix", default=str(DEFAULT_OUT_PREFIX))
    parser.add_argument("--out-json", default=str(DEFAULT_OUT_JSON))
    args = parser.parse_args()

    family_memory = _resolve(args.family_memory)
    memory_2087 = _resolve(args.memory_2087)
    summary_2089 = _resolve(args.summary_2089)
    summary_2090 = _resolve(args.summary_2090)
    out_prefix = _resolve(args.out_prefix)
    out_json = _resolve(args.out_json)

    source_rows = _filter_sources(summary_2089, summary_2090)
    source_paths = [
        _source_path(out_prefix, "2083_5m"),
        _source_path(out_prefix, "2086_5m"),
        _source_path(out_prefix, "2081_30m"),
    ]
    expected_counts = [35, 35, 30]
    for path, rows, expected in zip(source_paths, source_rows, expected_counts):
        if len(rows) != expected:
            raise ValueError(
                f"{path.name}: erwartet {expected} Quellzeilen, gefunden {len(rows)}"
            )
        _write_csv(path, rows)

    before_sources = [
        *_base_sources(),
        _new_source(BEFUNDE / "2086_RF05_VOLUME_ORIENTIERUNGS_HOLDOUT.summary.csv"),
    ]
    after_sources = [
        *before_sources,
        *_additional_sources(*source_paths),
    ]
    before = MCMRoleFamilyResponseMemory.from_sources(
        family_memory, before_sources, ROOT
    )
    after = MCMRoleFamilyResponseMemory.from_sources(
        family_memory, after_sources, ROOT
    )
    snapshot_2087 = _load_csv(memory_2087)
    reconstructed_2087 = [
        {key: str(row.get(key, "")) for key in snapshot_2087[0]}
        for row in before.to_rows()
    ]
    if reconstructed_2087 != snapshot_2087:
        raise ValueError("Rekonstruierte 2087-Memory weicht vom Snapshot ab")
    errors = after.validate()
    if errors:
        raise ValueError(";".join(errors))
    reversed_memory = MCMRoleFamilyResponseMemory.from_sources(
        family_memory, list(reversed(after_sources)), ROOT
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
    if len(new_observations) != 100:
        raise ValueError(
            f"Erwartet wurden 100 neue Beobachtungen, gefunden {len(new_observations)}"
        )
    if after.quality_profile()["response_identities"] != 32:
        raise ValueError("Die Reifung hat die Zahl der Antwortidentitäten verändert")

    before_aggregate = _aggregate(before.to_rows())
    after_aggregate = _aggregate(after.to_rows())
    volume_after = _volume_rows(after_aggregate)
    for role_family in ROLE_FAMILIES:
        row = volume_after[role_family]
        if int(row["observations"]) != 21 or int(row["evidence_sources"]) != 5:
            raise ValueError(
                f"{role_family}: Volumen-Evidenz nicht bei 21/5: "
                f"{row['observations']}/{row['evidence_sources']}"
            )

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
        source_paths,
        expected_counts,
        order_stable,
        duplicate_rejected,
    )

    print(f"records_before={len(before.records)}")
    print(f"records_after={len(after.records)}")
    print(f"new_observations={len(new_observations)}")
    print(f"response_identities={after.quality_profile()['response_identities']}")
    print(f"evidence_sources={after.quality_profile()['evidence_sources']}")
    print(f"validation_errors={len(errors)}")
    print(f"order_stable={order_stable}")
    print(f"duplicate_rejected={duplicate_rejected}")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
