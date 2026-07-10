from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
from statistics import mean, median

try:
    from tools.create_csv_slice import create_slice
    from tools.report_role_family_response_memory import _aggregate, _sources
    from tools.run_role_family_component_phase_profiles import (
        DEFAULT_COHESION,
        DEFAULT_MEMORY,
        _load_targets,
        _resolve,
        _write_csv,
    )
    from tools.run_role_family_followworld_probe import (
        _build_member_rows,
        _load_csv,
        _run_mini,
        _safe_float,
    )
    from tools.run_role_family_matched_pseudo_controls import (
        DEFAULT_OUT_PREFIX as PSEUDO_PREFIX,
        _empirical_percentile,
        _evaluate_pseudos,
        _fmt,
        _load_global_source_counts,
    )
    from tools.run_role_family_real_null_contrast import _relative, _write_control_archive
    from tools.run_rf05_component_phase_controls import ROWS, _phase_worlds
except ModuleNotFoundError:
    from create_csv_slice import create_slice
    from report_role_family_response_memory import _aggregate, _sources
    from run_role_family_component_phase_profiles import (
        DEFAULT_COHESION,
        DEFAULT_MEMORY,
        _load_targets,
        _resolve,
        _write_csv,
    )
    from run_role_family_followworld_probe import (
        _build_member_rows,
        _load_csv,
        _run_mini,
        _safe_float,
    )
    from run_role_family_matched_pseudo_controls import (
        DEFAULT_OUT_PREFIX as PSEUDO_PREFIX,
        _empirical_percentile,
        _evaluate_pseudos,
        _fmt,
        _load_global_source_counts,
    )
    from run_role_family_real_null_contrast import _relative, _write_control_archive
    from run_rf05_component_phase_controls import ROWS, _phase_worlds

from mini_dio.mcm_role_family_response_memory import (
    MCMRoleFamilyResponseMemory,
    ResponseEvidenceSource,
)


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = ROOT / "docs" / "befunde" / "2001-3000"
DEFAULT_DEFINITIONS = PSEUDO_PREFIX.with_suffix(".definitions.csv")
DEFAULT_DATA_DIR = ROOT / "data" / "generated" / "2083_rf05_volume_5m_memory_maturation"
DEFAULT_ARCHIVE = ROOT / "data" / "2083_rf05_volume_5m_memory_maturation.zip"
DEFAULT_DEBUG_ROOT = ROOT / "debug" / "2083_rf05_volume_5m_memory_maturation"
DEFAULT_OUT_PREFIX = BEFUNDE / "2083_RF05_VOLUME_5M_MEMORY_REIFUNG"
DEFAULT_FAMILY_MEMORY = BEFUNDE / "2069_PASSIVE_ROLLENFAMILIEN_MEMORY.csv"
DEFAULT_MEMORY_JSON = ROOT / "memory" / "passive_role_family_response_memory.json"
TARGET_FAMILY = "rf_05"
TARGET_COMPONENTS = ("volume",)
GROUPS = ("overall", "year:2024", "year:2025", "asset:BTC", "asset:SOL")
PRIMARY_METRICS = (
    "family_continuity_score",
    "mean_family_event_share",
    "mean_member_coverage",
)
SPECS = tuple(
    {
        "asset": asset,
        "year": year,
        "source": ROOT / "data" / f"1-12_{year}_5m_{asset}USDT.csv",
        "starts": (0, 36000, 72000),
    }
    for year in (2024, 2025)
    for asset in ("BTC", "SOL")
)


def _ensure_slice(source: Path, target: Path, start: int) -> Path:
    if target.exists() and len(_load_csv(target)) == ROWS:
        return target
    result = create_slice(source, target, start=start, rows=ROWS)
    if int(result.get("rows_written", 0)) != ROWS:
        raise ValueError(f"{source} schrieb {result.get('rows_written')} statt {ROWS} Zeilen")
    return target


def _build_records(data_dir: Path) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    real_records: list[dict[str, object]] = []
    phase_records: list[dict[str, object]] = []
    for spec in SPECS:
        source = Path(str(spec["source"]))
        if not source.exists():
            raise FileNotFoundError(source)
        for start_value in spec["starts"]:
            start = int(start_value)
            asset = str(spec["asset"])
            year = int(spec["year"])
            real_path = _ensure_slice(
                source,
                data_dir / f"holdout_2083_{asset.lower()}_{year}_5m_start{start}_rows{ROWS}.csv",
                start,
            )
            real: dict[str, object] = {
                "asset": asset,
                "timeframe": "5m",
                "year": year,
                "start": start,
                "rows": ROWS,
                "kind": "real",
                "seed": "",
                "source": source,
                "path": real_path,
            }
            real_records.append(real)
            paths = _phase_worlds(
                real_path,
                data_dir / f"control_2083_{asset.lower()}_{year}_5m_start{start}",
                TARGET_COMPONENTS,
            )
            for kind, path in paths.items():
                lag = int(kind.rsplit("_", 1)[1])
                phase_records.append({**real, "kind": kind, "seed": lag, "path": path})
    return real_records, phase_records


def _run_pool_worlds(
    records: list[dict[str, object]],
    symbols: list[str],
    debug_root: Path,
) -> list[dict[str, object]]:
    member_rows: list[dict[str, object]] = []
    for record in records:
        asset = str(record["asset"])
        year = int(record["year"])
        kind = str(record["kind"])
        start = int(record["start"])
        rows = int(record["rows"])
        world_label = f"{kind}_{asset.lower()}_{year}_5m_{start}_{start + rows}"
        path = Path(str(record["path"]))
        run_dir = _run_mini(path, debug_root / world_label, world_label)
        episodes = _load_csv(run_dir / "episodes.csv")
        world = {
            "asset": asset,
            "timeframe": "5m",
            "year": year,
            "world_kind": kind,
            "window_start": start,
            "window_end": start + rows,
            "world_label": world_label,
            "source_path": _relative(Path(str(record["source"]))),
            "data_path": _relative(path),
            "world_events": len(episodes),
        }
        member_rows.extend(_build_member_rows(world, episodes, {"pool": symbols}))
    return member_rows


def _observed_definition(
    targets: dict[str, list[str]],
    global_counts: Counter[str],
) -> list[dict[str, object]]:
    members = sorted(targets[TARGET_FAMILY])
    return [
        {
            "role_family": TARGET_FAMILY,
            "pseudo_index": 0,
            "pseudo_id": f"{TARGET_FAMILY}_observed",
            "members": ";".join(members),
            "member_count": len(members),
            "disjoint_from_real": 0,
            "match_distance": 0.0,
            "real_source_events": sum(global_counts[symbol] for symbol in members),
            "pseudo_source_events": sum(global_counts[symbol] for symbol in members),
            "source_event_ratio": 1.0,
        }
    ]


def _build_summary(
    observed_rows: list[dict[str, object]],
    pseudo_rows: list[dict[str, object]],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for observed in observed_rows:
        group = str(observed["group"])
        pseudos = [
            row
            for row in pseudo_rows
            if row["group"] == group
            and row["role_family"] == TARGET_FAMILY
            and row["component"] == "volume"
        ]
        row: dict[str, object] = {
            "group": group,
            "role_family": TARGET_FAMILY,
            "component": "volume",
            "primary_axis": 1,
            "expected_relation": "verstaerkt",
            "observed_relation": observed["relation"],
            "expected_relation_match": int(observed["relation"] == "verstaerkt"),
            "pseudo_same_relation": sum(
                item["relation"] == observed["relation"] for item in pseudos
            ),
            "pseudo_families": len(pseudos),
            "mean_match_distance": mean(
                _safe_float(item["match_distance"]) for item in pseudos
            ),
            "median_source_event_ratio": median(
                _safe_float(item["source_event_ratio"]) for item in pseudos
            ),
        }
        for metric in PRIMARY_METRICS:
            field = f"control_minus_real_{metric}"
            observed_value = _safe_float(observed[field])
            values = [_safe_float(item[field]) for item in pseudos]
            row[f"observed_{field}"] = observed_value
            row[f"pseudo_mean_{field}"] = mean(values)
            row[f"observed_percentile_{field}"] = _empirical_percentile(
                values, observed_value
            )
        rows.append(row)
    return rows


def _build_memory(
    family_memory: Path,
    summary_path: Path,
    out_prefix: Path,
    out_json: Path,
) -> tuple[MCMRoleFamilyResponseMemory, list[dict[str, object]], bool, bool]:
    sources = _sources(
        BEFUNDE / "2079_ROLLENFAMILIEN_GEMATCHE_PSEUDOFAMILIEN.summary.csv",
        BEFUNDE / "2080_RF08_SIGN_GEMATCHTER_CROSSYEAR_KONTRAST.summary.csv",
        BEFUNDE / "2081_RF08_SIGN_RF05_VOLUME_30M_HOLDOUT.summary.csv",
    )
    sources.append(
        ResponseEvidenceSource(
            evidence_id="2083_2024_2025_5m_rf05_volume_holdout",
            summary_path=summary_path,
            world_year_profile="2024;2025",
            timeframe_profile="5m",
            asset_profile="BTC;SOL",
            overall_real_worlds=12,
            subgroup_real_worlds=6,
        )
    )
    memory = MCMRoleFamilyResponseMemory.from_sources(family_memory, sources, ROOT)
    errors = memory.validate()
    if errors:
        raise ValueError(";".join(errors))
    reversed_memory = MCMRoleFamilyResponseMemory.from_sources(
        family_memory, list(reversed(sources)), ROOT
    )
    order_stable = memory.to_rows() == reversed_memory.to_rows()
    if not order_stable:
        raise ValueError("Memory hängt von der Reihenfolge der Evidenzquellen ab")
    records_before_duplicate = len(memory.records)
    duplicate_rejected = not memory.append(memory.records[0])
    duplicate_rejected = duplicate_rejected and len(memory.records) == records_before_duplicate
    if not duplicate_rejected:
        raise ValueError("Doppelte Beobachtung wurde in die Memory aufgenommen")
    memory.write_csv(out_prefix.with_suffix(".memory.csv"))
    memory.write_json(out_json)
    aggregate = _aggregate(memory.to_rows())
    _write_csv(out_prefix.with_suffix(".memory.summary.csv"), aggregate)
    return memory, aggregate, order_stable, duplicate_rejected


def _write_markdown(
    path: Path,
    summary: list[dict[str, object]],
    archive: Path,
    memory: MCMRoleFamilyResponseMemory,
    aggregate: list[dict[str, object]],
    order_stable: bool,
    duplicate_rejected: bool,
) -> None:
    indexed = {str(row["group"]): row for row in summary}
    overall = indexed["overall"]
    rf05_memory = next(
        row
        for row in aggregate
        if row["role_family"] == TARGET_FAMILY and row["component"] == "volume"
    )
    profile = memory.quality_profile()
    expected_matches = sum(int(row["expected_relation_match"]) for row in summary)
    lines = [
        "# 2083 - rf_05:volume im 5m-Holdout und Reifung der passiven Memory",
        "",
        "## Zweck",
        "",
        "Befund 2081 trug auf 30m. Dieser Lauf prüft die vorab festgelegte Volumen-Phasenantwort von `rf_05` auf der bisher ungenutzten 5m-Zeitebene und hängt das Ergebnis anschließend als neue passive Erfahrung an dieselbe Antwortidentität.",
        "",
        "## Vorab festgelegtes Design",
        "",
        "- Datenjahre `2024` und `2025`",
        "- Assets `BTC` und `SOL`",
        "- ausschließlich die bisher ungenutzte Zeitebene `5m`",
        "- Startpunkte `0`, `36000`, `72000` je Asset und Jahr",
        "- zwölf nicht überlappende Realwelten mit je `1000` Beobachtungen",
        "- ausschließlich die Komponente `volume`",
        "- feste Offsets `17`, `83`, `251`",
        "- `36` gezielte Phasenkontrollen",
        "- exakt dieselben 100 für `rf_05` gematchten Pseudo-Familien wie ab Befund 2079",
        "- vorab erwartete Antwort: `rf_05:volume = verstaerkt`",
        f"- Weltarchiv: `{_relative(archive)}`",
        "- keine neue Klasse, keine Handlung, kein Gate und keine Richtung",
        "",
        "## Holdout-Ergebnis",
        "",
        "| Gruppe | erwartet/beobachtet | Pseudo gleich | Δ Kontinuität | Δ Ereignisanteil | Δ Abdeckung | Perzentile K/E/A |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in summary:
        lines.append(
            f"| `{row['group']}` | `{row['expected_relation']}/{row['observed_relation']}` | "
            f"{row['pseudo_same_relation']}/{row['pseudo_families']} | "
            f"{_fmt(row['observed_control_minus_real_family_continuity_score'])} | "
            f"{_fmt(row['observed_control_minus_real_mean_family_event_share'], 4)} | "
            f"{_fmt(row['observed_control_minus_real_mean_member_coverage'])} | "
            f"{_fmt(row['observed_percentile_control_minus_real_family_continuity_score'])}/"
            f"{_fmt(row['observed_percentile_control_minus_real_mean_family_event_share'])}/"
            f"{_fmt(row['observed_percentile_control_minus_real_mean_member_coverage'])} |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"Im Gesamtprofil repliziert die vorab erwartete Verstärkung. Insgesamt tragen `{overall['pseudo_same_relation']}/100` gematchte Pseudo-Familien dieselbe Antwort; die drei beobachteten Abstände liegen bei den Perzentilen `{_fmt(overall['observed_percentile_control_minus_real_family_continuity_score'])}`, `{_fmt(overall['observed_percentile_control_minus_real_mean_family_event_share'])}` und `{_fmt(overall['observed_percentile_control_minus_real_mean_member_coverage'])}`.",
            "",
            f"Die Antwort ist jedoch nicht über alle Teilkontexte geschlossen: `{expected_matches}/5` Gruppen sind verstärkt. `year:2024` und `asset:BTC` sind gemischt, weil Kontinuität und Abdeckung jeweils leicht sinken, während der Ereignisanteil steigt. Dass ihre Maße gegenüber den Pseudo-Familien dennoch bei hohen Perzentilen liegen, zeigt einen familienbezogenen Abstand, aber keine starre gleichgerichtete Signatur.",
            "",
            "Der Lauf prüft keine feste Volumenbedeutung. Er verschiebt nur die Volumenphase relativ zur übrigen Welt. Belegt ist eine reproduzierbare, aber kontextplastische Familienantwort gegenüber gelöster Volumenphase, keine Handelsrichtung, keine Kausalität und keine bevorzugte Aktion.",
            "",
            "## Reifung der passiven Antwort-Memory",
            "",
            f"- Beobachtungen vorher/nachher: `212/{profile['records']}`",
            f"- stabile Antwortidentitäten vorher/nachher: `32/{profile['response_identities']}`",
            f"- eindeutige Beobachtungssymbole: `{profile['observation_identities']}`",
            f"- Evidenzquellen: `{profile['evidence_sources']}`",
            f"- `rf_05:volume` Antwortsymbol: `{rf05_memory['response_symbol']}`",
            f"- `rf_05:volume` Beobachtungen vorher/nachher: `11/{rf05_memory['observations']}`",
            f"- quellenreihenfolgenstabil: `{int(order_stable)}`",
            f"- doppelte Beobachtung abgewiesen: `{int(duplicate_rejected)}`",
            f"- passiv/handlungswirksam: `{profile['passive_only']}/{profile['influences_action']}`",
            "",
            "Die neue Evidenz erzeugt fünf neue Beobachtungssymbole für fünf Kontexte. Die Familien-Komponenten-Identität bleibt stabil. Das ist Reifung durch zusätzliche Erfahrung, keine fest programmierte Sonderregel für `rf_05`.",
            "",
            "## Grenze",
            "",
            "Auch nach dieser Reifung wird die Antwort-Memory nicht von MINI_DIO gelesen. Sie besitzt keine Antwortklasse, Bestätigung, Bedeutung oder Vorhersage. Der Lauf bleibt auf BTC/SOL, Marktzeitreihen, 1000er-Fenster und dieselbe zirkuläre Phasenoperation begrenzt.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prüft rf_05:volume auf 5m und reift die passive Antwort-Memory."
    )
    parser.add_argument("--memory", default=str(DEFAULT_MEMORY))
    parser.add_argument("--family-memory", default=str(DEFAULT_FAMILY_MEMORY))
    parser.add_argument("--cohesion-detail", default=str(DEFAULT_COHESION))
    parser.add_argument("--definitions", default=str(DEFAULT_DEFINITIONS))
    parser.add_argument("--data-dir", default=str(DEFAULT_DATA_DIR))
    parser.add_argument("--archive", default=str(DEFAULT_ARCHIVE))
    parser.add_argument("--debug-root", default=str(DEFAULT_DEBUG_ROOT))
    parser.add_argument("--out-prefix", default=str(DEFAULT_OUT_PREFIX))
    parser.add_argument("--memory-json", default=str(DEFAULT_MEMORY_JSON))
    args = parser.parse_args()

    role_memory = _resolve(args.memory)
    family_memory = _resolve(args.family_memory)
    cohesion = _resolve(args.cohesion_detail)
    definitions_path = _resolve(args.definitions)
    data_dir = _resolve(args.data_dir)
    archive = _resolve(args.archive)
    debug_root = _resolve(args.debug_root)
    out_prefix = _resolve(args.out_prefix)
    memory_json = _resolve(args.memory_json)

    targets = _load_targets(
        role_memory,
        ["rf_05", "rf_06", "rf_07", "rf_08", "rf_10", "rf_13", "rf_17", "rf_21"],
    )
    all_symbols = sorted({symbol for members in targets.values() for symbol in members})
    global_counts = _load_global_source_counts(cohesion, set(all_symbols))
    definitions = [
        row
        for row in _load_csv(definitions_path)
        if row["role_family"] == TARGET_FAMILY
    ]
    real_records, phase_records = _build_records(data_dir)
    _write_control_archive(archive, phase_records)
    pool_rows = _run_pool_worlds(real_records + phase_records, all_symbols, debug_root)

    observed_rows = _evaluate_pseudos(
        _observed_definition(targets, global_counts),
        pool_rows,
        global_counts,
        TARGET_COMPONENTS,
        GROUPS,
    )
    pseudo_rows = _evaluate_pseudos(
        definitions,
        pool_rows,
        global_counts,
        TARGET_COMPONENTS,
        GROUPS,
    )
    summary = _build_summary(observed_rows, pseudo_rows)
    summary_path = out_prefix.with_suffix(".summary.csv")
    _write_csv(out_prefix.with_suffix(".observed.csv"), observed_rows)
    _write_csv(out_prefix.with_suffix(".pseudos.csv"), pseudo_rows)
    _write_csv(summary_path, summary)

    memory, aggregate, order_stable, duplicate_rejected = _build_memory(
        family_memory, summary_path, out_prefix, memory_json
    )
    _write_markdown(
        out_prefix.with_suffix(".md"),
        summary,
        archive,
        memory,
        aggregate,
        order_stable,
        duplicate_rejected,
    )

    rf05_memory = next(
        row
        for row in aggregate
        if row["role_family"] == TARGET_FAMILY and row["component"] == "volume"
    )
    print(f"real_worlds={len(real_records)}")
    print(f"phase_worlds={len(phase_records)}")
    print(f"pool_member_rows={len(pool_rows)}")
    print(f"observed_rows={len(observed_rows)}")
    print(f"pseudo_rows={len(pseudo_rows)}")
    print(f"summary_rows={len(summary)}")
    print(f"memory_records={len(memory.records)}")
    print(f"response_identities={memory.quality_profile()['response_identities']}")
    print(f"rf05_volume_response_symbol={rf05_memory['response_symbol']}")
    print(f"rf05_volume_observations={rf05_memory['observations']}")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
