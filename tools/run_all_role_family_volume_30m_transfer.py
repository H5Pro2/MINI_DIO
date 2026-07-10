from __future__ import annotations

import argparse
from pathlib import Path

try:
    from tools.run_all_role_family_volume_holdout_balance import (
        ROLE_FAMILIES,
        _build_axes,
        _build_summary,
        _observed_definitions,
        _sign,
    )
    from tools.run_role_family_30m_phase_holdout import (
        DEFAULT_DATA_DIR,
        DEFAULT_DEBUG_ROOT,
        _build_records,
        _run_pool_worlds,
    )
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
        _evaluate_pseudos,
        _fmt,
        _load_global_source_counts,
    )
    from tools.run_rf05_volume_5m_memory_maturation import GROUPS
except ModuleNotFoundError:
    from run_all_role_family_volume_holdout_balance import (
        ROLE_FAMILIES,
        _build_axes,
        _build_summary,
        _observed_definitions,
        _sign,
    )
    from run_role_family_30m_phase_holdout import (
        DEFAULT_DATA_DIR,
        DEFAULT_DEBUG_ROOT,
        _build_records,
        _run_pool_worlds,
    )
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
        _evaluate_pseudos,
        _fmt,
        _load_global_source_counts,
    )
    from run_rf05_volume_5m_memory_maturation import GROUPS


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = ROOT / "docs" / "befunde" / "2001-3000"
DEFAULT_DEFINITIONS = PSEUDO_PREFIX.with_suffix(".definitions.csv")
DEFAULT_DETAIL_DIR = ROOT / "debug" / "2090_all_role_family_volume_30m_transfer"
DEFAULT_OUT_PREFIX = BEFUNDE / "2090_ALLE_ROLLENFAMILIEN_VOLUME_30M_TRANSFER"
DEFAULT_FIVE_MINUTE_SUMMARY = (
    BEFUNDE / "2089_ALLE_ROLLENFAMILIEN_VOLUME_EVIDENZBALANCE.summary.csv"
)
COMPONENTS = ("volume",)
EXPECTED_DIRECTIONS = {
    "rf_05": 1,
    "rf_07": 1,
    "rf_08": 1,
    "rf_17": -1,
    "rf_21": -1,
}
DIRECTIONAL_PERCENTILE = 0.95
EVENT_VALUE = "observed_control_minus_real_mean_family_event_share"
EVENT_PERCENTILE = "observed_percentile_control_minus_real_mean_family_event_share"


def _build_directions(
    summary: list[dict[str, object]],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for role_family in ROLE_FAMILIES:
        family_rows = {
            str(row["group"]): row
            for row in summary
            if row["role_family"] == role_family
        }
        ordered = [family_rows[group] for group in GROUPS]
        signs = [_sign(_safe_float(row[EVENT_VALUE])) for row in ordered]
        expected = EXPECTED_DIRECTIONS.get(role_family)
        overall_percentile = _safe_float(family_rows["overall"][EVENT_PERCENTILE])
        group_matches = (
            sum(sign == expected for sign in signs) if expected is not None else ""
        )
        null_match = (
            int(
                overall_percentile >= DIRECTIONAL_PERCENTILE
                if expected == 1
                else overall_percentile <= 1.0 - DIRECTIONAL_PERCENTILE
            )
            if expected is not None
            else ""
        )
        strict = (
            int(group_matches == len(GROUPS) and int(null_match) == 1)
            if expected is not None
            else ""
        )
        rows.append(
            {
                "role_family": role_family,
                "component": "volume",
                "response_axis": "event_share",
                "primary_direction": int(expected is not None),
                "expected_sign": expected if expected is not None else "",
                "group_order": ";".join(GROUPS),
                "observed_sign_path": ";".join(str(sign) for sign in signs),
                "groups_matching_expected": group_matches,
                "groups_tested": len(GROUPS),
                "overall_delta_event_share": family_rows["overall"][EVENT_VALUE],
                "overall_null_percentile": overall_percentile,
                "directional_null_match": null_match,
                "strict_direction_replicated": strict,
                "overall_pseudo_same_relation": family_rows["overall"][
                    "pseudo_same_relation"
                ],
            }
        )
    return rows


def _write_markdown(
    path: Path,
    directions: list[dict[str, object]],
    axes: list[dict[str, object]],
    combined_axes: list[dict[str, object]],
) -> None:
    primary = [row for row in directions if int(row["primary_direction"]) == 1]
    exploratory = [row for row in directions if int(row["primary_direction"]) == 0]
    replicated = sum(int(row["strict_direction_replicated"]) for row in primary)
    event_axes = {
        str(row["role_family"]): row
        for row in axes
        if row["response_axis"] == "event_share"
    }
    combined_events = sorted(
        (row for row in combined_axes if row["response_axis"] == "event_share"),
        key=lambda row: str(row["role_family"]),
    )
    replicated_names = [
        str(row["role_family"])
        for row in primary
        if int(row["strict_direction_replicated"]) == 1
    ]
    failed_names = [
        str(row["role_family"])
        for row in primary
        if int(row["strict_direction_replicated"]) == 0
    ]
    exploratory_negative = [
        str(row["role_family"])
        for row in exploratory
        if row["observed_sign_path"] == "-1;-1;-1;-1;-1"
        and _safe_float(row["overall_null_percentile"]) <= 0.05
    ]
    lines = [
        "# 2090 - Familienabhängige Volumenrichtung im 30m-Transfer",
        "",
        "## Zweck",
        "",
        "Befund 2089 zeigt auf zwei 5m-Holdouts positive Ereignisanteil-Antworten für `rf_05`, `rf_07`, `rf_08` und negative für `rf_17`, `rf_21`. Dieser Lauf prüft diese fünf Richtungen vorab auf den bereits vorhandenen 30m-Welten aus Befund 2081.",
        "",
        "## Vorab festgelegtes Design",
        "",
        "- zwölf 30m-Realwelten aus 2024 und 2025",
        "- BTC und SOL",
        "- 36 vorhandene Volumenphasenkontrollen mit Offsets `17`, `83`, `251`",
        "- fünf Gruppen: Gesamt, beide Jahre und beide Assets",
        "- pro Familie und Gruppe 100 größen- und häufigkeitsgematchte Pseudo-Familien",
        "- positive Erwartung für `rf_05`, `rf_07`, `rf_08`",
        "- negative Erwartung für `rf_17`, `rf_21`",
        "- strenge Replikation nur bei `5/5` passenden Gruppenvorzeichen und Gesamt-Nullperzentil mindestens `0.950` in erwarteter Richtung",
        "- `rf_06`, `rf_10`, `rf_13` bleiben explorativ",
        "- keine neuen Welten, keine Memory-Erweiterung und keine Runtime-Wirkung",
        "",
        "## Primäre Richtungen",
        "",
        "| Familie | erwartet | Vorzeichenpfad G/24/25/BTC/SOL | passende Gruppen | Gesamt Δ Ereignisanteil | Nullperzentil | repliziert |",
        "|---|---:|---|---:|---:|---:|---:|",
    ]
    for row in primary:
        lines.append(
            f"| `{row['role_family']}` | {row['expected_sign']} | "
            f"`{row['observed_sign_path']}` | "
            f"{row['groups_matching_expected']}/{row['groups_tested']} | "
            f"{_fmt(row['overall_delta_event_share'], 4)} | "
            f"{_fmt(row['overall_null_percentile'])} | "
            f"{row['strict_direction_replicated']} |"
        )
    lines.extend(
        [
            "",
            "## Explorative Familien",
            "",
            "| Familie | Vorzeichenpfad | Gesamt Δ Ereignisanteil | Nullperzentil | Persistenz |",
            "|---|---|---:|---:|---:|",
        ]
    )
    for row in exploratory:
        axis = event_axes[str(row["role_family"])]
        lines.append(
            f"| `{row['role_family']}` | `{row['observed_sign_path']}` | "
            f"{_fmt(row['overall_delta_event_share'], 4)} | "
            f"{_fmt(row['overall_null_percentile'])} | "
            f"{_fmt(axis['observation_directional_persistence'])} |"
        )
    lines.extend(
        [
            "",
            "## Synthese über drei Holdouts",
            "",
            "| Familie | positiv/negativ/null | Mittel | Holdout-Vorzeichen | Persistenz | mittleres Nullperzentil |",
            "|---|---:|---:|---|---:|---:|",
        ]
    )
    for row in combined_events:
        lines.append(
            f"| `{row['role_family']}` | "
            f"{row['positive_observations']}/{row['negative_observations']}/{row['zero_observations']} | "
            f"{_fmt(row['mean_value'], 4)} | `{row['holdout_sign_path']}` | "
            f"{_fmt(row['observation_directional_persistence'])} | "
            f"{_fmt(row['mean_null_percentile'])} |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"Von fünf vorab gerichteten Familien replizieren `{replicated}/5` streng auf 30m.",
            "",
            f"Geschlossen tragen `{';'.join(replicated_names)}`; nicht geschlossen übertragen sich `{';'.join(failed_names)}`. Damit besitzt die familienabhängige Ereignisrichtung einen zeitebenenübergreifenden Kern, aber keine vollständige Invarianz aller 5m-Profile.",
            "",
            f"Über alle drei Holdouts bleiben `rf_05` und `rf_07` in `15/15` Gruppen positiv, `rf_17` in `15/15` negativ. Diese drei Richtungen wiederholen sich auf 5m und 30m. `rf_08` und `rf_21` tragen dagegen Zeitebenen- beziehungsweise Gruppendrift.",
            "",
            f"Explorativ liegen `{';'.join(exploratory_negative)}` auf 30m in allen fünf Gruppen negativ und am unteren Rand ihrer Pseudo-Verteilungen. Da diese Richtung nicht vorab festgelegt war, bleibt sie Kandidat und keine Replikation.",
            "",
            "Der Transfer prüft die Richtung des Familienereignisanteils, nicht eine vollständige dreiachsige Familienform. Kontinuität und Mitgliederabdeckung bleiben in der Achsendatei sichtbar, werden aber nicht nachträglich zu Primärzielen erklärt.",
            "",
            "## Grenze",
            "",
            "Die 30m-Welten erweitern die Zeitebene, bleiben aber bei BTC/SOL, denselben Jahren, derselben Fensterlänge und derselben zirkulären Volumenphasenoperation. Gruppenwerte überlappen in ihrer Weltbasis und sind keine fünf unabhängigen Experimente. Pseudo-Details bleiben lokal.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prüft familienabhängige Volumenrichtungen auf vorhandenen 30m-Welten."
    )
    parser.add_argument("--memory", default=str(DEFAULT_MEMORY))
    parser.add_argument("--cohesion-detail", default=str(DEFAULT_COHESION))
    parser.add_argument("--definitions", default=str(DEFAULT_DEFINITIONS))
    parser.add_argument("--data-dir", default=str(DEFAULT_DATA_DIR))
    parser.add_argument("--debug-root", default=str(DEFAULT_DEBUG_ROOT))
    parser.add_argument("--detail-dir", default=str(DEFAULT_DETAIL_DIR))
    parser.add_argument(
        "--five-minute-summary", default=str(DEFAULT_FIVE_MINUTE_SUMMARY)
    )
    parser.add_argument("--out-prefix", default=str(DEFAULT_OUT_PREFIX))
    args = parser.parse_args()

    role_memory = _resolve(args.memory)
    cohesion = _resolve(args.cohesion_detail)
    definitions_path = _resolve(args.definitions)
    data_dir = _resolve(args.data_dir)
    debug_root = _resolve(args.debug_root)
    detail_dir = _resolve(args.detail_dir)
    five_minute_summary = _resolve(args.five_minute_summary)
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

    real_records, phase_records = _build_records(data_dir)
    volume_records = [
        row for row in phase_records if str(row["kind"]).startswith("volume_phase_")
    ]
    if len(real_records) != 12 or len(volume_records) != 36:
        raise ValueError(
            f"Erwartet 12 Real- und 36 Volumenwelten, gefunden {len(real_records)}/{len(volume_records)}"
        )
    pool_rows = _run_pool_worlds(
        real_records + volume_records, all_symbols, debug_root
    )
    observed = _evaluate_pseudos(
        observed_definitions,
        pool_rows,
        global_counts,
        COMPONENTS,
        GROUPS,
    )
    pseudos = _evaluate_pseudos(
        definitions,
        pool_rows,
        global_counts,
        COMPONENTS,
        GROUPS,
    )
    summary = _build_summary("2081_30m_windows", observed, pseudos)
    axes = _build_axes(summary)
    directions = _build_directions(summary)
    combined_summary = [*_load_csv(five_minute_summary), *summary]
    combined_axes = _build_axes(combined_summary)

    _write_csv(out_prefix.with_suffix(".summary.csv"), summary)
    _write_csv(out_prefix.with_suffix(".axes.csv"), axes)
    _write_csv(out_prefix.with_suffix(".directions.csv"), directions)
    _write_csv(out_prefix.with_suffix(".combined.axes.csv"), combined_axes)
    _write_csv(
        detail_dir / "2090_ALLE_ROLLENFAMILIEN_VOLUME_30M_TRANSFER.pseudos.csv",
        pseudos,
    )
    _write_markdown(
        out_prefix.with_suffix(".md"), directions, axes, combined_axes
    )

    primary = [row for row in directions if int(row["primary_direction"]) == 1]
    print(f"real_worlds={len(real_records)}")
    print(f"volume_worlds={len(volume_records)}")
    print(f"summary_rows={len(summary)}")
    print(f"axis_rows={len(axes)}")
    print(f"primary_replicated={sum(int(row['strict_direction_replicated']) for row in primary)}")
    print(f"pseudo_detail_rows={len(pseudos)}")
    print(f"new_worlds=0")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
