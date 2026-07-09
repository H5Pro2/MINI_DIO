from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from befunde_paths import befunde_root


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = befunde_root(ROOT) / "1581_MEHRROLLEN_FENSTERSUCHE_DOGE_XRP_BTC.md"
DEFAULT_CSV = befunde_root(ROOT) / "1581_MEHRROLLEN_FENSTERSUCHE_DOGE_XRP_BTC.csv"
DEFAULT_TITLE = "Mehrrollen-Fenstersuche DOGE/XRP/BTC"
DEFAULT_QUESTION = "In welchen Fenstern kippt Einzelrekopplung in Uebergang oder breitere Mehrrollennaehe?"


DEFAULT_WORLD_SPECS = [
    ("DOGE_2024_5M_10K", "data/kontrolliert_doge_2024_5m_10k_DOGEUSDT.csv"),
    ("XRP_2024_5M_10K", "data/kontrolliert_xrp_2024_5m_10k_XRPUSDT.csv"),
    ("BTC_2024_5M_10K", "data/kontrolliert_btc_2024_5m_10k_BTCUSDT.csv"),
]


def _path(value: str | Path) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _safe_label(value: str) -> str:
    result = []
    for char in value.lower():
        if char.isalnum():
            result.append(char)
        elif result and result[-1] != "-":
            result.append("-")
    return "".join(result).strip("-") or "welt"


def _parse_world_spec(value: str) -> tuple[str, str]:
    if "=" not in value:
        path = Path(value)
        return path.stem.upper(), value
    name, path_text = value.split("=", 1)
    return name.strip(), path_text.strip()


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    if result != result:
        return 0.0
    return result


def _int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def _write_rows(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _run_mini(data_path: Path, debug_root: Path, memory_path: Path) -> dict:
    command = [
        sys.executable,
        "-m",
        "mini_dio.run_mini",
        "--data",
        str(data_path.relative_to(ROOT)),
        "--runs",
        "1",
        "--memory",
        str(memory_path.relative_to(ROOT)),
        "--debug-root",
        str(debug_root.relative_to(ROOT)),
        "--reset-memory",
        "--sense-mode",
        "world_relative",
    ]
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        result.check_returncode()
    report_path = debug_root / "dio_mini_lauf_1" / "mini_report.json"
    return json.loads(report_path.read_text(encoding="utf-8"))


def _load_memory_roles(memory_path: Path) -> list[dict[str, object]]:
    memory = json.loads(memory_path.read_text(encoding="utf-8"))
    roles = dict(memory.get("mcm_field_episode_memory", {}) or {})
    rows: list[dict[str, object]] = []
    for symbol, item in roles.items():
        role = dict(item or {})
        rows.append(
            {
                "symbol": str(symbol),
                "duration": _int(role.get("duration")),
                "state": str(role.get("episode_state") or ""),
                "transition": str(role.get("transition") or ""),
                "carry": _float(role.get("avg_mcm_carry_quality")),
                "rekopplung": _float(role.get("avg_mcm_rekopplung_quality")),
                "strain": _float(role.get("avg_mcm_strain_quality")),
            }
        )
    return rows


def _classify(roles: list[dict[str, object]]) -> str:
    durable = [role for role in roles if _int(role.get("duration")) >= 10]
    long_roles = [role for role in roles if _int(role.get("duration")) >= 100]
    strain_roles = [role for role in roles if str(role.get("state")) == "field_strained"]
    if len(durable) >= 3:
        return "mehrrollen_kandidat"
    if len(durable) >= 2 and strain_roles:
        return "uebergang_mit_randkontakt"
    if len(long_roles) >= 2:
        return "zweikern_ohne_randkontakt"
    return "einzelrekopplung"


def _scan_world(name: str, source: Path, starts: list[int], size: int) -> list[dict[str, object]]:
    fieldnames, source_rows = _read_rows(source)
    result_rows: list[dict[str, object]] = []
    for start in starts:
        window = source_rows[start : start + size]
        if len(window) < size:
            continue
        safe_name = _safe_label(name)
        label = f"{safe_name}_start{start}_size{size}"
        data_path = ROOT / "data" / f"scan_{label}.csv"
        debug_root = ROOT / "debug" / "multirole_window_scan" / label
        memory_path = ROOT / "memory" / "multirole_window_scan" / f"{label}.json"
        if memory_path.exists():
            memory_path.unlink()
        _write_rows(data_path, fieldnames, window)
        report = _run_mini(data_path, debug_root, memory_path)
        roles = _load_memory_roles(memory_path)
        durable = [role for role in roles if _int(role.get("duration")) >= 10]
        long_roles = [role for role in roles if _int(role.get("duration")) >= 100]
        strain_roles = [role for role in roles if str(role.get("state")) == "field_strained"]
        top_roles = sorted(roles, key=lambda role: _int(role.get("duration")), reverse=True)[:5]
        result_rows.append(
            {
                "world": name,
                "start": start,
                "end": start + size,
                "data_path": str(data_path.relative_to(ROOT)),
                "class": _classify(roles),
                "role_count": len(roles),
                "durable_role_count": len(durable),
                "long_role_count": len(long_roles),
                "strain_role_count": len(strain_roles),
                "unique_symbols": _int(report.get("unique_symbols")),
                "episodes": _int(report.get("episodes")),
                "avg_rekopplung": _float(report.get("avg_mcm_rekopplung_quality")),
                "avg_carry": _float(report.get("avg_mcm_carry_quality")),
                "avg_strain": _float(report.get("avg_mcm_strain_quality")),
                "avg_afterimage": _float(report.get("avg_mini_afterimage")),
                "top_roles": "; ".join(
                    f"{role['symbol']}:{role['state']}:{role['duration']}" for role in top_roles
                ),
            }
        )
    return result_rows


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "world",
        "start",
        "end",
        "class",
        "role_count",
        "durable_role_count",
        "long_role_count",
        "strain_role_count",
        "unique_symbols",
        "episodes",
        "avg_rekopplung",
        "avg_carry",
        "avg_strain",
        "avg_afterimage",
        "top_roles",
        "data_path",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object, digits: int = 4) -> str:
    return f"{_float(value):.{digits}f}"


def _write_md(
    rows: list[dict[str, object]],
    path: Path,
    *,
    title: str = DEFAULT_TITLE,
    question: str = DEFAULT_QUESTION,
    world_description: str = "Aus DOGE, XRP und BTC 2024 5m 10k wurden mehrere 1000er-Fenster passiv geschnitten und mit frischem Memory gelesen.",
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    ordered = sorted(
        rows,
        key=lambda row: (
            _int(row.get("durable_role_count")),
            _int(row.get("strain_role_count")),
            _float(row.get("avg_afterimage")),
        ),
        reverse=True,
    )
    class_counts: dict[str, int] = {}
    for row in rows:
        key = str(row.get("class") or "-")
        class_counts[key] = class_counts.get(key, 0) + 1
    lines = [
        f"# {title}",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Grundfrage",
        "",
        question,
        "",
        "## Unterpruefung",
        "",
        world_description,
        "Die Diagnose ist passiv und erzeugt keine Handlung.",
        "",
        "## Klassenverteilung",
        "",
    ]
    for key, value in sorted(class_counts.items()):
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(
        [
            "",
            "## Fenster",
            "",
            "| Welt | Start | Klasse | Rollen | Dauerrollen | Lange Rollen | Strain | Rekopplung | Carry | Strain-Q | Top-Rollen |",
            "|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in ordered:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["world"]),
                    str(row["start"]),
                    str(row["class"]),
                    str(row["role_count"]),
                    str(row["durable_role_count"]),
                    str(row["long_role_count"]),
                    str(row["strain_role_count"]),
                    _fmt(row["avg_rekopplung"]),
                    _fmt(row["avg_carry"]),
                    _fmt(row["avg_strain"]),
                    str(row["top_roles"]).replace("|", "/"),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Die Fenstersuche trennt Asset-Faerbung von lokaler Feldlage. Entscheidend ist nicht, welches Asset gelesen wird, sondern ob das konkrete Fenster mehrere MCM-Feldrollen hervorbringt.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte der staerkste neu gefundene Uebergangs- oder Mehrrollen-Kandidat als Real-Sleep-Real-Kette mit Sleep-Reorganisation reproduziert werden.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Scannt 10k-Welten nach 1000er-Mehrrollenfenstern.")
    parser.add_argument("--window-size", type=int, default=1000)
    parser.add_argument("--starts", default="0,1000,2000,3000,4000,5000,6000,7000,8000,9000")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--csv-out", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--title", default=DEFAULT_TITLE)
    parser.add_argument("--question", default=DEFAULT_QUESTION)
    parser.add_argument("--world-description", default=None)
    parser.add_argument(
        "--world",
        action="append",
        default=[],
        help="Weltangabe als NAME=pfad.csv. Ohne --world werden DOGE/XRP/BTC genutzt.",
    )
    args = parser.parse_args()
    starts = [_int(item.strip()) for item in str(args.starts).split(",") if item.strip()]
    world_specs = [_parse_world_spec(item) for item in args.world] if args.world else DEFAULT_WORLD_SPECS
    rows: list[dict[str, object]] = []
    for name, path_text in world_specs:
        rows.extend(_scan_world(name, _path(path_text), starts, args.window_size))
    _write_csv(rows, args.csv_out if args.csv_out.is_absolute() else ROOT / args.csv_out)
    world_description = args.world_description
    if not world_description:
        world_names = ", ".join(name for name, _ in world_specs)
        world_description = (
            f"Aus {world_names} wurden mehrere {args.window_size}er-Fenster passiv geschnitten "
            "und mit frischem Memory gelesen."
        )
    _write_md(
        rows,
        args.out if args.out.is_absolute() else ROOT / args.out,
        title=args.title,
        question=args.question,
        world_description=world_description,
    )
    print(json.dumps({"rows": len(rows), "out": str(args.out), "csv": str(args.csv_out)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
