from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


PASSIVE_FLAGS = {
    "passive_only": 1,
    "read_by_mini_dio": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
}


FAMILY_TYPES = {
    "abverkauf_mit_bruch",
    "abverkauf_mit_rekopplung",
    "rekopplung_nach_abverkauf",
}


def _read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _avg(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _mode(row: dict[str, str]) -> str:
    typology = row.get("typology", "")
    if typology in FAMILY_TYPES:
        return typology
    chart_zone = row.get("chart_zone", "")
    movement = row.get("dominant_movement", "")
    if chart_zone == "abverkauf_getragen" and movement == "rekopplungs_uebergang":
        return "abverkauf_mit_rekopplung"
    if chart_zone == "abverkauf_getragen":
        return "abverkauf_mit_bruch"
    if chart_zone == "rekopplung_nach_abverkauf":
        return "rekopplung_nach_abverkauf"
    return ""


def _phase_hint(row: dict[str, str]) -> str:
    before = _safe_float(row.get("before_return_pct"))
    main = _safe_float(row.get("main_return_pct"))
    after = _safe_float(row.get("after_return_pct"))
    rng = _safe_float(row.get("main_range_pct"))
    movement = row.get("dominant_movement", "")
    if main < -2.0 and movement == "bewegungsbruch_zone":
        return "fallender_bruch"
    if main < -2.0 and movement == "rekopplungs_uebergang":
        return "fallende_rekopplung"
    if before < -2.0 and main > 1.0:
        return "erholung_nach_abverkauf"
    if rng > 20.0 and abs(main) < rng * 0.35:
        return "weite_unaufgeloeste_spannung"
    if movement == "rekopplungs_uebergang":
        return "rekopplungsfenster"
    if movement == "druck_uebergang":
        return "druckfenster"
    return "offenes_familienfenster"


def build_rows(sources: list[list[str]]) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    detail: list[dict[str, object]] = []
    for source_name, path_text in sources:
        for row in _read(Path(path_text)):
            mode = _mode(row)
            if not mode:
                continue
            item: dict[str, object] = {
                "source": source_name,
                "world": row.get("world", "-"),
                "pair": row.get("pair", "-"),
                "ticks": f"{row.get('tick_min', '-')}-{row.get('tick_max', '-')}",
                "mode": mode,
                "phase_hint": _phase_hint(row),
                "chart_zone": row.get("chart_zone", "-"),
                "dominant_movement": row.get("dominant_movement", "-"),
                "main_return_pct": row.get("main_return_pct", "0"),
                "main_range_pct": row.get("main_range_pct", "0"),
                "before_return_pct": row.get("before_return_pct", "0"),
                "after_return_pct": row.get("after_return_pct", "0"),
                "pressure_delta_abs_avg": row.get("pressure_delta_abs_avg", "0"),
                "rekopplung_delta_abs_avg": row.get("rekopplung_delta_abs_avg", "0"),
                **PASSIVE_FLAGS,
            }
            detail.append(item)

    by_mode: dict[str, list[dict[str, object]]] = defaultdict(list)
    by_phase: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in detail:
        by_mode[str(row["mode"])].append(row)
        by_phase[str(row["phase_hint"])].append(row)

    mode_rows: list[dict[str, object]] = []
    for mode, rows in by_mode.items():
        worlds = Counter(str(row["world"]) for row in rows)
        movements = Counter(str(row["dominant_movement"]) for row in rows)
        phases = Counter(str(row["phase_hint"]) for row in rows)
        mode_rows.append(
            {
                "mode": mode,
                "count": len(rows),
                "worlds": " | ".join(f"{key}:{value}" for key, value in worlds.most_common(8)),
                "movements": " | ".join(f"{key}:{value}" for key, value in movements.most_common()),
                "phase_hints": " | ".join(f"{key}:{value}" for key, value in phases.most_common()),
                "avg_return_pct": round(_avg([_safe_float(row["main_return_pct"]) for row in rows]), 6),
                "avg_range_pct": round(_avg([_safe_float(row["main_range_pct"]) for row in rows]), 6),
                "avg_before_pct": round(_avg([_safe_float(row["before_return_pct"]) for row in rows]), 6),
                "avg_after_pct": round(_avg([_safe_float(row["after_return_pct"]) for row in rows]), 6),
                "avg_pressure_abs": round(_avg([_safe_float(row["pressure_delta_abs_avg"]) for row in rows]), 6),
                "avg_rekopplung_abs": round(_avg([_safe_float(row["rekopplung_delta_abs_avg"]) for row in rows]), 6),
                **PASSIVE_FLAGS,
            }
        )

    phase_rows: list[dict[str, object]] = []
    for phase, rows in by_phase.items():
        modes = Counter(str(row["mode"]) for row in rows)
        phase_rows.append(
            {
                "phase_hint": phase,
                "count": len(rows),
                "modes": " | ".join(f"{key}:{value}" for key, value in modes.most_common()),
                "avg_return_pct": round(_avg([_safe_float(row["main_return_pct"]) for row in rows]), 6),
                "avg_range_pct": round(_avg([_safe_float(row["main_range_pct"]) for row in rows]), 6),
                "avg_before_pct": round(_avg([_safe_float(row["before_return_pct"]) for row in rows]), 6),
                "avg_after_pct": round(_avg([_safe_float(row["after_return_pct"]) for row in rows]), 6),
                "avg_pressure_abs": round(_avg([_safe_float(row["pressure_delta_abs_avg"]) for row in rows]), 6),
                "avg_rekopplung_abs": round(_avg([_safe_float(row["rekopplung_delta_abs_avg"]) for row in rows]), 6),
                **PASSIVE_FLAGS,
            }
        )

    mode_rows.sort(key=lambda row: (-int(row["count"]), str(row["mode"])))
    phase_rows.sort(key=lambda row: (-int(row["count"]), str(row["phase_hint"])))
    detail.sort(key=lambda row: (str(row["mode"]), str(row["world"]), str(row["pair"])))
    return detail, mode_rows, phase_rows


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames: list[str] = []
    for row in rows:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _clean(value: object) -> str:
    return str(value).replace("|", "<br>")


def _write_md(path: Path, detail: list[dict[str, object]], mode_rows: list[dict[str, object]], phase_rows: list[dict[str, object]]) -> None:
    lines = [
        f"# {path.stem.split('_', 1)[0]} - Abverkauf/Rekopplung-Familie",
        "",
        "Passive Familienlesung fuer Abverkauf, Bruch, Rekopplung und Nach-Abverkauf-Erholung.",
        "",
        "## Kurzbefund",
        "",
        f"- Familienfenster gesamt: {len(detail)}",
        f"- Modi: {len(mode_rows)}",
        f"- Phasenhinweise: {len(phase_rows)}",
        "",
        "## Modi",
        "",
        "| Modus | Anzahl | Welten | Bewegung | Phasenhinweise | Return % | Range % | Vorher % | Nachher % | Druck | Rekopplung |",
        "|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in mode_rows:
        lines.append(
            "| {mode} | {count} | {worlds} | {movements} | {phase_hints} | {avg_return_pct} | {avg_range_pct} | {avg_before_pct} | {avg_after_pct} | {avg_pressure_abs} | {avg_rekopplung_abs} |".format(
                **{key: _clean(value) for key, value in row.items()}
            )
        )
    lines.extend(
        [
            "",
            "## Phasenhinweise",
            "",
            "| Phase | Anzahl | Modi | Return % | Range % | Vorher % | Nachher % | Druck | Rekopplung |",
            "|---|---:|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in phase_rows:
        lines.append(
            "| {phase_hint} | {count} | {modes} | {avg_return_pct} | {avg_range_pct} | {avg_before_pct} | {avg_after_pct} | {avg_pressure_abs} | {avg_rekopplung_abs} |".format(
                **{key: _clean(value) for key, value in row.items()}
            )
        )
    lines.extend(
        [
            "",
            "## Einzelzuordnung",
            "",
            "| Modus | Phase | Quelle | Welt | Paar | Ticks | Chartzone | MCM-Bewegung | Return % | Range % |",
            "|---|---|---|---|---|---|---|---|---:|---:|",
        ]
    )
    for row in detail[:120]:
        lines.append(
            "| {mode} | {phase_hint} | {source} | {world} | `{pair}` | {ticks} | `{chart_zone}` | `{dominant_movement}` | {main_return_pct} | {main_range_pct} |".format(
                **row
            )
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Die Familie zerfaellt in drei lesbare Formen: fallender Bruch, fallende Rekopplung und Erholung nach vorherigem Abverkauf.",
            "",
            "`abverkauf_mit_rekopplung` ist derzeit die stabilere Familie als `rekopplung_nach_abverkauf`. Letztere wirkt eher wie eine grossraeumige Erholungsform nach vorherigem Druck.",
            "",
            "Fachlich bedeutet das: Das MCM-Feld liest nicht nur Preisrichtung. Es unterscheidet, ob ein fallendes Fenster bricht, rekoppelt oder nach vorheriger Belastung wieder Anschluss findet.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die Familie `abverkauf + rekopplung` gegen lokale Weltmerkmale gelesen werden: Lautstaerke/Energie, Rezeptorlast, Druckwechsel und Topologie-Rolle im gleichen Tickfenster.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", action="append", nargs=2, metavar=("NAME", "DETAIL_CSV"), required=True)
    parser.add_argument("--out-detail", type=Path, required=True)
    parser.add_argument("--out-mode-summary", type=Path, required=True)
    parser.add_argument("--out-phase-summary", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    detail, mode_rows, phase_rows = build_rows(args.source)
    _write_csv(args.out_detail, detail)
    _write_csv(args.out_mode_summary, mode_rows)
    _write_csv(args.out_phase_summary, phase_rows)
    _write_md(args.out_md, detail, mode_rows, phase_rows)
    print(f"details={len(detail)}")
    print(f"modes={len(mode_rows)}")
    print(f"phases={len(phase_rows)}")
    print(f"wrote {args.out_md}")


if __name__ == "__main__":
    main()
