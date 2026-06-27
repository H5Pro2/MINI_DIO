from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _int(row: dict[str, str], key: str) -> int:
    try:
        return int(float(row.get(key, "") or 0))
    except ValueError:
        return 0


def _float(row: dict[str, str], key: str) -> float:
    try:
        value = float(row.get(key, "") or 0.0)
    except ValueError:
        return 0.0
    return 0.0 if value != value else value


def _path_map(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {row.get("token", "-") or "-": row for row in rows}


def _zone_for(token: str, path_rows: dict[str, dict[str, str]]) -> str:
    row = path_rows.get(token)
    if not row:
        return "unbekannt"
    return row.get("follow_zone", "-") or "-"


def _class_for(token: str, path_rows: dict[str, dict[str, str]]) -> str:
    row = path_rows.get(token)
    if not row:
        return "unbekannt"
    return row.get("path_class", "-") or "-"


def _role_for(token: str, path_rows: dict[str, dict[str, str]]) -> str:
    row = path_rows.get(token)
    if not row:
        return "unbekannt"
    return row.get("follow_role", "-") or "-"


def _collect(edges: list[dict[str, str]], path_rows: dict[str, dict[str, str]], core_tokens: set[str]) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for row in edges:
        source = row.get("source", "-") or "-"
        target = row.get("target", "-") or "-"
        source_is_core = source in core_tokens
        target_is_core = target in core_tokens
        if not source_is_core and not target_is_core:
            continue
        if source_is_core and target_is_core:
            direction_type = "kern_intern"
            outside = "-"
        elif source_is_core:
            direction_type = "kern_zu_aussen"
            outside = target
        else:
            direction_type = "aussen_zu_kern"
            outside = source
        out.append(
            {
                "source": source,
                "target": target,
                "direction_type": direction_type,
                "outside_token": outside,
                "outside_path_class": _class_for(outside, path_rows) if outside != "-" else "-",
                "outside_zone": _zone_for(outside, path_rows) if outside != "-" else "-",
                "outside_role": _role_for(outside, path_rows) if outside != "-" else "-",
                "relation": row.get("relation", "-") or "-",
                "edge_kind": row.get("edge_kind", "-") or "-",
                "count": _int(row, "count"),
                "worlds": _int(row, "worlds"),
                "duration_avg": _float(row, "duration_avg"),
                "exit_phase": row.get("exit_phase", "-") or "-",
                "exit_rekopplung_delta_avg": _float(row, "exit_rekopplung_delta_avg"),
                "exit_strain_delta_avg": _float(row, "exit_strain_delta_avg"),
            }
        )
    out.sort(key=lambda item: (-int(item["count"]), str(item["direction_type"]), str(item["outside_path_class"]), str(item["outside_token"])))
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


def _weighted_counts(rows: list[dict[str, object]], key: str, direction_type: str) -> Counter[str]:
    counts: Counter[str] = Counter()
    for row in rows:
        if row["direction_type"] != direction_type:
            continue
        counts[str(row[key])] += int(row["count"])
    return counts


def _write_counts(lines: list[str], title: str, counts: Counter[str]) -> None:
    lines.extend(["", title, "", "| Typ | Gewicht |", "|---|---:|"])
    if counts:
        for name, count in counts.most_common():
            lines.append(f"| {name} | {count} |")
    else:
        lines.append("| - | 0 |")


def _write_markdown(rows: list[dict[str, object]], core_tokens: set[str], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    direction_counts = Counter(str(row["direction_type"]) for row in rows)
    phase_counts = Counter()
    for row in rows:
        phase_counts[str(row["exit_phase"])] += int(row["count"])

    lines = [
        "# MCM-Zentraler Brueckenkern Zielrollen",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest, wohin der zentrale Brueckenkern fuehrt.",
        "Sie unterscheidet interne Kernbewegung, Austritt aus dem Kern und Eintritt von aussen in den Kern.",
        "",
        f"- Kern: `{', '.join(sorted(core_tokens))}`",
        "",
        "## Kantenbestand",
        "",
        "| Richtungstyp | Kanten |",
        "|---|---:|",
    ]
    for name, count in sorted(direction_counts.items()):
        lines.append(f"| {name} | {count} |")

    _write_counts(lines, "## Austritte Vom Kern Nach Pfadklasse", _weighted_counts(rows, "outside_path_class", "kern_zu_aussen"))
    _write_counts(lines, "## Austritte Vom Kern Nach Zone", _weighted_counts(rows, "outside_zone", "kern_zu_aussen"))
    _write_counts(lines, "## Eintritte In Den Kern Nach Pfadklasse", _weighted_counts(rows, "outside_path_class", "aussen_zu_kern"))
    _write_counts(lines, "## Eintritte In Den Kern Nach Zone", _weighted_counts(rows, "outside_zone", "aussen_zu_kern"))

    lines.extend(["", "## Staerkste Kernkontakte", "", "| Richtung | Quelle | Ziel | Gewicht | Welten | Aussenklasse | Aussenzone | Phase |", "|---|---|---|---:|---:|---|---|---|"])
    for row in rows[:24]:
        lines.append(
            f"| {row['direction_type']} | {row['source']} | {row['target']} | {row['count']} | {row['worlds']} | "
            f"{row['outside_path_class']} | {row['outside_zone']} | {row['exit_phase']} |"
        )

    lines.extend(["", "## Austrittsphasen Gewichtet", "", "| Phase | Gewicht |", "|---|---:|"])
    for name, count in phase_counts.most_common():
        lines.append(f"| {name} | {count} |")

    exit_classes = _weighted_counts(rows, "outside_path_class", "kern_zu_aussen")
    exit_zones = _weighted_counts(rows, "outside_zone", "kern_zu_aussen")
    lines.extend(["", "## Befund", ""])
    if exit_classes:
        top_class, top_weight = exit_classes.most_common(1)[0]
        lines.append(f"Der zentrale Kern fuehrt gewichtet am staerksten zu `{top_class}` mit Gewicht `{top_weight}`.")
    if exit_zones:
        top_zone, top_weight = exit_zones.most_common(1)[0]
        lines.append(f"Die staerkste Zielzone ausserhalb des Kerns ist `{top_zone}` mit Gewicht `{top_weight}`.")
    if exit_classes.get("randpfad", 0) <= 1:
        lines.append("Der zentrale Kern fuehrt kaum direkt in Randpfade. Er wirkt eher als Zentrum-/Rekopplungsuebergang als als Randkanal.")
    if exit_classes.get("stabile_insel", 0) + exit_classes.get("rekoppelnder_pfad", 0) > exit_classes.get("offener_driftpfad", 0):
        lines.append("Die Austritte fuehren staerker in stabile oder rekoppelnde Rollen als in offene Drift. Das stuetzt die Lesart eines stabilisierenden Uebergangskerns.")

    lines.extend(
        [
            "",
            "## Bedeutung",
            "",
            "Der zentrale Brueckenkern wirkt nicht wie ein chaotischer Durchbruch nach aussen.",
            "Er verbindet vor allem interne Brueckenbewegung mit stabilen oder rekoppelnden Anschlussrollen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte derselbe Zielrollen-Test fuer die sekundaeren Brueckenkerne laufen. Dann wird sichtbar, ob der zentrale Kern eine Sonderrolle hat oder ob alle Kerne aehnlich anschliessen.",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--edges", required=True)
    parser.add_argument("--paths", required=True)
    parser.add_argument("--core-token", action="append", required=True)
    parser.add_argument("--out-md", required=True)
    parser.add_argument("--out-csv", required=True)
    args = parser.parse_args()

    rows = _collect(_load(Path(args.edges)), _path_map(_load(Path(args.paths))), set(args.core_token))
    _write_csv(rows, Path(args.out_csv))
    _write_markdown(rows, set(args.core_token), Path(args.out_md))
    print(f"core_edges={len(rows)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
