from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DELTA_KEYS = [
    "delta_mcm_kohaerenz",
    "delta_hoeren_stimulation",
    "delta_sehen_form_salience",
    "delta_mcm_asymmetrie",
    "delta_feldaufnahme_druck",
    "delta_mcm_spannung",
    "delta_kontakt_druck",
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


def _topology_binding(role: str, deltas: dict[str, float], avg_distance: float, avg_cosine: float) -> str:
    if role == "zielnahe_mitrolle" or (avg_distance <= 0.11 and avg_cosine >= 0.99):
        return "bruecke_zielnah"
    if deltas["delta_mcm_kohaerenz"] >= 0.09 and abs(deltas["delta_mcm_asymmetrie"]) < 0.10:
        return "zentrum_stabilisierend"
    if abs(deltas["delta_mcm_asymmetrie"]) >= 0.10:
        return "rand_polarisierend"
    if deltas["delta_hoeren_stimulation"] >= 0.08:
        return "nachhall_aktivierend"
    if deltas["delta_hoeren_stimulation"] <= -0.08:
        return "nachhall_daempfend"
    if deltas["delta_sehen_form_salience"] >= 0.08:
        return "sehen_formbindend"
    if deltas["delta_feldaufnahme_druck"] >= 0.06 or deltas["delta_mcm_spannung"] >= 0.06:
        return "feldkontakt_spannungsnah"
    return "gemischte_uebergangsrolle"


def _counter_text(counter: Counter[str]) -> str:
    return ";".join(f"{key}:{value}" for key, value in counter.most_common()) or "-"


def _top_families(rows: list[dict[str, str]], limit: int = 8) -> str:
    ranked = sorted(
        rows,
        key=lambda row: (
            int(_float(row.get("co_memory_count"))),
            int(_float(row.get("neighbor_count_sum"))),
        ),
        reverse=True,
    )
    return ";".join(str(row.get("neighbor_family", "-")) for row in ranked[:limit]) or "-"


def _write_md(path: Path, source_csv: str, rows: list[dict[str, object]]) -> None:
    lines = [
        "# 1796 - `dio_104t` Teilnetz-Rollen und Topologiebindung",
        "",
        "## Grundfrage",
        "",
        "Die Prüfung liest die in 1795 gefundenen Nachbarrollen als Teilnetze.",
        "",
        "Ziel ist nicht, neue Topologie zu erzwingen, sondern die vorhandenen Achsenabweichungen vorsichtig auf Zentrum, Brücke, Rand und Nachhall zu beziehen.",
        "",
        f"Quelle: `{source_csv}`",
        "",
        "## Rollenkarte",
        "",
        "| Rollenklasse | Familien | Memories | Cosinus | Abstand | Topologie-Lesung | Delta-Profil | Stärkste Familien |",
        "|---|---:|---:|---:|---:|---|---|---|",
    ]
    for row in rows:
        delta_profile = (
            f"kohaerenz:{row['avg_delta_mcm_kohaerenz']}; "
            f"hoeren:{row['avg_delta_hoeren_stimulation']}; "
            f"sehen:{row['avg_delta_sehen_form_salience']}; "
            f"asym:{row['avg_delta_mcm_asymmetrie']}; "
            f"feld:{row['avg_delta_feldaufnahme_druck']}"
        )
        lines.append(
            f"| `{row['role_reading']}` | {row['family_count']} | {row['avg_co_memory_count']} | "
            f"{row['avg_cosine']} | {row['avg_distance']} | `{row['topology_binding']}` | "
            f"`{delta_profile}` | `{row['top_families']}` |"
        )
    binding_counts = Counter(str(row["topology_binding"]) for row in rows)
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"- Topologie-Lesungen: `{_counter_text(binding_counts)}`",
            "- Die `dio_104t`-Nachbarschaft zeigt eine innere Staffelung: zielnahe Mitrollen, stabilisierende Kohärenzrollen, polarisierende Randrollen, Sehen-/Hören-Varianten und Übergangsrollen.",
            "- Damit wird das Feldnetz nicht als eine einzelne Fläche gelesen, sondern als mehrere Teilnetze um denselben Anschlussknoten.",
            "",
            "## Vorsicht",
            "",
            "Diese Lesung ist eine passive Diagnose aus vorhandenen Achsenwerten. Sie ist kein Gate, keine Handlung und keine fest programmierte Topologie.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte geprüft werden, ob diese Teilnetz-Lesungen in weiteren Kernfamilien ähnlich entstehen oder ob `dio_104t` eine besondere Anschlussrolle trägt.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="reports/dio_104t_neighbor_role_differentiation.csv")
    parser.add_argument("--out-csv", default="reports/dio_104t_role_topology_binding.csv")
    parser.add_argument("--out-md", default="docs/befunde/1001-2000/1751-2000/1796_DIO_104T_TEILNETZ_TOPOLOGIEBINDUNG.md")
    args = parser.parse_args()

    source = ROOT / args.source
    rows = _read_csv(source)
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get("role_reading") or "-")].append(row)

    out_rows: list[dict[str, object]] = []
    for role, items in sorted(grouped.items()):
        deltas = {key: _mean([_float(row.get(key)) for row in items]) for key in DELTA_KEYS}
        avg_distance = _mean([_float(row.get("avg_distance")) for row in items])
        avg_cosine = _mean([_float(row.get("avg_cosine")) for row in items])
        out_rows.append(
            {
                "role_reading": role,
                "family_count": len(items),
                "avg_co_memory_count": round(_mean([_float(row.get("co_memory_count")) for row in items]), 4),
                "avg_neighbor_count_sum": round(_mean([_float(row.get("neighbor_count_sum")) for row in items]), 4),
                "avg_cosine": round(avg_cosine, 6),
                "avg_distance": round(avg_distance, 6),
                "topology_binding": _topology_binding(role, deltas, avg_distance, avg_cosine),
                "top_families": _top_families(items),
                **{f"avg_{key}": round(value, 6) for key, value in deltas.items()},
            }
        )
    out_rows.sort(key=lambda row: (int(row["family_count"]), float(row["avg_co_memory_count"])), reverse=True)

    out_csv = ROOT / args.out_csv
    out_md = ROOT / args.out_md
    _write_csv(out_csv, out_rows)
    _write_md(out_md, args.source, out_rows)
    print({"roles": len(out_rows), "out": str(out_md.relative_to(ROOT))})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
