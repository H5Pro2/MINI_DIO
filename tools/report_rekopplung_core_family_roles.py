from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

VECTOR_KEYS = [
    "sehen_form_salience",
    "sehen_memory_recall",
    "hoeren_stimulation",
    "kontakt_druck",
    "feldaufnahme_druck",
    "mcm_kohaerenz",
    "mcm_spannung",
    "mcm_asymmetrie",
    "feldsignatur",
]


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _float(value: object) -> float:
    try:
        out = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if out != out else out


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _vector(record: dict) -> list[float]:
    values = list(record.get("vector", []) or [])
    values = [_float(value) for value in values[: len(VECTOR_KEYS)]]
    while len(values) < len(VECTOR_KEYS):
        values.append(0.0)
    return values


def _observation_profile(record: dict) -> str:
    observations = dict(record.get("observations", {}) or {})
    counts = {
        key: int((dict(value or {})).get("count", 0) or 0)
        for key, value in observations.items()
    }
    if not counts:
        return "-"
    return ";".join(f"{key}:{value}" for key, value in sorted(counts.items()))


def _dominant_axes(vector: list[float], limit: int = 4) -> str:
    ranked = sorted(
        ((VECTOR_KEYS[index], abs(value), value) for index, value in enumerate(vector)),
        key=lambda item: item[1],
        reverse=True,
    )
    return ";".join(f"{key}:{value:.4f}" for key, _, value in ranked[:limit])


def _role_reading(vector: list[float]) -> str:
    ranked = sorted(
        ((VECTOR_KEYS[index], abs(value), value) for index, value in enumerate(vector)),
        key=lambda item: item[1],
        reverse=True,
    )
    top = [item[0] for item in ranked[:3]]
    if "hoeren_stimulation" in top and "mcm_kohaerenz" in top:
        return "hoeren_kohaerenz_getragen"
    if "sehen_form_salience" in top and "mcm_kohaerenz" in top:
        return "sehen_kohaerenz_getragen"
    if "feldaufnahme_druck" in top or "mcm_spannung" in top:
        return "feldaufnahme_spannungsnah"
    if "sehen_memory_recall" in top:
        return "erinnerungsnah"
    return "gemischte_feldrolle"


def _field_profile(data: dict) -> str:
    maps = list(data.get("passive_inner_field_maps", []) or [])
    counter: Counter[str] = Counter()
    total = 0
    for field_map in maps:
        profile = dict(field_map.get("profile", {}) or {})
        for state, payload in profile.items():
            count = int(dict(payload or {}).get("count", 0) or 0)
            counter[state] += count
            total += count
    if not total:
        return "-"
    return ";".join(
        f"{state}:{count / total:.4f}" for state, count in counter.most_common()
    )


def _rows_for_memory(label: str, source: str, path: Path, families: list[str]) -> list[dict[str, object]]:
    data = _read_json(path)
    family_records = dict(data.get("families", {}) or {})
    symbols = dict(data.get("symbols", {}) or {})
    field_profile = _field_profile(data)
    rows: list[dict[str, object]] = []
    for family in families:
        record = dict(family_records.get(family, {}) or {})
        symbol_count = sum(
            1 for payload in symbols.values()
            if dict(payload or {}).get("syntax_family") == family
        )
        vector = _vector(record)
        rows.append(
            {
                "label": label,
                "source": source,
                "family": family,
                "present": 1 if record else 0,
                "count": int(record.get("count", 0) or 0),
                "symbol_count": symbol_count,
                "role_reading": _role_reading(vector) if record else "nicht_aktiv",
                "dominant_axes": _dominant_axes(vector) if record else "-",
                "observation_profile": _observation_profile(record) if record else "-",
                "field_profile": field_profile,
                **{
                    key: round(vector[index], 6)
                    for index, key in enumerate(VECTOR_KEYS)
                },
            }
        )
    return rows


def _summary(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["source"]), str(row["family"]))].append(row)
    out: list[dict[str, object]] = []
    for (source, family), items in sorted(grouped.items()):
        active = [row for row in items if int(row["present"]) == 1]
        role_counts = Counter(str(row["role_reading"]) for row in active)
        vectors_by_key = {
            key: [_float(row.get(key)) for row in active]
            for key in VECTOR_KEYS
        }
        avg_vector = [_mean(vectors_by_key[key]) for key in VECTOR_KEYS]
        out.append(
            {
                "source": source,
                "family": family,
                "active_windows": len(active),
                "total_count": sum(int(row["count"]) for row in active),
                "avg_symbol_count": round(_mean([float(row["symbol_count"]) for row in active]), 4),
                "role_profile": ";".join(f"{role}:{count}" for role, count in role_counts.most_common()) or "-",
                "dominant_axes": _dominant_axes(avg_vector) if active else "-",
                **{
                    f"avg_{key}": round(_mean(vectors_by_key[key]), 6)
                    for key in VECTOR_KEYS
                },
            }
        )
    return out


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, object]], summary: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# 1790 - Rekoppelnde Kernfamilien: Feldrollen",
        "",
        "## Grundfrage",
        "",
        "Nach 1789 war offen, ob die häufigen Kernfamilien nur Sammelfamilien sind oder unterschiedliche Feldrollen tragen.",
        "",
        "Die Prüfung bleibt passiv. Sie liest Memory-Dateien und verändert keine Laufmechanik.",
        "",
        "## Quellen",
        "",
        "- reale BTC-2025-Rekopplungsfenster",
        "- reale PAXG-2025-Rekopplungsfenster",
        "- synthetische 1787-/1788-Nachhallwelten",
        "",
        "## Zusammenfassung",
        "",
        "| Quelle | Familie | aktive Fenster | Count | Rollenprofil | Dominante Achsen |",
        "|---|---|---:|---:|---|---|",
    ]
    for row in summary:
        lines.append(
            f"| {row['source']} | `{row['family']}` | {row['active_windows']} | "
            f"{row['total_count']} | `{row['role_profile']}` | `{row['dominant_axes']}` |"
        )
    lines.extend(
        [
            "",
            "## Einzelfenster",
            "",
            "| Label | Quelle | Familie | Count | Rolle | Dominante Achsen | Feldprofil |",
            "|---|---|---|---:|---|---|---|",
        ]
    )
    for row in rows:
        if int(row["present"]) == 0:
            continue
        lines.append(
            f"| {row['label']} | {row['source']} | `{row['family']}` | {row['count']} | "
            f"`{row['role_reading']}` | `{row['dominant_axes']}` | `{row['field_profile']}` |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die realen Kernfamilien sind nicht bloß häufig. Sie tragen unterschiedliche Achsenmischungen:",
            "",
            "- `dio_104t` erscheint in BTC und PAXG als stark wiederkehrende Kohaerenz-/Hör-/Feldfamilie.",
            "- `dio_0l7p`, `dio_155c` und `dio_0m9z` erscheinen vor allem in realen rekoppelnden Fenstern, kaum in den synthetischen Kompaktwelten.",
            "- `dio_14wj` ist besonders PAXG-nah und trägt dort eine ruhige rekoppelnde Familienbreite.",
            "- `dio_1fll` ist synthetisch dominant, aber auch in PAXG sichtbar. Der Unterschied liegt nicht im Namen allein, sondern im Gesamtfamilienraum: synthetisch kollabiert diese Dominanz auf wenige Familien, real bleibt sie in ein breiteres Feld eingebettet.",
            "",
            "Damit verdichtet sich die Trennung:",
            "",
            "```text",
            "reale Rekopplung:",
            "  Kernfamilien + viele Nachbarfamilien + kleine Nebenunruhe",
            "",
            "synthetische Bindung:",
            "  wenige dominante Familien + vollständig stabiles Feldprofil",
            "```",
            "",
            "## Grenze",
            "",
            "Die Rollenlesung ist diagnostisch. Sie beweist keine bewusste Entscheidung des Feldes. Sie zeigt aber, dass dieselben `dio_*`-Bezeichnungen nicht isoliert gelesen werden dürfen. Bedeutung entsteht aus Familie, Nachbarschaft, Feldprofil und Weltphase.",
            "",
            "## Artefakte",
            "",
            "- `reports/rekopplung_core_family_roles.csv`",
            "- `reports/rekopplung_core_family_roles_summary.csv`",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte ein einzelner Kernfamilien-Kandidat isoliert werden: `dio_104t` als mögliche Zentrum-/Kohaerenzfamilie oder `dio_14wj` als PAXG-nahe Rekopplungsfamilie.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-csv", default="reports/rekopplung_core_family_roles.csv")
    parser.add_argument("--out-summary", default="reports/rekopplung_core_family_roles_summary.csv")
    parser.add_argument("--out-md", default="docs/befunde/1001-2000/1751-2000/1790_REKOPPELNDE_KERNFAMILIEN_FELDROLLEN.md")
    args = parser.parse_args()

    families = ["dio_104t", "dio_0l7p", "dio_155c", "dio_0m9z", "dio_14wj", "dio_1fll"]
    memories = [
        ("BTC_2025_1H_CORE_2000_3000", "real_btc", "memory/multiworld_axis_map/BTC_2025_1H_CORE_2000_3000/memory_B_real_run_after_sleep.json"),
        ("BTC_2025_15M_ZONE_9000_10000", "real_btc", "memory/multiworld_axis_map/BTC_2025_15M_ZONE_9000_10000/memory_B_real_run_after_sleep.json"),
        ("BTC_2025_30M_SHIFT_8000_9000", "real_btc", "memory/multiworld_axis_map/BTC_2025_30M_SHIFT_8000_9000/memory_B_real_run_after_sleep.json"),
        ("PAXG_2025_FOLLOW_1000_2000", "real_paxg", "memory/multiworld_axis_map/PAXG_2025_FOLLOW_1000_2000/memory_B_real_run_after_sleep.json"),
        ("PAXG_2025_FOLLOW_2000_3000", "real_paxg", "memory/multiworld_axis_map/PAXG_2025_FOLLOW_2000_3000/memory_B_real_run_after_sleep.json"),
        ("PAXG_2025_FOLLOW_3000_4000", "real_paxg", "memory/multiworld_axis_map/PAXG_2025_FOLLOW_3000_4000/memory_B_real_run_after_sleep.json"),
        ("SYN1787_BASE_TO_FOLLOW", "synthetisch", "memory/multiworld_axis_map/SYN1787_BASE_TO_FOLLOW/memory_B_real_run_after_sleep.json"),
        ("SYN1788_BASE_TO_FOLLOW", "synthetisch", "memory/multiworld_axis_map/SYN1788_BASE_TO_FOLLOW/memory_B_real_run_after_sleep.json"),
    ]
    rows: list[dict[str, object]] = []
    for label, source, rel_path in memories:
        rows.extend(_rows_for_memory(label, source, ROOT / rel_path, families))
    summary = _summary(rows)
    _write_csv(ROOT / args.out_csv, rows)
    _write_csv(ROOT / args.out_summary, summary)
    _write_md(ROOT / args.out_md, rows, summary)
    print({"rows": len(rows), "summary": len(summary), "out": args.out_md})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
