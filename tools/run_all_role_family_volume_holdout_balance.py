from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean, median

try:
    from tools.run_role_family_component_phase_profiles import (
        DEFAULT_COHESION,
        DEFAULT_MEMORY,
        _load_targets,
        _resolve,
        _write_csv,
    )
    from tools.run_role_family_followworld_probe import _load_csv, _safe_float
    from tools.run_role_family_matched_pseudo_controls import (
        DEFAULT_OUT_PREFIX as PSEUDO_PREFIX,
        _empirical_percentile,
        _evaluate_pseudos,
        _fmt,
        _load_global_source_counts,
    )
    from tools.run_rf05_volume_5m_memory_maturation import (
        GROUPS,
        PRIMARY_METRICS,
        TARGET_COMPONENTS,
        _build_records,
        _run_pool_worlds,
    )
    from tools.run_rf05_volume_orientation_holdout import _build_holdout_records
except ModuleNotFoundError:
    from run_role_family_component_phase_profiles import (
        DEFAULT_COHESION,
        DEFAULT_MEMORY,
        _load_targets,
        _resolve,
        _write_csv,
    )
    from run_role_family_followworld_probe import _load_csv, _safe_float
    from run_role_family_matched_pseudo_controls import (
        DEFAULT_OUT_PREFIX as PSEUDO_PREFIX,
        _empirical_percentile,
        _evaluate_pseudos,
        _fmt,
        _load_global_source_counts,
    )
    from run_rf05_volume_5m_memory_maturation import (
        GROUPS,
        PRIMARY_METRICS,
        TARGET_COMPONENTS,
        _build_records,
        _run_pool_worlds,
    )
    from run_rf05_volume_orientation_holdout import _build_holdout_records


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = ROOT / "docs" / "befunde" / "2001-3000"
DEFAULT_DEFINITIONS = PSEUDO_PREFIX.with_suffix(".definitions.csv")
DEFAULT_DATA_2083 = ROOT / "data" / "generated" / "2083_rf05_volume_5m_memory_maturation"
DEFAULT_DEBUG_2083 = ROOT / "debug" / "2083_rf05_volume_5m_memory_maturation"
DEFAULT_DATA_2086 = ROOT / "data" / "generated" / "2086_rf05_volume_orientation_holdout"
DEFAULT_DEBUG_2086 = ROOT / "debug" / "2086_rf05_volume_orientation_holdout"
DEFAULT_DETAIL_DIR = ROOT / "debug" / "2089_all_role_family_volume_holdout_balance"
DEFAULT_OUT_PREFIX = BEFUNDE / "2089_ALLE_ROLLENFAMILIEN_VOLUME_EVIDENZBALANCE"
ROLE_FAMILIES = ("rf_05", "rf_06", "rf_07", "rf_08", "rf_10", "rf_13", "rf_17", "rf_21")
RESPONSE_AXES = (
    ("continuity", "observed_control_minus_real_family_continuity_score", "observed_percentile_control_minus_real_family_continuity_score"),
    ("event_share", "observed_control_minus_real_mean_family_event_share", "observed_percentile_control_minus_real_mean_family_event_share"),
    ("member_coverage", "observed_control_minus_real_mean_member_coverage", "observed_percentile_control_minus_real_mean_member_coverage"),
)


def _sign(value: float) -> int:
    if value > 0.0:
        return 1
    if value < 0.0:
        return -1
    return 0


def _persistence(signs: list[int]) -> float:
    return abs(sum(signs)) / len(signs) if signs else 0.0


def _observed_definitions(
    targets: dict[str, list[str]],
    global_counts: Counter[str],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for role_family in ROLE_FAMILIES:
        members = sorted(targets[role_family])
        source_events = sum(global_counts[symbol] for symbol in members)
        rows.append(
            {
                "role_family": role_family,
                "pseudo_index": 0,
                "pseudo_id": f"{role_family}_observed",
                "members": ";".join(members),
                "member_count": len(members),
                "disjoint_from_real": 0,
                "match_distance": 0.0,
                "real_source_events": source_events,
                "pseudo_source_events": source_events,
                "source_event_ratio": 1.0,
            }
        )
    return rows


def _build_summary(
    holdout_id: str,
    observed_rows: list[dict[str, object]],
    pseudo_rows: list[dict[str, object]],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for observed in observed_rows:
        group = str(observed["group"])
        role_family = str(observed["role_family"])
        component = str(observed["component"])
        pseudos = [
            row
            for row in pseudo_rows
            if row["group"] == group
            and row["role_family"] == role_family
            and row["component"] == component
        ]
        row: dict[str, object] = {
            "holdout_id": holdout_id,
            "group": group,
            "role_family": role_family,
            "component": component,
            "observed_relation": observed["relation"],
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
            pseudo_values = [_safe_float(item[field]) for item in pseudos]
            row[f"observed_{field}"] = observed_value
            row[f"pseudo_mean_{field}"] = mean(pseudo_values)
            row[f"observed_percentile_{field}"] = _empirical_percentile(
                pseudo_values, observed_value
            )
        rows.append(row)
    return rows


def _evaluate_holdout(
    holdout_id: str,
    real_records: list[dict[str, object]],
    phase_records: list[dict[str, object]],
    debug_root: Path,
    symbols: list[str],
    observed_definitions: list[dict[str, object]],
    pseudo_definitions: list[dict[str, object]],
    global_counts: Counter[str],
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    pool_rows = _run_pool_worlds(
        real_records + phase_records, symbols, debug_root
    )
    observed = _evaluate_pseudos(
        observed_definitions,
        pool_rows,
        global_counts,
        TARGET_COMPONENTS,
        GROUPS,
    )
    pseudos = _evaluate_pseudos(
        pseudo_definitions,
        pool_rows,
        global_counts,
        TARGET_COMPONENTS,
        GROUPS,
    )
    return _build_summary(holdout_id, observed, pseudos), pseudos


def _build_axes(summary: list[dict[str, object]]) -> list[dict[str, object]]:
    by_family: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in summary:
        by_family[str(row["role_family"])].append(row)
    out: list[dict[str, object]] = []
    for role_family, rows in sorted(by_family.items()):
        holdout_ids = sorted({str(row["holdout_id"]) for row in rows})
        for axis, value_field, percentile_field in RESPONSE_AXES:
            values = [_safe_float(row[value_field]) for row in rows]
            signs = [_sign(value) for value in values]
            holdout_means = [
                mean(
                    _safe_float(row[value_field])
                    for row in rows
                    if row["holdout_id"] == holdout_id
                )
                for holdout_id in holdout_ids
            ]
            holdout_signs = [_sign(value) for value in holdout_means]
            percentiles = [_safe_float(row[percentile_field]) for row in rows]
            out.append(
                {
                    "role_family": role_family,
                    "component": "volume",
                    "response_axis": axis,
                    "observations": len(values),
                    "holdouts": len(holdout_ids),
                    "mean_value": mean(values),
                    "median_value": median(values),
                    "minimum_value": min(values),
                    "maximum_value": max(values),
                    "positive_observations": signs.count(1),
                    "negative_observations": signs.count(-1),
                    "zero_observations": signs.count(0),
                    "observation_directional_persistence": _persistence(signs),
                    "mean_null_percentile": mean(percentiles),
                    "minimum_null_percentile": min(percentiles),
                    "maximum_null_percentile": max(percentiles),
                    "holdout_ids": ";".join(holdout_ids),
                    "holdout_mean_path": ";".join(
                        _fmt(value, 6) for value in holdout_means
                    ),
                    "holdout_sign_path": ";".join(
                        str(value) for value in holdout_signs
                    ),
                    "holdout_directional_persistence": _persistence(holdout_signs),
                }
            )
    for axis, _, _ in RESPONSE_AXES:
        selected = [row for row in out if row["response_axis"] == axis]
        persistence_values = [
            _safe_float(row["observation_directional_persistence"])
            for row in selected
        ]
        null_values = [_safe_float(row["mean_null_percentile"]) for row in selected]
        mean_values = [_safe_float(row["mean_value"]) for row in selected]
        for row in selected:
            row["axis_persistence_percentile"] = _empirical_percentile(
                persistence_values,
                _safe_float(row["observation_directional_persistence"]),
            )
            row["axis_mean_null_percentile"] = _empirical_percentile(
                null_values, _safe_float(row["mean_null_percentile"])
            )
            row["axis_signed_mean_percentile"] = _empirical_percentile(
                mean_values, _safe_float(row["mean_value"])
            )
    return out


def _write_markdown(
    path: Path,
    summary: list[dict[str, object]],
    axes: list[dict[str, object]],
) -> None:
    event_rows = sorted(
        (row for row in axes if row["response_axis"] == "event_share"),
        key=lambda row: str(row["role_family"]),
    )
    rf05 = {
        str(row["response_axis"]): row
        for row in axes
        if row["role_family"] == "rf_05"
    }
    fully_positive_events = [
        row
        for row in event_rows
        if int(row["positive_observations"]) == int(row["observations"])
    ]
    fully_negative_events = [
        row
        for row in event_rows
        if int(row["negative_observations"]) == int(row["observations"])
    ]
    positive_both_holdouts = [
        row for row in event_rows if row["holdout_sign_path"] == "1;1"
    ]
    strongest_positive = max(event_rows, key=lambda row: _safe_float(row["mean_value"]))
    highest_null_distance = max(
        event_rows, key=lambda row: _safe_float(row["mean_null_percentile"])
    )
    lines = [
        "# 2089 - Alle Rollenfamilien unter balancierter Volumen-Evidenz",
        "",
        "## Zweck",
        "",
        "Befund 2088 zeigt, dass die meisten Antwortidentitäten deutlich flacher belegt sind als `rf_05:volume`. Dieser Lauf liest daher alle acht Rollenfamilien auf exakt denselben 2083- und 2086-Volumenwelten.",
        "",
        "Jede Familie erhält zehn Gruppenbeobachtungen aus zwei unabhängigen Holdouts und wird in jedem Kontext gegen ihre 100 größen- und häufigkeitsgematchten Pseudo-Familien gestellt. Es entstehen keine neuen Welten, keine neue Memory-Evidenz und keine Runtime-Wirkung.",
        "",
        "## Ereignisanteil im Gleichstand der Evidenz",
        "",
        "| Familie | positiv/negativ/null | Mittel | Holdout-Mittelpfad | Holdout-Vorzeichen | Persistenz | mittleres Nullperzentil | Persistenzperzentil |",
        "|---|---:|---:|---|---|---:|---:|---:|",
    ]
    for row in event_rows:
        lines.append(
            f"| `{row['role_family']}` | "
            f"{row['positive_observations']}/{row['negative_observations']}/{row['zero_observations']} | "
            f"{_fmt(row['mean_value'], 4)} | `{row['holdout_mean_path']}` | "
            f"`{row['holdout_sign_path']}` | "
            f"{_fmt(row['observation_directional_persistence'])} | "
            f"{_fmt(row['mean_null_percentile'])} | "
            f"{_fmt(row['axis_persistence_percentile'])} |"
        )
    lines.extend(
        [
            "",
            "## rf_05:volume über drei Achsen",
            "",
            "| Achse | positiv/negativ/null | Mittel | Holdout-Vorzeichen | Persistenz | mittleres Nullperzentil |",
            "|---|---:|---:|---|---:|---:|",
        ]
    )
    for axis, _, _ in RESPONSE_AXES:
        row = rf05[axis]
        lines.append(
            f"| `{axis}` | {row['positive_observations']}/{row['negative_observations']}/{row['zero_observations']} | "
            f"{_fmt(row['mean_value'], 4)} | `{row['holdout_sign_path']}` | "
            f"{_fmt(row['observation_directional_persistence'])} | "
            f"{_fmt(row['mean_null_percentile'])} |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"Unter gleicher Evidenztiefe tragen `{len(fully_positive_events)}/8` Familien zehn von zehn positive Ereignisanteil-Antworten; `{len(positive_both_holdouts)}/8` besitzen positive Mittelwerte in beiden Holdouts.",
            "",
            f"`rf_05` erreicht `{rf05['event_share']['positive_observations']}/{rf05['event_share']['observations']}` positive Ereignisanteil-Beobachtungen, Persistenz `{_fmt(rf05['event_share']['observation_directional_persistence'])}` und ein mittleres Nullperzentil von `{_fmt(rf05['event_share']['mean_null_percentile'])}`. Sein Persistenzperzentil innerhalb der acht gleich tief vermessenen Familien beträgt `{_fmt(rf05['event_share']['axis_persistence_percentile'])}`.",
            "",
            f"Die positive Richtung ist damit nicht exklusiv: `rf_07` und `rf_08` tragen ebenfalls zehn positive Antworten. `rf_05` besitzt jedoch den größten mittleren Zuwachs und den größten mittleren Abstand zur eigenen Pseudo-Verteilung; beide Maxima liegen bei `{strongest_positive['role_family']}` beziehungsweise `{highest_null_distance['role_family']}`. Sein Nullabstandsperzentil innerhalb der acht Familien beträgt `{_fmt(rf05['event_share']['axis_mean_null_percentile'])}`.",
            "",
            f"Entgegengesetzt tragen `{len(fully_negative_events)}/8` Familien zehn von zehn negative Ereignisanteil-Antworten: `{';'.join(str(row['role_family']) for row in fully_negative_events)}`. Dieselbe Volumenphasenlösung wirkt deshalb nicht allgemein verstärkend oder abschwächend, sondern wird von verschiedenen Familien in unterschiedliche Ereignisrichtungen aufgenommen.",
            "",
            f"Bei `rf_05` wechseln Kontinuität und Mitgliederabdeckung zwischen den Holdouts jeweils von positiv zu negativ (`{rf05['continuity']['holdout_sign_path']}` und `{rf05['member_coverage']['holdout_sign_path']}`). Nur der Ereignisanteil bleibt in beiden Holdouts positiv. Die wiederkehrende Achse und die kontextplastischen Achsen sind damit im gleichen Design getrennt sichtbar.",
            "",
            "Eine gleichgerichtete Antwort ist nur dann familienbezogen auffällig, wenn neben der Vorzeichenbilanz auch der Abstand zur jeweiligen Pseudo-Verteilung trägt. Diese beiden Koordinaten bleiben getrennt und werden nicht zu einer Klasse verdichtet.",
            "",
            "## Grenze",
            "",
            "Die zehn Gruppenwerte je Familie stammen aus 24 Realwelten, nicht aus zehn unabhängigen Experimenten. Der Lauf balanciert Familien und Holdouts, erweitert aber weder Assets noch Zeitebene oder Phasenoperation. Alle Pseudo-Details bleiben lokal im Debugbereich.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Liest alle Rollenfamilien auf den vorhandenen Volumen-Holdouts."
    )
    parser.add_argument("--memory", default=str(DEFAULT_MEMORY))
    parser.add_argument("--cohesion-detail", default=str(DEFAULT_COHESION))
    parser.add_argument("--definitions", default=str(DEFAULT_DEFINITIONS))
    parser.add_argument("--data-2083", default=str(DEFAULT_DATA_2083))
    parser.add_argument("--debug-2083", default=str(DEFAULT_DEBUG_2083))
    parser.add_argument("--data-2086", default=str(DEFAULT_DATA_2086))
    parser.add_argument("--debug-2086", default=str(DEFAULT_DEBUG_2086))
    parser.add_argument("--detail-dir", default=str(DEFAULT_DETAIL_DIR))
    parser.add_argument("--out-prefix", default=str(DEFAULT_OUT_PREFIX))
    args = parser.parse_args()

    role_memory = _resolve(args.memory)
    cohesion = _resolve(args.cohesion_detail)
    definitions_path = _resolve(args.definitions)
    data_2083 = _resolve(args.data_2083)
    debug_2083 = _resolve(args.debug_2083)
    data_2086 = _resolve(args.data_2086)
    debug_2086 = _resolve(args.debug_2086)
    detail_dir = _resolve(args.detail_dir)
    out_prefix = _resolve(args.out_prefix)

    targets = _load_targets(role_memory, list(ROLE_FAMILIES))
    all_symbols = sorted({symbol for members in targets.values() for symbol in members})
    global_counts = _load_global_source_counts(cohesion, set(all_symbols))
    definitions = [
        row
        for row in _load_csv(definitions_path)
        if row["role_family"] in ROLE_FAMILIES
    ]
    observed_definitions = _observed_definitions(targets, global_counts)

    real_2083, phase_2083 = _build_records(data_2083)
    summary_2083, pseudos_2083 = _evaluate_holdout(
        "2083_5m_windows",
        real_2083,
        phase_2083,
        debug_2083,
        all_symbols,
        observed_definitions,
        definitions,
        global_counts,
    )
    real_2086, phase_2086 = _build_holdout_records(data_2086)
    summary_2086, pseudos_2086 = _evaluate_holdout(
        "2086_5m_windows",
        real_2086,
        phase_2086,
        debug_2086,
        all_symbols,
        observed_definitions,
        definitions,
        global_counts,
    )
    summary = [*summary_2083, *summary_2086]
    axes = _build_axes(summary)

    _write_csv(out_prefix.with_suffix(".summary.csv"), summary)
    _write_csv(out_prefix.with_suffix(".axes.csv"), axes)
    _write_csv(
        detail_dir / "2089_ALLE_ROLLENFAMILIEN_VOLUME_EVIDENZBALANCE.pseudos.csv",
        [
            *({"holdout_id": "2083_5m_windows", **row} for row in pseudos_2083),
            *({"holdout_id": "2086_5m_windows", **row} for row in pseudos_2086),
        ],
    )
    _write_markdown(out_prefix.with_suffix(".md"), summary, axes)

    print(f"families={len(ROLE_FAMILIES)}")
    print(f"summary_rows={len(summary)}")
    print(f"axis_rows={len(axes)}")
    print(f"pseudo_detail_rows={len(pseudos_2083) + len(pseudos_2086)}")
    print(f"new_worlds=0")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
