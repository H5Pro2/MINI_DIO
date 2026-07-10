from __future__ import annotations

import argparse
from pathlib import Path

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
DEFAULT_DATA_DIR = ROOT / "data" / "generated" / "2076_rf05_component_phase_controls"
DEFAULT_ARCHIVE = ROOT / "data" / "2076_rf05_component_phase_controls.zip"
DEFAULT_DEBUG_ROOT = ROOT / "debug" / "2076_rf05_component_phase_controls"
DEFAULT_OUT_PREFIX = BEFUNDE / "2076_RF05_KOMPONENTEN_PHASENKONTROLLEN"
COMPONENTS = ("sign", "magnitude", "wick", "volume")
LAGS = (17, 83, 251)
EXACT_KINDS = tuple(
    f"{component}_phase_{lag:03d}" for component in COMPONENTS for lag in LAGS
)
GROUPS = ("overall", "asset:BTC", "asset:SOL", "timeframe:1h", "timeframe:15m")
PRIMARY_METRICS = (
    ("Kontinuität", "family_continuity_score"),
    ("Ereignisanteil", "mean_family_event_share"),
    ("Abdeckung", "mean_member_coverage"),
)


def _resolve(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def _rotate(values: list[object], lag: int) -> list[object]:
    offset = lag % len(values)
    if offset == 0:
        return list(values)
    return values[-offset:] + values[:-offset]


def _phase_worlds(source: Path, prefix: Path) -> dict[str, Path]:
    fieldnames, data = _read_rows(source, ROWS)
    if len(data) != ROWS:
        raise ValueError(f"{source} enthält {len(data)} statt {ROWS} Zeilen")
    shapes = [_row_shape(row) for row in data]
    symbol = str(data[0].get("symbol", "") or "")
    timeframe = str(data[0].get("timeframe", "") or "")

    signs = [-1.0 if shape["body"] < 0.0 else 1.0 for shape in shapes]
    magnitudes = [abs(shape["body"]) for shape in shapes]
    wicks = [(shape["upper"], shape["lower"]) for shape in shapes]
    volumes = [shape["volume"] for shape in shapes]

    controls: dict[str, list[dict[str, float]]] = {}
    for lag in LAGS:
        shifted_signs = _rotate(signs, lag)
        controls[f"sign_phase_{lag:03d}"] = [
            {**shape, "body": magnitudes[index] * float(shifted_signs[index])}
            for index, shape in enumerate(shapes)
        ]

        shifted_magnitudes = _rotate(magnitudes, lag)
        controls[f"magnitude_phase_{lag:03d}"] = [
            {**shape, "body": float(shifted_magnitudes[index]) * signs[index]}
            for index, shape in enumerate(shapes)
        ]

        shifted_wicks = _rotate(wicks, lag)
        controls[f"wick_phase_{lag:03d}"] = [
            {
                **shape,
                "upper": float(shifted_wicks[index][0]),
                "lower": float(shifted_wicks[index][1]),
            }
            for index, shape in enumerate(shapes)
        ]

        shifted_volumes = _rotate(volumes, lag)
        controls[f"volume_phase_{lag:03d}"] = [
            {**shape, "volume": float(shifted_volumes[index])}
            for index, shape in enumerate(shapes)
        ]

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


def _build_phase_records(
    real_records: list[dict[str, object]],
    data_dir: Path,
) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for real in real_records:
        asset = str(real["asset"])
        timeframe = str(real["timeframe"])
        start = int(real["start"])
        paths = _phase_worlds(
            Path(str(real["path"])),
            data_dir / f"control_2076_{asset.lower()}_2024_{timeframe}_start{start}",
        )
        for kind, path in paths.items():
            lag = int(kind.rsplit("_", 1)[1])
            records.append(
                {
                    **real,
                    "kind": kind,
                    "seed": lag,
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


def _summary_for_kinds(
    member_rows: list[dict[str, object]],
    targets: dict[str, list[str]],
    source_counts: dict,
    kinds: tuple[str, ...],
    group: str,
) -> dict[str, object]:
    rows = [row for row in member_rows if str(row["world_kind"]) in kinds]
    rows = _filter_group(rows, group)
    world_rows = _build_world_family_rows(rows)
    return _build_family_summary(world_rows, rows, targets, source_counts)[0]


def _kind_parts(kind: str) -> tuple[str, int]:
    component, _, lag = kind.rpartition("_phase_")
    return component, int(lag)


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
        for kind in EXACT_KINDS:
            control = indexed[(asset, timeframe, start, kind)]
            component, lag = _kind_parts(kind)
            row: dict[str, object] = {
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
    group: str,
    component: str,
    lag: int | None,
) -> dict[str, int]:
    rows = _filter_group(paired_rows, group)
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
        real = _summary_for_kinds(member_rows, targets, source_counts, ("real",), group)
        for component in COMPONENTS:
            scopes: list[tuple[str, int | None, tuple[str, ...]]] = [
                (
                    "component",
                    None,
                    tuple(kind for kind in EXACT_KINDS if kind.startswith(f"{component}_")),
                )
            ]
            scopes.extend(
                ("lag", lag, (f"{component}_phase_{lag:03d}",)) for lag in LAGS
            )
            for scope, lag, kinds in scopes:
                control = _summary_for_kinds(
                    member_rows,
                    targets,
                    source_counts,
                    kinds,
                    group,
                )
                row: dict[str, object] = {
                    "group": group,
                    "scope": scope,
                    "component": component,
                    "lag": "" if lag is None else lag,
                    "real_worlds": real["worlds"],
                    "control_worlds": control["worlds"],
                }
                for metric in SUMMARY_METRICS:
                    real_value = _safe_float(real.get(metric))
                    control_value = _safe_float(control.get(metric))
                    row[f"real_{metric}"] = real_value
                    row[f"control_{metric}"] = control_value
                    row[f"real_minus_control_{metric}"] = real_value - control_value
                row.update(_pair_counts(paired_rows, group, component, lag))
                rows.append(row)
    return rows


def _fmt(value: object, digits: int = 3) -> str:
    return f"{_safe_float(value):.{digits}f}"


def _axis_relation(row: dict[str, object]) -> str:
    above = [
        label
        for label, metric in PRIMARY_METRICS
        if _safe_float(row[f"control_{metric}"]) > _safe_float(row[f"real_{metric}"])
    ]
    return ";".join(above) or "-"


def _write_markdown(
    path: Path,
    comparisons: list[dict[str, object]],
    archive: Path,
) -> None:
    overall = [row for row in comparisons if row["group"] == "overall"]
    pooled = {str(row["component"]): row for row in overall if row["scope"] == "component"}
    exact = [row for row in overall if row["scope"] == "lag"]
    real = pooled[COMPONENTS[0]]

    consistently_lower: list[str] = []
    for component in COMPONENTS:
        component_rows = [row for row in exact if row["component"] == component]
        if all(
            all(
                _safe_float(row[f"control_{metric}"]) < _safe_float(row[f"real_{metric}"])
                for _, metric in PRIMARY_METRICS
            )
            for row in component_rows
        ):
            consistently_lower.append(component)
    all_axis_stronger = [
        f"{row['component']}:{row['lag']}"
        for row in exact
        if all(
            _safe_float(row[f"control_{metric}"]) > _safe_float(row[f"real_{metric}"])
            for _, metric in PRIMARY_METRICS
        )
    ]
    pooled_lower = [
        component
        for component, row in pooled.items()
        if all(
            _safe_float(row[f"control_{metric}"]) < _safe_float(row[f"real_{metric}"])
            for _, metric in PRIMARY_METRICS
        )
    ]
    sign_row = pooled["sign"]

    lines = [
        "# 2076 - rf_05 unter Komponenten-Phasenkontrollen",
        "",
        "## Zweck",
        "",
        "Befund 2075 zeigte, dass zufällige Einzelkomponenten-Permutationen `rf_05` teils abschwächen, teils aber deutlich verstärken. Dieser Versuch prüft enger, ob die Familie an der relativen zeitlichen Kopplung der OHLCV-Komponenten hängt.",
        "",
        "## Vorab Festgelegtes Design",
        "",
        "- identische zwölf 2024-Holdoutfenster aus 2074 und 2075",
        "- Komponenten: Körpervorzeichen, absolute Körpergröße, Dochtpaar und Volumen",
        "- feste zirkuläre Offsets: `17`, `83` und `251` Beobachtungen",
        "- jede Kontrolle erhält Reihenfolge, Verteilung und Autokorrelation der verschobenen Komponente vollständig",
        "- nur die relative zeitliche Ausrichtung zum übrigen Feld wird verändert",
        "- `144` neue Kontrollläufe und `12` Realreferenzläufe mit jeweils frischer episodischer Memory",
        "- unveränderte acht Mitglieder von `rf_05`",
        "- Wahrnehmungsmodus: `world_relative`",
        f"- Archiv der neuen Phasenkontrollen: `{_relative(archive)}`",
        "- keine neue Klasse, keine Handlung, kein Gate und keine Richtung",
        "",
        "Eine notwendige reale Komponentenkopplung wäre nur dann gestützt, wenn mehrere vorab festgelegte Offsets dieselbe Komponente gegenüber Real gemeinsam bei Kontinuität, Ereignisanteil und Abdeckung schwächen. Einzelne Offseteffekte gelten als Phasensensitivität, nicht als Ursache.",
        "",
        "## Gesamtprofil Nach Offset",
        "",
        f"Realreferenz: Kontinuität `{_fmt(real['real_family_continuity_score'])}`, Ereignisanteil `{_fmt(real['real_mean_family_event_share'], 4)}`, Abdeckung `{_fmt(real['real_mean_member_coverage'])}`.",
        "",
        "| Komponente | Offset | Kontinuität | Ereignisanteil | Abdeckung | Drift | Achsen über Real | gemeinsam Real höher |",
        "|---|---:|---:|---:|---:|---:|---|---:|",
    ]
    for row in exact:
        lines.append(
            f"| `{row['component']}` | {row['lag']} | "
            f"{_fmt(row['control_family_continuity_score'])} | "
            f"{_fmt(row['control_mean_family_event_share'], 4)} | "
            f"{_fmt(row['control_mean_member_coverage'])} | "
            f"{_fmt(row['control_member_distribution_drift'])} | "
            f"{_axis_relation(row)} | "
            f"{row['paired_joint_real_advantage']}/{row['paired_windows']} |"
        )

    lines.extend(
        [
            "",
            "## Komponentenprofil Über Alle Offsets",
            "",
            "Die Komponentenwerte bündeln jeweils `36` Kontrollwelten. Die Paarzahlen enthalten drei direkte Offsets je Realfenster.",
            "",
            "| Komponente | Kontinuität | Ereignisanteil | Abdeckung | Drift | Achsen über Real | gemeinsam Real höher |",
            "|---|---:|---:|---:|---:|---|---:|",
        ]
    )
    for component in COMPONENTS:
        row = pooled[component]
        lines.append(
            f"| `{component}` | {_fmt(row['control_family_continuity_score'])} | "
            f"{_fmt(row['control_mean_family_event_share'], 4)} | "
            f"{_fmt(row['control_mean_member_coverage'])} | "
            f"{_fmt(row['control_member_distribution_drift'])} | "
            f"{_axis_relation(row)} | "
            f"{row['paired_joint_real_advantage']}/{row['paired_windows']} |"
        )

    lines.extend(
        [
            "",
            "## Asset- Und Zeitebenenprofil",
            "",
            "Angegeben ist Real minus gebündelte Phasenkontrolle bei Kontinuität. Die Teilgruppen bleiben sekundär.",
            "",
            "| Gruppe | sign | magnitude | wick | volume |",
            "|---|---:|---:|---:|---:|",
        ]
    )
    for group in GROUPS[1:]:
        group_rows = {
            str(row["component"]): row
            for row in comparisons
            if row["group"] == group and row["scope"] == "component"
        }
        lines.append(
            f"| `{group}` | "
            + " | ".join(
                _fmt(group_rows[component]["real_minus_control_family_continuity_score"])
                for component in COMPONENTS
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"Über alle drei Offsets auf allen drei Primärachsen durchgehend unter Real liegen: `{';'.join(consistently_lower) or '-'}`.",
            "",
            f"Einzelne Phasenkontrollen, die Real gleichzeitig auf allen drei Primärachsen übertreffen: `{';'.join(all_axis_stronger) or '-'}`.",
            "",
            f"Im über alle Offsets gebündelten Profil liegt nur `{';'.join(pooled_lower) or '-'}` auf allen drei Primärachsen unter Real. Bei der Vorzeichenphase ist der Abstand jedoch nicht breit fensterstabil: Real trägt einen höheren Ereignisanteil in `{sign_row['paired_event_share_real_wins']}/{sign_row['paired_windows']}`, eine höhere Abdeckung in `{sign_row['paired_coverage_real_wins']}/{sign_row['paired_windows']}` und beides gemeinsam nur in `{sign_row['paired_joint_real_advantage']}/{sign_row['paired_windows']}` Paaren. Zudem hebt Offset `251` Kontinuität und Abdeckung wieder über Real.",
            "",
            "Die Größen-, Docht- und Volumenphase ist kein notwendiger Träger der realen Familienlesung. Ihre gebündelten Kontrollen liegen jeweils auf allen drei Primärachsen über Real; alle drei Volumen-Offsets tun dies auch einzeln. Damit widerspricht der Lauf einer allgemeinen notwendigen Kopplung aller OHLCV-Komponenten.",
            "",
            "Die relative Vorzeichenphase bleibt als begrenzter Empfindlichkeitskandidat offen, aber nicht als belastbare Feldbindung: Der Mittelwertabstand, die geringe gemeinsame Paarbreite und der gegenläufige längste Offset tragen nicht kohärent genug. Das Muster belegt Phasensensitivität, keine Ursache und keine feste Bedeutung von `rf_05`.",
            "",
            "Die Messung verändert keine Feldmechanik. Aus diesem Befund folgt keine begründete organische Erweiterung, weil die Wirkung weder über Komponenten noch über Offsets und direkte Fensterpaare kohärent trägt.",
            "",
            "## Grenze",
            "",
            "Die zirkuläre Verschiebung erzeugt am Umlaufpunkt eine künstliche Nachbarschaft und rekonstruiert anschließend einen neuen Preisweg. Sie bewahrt die Eigenfolge einer Komponente exakt, beweist aber weder Kausalität noch feste Semantik. Die Prüfung bleibt auf Marktzeitreihen und `1000` Beobachtungen je Welt begrenzt.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Prüft rf_05 mit Komponenten-Phasenlagen.")
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
    phase_records = _build_phase_records(real_records, data_dir)
    _write_control_archive(archive, phase_records)

    real_members = _run_worlds(real_records, targets, base_debug_root)
    phase_members = _run_worlds(phase_records, targets, debug_root)
    member_rows = real_members + phase_members
    world_rows = _build_world_rows(member_rows)
    paired_rows = _build_paired(world_rows)
    comparisons = _build_comparisons(member_rows, targets, source_counts, paired_rows)

    _write_csv(out_prefix.with_suffix(".worlds.csv"), world_rows)
    _write_csv(out_prefix.with_suffix(".paired.csv"), paired_rows)
    _write_csv(out_prefix.with_suffix(".comparison.csv"), comparisons)
    _write_markdown(out_prefix.with_suffix(".md"), comparisons, archive)

    print(f"real_worlds={len(real_records)}")
    print(f"new_phase_worlds={len(phase_records)}")
    print(f"world_rows={len(world_rows)}")
    print(f"paired_rows={len(paired_rows)}")
    print(f"comparison_rows={len(comparisons)}")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
