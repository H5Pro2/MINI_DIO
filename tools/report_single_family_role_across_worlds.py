from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

from befunde_paths import befunde_root


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = befunde_root(ROOT)


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


def _field_consistency(rows: list[dict[str, str]]) -> str:
    if not rows:
        return "nicht_wiedergefunden"
    fields = Counter(str(row.get("field_contact_class", "-")) for row in rows)
    dominant, count = fields.most_common(1)[0]
    share = count / max(1, len(rows))
    labels = {str(row.get("holdout_label", "-")) for row in rows}
    if len(labels) >= 3 and share >= 0.80:
        return "weltuebergreifende_grundrolle"
    if len(labels) >= 2 and share >= 0.80:
        return "weltuebergreifend_feldnah"
    if share >= 0.80:
        return "lokal_feldnah"
    return "feldverschoben"


def _build_report_rows(family: str, family_rows: list[dict[str, str]], bridge_rows: list[dict[str, str]]) -> tuple[list[dict[str, object]], dict[str, object]]:
    rows = [row for row in family_rows if row.get("symbol_family") == family]
    bridge = next((row for row in bridge_rows if row.get("symbol_family") == family), None)
    detail: list[dict[str, object]] = []
    for row in sorted(rows, key=lambda item: (str(item.get("holdout_label", "-")), str(item.get("field_contact_class", "-")))):
        detail.append(
            {
                "symbol_family": family,
                "holdout_label": row.get("holdout_label", "-"),
                "field_contact_class": row.get("field_contact_class", "-"),
                "events": _safe_int(row.get("events")),
                "distinct_symbols": _safe_int(row.get("distinct_symbols")),
                "top_symbols": row.get("top_symbols", "-"),
                "avg_carry": _fmt(_safe_float(row.get("avg_carry"))),
                "avg_strain": _fmt(_safe_float(row.get("avg_strain"))),
                "avg_rekopplung": _fmt(_safe_float(row.get("avg_rekopplung"))),
                "boundary": "single_family_passive_role_trace_no_action_no_direction",
            }
        )
    fields = Counter(str(row.get("field_contact_class", "-")) for row in rows)
    labels = Counter(str(row.get("holdout_label", "-")) for row in rows)
    summary: dict[str, object] = {
        "symbol_family": family,
        "role_status": _field_consistency(rows),
        "worlds": len(labels),
        "family_field_rows": len(rows),
        "total_events": sum(_safe_int(row.get("events")) for row in rows),
        "fields": ";".join(f"{key}:{value}" for key, value in fields.most_common()) or "-",
        "labels": ";".join(f"{key}:{value}" for key, value in labels.most_common()) or "-",
        "bridge_events": _safe_int((bridge or {}).get("events")),
        "bridge_field": (bridge or {}).get("dominant_field_contact_class", "-"),
        "bridge_reifung": (bridge or {}).get("syntax_reifung", "-"),
        "bridge_share": _fmt(_safe_float((bridge or {}).get("dominant_field_share"))),
        "bridge_mcm": (
            f"{_fmt(_safe_float((bridge or {}).get('avg_carry')))}/"
            f"{_fmt(_safe_float((bridge or {}).get('avg_strain')))}/"
            f"{_fmt(_safe_float((bridge or {}).get('avg_rekopplung')))}"
            if bridge
            else "-"
        ),
    }
    return detail, summary


def _write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def _md_table(rows: list[dict[str, object]], fields: list[str]) -> list[str]:
    lines = ["| " + " | ".join(fields) + " |", "| " + " | ".join("---" for _ in fields) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(field, "")) for field in fields) + " |")
    return lines


def _write_markdown(path: Path, detail: list[dict[str, object]], summary: dict[str, object]) -> None:
    lines = [
        f"# Einzelrolle {summary['symbol_family']} über geprüfte Welten",
        "",
        "## Zweck",
        "",
        "Diese Auswertung isoliert eine einzelne Syntaxfamilie, die zuvor unter Stress und in ruhiger Gegenprüfung stabil wirkte.",
        "",
        "Die Prüfung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung, kein Gate und keinen motorischen Impuls.",
        "",
        "## Übersicht",
        "",
        f"- Syntaxfamilie: `{summary['symbol_family']}`",
        f"- Rollenstatus: `{summary['role_status']}`",
        f"- Welten mit Wiederfund: `{summary['worlds']}`",
        f"- Feldzeilen: `{summary['family_field_rows']}`",
        f"- Ereignisse: `{summary['total_events']}`",
        f"- Feldrollen: `{summary['fields']}`",
        f"- Brückenreife: `{summary['bridge_reifung']}`",
        f"- Brücken-MCM Carry/Strain/Rekopplung: `{summary['bridge_mcm']}`",
        "",
        "## Detail nach Welt",
        "",
    ]
    lines.extend(
        _md_table(
            detail,
            [
                "holdout_label",
                "field_contact_class",
                "events",
                "distinct_symbols",
                "avg_carry",
                "avg_strain",
                "avg_rekopplung",
            ],
        )
    )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Wenn dieselbe Syntaxfamilie in mehreren Assets mit gleicher Feldrolle wieder auftaucht, ist sie ein stärkerer Kandidat für eine passive Grundrolle. Wenn sie nur in einzelnen Welten erscheint, bleibt sie eine situative Rolle.",
            "",
            "Diese Auswertung bewertet keine Richtung und keine Handlung. Sie prüft nur, ob eine wiederkehrende Feldbedeutung assetübergreifend getragen wird.",
            "",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--family", default="dio_17j2")
    parser.add_argument("--families", default="docs/befunde/2001-3000/2057_MULTI_ASSET_FELDKLASSEN_ZU_SYNTAXNAEHE.families.csv")
    parser.add_argument("--bridge", default="docs/befunde/2001-3000/2057_MULTI_ASSET_FELDKLASSEN_ZU_SYNTAXNAEHE.bridge.csv")
    parser.add_argument("--out-prefix", default="2058_DIO17J2_EINZELROLLE_MULTI_ASSET")
    args = parser.parse_args()

    detail, summary = _build_report_rows(args.family, _load_csv(Path(args.families)), _load_csv(Path(args.bridge)))
    detail_fields = [
        "symbol_family",
        "holdout_label",
        "field_contact_class",
        "events",
        "distinct_symbols",
        "top_symbols",
        "avg_carry",
        "avg_strain",
        "avg_rekopplung",
        "boundary",
    ]
    summary_fields = [
        "symbol_family",
        "role_status",
        "worlds",
        "family_field_rows",
        "total_events",
        "fields",
        "labels",
        "bridge_events",
        "bridge_field",
        "bridge_reifung",
        "bridge_share",
        "bridge_mcm",
    ]
    _write_csv(BEFUNDE / f"{args.out_prefix}.detail.csv", detail, detail_fields)
    _write_csv(BEFUNDE / f"{args.out_prefix}.summary.csv", [summary], summary_fields)
    _write_markdown(BEFUNDE / f"{args.out_prefix}.md", detail, summary)
    print(f"family={args.family}")
    print(f"worlds={summary['worlds']}")
    print(f"events={summary['total_events']}")
    print(f"role_status={summary['role_status']}")
    print(f"wrote={BEFUNDE / (args.out_prefix + '.md')}")


if __name__ == "__main__":
    main()
