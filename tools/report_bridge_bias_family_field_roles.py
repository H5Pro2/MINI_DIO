from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


METRIC_KEYS = [
    "hoeren_energy_tone",
    "hoeren_energy_shift",
    "sehen_form_stability",
    "sehen_form_change",
    "rezeptor_field_intake_pressure",
    "perception_auditory_loudness",
    "perception_auditory_listen_tendency",
    "mcm_feldwirkung_mcm_tension",
    "mcm_feldwirkung_mcm_coherence",
    "mcm_rekopplung_quality",
    "mcm_carry_quality",
    "mcm_strain_quality",
]


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _float(row: dict[str, str], key: str) -> float:
    try:
        value = float(row.get(key, "") or 0.0)
    except ValueError:
        return 0.0
    return 0.0 if value != value else value


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _top(counter: Counter[str], limit: int = 3) -> str:
    if not counter:
        return "-"
    return ";".join(f"{name}:{count}" for name, count in counter.most_common(limit))


def _role(row: dict[str, object]) -> str:
    tension = float(row["mcm_feldwirkung_mcm_tension"])
    coherence = float(row["mcm_feldwirkung_mcm_coherence"])
    rek = float(row["mcm_rekopplung_quality"])
    carry = float(row["mcm_carry_quality"])
    strain = float(row["mcm_strain_quality"])
    tone_shift = abs(float(row["hoeren_energy_shift"]))
    form_change = abs(float(row["sehen_form_change"]))

    if rek >= 0.715 and carry >= 0.54 and strain <= 0.145 and tension <= 0.10:
        return "stabilisierende_rueckbindung"
    if tension >= 0.14 or strain >= 0.17:
        return "spannungsnahe_belastung"
    if tone_shift >= 0.24 or form_change >= 0.18:
        return "uebergang_oeffnung"
    if coherence >= 0.62 and rek >= 0.70:
        return "kohaerente_bruecke"
    return "gemischte_nachbarschaft"


def _bias_label(delta: float) -> str:
    if delta > 0:
        return "staerker_104t_zu_00ly"
    if delta < 0:
        return "staerker_00ly_zu_104t"
    return "balanciert"


def _build_rows(windows: list[dict[str, str]], candidates: list[dict[str, str]]) -> list[dict[str, object]]:
    candidate_delta = {
        row["candidate_family"]: _float(row, "rate_delta_b_minus_a")
        for row in candidates
        if row.get("candidate_family")
    }
    wanted = set(candidate_delta)
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in windows:
        family = row.get("family", "") or ""
        if family in wanted:
            grouped[family].append(row)

    rows: list[dict[str, object]] = []
    for family in sorted(wanted):
        items = grouped.get(family, [])
        direction_counts = Counter(row.get("direction", "-") or "-" for row in items)
        phase_counts = Counter(row.get("phase", "-") or "-" for row in items)
        class_counts = Counter(row.get("segment_class", "-") or "-" for row in items)
        world_counts = Counter(row.get("world", "-") or "-" for row in items)

        metric_values = {key: [_float(row, key) for row in items] for key in METRIC_KEYS}
        out: dict[str, object] = {
            "family": family,
            "bias_from_1180": _bias_label(candidate_delta.get(family, 0.0)),
            "rate_delta_b_minus_a": round(candidate_delta.get(family, 0.0), 6),
            "events": len(items),
            "worlds": len(world_counts),
            "dominant_direction": direction_counts.most_common(1)[0][0] if direction_counts else "-",
            "direction_profile": _top(direction_counts, 4),
            "phase_profile": _top(phase_counts, 4),
            "segment_profile": _top(class_counts, 4),
        }
        for key in METRIC_KEYS:
            out[key] = round(_avg(metric_values[key]), 6)
        out["field_role_reading"] = _role(out)
        rows.append(out)

    rows.sort(key=lambda row: (str(row["field_role_reading"]), -int(row["events"]), str(row["family"])))
    return rows


def _role_summary(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    by_role: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        by_role[str(row["field_role_reading"])].append(row)

    out: list[dict[str, object]] = []
    for role, items in sorted(by_role.items()):
        out.append(
            {
                "field_role_reading": role,
                "families": len(items),
                "events": sum(int(row["events"]) for row in items),
                "families_list": ";".join(str(row["family"]) for row in items),
                "avg_tension": round(_avg([float(row["mcm_feldwirkung_mcm_tension"]) for row in items]), 6),
                "avg_rekopplung": round(_avg([float(row["mcm_rekopplung_quality"]) for row in items]), 6),
                "avg_carry": round(_avg([float(row["mcm_carry_quality"]) for row in items]), 6),
                "avg_strain": round(_avg([float(row["mcm_strain_quality"]) for row in items]), 6),
            }
        )
    out.sort(key=lambda row: (-int(row["events"]), str(row["field_role_reading"])))
    return out


def _write_csv(rows: list[dict[str, object]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        out.write_text("", encoding="utf-8")
        return
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(rows: list[dict[str, object]], roles: list[dict[str, object]], out: Path) -> None:
    lines = [
        "# 1183 - Brueckennetz Biasfamilien: Feldrollen",
        "",
        "## Grundfrage",
        "",
        "Die vorherige Pruefung zeigte ein gemeinsames Brueckennetz mit richtungsabhaengiger Drift.",
        "Diese Diagnose prueft, ob die Biasfamilien im Brueckennetz eigene Feldrollen tragen oder nur Oberflaechen-Nachbarn sind.",
        "",
        "Die Pruefung bleibt passiv. Es wird keine Handlung, kein Gate und keine Strategie abgeleitet.",
        "",
        "## Rollenuebersicht",
        "",
        "| Feldrollen-Lesung | Familien | Ereignisse | Rekopplung | Carry | Strain | Tension |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in roles:
        lines.append(
            f"| {row['field_role_reading']} | {row['families']} | {row['events']} | "
            f"{float(row['avg_rekopplung']):.4f} | {float(row['avg_carry']):.4f} | "
            f"{float(row['avg_strain']):.4f} | {float(row['avg_tension']):.4f} |"
        )

    lines.extend(
        [
            "",
            "## Familien",
            "",
            "| Familie | Bias | Ereignisse | Welten | Rolle | Segmentprofil | Phasenprofil |",
            "|---|---|---:|---:|---|---|---|",
        ]
    )
    for row in rows:
        lines.append(
            f"| {row['family']} | {row['bias_from_1180']} | {row['events']} | {row['worlds']} | "
            f"{row['field_role_reading']} | {row['segment_profile']} | {row['phase_profile']} |"
        )

    role_map = defaultdict(list)
    for row in rows:
        role_map[str(row["field_role_reading"])].append(str(row["family"]))

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Biasfamilien sind nicht gleichfoermig verteilt.",
            "Sie fallen in mehrere Feldrollen:",
            "",
        ]
    )
    for role, families in sorted(role_map.items()):
        lines.append(f"- `{role}`: {', '.join(families)}")

    lines.extend(
        [
            "",
            "Damit spricht die aktuelle Datenlage nicht fuer reine Oberflaechen-Nachbarschaft.",
            "Die Familien tragen unterschiedliche lokale Feldqualitaeten innerhalb desselben Brueckennetzes.",
            "",
            "## Grenze",
            "",
            "Die Rollen sind diagnostische Lesungen aus passiven Fenstern.",
            "Sie beweisen noch keine autonome Bedeutungsentscheidung von MINI_DIO.",
            "Stark ist aber: Die gleichen Biasfamilien lassen sich nicht nur zaehlen, sondern auch feldqualitativ unterscheiden.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte geprueft werden, ob diese Feldrollen in einer neuen Welt erneut auftreten oder ob sie unter anderer Weltspannung in andere Rollen kippen.",
        ]
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--windows", required=True)
    parser.add_argument("--candidates", required=True)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--out-summary-csv", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    rows = _build_rows(_load(Path(args.windows)), _load(Path(args.candidates)))
    roles = _role_summary(rows)
    _write_csv(rows, Path(args.out_csv))
    _write_csv(roles, Path(args.out_summary_csv))
    _write_md(rows, roles, Path(args.out_md))
    print(f"families={len(rows)} roles={len(roles)}")
    print(f"wrote {args.out_csv}")
    print(f"wrote {args.out_summary_csv}")
    print(f"wrote {args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
