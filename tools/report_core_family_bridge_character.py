from __future__ import annotations

import argparse
import csv
from collections import Counter
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


def _parse_counter(text: str) -> Counter[str]:
    counter: Counter[str] = Counter()
    for part in str(text or "").split(";"):
        if ":" not in part:
            continue
        key, value = part.rsplit(":", 1)
        counter[key] += int(_float(value))
    return counter


def _norm(value: float, minimum: float, maximum: float, invert: bool = False) -> float:
    if maximum <= minimum:
        out = 0.0
    else:
        out = max(0.0, min(1.0, (value - minimum) / (maximum - minimum)))
    return 1.0 - out if invert else out


def _bridge_reading(score: float, role_diversity: int, bridge_share: float, distance: float) -> str:
    if score >= 0.72 and role_diversity >= 5 and distance <= 0.22:
        return "starker_brueckenknoten"
    if score >= 0.58 and role_diversity >= 5:
        return "breiter_uebergangsknoten"
    if bridge_share >= 0.08 and distance <= 0.22:
        return "zielnaher_brueckenanker"
    if distance > 0.24:
        return "weiter_randnaher_knoten"
    return "gemischter_feldknoten"


def _write_md(path: Path, rows: list[dict[str, object]]) -> None:
    lines = [
        "# 1798 - Brückencharakter der Kernfamilien",
        "",
        "## Grundfrage",
        "",
        "Die Prüfung liest, welche Kernfamilie den klarsten Brückencharakter trägt.",
        "",
        "Brückencharakter meint hier: breite Nachbarschaft, geringe Distanz, hohe Achsenähnlichkeit und trotzdem mehrere unterscheidbare Rollen.",
        "",
        "## Rangfolge",
        "",
        "| Rang | Familie | Score | Lesung | Breite | Distanz | Cosinus | Rollenvielfalt | Brückenanteil | Rollenprofil |",
        "|---:|---|---:|---|---:|---:|---:|---:|---:|---|",
    ]
    for index, row in enumerate(rows, start=1):
        lines.append(
            f"| {index} | `{row['family']}` | {row['bridge_score']} | `{row['bridge_reading']}` | "
            f"{row['avg_co_memory_count']} | {row['avg_distance']} | {row['avg_cosine']} | "
            f"{row['role_diversity']} | {row['bridge_role_share']} | `{row['roles']}` |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "- Brückencharakter ist nicht identisch mit maximaler Breite.",
            "- Sehr breite Familien können randnaher wirken, wenn Distanz und Polarisierung steigen.",
            "- Der stärkste Brückencharakter liegt dort, wo Nähe und Rollenvielfalt zusammen auftreten.",
            "",
            "## Vorsicht",
            "",
            "Der Score ist eine Diagnosehilfe, kein absoluter Wert und kein Mechanik-Eingriff.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte der stärkste Brückenkandidat gegen konkrete Weltfenster rückgelesen werden: In welchen Außenweltlagen wird diese Brückenfunktion aktiviert?",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="reports/core_family_role_comparison.csv")
    parser.add_argument("--out-csv", default="reports/core_family_bridge_character.csv")
    parser.add_argument("--out-md", default="docs/befunde/1001-2000/1751-2000/1798_KERNFAMILIEN_BRUECKENCHARAKTER.md")
    args = parser.parse_args()

    rows = _read_csv(ROOT / args.source)
    widths = [_float(row.get("avg_co_memory_count")) for row in rows]
    distances = [_float(row.get("avg_distance")) for row in rows]
    cosines = [_float(row.get("avg_cosine")) for row in rows]
    min_width, max_width = min(widths or [0.0]), max(widths or [1.0])
    min_distance, max_distance = min(distances or [0.0]), max(distances or [1.0])
    min_cosine, max_cosine = min(cosines or [0.0]), max(cosines or [1.0])

    out_rows: list[dict[str, object]] = []
    for row in rows:
        role_counts = _parse_counter(row.get("roles", ""))
        topology_counts = _parse_counter(row.get("topology_bindings", ""))
        total_roles = sum(role_counts.values()) or 1
        role_diversity = len([key for key, value in role_counts.items() if value > 0])
        role_diversity_norm = min(1.0, role_diversity / 8.0)
        bridge_share = topology_counts.get("bruecke_zielnah", 0) / total_roles
        width_norm = _norm(_float(row.get("avg_co_memory_count")), min_width, max_width)
        distance_norm = _norm(_float(row.get("avg_distance")), min_distance, max_distance, invert=True)
        cosine_norm = _norm(_float(row.get("avg_cosine")), min_cosine, max_cosine)
        bridge_score = (
            width_norm * 0.28
            + distance_norm * 0.26
            + cosine_norm * 0.18
            + role_diversity_norm * 0.18
            + min(1.0, bridge_share * 8.0) * 0.10
        )
        out_rows.append(
            {
                "family": row.get("family", "-"),
                "bridge_score": round(bridge_score, 6),
                "bridge_reading": _bridge_reading(
                    bridge_score,
                    role_diversity,
                    bridge_share,
                    _float(row.get("avg_distance")),
                ),
                "avg_co_memory_count": row.get("avg_co_memory_count", "0"),
                "avg_cosine": row.get("avg_cosine", "0"),
                "avg_distance": row.get("avg_distance", "0"),
                "role_diversity": role_diversity,
                "bridge_role_share": round(bridge_share, 6),
                "width_norm": round(width_norm, 6),
                "distance_norm": round(distance_norm, 6),
                "cosine_norm": round(cosine_norm, 6),
                "roles": row.get("roles", "-"),
                "topology_bindings": row.get("topology_bindings", "-"),
                "top_neighbors": row.get("top_neighbors", "-"),
            }
        )
    out_rows.sort(key=lambda item: float(item["bridge_score"]), reverse=True)
    _write_csv(ROOT / args.out_csv, out_rows)
    _write_md(ROOT / args.out_md, out_rows)
    print({"families": len(out_rows), "top": out_rows[0]["family"] if out_rows else "-", "out": args.out_md})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
