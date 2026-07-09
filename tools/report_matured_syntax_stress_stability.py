from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = ROOT / "docs" / "befunde"


def _load_csv(path: Path) -> list[dict[str, str]]:
    path = path if path.is_absolute() else ROOT / path
    if not path.exists() or path.stat().st_size <= 0:
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _safe_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _fmt(value: float) -> str:
    return f"{value:.3f}"


def _index(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {str(row.get("symbol_family", "-")): row for row in rows if row.get("symbol_family")}


def _stress_status(matured: dict[str, str], stress: dict[str, str] | None) -> str:
    if not stress:
        return "stress_nicht_wiedergefunden"
    same_field = matured.get("follow_field") == stress.get("dominant_field_contact_class")
    reifung = str(stress.get("syntax_reifung", "-"))
    events = _safe_int(stress.get("events"))
    if same_field and reifung == "weltuebergreifend_feldstabil":
        return "stress_stabil_weltuebergreifend"
    if same_field and reifung == "lokal_feldstabil":
        return "stress_stabil_lokal"
    if same_field and events >= 50:
        return "stress_feldnah"
    if events >= 50:
        return "stress_verschoben"
    return "stress_jung_wiedergefunden"


def _build_rows(matured_rows: list[dict[str, str]], stress_rows: list[dict[str, str]]) -> list[dict[str, object]]:
    stress_index = _index(stress_rows)
    rows: list[dict[str, object]] = []
    for row in matured_rows:
        family = str(row.get("symbol_family", "-"))
        stress = stress_index.get(family)
        status = _stress_status(row, stress)
        rows.append(
            {
                "symbol_family": family,
                "matured_trace_class": row.get("matured_trace_class", "-"),
                "origin_present_in": row.get("origin_present_in", "-"),
                "origin_field": row.get("origin_field", "-"),
                "follow_field": row.get("follow_field", "-"),
                "follow_reifung": row.get("follow_reifung", "-"),
                "follow_events": _safe_int(row.get("follow_events")),
                "stress_status": status,
                "stress_events": _safe_int((stress or {}).get("events")),
                "stress_labels": (stress or {}).get("holdout_labels", "-"),
                "stress_field": (stress or {}).get("dominant_field_contact_class", "-"),
                "stress_reifung": (stress or {}).get("syntax_reifung", "-"),
                "stress_field_share": _fmt(_safe_float((stress or {}).get("dominant_field_share"))),
                "stress_mcm": (
                    f"{_fmt(_safe_float((stress or {}).get('avg_carry')))}/"
                    f"{_fmt(_safe_float((stress or {}).get('avg_strain')))}/"
                    f"{_fmt(_safe_float((stress or {}).get('avg_rekopplung')))}"
                    if stress
                    else "-"
                ),
                "boundary": "passive_stress_stability_trace_no_action_no_direction",
                "passive_only": 1,
                "influences_action": 0,
                "is_gate": 0,
                "is_motoric": 0,
                "is_entry_signal": 0,
                "is_direction_signal": 0,
            }
        )
    order = {
        "stress_stabil_weltuebergreifend": 0,
        "stress_stabil_lokal": 1,
        "stress_feldnah": 2,
        "stress_verschoben": 3,
        "stress_jung_wiedergefunden": 4,
        "stress_nicht_wiedergefunden": 5,
    }
    return sorted(rows, key=lambda item: (order.get(str(item["stress_status"]), 9), -int(item["stress_events"]), str(item["symbol_family"])))


def _summary(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    buckets: dict[str, list[dict[str, object]]] = {}
    for row in rows:
        buckets.setdefault(str(row.get("stress_status", "-")), []).append(row)
    summary: list[dict[str, object]] = []
    for status, bucket in sorted(buckets.items()):
        fields = Counter(str(row.get("stress_field", "-")) for row in bucket)
        origins = Counter(str(row.get("matured_trace_class", "-")) for row in bucket)
        summary.append(
            {
                "stress_status": status,
                "families": len(bucket),
                "matured_trace_classes": ";".join(f"{key}:{value}" for key, value in origins.most_common()),
                "stress_fields": ";".join(f"{key}:{value}" for key, value in fields.most_common()),
                "max_stress_events": max(_safe_int(row.get("stress_events")) for row in bucket),
            }
        )
    return summary


def _write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def _md_table(rows: list[dict[str, object]], fields: list[str], limit: int = 25) -> list[str]:
    lines = ["| " + " | ".join(fields) + " |", "| " + " | ".join("---" for _ in fields) + " |"]
    for row in rows[:limit]:
        lines.append("| " + " | ".join(str(row.get(field, "")) for field in fields) + " |")
    return lines


def _write_markdown(path: Path, rows: list[dict[str, object]], summary: list[dict[str, object]]) -> None:
    counts = Counter(str(row.get("stress_status", "-")) for row in rows)
    stable = counts.get("stress_stabil_weltuebergreifend", 0) + counts.get("stress_stabil_lokal", 0)
    fieldnear = stable + counts.get("stress_feldnah", 0)
    lines = [
        "# 2054 - Stressstabilität nachgereifter Syntaxspuren",
        "",
        "## Zweck",
        "",
        "Diese Auswertung prüft die 72 passiv nachgereiften Syntaxspuren aus 2052 gegen mehrere Stresswelten aus 2053.",
        "",
        "Die Prüfung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung, kein Gate und keinen motorischen Impuls.",
        "",
        "## Grundfrage",
        "",
        "Bleiben nachgereifte Bedeutungsinseln unter Stress feldnah, verschieben sie ihre Feldrolle, oder verschwinden sie wieder?",
        "",
        "## Übersicht",
        "",
        f"- geprüfte nachgereifte Familien: `{len(rows)}`",
        f"- feldstabil unter Stress: `{stable}`",
        f"- feldnah inklusive stabil: `{fieldnear}`",
        f"- Statusverteilung: `{dict(sorted(counts.items()))}`",
        "",
        "## Statusklassen",
        "",
    ]
    lines.extend(_md_table(summary, ["stress_status", "families", "matured_trace_classes", "stress_fields", "max_stress_events"], limit=20))
    lines.extend(["", "## Stärkste Stress-Wiederfunde", ""])
    lines.extend(
        _md_table(
            rows,
            [
                "symbol_family",
                "matured_trace_class",
                "stress_status",
                "follow_field",
                "stress_events",
                "stress_labels",
                "stress_field",
                "stress_reifung",
                "stress_mcm",
            ],
            limit=35,
        )
    )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- Eine feldnahe Wiederfindung unter Stress ist ein stärkerer passiver Robustheitskandidat.",
            "- Eine Verschiebung unter Stress ist kein Fehler, sondern Hinweis auf Belastungsdrift.",
            "- Ein Nicht-Wiederfinden heißt nicht, dass die Spur falsch war. Es heißt nur, dass sie in diesen Stresswelten nicht sichtbar getragen wurde.",
            "- Die Auswertung ist bewusst keine Strategie- oder Handlungslogik.",
            "",
            "## Bedeutung für MINI_DIO",
            "",
            "Die Prüfung trennt situative Reifung von belastbarer Reifung. Dadurch kann MINI_DIO später Feldgedächtnis nicht nur nach Häufigkeit, sondern nach Tragfähigkeit über Weltspannung hinweg betrachten.",
            "",
            "Wie es weitergeht: Als nächstes sollten die feldnahen Stress-Wiederfunde mit ruhigen Welten gegengeprüft werden. Entscheidend ist, ob dieselben Spuren nur unter Stress aktiv werden oder auch in ruhiger Welt als stabile Bedeutung erhalten bleiben.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--matured", default="docs/befunde/2052_PASSIVE_REIFESPUR_NACHGEREIFTER_SYNTAXINSELN.families.csv")
    parser.add_argument("--stress-bridge", default="docs/befunde/2053_STRESSWELTEN_FELDKLASSEN_ZU_SYNTAXNAEHE.bridge.csv")
    parser.add_argument("--out-prefix", default="2054_NACHGEREIFTE_SYNTAX_STRESS_STABILITAET")
    args = parser.parse_args()

    matured_rows = _load_csv(Path(args.matured))
    stress_rows = _load_csv(Path(args.stress_bridge))
    rows = _build_rows(matured_rows, stress_rows)
    summary = _summary(rows)

    detail_fields = [
        "symbol_family",
        "matured_trace_class",
        "origin_present_in",
        "origin_field",
        "follow_field",
        "follow_reifung",
        "follow_events",
        "stress_status",
        "stress_events",
        "stress_labels",
        "stress_field",
        "stress_reifung",
        "stress_field_share",
        "stress_mcm",
        "boundary",
        "passive_only",
        "influences_action",
        "is_gate",
        "is_motoric",
        "is_entry_signal",
        "is_direction_signal",
    ]
    summary_fields = ["stress_status", "families", "matured_trace_classes", "stress_fields", "max_stress_events"]

    _write_csv(BEFUNDE / f"{args.out_prefix}.detail.csv", rows, detail_fields)
    _write_csv(BEFUNDE / f"{args.out_prefix}.summary.csv", summary, summary_fields)
    _write_markdown(BEFUNDE / f"{args.out_prefix}.md", rows, summary)

    print(f"matured_families={len(matured_rows)}")
    print(f"stress_families={len(stress_rows)}")
    print(f"checked={len(rows)}")
    print(f"wrote={BEFUNDE / (args.out_prefix + '.md')}")


if __name__ == "__main__":
    main()
