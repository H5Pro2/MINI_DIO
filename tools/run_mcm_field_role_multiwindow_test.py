from __future__ import annotations

import argparse
import csv
import subprocess
import sys
from collections import Counter
from pathlib import Path

from build_equal_length_null_worlds import build_null_worlds
from create_csv_slice import create_slice
from report_mcm_field_role_repro_2025 import (
    ROOT,
    SOURCE_2024,
    _comparison_rows,
    _float,
    _mean,
    _phase_family_rows,
    _read_csv,
)


DEFAULT_SPECS = [
    ("BTC", "data/1-12_2025_5m_BTCUSDT.csv"),
    ("SOL", "data/1-12_2025_5m_SOLUSDT.csv"),
]


def _resolve(value: str | Path) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _safe_name(value: str) -> str:
    return "".join(ch.lower() if ch.isalnum() else "_" for ch in value).strip("_")


def _run_mini(data_path: Path, memory_path: Path, debug_root: Path, label: str) -> None:
    report_path = debug_root / "dio_mini_lauf_1" / "mini_report.json"
    if report_path.exists():
        return
    cmd = [
        sys.executable,
        "-m",
        "mini_dio.run_mini",
        "--data",
        str(data_path.relative_to(ROOT)),
        "--runs",
        "1",
        "--reset-memory",
        "--memory",
        str(memory_path.relative_to(ROOT)),
        "--debug-root",
        str(debug_root.relative_to(ROOT)),
        "--world-label",
        label,
        "--sense-mode",
        "world_relative",
    ]
    subprocess.run(cmd, cwd=ROOT, check=True, stdout=subprocess.DEVNULL)


def _ensure_worlds(asset: str, source: Path, start: int, rows: int, seed: int, data_dir: Path, tag: str) -> dict[str, Path]:
    stem = f"kontrolliert_{_safe_name(tag)}_{_safe_name(asset)}_start{start}_rows{rows}"
    real_path = data_dir / f"{stem}.csv"
    if not real_path.exists():
        result = create_slice(source, real_path, start=start, rows=rows)
        if int(result["rows_written"]) != rows:
            raise ValueError(f"{source} schrieb {result['rows_written']} statt {rows} Zeilen")
    null_prefix = data_dir / f"synthetic_{_safe_name(tag)}_{_safe_name(asset)}_start{start}_rows{rows}_null"
    random_path = null_prefix.with_name(f"{null_prefix.name}_random_sign_{rows}.csv")
    shuffle_path = null_prefix.with_name(f"{null_prefix.name}_shuffle_order_{rows}.csv")
    if not random_path.exists() or not shuffle_path.exists():
        build_null_worlds(real_path, null_prefix, rows=rows, seed=seed)
    return {
        "real": real_path,
        "null_random": random_path,
        "null_shuffle": shuffle_path,
    }


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames: list[str] = []
    seen: set[str] = set()
    for row in rows:
        for key in row.keys():
            if key not in seen:
                seen.add(key)
                fieldnames.append(key)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _kind_summary(summary_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for kind in ["real", "null_random", "null_shuffle"]:
        group = [row for row in summary_rows if row.get("kind") == kind]
        out.append(
            {
                "kind": kind,
                "worlds": len(group),
                "avg_kernfamilien": _mean([_float(row["kernfamilien"]) for row in group]),
                "avg_source_family_overlap": _mean([_float(row["source_family_overlap"]) for row in group]),
                "avg_source_kern_overlap": _mean([_float(row["source_kern_overlap"]) for row in group]),
                "avg_afterimage_delta": _mean([_float(row["avg_afterimage_delta"]) for row in group]),
                "avg_temporal_delta": _mean([_float(row["avg_temporal_delta"]) for row in group]),
                "states": "; ".join(
                    f"{name}:{count}"
                    for name, count in Counter(str(row["reproduction_state"]) for row in group).most_common()
                ),
            }
        )
    return out


def _asset_window_summary(summary_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str], dict[str, dict[str, object]]] = {}
    for row in summary_rows:
        key = (str(row["asset"]), str(row["window_start"]))
        grouped.setdefault(key, {})[str(row["kind"])] = row
    out: list[dict[str, object]] = []
    for (asset, start), rows in sorted(grouped.items(), key=lambda item: (item[0][0], int(item[0][1]))):
        real = rows.get("real", {})
        nulls = [rows.get("null_random", {}), rows.get("null_shuffle", {})]
        source_edge = _float(real.get("source_family_overlap")) - max(
            _float(row.get("source_family_overlap")) for row in nulls
        )
        kern_edge = _float(real.get("source_kern_overlap")) - max(_float(row.get("source_kern_overlap")) for row in nulls)
        after_edge = _float(real.get("avg_afterimage_delta")) - max(_float(row.get("avg_afterimage_delta")) for row in nulls)
        temporal_edge = _float(real.get("avg_temporal_delta")) - max(_float(row.get("avg_temporal_delta")) for row in nulls)
        field_edge_score = (
            (source_edge * 0.25)
            + (kern_edge * 0.45)
            + (after_edge * 0.15)
            + (temporal_edge * 0.15)
        )
        if kern_edge > 0.04 and temporal_edge >= 0.0:
            state = "realwelt_kernnaehe_staerker"
        elif source_edge > 0.04 and after_edge >= 0.0:
            state = "realwelt_anschluss_staerker"
        elif kern_edge < -0.04 and source_edge < -0.04:
            state = "nullwelt_staerker"
        elif field_edge_score > 0.025 and kern_edge > 0.0:
            state = "graduell_realnaeher_kern"
        elif field_edge_score < -0.025:
            state = "graduell_nullnaeher"
        elif after_edge > 0.0 and temporal_edge > 0.0 and kern_edge <= 0.0:
            state = "graduell_realer_nachhall_ohne_kern"
        elif kern_edge > 0.0 and (after_edge < 0.0 or temporal_edge < 0.0):
            state = "graduell_kernnaehe_ohne_feldzeitvorsprung"
        else:
            state = "graduell_gemischt"
        out.append(
            {
                "asset": asset,
                "window_start": start,
                "source_edge": source_edge,
                "kern_edge": kern_edge,
                "afterimage_edge": after_edge,
                "temporal_edge": temporal_edge,
                "field_edge_score": field_edge_score,
                "reading": state,
            }
        )
    return out


def _write_md(
    path: Path,
    summary_rows: list[dict[str, object]],
    kind_rows: list[dict[str, object]],
    window_rows: list[dict[str, object]],
    title: str,
) -> None:
    lines = [
        f"# {title}",
        "",
        "## Grundfrage",
        "",
        "Bleibt der Realwelt-Vorsprung ueber mehrere Startpunkte hinweg sichtbar, oder ist er nur ein Fensterartefakt?",
        "",
        "## Methode",
        "",
        "- Pro Asset und Startpunkt wird ein Realfenster geschnitten.",
        "- Daraus entstehen zwei assetnahe Nullwelten: Random-Sign und Shuffle-Order.",
        "- Alle Laeufe bleiben passiv und nutzen `world_relative`.",
        "- Bewertet werden Quellennaehe, Kernnaehe, Nachhall-Delta und Feldzeit-Delta.",
        "",
        "## Gruppenvergleich",
        "",
        "| Gruppe | Welten | Kernfamilien Ø | Quellennähe Ø | Kernnähe Ø | Nachhall-Delta Ø | Feldzeit-Delta Ø | Zustände |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in kind_rows:
        lines.append(
            f"| `{row['kind']}` | {row['worlds']} | {_float(row['avg_kernfamilien']):.2f} | "
            f"{_float(row['avg_source_family_overlap']):.3f} | {_float(row['avg_source_kern_overlap']):.3f} | "
            f"{_float(row['avg_afterimage_delta']):.4f} | {_float(row['avg_temporal_delta']):.4f} | `{row['states']}` |"
        )
    lines.extend(
        [
            "",
            "## Fensterlesung",
            "",
            "| Asset | Start | Quellenvorsprung | Kernvorsprung | Nachhallvorsprung | Feldzeitvorsprung | Feldvorsprung | Lesung |",
            "|---|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in window_rows:
        lines.append(
            f"| {row['asset']} | {row['window_start']} | {_float(row['source_edge']):.4f} | "
            f"{_float(row['kern_edge']):.4f} | {_float(row['afterimage_edge']):.4f} | "
            f"{_float(row['temporal_edge']):.4f} | {_float(row['field_edge_score']):.4f} | `{row['reading']}` |"
        )
    state_counts = Counter(str(row["reading"]) for row in window_rows)
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Fensterzustände:",
        ]
    )
    for state, count in state_counts.most_common():
        lines.append(f"- `{state}`: {count}")
    lines.extend(
        [
            "",
            "Der Test trennt Reifung nicht mehr an einem einzelnen Lauf.",
            "Er liest, ob Realwelt-Vorsprung als wiederkehrender Fenstereffekt erscheint oder ob Nullwelten gleich stark anschließen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte der Test auf mehr Assets mit vollständigen Jahresdateien erweitert werden.",
            "Wenn die Fensterlesung stabil bleibt, kann daraus eine robustere Reifungs-Metrik für die passive Feldrollen-Memory entstehen.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _parse_spec(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("world spec must be ASSET=path.csv")
    asset, path = value.split("=", 1)
    return asset.strip().upper(), _resolve(path.strip())


def main() -> int:
    parser = argparse.ArgumentParser(description="Fuehrt einen passiven MCM-Feldrollen-Mehrfenster-Test aus.")
    parser.add_argument("--world", action="append", type=_parse_spec, help="ASSET=CSV; Standard: BTC und SOL 2025 5m.")
    parser.add_argument("--start", action="append", type=int, default=None)
    parser.add_argument("--rows", type=int, default=17000)
    parser.add_argument("--debug-root", default="debug/1845_multiwindow_field_roles")
    parser.add_argument("--data-dir", default="data/1845_multiwindow")
    parser.add_argument("--out-md", default="docs/befunde/1001-2000/1751-2000/1845_MCM_FELDROLLEN_MEHRFENSTER_TEST.md")
    parser.add_argument("--out-csv", default="docs/befunde/1001-2000/1751-2000/1845_MCM_FELDROLLEN_MEHRFENSTER_TEST.csv")
    parser.add_argument("--title", default="1845 - MCM-Feldrollen-Memory: automatischer Mehrfenster-Test")
    parser.add_argument("--tag", default="1845")
    args = parser.parse_args()

    specs = args.world or [(asset, _resolve(path)) for asset, path in DEFAULT_SPECS]
    debug_root = _resolve(args.debug_root)
    data_dir = _resolve(args.data_dir)
    source_rows = _read_csv(SOURCE_2024)
    detail_rows: list[dict[str, object]] = []
    kind_by_label: dict[tuple[str, str], str] = {}
    start_by_label: dict[tuple[str, str], int] = {}

    starts = args.start or [0, 17000, 34000]
    for asset, source in specs:
        for start in starts:
            worlds = _ensure_worlds(
                asset,
                source,
                start=start,
                rows=args.rows,
                seed=184500 + start + len(asset),
                data_dir=data_dir,
                tag=args.tag,
            )
            for kind, path in worlds.items():
                label = f"{asset.lower()}_start{start}_{kind}_{args.rows}"
                run_root = debug_root / label
                memory_path = run_root / "memory.json"
                _run_mini(path, memory_path, run_root, label)
                kind_by_label[(asset, f"start{start}_{kind}_{args.rows}")] = kind
                start_by_label[(asset, f"start{start}_{kind}_{args.rows}")] = start
                for row in _phase_family_rows(asset, f"start{start}_{kind}_{args.rows}", str(run_root.relative_to(ROOT) / "dio_mini_lauf_1")):
                    row["kind"] = kind
                    row["window_start"] = start
                    detail_rows.append(row)

    summary_rows = _comparison_rows(source_rows, detail_rows)
    for row in summary_rows:
        key = (str(row["asset"]), str(row["label"]))
        row["kind"] = kind_by_label[key]
        row["window_start"] = start_by_label[key]
    kind_rows = _kind_summary(summary_rows)
    window_rows = _asset_window_summary(summary_rows)
    csv_rows = (
        [{**row, "row_type": "summary"} for row in summary_rows]
        + [{**row, "row_type": "kind_summary"} for row in kind_rows]
        + [{**row, "row_type": "window_summary"} for row in window_rows]
        + [{**row, "row_type": "detail"} for row in detail_rows]
    )
    _write_csv(_resolve(args.out_csv), csv_rows)
    _write_md(_resolve(args.out_md), summary_rows, kind_rows, window_rows, args.title)
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
