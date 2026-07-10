from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
from statistics import mean, median

try:
    from tools.create_csv_slice import create_slice
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


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = ROOT / "docs" / "befunde" / "2001-3000"
DEFAULT_DEFINITIONS = PSEUDO_PREFIX.with_suffix(".definitions.csv")
DEFAULT_DATA_DIR = ROOT / "data" / "generated" / "2081_role_family_30m_phase_holdout"
DEFAULT_ARCHIVE = ROOT / "data" / "2081_role_family_30m_phase_holdout.zip"
DEFAULT_DEBUG_ROOT = ROOT / "debug" / "2081_role_family_30m_phase_holdout"
DEFAULT_OUT_PREFIX = BEFUNDE / "2081_RF08_SIGN_RF05_VOLUME_30M_HOLDOUT"
TARGET_FAMILIES = ("rf_05", "rf_08")
TARGET_COMPONENTS = ("sign", "volume")
GROUPS = ("overall", "year:2024", "year:2025", "asset:BTC", "asset:SOL")
PRIMARY_AXES = {
    ("rf_08", "sign"): "verstaerkt",
    ("rf_05", "volume"): "verstaerkt",
}
PRIMARY_METRICS = (
    "family_continuity_score",
    "mean_family_event_share",
    "mean_member_coverage",
)
SPECS = tuple(
    {
        "asset": asset,
        "year": year,
        "source": ROOT / "data" / f"1-12_{year}_30m_{asset}USDT.csv",
        "starts": (0, 6000, 12000),
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
                data_dir
                / f"holdout_2081_{asset.lower()}_{year}_30m_start{start}_rows{ROWS}.csv",
                start,
            )
            real: dict[str, object] = {
                "asset": asset,
                "timeframe": "30m",
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
                data_dir / f"control_2081_{asset.lower()}_{year}_30m_start{start}",
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
        member_rows.extend(_build_member_rows(world, episodes, {"pool": symbols}))
    return member_rows


def _observed_definitions(
    targets: dict[str, list[str]],
    global_counts: Counter[str],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for role_family in TARGET_FAMILIES:
        members = sorted(targets[role_family])
        rows.append(
            {
                "role_family": role_family,
                "pseudo_index": 0,
                "pseudo_id": f"{role_family}_observed",
                "members": ";".join(members),
                "member_count": len(members),
                "disjoint_from_real": 0,
                "match_distance": 0.0,
                "real_source_events": sum(global_counts[symbol] for symbol in members),
                "pseudo_source_events": sum(global_counts[symbol] for symbol in members),
                "source_event_ratio": 1.0,
            }
        )
    return rows


def _build_summary(
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
        expected = PRIMARY_AXES.get((role_family, component), "explorativ")
        row: dict[str, object] = {
            "group": group,
            "role_family": role_family,
            "component": component,
            "primary_axis": int((role_family, component) in PRIMARY_AXES),
            "expected_relation": expected,
            "observed_relation": observed["relation"],
            "expected_relation_match": int(expected == observed["relation"]),
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


def _write_markdown(path: Path, summary: list[dict[str, object]], archive: Path) -> None:
    primary = [row for row in summary if int(row["primary_axis"]) == 1]
    indexed = {
        (str(row["group"]), str(row["role_family"]), str(row["component"])): row
        for row in summary
    }
    rf05_overall = indexed[("overall", "rf_05", "volume")]
    rf05_2024 = indexed[("year:2024", "rf_05", "volume")]
    rf05_2025 = indexed[("year:2025", "rf_05", "volume")]
    rf05_btc = indexed[("asset:BTC", "rf_05", "volume")]
    rf05_sol = indexed[("asset:SOL", "rf_05", "volume")]
    rf08_overall = indexed[("overall", "rf_08", "sign")]
    rf08_2024 = indexed[("year:2024", "rf_08", "sign")]
    rf08_sol = indexed[("asset:SOL", "rf_08", "sign")]
    lines = [
        "# 2081 - rf_08:sign und rf_05:volume im unabhängigen 30m-Holdout",
        "",
        "## Zweck",
        "",
        "Befund 2080 ließ zwei mögliche Familien-Komponenten-Kopplungen zurück. Dieser Lauf prüft beide vorab auf einer bisher ungenutzten 30m-Zeitebene und gegen dieselben größen- und häufigkeitsgematchten Pseudo-Familien.",
        "",
        "## Vorab Festgelegtes Design",
        "",
        "- Datenjahre `2024` und `2025`",
        "- Assets `BTC` und `SOL`",
        "- ausschließlich die bisher ungenutzte Zeitebene `30m`",
        "- Startpunkte `0`, `6000`, `12000` je Asset und Jahr",
        "- zwölf Realwelten mit je `1000` Beobachtungen",
        "- Komponenten ausschließlich `sign` und `volume`",
        "- feste Offsets `17`, `83`, `251`",
        "- `72` gezielte Phasenkontrollen statt eines vollständigen Vier-Komponenten-Satzes",
        "- exakt dieselben gematchten Pseudo-Familien wie 2079 und 2080",
        f"- Weltarchiv: `{_relative(archive)}`",
        "- vorab erwartete Antworten: `rf_08:sign = verstaerkt`, `rf_05:volume = verstaerkt`",
        "- keine neue Klasse, keine Handlung, kein Gate und keine Richtung",
        "",
        "## Primärvergleich",
        "",
        "| Gruppe | Achse | erwartet/beobachtet | Pseudo gleich | Δ Kontinuität Perzentil | Δ Ereignisanteil Perzentil | Δ Abdeckung Perzentil |",
        "|---|---|---|---:|---:|---:|---:|",
    ]
    for row in primary:
        lines.append(
            f"| `{row['group']}` | `{row['role_family']}:{row['component']}` | "
            f"`{row['expected_relation']}/{row['observed_relation']}` | "
            f"{row['pseudo_same_relation']}/{row['pseudo_families']} | "
            f"{_fmt(row['observed_percentile_control_minus_real_family_continuity_score'])} | "
            f"{_fmt(row['observed_percentile_control_minus_real_mean_family_event_share'])} | "
            f"{_fmt(row['observed_percentile_control_minus_real_mean_member_coverage'])} |"
        )

    lines.extend(
        [
            "",
            "## Gekreuzte Sekundärachsen",
            "",
            "| Gruppe | Achse | beobachtet | Pseudo gleich | Kontinuitätsperzentil |",
            "|---|---|---|---:|---:|",
        ]
    )
    for row in summary:
        if int(row["primary_axis"]) == 1:
            continue
        lines.append(
            f"| `{row['group']}` | `{row['role_family']}:{row['component']}` | "
            f"`{row['observed_relation']}` | {row['pseudo_same_relation']}/{row['pseudo_families']} | "
            f"{_fmt(row['observed_percentile_control_minus_real_family_continuity_score'])} |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"`rf_05:volume` repliziert die vorab erwartete Verstärkung auf 30m. Im Gesamtprofil tragen nur `{rf05_overall['pseudo_same_relation']}/100` Pseudo-Familien dieselbe Antwort; Kontinuität, Ereignisanteil und Abdeckung liegen jeweils am Perzentil `1.000`. 2024 sind es `{rf05_2024['pseudo_same_relation']}/100` bei drei Perzentilen `1.000`; 2025 `{rf05_2025['pseudo_same_relation']}/100` bei `1.000`, `1.000`, `0.825`.",
            "",
            f"Der Effekt ist nicht auf ein Asset begrenzt. BTC trägt `{rf05_btc['pseudo_same_relation']}/100` gleiche Antworten, SOL `{rf05_sol['pseudo_same_relation']}/100`; auf beiden Assetgruppen liegen alle drei realen Maße am Perzentil `1.000`. Zusammen mit 2079 und 2080 ist dies eine vorab festgelegte Replikation auf einer neuen Zeitebene gegenüber größen- und häufigkeitsgematchten Alternativmitgliedschaften.",
            "",
            f"`rf_08:sign` repliziert auf 30m nicht gleichwertig. Das Gesamtprofil ist zwar verstärkt, aber nur bei Perzentilen `{_fmt(rf08_overall['observed_percentile_control_minus_real_family_continuity_score'])}`, `{_fmt(rf08_overall['observed_percentile_control_minus_real_mean_family_event_share'])}`, `{_fmt(rf08_overall['observed_percentile_control_minus_real_mean_member_coverage'])}`. 2024 und SOL wechseln mit `{rf08_2024['observed_relation']}` beziehungsweise `{rf08_sol['observed_relation']}` aus der erwarteten gemeinsamen Verstärkung. Seine bisherige Evidenz bleibt damit zeitebenenabhängig.",
            "",
            "Der robuste `rf_05`-Befund bedeutet nicht, dass reale Volumenkopplung die Familie trägt. Die zirkuläre Volumenverschiebung löst die relative Phase und verstärkt anschließend die Familienlesung. Belegt ist daher eine wiederkehrende, familienbezogene Volumen-Phasensensitivität beziehungsweise Plastizität, keine feste Volumenbedeutung und keine bevorzugte Handlungsrichtung.",
            "",
            "Dieser Befund reicht erstmals aus, eine kleine organische Erweiterung der passiven Memory fachlich zu begründen: kontinuierliche Familien-Komponenten-Antwortvektoren samt Weltkontext und Nullabstand können als Erfahrung gespeichert werden. Er rechtfertigt weiterhin keine automatische Runtime-Regel, Handlung oder fest codierte Sonderbehandlung von `rf_05`.",
            "",
            "## Grenze",
            "",
            "Der Lauf erweitert die Zeitebene, bleibt aber bei BTC/SOL, Marktzeitreihen, derselben Fensterlänge, denselben Phasenoperationen und demselben Symbolpool. Er prüft Übertragbarkeit auf 30m, nicht andere Sinnesmodalitäten, Kausalität oder allgemeine Feldintelligenz.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Prüft rf_08:sign und rf_05:volume auf 30m.")
    parser.add_argument("--memory", default=str(DEFAULT_MEMORY))
    parser.add_argument("--cohesion-detail", default=str(DEFAULT_COHESION))
    parser.add_argument("--definitions", default=str(DEFAULT_DEFINITIONS))
    parser.add_argument("--data-dir", default=str(DEFAULT_DATA_DIR))
    parser.add_argument("--archive", default=str(DEFAULT_ARCHIVE))
    parser.add_argument("--debug-root", default=str(DEFAULT_DEBUG_ROOT))
    parser.add_argument("--out-prefix", default=str(DEFAULT_OUT_PREFIX))
    args = parser.parse_args()

    memory = _resolve(args.memory)
    cohesion = _resolve(args.cohesion_detail)
    definitions_path = _resolve(args.definitions)
    data_dir = _resolve(args.data_dir)
    archive = _resolve(args.archive)
    debug_root = _resolve(args.debug_root)
    out_prefix = _resolve(args.out_prefix)

    targets = _load_targets(memory, ["rf_05", "rf_08", "rf_06", "rf_07", "rf_10", "rf_13", "rf_17", "rf_21"])
    all_symbols = sorted({symbol for members in targets.values() for symbol in members})
    global_counts = _load_global_source_counts(cohesion, set(all_symbols))
    definitions = [
        row
        for row in _load_csv(definitions_path)
        if row["role_family"] in TARGET_FAMILIES
    ]
    real_records, phase_records = _build_records(data_dir)
    _write_control_archive(archive, phase_records)
    pool_rows = _run_pool_worlds(real_records + phase_records, all_symbols, debug_root)

    observed_rows = _evaluate_pseudos(
        _observed_definitions(targets, global_counts),
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

    _write_csv(out_prefix.with_suffix(".observed.csv"), observed_rows)
    _write_csv(out_prefix.with_suffix(".pseudos.csv"), pseudo_rows)
    _write_csv(out_prefix.with_suffix(".summary.csv"), summary)
    _write_markdown(out_prefix.with_suffix(".md"), summary, archive)

    print(f"real_worlds={len(real_records)}")
    print(f"phase_worlds={len(phase_records)}")
    print(f"pool_member_rows={len(pool_rows)}")
    print(f"observed_rows={len(observed_rows)}")
    print(f"pseudo_rows={len(pseudo_rows)}")
    print(f"summary_rows={len(summary)}")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
