from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
from statistics import mean

try:
    from tools.build_equal_length_null_worlds import build_null_worlds
    from tools.create_csv_slice import create_slice
    from tools.run_role_family_followworld_probe import (
        _build_family_summary,
        _build_member_rows,
        _build_world_family_rows,
        _load_csv,
        _load_source_member_counts,
        _load_targets,
        _run_mini,
        _safe_float,
        _write_csv,
    )
    from tools.run_role_family_real_null_contrast import _relative, _write_control_archive
except ModuleNotFoundError:
    from build_equal_length_null_worlds import build_null_worlds
    from create_csv_slice import create_slice
    from run_role_family_followworld_probe import (
        _build_family_summary,
        _build_member_rows,
        _build_world_family_rows,
        _load_csv,
        _load_source_member_counts,
        _load_targets,
        _run_mini,
        _safe_float,
        _write_csv,
    )
    from run_role_family_real_null_contrast import _relative, _write_control_archive


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = ROOT / "docs" / "befunde" / "2001-3000"
DEFAULT_MEMORY = BEFUNDE / "2069_PASSIVE_ROLLENFAMILIEN_MEMORY.csv"
DEFAULT_COHESION = BEFUNDE / "2066_REALVERSTAERKTE_ROLLENFAMILIEN_KOHAESION.detail.csv"
DEFAULT_DATA_DIR = ROOT / "data" / "generated" / "2074_rf05_holdout"
DEFAULT_ARCHIVE = ROOT / "data" / "2074_rf05_crossyear_timeframe_holdout.zip"
DEFAULT_DEBUG_ROOT = ROOT / "debug" / "2074_rf05_holdout"
DEFAULT_OUT_PREFIX = BEFUNDE / "2074_RF05_CROSSYEAR_TIMEFRAME_HOLDOUT"
ROWS = 1000
SPECS = (
    {
        "asset": "BTC",
        "timeframe": "1h",
        "source": ROOT / "data" / "1-12_2024_1h_BTCUSDT.csv",
        "starts": (0, 3000, 6000),
    },
    {
        "asset": "SOL",
        "timeframe": "1h",
        "source": ROOT / "data" / "1-12_2024_1h_SOLUSDT.csv",
        "starts": (0, 3000, 6000),
    },
    {
        "asset": "BTC",
        "timeframe": "15m",
        "source": ROOT / "data" / "1-12_2024_15m_BTCUSDT.csv",
        "starts": (0, 12000, 24000),
    },
    {
        "asset": "SOL",
        "timeframe": "15m",
        "source": ROOT / "data" / "1-12_2024_15m_SOLUSDT.csv",
        "starts": (0, 12000, 24000),
    },
)
SUMMARY_METRICS = (
    "world_presence_ratio",
    "whole_family_ratio",
    "mean_member_coverage",
    "mean_family_event_share",
    "mean_phase_complete_ratio",
    "member_distribution_drift",
    "mean_afterimage_delta",
    "mean_temporal_delta",
    "family_continuity_score",
)
PAIR_METRICS = (
    "member_coverage",
    "family_event_share",
    "phase_complete_ratio",
    "mean_afterimage_delta",
    "mean_temporal_delta",
)


def _resolve(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def _ensure_slice(
    source: Path,
    target: Path,
    start: int,
    rows: int,
) -> Path:
    if target.exists() and len(_load_csv(target)) == rows:
        return target
    result = create_slice(source, target, start=start, rows=rows)
    if int(result.get("rows_written", 0)) != rows:
        raise ValueError(f"{source} schrieb {result.get('rows_written')} statt {rows} Zeilen")
    return target


def _build_world_records(data_dir: Path) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    real_index = 0
    for spec in SPECS:
        source = Path(str(spec["source"]))
        if not source.exists():
            raise FileNotFoundError(source)
        for start in spec["starts"]:
            asset = str(spec["asset"])
            timeframe = str(spec["timeframe"])
            target = data_dir / (
                f"holdout_2074_{asset.lower()}_2024_{timeframe}_start{start}_rows{ROWS}.csv"
            )
            real_path = _ensure_slice(source, target, int(start), ROWS)
            seed = 207400 + real_index
            real = {
                "asset": asset,
                "timeframe": timeframe,
                "year": 2024,
                "start": int(start),
                "rows": ROWS,
                "kind": "real",
                "seed": "",
                "source": source,
                "path": real_path,
            }
            records.append(real)
            built = build_null_worlds(
                real_path,
                data_dir / f"holdout_2074_{asset.lower()}_2024_{timeframe}_start{start}",
                rows=ROWS,
                seed=seed,
            )
            for kind, key in (("shuffle", "shuffle_order"), ("random_sign", "random_sign")):
                records.append(
                    {
                        **real,
                        "kind": kind,
                        "seed": seed,
                        "path": Path(str(built[key])),
                    }
                )
            real_index += 1
    return records


def _run_worlds(
    records: list[dict[str, object]],
    targets: dict[str, list[str]],
    debug_root: Path,
) -> list[dict[str, object]]:
    member_rows: list[dict[str, object]] = []
    for record in records:
        asset = str(record["asset"])
        timeframe = str(record["timeframe"])
        kind = str(record["kind"])
        start = int(record["start"])
        rows = int(record["rows"])
        world_label = f"{kind}_{asset.lower()}_2024_{timeframe}_{start}_{start + rows}"
        path = Path(str(record["path"]))
        run_dir = _run_mini(path, debug_root / world_label, world_label)
        episodes = _load_csv(run_dir / "episodes.csv")
        world = {
            "asset": asset,
            "timeframe": timeframe,
            "year": 2024,
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


def _summary_for(
    member_rows: list[dict[str, object]],
    targets: dict[str, list[str]],
    source_counts: dict,
    kind: str,
    group: str,
) -> dict[str, object]:
    rows = [row for row in member_rows if row["world_kind"] == kind]
    if group.startswith("asset:"):
        asset = group.split(":", 1)[1]
        rows = [row for row in rows if row["asset"] == asset]
    elif group.startswith("timeframe:"):
        timeframe = group.split(":", 1)[1]
        rows = [row for row in rows if row["timeframe"] == timeframe]
    world_rows = _build_world_family_rows(rows)
    summary = _build_family_summary(world_rows, rows, targets, source_counts)[0]
    return {**summary, "world_kind": kind, "group": group}


def _build_comparisons(
    member_rows: list[dict[str, object]],
    targets: dict[str, list[str]],
    source_counts: dict,
) -> list[dict[str, object]]:
    groups = ("overall", "asset:BTC", "asset:SOL", "timeframe:1h", "timeframe:15m")
    rows: list[dict[str, object]] = []
    for group in groups:
        summaries = {
            kind: _summary_for(member_rows, targets, source_counts, kind, group)
            for kind in ("real", "shuffle", "random_sign")
        }
        row: dict[str, object] = {
            "group": group,
            "real_worlds": summaries["real"]["worlds"],
        }
        for metric in SUMMARY_METRICS:
            real_value = _safe_float(summaries["real"].get(metric))
            shuffle_value = _safe_float(summaries["shuffle"].get(metric))
            random_value = _safe_float(summaries["random_sign"].get(metric))
            row[f"real_{metric}"] = real_value
            row[f"shuffle_{metric}"] = shuffle_value
            row[f"random_sign_{metric}"] = random_value
            row[f"real_minus_control_mean_{metric}"] = real_value - mean(
                (shuffle_value, random_value)
            )
        row["real_minus_strongest_control_continuity"] = _safe_float(
            summaries["real"]["family_continuity_score"]
        ) - max(
            _safe_float(summaries["shuffle"]["family_continuity_score"]),
            _safe_float(summaries["random_sign"]["family_continuity_score"]),
        )
        rows.append(row)
    return rows


def _build_world_rows(member_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in member_rows:
        grouped[str(row["world_kind"])].append(row)
    for kind, kind_members in grouped.items():
        built = _build_world_family_rows(kind_members)
        metadata = {str(row["world_label"]): row for row in kind_members}
        for row in built:
            source = metadata[str(row["world_label"])]
            row["world_kind"] = kind
            row["timeframe"] = source["timeframe"]
            row["year"] = source["year"]
        rows.extend(built)
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
    rows: list[dict[str, object]] = []
    for asset in ("BTC", "SOL"):
        for timeframe, starts in (("1h", (0, 3000, 6000)), ("15m", (0, 12000, 24000))):
            for start in starts:
                real = indexed[(asset, timeframe, start, "real")]
                for kind in ("shuffle", "random_sign"):
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
        group = str(comparison["group"])
        group_rows = paired_rows
        if group.startswith("asset:"):
            group_rows = [row for row in group_rows if row["asset"] == group.split(":", 1)[1]]
        elif group.startswith("timeframe:"):
            group_rows = [
                row for row in group_rows if row["timeframe"] == group.split(":", 1)[1]
            ]
        for kind in ("shuffle", "random_sign"):
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
    primary_advantages = {
        "Kontinuität": _safe_float(overall["real_family_continuity_score"])
        > max(
            _safe_float(overall["shuffle_family_continuity_score"]),
            _safe_float(overall["random_sign_family_continuity_score"]),
        ),
        "Ereignisanteil": _safe_float(overall["real_mean_family_event_share"])
        > max(
            _safe_float(overall["shuffle_mean_family_event_share"]),
            _safe_float(overall["random_sign_mean_family_event_share"]),
        ),
        "Mitgliederabdeckung": _safe_float(overall["real_mean_member_coverage"])
        > max(
            _safe_float(overall["shuffle_mean_member_coverage"]),
            _safe_float(overall["random_sign_mean_member_coverage"]),
        ),
    }
    carried_axes = [name for name, carried in primary_advantages.items() if carried]
    random_joint_wins = int(overall["paired_random_sign_joint_real_advantage"])
    random_windows = int(overall["paired_random_sign_windows"])
    lines = [
        "# 2074 - rf_05 im unabhängigen Jahres- und Zeitebenen-Holdout",
        "",
        "## Zweck",
        "",
        "Befund 2073 ließ `rf_05` als einzige Rollenfamilie mit gemeinsamem Gruppenabstand bei Kontinuität, Ereignisanteil und Mitgliederabdeckung zurück. Dieser Holdout prüft, ob der Vorsprung außerhalb der verwendeten 2025er 1h-Fenster bestehen bleibt.",
        "",
        "## Vorab Festgelegtes Design",
        "",
        "- ausschließlich Datenjahr `2024`",
        "- Assets: `BTC` und `SOL`",
        "- Zeitebenen: `1h` und `15m`",
        "- drei über das Jahr verteilte Fenster je Asset und Zeitebene",
        "- `12` Realfenster mit jeweils `1000` Beobachtungen",
        "- je Realfenster eine Shuffle- und eine Random-Sign-Kontrolle",
        "- insgesamt `36` frische Läufe mit jeweils frischer episodischer Memory",
        "- unveränderte acht Mitglieder von `rf_05` aus Befund 2066",
        "- Wahrnehmungsmodus: `world_relative`",
        f"- reproduzierbares Weltarchiv: `{_relative(archive)}`",
        "- keine neue Klasse, keine Handlung, kein Gate und keine Richtung",
        "",
        "Der Primärvergleich wurde vor dem Lauf auf drei Achsen festgelegt: Familienkontinuität, mittlerer Familienereignisanteil und mittlere Mitgliederabdeckung. Der Zeitebenen- und Assetvergleich ist sekundär.",
        "",
        "## Gesamtvergleich",
        "",
        "| Gruppe | Welten | Kontinuität real/shuffle/random | Real minus stärkste Kontrolle | Ereignisanteil real/shuffle/random | Abdeckung real/shuffle/random | Drift real/shuffle/random |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in comparisons:
        lines.append(
            f"| `{row['group']}` | {row['real_worlds']} | "
            f"{_fmt(row['real_family_continuity_score'])}/{_fmt(row['shuffle_family_continuity_score'])}/{_fmt(row['random_sign_family_continuity_score'])} | "
            f"{_fmt(row['real_minus_strongest_control_continuity'])} | "
            f"{_fmt(row['real_mean_family_event_share'], 4)}/{_fmt(row['shuffle_mean_family_event_share'], 4)}/{_fmt(row['random_sign_mean_family_event_share'], 4)} | "
            f"{_fmt(row['real_mean_member_coverage'])}/{_fmt(row['shuffle_mean_member_coverage'])}/{_fmt(row['random_sign_mean_member_coverage'])} | "
            f"{_fmt(row['real_member_distribution_drift'])}/{_fmt(row['shuffle_member_distribution_drift'])}/{_fmt(row['random_sign_member_distribution_drift'])} |"
        )
    lines.extend(
        [
            "",
            "## Paarvergleich",
            "",
            "Die Paarzahlen zeigen, in wie vielen direkt zugeordneten Fenstern Realwelt die jeweilige Kontrolle übertrifft. `gemeinsam` verlangt gleichzeitig höhere Abdeckung und höheren Ereignisanteil.",
            "",
            "| Gruppe | Ereignis real > shuffle/random | Abdeckung real > shuffle/random | gemeinsam real > shuffle/random |",
            "|---|---:|---:|---:|",
        ]
    )
    for row in comparisons:
        shuffle_n = row["paired_shuffle_windows"]
        random_n = row["paired_random_sign_windows"]
        lines.append(
            f"| `{row['group']}` | "
            f"{row['paired_shuffle_event_share_real_wins']}/{shuffle_n} / {row['paired_random_sign_event_share_real_wins']}/{random_n} | "
            f"{row['paired_shuffle_coverage_real_wins']}/{shuffle_n} / {row['paired_random_sign_coverage_real_wins']}/{random_n} | "
            f"{row['paired_shuffle_joint_real_advantage']}/{shuffle_n} / {row['paired_random_sign_joint_real_advantage']}/{random_n} |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"Im vorab festgelegten Gesamtvergleich liegt Realwelt auf folgenden Primärachsen über beiden Kontrollen: `{';'.join(carried_axes) or '-'}`.",
            "",
            f"Der gemeinsame Vorsprung von `rf_05` aus 2073 wird damit im unabhängigen Holdout nicht reproduziert. Realwelt liegt zwar auf allen drei Primärachsen über Shuffle, bleibt aber auf allen drei unter Random Sign. Im direkten Paarvergleich übertrifft Real die Random-Sign-Kontrolle gleichzeitig bei Abdeckung und Ereignisanteil nur in `{random_joint_wins}/{random_windows}` Fenstern.",
            "",
            "Die Asymmetrie der Kontrollen ist fachlich wichtig: Shuffle zerstört die Reihenfolge der lokalen Kerzenformen, Random Sign erhält dagegen die zeitliche Folge von Größenordnung, Dochten und Volumen und verändert vor allem die Körperrichtung. Das Profil spricht daher eher für eine Bindung an zeitliche Intensitäts- und Formfolge als für eine bereits belegte Bindung an reale Richtungsfolge. Diese Lesung ist eine Hypothese aus dem Kontrollmuster, kein neuer Mechanismus.",
            "",
            "Ein Vorsprung auf nur einer Achse reicht nicht, um `rf_05` als realweltspezifischen Bedeutungsraum zu lesen. Entscheidend ist, ob die relationale Familie zugleich breiter, häufiger und über die Fenster hinweg kontinuierlicher getragen wird.",
            "",
            "Die Teilgruppen zeigen, ob ein möglicher Gesamtabstand von einem einzelnen Asset oder einer Zeitebene stammt. Sie werden nicht nachträglich zur Hauptbestätigung umgedeutet.",
            "",
            "## Grenze",
            "",
            "Der Holdout erweitert Jahr, Asset und Zeitebene, bleibt aber bei Marktzeitreihen und `1000` Beobachtungen je Welt. Er prüft keine Robotiksensorik, keine andere Sinnesmodalität und keine feste Semantik. Alle Werte bleiben passive Forschungsmaße.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Prüft rf_05 in einem unabhängigen 2024-Holdout.")
    parser.add_argument("--memory", default=str(DEFAULT_MEMORY))
    parser.add_argument("--cohesion-detail", default=str(DEFAULT_COHESION))
    parser.add_argument("--data-dir", default=str(DEFAULT_DATA_DIR))
    parser.add_argument("--archive", default=str(DEFAULT_ARCHIVE))
    parser.add_argument("--debug-root", default=str(DEFAULT_DEBUG_ROOT))
    parser.add_argument("--out-prefix", default=str(DEFAULT_OUT_PREFIX))
    args = parser.parse_args()

    memory = _resolve(args.memory)
    cohesion = _resolve(args.cohesion_detail)
    data_dir = _resolve(args.data_dir)
    archive = _resolve(args.archive)
    debug_root = _resolve(args.debug_root)
    out_prefix = _resolve(args.out_prefix)

    targets = _load_targets(memory, ["rf_05"])
    source_counts = _load_source_member_counts(cohesion, targets)
    records = _build_world_records(data_dir)
    _write_control_archive(archive, records)
    member_rows = _run_worlds(records, targets, debug_root)
    world_rows = _build_world_rows(member_rows)
    comparisons = _build_comparisons(member_rows, targets, source_counts)
    paired_rows = _build_paired(world_rows)
    _add_pair_counts(comparisons, paired_rows)

    _write_csv(out_prefix.with_suffix(".worlds.csv"), world_rows)
    _write_csv(out_prefix.with_suffix(".paired.csv"), paired_rows)
    _write_csv(out_prefix.with_suffix(".comparison.csv"), comparisons)
    _write_markdown(out_prefix.with_suffix(".md"), comparisons, archive)

    print(f"worlds={len(records)}")
    print(f"member_rows={len(member_rows)}")
    print(f"world_rows={len(world_rows)}")
    print(f"comparison_rows={len(comparisons)}")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
