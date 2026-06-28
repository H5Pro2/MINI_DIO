from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


def _read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def _int(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def _float(value: str) -> float:
    try:
        return float(value or 0.0)
    except ValueError:
        return 0.0


def _token(short_token: str) -> str:
    return f"dio_mcm_episode_{short_token}"


def _profile(details: list[dict[str, str]], token: str, landscape: str) -> dict[str, object]:
    rows = [row for row in details if row.get("token") == token]
    if not rows:
        return {
            "landscape": landscape,
            "segments": 0,
            "first_tick": 0,
            "last_tick": 0,
            "duration_sum": 0.0,
            "avg_duration": 0.0,
            "max_duration": 0.0,
            "worlds": "",
            "dominant_world": "",
        }
    worlds: dict[str, int] = defaultdict(int)
    duration_sum = 0.0
    max_duration = 0.0
    first_tick = min(_int(row.get("start_tick", "0")) for row in rows)
    last_tick = max(_int(row.get("end_tick", "0")) for row in rows)
    for row in rows:
        duration = _float(row.get("duration", "0"))
        duration_sum += duration
        max_duration = max(max_duration, duration)
        worlds[row.get("world", "-")] += 1
    dominant_world = max(worlds.items(), key=lambda item: item[1])[0]
    return {
        "landscape": landscape,
        "segments": len(rows),
        "first_tick": first_tick,
        "last_tick": last_tick,
        "duration_sum": duration_sum,
        "avg_duration": duration_sum / max(1, len(rows)),
        "max_duration": max_duration,
        "worlds": "|".join(sorted(worlds)),
        "dominant_world": dominant_world,
    }


def _row_for(cond: dict[str, str], base_details: list[dict[str, str]], compare_details: list[dict[str, str]]) -> dict[str, str]:
    short = cond.get("short_token", "")
    token = _token(short)
    base = _profile(base_details, token, "894_basis")
    compare = _profile(compare_details, token, "901_vergleich")
    base_segments = _int(str(base["segments"]))
    compare_segments = _int(str(compare["segments"]))
    if base_segments == 0 and compare_segments == 0:
        first_shift = "detaildaten_fehlend"
    elif base_segments == 0 and compare_segments > 0:
        first_shift = "compare_only"
    elif base_segments > 0 and compare_segments == 0:
        first_shift = "base_only"
    else:
        first_shift = "both_landscapes"
    return {
        "short_token": short,
        "base_class": cond.get("base_class", "-"),
        "compare_class": cond.get("compare_class", "-"),
        "condensation_stage": cond.get("condensation_stage", "-"),
        "first_shift": first_shift,
        "base_segments": str(base["segments"]),
        "base_first_tick": str(base["first_tick"]),
        "base_last_tick": str(base["last_tick"]),
        "base_duration_sum": f"{float(base['duration_sum']):.6f}",
        "base_avg_duration": f"{float(base['avg_duration']):.6f}",
        "base_max_duration": f"{float(base['max_duration']):.6f}",
        "base_worlds": str(base["worlds"]),
        "base_dominant_world": str(base["dominant_world"]),
        "compare_segments": str(compare["segments"]),
        "compare_first_tick": str(compare["first_tick"]),
        "compare_last_tick": str(compare["last_tick"]),
        "compare_duration_sum": f"{float(compare['duration_sum']):.6f}",
        "compare_avg_duration": f"{float(compare['avg_duration']):.6f}",
        "compare_max_duration": f"{float(compare['max_duration']):.6f}",
        "compare_worlds": str(compare["worlds"]),
        "compare_dominant_world": str(compare["dominant_world"]),
    }


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, str]]) -> None:
    compare_only = [row for row in rows if row["first_shift"] == "compare_only"]
    both = [row for row in rows if row["first_shift"] == "both_landscapes"]
    missing = [row for row in rows if row["first_shift"] == "detaildaten_fehlend"]
    lines: list[str] = []
    lines.append("# MCM-Verdichtungspfade Zeitordnung")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append("Diese Diagnose prueft, ob die Verdichtungsstufen aus 906 zeitlich als Folge sichtbar werden oder ob sie erst im Vergleich zweier Landschaften auftreten.")
    lines.append("")
    lines.append("## Profil")
    lines.append("")
    lines.append(f"- Verdichtende Tokens gesamt: `{len(rows)}`")
    lines.append(f"- In beiden Landschaften vorhanden: `{len(both)}`")
    lines.append(f"- Erst in Vergleichslandschaft sichtbar: `{len(compare_only)}`")
    lines.append(f"- In den Detaildaten nicht zeitlich pruefbar: `{len(missing)}`")
    lines.append("")
    lines.append("## Tokens")
    lines.append("")
    lines.append("| Token | Stufe | Basis Segmente | Vergleich Segmente | Basis Erste | Vergleich Erste | Vergleich Dominante Welt | Lesung |")
    lines.append("|---|---|---:|---:|---:|---:|---|---|")
    for row in rows:
        if row["first_shift"] == "compare_only":
            reading = "neue Verdichtung in Folgelandschaft"
        elif row["first_shift"] == "detaildaten_fehlend":
            reading = "nicht zeitlich pruefbar"
        else:
            reading = "Rollenumbau vorhandener Spur"
        lines.append(
            f"| `{row['short_token']}` | {row['condensation_stage']} | {row['base_segments']} | {row['compare_segments']} | {row['base_first_tick']} | {row['compare_first_tick']} | {row['compare_dominant_world']} | {reading} |"
        )
    lines.append("")
    lines.append("## Befund")
    lines.append("")
    lines.append("Die pruefbaren Detaildaten zeigen keine einfache interne Zeitreihe im Sinne einer festen Leiter innerhalb einer einzelnen Landschaft.")
    lines.append("Stattdessen gibt es zwei pruefbare Muster:")
    lines.append("")
    lines.append("1. vorhandene Spuren werden in der Vergleichslandschaft anders organisiert und rollenhaft verdichtet.")
    lines.append("2. neue Spuren treten erst in der Vergleichslandschaft auf und erscheinen dort bereits als verdichtete Rolle.")
    lines.append("")
    lines.append("Ein Teil der 906-Kandidaten ist in diesen Detaildaten nicht zeitlich pruefbar. Fuer diese Tokens bleibt die Rollenwanderung ein Landschaftsvergleich, keine Zeitfolgen-Aussage.")
    lines.append("")
    lines.append("Damit ist die Verdichtung in den pruefbaren Faellen eher landschafts- und nachbarschaftsabhaengig als eine starre lineare Entwicklungsfolge.")
    lines.append("")
    lines.append("## Konsequenz")
    lines.append("")
    lines.append("Mini-DIO sollte Rollenreifung nicht als feste Leiter speichern.")
    lines.append("Besser ist eine dynamische Reifelesung:")
    lines.append("")
    lines.append("```text")
    lines.append("Diese Spur war vorhanden.")
    lines.append("Unter anderer Welt- und Nachbarschaftsspannung traegt sie eine andere Rolle.")
    lines.append("Manche Spuren entstehen erst in neuer Weltspannung und sind dort direkt verdichtet.")
    lines.append("```")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    lines.append("Als naechstes sollte eine echte Mehrlandschafts-Folge gebaut werden: nicht nur Basis vs. Vergleich, sondern drei oder mehr Landschaften in Reihenfolge, um Rollenreife und Rollendrift als Verlauf zu messen.")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--condensations", required=True, type=Path)
    parser.add_argument("--base-details", required=True, type=Path)
    parser.add_argument("--compare-details", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    cond = _read(args.condensations)
    base_details = _read(args.base_details)
    compare_details = _read(args.compare_details)
    rows = [_row_for(row, base_details, compare_details) for row in cond]
    rows.sort(key=lambda row: (row["first_shift"], row["short_token"]))
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
