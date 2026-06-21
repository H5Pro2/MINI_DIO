from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


BASE_DEFAULT = Path("docs/befunde/409_PASSIVE_SINNESAUFNAHME_MEMORY.csv")
PROBE_DEFAULT = Path("docs/befunde/412_BTC2024_5M_QUIET_PASSIVE_SINNESAUFNAHME_MEMORY.csv")
CSV_DEFAULT = Path("docs/befunde/413_BTC2024_5M_QUIET_INTAKE_MEMORY_ABGLEICH.csv")
MD_DEFAULT = Path("docs/befunde/413_BTC2024_5M_QUIET_INTAKE_MEMORY_ABGLEICH.md")


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    if result != result:
        return 0.0
    return result


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=";"))


def _report_title(path: Path) -> str:
    stem = path.stem
    if "_" in stem:
        number, rest = stem.split("_", 1)
        if number.isdigit():
            return f"# {number} - {rest.replace('_', ' ').title()}"
    return f"# {stem.replace('_', ' ').title()}"


def _by_key(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {str(row.get("intake_key") or ""): row for row in rows if row.get("intake_key")}


def _state(base: dict[str, str], probe: dict[str, str]) -> str:
    base_quality = str(base.get("intake_memory_quality") or "-")
    probe_quality = str(probe.get("intake_memory_quality") or "-")
    base_balance = _float(base.get("avg_recoupling_balance"))
    probe_balance = _float(probe.get("avg_recoupling_balance"))
    base_pressure = _float(base.get("avg_field_intake_pressure"))
    probe_pressure = _float(probe.get("avg_field_intake_pressure"))
    if base_quality == probe_quality:
        return "quality_reproduced"
    if probe_quality == "contact_loaded_intake" and base_quality != "contact_loaded_intake":
        return "became_contact_loaded"
    if probe_quality in {"reproduced_quiet_intake", "recurrently_carried_intake"} and base_quality in {
        "open_recurrent_intake",
        "contact_loaded_intake",
        "strained_intake",
    }:
        return "became_quieter"
    if probe_balance < base_balance - 0.08 or probe_pressure > base_pressure + 0.08:
        return "drifted_heavier"
    if probe_balance > base_balance + 0.08 or probe_pressure < base_pressure - 0.08:
        return "drifted_lighter"
    return "quality_shift_open"


def build_rows(base_path: Path, probe_path: Path) -> list[dict[str, object]]:
    base = _by_key(_read_rows(base_path))
    probe = _by_key(_read_rows(probe_path))
    rows: list[dict[str, object]] = []
    for key in sorted(set(base) & set(probe)):
        left = base[key]
        right = probe[key]
        rows.append(
            {
                "intake_key": key,
                "axis": right.get("axis") or left.get("axis") or "-",
                "inner_effect_state": right.get("inner_effect_state") or left.get("inner_effect_state") or "-",
                "mcm_preview_symbol": right.get("mcm_preview_symbol") or left.get("mcm_preview_symbol") or "-",
                "base_quality": left.get("intake_memory_quality") or "-",
                "probe_quality": right.get("intake_memory_quality") or "-",
                "comparison_state": _state(left, right),
                "base_events": int(_float(left.get("total_events"))),
                "probe_events": int(_float(right.get("total_events"))),
                "base_balance": _float(left.get("avg_recoupling_balance")),
                "probe_balance": _float(right.get("avg_recoupling_balance")),
                "balance_delta": _float(right.get("avg_recoupling_balance")) - _float(left.get("avg_recoupling_balance")),
                "base_strain": _float(left.get("avg_strain_quality")),
                "probe_strain": _float(right.get("avg_strain_quality")),
                "base_fieldinput": _float(left.get("avg_field_intake_pressure")),
                "probe_fieldinput": _float(right.get("avg_field_intake_pressure")),
                "fieldinput_delta": _float(right.get("avg_field_intake_pressure")) - _float(left.get("avg_field_intake_pressure")),
            }
        )
    rows.sort(
        key=lambda row: (
            row["comparison_state"] != "quality_reproduced",
            -int(row["probe_events"]),
            str(row["intake_key"]),
        )
    )
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), delimiter=";")
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path: Path, rows: list[dict[str, object]], base_path: Path, probe_path: Path, base_count: int, probe_count: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    states = Counter(str(row["comparison_state"]) for row in rows)
    reproduced = states.get("quality_reproduced", 0)
    lines = [
        _report_title(path),
        "",
        "## Fragestellung",
        "",
        "Erkennt die passive Sinnesaufnahme-Memory in einer neuen Welt bereits bekannte Aufnahmefamilien wieder?",
        "",
        "Verglichen wird:",
        "",
        f"- Basis: `{base_path.name}`",
        f"- Gegenwelt: `{probe_path.name}`",
        "",
        "## Kurzbefund",
        "",
        f"- Basis-Eintraege: {base_count}.",
        f"- Gegenwelt-Eintraege: {probe_count}.",
        f"- Gemeinsame Intake-Keys: {len(rows)}.",
        f"- Gleiche Memory-Qualitaet: {reproduced}.",
        "",
        "## Vergleichszustaende",
        "",
        "| Zustand | Count |",
        "|---|---:|",
    ]
    for state, count in states.most_common():
        lines.append(f"| {state} | {count} |")
    lines.extend(
        [
            "",
            "## Staerkste gemeinsame Spuren",
            "",
            "| Intake-Key | Basis | Gegenwelt | Zustand | Probe Count | Balance Delta | Feldinput Delta |",
            "|---|---|---|---|---:|---:|---:|",
        ]
    )
    for row in rows[:20]:
        lines.append(
            f"| {row['intake_key']} | {row['base_quality']} | {row['probe_quality']} | "
            f"{row['comparison_state']} | {int(row['probe_events'])} | "
            f"{float(row['balance_delta']):.4f} | {float(row['fieldinput_delta']):.4f} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Die Gegenwelt erzeugt nicht nur neue Einzelspuren, sondern trifft einen Teil der bestehenden Intake-Familien wieder. Entscheidend ist, ob die Qualitaet gleich bleibt oder nur der gleiche Key unter anderer Last erscheint.",
            "",
            "`quality_reproduced` bedeutet: dieselbe Aufnahmeachse, dieselbe Innenfeldlage und dieselbe MCM-Preview tragen auch in der neuen Welt dieselbe passive Memory-Qualitaet.",
            "",
            "Das bleibt vor Handlung. Der Befund sagt nicht, was MINI_DIO tun soll, sondern welche Aufnahmeform im Innenfeld wiedererkennbar bleibt.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte eine deutlich andere Gegenwelt laufen. Wenn dieselben ruhigen Spuren dort erhalten bleiben, spricht das fuer stabile Aufnahmefamilien. Wenn sie kippen, wird die Drift der Aufnahmequalitaet sichtbar.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=Path, default=BASE_DEFAULT)
    parser.add_argument("--probe", type=Path, default=PROBE_DEFAULT)
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    args = parser.parse_args()

    base_rows = _read_rows(args.base)
    probe_rows = _read_rows(args.probe)
    rows = build_rows(args.base, args.probe)
    write_csv(args.csv_out, rows)
    write_markdown(args.md_out, rows, args.base, args.probe, len(base_rows), len(probe_rows))
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    print(f"shared={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
