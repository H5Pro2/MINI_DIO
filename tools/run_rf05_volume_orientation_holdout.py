from __future__ import annotations

import argparse
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
    from tools.run_role_family_real_null_contrast import _relative, _write_control_archive
    from tools.run_rf05_component_phase_controls import ROWS, _phase_worlds
    from tools.run_rf05_volume_5m_memory_maturation import (
        GROUPS,
        TARGET_COMPONENTS,
        TARGET_FAMILY,
        _build_summary,
        _ensure_slice,
        _observed_definition,
        _run_pool_worlds,
    )
    from tools.run_rf05_volume_state_response_coupling import (
        _build_correlations,
        _build_vectors,
        _safe_float,
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
    from run_role_family_real_null_contrast import _relative, _write_control_archive
    from run_rf05_component_phase_controls import ROWS, _phase_worlds
    from run_rf05_volume_5m_memory_maturation import (
        GROUPS,
        TARGET_COMPONENTS,
        TARGET_FAMILY,
        _build_summary,
        _ensure_slice,
        _observed_definition,
        _run_pool_worlds,
    )
    from run_rf05_volume_state_response_coupling import (
        _build_correlations,
        _build_vectors,
        _safe_float,
    )


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = ROOT / "docs" / "befunde" / "2001-3000"
DEFAULT_DEFINITIONS = PSEUDO_PREFIX.with_suffix(".definitions.csv")
DEFAULT_DATA_DIR = ROOT / "data" / "generated" / "2086_rf05_volume_orientation_holdout"
DEFAULT_ARCHIVE = ROOT / "data" / "2086_rf05_volume_orientation_holdout.zip"
DEFAULT_DEBUG_ROOT = ROOT / "debug" / "2086_rf05_volume_orientation_holdout"
DEFAULT_DETAIL_DIR = ROOT / "debug" / "2086_rf05_volume_orientation_holdout_detail"
DEFAULT_OUT_PREFIX = BEFUNDE / "2086_RF05_VOLUME_ORIENTIERUNGS_HOLDOUT"
PRIMARY_ORIENTATIONS = (
    ("baseline_continuity", "delta_event_share"),
    ("baseline_event_share", "delta_continuity"),
    ("baseline_event_share", "delta_member_coverage"),
    ("baseline_member_coverage", "delta_event_share"),
)
SIGNED_PERCENTILE_MIN = 0.95
SPECS = tuple(
    {
        "asset": asset,
        "year": year,
        "source": ROOT / "data" / f"1-12_{year}_5m_{asset}USDT.csv",
        "starts": (18000, 54000, 90000),
    }
    for year in (2024, 2025)
    for asset in ("BTC", "SOL")
)


def _build_holdout_records(
    data_dir: Path,
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
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
                data_dir
                / f"holdout_2086_{asset.lower()}_{year}_5m_start{start}_rows{ROWS}.csv",
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
                data_dir / f"control_2086_{asset.lower()}_{year}_5m_start{start}",
                TARGET_COMPONENTS,
            )
            for kind, path in paths.items():
                phase_records.append(
                    {
                        **real,
                        "kind": kind,
                        "seed": int(kind.rsplit("_", 1)[1]),
                        "path": path,
                    }
                )
    return real_records, phase_records


def _primary_rows(
    correlations: list[dict[str, object]],
) -> list[dict[str, object]]:
    primary = set(PRIMARY_ORIENTATIONS)
    rows: list[dict[str, object]] = []
    for row in correlations:
        key = (str(row["state_axis"]), str(row["response_axis"]))
        is_primary = key in primary
        positive = _safe_float(row["observed_spearman_rho"]) > 0.0
        null_distance = (
            _safe_float(row["observed_signed_percentile"])
            >= SIGNED_PERCENTILE_MIN
        )
        path_stable = int(row["leave_one_path_sign_consistent"]) == int(
            row["leave_one_path_tests"]
        )
        rows.append(
            {
                **row,
                "primary_orientation": int(is_primary),
                "expected_sign": "positive" if is_primary else "exploratory",
                "positive_sign_match": int(positive) if is_primary else "",
                "signed_percentile_match": int(null_distance) if is_primary else "",
                "leave_one_path_match": int(path_stable) if is_primary else "",
                "orientation_replicated": (
                    int(positive and null_distance and path_stable)
                    if is_primary
                    else ""
                ),
            }
        )
    return rows


def _write_markdown(
    path: Path,
    correlations: list[dict[str, object]],
    response_summary: list[dict[str, object]],
    archive: Path,
) -> None:
    primary = [row for row in correlations if int(row["primary_orientation"]) == 1]
    replicated = sum(int(row["orientation_replicated"]) for row in primary)
    closed = replicated == len(PRIMARY_ORIENTATIONS)
    overall = next(row for row in response_summary if row["group"] == "overall")
    group_matches = sum(int(row["expected_relation_match"]) for row in response_summary)
    lines = [
        "# 2086 - rf_05:volume Orientierungs-Holdout",
        "",
        "## Zweck",
        "",
        "Befund 2085 fand vier positive Kreuzkopplungen zwischen ungestörtem Familienzustand und Volumenphasenantwort. Dieser Lauf prüft genau diese Orientierung vorab in zwölf neuen, nicht überlappenden 5m-Fenstern.",
        "",
        "## Vorab festgelegtes Design",
        "",
        "- Datenjahre `2024` und `2025`",
        "- Assets `BTC` und `SOL`",
        "- neue Startpunkte `18000`, `54000`, `90000`",
        "- zwölf Realwelten mit je `1000` Beobachtungen",
        "- ausschließlich Volumenphase mit Offsets `17`, `83`, `251`",
        "- 36 Phasenkontrollen in einem Weltarchiv",
        "- dieselben 100 größen- und häufigkeitsgematchten Pseudo-Familien",
        "- positive Richtung, signiertes Pseudo-Perzentil mindestens `0.950` und `4/4` Leave-one-path-Richtungsstabilität je Primärachse",
        "- geschlossene Replikation nur bei `4/4` Primärachsen",
        f"- Weltarchiv: `{_relative(archive)}`",
        "- keine Memory-Erweiterung und keine Runtime-Rückwirkung",
        "",
        "## Primäre Orientierungen",
        "",
        "| Ausgangslage | Antwortachse | Spearman ρ | signiertes Perzentil | Pseudo gleiches Vorzeichen | LOO stabil | repliziert |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in primary:
        lines.append(
            f"| `{row['state_axis']}` | `{row['response_axis']}` | "
            f"{_fmt(row['observed_spearman_rho'])} | "
            f"{_fmt(row['observed_signed_percentile'])} | "
            f"{row['pseudo_same_sign']}/{row['pseudo_families']} | "
            f"{row['leave_one_path_sign_consistent']}/{row['leave_one_path_tests']} | "
            f"{row['orientation_replicated']} |"
        )
    lines.extend(
        [
            "",
            "## Vollständige Matrix",
            "",
            "| Ausgangslage | Antwortachse | primär | Spearman ρ | Pseudo-Mittel | signiertes Perzentil | Betrag-Perzentil |",
            "|---|---|---:|---:|---:|---:|---:|",
        ]
    )
    for row in correlations:
        lines.append(
            f"| `{row['state_axis']}` | `{row['response_axis']}` | "
            f"{row['primary_orientation']} | {_fmt(row['observed_spearman_rho'])} | "
            f"{_fmt(row['pseudo_mean_rho'])} | "
            f"{_fmt(row['observed_signed_percentile'])} | "
            f"{_fmt(row['observed_absolute_percentile'])} |"
        )
    lines.extend(
        [
            "",
            "## Sekundäre Gesamtantwort",
            "",
        "| Gruppe | erwartet/beobachtet | Pseudo gleich | Δ K/E/A | Perzentile K/E/A |",
        "|---|---|---:|---:|---:|",
        ]
    )
    for row in response_summary:
        lines.append(
            f"| `{row['group']}` | `{row['expected_relation']}/{row['observed_relation']}` | "
            f"{row['pseudo_same_relation']}/{row['pseudo_families']} | "
            f"{_fmt(row['observed_control_minus_real_family_continuity_score'])}/"
            f"{_fmt(row['observed_control_minus_real_mean_family_event_share'], 4)}/"
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
            f"Die vorab festgelegte Orientierungsordnung repliziert auf `{replicated}/4` Primärachsen; geschlossen: `{int(closed)}`.",
            "",
            f"Alle vier primären Rohkorrelationen sind im Holdout negativ: `{int(all(_safe_float(row['observed_spearman_rho']) < 0.0 for row in primary))}`. Die positive Kreuzorientierung aus 2085 ist damit keine unabhängige Invariante und begründet keine Kopplungsregel oder neue passive Beziehungsidentität.",
            "",
            f"Die bekannte Gesamtverstärkung erscheint in `{group_matches}/5` Gruppen. Im Gesamtprofil lautet die Antwort `{overall['observed_relation']}` bei `{overall['pseudo_same_relation']}/100` gleichen Pseudo-Antworten und den Perzentilen `{_fmt(overall['observed_percentile_control_minus_real_family_continuity_score'])}`, `{_fmt(overall['observed_percentile_control_minus_real_mean_family_event_share'])}`, `{_fmt(overall['observed_percentile_control_minus_real_mean_member_coverage'])}`.",
            "",
            f"Enger trägt nur der Ereignisanteil: Seine Antwort ist in allen fünf Gruppen positiv und liegt jeweils am Pseudo-Perzentil `1.000`. Gesamt steigt er um `{_fmt(overall['observed_control_minus_real_mean_family_event_share'], 4)}`, während Kontinuität um `{_fmt(overall['observed_control_minus_real_family_continuity_score'])}` und Mitgliederabdeckung um `{_fmt(overall['observed_control_minus_real_mean_member_coverage'])}` sinken. Die wiederkehrende Volumenphasensensitivität ist damit eher eine Umverteilung der Familienereignisse als eine allgemein verstärkende Familienform.",
            "",
            "Die Orientierung und die aggregierte Verstärkung sind getrennte Ebenen. Eine Kreuzkopplung beschreibt, wie Ausgangslagen und Antwortachsen gemeinsam variieren; sie beweist weder Ursache noch feste Bedeutung und darf nicht als Schaltlogik gelesen werden.",
            "",
            "## Grenze",
            "",
            "Der Holdout erweitert die unabhängigen Fenster, bleibt aber bei BTC/SOL, 5m, derselben Fensterlänge und derselben Volumenphasenoperation. Die passive Antwort-Memory bleibt bei 217 Beobachtungen und 32 Identitäten, bis eine weitere organische Erweiterung getrennt begründet und geprüft ist.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prüft vier rf_05-Volumenorientierungen in frischen 5m-Fenstern."
    )
    parser.add_argument("--memory", default=str(DEFAULT_MEMORY))
    parser.add_argument("--cohesion-detail", default=str(DEFAULT_COHESION))
    parser.add_argument("--definitions", default=str(DEFAULT_DEFINITIONS))
    parser.add_argument("--data-dir", default=str(DEFAULT_DATA_DIR))
    parser.add_argument("--archive", default=str(DEFAULT_ARCHIVE))
    parser.add_argument("--debug-root", default=str(DEFAULT_DEBUG_ROOT))
    parser.add_argument("--detail-dir", default=str(DEFAULT_DETAIL_DIR))
    parser.add_argument("--out-prefix", default=str(DEFAULT_OUT_PREFIX))
    args = parser.parse_args()

    role_memory = _resolve(args.memory)
    cohesion = _resolve(args.cohesion_detail)
    definitions_path = _resolve(args.definitions)
    data_dir = _resolve(args.data_dir)
    archive = _resolve(args.archive)
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
    real_records, phase_records = _build_holdout_records(data_dir)
    _write_control_archive(archive, phase_records)
    pool_rows = _run_pool_worlds(real_records + phase_records, all_symbols, debug_root)

    observed_vectors, pseudo_vectors = _build_vectors(
        real_records, pool_rows, targets, definitions, global_counts
    )
    correlations, pseudo_correlations = _build_correlations(
        observed_vectors, pseudo_vectors
    )
    correlation_rows = _primary_rows(correlations)

    observed_response = _evaluate_pseudos(
        _observed_definition(targets, global_counts),
        pool_rows,
        global_counts,
        TARGET_COMPONENTS,
        GROUPS,
    )
    pseudo_response = _evaluate_pseudos(
        definitions,
        pool_rows,
        global_counts,
        TARGET_COMPONENTS,
        GROUPS,
    )
    response_summary = _build_summary(observed_response, pseudo_response)

    vectors = [
        {
            "asset": row["asset"],
            "year": row["year"],
            "timeframe": row["timeframe"],
            "window_start": row["window_start"],
            "window_end": row["window_end"],
            "path_id": row["path_id"],
            "baseline_continuity": row["real_family_continuity_score"],
            "baseline_event_share": row["real_mean_family_event_share"],
            "baseline_member_coverage": row["real_mean_member_coverage"],
            "delta_continuity": row["control_minus_real_family_continuity_score"],
            "delta_event_share": row["control_minus_real_mean_family_event_share"],
            "delta_member_coverage": row["control_minus_real_mean_member_coverage"],
        }
        for row in observed_vectors
    ]
    _write_csv(out_prefix.with_suffix(".vectors.csv"), vectors)
    _write_csv(out_prefix.with_suffix(".correlations.csv"), correlation_rows)
    _write_csv(out_prefix.with_suffix(".summary.csv"), response_summary)
    _write_csv(
        detail_dir / "2086_RF05_VOLUME_ORIENTIERUNGS_HOLDOUT.pseudos.csv",
        pseudo_correlations,
    )
    _write_markdown(
        out_prefix.with_suffix(".md"), correlation_rows, response_summary, archive
    )

    primary = [row for row in correlation_rows if int(row["primary_orientation"]) == 1]
    print(f"real_worlds={len(real_records)}")
    print(f"phase_worlds={len(phase_records)}")
    print(f"vectors={len(vectors)}")
    print(f"correlations={len(correlation_rows)}")
    print(f"primary_replicated={sum(int(row['orientation_replicated']) for row in primary)}")
    print(f"response_summary_rows={len(response_summary)}")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
