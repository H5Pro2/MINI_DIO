from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


def _load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists() or path.stat().st_size <= 0:
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _raw_motion_class(row: dict[str, str]) -> str:
    direction = str(row.get("raw_direction") or "offen")
    range_pct = _safe_float(row.get("raw_range_pct"))
    changes = _safe_float(row.get("raw_direction_changes"))
    body = _safe_float(row.get("raw_avg_body_pct"))
    if range_pct >= 4.0 and changes >= 20:
        return f"weite_unruhige_vorphase_{direction}"
    if range_pct >= 4.0:
        return f"weite_gerichtete_vorphase_{direction}"
    if changes >= 20:
        return f"enge_unruhige_vorphase_{direction}"
    if body <= 0.035:
        return f"feine_ruhevorphase_{direction}"
    return f"mittlere_vorphase_{direction}"


def _sensory_class(row: dict[str, str]) -> str:
    visual_stability = _safe_float(row.get("sehen_form_stability"))
    visual_change = _safe_float(row.get("sehen_form_change"))
    tone = _safe_float(row.get("hoeren_energy_tone"))
    shift = abs(_safe_float(row.get("hoeren_energy_shift")))
    loudness = _safe_float(row.get("perception_auditory_loudness"))

    if tone >= 0.45 and shift >= 0.45:
        hearing = "hoch_schwingend"
    elif tone >= 0.45:
        hearing = "hell_getragen"
    elif shift >= 0.35:
        hearing = "wechselnd"
    else:
        hearing = "gedaempft"

    if visual_stability >= max(0.25, abs(visual_change)):
        visual = "sicht_stabil"
    elif visual_change <= -0.25:
        visual = "sicht_zerfaellt"
    elif abs(visual_change) >= 0.25:
        visual = "sicht_wechselt"
    else:
        visual = "sicht_offen"

    if loudness >= 0.55:
        level = "laut"
    elif loudness <= 0.25:
        level = "leise"
    else:
        level = "mittel"
    return f"{visual}_{hearing}_{level}"


def _field_contact_class(row: dict[str, str]) -> str:
    carry = _safe_float(row.get("mcm_carry_quality"))
    strain = _safe_float(row.get("mcm_strain_quality"))
    rekopplung = _safe_float(row.get("mcm_rekopplung_quality"))

    if rekopplung >= 0.62 and carry >= 0.40 and strain <= 0.24:
        return "tragende_rekopplung"
    if rekopplung >= 0.58 and strain <= 0.28:
        return "offene_rekopplung"
    if strain >= 0.28 and rekopplung <= 0.59:
        return "spannungsnahe_oeffnung"
    if carry >= 0.40:
        return "getragen_offen"
    return "offener_feldkontakt"


def _combined_class(row: dict[str, str]) -> str:
    return f"{_raw_motion_class(row)} | {_sensory_class(row)} | {_field_contact_class(row)}"


def _load_labeled(inputs: list[str]) -> dict[str, list[dict[str, str]]]:
    data: dict[str, list[dict[str, str]]] = {}
    for raw in inputs:
        if "=" not in raw:
            raise SystemExit(f"Ungültiges Input-Format: {raw}")
        label, path = raw.split("=", 1)
        data[label.strip()] = _load_csv(Path(path))
    return data


def _build_rows(data: dict[str, list[dict[str, str]]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    event_rows: list[dict[str, object]] = []
    for lookback, rows in data.items():
        for row in rows:
            out = dict(row)
            out["lookback"] = lookback
            out["raw_motion_class"] = _raw_motion_class(row)
            out["sensory_class"] = _sensory_class(row)
            out["field_contact_class"] = _field_contact_class(row)
            out["combined_prephase_class"] = _combined_class(row)
            event_rows.append(out)

    groups: dict[tuple[str, str, str], list[dict[str, object]]] = defaultdict(list)
    for row in event_rows:
        groups[(str(row["lookback"]), str(row["target_group"]), str(row["chain"]))].append(row)

    summary_rows: list[dict[str, object]] = []
    for (lookback, target_group, chain), items in sorted(groups.items()):
        motion = Counter(str(row["raw_motion_class"]) for row in items)
        sensory = Counter(str(row["sensory_class"]) for row in items)
        field = Counter(str(row["field_contact_class"]) for row in items)
        combined = Counter(str(row["combined_prephase_class"]) for row in items)
        symbols = Counter(str(row["preview_symbol"]) for row in items)
        summary_rows.append(
            {
                "lookback": lookback,
                "target_group": target_group,
                "chain": chain,
                "events": len(items),
                "dominant_motion_class": motion.most_common(1)[0][0],
                "dominant_motion_share": motion.most_common(1)[0][1] / max(1, len(items)),
                "dominant_sensory_class": sensory.most_common(1)[0][0],
                "dominant_sensory_share": sensory.most_common(1)[0][1] / max(1, len(items)),
                "dominant_field_contact_class": field.most_common(1)[0][0],
                "dominant_field_contact_share": field.most_common(1)[0][1] / max(1, len(items)),
                "dominant_combined_class": combined.most_common(1)[0][0],
                "dominant_combined_share": combined.most_common(1)[0][1] / max(1, len(items)),
                "symbols": ";".join(f"{key}:{value}" for key, value in symbols.most_common()),
                "motion_classes": ";".join(f"{key}:{value}" for key, value in motion.most_common(8)),
                "sensory_classes": ";".join(f"{key}:{value}" for key, value in sensory.most_common(8)),
                "field_contact_classes": ";".join(f"{key}:{value}" for key, value in field.most_common(8)),
                "avg_range": _avg([_safe_float(row.get("raw_range_pct")) for row in items]),
                "avg_changes": _avg([_safe_float(row.get("raw_direction_changes")) for row in items]),
                "avg_carry": _avg([_safe_float(row.get("mcm_carry_quality")) for row in items]),
                "avg_strain": _avg([_safe_float(row.get("mcm_strain_quality")) for row in items]),
                "avg_rekopplung": _avg([_safe_float(row.get("mcm_rekopplung_quality")) for row in items]),
            }
        )
    return event_rows, summary_rows


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = list(rows[0].keys()) if rows else ["lookback"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(path: Path, summary_rows: list[dict[str, object]], labels: list[str]) -> None:
    lines = [
        "# 2038 - Feldfunktionswechsel Vorphasen-Klassen",
        "",
        "## Zweck",
        "",
        "Diese Diagnose verdichtet die Rohweltfenster vor Feldfunktionswechseln zu passiven Vorphasen-Klassen.",
        "",
        "Geprüft wird, ob vor Öffnung und Rekopplung wiederkehrende Welt-, Sinnes- und Feldkontaktprofile sichtbar sind.",
        "",
        "## Eingaben",
        "",
    ]
    for label in labels:
        lines.append(f"- `{label}`")

    lines.extend(
        [
            "",
            "## Zusammenfassung",
            "",
            "| Lookback | Gruppe | Kette | Ereignisse | dominante Rohphase | dominante Sinnesphase | dominanter Feldkontakt | MCM carry/strain/rekopplung |",
            "|---|---|---|---:|---|---|---|---:|",
        ]
    )
    for row in summary_rows:
        lines.append(
            "| "
            f"`{row['lookback']}` | "
            f"`{row['target_group']}` | "
            f"`{row['chain']}` | "
            f"{row['events']} | "
            f"`{row['dominant_motion_class']}` ({float(row['dominant_motion_share']):.2f}) | "
            f"`{row['dominant_sensory_class']}` ({float(row['dominant_sensory_share']):.2f}) | "
            f"`{row['dominant_field_contact_class']}` ({float(row['dominant_field_contact_share']):.2f}) | "
            f"{float(row['avg_carry']):.3f}/{float(row['avg_strain']):.3f}/{float(row['avg_rekopplung']):.3f} |"
        )

    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Die Vorphasen-Klassen trennen drei Ebenen:",
            "",
            "- Rohweltbewegung: wie breit, unruhig oder gerichtet das vorherige Fenster ist",
            "- Sinnesprofil: ob Sehen/Hören stabil, wechselnd, hoch schwingend oder gedämpft wirken",
            "- Feldkontakt: ob der Kontakt tragend rekoppelt oder spannungsnah öffnet",
            "",
            "Damit wird der Rollenwechsel nicht als isolierter Moment gelesen, sondern als Kontaktpunkt nach einer passiven Vorphase.",
            "",
            "## Bedeutung für DIO",
            "",
            "DIO kann daraus später eine organische Vorwahrnehmung entwickeln: nicht handeln, sondern merken, welche Vorphase typischerweise zu Öffnung oder Rekopplung führt.",
            "",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", action="append", required=True, help="Format: label=path")
    parser.add_argument("--out-prefix", default="2038_FELDFUNKTIONSWECHSEL_VORPHASEN_KLASSEN")
    args = parser.parse_args()

    labels = [raw.split("=", 1)[0].strip() for raw in args.input]
    event_rows, summary_rows = _build_rows(_load_labeled(args.input))
    out_dir = Path("docs") / "befunde"
    _write_csv(out_dir / f"{args.out_prefix}.events.csv", event_rows)
    _write_csv(out_dir / f"{args.out_prefix}.summary.csv", summary_rows)
    _write_markdown(out_dir / f"{args.out_prefix}.md", summary_rows, labels)

    print(f"events={len(event_rows)}")
    print(f"summary_rows={len(summary_rows)}")
    print(f"wrote={out_dir / (args.out_prefix + '.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
