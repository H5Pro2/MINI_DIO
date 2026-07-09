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


def _quiet_status(stress_row: dict[str, str], quiet_row: dict[str, str] | None) -> str:
    if not quiet_row:
        return "quiet_nicht_wiedergefunden"
    same_field = stress_row.get("stress_field") == quiet_row.get("dominant_field_contact_class")
    reifung = str(quiet_row.get("syntax_reifung", "-"))
    events = _safe_int(quiet_row.get("events"))
    if same_field and reifung == "weltuebergreifend_feldstabil":
        return "allgemeine_feldrolle"
    if same_field and reifung == "lokal_feldstabil":
        return "ruhig_lokal_stabil"
    if same_field and events >= 50:
        return "ruhig_feldnah"
    if events >= 50:
        return "ruhig_verschoben"
    return "ruhig_jung_wiedergefunden"


def _build_rows(stress_rows: list[dict[str, str]], quiet_rows: list[dict[str, str]]) -> list[dict[str, object]]:
    quiet_index = _index(quiet_rows)
    candidates = [row for row in stress_rows if row.get("stress_status") == "stress_stabil_weltuebergreifend"]
    rows: list[dict[str, object]] = []
    for row in candidates:
        family = str(row.get("symbol_family", "-"))
        quiet = quiet_index.get(family)
        status = _quiet_status(row, quiet)
        rows.append(
            {
                "symbol_family": family,
                "matured_trace_class": row.get("matured_trace_class", "-"),
                "stress_field": row.get("stress_field", "-"),
                "stress_events": _safe_int(row.get("stress_events")),
                "stress_labels": row.get("stress_labels", "-"),
                "stress_mcm": row.get("stress_mcm", "-"),
                "quiet_status": status,
                "quiet_events": _safe_int((quiet or {}).get("events")),
                "quiet_labels": (quiet or {}).get("holdout_labels", "-"),
                "quiet_field": (quiet or {}).get("dominant_field_contact_class", "-"),
                "quiet_reifung": (quiet or {}).get("syntax_reifung", "-"),
                "quiet_field_share": _fmt(_safe_float((quiet or {}).get("dominant_field_share"))),
                "quiet_mcm": (
                    f"{_fmt(_safe_float((quiet or {}).get('avg_carry')))}/"
                    f"{_fmt(_safe_float((quiet or {}).get('avg_strain')))}/"
                    f"{_fmt(_safe_float((quiet or {}).get('avg_rekopplung')))}"
                    if quiet
                    else "-"
                ),
                "boundary": "passive_quiet_countercheck_no_action_no_direction",
                "passive_only": 1,
                "influences_action": 0,
                "is_gate": 0,
                "is_motoric": 0,
                "is_entry_signal": 0,
                "is_direction_signal": 0,
            }
        )
    order = {
        "allgemeine_feldrolle": 0,
        "ruhig_lokal_stabil": 1,
        "ruhig_feldnah": 2,
        "ruhig_verschoben": 3,
        "ruhig_jung_wiedergefunden": 4,
        "quiet_nicht_wiedergefunden": 5,
    }
    return sorted(rows, key=lambda item: (order.get(str(item["quiet_status"]), 9), -int(item["quiet_events"]), str(item["symbol_family"])))


def _summary(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    buckets: dict[str, list[dict[str, object]]] = {}
    for row in rows:
        buckets.setdefault(str(row.get("quiet_status", "-")), []).append(row)
    summary: list[dict[str, object]] = []
    for status, bucket in sorted(buckets.items()):
        fields = Counter(str(row.get("quiet_field", "-")) for row in bucket)
        summary.append(
            {
                "quiet_status": status,
                "families": len(bucket),
                "quiet_fields": ";".join(f"{key}:{value}" for key, value in fields.most_common()),
                "max_quiet_events": max(_safe_int(row.get("quiet_events")) for row in bucket),
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
    counts = Counter(str(row.get("quiet_status", "-")) for row in rows)
    lines = [
        "# 2056 - Ruhige Gegenprüfung stressstabiler Syntaxspuren",
        "",
        "## Zweck",
        "",
        "Diese Auswertung nimmt nur die unter Stress weltübergreifend stabilen Spuren aus 2054 und prüft sie gegen ruhige oder seitwärts laufende Welten aus 2055.",
        "",
        "Die Prüfung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung, kein Gate und keine motorische Kopplung.",
        "",
        "## Grundfrage",
        "",
        "Sind die stressstabilen Spuren allgemeine Feldrollen, oder werden sie hauptsächlich durch belastete Außenwelt aktiviert?",
        "",
        "## Übersicht",
        "",
        f"- geprüfte stressstabile Spuren: `{len(rows)}`",
        f"- Statusverteilung: `{dict(sorted(counts.items()))}`",
        "",
        "## Statusklassen",
        "",
    ]
    lines.extend(_md_table(summary, ["quiet_status", "families", "quiet_fields", "max_quiet_events"], limit=20))
    lines.extend(["", "## Detail", ""])
    lines.extend(
        _md_table(
            rows,
            [
                "symbol_family",
                "quiet_status",
                "stress_field",
                "stress_events",
                "quiet_events",
                "quiet_labels",
                "quiet_field",
                "quiet_reifung",
                "quiet_mcm",
            ],
            limit=20,
        )
    )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- Wenn eine Spur auch in ruhigen Welten feldnah bleibt, ist sie eher eine allgemeine Feldrolle.",
            "- Wenn sie in ruhigen Welten nicht wieder auftaucht, wirkt sie eher stressspezifisch.",
            "- Wenn sie ruhig verschoben wieder auftaucht, spricht das für eine Feldrolle, deren Bedeutung von Weltspannung moduliert wird.",
            "",
            "## Bedeutung für MINI_DIO",
            "",
            "Die Gegenprüfung verhindert, dass Stressrobustheit automatisch als allgemeine Reife gelesen wird. MINI_DIO kann damit später zwischen Grundrolle, Stressrolle und situativer Aktivierung unterscheiden.",
            "",
            "Wie es weitergeht: Als nächstes sollten wir die stressspezifischen und die allgemeinen Rollen getrennt gegen weitere Assets prüfen. Entscheidend ist, ob sich daraus eine Rollenkarte bildet, die Weltspannung, Ruhe und Drift sauber auseinanderhält.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stress-detail", default="docs/befunde/2054_NACHGEREIFTE_SYNTAX_STRESS_STABILITAET.detail.csv")
    parser.add_argument("--quiet-bridge", default="docs/befunde/2055_RUHIGE_WELTEN_FELDKLASSEN_ZU_SYNTAXNAEHE.bridge.csv")
    parser.add_argument("--out-prefix", default="2056_RUHIGE_GEGENPRUEFUNG_STRESSSTABILER_SYNTAXSPUREN")
    args = parser.parse_args()

    stress_rows = _load_csv(Path(args.stress_detail))
    quiet_rows = _load_csv(Path(args.quiet_bridge))
    rows = _build_rows(stress_rows, quiet_rows)
    summary = _summary(rows)

    detail_fields = [
        "symbol_family",
        "matured_trace_class",
        "stress_field",
        "stress_events",
        "stress_labels",
        "stress_mcm",
        "quiet_status",
        "quiet_events",
        "quiet_labels",
        "quiet_field",
        "quiet_reifung",
        "quiet_field_share",
        "quiet_mcm",
        "boundary",
        "passive_only",
        "influences_action",
        "is_gate",
        "is_motoric",
        "is_entry_signal",
        "is_direction_signal",
    ]
    summary_fields = ["quiet_status", "families", "quiet_fields", "max_quiet_events"]

    _write_csv(BEFUNDE / f"{args.out_prefix}.detail.csv", rows, detail_fields)
    _write_csv(BEFUNDE / f"{args.out_prefix}.summary.csv", summary, summary_fields)
    _write_markdown(BEFUNDE / f"{args.out_prefix}.md", rows, summary)

    print(f"stress_stable_checked={len(rows)}")
    print(f"quiet_families={len(quiet_rows)}")
    print(f"wrote={BEFUNDE / (args.out_prefix + '.md')}")


if __name__ == "__main__":
    main()
