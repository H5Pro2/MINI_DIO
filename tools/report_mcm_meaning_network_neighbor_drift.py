from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

from befunde_paths import befunde_root


ROOT = Path(__file__).resolve().parents[1]
IN_CSV = befunde_root(ROOT) / "1390_BEDEUTUNGSNETZ_FOLGEWELTEN.csv"
OUT_CSV = befunde_root(ROOT) / "1391_BEDEUTUNGSNETZ_NACHBARSCHAFTSDRIFT.csv"
OUT_MD = befunde_root(ROOT) / "1391_BEDEUTUNGSNETZ_NACHBARSCHAFTSDRIFT.md"


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def _drift_state(exact_count: int, near_count: int, new_signatures: int, worlds: int) -> str:
    if exact_count >= 3 and new_signatures <= 2:
        return "stabil_wiederkehrend"
    if exact_count > 0 and near_count > exact_count and new_signatures >= 3:
        return "wiederkehr_mit_teilung"
    if near_count >= 5 and worlds >= 2 and exact_count == 0:
        return "nachbarschaft_ohne_exakten_kern"
    if new_signatures >= 4:
        return "offene_aufteilung"
    return "schwache_spur"


def main() -> None:
    rows = _read_rows(IN_CSV)
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        node = row.get("exact_old_node") or row.get("nearest_old_node")
        if node:
            grouped[node].append(row)

    out_rows: list[dict[str, str]] = []
    for node, node_rows in sorted(grouped.items()):
        exact_rows = [row for row in node_rows if row.get("exact_old_node") == node]
        near_rows = [row for row in node_rows if row.get("nearest_old_node") == node and not row.get("exact_old_node")]
        signatures = Counter(row.get("mischlinien_signature", "") for row in node_rows)
        near_signatures = Counter(row.get("mischlinien_signature", "") for row in near_rows)
        worlds = Counter(row.get("world", "") for row in node_rows)
        states = Counter(row.get("follow_state", "") for row in node_rows)
        old_state = ""
        for row in node_rows:
            old_state = row.get("exact_old_state") or row.get("nearest_old_state") or old_state

        out_rows.append(
            {
                "old_node": node,
                "old_state": old_state,
                "total_windows": str(len(node_rows)),
                "exact_windows": str(len(exact_rows)),
                "near_windows": str(len(near_rows)),
                "world_count": str(len(worlds)),
                "signature_count": str(len(signatures)),
                "near_signature_count": str(len(near_signatures)),
                "drift_state": _drift_state(
                    len(exact_rows),
                    len(near_rows),
                    len(near_signatures),
                    len(worlds),
                ),
                "top_worlds": " | ".join(f"{key}:{value}" for key, value in worlds.most_common(4)),
                "follow_states": " | ".join(f"{key}:{value}" for key, value in states.most_common()),
                "top_signatures": " || ".join(
                    f"{signature}:{count}" for signature, count in signatures.most_common(4)
                ),
            }
        )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    drift_counts = Counter(row["drift_state"] for row in out_rows)
    strongest = sorted(out_rows, key=lambda row: int(row["total_windows"]), reverse=True)[:10]
    split_like = [
        row
        for row in out_rows
        if row["drift_state"] in {"wiederkehr_mit_teilung", "nachbarschaft_ohne_exakten_kern", "offene_aufteilung"}
    ]

    lines = [
        "# 1391 - Bedeutungsnetz Nachbarschaftsdrift",
        "",
        "## Zweck",
        "",
        "Diese Diagnose isoliert alte Bedeutungsnetz-Knoten aus `1390` und prueft, ob Folgewelten sie exakt wiederfinden, nur benachbart aktivieren oder in mehrere Nachbarschaften aufteilen.",
        "",
        "Die Diagnose bleibt passiv. Sie beschreibt Feldnaehe, keine Handlung.",
        "",
        "## Befund",
        "",
        f"- untersuchte alte Knoten: `{len(out_rows)}`",
        f"- Driftzustaende: `{', '.join(f'{key}:{value}' for key, value in drift_counts.most_common())}`",
        f"- Knoten mit moeglicher Teilung oder Erweiterung: `{len(split_like)}`",
        "",
        "## Staerkste Knoten",
        "",
        *[
            f"- `{row['old_node']}` ({row['old_state']}): `{row['drift_state']}`, Fenster `{row['total_windows']}`, exakt `{row['exact_windows']}`, nah `{row['near_windows']}`, Welten `{row['world_count']}`"
            for row in strongest
        ],
        "",
        "## Lesung",
        "",
        "Stabil wiederkehrende Knoten wirken wie ein erhaltener Bedeutungsanker.",
        "Wiederkehr mit Teilung bedeutet: ein alter Knoten bleibt erkennbar, bildet aber neue Nachbarschaften aus.",
        "Nachbarschaft ohne exakten Kern bedeutet: Die alte Bedeutung wird nicht kopiert, aber das Feld findet weiterhin eine aehnliche Lage.",
        "",
        "## Wie es weitergeht",
        "",
        "Als naechstes sollte fuer die teilenden Knoten geprueft werden, welche Sinnesachse die Teilung traegt: Ton, Sicht, Rezeptorkontakt oder MCM-Feldspannung.",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
