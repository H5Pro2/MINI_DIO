from __future__ import annotations

import argparse
import random
from pathlib import Path
from statistics import mean

try:
    from tools.build_equal_length_null_worlds import (
        _read_rows,
        _rebuild_from_shapes,
        _row_shape,
        _write_rows,
    )
    from tools.run_role_family_followworld_probe import (
        _build_family_summary,
        _build_world_family_rows,
        _load_source_member_counts,
        _load_targets,
        _safe_float,
        _write_csv,
    )
    from tools.run_role_family_real_null_contrast import _relative, _write_control_archive
    from tools.run_rf05_crossyear_timeframe_holdout import (
        DEFAULT_COHESION,
        DEFAULT_DATA_DIR as BASE_DATA_DIR,
        DEFAULT_DEBUG_ROOT as BASE_DEBUG_ROOT,
        DEFAULT_MEMORY,
        PAIR_METRICS,
        ROWS,
        SUMMARY_METRICS,
        _build_world_records,
        _build_world_rows,
        _run_worlds,
    )
except ModuleNotFoundError:
    from build_equal_length_null_worlds import (
        _read_rows,
        _rebuild_from_shapes,
        _row_shape,
        _write_rows,
    )
    from run_role_family_followworld_probe import (
        _build_family_summary,
        _build_world_family_rows,
        _load_source_member_counts,
        _load_targets,
        _safe_float,
        _write_csv,
    )
    from run_role_family_real_null_contrast import _relative, _write_control_archive
    from run_rf05_crossyear_timeframe_holdout import (
        DEFAULT_COHESION,
        DEFAULT_DATA_DIR as BASE_DATA_DIR,
        DEFAULT_DEBUG_ROOT as BASE_DEBUG_ROOT,
        DEFAULT_MEMORY,
        PAIR_METRICS,
        ROWS,
        SUMMARY_METRICS,
        _build_world_records,
        _build_world_rows,
        _run_worlds,
    )


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = ROOT / "docs" / "befunde" / "2001-3000"
DEFAULT_DATA_DIR = ROOT / "data" / "generated" / "2075_rf05_component_controls"
DEFAULT_ARCHIVE = ROOT / "data" / "2075_rf05_component_controls.zip"
DEFAULT_DEBUG_ROOT = ROOT / "debug" / "2075_rf05_component_controls"
DEFAULT_OUT_PREFIX = BEFUNDE / "2075_RF05_KOMPONENTEN_KONTROLLEN"
BASE_KINDS = ("real", "shuffle", "random_sign")
COMPONENT_KINDS = ("sign_shuffle", "magnitude_shuffle", "wick_shuffle", "volume_shuffle")
ALL_KINDS = BASE_KINDS + COMPONENT_KINDS
GROUPS = ("overall", "asset:BTC", "asset:SOL", "timeframe:1h", "timeframe:15m")


def _resolve(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def _component_worlds(source: Path, prefix: Path, seed: int) -> dict[str, Path]:
    fieldnames, data = _read_rows(source, ROWS)
    if len(data) != ROWS:
        raise ValueError(f"{source} enthält {len(data)} statt {ROWS} Zeilen")
    shapes = [_row_shape(row) for row in data]
    symbol = str(data[0].get("symbol", "") or "")
    timeframe = str(data[0].get("timeframe", "") or "")

    signs = [-1.0 if shape["body"] < 0.0 else 1.0 for shape in shapes]
    shuffled_signs = list(signs)
    random.Random(seed).shuffle(shuffled_signs)
    sign_shapes = [
        {**shape, "body": abs(shape["body"]) * shuffled_signs[index]}
        for index, shape in enumerate(shapes)
    ]

    magnitudes = [abs(shape["body"]) for shape in shapes]
    shuffled_magnitudes = list(magnitudes)
    random.Random(seed + 1000).shuffle(shuffled_magnitudes)
    magnitude_shapes = [
        {**shape, "body": shuffled_magnitudes[index] * signs[index]}
        for index, shape in enumerate(shapes)
    ]

    wicks = [(shape["upper"], shape["lower"]) for shape in shapes]
    shuffled_wicks = list(wicks)
    random.Random(seed + 2000).shuffle(shuffled_wicks)
    wick_shapes = [
        {
            **shape,
            "upper": shuffled_wicks[index][0],
            "lower": shuffled_wicks[index][1],
        }
        for index, shape in enumerate(shapes)
    ]

    volumes = [shape["volume"] for shape in shapes]
    shuffled_volumes = list(volumes)
    random.Random(seed + 3000).shuffle(shuffled_volumes)
    volume_shapes = [
        {**shape, "volume": shuffled_volumes[index]}
        for index, shape in enumerate(shapes)
    ]

    controls = {
        "sign_shuffle": sign_shapes,
        "magnitude_shuffle": magnitude_shapes,
        "wick_shuffle": wick_shapes,
        "volume_shuffle": volume_shapes,
    }
    paths: dict[str, Path] = {}
    for kind, control_shapes in controls.items():
        path = prefix.with_name(f"{prefix.name}_{kind}_{ROWS}.csv")
        _write_rows(
            path,
            fieldnames,
            _rebuild_from_shapes(data, control_shapes, symbol, timeframe),
        )
        paths[kind] = path
    return paths


def _build_component_records(
    real_records: list[dict[str, object]],
    data_dir: Path,
) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for index, real in enumerate(real_records):
        asset = str(real["asset"])
        timeframe = str(real["timeframe"])
        start = int(real["start"])
        seed = 207500 + index
        paths = _component_worlds(
            Path(str(real["path"])),
            data_dir / f"control_2075_{asset.lower()}_2024_{timeframe}_start{start}",
            seed,
        )
        for kind, path in paths.items():
            records.append(
                {
                    **real,
                    "kind": kind,
                    "seed": seed,
                    "path": path,
                }
            )
    return records


def _filter_group(rows: list[dict[str, object]], group: str) -> list[dict[str, object]]:
    if group.startswith("asset:"):
        asset = group.split(":", 1)[1]
        return [row for row in rows if row["asset"] == asset]
    if group.startswith("timeframe:"):
        timeframe = group.split(":", 1)[1]
        return [row for row in rows if row["timeframe"] == timeframe]
    return rows


def _summary_for(
    member_rows: list[dict[str, object]],
    targets: dict[str, list[str]],
    source_counts: dict,
    kind: str,
    group: str,
) -> dict[str, object]:
    rows = [row for row in member_rows if row["world_kind"] == kind]
    rows = _filter_group(rows, group)
    world_rows = _build_world_family_rows(rows)
    return _build_family_summary(world_rows, rows, targets, source_counts)[0]


def _build_comparisons(
    member_rows: list[dict[str, object]],
    targets: dict[str, list[str]],
    source_counts: dict,
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for group in GROUPS:
        summaries = {
            kind: _summary_for(member_rows, targets, source_counts, kind, group)
            for kind in ALL_KINDS
        }
        real = summaries["real"]
        row: dict[str, object] = {"group": group, "real_worlds": real["worlds"]}
        for kind, summary in summaries.items():
            for metric in SUMMARY_METRICS:
                row[f"{kind}_{metric}"] = _safe_float(summary.get(metric))
                if kind != "real":
                    row[f"real_minus_{kind}_{metric}"] = _safe_float(real.get(metric)) - _safe_float(
                        summary.get(metric)
                    )
        rows.append(row)
    return rows


def _build_paired(world_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    indexed = {
        (
            str(row["asset"]),
            str(row["timeframe"]),
            int(row["window_start"]),
            str(row["world_kind"]),
        ): row
        for row in world_rows
    }
    real_keys = sorted(key for key in indexed if key[3] == "real")
    rows: list[dict[str, object]] = []
    for asset, timeframe, start, _ in real_keys:
        real = indexed[(asset, timeframe, start, "real")]
        for kind in ALL_KINDS[1:]:
            control = indexed[(asset, timeframe, start, kind)]
            row: dict[str, object] = {
                "asset": asset,
                "timeframe": timeframe,
                "window_start": start,
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


def _add_pair_counts(
    comparisons: list[dict[str, object]],
    paired_rows: list[dict[str, object]],
) -> None:
    for comparison in comparisons:
        group_rows = _filter_group(paired_rows, str(comparison["group"]))
        for kind in ALL_KINDS[1:]:
            rows = [row for row in group_rows if row["control_kind"] == kind]
            comparison[f"paired_{kind}_windows"] = len(rows)
            comparison[f"paired_{kind}_event_share_real_wins"] = sum(
                _safe_float(row["real_minus_control_family_event_share"]) > 0.0 for row in rows
            )
            comparison[f"paired_{kind}_coverage_real_wins"] = sum(
                _safe_float(row["real_minus_control_member_coverage"]) > 0.0 for row in rows
            )
            comparison[f"paired_{kind}_joint_real_advantage"] = sum(
                int(row["real_joint_coverage_event_advantage"]) for row in rows
            )


def _fmt(value: object, digits: int = 3) -> str:
    return f"{_safe_float(value):.{digits}f}"


def _write_markdown(
    path: Path,
    comparisons: list[dict[str, object]],
    archive: Path,
) -> None:
    overall = next(row for row in comparisons if row["group"] == "overall")
    control_axis_wins: dict[str, list[str]] = {}
    for kind in ALL_KINDS[1:]:
        wins: list[str] = []
        for label, metric in (
            ("Kontinuität", "family_continuity_score"),
            ("Ereignisanteil", "mean_family_event_share"),
            ("Abdeckung", "mean_member_coverage"),
        ):
            if _safe_float(overall[f"{kind}_{metric}"]) > _safe_float(overall[f"real_{metric}"]):
                wins.append(label)
        control_axis_wins[kind] = wins
    strongest_control = max(
        ALL_KINDS[1:],
        key=lambda kind: _safe_float(overall[f"{kind}_family_continuity_score"]),
    )
    strongest_event_control = max(
        ALL_KINDS[1:],
        key=lambda kind: _safe_float(overall[f"{kind}_mean_family_event_share"]),
    )
    strongest_coverage_control = max(
        ALL_KINDS[1:],
        key=lambda kind: _safe_float(overall[f"{kind}_mean_member_coverage"]),
    )
    all_axis_controls = [
        kind for kind, wins in control_axis_wins.items() if len(wins) == 3
    ]
    lines = [
        "# 2075 - rf_05 unter komponentenisolierten Kontrollen",
        "",
        "## Zweck",
        "",
        "Befund 2074 zeigte eine klare Kontrollasymmetrie: `rf_05` lag über vollständigem Shape-Shuffle, aber unter Random Sign. Dieser Versuch trennt Körperrichtung, Körpergröße, Dochte und Volumen, um die tragende relationale Komponente enger einzugrenzen.",
        "",
        "## Methode",
        "",
        "- identische zwölf 2024-Holdoutfenster aus 2074",
        "- Referenzen aus 2074: Realwelt, vollständiges Shape-Shuffle und Random Sign",
        "- vier neue Komponenten-Kontrollen pro Realfenster",
        "- `48` neue Kontrollläufe mit jeweils frischer episodischer Memory",
        "- unveränderte acht Mitglieder von `rf_05`",
        "- Wahrnehmungsmodus: `world_relative`",
        f"- Archiv der neuen Komponenten-Kontrollen: `{_relative(archive)}`",
        "- keine neue Klasse, keine Handlung, kein Gate und keine Richtung",
        "",
        "Kontrollformen:",
        "",
        "- `sign_shuffle`: permutiert nur die Körpervorzeichen und erhält deren Gesamtverteilung",
        "- `magnitude_shuffle`: permutiert nur die absoluten Körpergrößen und erhält die Richtungsfolge",
        "- `wick_shuffle`: permutiert nur die Paare aus oberem und unterem Docht",
        "- `volume_shuffle`: permutiert nur die Volumenfolge",
        "- `shuffle`: permutiert vollständige lokale Kerzenformen samt Volumen",
        "- `random_sign`: setzt Körpervorzeichen zufällig und erhält die zeitliche Größen-, Docht- und Volumenfolge",
        "",
        "## Gesamtprofil",
        "",
        "| Weltform | Kontinuität | Ereignisanteil | Abdeckung | Drift | Achsen über Real |",
        "|---|---:|---:|---:|---:|---|",
        f"| `real` | {_fmt(overall['real_family_continuity_score'])} | {_fmt(overall['real_mean_family_event_share'], 4)} | {_fmt(overall['real_mean_member_coverage'])} | {_fmt(overall['real_member_distribution_drift'])} | - |",
    ]
    for kind in ALL_KINDS[1:]:
        lines.append(
            f"| `{kind}` | {_fmt(overall[f'{kind}_family_continuity_score'])} | "
            f"{_fmt(overall[f'{kind}_mean_family_event_share'], 4)} | "
            f"{_fmt(overall[f'{kind}_mean_member_coverage'])} | "
            f"{_fmt(overall[f'{kind}_member_distribution_drift'])} | "
            f"{';'.join(control_axis_wins[kind]) or '-'} |"
        )
    lines.extend(
        [
            "",
            "## Paarvergleich",
            "",
            "| Kontrolle | Ereignis Real höher | Abdeckung Real höher | gemeinsam Real höher |",
            "|---|---:|---:|---:|",
        ]
    )
    for kind in ALL_KINDS[1:]:
        windows = overall[f"paired_{kind}_windows"]
        lines.append(
            f"| `{kind}` | {overall[f'paired_{kind}_event_share_real_wins']}/{windows} | "
            f"{overall[f'paired_{kind}_coverage_real_wins']}/{windows} | "
            f"{overall[f'paired_{kind}_joint_real_advantage']}/{windows} |"
        )
    lines.extend(
        [
            "",
            "## Asset- Und Zeitebenenprofil",
            "",
            "Die Teilgruppen bleiben sekundär. Angegeben ist jeweils Real minus Kontrolle bei Kontinuität.",
            "",
            "| Gruppe | shape shuffle | random sign | sign shuffle | magnitude shuffle | wick shuffle | volume shuffle |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in comparisons[1:]:
        lines.append(
            f"| `{row['group']}` | "
            + " | ".join(
                _fmt(row[f"real_minus_{kind}_family_continuity_score"])
                for kind in ALL_KINDS[1:]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"Die höchste Kontrollkontinuität trägt `{strongest_control}` mit `{_fmt(overall[f'{strongest_control}_family_continuity_score'])}` gegenüber Real `{_fmt(overall['real_family_continuity_score'])}`.",
            "",
            f"Den höchsten Familienereignisanteil trägt `{strongest_event_control}` mit `{_fmt(overall[f'{strongest_event_control}_mean_family_event_share'], 4)}`; die höchste Mitgliederabdeckung trägt `{strongest_coverage_control}` mit `{_fmt(overall[f'{strongest_coverage_control}_mean_member_coverage'])}`. Auf allen drei Primärachsen über Real liegen: `{';'.join(all_axis_controls) or '-'}`.",
            "",
            "Die reale Vorzeichenreihenfolge besitzt gegenüber `sign_shuffle` einen kleinen gemeinsamen Vorsprung. Dieser Befund reicht jedoch nicht für eine Richtungsbindung, weil `random_sign` Real gleichzeitig bei Kontinuität, Ereignisanteil und Abdeckung übertrifft. Die Wirkung der Vorzeichenänderung ist damit nicht monoton und hängt von der konkreten Kontrollform ab.",
            "",
            "Auch die reale Größen- und Volumenfolge ist nicht notwendig für starke Familienlesung: `magnitude_shuffle` und `volume_shuffle` verstärken `rf_05` auf allen drei Primärachsen. `wick_shuffle` erhöht den Ereignisanteil, senkt aber Kontinuität und Abdeckung. Erst vollständiges Shape-Shuffle senkt alle drei Achsen gemeinsam.",
            "",
            "Das Gesamtmuster spricht gegen eine einzelne tragende OHLCV-Komponente. `rf_05` reagiert eher auf die gekoppelte Organisation mehrerer zeitlicher Komponenten und kann durch isolierte Entkopplung sogar verstärkt werden. Daraus folgt derzeit keine begründete organische Erweiterung der Feldmechanik.",
            "",
            "Eine einzelne permutierte Komponente wird nicht automatisch als Ursache gelesen. Aussagekräftig ist das Muster über Kontinuität, Ereignisanteil, Abdeckung und die zwölf direkten Paarfenster. Kontrollen, die Real auf mehreren Achsen erreichen oder übertreffen, markieren Komponenten, deren reale Reihenfolge für `rf_05` nicht hinreichend spezifisch ist.",
            "",
            "Wenn eine isolierte Permutation deutlich unter Real fällt, bleibt die ursprüngliche Reihenfolge dieser Komponente ein Kandidat für die Tragung. Das ist eine diagnostische Eingrenzung und keine neue Feldregel.",
            "",
            "## Grenze",
            "",
            "Die Komponenten sind innerhalb rekonstruierter OHLCV-Welten nicht vollständig unabhängig. Eine veränderte Körpergröße beeinflusst den fortlaufenden Preisweg; Dochte und Körper bleiben geometrisch gekoppelt. Der Versuch lokalisiert Empfindlichkeiten, beweist aber keine einzelne kausale Quelle und keine feste Bedeutung von `rf_05`.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Isoliert tragende Komponenten von rf_05.")
    parser.add_argument("--memory", default=str(DEFAULT_MEMORY))
    parser.add_argument("--cohesion-detail", default=str(DEFAULT_COHESION))
    parser.add_argument("--base-data-dir", default=str(BASE_DATA_DIR))
    parser.add_argument("--base-debug-root", default=str(BASE_DEBUG_ROOT))
    parser.add_argument("--data-dir", default=str(DEFAULT_DATA_DIR))
    parser.add_argument("--archive", default=str(DEFAULT_ARCHIVE))
    parser.add_argument("--debug-root", default=str(DEFAULT_DEBUG_ROOT))
    parser.add_argument("--out-prefix", default=str(DEFAULT_OUT_PREFIX))
    args = parser.parse_args()

    memory = _resolve(args.memory)
    cohesion = _resolve(args.cohesion_detail)
    base_data_dir = _resolve(args.base_data_dir)
    base_debug_root = _resolve(args.base_debug_root)
    data_dir = _resolve(args.data_dir)
    archive = _resolve(args.archive)
    debug_root = _resolve(args.debug_root)
    out_prefix = _resolve(args.out_prefix)

    targets = _load_targets(memory, ["rf_05"])
    source_counts = _load_source_member_counts(cohesion, targets)
    base_records = _build_world_records(base_data_dir)
    real_records = [record for record in base_records if record["kind"] == "real"]
    component_records = _build_component_records(real_records, data_dir)
    _write_control_archive(archive, component_records)

    base_members = _run_worlds(base_records, targets, base_debug_root)
    component_members = _run_worlds(component_records, targets, debug_root)
    member_rows = base_members + component_members
    world_rows = _build_world_rows(member_rows)
    comparisons = _build_comparisons(member_rows, targets, source_counts)
    paired_rows = _build_paired(world_rows)
    _add_pair_counts(comparisons, paired_rows)

    _write_csv(out_prefix.with_suffix(".worlds.csv"), world_rows)
    _write_csv(out_prefix.with_suffix(".paired.csv"), paired_rows)
    _write_csv(out_prefix.with_suffix(".comparison.csv"), comparisons)
    _write_markdown(out_prefix.with_suffix(".md"), comparisons, archive)

    print(f"base_worlds={len(base_records)}")
    print(f"new_component_worlds={len(component_records)}")
    print(f"world_rows={len(world_rows)}")
    print(f"paired_rows={len(paired_rows)}")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
