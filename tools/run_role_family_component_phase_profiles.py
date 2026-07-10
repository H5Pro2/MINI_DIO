from __future__ import annotations

import argparse
from pathlib import Path

try:
    from tools.run_role_family_followworld_probe import (
        _build_family_summary,
        _build_world_family_rows,
        _load_source_member_counts,
        _load_targets,
        _safe_float,
        _write_csv,
    )
    from tools.run_rf05_component_phase_controls import (
        BASE_DATA_DIR,
        BASE_DEBUG_ROOT,
        COMPONENTS,
        DEFAULT_ARCHIVE as PHASE_ARCHIVE,
        DEFAULT_COHESION,
        DEFAULT_DATA_DIR as PHASE_DATA_DIR,
        DEFAULT_DEBUG_ROOT as PHASE_DEBUG_ROOT,
        DEFAULT_MEMORY,
        EXACT_KINDS,
        LAGS,
        PAIR_METRICS,
        PRIMARY_METRICS,
        SUMMARY_METRICS,
        _build_phase_records,
        _build_world_records,
        _build_world_rows,
        _filter_group,
        _fmt,
        _relative,
        _resolve,
        _run_worlds,
    )
except ModuleNotFoundError:
    from run_role_family_followworld_probe import (
        _build_family_summary,
        _build_world_family_rows,
        _load_source_member_counts,
        _load_targets,
        _safe_float,
        _write_csv,
    )
    from run_rf05_component_phase_controls import (
        BASE_DATA_DIR,
        BASE_DEBUG_ROOT,
        COMPONENTS,
        DEFAULT_ARCHIVE as PHASE_ARCHIVE,
        DEFAULT_COHESION,
        DEFAULT_DATA_DIR as PHASE_DATA_DIR,
        DEFAULT_DEBUG_ROOT as PHASE_DEBUG_ROOT,
        DEFAULT_MEMORY,
        EXACT_KINDS,
        LAGS,
        PAIR_METRICS,
        PRIMARY_METRICS,
        SUMMARY_METRICS,
        _build_phase_records,
        _build_world_records,
        _build_world_rows,
        _filter_group,
        _fmt,
        _relative,
        _resolve,
        _run_worlds,
    )


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = ROOT / "docs" / "befunde" / "2001-3000"
DEFAULT_OUT_PREFIX = BEFUNDE / "2077_ROLLENFAMILIEN_KOMPONENTEN_PHASENPROFILE"
ROLE_FAMILIES = ("rf_05", "rf_06", "rf_07", "rf_08", "rf_10", "rf_13", "rf_17", "rf_21")
GROUPS = ("overall", "asset:BTC", "asset:SOL", "timeframe:1h", "timeframe:15m")


def _kind_parts(kind: str) -> tuple[str, int]:
    component, _, lag = kind.rpartition("_phase_")
    return component, int(lag)


def _summaries_for_kinds(
    member_rows: list[dict[str, object]],
    targets: dict[str, list[str]],
    source_counts: dict,
    kinds: tuple[str, ...],
    group: str,
) -> dict[str, dict[str, object]]:
    rows = [row for row in member_rows if str(row["world_kind"]) in kinds]
    rows = _filter_group(rows, group)
    world_rows = _build_world_family_rows(rows)
    summaries = _build_family_summary(world_rows, rows, targets, source_counts)
    return {str(row["role_family"]): row for row in summaries}


def _build_paired(world_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    indexed = {
        (
            str(row["role_family"]),
            str(row["asset"]),
            str(row["timeframe"]),
            int(row["window_start"]),
            str(row["world_kind"]),
        ): row
        for row in world_rows
    }
    real_keys = sorted(key for key in indexed if key[4] == "real")
    rows: list[dict[str, object]] = []
    for role_family, asset, timeframe, start, _ in real_keys:
        real = indexed[(role_family, asset, timeframe, start, "real")]
        for kind in EXACT_KINDS:
            control = indexed[(role_family, asset, timeframe, start, kind)]
            component, lag = _kind_parts(kind)
            row: dict[str, object] = {
                "role_family": role_family,
                "asset": asset,
                "timeframe": timeframe,
                "window_start": start,
                "component": component,
                "lag": lag,
                "control_kind": kind,
            }
            for metric in PAIR_METRICS:
                real_value = _safe_float(real.get(metric))
                control_value = _safe_float(control.get(metric))
                row[f"real_{metric}"] = real_value
                row[f"control_{metric}"] = control_value
                row[f"real_minus_control_{metric}"] = real_value - control_value
            row["real_joint_coverage_event_advantage"] = int(
                _safe_float(row["real_minus_control_member_coverage"]) > 0.0
                and _safe_float(row["real_minus_control_family_event_share"]) > 0.0
            )
            rows.append(row)
    return rows


def _pair_counts(
    paired_rows: list[dict[str, object]],
    role_family: str,
    group: str,
    component: str,
    lag: int | None,
) -> dict[str, int]:
    rows = [row for row in paired_rows if row["role_family"] == role_family]
    rows = _filter_group(rows, group)
    rows = [row for row in rows if row["component"] == component]
    if lag is not None:
        rows = [row for row in rows if int(row["lag"]) == lag]
    return {
        "paired_windows": len(rows),
        "paired_event_share_real_wins": sum(
            _safe_float(row["real_minus_control_family_event_share"]) > 0.0 for row in rows
        ),
        "paired_coverage_real_wins": sum(
            _safe_float(row["real_minus_control_member_coverage"]) > 0.0 for row in rows
        ),
        "paired_joint_real_advantage": sum(
            int(row["real_joint_coverage_event_advantage"]) for row in rows
        ),
    }


def _build_comparisons(
    member_rows: list[dict[str, object]],
    targets: dict[str, list[str]],
    source_counts: dict,
    paired_rows: list[dict[str, object]],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for group in GROUPS:
        real = _summaries_for_kinds(member_rows, targets, source_counts, ("real",), group)
        for component in COMPONENTS:
            scopes: list[tuple[str, int | None, tuple[str, ...]]] = [
                (
                    "component",
                    None,
                    tuple(kind for kind in EXACT_KINDS if kind.startswith(f"{component}_")),
                )
            ]
            if group == "overall":
                scopes.extend(
                    ("lag", lag, (f"{component}_phase_{lag:03d}",)) for lag in LAGS
                )
            for scope, lag, kinds in scopes:
                control = _summaries_for_kinds(
                    member_rows,
                    targets,
                    source_counts,
                    kinds,
                    group,
                )
                for role_family in ROLE_FAMILIES:
                    real_row = real[role_family]
                    control_row = control[role_family]
                    row: dict[str, object] = {
                        "group": group,
                        "scope": scope,
                        "role_family": role_family,
                        "component": component,
                        "lag": "" if lag is None else lag,
                        "real_worlds": real_row["worlds"],
                        "control_worlds": control_row["worlds"],
                    }
                    for metric in SUMMARY_METRICS:
                        real_value = _safe_float(real_row.get(metric))
                        control_value = _safe_float(control_row.get(metric))
                        row[f"real_{metric}"] = real_value
                        row[f"control_{metric}"] = control_value
                        row[f"control_minus_real_{metric}"] = control_value - real_value
                    row.update(_pair_counts(paired_rows, role_family, group, component, lag))
                    rows.append(row)
    return rows


def _relation(row: dict[str, object]) -> str:
    deltas = [
        _safe_float(row[f"control_minus_real_{metric}"]) for _, metric in PRIMARY_METRICS
    ]
    if all(delta > 0.0 for delta in deltas):
        return "verstaerkt"
    if all(delta < 0.0 for delta in deltas):
        return "abgeschwaecht"
    return "gemischt"


def _build_family_profiles(comparisons: list[dict[str, object]]) -> list[dict[str, object]]:
    overall = [row for row in comparisons if row["group"] == "overall"]
    pooled = [row for row in overall if row["scope"] == "component"]
    exact = [row for row in overall if row["scope"] == "lag"]
    rows: list[dict[str, object]] = []
    for role_family in ROLE_FAMILIES:
        family_pooled = {
            str(row["component"]): row for row in pooled if row["role_family"] == role_family
        }
        family_exact = [row for row in exact if row["role_family"] == role_family]
        row: dict[str, object] = {"role_family": role_family}
        relations: list[str] = []
        for component in COMPONENTS:
            relation = _relation(family_pooled[component])
            row[f"{component}_relation"] = relation
            relations.append(relation)
        row["component_signature"] = ";".join(relations)
        row["pooled_strengthened_components"] = sum(
            relation == "verstaerkt" for relation in relations
        )
        row["pooled_weakened_components"] = sum(
            relation == "abgeschwaecht" for relation in relations
        )
        row["exact_strengthened_conditions"] = sum(
            _relation(item) == "verstaerkt" for item in family_exact
        )
        row["exact_weakened_conditions"] = sum(
            _relation(item) == "abgeschwaecht" for item in family_exact
        )
        rows.append(row)
    return rows


def _write_markdown(
    path: Path,
    comparisons: list[dict[str, object]],
    profiles: list[dict[str, object]],
    phase_archive: Path,
) -> None:
    pooled = [
        row
        for row in comparisons
        if row["group"] == "overall" and row["scope"] == "component"
    ]
    profile_by_family = {str(row["role_family"]): row for row in profiles}
    rf05 = profile_by_family["rf_05"]
    rf07 = profile_by_family["rf_07"]
    rf08 = profile_by_family["rf_08"]
    rf10 = profile_by_family["rf_10"]
    rf17 = profile_by_family["rf_17"]
    rf05_sign = next(
        row
        for row in pooled
        if row["role_family"] == "rf_05" and row["component"] == "sign"
    )
    same_signature = [
        family
        for family, row in profile_by_family.items()
        if family != "rf_05" and row["component_signature"] == rf05["component_signature"]
    ]
    same_sign_volume = [
        family
        for family, row in profile_by_family.items()
        if family != "rf_05"
        and row["sign_relation"] == rf05["sign_relation"]
        and row["volume_relation"] == rf05["volume_relation"]
    ]

    lines = [
        "# 2077 - Rollenfamilien unter Komponenten-Phasenprofilen",
        "",
        "## Zweck",
        "",
        "Befund 2076 fand bei `rf_05` keine allgemeine notwendige OHLCV-Kopplung, aber ein asymmetrisches Phasenprofil. Dieser Lauf prüft dieselben Welten mit allen acht Rollenfamilien, um familienspezifische Reaktion von einer allgemeinen Eigenschaft des Feldlesers zu trennen.",
        "",
        "## Vorab Festgelegtes Design",
        "",
        "- dieselben zwölf Realfenster und `144` Phasenkontrollen aus 2076",
        "- keine neue Kontrollwelt und kein zusätzliches Weltarchiv",
        f"- wiederverwendetes Archiv: `{_relative(phase_archive)}`",
        "- acht unveränderte Rollenfamilien mit zusammen 29 Mitgliedern",
        "- Komponenten: Körpervorzeichen, absolute Körpergröße, Dochtpaar und Volumen",
        "- feste zirkuläre Offsets: `17`, `83` und `251` Beobachtungen",
        "- Primärachsen: Kontinuität, Ereignisanteil und Mitgliederabdeckung",
        "- direkte Paarprüfung je Familie, Fenster, Komponente und Offset",
        "- keine neue Klasse, keine Handlung, kein Gate und keine Richtung",
        "",
        "Eine Komponente gilt im gebündelten Profil nur dann als verstärkt oder abgeschwächt, wenn alle drei Primärachsen gleichgerichtet über beziehungsweise unter Real liegen. Gemischte Achsen bleiben ausdrücklich offen.",
        "",
        "## Gebündelte Komponentenprofile",
        "",
        "Differenzen sind Kontrolle minus Real. Jede Zeile bündelt `36` Kontrollwelten und `36` direkte Paare.",
        "",
        "| Familie | Komponente | Δ Kontinuität | Δ Ereignisanteil | Δ Abdeckung | Profil | gemeinsam Real höher |",
        "|---|---|---:|---:|---:|---|---:|",
    ]
    for role_family in ROLE_FAMILIES:
        for component in COMPONENTS:
            row = next(
                item
                for item in pooled
                if item["role_family"] == role_family and item["component"] == component
            )
            lines.append(
                f"| `{role_family}` | `{component}` | "
                f"{_fmt(row['control_minus_real_family_continuity_score'])} | "
                f"{_fmt(row['control_minus_real_mean_family_event_share'], 4)} | "
                f"{_fmt(row['control_minus_real_mean_member_coverage'])} | "
                f"`{_relation(row)}` | "
                f"{row['paired_joint_real_advantage']}/{row['paired_windows']} |"
            )

    lines.extend(
        [
            "",
            "## Familienprofile",
            "",
            "| Familie | sign | magnitude | wick | volume | Einzelbedingungen verstärkt/abgeschwächt |",
            "|---|---|---|---|---|---:|",
        ]
    )
    for row in profiles:
        lines.append(
            f"| `{row['role_family']}` | `{row['sign_relation']}` | "
            f"`{row['magnitude_relation']}` | `{row['wick_relation']}` | "
            f"`{row['volume_relation']}` | "
            f"{row['exact_strengthened_conditions']}/{row['exact_weakened_conditions']} |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"Das gebündelte Profil von `rf_05` lautet `{rf05['component_signature']}`. Dasselbe vollständige Vier-Komponenten-Profil tragen weitere Familien: `{';'.join(same_signature) or '-'}`.",
            "",
            f"Dieselbe Kombination aus Vorzeichen- und Volumenreaktion wie `rf_05` tragen: `{';'.join(same_sign_volume) or '-'}`.",
            "",
            f"Damit ist die 2076-Asymmetrie innerhalb dieses Kontrollraums nicht als allgemeine Eigenschaft des Feldlesers reproduziert. `rf_05` zeigt eine selektive Antwortform mit `{rf05['exact_strengthened_conditions']}` verstärkten und `{rf05['exact_weakened_conditions']}` abgeschwächten Einzelbedingungen. Der schwächere Vorzeichenpol bleibt jedoch schmal: Real liegt dort nur in `{rf05_sign['paired_joint_real_advantage']}/{rf05_sign['paired_windows']}` Paaren gleichzeitig bei Ereignisanteil und Abdeckung vorn.",
            "",
            f"Die übrigen Familien bilden deutlich andere Antwortformen. `rf_08` wird gebündelt bei allen vier Komponenten verstärkt und in `{rf08['exact_strengthened_conditions']}/12` Einzelbedingungen gleichgerichtet verstärkt. `rf_10` wird bei allen vier Komponenten und in `{rf10['exact_weakened_conditions']}/12` Einzelbedingungen abgeschwächt. `rf_17` teilt das gebündelte Abschwächungsprofil, trägt es aber nur in `{rf17['exact_weakened_conditions']}/12` Einzelbedingungen; `rf_07` bleibt mit `{rf07['component_signature']}` vollständig achsengemischt.",
            "",
            "Der tragfähige Befund ist daher keine Komponentenbedeutung, sondern eine familienabhängige Phasen-Antworttopologie: Rollenfamilien reagieren verschieden darauf, dass Eigenzeit erhalten und relative Kopplung gelöst wird. Diese Antwortformen sind passive Forschungsevidenz. Sie werden weder als Bedeutungsetikett noch als neue Runtime-Regel gespeichert.",
            "",
            "Eine organische Erweiterung ist noch nicht begründet. Dafür müsste dieselbe Familienindividualität in unabhängigen Welten wiederkehren und gegenüber gemeinsamer Messgeometrie bestehen.",
            "",
            "## Grenze",
            "",
            "Alle Familien werden auf denselben Marktfenstern und denselben rekonstruierten Phasenkontrollen gelesen. Gemeinsame Profile können daher sowohl aus geteilter Feldorganisation als auch aus gemeinsamer Messgeometrie entstehen. Der Lauf prüft Spezifität innerhalb dieses Kontrollraums, nicht Kausalität, feste Semantik oder Übertragbarkeit auf andere Sinnesmodalitäten.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Vergleicht Phasenprofile aller Rollenfamilien.")
    parser.add_argument("--memory", default=str(DEFAULT_MEMORY))
    parser.add_argument("--cohesion-detail", default=str(DEFAULT_COHESION))
    parser.add_argument("--base-data-dir", default=str(BASE_DATA_DIR))
    parser.add_argument("--base-debug-root", default=str(BASE_DEBUG_ROOT))
    parser.add_argument("--phase-data-dir", default=str(PHASE_DATA_DIR))
    parser.add_argument("--phase-debug-root", default=str(PHASE_DEBUG_ROOT))
    parser.add_argument("--phase-archive", default=str(PHASE_ARCHIVE))
    parser.add_argument("--out-prefix", default=str(DEFAULT_OUT_PREFIX))
    args = parser.parse_args()

    memory = _resolve(args.memory)
    cohesion = _resolve(args.cohesion_detail)
    base_data_dir = _resolve(args.base_data_dir)
    base_debug_root = _resolve(args.base_debug_root)
    phase_data_dir = _resolve(args.phase_data_dir)
    phase_debug_root = _resolve(args.phase_debug_root)
    phase_archive = _resolve(args.phase_archive)
    out_prefix = _resolve(args.out_prefix)

    if not phase_archive.exists():
        raise FileNotFoundError(phase_archive)
    targets = _load_targets(memory, list(ROLE_FAMILIES))
    source_counts = _load_source_member_counts(cohesion, targets)
    base_records = _build_world_records(base_data_dir)
    real_records = [record for record in base_records if record["kind"] == "real"]
    phase_records = _build_phase_records(real_records, phase_data_dir)

    real_members = _run_worlds(real_records, targets, base_debug_root)
    phase_members = _run_worlds(phase_records, targets, phase_debug_root)
    member_rows = real_members + phase_members
    world_rows = _build_world_rows(member_rows)
    paired_rows = _build_paired(world_rows)
    comparisons = _build_comparisons(member_rows, targets, source_counts, paired_rows)
    profiles = _build_family_profiles(comparisons)

    _write_csv(out_prefix.with_suffix(".worlds.csv"), world_rows)
    _write_csv(out_prefix.with_suffix(".paired.csv"), paired_rows)
    _write_csv(out_prefix.with_suffix(".comparison.csv"), comparisons)
    _write_csv(out_prefix.with_suffix(".profiles.csv"), profiles)
    _write_markdown(out_prefix.with_suffix(".md"), comparisons, profiles, phase_archive)

    print(f"families={len(targets)}")
    print(f"worlds={len(real_records) + len(phase_records)}")
    print(f"world_rows={len(world_rows)}")
    print(f"paired_rows={len(paired_rows)}")
    print(f"comparison_rows={len(comparisons)}")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
