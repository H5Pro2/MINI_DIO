from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DEFAULT_SOURCES = [
    "reports/dio_104t_neighbor_role_differentiation.csv",
    "reports/dio_0l7p_neighbor_role_differentiation.csv",
    "reports/dio_155c_neighbor_role_differentiation.csv",
    "reports/dio_0m9z_neighbor_role_differentiation.csv",
    "reports/dio_14wj_neighbor_role_differentiation.csv",
    "reports/dio_1fll_neighbor_role_differentiation.csv",
]


def _float(value: object) -> float:
    try:
        out = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if out != out else out


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


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


def _topology_binding(role: str) -> str:
    if role == "zielnahe_mitrolle":
        return "bruecke_zielnah"
    if role == "kohaerenz_hoeher":
        return "zentrum_stabilisierend"
    if role in {"asymmetrie_plus", "asymmetrie_minus"}:
        return "rand_polarisierend"
    if role == "hoeren_staerker":
        return "nachhall_aktivierend"
    if role == "hoeren_leiser":
        return "nachhall_daempfend"
    if role == "sehen_schaerfer":
        return "sehen_formbindend"
    if role == "feldkontakt_drucknah":
        return "feldkontakt_spannungsnah"
    return "gemischte_uebergangsrolle"


def _counter_text(counter: Counter[str], limit: int = 8) -> str:
    return ";".join(f"{key}:{value}" for key, value in counter.most_common(limit)) or "-"


def _top_rows(rows: list[dict[str, str]], limit: int = 5) -> str:
    ranked = sorted(
        rows,
        key=lambda row: (
            int(_float(row.get("co_memory_count"))),
            int(_float(row.get("neighbor_count_sum"))),
        ),
        reverse=True,
    )
    return ";".join(f"{row.get('neighbor_family')}:{row.get('role_reading')}" for row in ranked[:limit]) or "-"


def _summarize_family(path: Path) -> dict[str, object]:
    rows = _read_csv(path)
    family = str(rows[0].get("target_family") if rows else path.stem.split("_neighbor", 1)[0])
    role_counts = Counter(str(row.get("role_reading") or "-") for row in rows)
    topology_counts = Counter(_topology_binding(str(row.get("role_reading") or "-")) for row in rows)
    major_axis_counts = Counter(str(row.get("major_delta_axis") or "-") for row in rows)
    return {
        "family": family,
        "neighbor_rows": len(rows),
        "avg_co_memory_count": round(_mean([_float(row.get("co_memory_count")) for row in rows]), 4),
        "avg_cosine": round(_mean([_float(row.get("avg_cosine")) for row in rows]), 6),
        "avg_distance": round(_mean([_float(row.get("avg_distance")) for row in rows]), 6),
        "roles": _counter_text(role_counts),
        "topology_bindings": _counter_text(topology_counts),
        "major_delta_axes": _counter_text(major_axis_counts),
        "top_neighbors": _top_rows(rows),
        "source": str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path),
    }


def _write_md(path: Path, rows: list[dict[str, object]]) -> None:
    lines = [
        "# 1797 - Kernfamilien im Teilnetz-Vergleich",
        "",
        "## Grundfrage",
        "",
        "Nach 1796 ist offen, ob `dio_104t` eine besondere Anschlussrolle trägt oder ob ähnliche Teilnetz-Rollen auch bei anderen Kernfamilien entstehen.",
        "",
        "Die Prüfung liest vorhandene Nachbarrollen-Diagnosen passiv und vergleicht Rollenverteilung, Topologiebindung und Achsenabweichungen.",
        "",
        "## Vergleich",
        "",
        "| Familie | Nachbarn | Cosinus | Abstand | Rollenprofil | Topologiebindung | Hauptachsen | Stärkste Nachbarn |",
        "|---|---:|---:|---:|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['family']}` | {row['neighbor_rows']} | {row['avg_cosine']} | {row['avg_distance']} | "
            f"`{row['roles']}` | `{row['topology_bindings']}` | `{row['major_delta_axes']}` | `{row['top_neighbors']}` |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "- Mehrere Kernfamilien bilden Teilnetz-Rollen, nicht nur `dio_104t`.",
            "- Die Rollen entstehen aber nicht identisch: manche Familien tragen stärker Randpolarisierung, andere eher Kohärenzstabilisierung, Hören/Nachhall oder Formbindung.",
            "- `dio_104t` bleibt damit nicht einzigartig als einziges strukturiertes Feld, aber es bleibt ein starker Anschlussknoten, weil seine Nachbarschaft sehr breit und zugleich rollendifferenziert ist.",
            "",
            "## Vorsicht",
            "",
            "Das ist weiterhin eine passive Strukturdiagnose. Die Auswertung beschreibt Nachbarschaftsordnung im gespeicherten Feld, nicht Handlung, Richtung oder Strategie.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sources", nargs="*", default=DEFAULT_SOURCES)
    parser.add_argument("--out-csv", default="reports/core_family_role_comparison.csv")
    parser.add_argument("--out-md", default="docs/befunde/1001-2000/1751-2000/1797_KERNFAMILIEN_TEILNETZ_VERGLEICH.md")
    args = parser.parse_args()

    rows = [_summarize_family(ROOT / source) for source in args.sources if (ROOT / source).exists()]
    rows.sort(key=lambda row: (float(row["avg_co_memory_count"]), float(row["avg_cosine"])), reverse=True)
    _write_csv(ROOT / args.out_csv, rows)
    _write_md(ROOT / args.out_md, rows)
    print({"families": len(rows), "out": args.out_md})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
