from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


def _read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _by_short(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for row in rows:
        short = row.get("short_token") or row.get("token", "").replace("dio_mcm_episode_", "")
        if short:
            out[short] = row
    return out


def _classify(memory: dict[str, str], nonbridge: dict[str, str] | None) -> tuple[str, str]:
    longterm = memory.get("longterm_class", "-")
    if nonbridge is None:
        if longterm == "verschwunden_bestaetigt":
            return "nichtbruecke_verschwindung_bestaetigt", "Auch die Nicht-Bruecken-Lesung findet die Spur nicht."
        if longterm == "kurzfristige_oberflaeche":
            return "nichtbruecke_oberflaeche_nicht_getragen", "Kurzfristige Oberflaeche bleibt unsichtbar."
        return "nichtbruecke_nicht_sichtbar", "Spur wird auch ausserhalb der Brueckenlogik nicht sichtbar."

    nb_class = nonbridge.get("nonbridge_class", "-")
    if longterm == "langfristig_getragen":
        if nb_class in {"nichtbruecke_zentrum_getragen", "nichtbruecke_rekopplungsfeld"}:
            return "reifung_bleibt_als_nichtbruecke_getragen", "Langzeitspur verliert Brueckenrolle, bleibt aber zentrumsnah getragen."
        return "reifung_sichtbar_aber_umorganisiert", "Langzeitspur bleibt sichtbar, aber in anderer Nicht-Bruecken-Klasse."
    if longterm == "langfristig_belastet_getragen":
        return "belastete_reifung_bleibt_sichtbar", "Belastete Langzeitspur bleibt als Nicht-Bruecken-Zeichen sichtbar."
    if longterm == "weltabhaengig_getragen":
        return "weltabhaengige_reifung_sichtbar", "Weltabhaengige Spur bleibt sichtbar, aber nicht als stabile Bruecke."
    if longterm == "abgeschwaecht_oder_verloren":
        return "verlorene_reifung_taucht_umorganisiert_auf", "Vorher verlorene Spur erscheint in anderer Ordnung wieder."
    if longterm == "kurzfristige_oberflaeche":
        return "oberflaeche_taucht_umorganisiert_auf", "Kurzfristige Oberflaeche erscheint in Nicht-Bruecken-Ordnung."
    if longterm == "verschwunden_bestaetigt":
        return "verschwindung_widersprochen_durch_nichtbruecke", "Spur verschwand in Brueckenlogik, ist aber als Nicht-Bruecken-Ordnung sichtbar."
    return "nichtbruecke_sichtbar_offen", "Spur ist sichtbar, aber Langzeitdeutung bleibt offen."


def _build(memory_rows: list[dict[str, str]], nonbridge_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    nonbridge = _by_short(nonbridge_rows)
    out: list[dict[str, str]] = []
    for memory in memory_rows:
        short = memory.get("short_token", "")
        current = nonbridge.get(short)
        state, note = _classify(memory, current)
        out.append(
            {
                "maturation_symbol": memory.get("maturation_symbol", ""),
                "short_token": short,
                "longterm_class": memory.get("longterm_class", "-"),
                "memory_maturation_quality": memory.get("memory_maturation_quality", "-"),
                "memory_follow_class": memory.get("memory_follow_class", "-"),
                "nonbridge_class": (current or {}).get("nonbridge_class", "-"),
                "condensation_zone": (current or {}).get("condensation_zone", "-"),
                "dominant_role": (current or {}).get("dominant_role", "-"),
                "observations": (current or {}).get("observations", "0"),
                "worlds": (current or {}).get("worlds", "0"),
                "avg_rekopplung": (current or {}).get("avg_rekopplung", "0"),
                "avg_strain": (current or {}).get("avg_strain", "0"),
                "read_state": state,
                "note": note,
            }
        )
    out.sort(key=lambda row: (row["read_state"], row["short_token"]))
    return out


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, str]]) -> None:
    counts = Counter(row["read_state"] for row in rows)
    lines: list[str] = [
        "# MCM-Langzeitreifung gegen Nicht-Bruecken-Ordnung",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft, ob Reifungstokens aus 948 in der siebten Welt zwar nicht als Bruecken, aber als andere Feldordnung sichtbar bleiben.",
        "",
        "## Lesestatus",
        "",
        "| Status | Anzahl |",
        "|---|---:|",
    ]
    for state, count in counts.most_common():
        lines.append(f"| `{state}` | {count} |")

    lines.extend(
        [
            "",
            "## Token-Lesung",
            "",
            "| Token | Langzeitklasse | Nicht-Bruecken-Klasse | Zone | Beobachtungen | Welten | Lesung |",
            "|---|---|---|---|---:|---:|---|",
        ]
    )
    for row in rows:
        lines.append(
            f"| `{row['short_token']}` | `{row['longterm_class']}` | `{row['nonbridge_class']}` | `{row['condensation_zone']}` | {row['observations']} | {row['worlds']} | {row['read_state']} |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Die siebte Welt widerlegt die Reifung nicht einfach.",
            "Sie zeigt, dass ein Zeichen seine Brueckenrolle verlieren kann und trotzdem als zentrumsnahe oder umorganisierte Feldordnung sichtbar bleibt.",
            "",
            "Das ist fachlich wichtig:",
            "",
            "- Brueckenrolle ist eine Organisationsform, nicht die einzige Existenzform eines Zeichens.",
            "- Reifung kann sich unter anderer Weltspannung umlagern.",
            "- Nicht-Wiederfinden in einer Brueckenlandschaft darf nicht automatisch als Feldverlust gelesen werden.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte eine Synthese entscheiden, welche Zeichen wirklich verloren sind und welche nur ihre Rolle gewechselt haben.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--memory", required=True, type=Path)
    parser.add_argument("--nonbridge", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    rows = _build(_read(args.memory), _read(args.nonbridge))
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"rows={len(rows)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
