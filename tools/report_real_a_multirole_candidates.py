from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime
from pathlib import Path

from befunde_paths import befunde_root


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DEBUG_ROOT = ROOT / "debug" / "real_sleep_real"
DEFAULT_OUT = befunde_root(ROOT) / "1574_REAL_A_MEHRROLLEN_KANDIDATEN.md"
DEFAULT_CSV = befunde_root(ROOT) / "1574_REAL_A_MEHRROLLEN_KANDIDATEN.csv"


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


def _summary_path(label_dir: Path) -> Path:
    return label_dir / "real_sleep_real_summary.json"


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _resolve_memory_path(summary: dict) -> Path | None:
    raw = str(summary.get("memory_a_real") or "")
    if not raw:
        return None
    path = Path(raw)
    if not path.is_absolute():
        path = ROOT / path
    return path if path.exists() else None


def _metric(summary: dict, name: str, side: str = "real_a") -> float:
    metrics = dict(dict(summary.get("comparison", {}) or {}).get("metrics", {}) or {})
    item = dict(metrics.get(name, {}) or {})
    return _float(item.get(side))


def _role_rows(memory: dict) -> list[dict[str, object]]:
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
                "sensory": _float(role.get("avg_sensory_coupling")),
                "hearing_gap": _float(role.get("avg_hearing_field_gap")),
                "visual_gap": _float(role.get("avg_visual_field_gap")),
                "carrier_family_count": _int(role.get("carrier_family_count")),
            }
        )
    return rows


def _classify(row: dict[str, object]) -> str:
    durable_roles = _int(row.get("durable_role_count"))
    strain_roles = _int(row.get("strain_role_count"))
    sleep_combos = _int(row.get("sleep_combination_trace_count"))
    if durable_roles >= 3 and sleep_combos > 0:
        return "real_a_mehrrollen_mit_sleep_kombination"
    if durable_roles >= 3:
        return "real_a_mehrrollen_ohne_sleep_nachweis"
    if durable_roles >= 2 and strain_roles > 0:
        return "uebergang_mit_randkontakt"
    if durable_roles <= 1:
        return "einzelrolle_oder_spikefeld"
    return "unklarer_uebergang"


def _analyze_label(label_dir: Path) -> dict[str, object] | None:
    summary_file = _summary_path(label_dir)
    if not summary_file.exists():
        return None
    summary = _load_json(summary_file)
    memory_path = _resolve_memory_path(summary)
    if memory_path is None:
        return None
    memory = _load_json(memory_path)
    roles = _role_rows(memory)
    total_duration = sum(_int(role["duration"]) for role in roles)
    durable_roles = [role for role in roles if _int(role["duration"]) >= 10]
    long_roles = [role for role in roles if _int(role["duration"]) >= 100]
    strain_roles = [role for role in roles if str(role["state"]) == "field_strained"]
    carried_roles = [role for role in roles if str(role["state"]) == "field_carried"]
    role_count = len(roles)
    sleep = dict(summary.get("sleep_reorganization_memory", {}) or {})
    followup = dict(summary.get("sleep_reorganization_followup", {}) or {})

    def share(items: list[dict[str, object]]) -> float:
        return sum(_int(role["duration"]) for role in items) / max(1, total_duration)

    top_roles = sorted(roles, key=lambda role: _int(role["duration"]), reverse=True)[:5]
    row: dict[str, object] = {
        "label": str(summary.get("label") or label_dir.name),
        "data_path": str(summary.get("data_path") or ""),
        "follow_data_path": str(summary.get("follow_data_path") or ""),
        "role_count": role_count,
        "durable_role_count": len(durable_roles),
        "long_role_count": len(long_roles),
        "strain_role_count": len(strain_roles),
        "carried_role_count": len(carried_roles),
        "durable_duration_share": share(durable_roles),
        "strain_duration_share": share(strain_roles),
        "top_role_duration_share": (_int(top_roles[0]["duration"]) / max(1, total_duration)) if top_roles else 0.0,
        "real_a_episodes": _metric(summary, "episodes"),
        "real_a_unique_symbols": _metric(summary, "unique_symbols"),
        "real_a_rekopplung": _metric(summary, "avg_mcm_rekopplung_quality"),
        "real_a_carry": _metric(summary, "avg_mcm_carry_quality"),
        "real_a_strain": _metric(summary, "avg_mcm_strain_quality"),
        "real_a_afterimage": _metric(summary, "avg_mini_afterimage"),
        "sleep_touched_role_count": _int(sleep.get("touched_role_count")),
        "sleep_combination_trace_count": _int(sleep.get("combination_trace_count")),
        "sleep_full_reactivated": _int(followup.get("combination_fully_reactivated_count")),
        "top_roles": "; ".join(
            f"{role['symbol']}:{role['state']}:{role['duration']}" for role in top_roles
        ),
    }
    row["candidate_class"] = _classify(row)
    return row


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "label",
        "candidate_class",
        "role_count",
        "durable_role_count",
        "long_role_count",
        "strain_role_count",
        "durable_duration_share",
        "strain_duration_share",
        "top_role_duration_share",
        "real_a_unique_symbols",
        "real_a_rekopplung",
        "real_a_carry",
        "real_a_strain",
        "real_a_afterimage",
        "sleep_touched_role_count",
        "sleep_combination_trace_count",
        "sleep_full_reactivated",
        "top_roles",
        "data_path",
        "follow_data_path",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object, digits: int = 4) -> str:
    return f"{_float(value):.{digits}f}"


def _write_md(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    ordered = sorted(
        rows,
        key=lambda row: (
            _int(row.get("durable_role_count")),
            _int(row.get("sleep_combination_trace_count")),
            _float(row.get("durable_duration_share")),
        ),
        reverse=True,
    )
    lines = [
        "# Real-A-Mehrrollen-Kandidaten",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Grundfrage",
        "",
        "Welche vorhandenen Real-A-Welten beruehren bereits mehrere MCM-Feldrollen, bevor die Offline-/Sleep-Reorganisation arbeitet?",
        "",
        "## Unterpruefung",
        "",
        "Die Diagnose liest die gespeicherten `memory_A_real_run.json` Dateien aus den bisherigen Real-Sleep-Real-Laeufen.",
        "Bewertet wird passiv:",
        "",
        "- wie viele MCM-Feldrollen in Real-A entstanden sind,",
        "- wie viele davon laenger als kurze Spikes getragen wurden,",
        "- ob Rand-/Strain-Rollen nur als kurze Kontaktpunkte oder als Feldanteil auftreten,",
        "- ob danach Sleep-Kombinationen sichtbar wurden.",
        "",
        "## Kandidaten",
        "",
        "| Label | Klasse | Rollen | Dauerrollen | Lange Rollen | Strain-Rollen | Daueranteil | Top-Anteil | Sleep-Kombis | Top-Rollen |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in ordered:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["label"]),
                    str(row["candidate_class"]),
                    str(row["role_count"]),
                    str(row["durable_role_count"]),
                    str(row["long_role_count"]),
                    str(row["strain_role_count"]),
                    _fmt(row["durable_duration_share"]),
                    _fmt(row["top_role_duration_share"]),
                    str(row["sleep_combination_trace_count"]),
                    str(row["top_roles"]).replace("|", "/"),
                ]
            )
            + " |"
        )

    multi = [row for row in ordered if _int(row.get("durable_role_count")) >= 3]
    combo = [row for row in ordered if _int(row.get("sleep_combination_trace_count")) > 0]
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            f"Mehrrollige Real-A-Kandidaten: `{len(multi)}` von `{len(rows)}`.",
            f"Welten mit anschliessender Sleep-Kombination: `{len(combo)}` von `{len(rows)}`.",
            "",
            "Der wichtige Punkt ist die Trennung zwischen kurzer Randberuehrung und wirklich getragener Mehrrollennaehe.",
            "Eine Welt kann mehrere Rollen erzeugen, ohne dass daraus automatisch eine Offline-Kombination entsteht.",
            "Umgekehrt scheinen Sleep-Kombinationen dort naheliegender, wo Real-A bereits mehrere Rollen nicht nur als Einzelspikes, sondern als Feldnaehe traegt.",
            "",
            "## Grenze",
            "",
            "Das ist eine Kandidatenkarte, kein Beweis. Sie nutzt vorhandene Laeufe und erzeugt keine neue Handlung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte aus SOL-Mehrrollenfeld, BTC-Uebergangsfeld und PAXG/KAS-Einzelrekopplung eine Klassensynthese gebaut werden. Entscheidend ist, ob sich daraus eine stabile Abstufung der MCM-Feldnaehe ergibt.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Findet Real-A-Mehrrollen-Kandidaten in vorhandenen Real-Sleep-Real-Laeufen.")
    parser.add_argument("--debug-root", type=Path, default=DEFAULT_DEBUG_ROOT)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--csv-out", type=Path, default=DEFAULT_CSV)
    args = parser.parse_args()

    debug_root = args.debug_root if args.debug_root.is_absolute() else ROOT / args.debug_root
    rows = [
        row
        for label_dir in sorted(debug_root.iterdir())
        if label_dir.is_dir()
        for row in [_analyze_label(label_dir)]
        if row is not None
    ]
    _write_csv(rows, args.csv_out if args.csv_out.is_absolute() else ROOT / args.csv_out)
    _write_md(rows, args.out if args.out.is_absolute() else ROOT / args.out)
    print(json.dumps({"rows": len(rows), "out": str(args.out), "csv": str(args.csv_out)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
