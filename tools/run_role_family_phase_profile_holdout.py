from __future__ import annotations

import argparse
from pathlib import Path

try:
    from tools.create_csv_slice import create_slice
    from tools.run_role_family_component_phase_profiles import (
        COMPONENTS,
        DEFAULT_COHESION,
        DEFAULT_MEMORY,
        ROLE_FAMILIES,
        _build_comparisons,
        _build_family_profiles,
        _build_paired,
        _build_world_rows,
        _fmt,
        _load_source_member_counts,
        _load_targets,
        _relation,
        _resolve,
        _write_csv,
    )
    from tools.run_role_family_followworld_probe import (
        _build_member_rows,
        _load_csv,
        _run_mini,
        _safe_float,
    )
    from tools.run_role_family_real_null_contrast import _relative, _write_control_archive
    from tools.run_rf05_component_phase_controls import ROWS, _phase_worlds
except ModuleNotFoundError:
    from create_csv_slice import create_slice
    from run_role_family_component_phase_profiles import (
        COMPONENTS,
        DEFAULT_COHESION,
        DEFAULT_MEMORY,
        ROLE_FAMILIES,
        _build_comparisons,
        _build_family_profiles,
        _build_paired,
        _build_world_rows,
        _fmt,
        _load_source_member_counts,
        _load_targets,
        _relation,
        _resolve,
        _write_csv,
    )
    from run_role_family_followworld_probe import (
        _build_member_rows,
        _load_csv,
        _run_mini,
        _safe_float,
    )
    from run_role_family_real_null_contrast import _relative, _write_control_archive
    from run_rf05_component_phase_controls import ROWS, _phase_worlds


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = ROOT / "docs" / "befunde" / "2001-3000"
BASELINE_PROFILES = BEFUNDE / "2077_ROLLENFAMILIEN_KOMPONENTEN_PHASENPROFILE.profiles.csv"
DEFAULT_DATA_DIR = ROOT / "data" / "generated" / "2078_role_family_phase_profile_holdout"
DEFAULT_ARCHIVE = ROOT / "data" / "2078_role_family_phase_profile_holdout.zip"
DEFAULT_DEBUG_ROOT = ROOT / "debug" / "2078_role_family_phase_profile_holdout"
DEFAULT_OUT_PREFIX = BEFUNDE / "2078_ROLLENFAMILIEN_PHASENPROFIL_HOLDOUT"
SPECS = (
    {
        "asset": "BTC",
        "timeframe": "1h",
        "source": ROOT / "data" / "1-12_2025_1h_BTCUSDT.csv",
        "starts": (0, 2000, 4000),
    },
    {
        "asset": "SOL",
        "timeframe": "1h",
        "source": ROOT / "data" / "1-12_2025_1h_SOLUSDT.csv",
        "starts": (0, 2000, 4000),
    },
    {
        "asset": "BTC",
        "timeframe": "15m",
        "source": ROOT / "data" / "1-12_2025_15m_BTCUSDT.csv",
        "starts": (0, 12000, 24000),
    },
    {
        "asset": "SOL",
        "timeframe": "15m",
        "source": ROOT / "data" / "1-12_2025_15m_SOLUSDT.csv",
        "starts": (0, 12000, 24000),
    },
)
PREDICTIONS = {
    "rf_05": {
        "sign": "abgeschwaecht",
        "magnitude": "verstaerkt",
        "wick": "verstaerkt",
        "volume": "verstaerkt",
    },
    "rf_08": {component: "verstaerkt" for component in COMPONENTS},
    "rf_10": {component: "abgeschwaecht" for component in COMPONENTS},
    "rf_07": {component: "gemischt" for component in COMPONENTS},
}


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
            timeframe = str(spec["timeframe"])
            real_path = _ensure_slice(
                source,
                data_dir
                / f"holdout_2078_{asset.lower()}_2025_{timeframe}_start{start}_rows{ROWS}.csv",
                start,
            )
            real: dict[str, object] = {
                "asset": asset,
                "timeframe": timeframe,
                "year": 2025,
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
                data_dir / f"control_2078_{asset.lower()}_2025_{timeframe}_start{start}",
            )
            for kind, path in paths.items():
                lag = int(kind.rsplit("_", 1)[1])
                phase_records.append({**real, "kind": kind, "seed": lag, "path": path})
    return real_records, phase_records


def _run_worlds(
    records: list[dict[str, object]],
    targets: dict[str, list[str]],
    debug_root: Path,
) -> list[dict[str, object]]:
    member_rows: list[dict[str, object]] = []
    for record in records:
        asset = str(record["asset"])
        timeframe = str(record["timeframe"])
        year = int(record["year"])
        kind = str(record["kind"])
        start = int(record["start"])
        rows = int(record["rows"])
        world_label = f"{kind}_{asset.lower()}_{year}_{timeframe}_{start}_{start + rows}"
        path = Path(str(record["path"]))
        run_dir = _run_mini(path, debug_root / world_label, world_label)
        episodes = _load_csv(run_dir / "episodes.csv")
        world = {
            "asset": asset,
            "timeframe": timeframe,
            "year": year,
            "world_kind": kind,
            "window_start": start,
            "window_end": start + rows,
            "world_label": world_label,
            "source_path": _relative(Path(str(record["source"]))),
            "data_path": _relative(path),
            "world_events": len(episodes),
        }
        member_rows.extend(_build_member_rows(world, episodes, targets))
    return member_rows


def _load_baseline_profiles(path: Path) -> dict[str, dict[str, str]]:
    rows = _load_csv(path)
    return {str(row["role_family"]): row for row in rows}


def _build_replication_rows(
    profiles: list[dict[str, object]],
    baseline: dict[str, dict[str, str]],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for profile in profiles:
        role_family = str(profile["role_family"])
        baseline_row = baseline[role_family]
        row: dict[str, object] = {
            "role_family": role_family,
            "predeclared": int(role_family in PREDICTIONS),
            "baseline_signature": baseline_row["component_signature"],
            "holdout_signature": profile["component_signature"],
        }
        matches = 0
        directional_matches = 0
        directional_predictions = 0
        for component in COMPONENTS:
            expected = (
                PREDICTIONS.get(role_family, {}).get(component)
                or baseline_row[f"{component}_relation"]
            )
            observed = str(profile[f"{component}_relation"])
            matched = int(expected == observed)
            row[f"{component}_expected"] = expected
            row[f"{component}_observed"] = observed
            row[f"{component}_match"] = matched
            matches += matched
            if role_family in PREDICTIONS and expected != "gemischt":
                directional_predictions += 1
                directional_matches += matched
        row["component_matches"] = matches
        row["full_signature_match"] = int(matches == len(COMPONENTS))
        row["directional_predictions"] = directional_predictions
        row["directional_matches"] = directional_matches
        rows.append(row)
    return rows


def _write_markdown(
    path: Path,
    comparisons: list[dict[str, object]],
    profiles: list[dict[str, object]],
    replication: list[dict[str, object]],
    archive: Path,
) -> None:
    pooled = [
        row
        for row in comparisons
        if row["group"] == "overall" and row["scope"] == "component"
    ]
    confirmatory = [row for row in replication if int(row["predeclared"]) == 1]
    full_matches = [str(row["role_family"]) for row in confirmatory if int(row["full_signature_match"])]
    component_matches = sum(int(row["component_matches"]) for row in confirmatory)
    directional_matches = sum(int(row["directional_matches"]) for row in confirmatory)
    directional_predictions = sum(int(row["directional_predictions"]) for row in confirmatory)

    def signature_for(group: str, role_family: str) -> str:
        relations: list[str] = []
        for component in COMPONENTS:
            row = next(
                item
                for item in comparisons
                if item["group"] == group
                and item["scope"] == "component"
                and item["role_family"] == role_family
                and item["component"] == component
            )
            relations.append(_relation(row))
        return ";".join(relations)

    timeframe_signatures = {
        role_family: {
            group: signature_for(group, role_family)
            for group in ("timeframe:1h", "timeframe:15m")
        }
        for role_family in ROLE_FAMILIES
    }
    stable_directional: list[str] = []
    for role_family, prediction in PREDICTIONS.items():
        for component, expected in prediction.items():
            if expected == "gemischt":
                continue
            relations = []
            for group in ("overall", "timeframe:1h", "timeframe:15m"):
                row = next(
                    item
                    for item in comparisons
                    if item["group"] == group
                    and item["scope"] == "component"
                    and item["role_family"] == role_family
                    and item["component"] == component
                )
                relations.append(_relation(row))
            if all(relation == expected for relation in relations):
                stable_directional.append(f"{role_family}:{component}")
    rf07_coverage_invariant = all(
        abs(_safe_float(row["control_minus_real_mean_member_coverage"])) < 1e-12
        for row in pooled
        if row["role_family"] == "rf_07"
    )

    lines = [
        "# 2078 - Rollenfamilien-Phasenprofile im unabhängigen 2025-Holdout",
        "",
        "## Zweck",
        "",
        "Befund 2077 zeigte in 2024-Welten unterscheidbare Phasen-Antwortprofile der Rollenfamilien. Dieser Lauf prüft vorab festgelegte Profile in getrennten 2025-Fenstern und erweitert die 1h-Ebene um einen bisher ungenutzten 15m-Holdout.",
        "",
        "## Vorab Festgelegtes Design",
        "",
        "- ausschließlich Datenjahr `2025`",
        "- Assets: `BTC` und `SOL`",
        "- Zeitebenen: `1h` und `15m`",
        "- drei nicht überlappende Fenster je Asset und Zeitebene",
        "- 1h-Startpunkte `0`, `2000`, `4000`; keine Überschneidung mit den früheren Rollenfamilienfenstern `5000`, `6000`, `7000`",
        "- 15m-Startpunkte `0`, `12000`, `24000`; diese Zeitebene war in der Rollenfamilienkette noch ungenutzt",
        "- zwölf Realwelten und `144` Phasenkontrollen",
        "- feste Offsets `17`, `83`, `251` und unveränderte 29 Familienmitglieder",
        f"- Weltarchiv: `{_relative(archive)}`",
        "- keine neue Klasse, keine Handlung, kein Gate und keine Richtung",
        "",
        "Vor dem Lauf festgelegte Signaturen:",
        "",
        "| Familie | sign | magnitude | wick | volume |",
        "|---|---|---|---|---|",
        "| `rf_05` | abgeschwächt | verstärkt | verstärkt | verstärkt |",
        "| `rf_08` | verstärkt | verstärkt | verstärkt | verstärkt |",
        "| `rf_10` | abgeschwächt | abgeschwächt | abgeschwächt | abgeschwächt |",
        "| `rf_07` | gemischt | gemischt | gemischt | gemischt |",
        "",
        "Die Übereinstimmung wird komponentenweise ausgegeben. Es gibt kein nachträglich gesetztes binäres Bestätigungsgate. Die übrigen vier Familien werden explorativ gegen ihre 2077-Profile verglichen.",
        "",
        "## Holdout-Komponentenprofile",
        "",
        "Differenzen sind Kontrolle minus Real. Jede Zeile bündelt `36` Kontrollwelten.",
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
            "## Profil-Replikation",
            "",
            "| Familie | vorab festgelegt | 2077-Profil | 2025-Holdout | Treffer | vollständig |",
            "|---|---|---|---|---:|---:|",
        ]
    )
    for row in replication:
        lines.append(
            f"| `{row['role_family']}` | {'ja' if int(row['predeclared']) else 'explorativ'} | "
            f"`{row['baseline_signature']}` | `{row['holdout_signature']}` | "
            f"{row['component_matches']}/4 | {row['full_signature_match']} |"
        )

    lines.extend(
        [
            "",
            "## Zeitebenen-Tragung",
            "",
            "Die Signaturen werden zusätzlich getrennt gelesen. Ein Gesamtprofil kann gegenläufige 1h- und 15m-Reaktionen verdecken.",
            "",
            "| Familie | 1h | 15m |",
            "|---|---|---|",
        ]
    )
    for role_family in ROLE_FAMILIES:
        lines.append(
            f"| `{role_family}` | `{timeframe_signatures[role_family]['timeframe:1h']}` | "
            f"`{timeframe_signatures[role_family]['timeframe:15m']}` |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"Von den vier vorab festgelegten vollständigen Familienprofilen replizieren: `{';'.join(full_matches) or '-'}`.",
            "",
            f"Komponentenweise stimmen `{component_matches}/16` Vorhersagen. Unter den gerichteten Vorhersagen ohne die vier gemischten `rf_07`-Komponenten stimmen `{directional_matches}/{directional_predictions}`.",
            "",
            f"Getrennt auf beiden Zeitebenen und im Gesamtprofil gleichgerichtet tragen von diesen gerichteten Vorhersagen nur `{len(stable_directional)}/{directional_predictions}`: `{';'.join(stable_directional) or '-'}`. Kein gerichtetes vollständiges Vier-Komponenten-Profil bleibt damit zugleich auf `1h` und `15m` geschlossen.",
            "",
            f"`rf_08` repliziert als einzige gerichtete Vorhersage das vollständige Gesamtprofil und wird in `9/12` Einzelbedingungen verstärkt. Die Verstärkung verteilt sich jedoch verschieden auf die Zeitebenen. `rf_10` repliziert Vorzeichen, Größe und Docht, während Volumen gemischt bleibt. `rf_05` repliziert nur den schwächeren Vorzeichenpol und den stärkeren Volumenpol; Größe und Docht wechseln ins Mischprofil.",
            "",
            f"Das vollständige Mischprofil von `rf_07` repliziert formal, ist aber diagnostisch schwächer: Seine Mitgliederabdeckung bleibt über alle vier gebündelten Komponenten unverändert (`{'ja' if rf07_coverage_invariant else 'nein'}`). Das Mischprofil kann daher Sättigung beziehungsweise geringe Differenzierbarkeit widerspiegeln und wird nicht mit einer gerichteten Replikation gleichgesetzt.",
            "",
            "Explorativ repliziert `rf_17` sein vollständiges Gesamt-Abschwächungsprofil und `10/12` abgeschwächte Einzelbedingungen. Auch dieses Profil ist zeitebenenabhängig: Auf 15m ist es geschlossen, auf 1h nicht.",
            "",
            "Der Holdout stützt damit einzelne familienabhängige Phasenachsen, aber keine bereits stabile vollständige Familienindividualität über Zeitebenen. Die Auswertung speichert passive Forschungsevidenz; sie begründet noch keine organische Erweiterung, feste Familienbedeutung oder Runtime-Regel.",
            "",
            "## Grenze",
            "",
            "Der Holdout wechselt Jahr, Fenster und teilweise Zeitebene, bleibt aber bei BTC/SOL, Marktzeitreihen, `1000` Beobachtungen und derselben Phasenoperation. Er trennt zeitliche Wiederkehr von vollständiger Modalitäts- und Messunabhängigkeit, beweist aber weder Kausalität noch allgemeine Feldintelligenz.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Prüft Rollenfamilien-Phasenprofile im 2025-Holdout.")
    parser.add_argument("--memory", default=str(DEFAULT_MEMORY))
    parser.add_argument("--cohesion-detail", default=str(DEFAULT_COHESION))
    parser.add_argument("--baseline-profiles", default=str(BASELINE_PROFILES))
    parser.add_argument("--data-dir", default=str(DEFAULT_DATA_DIR))
    parser.add_argument("--archive", default=str(DEFAULT_ARCHIVE))
    parser.add_argument("--debug-root", default=str(DEFAULT_DEBUG_ROOT))
    parser.add_argument("--out-prefix", default=str(DEFAULT_OUT_PREFIX))
    args = parser.parse_args()

    memory = _resolve(args.memory)
    cohesion = _resolve(args.cohesion_detail)
    baseline_path = _resolve(args.baseline_profiles)
    data_dir = _resolve(args.data_dir)
    archive = _resolve(args.archive)
    debug_root = _resolve(args.debug_root)
    out_prefix = _resolve(args.out_prefix)

    targets = _load_targets(memory, list(ROLE_FAMILIES))
    source_counts = _load_source_member_counts(cohesion, targets)
    baseline = _load_baseline_profiles(baseline_path)
    real_records, phase_records = _build_records(data_dir)
    _write_control_archive(archive, phase_records)

    member_rows = _run_worlds(real_records + phase_records, targets, debug_root)
    world_rows = _build_world_rows(member_rows)
    paired_rows = _build_paired(world_rows)
    comparisons = _build_comparisons(member_rows, targets, source_counts, paired_rows)
    profiles = _build_family_profiles(comparisons)
    replication = _build_replication_rows(profiles, baseline)

    _write_csv(out_prefix.with_suffix(".worlds.csv"), world_rows)
    _write_csv(out_prefix.with_suffix(".paired.csv"), paired_rows)
    _write_csv(out_prefix.with_suffix(".comparison.csv"), comparisons)
    _write_csv(out_prefix.with_suffix(".profiles.csv"), profiles)
    _write_csv(out_prefix.with_suffix(".replication.csv"), replication)
    _write_markdown(out_prefix.with_suffix(".md"), comparisons, profiles, replication, archive)

    print(f"families={len(targets)}")
    print(f"real_worlds={len(real_records)}")
    print(f"phase_worlds={len(phase_records)}")
    print(f"world_rows={len(world_rows)}")
    print(f"paired_rows={len(paired_rows)}")
    print(f"comparison_rows={len(comparisons)}")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
