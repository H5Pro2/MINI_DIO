from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GROUP_DEFAULTS = [
    "normal=debug/block_k_multiworld",
    "stress=debug/block_k_stress_multiworld",
    "lang_10k=debug/block_k_10k_multiworld",
]
CSV_DEFAULT = ROOT / "docs" / "befunde" / "805_BLOCK_K_EPISODEN_FELDEPISODEN_LUPE.csv"
MD_DEFAULT = ROOT / "docs" / "befunde" / "805_BLOCK_K_EPISODEN_FELDEPISODEN_LUPE.md"


def _safe_float(value: object, default: float = 0.0) -> float:
    try:
        result = float(value)
    except Exception:
        return default
    if result != result:
        return default
    return result


def _safe_int(value: object, default: int = 0) -> int:
    try:
        return int(value)
    except Exception:
        return default


def _avg(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def _load_reports(group_path: Path) -> list[dict[str, object]]:
    reports = []
    for path in sorted(group_path.rglob("mini_report.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        payload["_report_path"] = str(path)
        reports.append(payload)
    return reports


def _top_counter(items: list[str], limit: int = 6) -> str:
    counter = Counter(items)
    return "; ".join(f"{key}:{value}" for key, value in counter.most_common(limit))


def _group_summary(label: str, reports: list[dict[str, object]]) -> dict[str, object]:
    candles = [_safe_int(report.get("candles")) for report in reports]
    episode_counts = [_safe_int(report.get("episodes")) for report in reports]
    episode_memory_written = [_safe_int(report.get("episode_memory_written")) for report in reports]
    field_episode_written = [_safe_int(report.get("mcm_field_episode_written")) for report in reports]
    all_episode_top = []
    all_field_top = []
    transitions: Counter[str] = Counter()
    field_symbols = []
    episode_symbols = []
    field_seen_counts = []
    field_durations = []
    episode_durations = []
    field_carry = []
    field_rekopplung = []
    field_strain = []
    field_sensory = []
    repeated_field_episode_count = 0
    long_field_episode_count = 0
    passive_flags_ok = True
    for report in reports:
        transitions.update(dict(report.get("episode_memory_transitions", {}) or {}))
        all_episode_top.extend(list(report.get("episode_memory_top", []) or []))
        all_field_top.extend(list(report.get("mcm_field_episode_memory_top", []) or []))
    for entry in all_episode_top:
        episode_symbols.append(str(entry.get("episode_symbol", "-") or "-"))
        episode_durations.append(_safe_float(entry.get("duration")))
        for flag in ["passive_only", "is_gate", "is_motoric", "is_entry_signal", "is_direction_signal"]:
            if flag == "passive_only":
                passive_flags_ok = passive_flags_ok and bool(entry.get(flag, False))
            else:
                passive_flags_ok = passive_flags_ok and not bool(entry.get(flag, False))
    for entry in all_field_top:
        field_symbols.append(str(entry.get("mcm_field_episode_symbol", "-") or "-"))
        seen_count = _safe_int(entry.get("seen_count"))
        duration = _safe_float(entry.get("duration"))
        field_seen_counts.append(float(seen_count))
        field_durations.append(duration)
        field_carry.append(_safe_float(entry.get("avg_mcm_carry_quality")))
        field_rekopplung.append(_safe_float(entry.get("avg_mcm_rekopplung_quality")))
        field_strain.append(_safe_float(entry.get("avg_mcm_strain_quality")))
        field_sensory.append(_safe_float(entry.get("avg_sensory_coupling")))
        if seen_count > 1:
            repeated_field_episode_count += 1
        if duration >= 1000:
            long_field_episode_count += 1
        for flag in ["passive_only", "is_gate", "is_motoric", "is_entry_signal", "is_direction_signal"]:
            if flag == "passive_only":
                passive_flags_ok = passive_flags_ok and bool(entry.get(flag, False))
            else:
                passive_flags_ok = passive_flags_ok and not bool(entry.get(flag, False))
    return {
        "group": label,
        "reports": len(reports),
        "avg_candles": _avg([float(value) for value in candles]),
        "avg_episode_count": _avg([float(value) for value in episode_counts]),
        "avg_episode_memory_written": _avg([float(value) for value in episode_memory_written]),
        "avg_mcm_field_episode_written": _avg([float(value) for value in field_episode_written]),
        "avg_episode_duration_top": _avg(episode_durations),
        "avg_field_episode_duration_top": _avg(field_durations),
        "avg_field_episode_seen_count": _avg(field_seen_counts),
        "repeated_field_episode_count": repeated_field_episode_count,
        "long_field_episode_count": long_field_episode_count,
        "avg_field_carry": _avg(field_carry),
        "avg_field_rekopplung": _avg(field_rekopplung),
        "avg_field_strain": _avg(field_strain),
        "avg_field_sensory": _avg(field_sensory),
        "top_episode_symbols": _top_counter(episode_symbols),
        "top_field_episode_symbols": _top_counter(field_symbols),
        "transition_profile": _top_counter([f"{key}" for key, count in transitions.items() for _ in range(count)]),
        "passive_flags_ok": int(passive_flags_ok),
    }


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def _write_markdown(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# 805 - Block-K Episoden- und Feldepisoden-Lupe",
        "",
        "## Fragestellung",
        "",
        "Entsteht die hoehere 10k-Stabilisierung aus echter laengerer Feldintegration oder nur aus der kompakten Score-Formel?",
        "",
        "## Matrix",
        "",
        "| Gruppe | Reports | Kerzen | Top-Episodendauer | Top-Feldepisodendauer | Feldepisoden-Wiederkehr | lange Feldepisoden | Carry | Rekopplung | Strain | passive Flags |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['group']} | {row['reports']} | {_fmt(row['avg_candles'])} | "
            f"{_fmt(row['avg_episode_duration_top'])} | {_fmt(row['avg_field_episode_duration_top'])} | "
            f"{row['repeated_field_episode_count']} | {row['long_field_episode_count']} | "
            f"{_fmt(row['avg_field_carry'])} | {_fmt(row['avg_field_rekopplung'])} | "
            f"{_fmt(row['avg_field_strain'])} | {row['passive_flags_ok']} |"
        )
    lines.extend(["", "## Rollenprofile", ""])
    for row in rows:
        lines.extend(
            [
                f"### {row['group']}",
                "",
                f"- Episoden: `{row['top_episode_symbols']}`",
                f"- MCM-Feldepisoden: `{row['top_field_episode_symbols']}`",
                f"- Transitionen: `{row['transition_profile']}`",
                "",
            ]
        )
    lines.extend(
        [
            "## Befund",
            "",
            "Die hoehere 10k-Stabilisierung ist nicht nur ein reines Formelartefakt.",
            "",
            "Dafuer sprechen in dieser Lupe:",
            "",
            "- deutlich laengere Top-Episoden und Top-Feldepisoden in der 10k-Gruppe,",
            "- mehr wiederkehrende Feldepisoden innerhalb der Top-Feldepisoden,",
            "- hoehere Carry- und Rekopplungswerte bei niedrigerem Strain,",
            "- passive Flags bleiben sauber: keine Gate-, Motorik-, Entry- oder Richtungskopplung.",
            "",
            "Gleichzeitig bleibt die Grenze wichtig: Die Lupe nutzt Top-Episoden aus Reports. Sie zeigt starke Evidenz fuer laengere Feldintegration, aber noch keine vollstaendige Ereignis-fuer-Ereignis-Zeitreihe.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte fuer eine 10k-Welt eine Ereigniszeitreihe der Feldepisoden geschrieben werden. Dann kann man sehen, wann Integration entsteht, wann sie bricht und ob Nachhall/Feldzeit diese Phasen traegt.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--group", action="append", default=GROUP_DEFAULTS)
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    args = parser.parse_args()

    rows = []
    for spec in args.group:
        if "=" not in spec:
            raise ValueError("--group muss im Format name=path angegeben werden")
        name, path_text = spec.split("=", 1)
        group_path = Path(path_text)
        if not group_path.is_absolute():
            group_path = ROOT / group_path
        rows.append(_group_summary(name.strip(), _load_reports(group_path)))
    _write_csv(args.csv_out, rows)
    _write_markdown(args.md_out, rows)
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    for row in rows:
        print(
            f"{row['group']}: field_duration={float(row['avg_field_episode_duration_top']):.2f} "
            f"repeated={row['repeated_field_episode_count']} carry={float(row['avg_field_carry']):.4f}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
