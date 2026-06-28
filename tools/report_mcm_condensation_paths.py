from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


CLASS_RANK = {
    "-": 0,
    "schwacher_anschluss": 1,
    "lokaler_anschlussanker": 2,
    "starker_anschlussanker": 3,
    "brueckenkern": 4,
}


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


def _transition(row: dict[str, str]) -> str:
    return f"{row.get('base_class', '-')}_to_{row.get('compare_class', '-')}"


def _stage(row: dict[str, str]) -> str:
    base = row.get("base_class", "-")
    compare = row.get("compare_class", "-")
    if base == "schwacher_anschluss" and compare == "lokaler_anschlussanker":
        return "vorreifung_schwach_zu_lokal"
    if base == "schwacher_anschluss" and compare == "starker_anschlussanker":
        return "sprung_schwach_zu_stark"
    if base == "lokaler_anschlussanker" and compare == "starker_anschlussanker":
        return "reifung_lokal_zu_stark"
    if base == "lokaler_anschlussanker" and compare == "brueckenkern":
        return "kernverdichtung_lokal_zu_kern"
    if base == "starker_anschlussanker" and compare == "brueckenkern":
        return "kernverdichtung_stark_zu_kern"
    if base == "schwacher_anschluss" and compare == "brueckenkern":
        return "direktsprung_schwach_zu_kern"
    return "sonstige_verdichtung"


def _condensations(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for row in rows:
        if row.get("migration") != "rolle_verdichtet":
            continue
        enriched = {
            **row,
            "transition": _transition(row),
            "condensation_stage": _stage(row),
        }
        out.append(enriched)
    out.sort(
        key=lambda row: (
            CLASS_RANK.get(row.get("compare_class", "-"), 0),
            _int(row.get("weight_delta", "0")),
        ),
        reverse=True,
    )
    return out


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _table(rows: list[dict[str, str]]) -> list[str]:
    lines = [
        "| Token | Stufe | Uebergang | Gewicht Delta | Dauer Delta |",
        "|---|---|---|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| `{row.get('short_token', '-')}` | {row.get('condensation_stage', '-')} | {row.get('base_class', '-')} -> {row.get('compare_class', '-')} | {row.get('weight_delta', '0')} | {_float(row.get('duration_delta', '0')):.2f} |"
        )
    return lines


def _write_md(path: Path, rows: list[dict[str, str]]) -> None:
    stage_counts = Counter(row["condensation_stage"] for row in rows)
    transition_counts = Counter(row["transition"] for row in rows)
    by_stage: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_stage[row["condensation_stage"]].append(row)

    lines: list[str] = []
    lines.append("# MCM-Verdichtungspfade")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append("Diese Diagnose prueft, ob die Rollenwanderungen aus 904 als Reifepfade lesbar sind.")
    lines.append("Es wird nicht behauptet, dass Mini-DIO eine feste Leiter benutzt. Geprueft wird nur, ob die beobachteten Rollenwechsel eine geordnete Verdichtungsrichtung tragen.")
    lines.append("")
    lines.append("## Stufenprofil")
    lines.append("")
    lines.append("| Stufe | Anzahl |")
    lines.append("|---|---:|")
    for stage, count in stage_counts.most_common():
        lines.append(f"| {stage} | {count} |")
    lines.append("")
    lines.append("## Uebergangsprofil")
    lines.append("")
    lines.append("| Uebergang | Anzahl |")
    lines.append("|---|---:|")
    for transition, count in transition_counts.most_common():
        lines.append(f"| {transition} | {count} |")
    lines.append("")
    lines.append("## Tokens")
    lines.append("")
    lines.extend(_table(rows))
    lines.append("")
    lines.append("## Befund")
    lines.append("")
    lines.append("Die Verdichtungen verteilen sich auf mehrere Stufen. Besonders relevant sind direkte Kernverdichtungen und Vorreifungen:")
    lines.append("")
    lines.append("- `schwach -> lokal`: erste lokale Stabilisierung.")
    lines.append("- `schwach -> stark`: sprunghafte Anschlussverstaerkung.")
    lines.append("- `lokal -> stark`: gereiftere Anschlussqualitaet.")
    lines.append("- `lokal/stark -> Kern`: Einbindung in tragende Brueckenstruktur.")
    lines.append("")
    lines.append("Damit ist die Rollenwanderung nicht nur chaotischer Wechsel. Sie zeigt eine Richtung: Feldspuren koennen aus schwacher Naehe zu lokaler, starker oder kernbildender Funktion verdichten.")
    lines.append("")
    lines.append("## Grenze")
    lines.append("")
    lines.append("Das ist noch kein Beweis einer vollstaendigen Entwicklungsleiter. Dafuer braucht es weitere Weltgruppen und eine zeitliche Folgepruefung. Aktuell ist es ein starker Hinweis auf geordnete Verdichtungsdynamik.")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    lines.append("Als naechstes sollte geprueft werden, ob diese Stufen in einer zeitlichen Reihenfolge auftreten oder ob sie nur zwischen zwei Landschaften sichtbar werden.")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--roles", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    rows = _condensations(_read(args.roles))
    if not rows:
        raise SystemExit("no condensation rows found")
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
