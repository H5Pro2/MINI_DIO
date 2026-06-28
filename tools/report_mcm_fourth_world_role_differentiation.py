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


def _int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _rank(anchor_class: str) -> int:
    return CLASS_RANK.get(anchor_class or "-", 0)


def _reading_by_token(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {row.get("short_token", ""): row for row in rows if row.get("short_token")}


def _classify(row: dict[str, str], reading: dict[str, str] | None) -> tuple[str, str]:
    previous_classes = [row.get(f"L{label}_class", "-") or "-" for label in ("894", "901", "911")]
    current_class = row.get("L923_class", "-") or "-"
    previous_visible = [value for value in previous_classes if value != "-"]
    current_rank = _rank(current_class)
    max_previous_rank = max((_rank(value) for value in previous_classes), default=0)
    trend = row.get("trend", "-") or "-"
    read_state = (reading or {}).get("read_state", "-")

    if current_class == "-" and previous_visible:
        return "aus_vierter_welt_entlastet", "Token war vorher sichtbar, in der vierten Landschaft aber nicht mehr."
    if current_class == "-" and not previous_visible:
        return "nicht_sichtbar", "Token ist in keiner betrachteten Landschaft sichtbar."
    if not previous_visible and current_class != "-":
        return "neue_vierte_welt_insel", "Token wird erst in der vierten Landschaft sichtbar."

    if read_state in {"kernnaehe_gehalten", "verdichtung_gehalten", "stabil_bestaetigt"}:
        return "memory_getragen", "Die aus 894->901 gebildete Memory wird in der vierten Landschaft erneut getragen."
    if trend == "kernnah_gehalten" or (current_rank >= 3 and max_previous_rank >= 3):
        return "kernrolle_getragen", "Token bleibt ueber mehrere Landschaften kernnah oder stark angeschlossen."
    if read_state in {"verdichtung_entlastet_oder_driftet", "stabilitaet_gebrochen", "kernnaehe_verloren"}:
        return "reorganisation_oder_drift", "Gespeicherte Rollenqualitaet wird sichtbar umgebaut oder verliert Bindung."
    if trend == "rollendrift":
        return "rollendrift", "Die Klassenfolge wechselt, ohne vollstaendig zu verschwinden."
    if trend == "absteigende_entlastung":
        return "entlastung", "Die Rolle wird schwacher oder verlaesst den Kernbereich."
    if trend == "aufsteigende_verdichtung":
        return "neue_oder_fortgesetzte_verdichtung", "Die Rolle gewinnt Sichtbarkeit oder Anschluss."
    if trend == "stabile_rolle":
        return "stabile_oberflaeche", "Die Klasse bleibt formal stabil."
    return "offen", "Kein eindeutiger Differenzierungsstatus."


def _rows(sequence_rows: list[dict[str, str]], reading_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    reading_map = _reading_by_token(reading_rows)
    out: list[dict[str, str]] = []
    for row in sequence_rows:
        short = row.get("short_token", "")
        reading = reading_map.get(short)
        status, reason = _classify(row, reading)
        out.append(
            {
                "short_token": short,
                "status": status,
                "reason": reason,
                "trend": row.get("trend", "-"),
                "read_state": (reading or {}).get("read_state", "-"),
                "class_sequence": row.get("class_sequence", "-"),
                "weight_sequence": row.get("weight_sequence", "-"),
                "world_span_sequence": row.get("world_span_sequence", "-"),
                "L923_class": row.get("L923_class", "-"),
                "L923_weight": row.get("L923_weight", "0"),
                "rank_delta_from_max": (reading or {}).get("rank_delta_from_max", "-"),
            }
        )
    out.sort(
        key=lambda item: (
            item["status"],
            -_int(item.get("L923_weight", "0")),
            item["short_token"],
        )
    )
    return out


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _table(rows: list[dict[str, str]], status: str, limit: int = 14) -> list[str]:
    selected = [row for row in rows if row["status"] == status][:limit]
    lines = [
        "| Token | Status | Trend | Memory-Lesung | Klassenfolge | Gewichtfolge |",
        "|---|---|---|---|---|---|",
    ]
    for row in selected:
        lines.append(
            f"| `{row['short_token']}` | {row['status']} | {row['trend']} | {row['read_state']} | {row['class_sequence']} | {row['weight_sequence']} |"
        )
    return lines


def _write_md(path: Path, rows: list[dict[str, str]]) -> None:
    counts = Counter(row["status"] for row in rows)
    lines: list[str] = []
    lines.append("# MCM-Rollendifferenzierung der vierten Welt")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append("Diese Diagnose trennt die vierte Landschaft nach Rollenqualitaet.")
    lines.append("Geprueft wird nicht, ob ein Token exakt gleich bleibt, sondern ob die vierte Welt neue Inseln bildet, bestehende Rollen traegt oder Drift/Reorganisation sichtbar macht.")
    lines.append("")
    lines.append("## Profil")
    lines.append("")
    lines.append("| Status | Anzahl |")
    lines.append("|---|---:|")
    for status, count in counts.most_common():
        lines.append(f"| {status} | {count} |")
    lines.append("")
    for status in (
        "memory_getragen",
        "kernrolle_getragen",
        "neue_vierte_welt_insel",
        "reorganisation_oder_drift",
        "rollendrift",
        "entlastung",
    ):
        if counts.get(status, 0):
            lines.append(f"## {status}")
            lines.append("")
            lines.extend(_table(rows, status))
            lines.append("")
    lines.append("## Befund")
    lines.append("")
    lines.append("Die vierte Landschaft wirkt nicht wie eine reine Wiederholung.")
    lines.append("Ein Teil der Rollenbewegungs-Memory wird getragen, ein Teil wird umgebaut, und ein Teil taucht als neue vierte-Welt-Insel auf.")
    lines.append("Damit wird `dio_role_*` als passive Rollenbewegung lesbar: nicht starre Klasse, sondern Feldverlauf mit Tragen, Drift, Entlastung und neuer Verdichtung.")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    lines.append("Als naechstes sollte die Reorganisationsgruppe isoliert werden: Welche Sinnes-/Feldachsen kippen dort zuerst, und ob diese Kippung eine neue Bedeutungsinsel vorbereitet oder nur Entlastung ist.")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sequence", required=True, type=Path)
    parser.add_argument("--reading", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    rows = _rows(_read(args.sequence), _read(args.reading))
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
