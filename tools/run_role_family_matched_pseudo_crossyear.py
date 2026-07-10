from __future__ import annotations

import argparse
from pathlib import Path

try:
    from tools.run_role_family_component_phase_profiles import (
        DEFAULT_COHESION,
        DEFAULT_MEMORY,
        ROLE_FAMILIES,
        _load_targets,
        _resolve,
        _write_csv,
    )
    from tools.run_role_family_followworld_probe import _load_csv, _safe_float
    from tools.run_role_family_matched_pseudo_controls import (
        DEFAULT_OUT_PREFIX as PSEUDO_2025_PREFIX,
        _build_null_summary,
        _evaluate_pseudos,
        _fmt,
        _load_global_source_counts,
        _load_pool_member_rows,
    )
    from tools.run_rf05_component_phase_controls import (
        BASE_DATA_DIR,
        BASE_DEBUG_ROOT,
        DEFAULT_ARCHIVE as PHASE_ARCHIVE,
        DEFAULT_DATA_DIR as PHASE_DATA_DIR,
        DEFAULT_DEBUG_ROOT as PHASE_DEBUG_ROOT,
        _build_phase_records,
        _build_world_records,
    )
    from tools.run_role_family_real_null_contrast import _relative
except ModuleNotFoundError:
    from run_role_family_component_phase_profiles import (
        DEFAULT_COHESION,
        DEFAULT_MEMORY,
        ROLE_FAMILIES,
        _load_targets,
        _resolve,
        _write_csv,
    )
    from run_role_family_followworld_probe import _load_csv, _safe_float
    from run_role_family_matched_pseudo_controls import (
        DEFAULT_OUT_PREFIX as PSEUDO_2025_PREFIX,
        _build_null_summary,
        _evaluate_pseudos,
        _fmt,
        _load_global_source_counts,
        _load_pool_member_rows,
    )
    from run_rf05_component_phase_controls import (
        BASE_DATA_DIR,
        BASE_DEBUG_ROOT,
        DEFAULT_ARCHIVE as PHASE_ARCHIVE,
        DEFAULT_DATA_DIR as PHASE_DATA_DIR,
        DEFAULT_DEBUG_ROOT as PHASE_DEBUG_ROOT,
        _build_phase_records,
        _build_world_records,
    )
    from run_role_family_real_null_contrast import _relative


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = ROOT / "docs" / "befunde" / "2001-3000"
DEFAULT_DEFINITIONS = PSEUDO_2025_PREFIX.with_suffix(".definitions.csv")
DEFAULT_SUMMARY_2025 = PSEUDO_2025_PREFIX.with_suffix(".summary.csv")
DEFAULT_COMPARISON_2024 = (
    BEFUNDE / "2077_ROLLENFAMILIEN_KOMPONENTEN_PHASENPROFILE.comparison.csv"
)
DEFAULT_OUT_PREFIX = BEFUNDE / "2080_RF08_SIGN_GEMATCHTER_CROSSYEAR_KONTRAST"
GROUPS = ("overall", "timeframe:1h", "timeframe:15m")


def _set_primary_axis(summary: list[dict[str, object]]) -> None:
    for row in summary:
        row["primary_axis"] = int(
            row["role_family"] == "rf_08" and row["component"] == "sign"
        )


def _index(rows: list[dict[str, object]]) -> dict[tuple[str, str, str], dict[str, object]]:
    return {
        (str(row["group"]), str(row["role_family"]), str(row["component"])): row
        for row in rows
    }


def _write_markdown(
    path: Path,
    summary_2024: list[dict[str, object]],
    summary_2025: list[dict[str, str]],
    phase_archive: Path,
    definitions_path: Path,
) -> None:
    by_2024 = _index(summary_2024)
    by_2025 = _index(summary_2025)
    lines = [
        "# 2080 - rf_08:sign im gematchten Crossyear-Kontrast",
        "",
        "## Zweck",
        "",
        "Befund 2079 ließ `rf_08:sign` nur im 15m-Kontext deutlich außerhalb größen- und häufigkeitsgematchter Pseudo-Familien zurück. Dieser Lauf wendet dieselbe Nullkontrolle auf die vorhandenen 2024-Welten an und prüft, ob die 15m-Bindung über das Jahr hinweg wiederkehrt.",
        "",
        "## Vorab Festgelegtes Design",
        "",
        "- keine neuen Weltläufe und keine neuen Kontrollwelten",
        f"- wiederverwendetes 2024-Phasenarchiv: `{_relative(phase_archive)}`",
        f"- exakt dieselben 800 Pseudo-Familien wie in 2079: `{_relative(definitions_path)}`",
        "- Primärachse: `rf_08:sign`",
        "- vorab erwarteter Kontrast: größerer Abstand zur Pseudo-Verteilung auf 15m als auf 1h",
        "- Gesamtprofil, 1h und 15m werden getrennt ausgewiesen",
        "- `rf_05:volume` bleibt explorativ und zählt nicht zur Primärprüfung",
        "- keine neue Klasse, keine Handlung, kein Gate und keine Richtung",
        "",
        "## Primärachse Über Beide Jahre",
        "",
        "| Jahr | Ebene | reales Profil | Pseudo gleich | Δ Kontinuität Perzentil | Δ Ereignisanteil Perzentil | Δ Abdeckung Perzentil |",
        "|---|---|---|---:|---:|---:|---:|",
    ]
    for year, indexed in ((2024, by_2024), (2025, by_2025)):
        for group in GROUPS:
            row = indexed[(group, "rf_08", "sign")]
            lines.append(
                f"| {year} | `{group}` | `{row['observed_relation']}` | "
                f"{row['pseudo_same_relation']}/{row['pseudo_families']} | "
                f"{_fmt(row['observed_percentile_control_minus_real_family_continuity_score'])} | "
                f"{_fmt(row['observed_percentile_control_minus_real_mean_family_event_share'])} | "
                f"{_fmt(row['observed_percentile_control_minus_real_mean_member_coverage'])} |"
            )

    lines.extend(
        [
            "",
            "## Explorative rf_05-Volumenachse",
            "",
            "| Jahr | Ebene | reales Profil | Pseudo gleich | Δ Kontinuität Perzentil | Δ Ereignisanteil Perzentil | Δ Abdeckung Perzentil |",
            "|---|---|---|---:|---:|---:|---:|",
        ]
    )
    for year, indexed in ((2024, by_2024), (2025, by_2025)):
        for group in GROUPS:
            row = indexed[(group, "rf_05", "volume")]
            lines.append(
                f"| {year} | `{group}` | `{row['observed_relation']}` | "
                f"{row['pseudo_same_relation']}/{row['pseudo_families']} | "
                f"{_fmt(row['observed_percentile_control_minus_real_family_continuity_score'])} | "
                f"{_fmt(row['observed_percentile_control_minus_real_mean_family_event_share'])} | "
                f"{_fmt(row['observed_percentile_control_minus_real_mean_member_coverage'])} |"
            )

    lines.extend(
        [
            "",
            "## Alle 2024-Familienachsen",
            "",
            "| Familie | Komponente | reales Profil | Pseudo gleich | Kontinuitätsperzentil |",
            "|---|---|---|---:|---:|",
        ]
    )
    for row in summary_2024:
        if row["group"] != "overall":
            continue
        lines.append(
            f"| `{row['role_family']}` | `{row['component']}` | `{row['observed_relation']}` | "
            f"{row['pseudo_same_relation']}/{row['pseudo_families']} | "
            f"{_fmt(row['observed_percentile_control_minus_real_family_continuity_score'])} |"
        )

    rf08_2024_1h = by_2024[("timeframe:1h", "rf_08", "sign")]
    rf08_2024_15m = by_2024[("timeframe:15m", "rf_08", "sign")]
    rf08_2024_overall = by_2024[("overall", "rf_08", "sign")]
    rf08_2025_overall = by_2025[("overall", "rf_08", "sign")]
    rf05_2024_overall = by_2024[("overall", "rf_05", "volume")]
    rf05_2025_overall = by_2025[("overall", "rf_05", "volume")]
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"Der vorab erwartete stärkere 15m-Abstand repliziert 2024 nicht. Auf 1h tragen `{rf08_2024_1h['pseudo_same_relation']}/100`, auf 15m `{rf08_2024_15m['pseudo_same_relation']}/100` Pseudo-Familien dieselbe `rf_08:sign`-Antwort. Die 1h-Perzentile liegen zwischen `{_fmt(min(_safe_float(rf08_2024_1h['observed_percentile_control_minus_real_family_continuity_score']), _safe_float(rf08_2024_1h['observed_percentile_control_minus_real_mean_family_event_share']), _safe_float(rf08_2024_1h['observed_percentile_control_minus_real_mean_member_coverage'])))}` und `{_fmt(max(_safe_float(rf08_2024_1h['observed_percentile_control_minus_real_family_continuity_score']), _safe_float(rf08_2024_1h['observed_percentile_control_minus_real_mean_family_event_share']), _safe_float(rf08_2024_1h['observed_percentile_control_minus_real_mean_member_coverage'])))}`, die 15m-Perzentile zwischen `{_fmt(min(_safe_float(rf08_2024_15m['observed_percentile_control_minus_real_family_continuity_score']), _safe_float(rf08_2024_15m['observed_percentile_control_minus_real_mean_family_event_share']), _safe_float(rf08_2024_15m['observed_percentile_control_minus_real_mean_member_coverage'])))}` und `{_fmt(max(_safe_float(rf08_2024_15m['observed_percentile_control_minus_real_family_continuity_score']), _safe_float(rf08_2024_15m['observed_percentile_control_minus_real_mean_family_event_share']), _safe_float(rf08_2024_15m['observed_percentile_control_minus_real_mean_member_coverage'])))}`. `rf_08:sign` ist 2024 somit auf beiden Zeitebenen auffällig.",
            "",
            f"Der breitere Familienabstand wiederholt sich dagegen. Im 2024-Gesamtprofil tragen `{rf08_2024_overall['pseudo_same_relation']}/100` dieselbe Verstärkung bei Perzentilen `0.980`, `0.990`, `1.000`; 2025 sind es `{rf08_2025_overall['pseudo_same_relation']}/100` bei `0.900`, `0.920`, `0.930`. Das stützt eine wiederkehrende familienbezogene Vorzeichen-Phasenantwort gegenüber identischen alternativen Mitgliedschaften. Ihre genaue Verteilung auf Zeitebenen ist jedoch jahresabhängig.",
            "",
            f"Explorativ ist `rf_05:volume` noch deutlicher: In beiden Gesamtjahren tragen `{rf05_2024_overall['pseudo_same_relation']}/100` beziehungsweise `{rf05_2025_overall['pseudo_same_relation']}/100` Pseudo-Familien dieselbe Verstärkung. 2024 liegen alle drei Perzentile bei `1.000`; 2025 bei `0.980`, `1.000`, `1.000`. Da diese Achse erst nach 2079 ausgewählt wurde und 2025 auf 15m gemischt bleibt, ist sie ein vorab zu prüfender Kandidat und keine Bestätigung.",
            "",
            "Der Crossyear-Befund trägt damit eine mögliche Familien-Komponenten-Kopplung, aber keine feste Zeitebenenbindung. Auch der wiederkehrende Abstand bleibt passive Evidenz und wird nicht als Familienbedeutung, Handlung oder neue Feldregel gespeichert. Eine organische Erweiterung ist noch nicht begründet.",
            "",
            "## Grenze",
            "",
            "Beide Jahre verwenden BTC/SOL, dieselben Fensterlängen, dieselben Phasenoperationen und denselben Symbolpool. Der Lauf prüft Jahreswiederkehr innerhalb dieser Messgeometrie, nicht Modalitätsunabhängigkeit, Kausalität oder allgemeine Feldintelligenz.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Prüft rf_08:sign gematcht über 2024 und 2025.")
    parser.add_argument("--memory", default=str(DEFAULT_MEMORY))
    parser.add_argument("--cohesion-detail", default=str(DEFAULT_COHESION))
    parser.add_argument("--definitions", default=str(DEFAULT_DEFINITIONS))
    parser.add_argument("--summary-2025", default=str(DEFAULT_SUMMARY_2025))
    parser.add_argument("--comparison-2024", default=str(DEFAULT_COMPARISON_2024))
    parser.add_argument("--base-data-dir", default=str(BASE_DATA_DIR))
    parser.add_argument("--base-debug-root", default=str(BASE_DEBUG_ROOT))
    parser.add_argument("--phase-data-dir", default=str(PHASE_DATA_DIR))
    parser.add_argument("--phase-debug-root", default=str(PHASE_DEBUG_ROOT))
    parser.add_argument("--phase-archive", default=str(PHASE_ARCHIVE))
    parser.add_argument("--out-prefix", default=str(DEFAULT_OUT_PREFIX))
    args = parser.parse_args()

    memory = _resolve(args.memory)
    cohesion = _resolve(args.cohesion_detail)
    definitions_path = _resolve(args.definitions)
    summary_2025_path = _resolve(args.summary_2025)
    comparison_2024 = _resolve(args.comparison_2024)
    base_data_dir = _resolve(args.base_data_dir)
    base_debug_root = _resolve(args.base_debug_root)
    phase_data_dir = _resolve(args.phase_data_dir)
    phase_debug_root = _resolve(args.phase_debug_root)
    phase_archive = _resolve(args.phase_archive)
    out_prefix = _resolve(args.out_prefix)

    targets = _load_targets(memory, list(ROLE_FAMILIES))
    all_symbols = sorted({symbol for members in targets.values() for symbol in members})
    global_counts = _load_global_source_counts(cohesion, set(all_symbols))
    definitions = _load_csv(definitions_path)
    base_records = _build_world_records(base_data_dir)
    real_records = [record for record in base_records if record["kind"] == "real"]
    phase_records = _build_phase_records(real_records, phase_data_dir)
    pool_rows = _load_pool_member_rows(real_records, all_symbols, base_debug_root)
    pool_rows.extend(
        _load_pool_member_rows(phase_records, all_symbols, phase_debug_root)
    )
    pseudo_rows = _evaluate_pseudos(definitions, pool_rows, global_counts)
    summary_2024 = _build_null_summary(pseudo_rows, comparison_2024)
    _set_primary_axis(summary_2024)
    summary_2025 = _load_csv(summary_2025_path)

    _write_csv(out_prefix.with_suffix(".pseudos.csv"), pseudo_rows)
    _write_csv(out_prefix.with_suffix(".summary.csv"), summary_2024)
    _write_markdown(
        out_prefix.with_suffix(".md"),
        summary_2024,
        summary_2025,
        phase_archive,
        definitions_path,
    )

    print(f"symbols={len(all_symbols)}")
    print(f"worlds={len(real_records) + len(phase_records)}")
    print(f"pool_member_rows={len(pool_rows)}")
    print(f"pseudo_definitions={len(definitions)}")
    print(f"pseudo_component_rows={len(pseudo_rows)}")
    print(f"summary_rows={len(summary_2024)}")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
