from __future__ import annotations

import argparse
import math
from collections import Counter
from heapq import nsmallest
from itertools import combinations
from pathlib import Path
from statistics import mean, median

try:
    from tools.run_role_family_component_phase_profiles import (
        COMPONENTS,
        DEFAULT_COHESION,
        DEFAULT_MEMORY,
        ROLE_FAMILIES,
        _build_world_rows,
        _fmt,
        _load_targets,
        _relation,
        _resolve,
        _write_csv,
    )
    from tools.run_role_family_followworld_probe import (
        _build_family_summary,
        _build_member_rows,
        _load_csv,
        _safe_float,
    )
    from tools.run_role_family_phase_profile_holdout import (
        DEFAULT_ARCHIVE as HOLDOUT_ARCHIVE,
        DEFAULT_DATA_DIR as HOLDOUT_DATA_DIR,
        DEFAULT_DEBUG_ROOT as HOLDOUT_DEBUG_ROOT,
        DEFAULT_OUT_PREFIX as HOLDOUT_OUT_PREFIX,
        _build_records,
    )
    from tools.run_role_family_real_null_contrast import _relative
except ModuleNotFoundError:
    from run_role_family_component_phase_profiles import (
        COMPONENTS,
        DEFAULT_COHESION,
        DEFAULT_MEMORY,
        ROLE_FAMILIES,
        _build_world_rows,
        _fmt,
        _load_targets,
        _relation,
        _resolve,
        _write_csv,
    )
    from run_role_family_followworld_probe import (
        _build_family_summary,
        _build_member_rows,
        _load_csv,
        _safe_float,
    )
    from run_role_family_phase_profile_holdout import (
        DEFAULT_ARCHIVE as HOLDOUT_ARCHIVE,
        DEFAULT_DATA_DIR as HOLDOUT_DATA_DIR,
        DEFAULT_DEBUG_ROOT as HOLDOUT_DEBUG_ROOT,
        DEFAULT_OUT_PREFIX as HOLDOUT_OUT_PREFIX,
        _build_records,
    )
    from run_role_family_real_null_contrast import _relative


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = ROOT / "docs" / "befunde" / "2001-3000"
DEFAULT_OUT_PREFIX = BEFUNDE / "2079_ROLLENFAMILIEN_GEMATCHE_PSEUDOFAMILIEN"
DEFAULT_HOLDOUT_COMPARISON = HOLDOUT_OUT_PREFIX.with_suffix(".comparison.csv")
PSEUDOS_PER_FAMILY = 100
PRIMARY_AXES = (
    ("rf_08", "sign", "verstaerkt"),
    ("rf_10", "sign", "abgeschwaecht"),
    ("rf_10", "magnitude", "abgeschwaecht"),
)
PRIMARY_METRICS = (
    "family_continuity_score",
    "mean_family_event_share",
    "mean_member_coverage",
)
GROUPS = ("overall", "timeframe:1h", "timeframe:15m")


def _load_global_source_counts(path: Path, symbols: set[str]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for row in _load_csv(path):
        symbol = str(row.get("symbol_family", "") or "")
        if symbol in symbols:
            counts[symbol] += int(float(row.get("follow_events", 0) or 0))
    missing = sorted(symbol for symbol in symbols if counts[symbol] <= 0)
    if missing:
        raise ValueError(f"Quellhäufigkeit fehlt: {';'.join(missing)}")
    return counts


def _match_distance(
    target: tuple[str, ...],
    candidate: tuple[str, ...],
    counts: Counter[str],
) -> float:
    target_logs = sorted(math.log1p(counts[symbol]) for symbol in target)
    candidate_logs = sorted(math.log1p(counts[symbol]) for symbol in candidate)
    shape_distance = mean(
        abs(target_value - candidate_value)
        for target_value, candidate_value in zip(target_logs, candidate_logs)
    )
    total_distance = abs(
        math.log1p(sum(counts[symbol] for symbol in target))
        - math.log1p(sum(counts[symbol] for symbol in candidate))
    )
    return shape_distance + total_distance


def _build_matched_definitions(
    targets: dict[str, list[str]],
    counts: Counter[str],
) -> list[dict[str, object]]:
    all_symbols = sorted(counts)
    rows: list[dict[str, object]] = []
    for role_family in ROLE_FAMILIES:
        true_members = tuple(sorted(targets[role_family]))
        eligible = [symbol for symbol in all_symbols if symbol not in true_members]
        scored = (
            (_match_distance(true_members, candidate, counts), candidate)
            for candidate in combinations(eligible, len(true_members))
        )
        selected = nsmallest(PSEUDOS_PER_FAMILY, scored, key=lambda item: (item[0], item[1]))
        if len(selected) != PSEUDOS_PER_FAMILY:
            raise ValueError(
                f"Für {role_family} wurden nur {len(selected)} Pseudo-Familien gefunden"
            )
        true_total = sum(counts[symbol] for symbol in true_members)
        for index, (distance, members) in enumerate(selected, start=1):
            candidate_total = sum(counts[symbol] for symbol in members)
            rows.append(
                {
                    "role_family": role_family,
                    "pseudo_index": index,
                    "pseudo_id": f"{role_family}_pseudo_{index:03d}",
                    "members": ";".join(members),
                    "member_count": len(members),
                    "disjoint_from_real": 1,
                    "match_distance": distance,
                    "real_source_events": true_total,
                    "pseudo_source_events": candidate_total,
                    "source_event_ratio": candidate_total / true_total,
                }
            )
    return rows


def _world_metadata(record: dict[str, object]) -> dict[str, object]:
    asset = str(record["asset"])
    timeframe = str(record["timeframe"])
    year = int(record["year"])
    kind = str(record["kind"])
    start = int(record["start"])
    rows = int(record["rows"])
    world_label = f"{kind}_{asset.lower()}_{year}_{timeframe}_{start}_{start + rows}"
    return {
        "asset": asset,
        "timeframe": timeframe,
        "year": year,
        "world_kind": kind,
        "window_start": start,
        "window_end": start + rows,
        "world_label": world_label,
        "source_path": _relative(Path(str(record["source"]))),
        "data_path": _relative(Path(str(record["path"]))),
    }


def _load_pool_member_rows(
    records: list[dict[str, object]],
    symbols: list[str],
    debug_root: Path,
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for record in records:
        world = _world_metadata(record)
        episode_paths = sorted((debug_root / str(world["world_label"])).glob("*/episodes.csv"))
        if len(episode_paths) != 1:
            raise ValueError(
                f"Erwartet wurde ein Episodenlauf für {world['world_label']}, gefunden {len(episode_paths)}"
            )
        episodes = _load_csv(episode_paths[0])
        world["world_events"] = len(episodes)
        rows.extend(_build_member_rows(world, episodes, {"pool": symbols}))
    return rows


def _summary_for_kind(
    member_rows: list[dict[str, object]],
    world_rows: list[dict[str, object]],
    pseudo_id: str,
    members: list[str],
    source_counts: Counter[str],
    kinds: tuple[str, ...],
    group: str,
) -> dict[str, object]:
    selected_members = [row for row in member_rows if str(row["world_kind"]) in kinds]
    selected_worlds = [row for row in world_rows if str(row["world_kind"]) in kinds]
    if group.startswith("timeframe:"):
        timeframe = group.split(":", 1)[1]
        selected_members = [
            row for row in selected_members if str(row["timeframe"]) == timeframe
        ]
        selected_worlds = [
            row for row in selected_worlds if str(row["timeframe"]) == timeframe
        ]
    elif group.startswith("year:"):
        year = int(group.split(":", 1)[1])
        selected_members = [row for row in selected_members if int(row["year"]) == year]
        selected_worlds = [row for row in selected_worlds if int(row["year"]) == year]
    elif group.startswith("asset:"):
        asset = group.split(":", 1)[1]
        selected_members = [row for row in selected_members if str(row["asset"]) == asset]
        selected_worlds = [row for row in selected_worlds if str(row["asset"]) == asset]
    return _build_family_summary(
        selected_worlds,
        selected_members,
        {pseudo_id: members},
        {pseudo_id: source_counts},
    )[0]


def _evaluate_pseudos(
    definitions: list[dict[str, object]],
    pool_rows: list[dict[str, object]],
    global_counts: Counter[str],
    components: tuple[str, ...] = COMPONENTS,
    groups: tuple[str, ...] = GROUPS,
) -> list[dict[str, object]]:
    by_symbol_world = {
        (str(row["world_label"]), str(row["symbol_family"])): row for row in pool_rows
    }
    world_labels = sorted({str(row["world_label"]) for row in pool_rows})
    rows: list[dict[str, object]] = []
    for definition in definitions:
        pseudo_id = str(definition["pseudo_id"])
        role_family = str(definition["role_family"])
        members = str(definition["members"]).split(";")
        candidate_members: list[dict[str, object]] = []
        for world_label in world_labels:
            for symbol in members:
                source = by_symbol_world[(world_label, symbol)]
                candidate_members.append(
                    {
                        **source,
                        "role_family": pseudo_id,
                        "target_members": len(members),
                    }
                )
        candidate_worlds = _build_world_rows(candidate_members)
        source_counts = Counter({symbol: global_counts[symbol] for symbol in members})
        for group in groups:
            real = _summary_for_kind(
                candidate_members,
                candidate_worlds,
                pseudo_id,
                members,
                source_counts,
                ("real",),
                group,
            )
            for component in components:
                kinds = tuple(
                    f"{component}_phase_{lag:03d}" for lag in (17, 83, 251)
                )
                control = _summary_for_kind(
                    candidate_members,
                    candidate_worlds,
                    pseudo_id,
                    members,
                    source_counts,
                    kinds,
                    group,
                )
                row: dict[str, object] = {
                    "group": group,
                    "role_family": role_family,
                    "pseudo_index": definition["pseudo_index"],
                    "pseudo_id": pseudo_id,
                    "component": component,
                    "members": definition["members"],
                    "match_distance": definition["match_distance"],
                    "source_event_ratio": definition["source_event_ratio"],
                }
                for metric in PRIMARY_METRICS:
                    real_value = _safe_float(real.get(metric))
                    control_value = _safe_float(control.get(metric))
                    row[f"real_{metric}"] = real_value
                    row[f"control_{metric}"] = control_value
                    row[f"control_minus_real_{metric}"] = control_value - real_value
                row["relation"] = _relation(row)
                rows.append(row)
    return rows


def _empirical_percentile(values: list[float], observed: float) -> float:
    lower = sum(value < observed for value in values)
    equal = sum(value == observed for value in values)
    return (lower + 0.5 * equal) / len(values)


def _build_null_summary(
    pseudo_rows: list[dict[str, object]],
    holdout_comparison: Path,
) -> list[dict[str, object]]:
    observed_rows = [
        row for row in _load_csv(holdout_comparison) if row["scope"] == "component"
    ]
    rows: list[dict[str, object]] = []
    for group in GROUPS:
        for role_family in ROLE_FAMILIES:
            for component in COMPONENTS:
                observed = next(
                    row
                    for row in observed_rows
                    if row["group"] == group
                    and row["role_family"] == role_family
                    and row["component"] == component
                )
                pseudos = [
                    row
                    for row in pseudo_rows
                    if row["group"] == group
                    and row["role_family"] == role_family
                    and row["component"] == component
                ]
                observed_relation = _relation(observed)
                row: dict[str, object] = {
                    "group": group,
                    "role_family": role_family,
                    "component": component,
                    "primary_axis": int(
                        any(
                            family == role_family and axis_component == component
                            for family, axis_component, _ in PRIMARY_AXES
                        )
                    ),
                    "observed_relation": observed_relation,
                    "pseudo_same_relation": sum(
                        str(item["relation"]) == observed_relation for item in pseudos
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
                    observed_value = _safe_float(observed.get(field))
                    values = [_safe_float(item.get(field)) for item in pseudos]
                    row[f"observed_{field}"] = observed_value
                    row[f"pseudo_mean_{field}"] = mean(values)
                    row[f"observed_percentile_{field}"] = _empirical_percentile(
                        values, observed_value
                    )
                rows.append(row)
    return rows


def _write_markdown(
    path: Path,
    definitions: list[dict[str, object]],
    summary: list[dict[str, object]],
    holdout_archive: Path,
) -> None:
    primary = [row for row in summary if int(row["primary_axis"]) == 1]
    indexed = {
        (str(row["group"]), str(row["role_family"]), str(row["component"])): row
        for row in summary
    }
    rf08_overall = indexed[("overall", "rf_08", "sign")]
    rf08_1h = indexed[("timeframe:1h", "rf_08", "sign")]
    rf08_15m = indexed[("timeframe:15m", "rf_08", "sign")]
    rf10_sign = indexed[("overall", "rf_10", "sign")]
    rf10_magnitude = indexed[("overall", "rf_10", "magnitude")]
    rf05_volume = indexed[("overall", "rf_05", "volume")]
    rf05_volume_1h = indexed[("timeframe:1h", "rf_05", "volume")]
    lines = [
        "# 2079 - Rollenfamilien gegen größen- und häufigkeitsgematchte Pseudo-Familien",
        "",
        "## Zweck",
        "",
        "Befund 2078 ließ drei gerichtete Phasenachsen über Gesamtprofil, 1h und 15m gleichgerichtet zurück. Dieser Lauf prüft, ob diese Achsen über die konkrete relationale Familienzugehörigkeit hinausgehen oder bereits durch Mitgliederzahl und Quellhäufigkeit entstehen können.",
        "",
        "## Vorab Festgelegtes Design",
        "",
        "- keine neuen Weltläufe und keine neuen Kontrollwelten",
        f"- wiederverwendetes 2025-Holdoutarchiv: `{_relative(holdout_archive)}`",
        "- für jede der acht Familien `100` Pseudo-Familien",
        "- exakt gleiche Mitgliederzahl",
        "- vollständig disjunkt von den Mitgliedern der jeweiligen realen Familie",
        "- deterministische Auswahl der 100 nächstliegenden Quellhäufigkeitsprofile",
        "- Matching über sortierte logarithmische Mitgliedshäufigkeiten und Gesamthäufigkeit",
        "- dieselben zwölf Realwelten und `144` Phasenkontrollen wie in 2078",
        "- Primärachsen aus 2078: `rf_08:sign`, `rf_10:sign`, `rf_10:magnitude`",
        "- keine neue Klasse, keine Handlung, kein Gate und keine Richtung",
        "",
        "Die Nullverteilung wird nicht durch einen festen Grenzwert in bestätigt oder verworfen geteilt. Ausgegeben werden die Lage des realen Effekts innerhalb der 100 gematchten Pseudo-Familien und die Häufigkeit derselben kategorialen Antwort.",
        "",
        "## Matching-Qualität",
        "",
        "| Familie | Mitglieder | mittlere Distanz | Median Häufigkeitsverhältnis |",
        "|---|---:|---:|---:|",
    ]
    for role_family in ROLE_FAMILIES:
        family_definitions = [row for row in definitions if row["role_family"] == role_family]
        lines.append(
            f"| `{role_family}` | {family_definitions[0]['member_count']} | "
            f"{_fmt(mean(_safe_float(row['match_distance']) for row in family_definitions), 4)} | "
            f"{_fmt(median(_safe_float(row['source_event_ratio']) for row in family_definitions), 3)} |"
        )

    lines.extend(
        [
            "",
            "## Primärachsen",
            "",
            "Perzentile geben die Lage des realen Differenzwerts innerhalb der gematchten Pseudo-Familien an.",
            "",
            "| Ebene | Achse | reales Profil | Pseudo gleich | Δ Kontinuität Perzentil | Δ Ereignisanteil Perzentil | Δ Abdeckung Perzentil |",
            "|---|---|---|---:|---:|---:|---:|",
        ]
    )
    for row in primary:
        lines.append(
            f"| `{row['group']}` | `{row['role_family']}:{row['component']}` | `{row['observed_relation']}` | "
            f"{row['pseudo_same_relation']}/{row['pseudo_families']} | "
            f"{_fmt(row['observed_percentile_control_minus_real_family_continuity_score'])} | "
            f"{_fmt(row['observed_percentile_control_minus_real_mean_family_event_share'])} | "
            f"{_fmt(row['observed_percentile_control_minus_real_mean_member_coverage'])} |"
        )

    lines.extend(
        [
            "",
            "## Alle Familienachsen",
            "",
            "| Familie | Komponente | reales Profil | Pseudo gleich | Kontinuitätsperzentil |",
            "|---|---|---|---:|---:|",
        ]
    )
    for row in summary:
        if row["group"] != "overall":
            continue
        lines.append(
            f"| `{row['role_family']}` | `{row['component']}` | `{row['observed_relation']}` | "
            f"{row['pseudo_same_relation']}/{row['pseudo_families']} | "
            f"{_fmt(row['observed_percentile_control_minus_real_family_continuity_score'])} |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"Von den drei vorab festgelegten Achsen bleibt nur `rf_08:sign` im Gesamtprofil gegenüber den gematchten Pseudo-Familien auffällig: dieselbe Verstärkung tragen `{rf08_overall['pseudo_same_relation']}/100`, die drei Primärmaße liegen auf den Perzentilen `{_fmt(rf08_overall['observed_percentile_control_minus_real_family_continuity_score'])}`, `{_fmt(rf08_overall['observed_percentile_control_minus_real_mean_family_event_share'])}` und `{_fmt(rf08_overall['observed_percentile_control_minus_real_mean_member_coverage'])}`.",
            "",
            f"Dieser Abstand ist zeitebenengebunden. Auf `1h` tragen `{rf08_1h['pseudo_same_relation']}/100` Pseudo-Familien dieselbe Antwort und die Perzentile liegen nur zwischen `{_fmt(min(_safe_float(rf08_1h['observed_percentile_control_minus_real_family_continuity_score']), _safe_float(rf08_1h['observed_percentile_control_minus_real_mean_family_event_share']), _safe_float(rf08_1h['observed_percentile_control_minus_real_mean_member_coverage'])))}` und `{_fmt(max(_safe_float(rf08_1h['observed_percentile_control_minus_real_family_continuity_score']), _safe_float(rf08_1h['observed_percentile_control_minus_real_mean_family_event_share']), _safe_float(rf08_1h['observed_percentile_control_minus_real_mean_member_coverage'])))}`. Auf `15m` tragen nur `{rf08_15m['pseudo_same_relation']}/100` dieselbe Verstärkung; alle drei Perzentile liegen zwischen `{_fmt(min(_safe_float(rf08_15m['observed_percentile_control_minus_real_family_continuity_score']), _safe_float(rf08_15m['observed_percentile_control_minus_real_mean_family_event_share']), _safe_float(rf08_15m['observed_percentile_control_minus_real_mean_member_coverage'])))}` und `{_fmt(max(_safe_float(rf08_15m['observed_percentile_control_minus_real_family_continuity_score']), _safe_float(rf08_15m['observed_percentile_control_minus_real_mean_family_event_share']), _safe_float(rf08_15m['observed_percentile_control_minus_real_mean_member_coverage'])))}`. Damit bleibt kein allgemeiner Familienmarker, sondern ein möglicher `rf_08`-Vorzeichen-Kopplungseffekt im 15m-Kontext.",
            "",
            f"Die beiden `rf_10`-Achsen werden durch die Pseudo-Kontrolle nicht als familienspezifisch getragen. Bei Vorzeichen zeigen `{rf10_sign['pseudo_same_relation']}/100`, bei Körpergröße `{rf10_magnitude['pseudo_same_relation']}/100` dieselbe Abschwächung; ihre Gesamtperzentile liegen überwiegend im mittleren Bereich. Mitgliederzahl und Quellhäufigkeitsnähe reichen damit aus, um diese Antwort häufig hervorzubringen.",
            "",
            f"Explorativ fällt `rf_05:volume` auf. Diese Achse gehörte wegen fehlender Zeitebenenstabilität nicht zum Primärvergleich, liegt insgesamt aber bei `{rf05_volume['pseudo_same_relation']}/100` gleichen Pseudo-Antworten und Perzentilen `{_fmt(rf05_volume['observed_percentile_control_minus_real_family_continuity_score'])}`, `{_fmt(rf05_volume['observed_percentile_control_minus_real_mean_family_event_share'])}`, `{_fmt(rf05_volume['observed_percentile_control_minus_real_mean_member_coverage'])}`. Auf `1h` liegen alle drei Maße zwischen `{_fmt(min(_safe_float(rf05_volume_1h['observed_percentile_control_minus_real_family_continuity_score']), _safe_float(rf05_volume_1h['observed_percentile_control_minus_real_mean_family_event_share']), _safe_float(rf05_volume_1h['observed_percentile_control_minus_real_mean_member_coverage'])))}` und `1.000`. Das ist ein nachgelagerter, kontextgebundener Kandidat und keine Bestätigung.",
            "",
            "Der tragfähige Befund ist damit enger als 2078: Phasenantworten können aus Größe und Häufigkeitsprofil entstehen; nur einzelne Familien-Komponenten-Kontexte bleiben darüber hinaus auffällig. Diese Kontextbindung ist passive Evidenz für mögliche relationale Kopplung, aber noch keine stabile Familienindividualität, feste Bedeutung oder organische Runtime-Erweiterung.",
            "",
            "## Grenze",
            "",
            "Das Matching nähert Quellhäufigkeiten an, kann sie bei extremen Familienprofilen aber nicht identisch ersetzen. Pseudo-Familien verwenden denselben 29-Symbol-Pool und dieselben Marktwelten. Der Lauf trennt Familienzugehörigkeit von Größe und Häufigkeitsnähe, nicht von allen möglichen Eigenschaften der Symbolgeometrie oder Messpipeline.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Prüft Rollenfamilien gegen gematchte Pseudo-Familien.")
    parser.add_argument("--memory", default=str(DEFAULT_MEMORY))
    parser.add_argument("--cohesion-detail", default=str(DEFAULT_COHESION))
    parser.add_argument("--holdout-data-dir", default=str(HOLDOUT_DATA_DIR))
    parser.add_argument("--holdout-debug-root", default=str(HOLDOUT_DEBUG_ROOT))
    parser.add_argument("--holdout-archive", default=str(HOLDOUT_ARCHIVE))
    parser.add_argument("--holdout-comparison", default=str(DEFAULT_HOLDOUT_COMPARISON))
    parser.add_argument("--out-prefix", default=str(DEFAULT_OUT_PREFIX))
    args = parser.parse_args()

    memory = _resolve(args.memory)
    cohesion = _resolve(args.cohesion_detail)
    holdout_data_dir = _resolve(args.holdout_data_dir)
    holdout_debug_root = _resolve(args.holdout_debug_root)
    holdout_archive = _resolve(args.holdout_archive)
    holdout_comparison = _resolve(args.holdout_comparison)
    out_prefix = _resolve(args.out_prefix)

    if not holdout_archive.exists():
        raise FileNotFoundError(holdout_archive)
    targets = _load_targets(memory, list(ROLE_FAMILIES))
    all_symbols = sorted({symbol for members in targets.values() for symbol in members})
    global_counts = _load_global_source_counts(cohesion, set(all_symbols))
    definitions = _build_matched_definitions(targets, global_counts)
    real_records, phase_records = _build_records(holdout_data_dir)
    pool_rows = _load_pool_member_rows(
        real_records + phase_records,
        all_symbols,
        holdout_debug_root,
    )
    pseudo_rows = _evaluate_pseudos(definitions, pool_rows, global_counts)
    summary = _build_null_summary(pseudo_rows, holdout_comparison)

    _write_csv(out_prefix.with_suffix(".definitions.csv"), definitions)
    _write_csv(out_prefix.with_suffix(".pseudos.csv"), pseudo_rows)
    _write_csv(out_prefix.with_suffix(".summary.csv"), summary)
    _write_markdown(out_prefix.with_suffix(".md"), definitions, summary, holdout_archive)

    print(f"symbols={len(all_symbols)}")
    print(f"worlds={len(real_records) + len(phase_records)}")
    print(f"pool_member_rows={len(pool_rows)}")
    print(f"pseudo_definitions={len(definitions)}")
    print(f"pseudo_component_rows={len(pseudo_rows)}")
    print(f"summary_rows={len(summary)}")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
