from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FINDINGS = ROOT / "docs" / "befunde"

INPUT_PATH = FINDINGS / "946_MCM_ROLLENREIFUNGS_MEMORY_LESUNG_SECHSTE_WELT.csv"
OUT_CSV = FINDINGS / "948_MCM_LANGZEIT_REIFUNGSKLASSIFIKATION.csv"
OUT_MD = FINDINGS / "948_MCM_LANGZEIT_REIFUNGSKLASSIFIKATION.md"


def classify(row: dict[str, str]) -> tuple[str, str]:
    read_state = row.get("read_state", "")
    memory_quality = row.get("memory_maturation_quality", "")
    segment_quality = row.get("memory_segment_quality", "")
    current_class = row.get("current_class", "")
    current_weight = int(float(row.get("current_weight") or 0))
    current_world_span = int(float(row.get("current_world_span") or 0))

    if read_state == "bruecke_gehalten":
        return (
            "langfristig_getragen",
            "Reorganisationsbruecke bleibt auch in weiterer Welt sichtbar.",
        )
    if read_state == "rolle_gehalten_bestaetigt":
        return (
            "langfristig_belastet_getragen",
            "Rolle bleibt sichtbar, traegt aber belastete Kernnaehe.",
        )
    if read_state == "reifung_abgeschwaecht":
        return (
            "weltabhaengig_getragen",
            "Reifung bleibt sichtbar, verliert aber Zentralitaet.",
        )
    if read_state == "verschwindung_bestaetigt":
        return (
            "verschwunden_bestaetigt",
            "Verschwinden wird erneut gelesen und ist selbst Information.",
        )
    if read_state == "nicht_wiedergefunden":
        if memory_quality == "maturation_reifung":
            return (
                "abgeschwaecht_oder_verloren",
                "Vorherige junge Reifung wird in Folgewelt nicht getragen.",
            )
        return (
            "kurzfristige_oberflaeche",
            "Junge oder offene Spur bleibt nicht sichtbar.",
        )
    if current_class != "-" and current_weight > 0 and current_world_span > 0:
        if segment_quality in {"mehrwelt_segmentbruecke", "lange_mehrweltphase"}:
            return (
                "mehrwelt_sichtbar_ungeklaert",
                "Spur bleibt ueber mehrere Welten sichtbar, braucht aber weitere Lesung.",
            )
    return ("offen", "Keine belastbare Langzeitklassifikation.")


def read_rows() -> list[dict[str, str]]:
    with INPUT_PATH.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(rows: list[dict[str, str]]) -> None:
    fields = [
        "maturation_symbol",
        "short_token",
        "longterm_class",
        "read_state",
        "memory_maturation_quality",
        "memory_segment_quality",
        "memory_field_quality",
        "memory_follow_class",
        "current_class",
        "current_weight",
        "current_world_span",
        "classification_note",
    ]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def write_md(rows: list[dict[str, str]]) -> None:
    counts = Counter(row["longterm_class"] for row in rows)
    lines = [
        "# MCM-Langzeit-Reifungsklassifikation",
        "",
        "## Zweck",
        "",
        "Diese Auswertung verdichtet die passive `dio_mature_*`-Lesung aus 946 zu einer Langzeitklasse.",
        "Sie bleibt diagnostisch: keine Handlung, kein Gate, keine Richtungsvorgabe.",
        "",
        "## Klassen",
        "",
    ]
    for key, count in sorted(counts.items()):
        lines.append(f"- `{key}`: {count}")
    lines.extend(
        [
            "",
            "## Token-Lesung",
            "",
            "| Token | Symbol | Langzeitklasse | Lesung | aktuelle Rolle | Note |",
            "|---|---|---|---|---|---|",
        ]
    )
    for row in rows:
        lines.append(
            "| `{short_token}` | `{maturation_symbol}` | `{longterm_class}` | `{read_state}` | `{current_class}` | {classification_note} |".format(
                **row
            )
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Die MCM-Reifung verhaelt sich nicht linear.",
            "Ein Teil der Spuren bleibt ueber Folgewelten tragend, ein Teil wird weltabhaengig abgeschwaecht, und ein Teil verschwindet wieder.",
            "Wichtig ist dabei: Auch Verschwinden ist kein Fehler, sondern Feldinformation.",
            "",
            "Damit entsteht eine passive Reifungsordnung:",
            "",
            "- stabile Reorganisationsbruecken",
            "- belastet gehaltene Kernnaehe",
            "- weltabhaengige Reifung",
            "- bestaetigtes Verschwinden",
            "- kurzfristige Oberflaeche",
            "",
            "## Schlussfolgerung",
            "",
            "`dio_mature_*` kann als passive Langzeit-Memory genutzt werden, um Reifung von Oberflaeche zu trennen.",
            "Die Schicht beschreibt nicht, was MINI_DIO tun soll.",
            "Sie beschreibt nur, welche inneren Feldrollen ueber mehrere Welten sichtbar bleiben.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese Klassifikation gegen eine weitere Welt gelesen werden.",
            "Entscheidend ist, ob `langfristig_getragen` stabil bleibt und ob `weltabhaengig_getragen` weiter driftet oder wieder rekoppelt.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    rows = read_rows()
    enriched: list[dict[str, str]] = []
    for row in rows:
        longterm_class, note = classify(row)
        enriched.append(
            {
                **row,
                "longterm_class": longterm_class,
                "classification_note": note,
            }
        )
    write_csv(enriched)
    write_md(enriched)
    print(f"written={OUT_CSV.relative_to(ROOT)}")
    print(f"written={OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
