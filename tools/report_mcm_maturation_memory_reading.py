from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


CLASS_RANK = {
    "-": 0,
    "schwacher_anschluss": 1,
    "schwacher_brueckenpfad": 1,
    "lokaler_anschlussanker": 2,
    "starker_anschlussanker": 3,
    "brueckenkern": 4,
}


def _read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _short(token: str) -> str:
    return token.replace("dio_mcm_episode_", "")


def _rank(value: str) -> int:
    return CLASS_RANK.get(value or "-", 0)


def _by_short(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for row in rows:
        short = row.get("short_token") or _short(row.get("token", ""))
        if short:
            out[short] = row
    return out


def _read_state(memory: dict[str, str], current: dict[str, str] | None) -> tuple[str, str]:
    maturation = memory.get("maturation_quality") or memory.get("memory_maturation_quality", "-")
    longterm_class = memory.get("longterm_class", "-")
    memory_class = memory.get("follow_class") or memory.get("memory_follow_class", "-")
    current_class = (current or {}).get("anchor_class", "-")
    memory_rank = _rank(memory_class)
    current_rank = _rank(current_class)

    if current is None:
        if longterm_class == "verschwunden_bestaetigt":
            return "verschwindung_weiter_bestaetigt", "Langzeitklasse erwartete bestaetigtes Verschwinden; Folgewelt zeigt keine sichtbare Rolle."
        if longterm_class == "kurzfristige_oberflaeche":
            return "oberflaeche_weiter_nicht_getragen", "Kurzfristige Oberflaeche bleibt in Folgewelt unsichtbar."
        if longterm_class in {"langfristig_getragen", "langfristig_belastet_getragen"}:
            return "langzeitspur_verloren", "Vorher langfristig gelesene Spur wird in dieser Folgewelt nicht wiedergefunden."
        if longterm_class == "weltabhaengig_getragen":
            return "weltabhaengigkeit_bestaetigt_durch_verlust", "Weltabhaengige Spur wird in dieser Folgewelt nicht getragen."
        if longterm_class == "abgeschwaecht_oder_verloren":
            return "verlust_weiter_bestaetigt", "Abgeschwaechte/verlorene Spur bleibt unsichtbar."
        if maturation == "maturation_verschwindet":
            return "verschwindung_bestaetigt", "Memory erwartete/las Verschwinden; Folgewelt zeigt keine sichtbare Rolle."
        return "nicht_wiedergefunden", "Reifungsspur ist in der Folgewelt nicht sichtbar."

    if longterm_class == "langfristig_getragen":
        if current_rank >= 2:
            return "langzeitspur_getragen", "Langfristige Spur bleibt mindestens lokal sichtbar."
        return "langzeitspur_abgeschwaecht", "Langfristige Spur ist sichtbar, aber verliert Anschluss."
    if longterm_class == "langfristig_belastet_getragen":
        if current_rank > 0:
            return "belastete_langzeitspur_sichtbar", "Belastete Langzeitspur bleibt sichtbar."
    if longterm_class == "weltabhaengig_getragen":
        if current_rank > 0:
            return "weltabhaengige_spur_sichtbar", "Weltabhaengige Spur erscheint wieder, bleibt aber nicht automatisch stabil."
    if longterm_class == "kurzfristige_oberflaeche":
        return "oberflaeche_taucht_wieder_auf", "Vorher kurzfristige Oberflaeche taucht wieder auf."
    if longterm_class == "verschwunden_bestaetigt":
        return "verschwindung_widersprochen", "Spur erscheint wieder, obwohl Verschwinden als Langzeitklasse gelesen wurde."

    if maturation == "maturation_reifung":
        if current_rank >= memory_rank and current_rank >= 3:
            return "reifung_bestaetigt", "Reifung bleibt stark oder kernnah sichtbar."
        if current_rank > 0:
            return "reifung_abgeschwaecht", "Reifung bleibt sichtbar, aber weniger tragend."
    if maturation == "maturation_jung_gehalten":
        if current_rank <= 1:
            return "jung_gehalten_bestaetigt", "Junge Spur bleibt schwach/jung."
        return "jungspur_reift", "Junge Spur gewinnt Anschlussreife."
    if maturation == "maturation_reorganisationsbruecke_gehalten":
        if current_rank >= 2:
            return "bruecke_gehalten", "Reorganisationsbruecke bleibt mindestens lokal sichtbar."
        return "bruecke_verliert_bindung", "Reorganisationsbruecke verliert Anschluss."
    if maturation == "maturation_rolle_gehalten":
        if current_rank == memory_rank:
            return "rolle_gehalten_bestaetigt", "Rolle bleibt auf gleicher Stufe sichtbar."
        if current_rank > memory_rank:
            return "rolle_reift_weiter", "Rolle gewinnt Reife."
        return "rolle_entlastet", "Rolle wird schwaecher."
    if maturation == "maturation_verschwindet":
        return "verschwindung_widersprochen", "Spur erscheint wieder, obwohl sie vorher verschwand."

    return "offen_gelesen", "Keine eindeutige Reifungslesung."


def _rows(memory_rows: list[dict[str, str]], landscape_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    landscape = _by_short(landscape_rows)
    out: list[dict[str, str]] = []
    for memory in memory_rows:
        short = memory.get("short_token", "")
        current = landscape.get(short)
        state, reason = _read_state(memory, current)
        out.append(
            {
                "maturation_symbol": memory.get("maturation_symbol", ""),
                "short_token": short,
                "memory_longterm_class": memory.get("longterm_class", "-"),
                "memory_maturation_quality": memory.get("maturation_quality") or memory.get("memory_maturation_quality", "-"),
                "memory_segment_quality": memory.get("segment_quality") or memory.get("memory_segment_quality", "-"),
                "memory_field_quality": memory.get("field_quality") or memory.get("memory_field_quality", "-"),
                "memory_follow_class": memory.get("follow_class") or memory.get("memory_follow_class", "-"),
                "current_class": (current or {}).get("anchor_class", "-"),
                "current_weight": (current or {}).get("total_weight", "0"),
                "current_world_span": (current or {}).get("max_world_span", "0"),
                "read_state": state,
                "reason": reason,
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
    lines: list[str] = []
    lines.append("# MCM-Rollenreifungs-Memory Lesung")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append("Diese Diagnose liest passive `dio_mature_*` Reifungs-Memory gegen eine weitere Landschaft.")
    lines.append("Geprueft wird, ob Reifung bestaetigt, abgeschwaecht, gehalten, entlastet oder nicht wiedergefunden wird.")
    lines.append("")
    lines.append("## Lesestatus")
    lines.append("")
    lines.append("| Status | Anzahl |")
    lines.append("|---|---:|")
    for state, count in counts.most_common():
        lines.append(f"| {state} | {count} |")
    lines.append("")
    lines.append("## Tokens")
    lines.append("")
    lines.append("| Symbol | Token | Memory | Aktuell | Lesung |")
    lines.append("|---|---|---|---|---|")
    for row in rows:
        lines.append(
            f"| `{row['maturation_symbol']}` | `{row['short_token']}` | {row['memory_longterm_class']} / {row['memory_maturation_quality']} / {row['memory_follow_class']} | {row['current_class']} | {row['read_state']} |"
        )
    lines.append("")
    lines.append("## Befund")
    lines.append("")
    lines.append("Die Reifungs-Memory wird als passive Folgequalitaet gelesen.")
    lines.append("Wichtig ist nicht nur, ob ein Token wieder auftaucht, sondern ob seine Reifung gleichartig getragen bleibt.")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    lines.append("Als naechstes sollte die Lesung synthetisiert werden: Welche Reifungsqualitaeten sind stabil genug fuer langfristige passive Memory, und welche bleiben nur kurzfristige Oberflaeche?")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--memory", required=True, type=Path)
    parser.add_argument("--landscape", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    rows = _rows(_read(args.memory), _read(args.landscape))
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
