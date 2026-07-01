from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


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


def _zone(row: dict[str, str]) -> str:
    observed = row.get("observed_role_profile", "") or ""
    baseline = row.get("baseline_role", "") or ""
    state = row.get("role_state", "") or ""
    tension = _float(row, "mcm_feldwirkung_mcm_tension")
    strain = _float(row, "mcm_strain_quality")
    rekopplung = _float(row, "mcm_rekopplung_quality")

    if baseline == "stabilisierende_rueckbindung" and state == "stabil" and rekopplung >= 0.715:
        return "zone_stabile_rueckbindung"
    if baseline == "spannungsnahe_belastung" and tension >= 0.14:
        return "zone_belastete_randnaehe"
    if "uebergang_oeffnung" in observed or baseline == "uebergang_oeffnung":
        return "zone_uebergangsoeffnung"
    if baseline == "kohaerente_bruecke" and strain < 0.15:
        return "zone_kohaerente_bruecke"
    return "zone_gemischte_nachbarschaft"


def _build(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[_zone(row)].append(row)

    out: list[dict[str, object]] = []
    for zone, items in sorted(grouped.items()):
        families = Counter(row.get("family", "-") or "-" for row in items)
        state_counts = Counter(row.get("role_state", "-") or "-" for row in items)
        role_counts = Counter(row.get("baseline_role", "-") or "-" for row in items)
        out.append(
            {
                "field_zone": zone,
                "rows": len(items),
                "events": sum(int(float(row.get("events", "0") or 0)) for row in items),
                "families": ";".join(f"{name}:{count}" for name, count in families.most_common()),
                "role_states": ";".join(f"{name}:{count}" for name, count in state_counts.most_common()),
                "baseline_roles": ";".join(f"{name}:{count}" for name, count in role_counts.most_common()),
                "avg_rekopplung": round(_avg([_float(row, "mcm_rekopplung_quality") for row in items]), 6),
                "avg_carry": round(_avg([_float(row, "mcm_carry_quality") for row in items]), 6),
                "avg_strain": round(_avg([_float(row, "mcm_strain_quality") for row in items]), 6),
                "avg_tension": round(_avg([_float(row, "mcm_feldwirkung_mcm_tension") for row in items]), 6),
                "avg_coherence": round(_avg([_float(row, "mcm_feldwirkung_mcm_coherence") for row in items]), 6),
                "avg_tone": round(_avg([_float(row, "hoeren_energy_tone") for row in items]), 6),
                "avg_tone_shift": round(_avg([_float(row, "hoeren_energy_shift") for row in items]), 6),
                "avg_form_stability": round(_avg([_float(row, "sehen_form_stability") for row in items]), 6),
                "avg_form_change": round(_avg([_float(row, "sehen_form_change") for row in items]), 6),
                "avg_raw_return": round(_avg([_float(row, "raw_return") for row in items]), 8),
                "avg_raw_range": round(_avg([_float(row, "raw_range_ratio") for row in items]), 8),
                "avg_raw_body": round(_avg([_float(row, "raw_body_ratio") for row in items]), 8),
                "avg_raw_volume_to_world": round(_avg([_float(row, "raw_volume_to_world") for row in items]), 8),
                "avg_raw_direction_consistency": round(
                    _avg([_float(row, "raw_direction_consistency") for row in items]), 8
                ),
            }
        )
    out.sort(key=lambda row: (-int(row["events"]), str(row["field_zone"])))
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


def _write_md(rows: list[dict[str, object]], out: Path) -> None:
    lines = [
        "# 1189 - Passive MCM-Rollenkarte",
        "",
        "## Grundfrage",
        "",
        "Welche passiven Feldzonen ergeben sich aus den stabilen und kippenden Brueckenrollen?",
        "",
        "Die Rollenkarte ist eine Verdichtung der Befunde 1184 bis 1187.",
        "Sie ist keine Steuerlogik und kein Gate.",
        "",
        "## Feldzonen",
        "",
        "| Feldzone | Ereignisse | Familien | Rekopplung | Carry | Strain | Tension | Ton | Formstabilitaet | Roh-Range |",
        "|---|---:|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['field_zone']} | {row['events']} | {row['families']} | "
            f"{float(row['avg_rekopplung']):.4f} | {float(row['avg_carry']):.4f} | "
            f"{float(row['avg_strain']):.4f} | {float(row['avg_tension']):.4f} | "
            f"{float(row['avg_tone']):+.4f} | {float(row['avg_form_stability']):+.4f} | "
            f"{float(row['avg_raw_range']):.5f} |"
        )

    zone_names = [str(row["field_zone"]) for row in rows]
    lines.extend(
        [
            "",
            "## Lesart",
            "",
            f"Es entstehen `{len(rows)}` passive Feldzonen: `{', '.join(zone_names)}`.",
            "",
            "Die Karte zeigt eine Feldorganisation:",
            "",
            "- Rueckbindung ist eine eigene Zone mit hoher Rekopplung und niedriger Spannung.",
            "- Belastete Randnaehe ist eine eigene Zone mit hoher Spannung und hohem Strain.",
            "- Uebergangsoeffnung ist keine reine Stoerung, sondern eine wiederkehrende Rollenverschiebung.",
            "- Kohaerente Bruecke liegt zwischen Rueckbindung und Uebergang.",
            "",
            "Damit wird MINI_DIOs MCM-Feld als dynamische Zonenkonfiguration lesbar.",
            "Die Bedeutung entsteht nicht isoliert im Symbol, sondern durch Lage im Feld, Weltfenster, Sinnesaufnahme und Nachbarschaft.",
            "",
            "## Grenze",
            "",
            "Diese Karte ist eine Forschungslesung.",
            "Sie sagt nicht, dass MINI_DIO bewusst eine Zone auswaehlt.",
            "Sie zeigt aber, dass sich aus passiver Feldwirkung eine stabile, beschreibbare Zonenstruktur ableiten laesst.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte geprueft werden, ob diese Feldzonen ueber weitere Assets und Zeitraeume gleich bleiben oder ob neue Zonen entstehen.",
        ]
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", required=True)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    rows = _build(_load(Path(args.summary)))
    _write_csv(rows, Path(args.out_csv))
    _write_md(rows, Path(args.out_md))
    print(f"zones={len(rows)}")
    print(f"wrote {args.out_csv}")
    print(f"wrote {args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
