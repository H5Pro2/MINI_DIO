from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

from befunde_paths import befunde_root


ROOT = Path(__file__).resolve().parents[1]
IN_CSV = befunde_root(ROOT) / "1390_BEDEUTUNGSNETZ_FOLGEWELTEN.csv"
OUT_CSV = befunde_root(ROOT) / "1392_BEDEUTUNGSNETZ_TEILUNGSACHSEN.csv"
OUT_MD = befunde_root(ROOT) / "1392_BEDEUTUNGSNETZ_TEILUNGSACHSEN.md"

AXES = ("hoeren", "sehen", "bewegung_proxy", "feldkontakt")


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def _split_signature(signature: str) -> tuple[str, str, str, str]:
    parts = (signature or "").split("|")
    while len(parts) < 4:
        parts.append("")
    return tuple(parts[:4])  # type: ignore[return-value]


def _axis_summary(values: list[str]) -> tuple[int, str]:
    counter = Counter(values)
    return len(counter), " | ".join(f"{key}:{value}" for key, value in counter.most_common(4))


def _carrier_axis(unique_counts: dict[str, int]) -> str:
    ranked = sorted(unique_counts.items(), key=lambda item: item[1], reverse=True)
    if not ranked:
        return "unklar"
    top_axis, top_value = ranked[0]
    if top_value <= 1:
        return "keine_deutliche_teilung"
    if len(ranked) > 1 and ranked[1][1] == top_value:
        tied = [axis for axis, value in ranked if value == top_value]
        return "mehrfachachse_" + "_".join(tied)
    return top_axis


def main() -> None:
    rows = _read_rows(IN_CSV)
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        node = row.get("nearest_old_node") or row.get("exact_old_node")
        if node:
            grouped[node].append(row)

    out_rows: list[dict[str, str]] = []
    for node, node_rows in sorted(grouped.items()):
        near_rows = [row for row in node_rows if row.get("nearest_old_node") == node and not row.get("exact_old_node")]
        if not near_rows:
            continue
        axis_values: dict[str, list[str]] = {axis: [] for axis in AXES}
        worlds = Counter(row.get("world", "") for row in near_rows)
        old_state = ""
        similarities: list[float] = []
        for row in near_rows:
            old_state = row.get("nearest_old_state") or old_state
            for axis, value in zip(AXES, _split_signature(row.get("mischlinien_signature", ""))):
                axis_values[axis].append(value)
            try:
                similarities.append(float(row.get("nearest_similarity", "0") or 0.0))
            except ValueError:
                similarities.append(0.0)

        unique_counts: dict[str, int] = {}
        summaries: dict[str, str] = {}
        for axis in AXES:
            unique_count, summary = _axis_summary(axis_values[axis])
            unique_counts[axis] = unique_count
            summaries[axis] = summary

        out_rows.append(
            {
                "old_node": node,
                "old_state": old_state,
                "near_windows": str(len(near_rows)),
                "world_count": str(len(worlds)),
                "avg_similarity": f"{(sum(similarities) / len(similarities)) if similarities else 0.0:.6f}",
                "carrier_axis": _carrier_axis(unique_counts),
                "hoeren_unique": str(unique_counts["hoeren"]),
                "sehen_unique": str(unique_counts["sehen"]),
                "bewegung_proxy_unique": str(unique_counts["bewegung_proxy"]),
                "feldkontakt_unique": str(unique_counts["feldkontakt"]),
                "hoeren_summary": summaries["hoeren"],
                "sehen_summary": summaries["sehen"],
                "bewegung_proxy_summary": summaries["bewegung_proxy"],
                "feldkontakt_summary": summaries["feldkontakt"],
                "worlds": " | ".join(f"{key}:{value}" for key, value in worlds.most_common()),
            }
        )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    carrier_counts = Counter(row["carrier_axis"] for row in out_rows)
    strongest = sorted(out_rows, key=lambda row: int(row["near_windows"]), reverse=True)[:10]

    lines = [
        "# 1392 - Bedeutungsnetz Teilungsachsen",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft, welche Sinnes- oder Feldachse die Nachbarschaftsdrift aus `1391` am staerksten traegt.",
        "",
        "Unterschieden werden Hoeren, Sehen, Bewegungsnaehe als Rohwelt-Proxy und Feldkontakt.",
        "",
        "## Befund",
        "",
        f"- untersuchte Nachbarschaftsknoten: `{len(out_rows)}`",
        f"- tragende Achsen: `{', '.join(f'{key}:{value}' for key, value in carrier_counts.most_common())}`",
        "",
        "## Staerkste Nachbarschaftsknoten",
        "",
        *[
            f"- `{row['old_node']}` ({row['old_state']}): Achse `{row['carrier_axis']}`, nahe Fenster `{row['near_windows']}`, Welten `{row['world_count']}`, mittlere Naehe `{row['avg_similarity']}`"
            for row in strongest
        ],
        "",
        "## Lesung",
        "",
        "Wenn die Teilung vor allem im Hoeren liegt, bleibt die Feldrolle sichtbar, waehrend Ton/Energie neue Unterformen bildet.",
        "Wenn sie im Feldkontakt liegt, veraendert sich die innere Aufnahmequalitaet.",
        "Wenn sie im Sehen liegt, waere die sichtbare Form selbst der Haupttreiber der Bedeutungsdrift.",
        "",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
