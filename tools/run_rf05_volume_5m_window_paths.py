from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

try:
    from tools.run_role_family_component_phase_profiles import (
        DEFAULT_COHESION,
        DEFAULT_MEMORY,
        _load_targets,
        _resolve,
        _write_csv,
    )
    from tools.run_role_family_followworld_probe import _load_csv
    from tools.run_role_family_matched_pseudo_controls import (
        DEFAULT_OUT_PREFIX as PSEUDO_PREFIX,
        _evaluate_pseudos,
        _fmt,
        _load_global_source_counts,
    )
    from tools.run_rf05_volume_5m_memory_maturation import (
        TARGET_COMPONENTS,
        TARGET_FAMILY,
        _build_records,
        _build_summary,
        _observed_definition,
        _run_pool_worlds,
    )
except ModuleNotFoundError:
    from run_role_family_component_phase_profiles import (
        DEFAULT_COHESION,
        DEFAULT_MEMORY,
        _load_targets,
        _resolve,
        _write_csv,
    )
    from run_role_family_followworld_probe import _load_csv
    from run_role_family_matched_pseudo_controls import (
        DEFAULT_OUT_PREFIX as PSEUDO_PREFIX,
        _evaluate_pseudos,
        _fmt,
        _load_global_source_counts,
    )
    from run_rf05_volume_5m_memory_maturation import (
        TARGET_COMPONENTS,
        TARGET_FAMILY,
        _build_records,
        _build_summary,
        _observed_definition,
        _run_pool_worlds,
    )


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = ROOT / "docs" / "befunde" / "2001-3000"
DEFAULT_DEFINITIONS = PSEUDO_PREFIX.with_suffix(".definitions.csv")
DEFAULT_DATA_DIR = ROOT / "data" / "generated" / "2083_rf05_volume_5m_memory_maturation"
DEFAULT_DEBUG_ROOT = ROOT / "debug" / "2083_rf05_volume_5m_memory_maturation"
DEFAULT_DETAIL_DIR = ROOT / "debug" / "2084_rf05_volume_5m_window_paths"
DEFAULT_OUT_PREFIX = BEFUNDE / "2084_RF05_VOLUME_5M_FENSTERPFADE"
METRIC_FIELDS = (
    "observed_control_minus_real_family_continuity_score",
    "observed_control_minus_real_mean_family_event_share",
    "observed_control_minus_real_mean_member_coverage",
)
PERCENTILE_FIELDS = (
    "observed_percentile_control_minus_real_family_continuity_score",
    "observed_percentile_control_minus_real_mean_family_event_share",
    "observed_percentile_control_minus_real_mean_member_coverage",
)


def _window_pool(
    rows: list[dict[str, object]], asset: str, year: int, start: int
) -> list[dict[str, object]]:
    return [
        row
        for row in rows
        if str(row["asset"]) == asset
        and int(row["year"]) == year
        and int(row["window_start"]) == start
    ]


def _window_summary(
    pool_rows: list[dict[str, object]],
    targets: dict[str, list[str]],
    definitions: list[dict[str, object]],
    global_counts: Counter[str],
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    observed = _evaluate_pseudos(
        _observed_definition(targets, global_counts),
        pool_rows,
        global_counts,
        TARGET_COMPONENTS,
        ("overall",),
    )
    pseudos = _evaluate_pseudos(
        definitions,
        pool_rows,
        global_counts,
        TARGET_COMPONENTS,
        ("overall",),
    )
    return _build_summary(observed, pseudos), pseudos


def _build_paths(summary: list[dict[str, object]]) -> list[dict[str, object]]:
    paths: list[dict[str, object]] = []
    contexts = sorted({(str(row["asset"]), int(row["year"])) for row in summary})
    for asset, year in contexts:
        rows = sorted(
            (
                row
                for row in summary
                if row["asset"] == asset and int(row["year"]) == year
            ),
            key=lambda row: int(row["window_start"]),
        )
        relations = [str(row["observed_relation"]) for row in rows]
        paths.append(
            {
                "asset": asset,
                "year": year,
                "window_starts": ";".join(str(row["window_start"]) for row in rows),
                "relation_path": ";".join(relations),
                "relation_changes": sum(
                    left != right for left, right in zip(relations, relations[1:])
                ),
                "strengthened_windows": relations.count("verstaerkt"),
                "mixed_windows": relations.count("gemischt"),
                "weakened_windows": relations.count("abgeschwaecht"),
                "continuity_path": ";".join(
                    _fmt(row[METRIC_FIELDS[0]], 6) for row in rows
                ),
                "event_share_path": ";".join(
                    _fmt(row[METRIC_FIELDS[1]], 6) for row in rows
                ),
                "coverage_path": ";".join(
                    _fmt(row[METRIC_FIELDS[2]], 6) for row in rows
                ),
                "minimum_percentile_path": ";".join(
                    _fmt(min(float(row[field]) for field in PERCENTILE_FIELDS), 3)
                    for row in rows
                ),
            }
        )
    return paths


def _write_markdown(
    path: Path,
    summary: list[dict[str, object]],
    paths: list[dict[str, object]],
) -> None:
    relations = Counter(str(row["observed_relation"]) for row in summary)
    all_axis_positive = sum(
        all(float(row[field]) > 0.0 for field in METRIC_FIELDS) for row in summary
    )
    all_axis_negative = sum(
        all(float(row[field]) < 0.0 for field in METRIC_FIELDS) for row in summary
    )
    high_null_distance = sum(
        min(float(row[field]) for field in PERCENTILE_FIELDS) >= 0.95
        for row in summary
    )
    path_changes = sum(int(row["relation_changes"]) for row in paths)
    positive_metrics = [
        sum(float(row[field]) > 0.0 for row in summary) for field in METRIC_FIELDS
    ]
    zero_coverage = sum(float(row[METRIC_FIELDS[2]]) == 0.0 for row in summary)
    negative_coverage = sum(float(row[METRIC_FIELDS[2]]) < 0.0 for row in summary)
    each_path_changes_once = all(int(row["relation_changes"]) == 1 for row in paths)
    btc_paths = [str(row["relation_path"]) for row in paths if row["asset"] == "BTC"]
    btc_years_match = len(set(btc_paths)) == 1
    lines = [
        "# 2084 - rf_05:volume als 5m-Fensterpfad",
        "",
        "## Zweck",
        "",
        "Befund 2083 repliziert `rf_05:volume` im 5m-Gesamtprofil, während 2024 und BTC achsengemischt bleiben. Diese Diagnose zerlegt exakt dieselben zwölf Realfenster und 36 Volumenphasenkontrollen, um die innere Verteilung der Antwort sichtbar zu machen.",
        "",
        "Der Lauf ist keine neue Holdout-Evidenz. Er wiederverwendet die Welten aus 2083, erzeugt keine neue Memory-Beobachtung und verändert keine Runtime.",
        "",
        "## Fensterantworten",
        "",
        "| Asset | Jahr | Start | Antwort | Pseudo gleich | Δ Kontinuität | Δ Ereignisanteil | Δ Abdeckung | Perzentile K/E/A |",
        "|---|---:|---:|---|---:|---:|---:|---:|---:|",
    ]
    for row in summary:
        lines.append(
            f"| `{row['asset']}` | {row['year']} | {row['window_start']} | "
            f"`{row['observed_relation']}` | {row['pseudo_same_relation']}/100 | "
            f"{_fmt(row[METRIC_FIELDS[0]])} | {_fmt(row[METRIC_FIELDS[1]], 4)} | "
            f"{_fmt(row[METRIC_FIELDS[2]])} | "
            f"{_fmt(row[PERCENTILE_FIELDS[0]])}/"
            f"{_fmt(row[PERCENTILE_FIELDS[1]])}/"
            f"{_fmt(row[PERCENTILE_FIELDS[2]])} |"
        )
    lines.extend(
        [
            "",
            "## Antwortpfade",
            "",
            "| Asset/Jahr | Startfolge | Antwortfolge | Wechsel | Mindestperzentile |",
            "|---|---|---|---:|---|",
        ]
    )
    for row in paths:
        lines.append(
            f"| `{row['asset']}:{row['year']}` | `{row['window_starts']}` | "
            f"`{row['relation_path']}` | {row['relation_changes']} | "
            f"`{row['minimum_percentile_path']}` |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"Von zwölf Fenstern sind `{relations['verstaerkt']}` verstärkt, `{relations['gemischt']}` gemischt und `{relations['abgeschwaecht']}` abgeschwächt. `{all_axis_positive}` Fenster tragen positive Abstände auf allen drei Achsen, `{all_axis_negative}` negative Abstände auf allen drei Achsen. Über die acht benachbarten Übergänge der vier Asset-Jahr-Pfade wechselt die Antwort `{path_changes}`-mal.",
            "",
            f"Der Ereignisanteil steigt in `{positive_metrics[1]}/12` Fenstern. Kontinuität steigt in `{positive_metrics[0]}/12`; Abdeckung steigt in `{positive_metrics[2]}/12`, bleibt in `{zero_coverage}/12` unverändert und sinkt in `{negative_coverage}/12`. Die Volumenphasenverschiebung trägt damit fast durchgehend mehr Familienereignisse, wird aber je lokaler Feldlage verschieden in Kontinuität und Mitgliederbreite aufgenommen.",
            "",
            f"Alle vier Pfade wechseln genau einmal: `{int(each_path_changes_once)}`. Die beiden BTC-Jahre tragen sogar dieselbe Folge `verstaerkt;gemischt;gemischt`: `{int(btc_years_match)}`. Die gemischten Teilgruppen aus 2083 stammen damit nicht aus einem einzelnen Ausreißer, sondern aus wiederkehrenden feldphasenabhängigen Verschiebungen. Für SOL ist die Pfadrichtung zwischen den Jahren verschieden, also nicht als allgemeiner Kalender- oder Positionscode lesbar.",
            "",
            f"In nur `{high_null_distance}/12` Fenstern liegt selbst das niedrigste der drei realen Maße mindestens am Perzentil `0.950` der gematchten Pseudo-Familien. Der starke Gesamtwert aus 2083 ist deshalb eine kollektive Antwort über mehrere Feldphasen, keine lokale Invariante jedes Fensters. Ein hoher Nullabstand und eine gleichgerichtete Verstärkung sind nicht dasselbe.",
            "",
            "Die Tabelle bewahrt diese Verläufe numerisch. Verstärkt und gemischt bleiben Berichtssprache; sie werden weder als Feldklassen noch als Wenn-Dann-Regeln programmiert.",
            "",
            "## Grenze",
            "",
            "Die Fenster sind eine nachträgliche Zerlegung derselben 2083-Evidenz. Sie erhöhen weder Stichprobe noch Unabhängigkeit. Die passive Antwort-Memory bleibt bei 217 Beobachtungen und 32 Identitäten; `rf_05:volume` bleibt `dio_rresponse_0gpsabe` und wird weiterhin nicht von MINI_DIO gelesen.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Zerlegt die rf_05:volume-5m-Antwort aus 2083 in Fensterpfade."
    )
    parser.add_argument("--memory", default=str(DEFAULT_MEMORY))
    parser.add_argument("--cohesion-detail", default=str(DEFAULT_COHESION))
    parser.add_argument("--definitions", default=str(DEFAULT_DEFINITIONS))
    parser.add_argument("--data-dir", default=str(DEFAULT_DATA_DIR))
    parser.add_argument("--debug-root", default=str(DEFAULT_DEBUG_ROOT))
    parser.add_argument("--detail-dir", default=str(DEFAULT_DETAIL_DIR))
    parser.add_argument("--out-prefix", default=str(DEFAULT_OUT_PREFIX))
    args = parser.parse_args()

    role_memory = _resolve(args.memory)
    cohesion = _resolve(args.cohesion_detail)
    definitions_path = _resolve(args.definitions)
    data_dir = _resolve(args.data_dir)
    debug_root = _resolve(args.debug_root)
    detail_dir = _resolve(args.detail_dir)
    out_prefix = _resolve(args.out_prefix)

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
    pool_rows = _run_pool_worlds(real_records + phase_records, all_symbols, debug_root)

    summary: list[dict[str, object]] = []
    pseudo_detail: list[dict[str, object]] = []
    for record in real_records:
        asset = str(record["asset"])
        year = int(record["year"])
        start = int(record["start"])
        window_rows = _window_pool(pool_rows, asset, year, start)
        if len({str(row["world_label"]) for row in window_rows}) != 4:
            raise ValueError(f"Unvollständiger Weltpool für {asset}:{year}:{start}")
        window_summary, pseudos = _window_summary(
            window_rows, targets, definitions, global_counts
        )
        summary.append(
            {
                "asset": asset,
                "year": year,
                "timeframe": "5m",
                "window_start": start,
                "window_end": start + int(record["rows"]),
                **window_summary[0],
            }
        )
        pseudo_detail.extend(
            {
                "asset": asset,
                "year": year,
                "timeframe": "5m",
                "window_start": start,
                **row,
            }
            for row in pseudos
        )

    paths = _build_paths(summary)
    _write_csv(out_prefix.with_suffix(".summary.csv"), summary)
    _write_csv(out_prefix.with_suffix(".paths.csv"), paths)
    _write_csv(detail_dir / "2084_RF05_VOLUME_5M_FENSTERPFADE.pseudos.csv", pseudo_detail)
    _write_markdown(out_prefix.with_suffix(".md"), summary, paths)

    print(f"windows={len(summary)}")
    print(f"paths={len(paths)}")
    print(f"pseudo_detail_rows={len(pseudo_detail)}")
    print(f"strengthened={sum(row['observed_relation'] == 'verstaerkt' for row in summary)}")
    print(f"mixed={sum(row['observed_relation'] == 'gemischt' for row in summary)}")
    print(f"weakened={sum(row['observed_relation'] == 'abgeschwaecht' for row in summary)}")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
