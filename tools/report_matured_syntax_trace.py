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


def _classify_trace(row: dict[str, str]) -> str:
    origin = row.get("origin_present_in", "-")
    field = row.get("follow_field", "-")
    events = _safe_int(row.get("follow_events"))
    if row.get("follow_status") != "gereift_zu_robuster_feldsyntax":
        return "nicht_nachgereift"
    if field == "tragende_rekopplung" and events >= 20:
        return "nachgereift_tragend"
    if field == "offene_rekopplung" and events >= 20:
        return "nachgereift_offen"
    if field == "spannungsnahe_oeffnung":
        return "nachgereift_spannungsnah"
    if origin == "multi_only":
        return "nachgereift_multi_zu_folgewelt"
    return "nachgereift_schwach"


def _build_rows(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    out = []
    for row in rows:
        if row.get("follow_status") != "gereift_zu_robuster_feldsyntax":
            continue
        out.append(
            {
                "symbol_family": row.get("symbol_family", "-"),
                "matured_trace_class": _classify_trace(row),
                "origin_present_in": row.get("origin_present_in", "-"),
                "origin_xrp_events": _safe_int(row.get("origin_xrp_events")),
                "origin_multi_events": _safe_int(row.get("origin_multi_events")),
                "origin_field": row.get("origin_xrp_field") if row.get("origin_xrp_field") != "-" else row.get("origin_multi_field", "-"),
                "follow_events": _safe_int(row.get("follow_events")),
                "follow_labels": row.get("follow_labels", "-"),
                "follow_field": row.get("follow_field", "-"),
                "follow_reifung": row.get("follow_reifung", "-"),
                "follow_mcm": row.get("follow_mcm", "-"),
                "boundary": "passive_matured_syntax_trace_no_action_no_direction",
                "passive_only": 1,
                "influences_action": 0,
                "is_gate": 0,
                "is_motoric": 0,
                "is_entry_signal": 0,
                "is_direction_signal": 0,
            }
        )
    return sorted(out, key=lambda item: (str(item["matured_trace_class"]), -int(item["follow_events"]), str(item["symbol_family"])))


def _summary(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    buckets: dict[str, list[dict[str, object]]] = {}
    for row in rows:
        buckets.setdefault(str(row.get("matured_trace_class", "-")), []).append(row)
    out = []
    for name, bucket in sorted(buckets.items()):
        origins = Counter(str(row.get("origin_present_in", "-")) for row in bucket)
        fields = Counter(str(row.get("follow_field", "-")) for row in bucket)
        out.append(
            {
                "matured_trace_class": name,
                "families": len(bucket),
                "origin_present_in": ";".join(f"{key}:{value}" for key, value in origins.most_common()),
                "follow_fields": ";".join(f"{key}:{value}" for key, value in fields.most_common()),
                "max_follow_events": max(_safe_int(row.get("follow_events")) for row in bucket),
            }
        )
    return out


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
    counts = Counter(str(row.get("matured_trace_class", "-")) for row in rows)
    lines = [
        "# 2052 - Passive Reifespur nachgereifter Syntaxinseln",
        "",
        "## Zweck",
        "",
        "Diese Auswertung markiert lokale Syntaxinseln, die in Folgewelten zu robuster Feldsyntax nachgereift sind. Sie werden bewusst getrennt von den ursprünglichen robusten Familien geführt.",
        "",
        "Die Trennung ist wichtig: Eine Familie kann primär weltübergreifend stabil sein oder erst über weitere Weltzufuhr nachreifen. Beides ist Feldsyntax, aber nicht derselbe Reifeweg.",
        "",
        "## Übersicht",
        "",
        f"- nachgereifte Familien: `{len(rows)}`",
        f"- Klassenverteilung: `{dict(sorted(counts.items()))}`",
        "",
        "## Reifeklassen",
        "",
    ]
    lines.extend(_md_table(summary, ["matured_trace_class", "families", "origin_present_in", "follow_fields", "max_follow_events"], limit=20))
    lines.extend(["", "## Stärkste nachgereifte Familien", ""])
    lines.extend(
        _md_table(
            rows,
            [
                "symbol_family",
                "matured_trace_class",
                "origin_present_in",
                "origin_field",
                "follow_events",
                "follow_labels",
                "follow_field",
                "follow_mcm",
            ],
            limit=30,
        )
    )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Nachgereifte Familien sind keine neuen Regeln. Sie zeigen, dass eine zuerst lokale Insel unter weiterer Weltzufuhr wieder anschließen und stabiler werden kann.",
            "",
            "Diese Spur ist für MINI_DIO wichtig, weil Entwicklung dadurch nicht binär gelesen wird. Eine Insel muss nicht sofort robust sein. Sie kann jung erscheinen, später wieder auftauchen und erst dann Reife bekommen.",
            "",
            "## Grenze",
            "",
            "Keine Handlung, keine Richtung, kein Gate. Diese Reifespur beschreibt nur Entwicklungsqualität im Feldgedächtnis.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollten diese nachgereiften Familien unter Stress geprüft werden. Entscheidend ist, ob sie belastbar bleiben oder wieder in junge, lokale Inseln zurückfallen.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--detail", default="docs/befunde/2001-3000/2051_LOKALE_SYNTAXINSELN_FOLGEWELT_REIFUNG.detail.csv")
    parser.add_argument("--out-prefix", default="2052_PASSIVE_REIFESPUR_NACHGEREIFTER_SYNTAXINSELN")
    args = parser.parse_args()

    rows = _build_rows(_load_csv(Path(args.detail)))
    summary = _summary(rows)
    out_prefix = BEFUNDE / args.out_prefix
    fields = [
        "symbol_family",
        "matured_trace_class",
        "origin_present_in",
        "origin_xrp_events",
        "origin_multi_events",
        "origin_field",
        "follow_events",
        "follow_labels",
        "follow_field",
        "follow_reifung",
        "follow_mcm",
        "boundary",
        "passive_only",
        "influences_action",
        "is_gate",
        "is_motoric",
        "is_entry_signal",
        "is_direction_signal",
    ]
    _write_csv(out_prefix.with_suffix(".families.csv"), rows, fields)
    _write_csv(
        out_prefix.with_suffix(".summary.csv"),
        summary,
        ["matured_trace_class", "families", "origin_present_in", "follow_fields", "max_follow_events"],
    )
    _write_markdown(out_prefix.with_suffix(".md"), rows, summary)
    print(f"matured={len(rows)}")
    print(f"classes={dict(Counter(str(row.get('matured_trace_class', '-')) for row in rows))}")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
