from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _float(value: object) -> float:
    try:
        out = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if out != out else out


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _family_signature(path: Path) -> dict[str, object]:
    rows = _read_csv(path)
    family = rows[0].get("family", path.stem.split("_bridge", 1)[0]) if rows else path.stem
    grouped: dict[str, dict[str, dict[str, str]]] = defaultdict(dict)
    for row in rows:
        grouped[str(row.get("pattern") or "-")][str(row.get("phase") or "-")] = row
    patterns = sorted(grouped)
    event_fields = {
        pattern: grouped[pattern].get("ereignis", {}).get("field", "-")
        for pattern in patterns
    }
    event_tension = {
        pattern: _float(grouped[pattern].get("ereignis", {}).get("avg_tension"))
        for pattern in patterns
    }
    event_rekopplung = {
        pattern: _float(grouped[pattern].get("ereignis", {}).get("avg_rekopplung"))
        for pattern in patterns
    }
    after_fields = {
        pattern: grouped[pattern].get("nachlauf", {}).get("field", "-")
        for pattern in patterns
    }
    after_tension = {
        pattern: _float(grouped[pattern].get("nachlauf", {}).get("avg_tension"))
        for pattern in patterns
    }
    tones = sorted({row.get("tone", "-") for row in rows})

    if patterns == ["tragende_verarbeitung"] and after_fields.get("tragende_verarbeitung") == "offen":
        reading = "tragend_mit_offener_nachprüfung"
    elif patterns == ["tragende_verarbeitung"] and after_fields.get("tragende_verarbeitung") == "rekoppelt":
        reading = "tragend_mit_gehaltener_rekopplung"
    elif patterns == ["kippnaehe"] and event_fields.get("kippnaehe") == "belastet_kippnah":
        reading = "kippnaher_randkontakt"
    elif set(patterns) == {"kippnaehe", "tragende_verarbeitung"}:
        reading = "duale_feldrolle"
    else:
        reading = "gemischte_tickrolle"

    return {
        "family": family,
        "patterns": ";".join(patterns),
        "event_fields": ";".join(f"{key}:{value}" for key, value in event_fields.items()),
        "after_fields": ";".join(f"{key}:{value}" for key, value in after_fields.items()),
        "event_tension": ";".join(f"{key}:{round(value, 6)}" for key, value in event_tension.items()),
        "after_tension": ";".join(f"{key}:{round(value, 6)}" for key, value in after_tension.items()),
        "event_rekopplung": ";".join(f"{key}:{round(value, 6)}" for key, value in event_rekopplung.items()),
        "tones": ";".join(tones),
        "tick_signature_reading": reading,
    }


def _write_md(path: Path, rows: list[dict[str, object]]) -> None:
    lines = [
        "# 1816 - Kernfamilien Tickfenster-Rollenprüfung",
        "",
        "## Grundfrage",
        "",
        "Diese Prüfung kontrolliert, ob die Rollentaxonomie aus 1807 in konkreten Tickfenstern sichtbar bleibt.",
        "",
        "Die Diagnose bleibt passiv: keine Handlung, kein Gate, keine Richtung.",
        "",
        "## Übersicht",
        "",
        "| Familie | Muster | Ereignisfelder | Nachlauffelder | Ton | Tick-Lesung |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['family']}` | `{row['patterns']}` | `{row['event_fields']}` | "
            f"`{row['after_fields']}` | `{row['tones']}` | `{row['tick_signature_reading']}` |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die konkrete Tickfensterprüfung bestätigt die Rollenkarte differenziert und macht die Unterschiede schärfer:",
            "",
            "- `dio_14wj` trägt Rekopplung punktuell sehr sauber, fällt danach aber wieder in offenere Nachprüfung. Das passt zu einem breiten Übergangsknoten.",
            "- `dio_1fll` bleibt über Vorlauf, Ereignis und Nachlauf rekoppelter. Das passt zu einer Sammelrolle mit stärker gehaltener Feldbindung als die reine Randnähe vermuten ließ.",
            "- `dio_0m9z` erscheint in den geprüften Fenstern fast rein kippnah und belastet. Das stützt die Lesung als Hör-/Nachhallknoten mit Randkontakt.",
            "- `dio_155c` trägt beide Seiten: Kippnähe und tragende Verarbeitung. Das wirkt wie eine duale Feldrolle zwischen Lastaufnahme und Rekopplung.",
            "",
            "Damit wird die frühere Taxonomie präziser: Rollen sind nicht nur Kategorien, sondern Feldfolgen. Eine Familie kann Anschluss, Rand, Nachhall oder Brücke je nach Weltfenster verschieden ausprägen.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", action="append", required=True)
    parser.add_argument("--out-csv", default="reports/core_family_tick_signature_summary.csv")
    parser.add_argument("--out-md", default="docs/befunde/1001-2000/1751-2000/1816_KERNFAMILIEN_TICKFENSTER_ROLLENPRUEFUNG.md")
    args = parser.parse_args()

    rows = [_family_signature(ROOT / source) for source in args.source]
    _write_csv(ROOT / args.out_csv, rows)
    _write_md(ROOT / args.out_md, rows)
    print({"rows": len(rows), "out": args.out_md})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
