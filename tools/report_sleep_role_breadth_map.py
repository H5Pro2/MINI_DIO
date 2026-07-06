from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "1595_SLEEP_ROLLENBREITEN_KARTE.md"
DEFAULT_CSV = ROOT / "docs" / "befunde" / "1595_SLEEP_ROLLENBREITEN_KARTE.csv"


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


def _summary_path(label: str) -> Path:
    return ROOT / "debug" / "real_sleep_real" / label / "real_sleep_real_summary.json"


def _load_summary(label: str) -> dict:
    path = _summary_path(label)
    return json.loads(path.read_text(encoding="utf-8"))


def _metric(summary: dict, name: str, side: str = "real_a") -> float:
    metrics = dict(dict(summary.get("comparison", {}) or {}).get("metrics", {}) or {})
    item = dict(metrics.get(name, {}) or {})
    return _float(item.get(side))


def _ratio(part: int, total: int) -> float:
    if total <= 0:
        return 0.0
    return part / total


def _classify_reactivation(row: dict[str, object]) -> str:
    role_ratio = _float(row.get("role_reactivation_ratio"))
    combo_ratio = _float(row.get("combo_full_reactivation_ratio"))
    partial = _int(row.get("partial_reactivated_combos"))
    roles = _int(row.get("touched_role_count"))
    combos = _int(row.get("combination_trace_count"))
    if roles <= 0:
        return "keine_sleep_rollen"
    if role_ratio >= 0.999 and combo_ratio >= 0.999 and partial == 0:
        return "voll_fokussiert"
    if role_ratio >= 0.75 and combo_ratio >= 0.50:
        return "selektiv_breit"
    if combos > 0:
        return "offen_fragmentiert"
    return "einzel_oder_schwach"


def _row(label: str, group: str) -> dict[str, object]:
    summary = _load_summary(label)
    sleep = dict(summary.get("sleep_reorganization_memory", {}) or {})
    followup = dict(summary.get("sleep_reorganization_followup", {}) or {})
    comparison = dict(summary.get("comparison", {}) or {})
    real_a_states = dict(comparison.get("real_a_episode_states", {}) or {})
    real_a_effects = dict(comparison.get("real_a_effect_classes", {}) or {})
    memory_a = dict(summary.get("memory_a_summary", {}) or {})
    field_roles = dict(memory_a.get("field_roles", {}) or {})

    touched_roles = _int(sleep.get("touched_role_count"))
    combos = _int(sleep.get("combination_trace_count"))
    reactivated_roles = _int(followup.get("reactivated_role_count"))
    full_combos = _int(followup.get("combination_fully_reactivated_count"))
    partial_combos = _int(followup.get("combination_partly_reactivated_count"))
    field_carried_roles = _int(field_roles.get("field_carried"))
    field_strained_roles = _int(field_roles.get("field_strained"))
    total_field_roles = max(1, field_carried_roles + field_strained_roles)

    row: dict[str, object] = {
        "label": label,
        "group_hint": group,
        "data_path": str(summary.get("data_path", "")),
        "touched_role_count": touched_roles,
        "combination_trace_count": combos,
        "active_role_set_count": _int(sleep.get("active_role_set_count")),
        "roles_reactivated": reactivated_roles,
        "full_reactivated_combos": full_combos,
        "partial_reactivated_combos": partial_combos,
        "role_reactivation_ratio": _ratio(reactivated_roles, touched_roles),
        "combo_full_reactivation_ratio": _ratio(full_combos, combos),
        "combo_partial_ratio": _ratio(partial_combos, combos),
        "real_a_field_roles": _int(memory_a.get("mcm_field_episode_memory")),
        "field_carried_roles": field_carried_roles,
        "field_strained_roles": field_strained_roles,
        "field_strained_role_ratio": _ratio(field_strained_roles, total_field_roles),
        "episode_state_carried": _int(real_a_states.get("field_carried")),
        "episode_state_strained": _int(real_a_states.get("field_strained")),
        "effect_stabil": _int(real_a_effects.get("stabil")),
        "effect_tragend_unruhig": _int(real_a_effects.get("tragend_unruhig")),
        "effect_kippend": _int(real_a_effects.get("kippend")),
        "effect_gespannt": _int(real_a_effects.get("gespannt")),
        "real_a_symbols": _int(_metric(summary, "unique_symbols")),
        "real_a_afterimage": _metric(summary, "avg_mini_afterimage"),
        "real_a_rekopplung": _metric(summary, "avg_mcm_rekopplung_quality"),
        "real_a_carry": _metric(summary, "avg_mcm_carry_quality"),
        "real_a_strain": _metric(summary, "avg_mcm_strain_quality"),
        "real_a_sensory": _metric(summary, "avg_mcm_sensory_coupling"),
        "real_a_neuro_balance": _metric(summary, "avg_mini_neuro_balance"),
        "real_a_neuro_load": _metric(summary, "avg_mini_neuro_load"),
    }
    row["reactivation_class"] = _classify_reactivation(row)
    return row


def _fmt(value: object, digits: int = 4) -> str:
    return f"{_float(value):.{digits}f}"


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "label",
        "group_hint",
        "reactivation_class",
        "touched_role_count",
        "combination_trace_count",
        "active_role_set_count",
        "roles_reactivated",
        "full_reactivated_combos",
        "partial_reactivated_combos",
        "role_reactivation_ratio",
        "combo_full_reactivation_ratio",
        "combo_partial_ratio",
        "real_a_field_roles",
        "field_carried_roles",
        "field_strained_roles",
        "field_strained_role_ratio",
        "episode_state_carried",
        "episode_state_strained",
        "effect_stabil",
        "effect_tragend_unruhig",
        "effect_kippend",
        "effect_gespannt",
        "real_a_symbols",
        "real_a_afterimage",
        "real_a_rekopplung",
        "real_a_carry",
        "real_a_strain",
        "real_a_sensory",
        "real_a_neuro_balance",
        "real_a_neuro_load",
        "data_path",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _write_md(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    full_breadths = sorted(
        {
            (_int(row.get("touched_role_count")), _int(row.get("combination_trace_count")))
            for row in rows
            if row["reactivation_class"] == "voll_fokussiert"
        }
    )
    selective_breadths = sorted(
        {
            (_int(row.get("touched_role_count")), _int(row.get("combination_trace_count")))
            for row in rows
            if row["reactivation_class"] == "selektiv_breit"
        }
    )
    full_line = ", ".join(f"{roles} Rollen / {combos} Kombinationen" for roles, combos in full_breadths) or "-"
    selective_line = (
        ", ".join(f"{roles} Rollen / {combos} Kombinationen" for roles, combos in selective_breadths) or "-"
    )
    lines = [
        "# Sleep-Rollenbreiten-Karte",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Grundfrage",
        "",
        "Wo kippt Offline-Feld-Reorganisation von voller fokussierter Rekopplung in selektive Reorganisation?",
        "",
        "## Unterpruefung",
        "",
        "Verglichen werden Real-Sleep-Real-Laeufe mit 2000er-Fenstern. Die Diagnose ist passiv: Sie liest Rollenanzahl, Kombinationen, Strain-Anteil und Sleep-Reaktivierung.",
        "",
        "## Rollenbreiten-Karte",
        "",
        "| Label | Klasse | Rollen | Kombinationen | Rollen reaktiviert | Kombis voll | Kombis teilweise | Strain-Rollen | Afterimage | Rekopplung | Carry | Strain |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["label"]),
                    str(row["reactivation_class"]),
                    str(row["touched_role_count"]),
                    str(row["combination_trace_count"]),
                    f"{row['roles_reactivated']} ({_fmt(row['role_reactivation_ratio'])})",
                    f"{row['full_reactivated_combos']} ({_fmt(row['combo_full_reactivation_ratio'])})",
                    f"{row['partial_reactivated_combos']} ({_fmt(row['combo_partial_ratio'])})",
                    f"{row['field_strained_roles']} ({_fmt(row['field_strained_role_ratio'])})",
                    _fmt(row["real_a_afterimage"]),
                    _fmt(row["real_a_rekopplung"]),
                    _fmt(row["real_a_carry"]),
                    _fmt(row["real_a_strain"]),
                ]
            )
            + " |"
        )

    full_rows = [row for row in rows if row["reactivation_class"] == "voll_fokussiert"]
    selective_rows = [row for row in rows if row["reactivation_class"] == "selektiv_breit"]
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"- Voll fokussierte Rekopplung: `{len(full_rows)}` Fenster.",
            f"- Selektiv breite Reorganisation: `{len(selective_rows)}` Fenster.",
            "",
            "Die aktuelle Stichprobe zeigt keine lineare Regel nach Fensterlaenge. Rollenbreite allein erklaert die Reaktivierung ebenfalls nicht vollstaendig:",
            "",
            "```text",
            f"{full_line} -> voll fokussierte Rekopplung.",
            f"{selective_line} -> selektive breite Reorganisation.",
            "```",
            "",
            "Wichtig ist: 5 Rollen / 10 Kombinationen koennen in einem realen XRP-Fenster voll rekoppeln, waehrend das synthetische Rand-/Kippfenster bei derselben Rollenbreite selektiv bleibt.",
            "",
            "Der sichtbare Unterschied liegt daher nicht in Rollenbreite allein, sondern im Feldmilieu: Nachhall, synthetische Randnaehe, Co-Touch-Qualitaet und Strain-Verteilung muessen gemeinsam gelesen werden.",
            "",
            "## Grenze",
            "",
            "Das ist eine kleine Diagnosekarte, kein Beweis. Sie definiert aber eine pruefbare Achse: Weitere Fenster koennen auf Rollenbreite, Strain-Anteil und Reaktivierungsklasse eingetragen werden.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollten die realen 5-Rollen-Fenster `DOGE_2024_5M start0` und `DOGE_2024_5M start8000` reproduziert werden. Ziel ist zu pruefen, ob reale 5-Rollen-Fenster generell voll rekoppeln und ob Selektivitaet vor allem am synthetischen Rand-/Kippmilieu haengt.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Erstellt eine passive Sleep-Rollenbreiten-Karte.")
    parser.add_argument("--label", action="append", nargs=2, metavar=("GRUPPE", "LABEL"))
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--csv-out", type=Path, default=DEFAULT_CSV)
    args = parser.parse_args()

    labels = args.label or [
        ("synthetisch_breit", "synth_rand_kipp_2000_start0_multirole_repro"),
        ("real_fokussiert", "ruhig_sideways_2000_start6000_transition_repro"),
        ("real_fokussiert", "expansion_positiv_2000_start2000_transition_repro"),
    ]
    rows = [_row(label, group) for group, label in labels]
    out_path = args.out if args.out.is_absolute() else ROOT / args.out
    csv_path = args.csv_out if args.csv_out.is_absolute() else ROOT / args.csv_out
    _write_csv(rows, csv_path)
    _write_md(rows, out_path)


if __name__ == "__main__":
    main()
