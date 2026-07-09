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


def _follow_reifung(local: dict[str, str], follow: dict[str, str] | None) -> str:
    if not follow:
        return "nicht_wiedergefunden"
    same_field = local.get("xrp_field") == follow.get("dominant_field_contact_class") or local.get("multi_field") == follow.get("dominant_field_contact_class")
    follow_reife = str(follow.get("syntax_reifung", "-"))
    follow_events = _safe_int(follow.get("events"))
    if same_field and follow_reife == "weltuebergreifend_feldstabil":
        return "gereift_zu_robuster_feldsyntax"
    if same_field and follow_events >= 100:
        return "wiedergefunden_feldnah"
    if follow_events >= 100:
        return "wiedergefunden_verschoben"
    return "wiedergefunden_jung"


def _build_rows(candidates: list[dict[str, str]], follow_rows: list[dict[str, str]]) -> list[dict[str, object]]:
    follow = _index(follow_rows)
    rows: list[dict[str, object]] = []
    for row in candidates:
        if row.get("candidate_class") != "lokale_junge_syntaxinsel":
            continue
        family = str(row.get("symbol_family", "-"))
        follow_row = follow.get(family)
        status = _follow_reifung(row, follow_row)
        rows.append(
            {
                "symbol_family": family,
                "origin_present_in": row.get("present_in", "-"),
                "origin_xrp_events": _safe_int(row.get("xrp_events")),
                "origin_multi_events": _safe_int(row.get("multi_events")),
                "origin_xrp_field": row.get("xrp_field", "-"),
                "origin_multi_field": row.get("multi_field", "-"),
                "follow_events": _safe_int((follow_row or {}).get("events")),
                "follow_labels": (follow_row or {}).get("holdout_labels", "-"),
                "follow_field": (follow_row or {}).get("dominant_field_contact_class", "-"),
                "follow_reifung": (follow_row or {}).get("syntax_reifung", "-"),
                "follow_status": status,
                "follow_mcm": (
                    f"{_fmt(_safe_float((follow_row or {}).get('avg_carry')))}/"
                    f"{_fmt(_safe_float((follow_row or {}).get('avg_strain')))}/"
                    f"{_fmt(_safe_float((follow_row or {}).get('avg_rekopplung')))}"
                    if follow_row
                    else "-"
                ),
            }
        )
    return sorted(
        rows,
        key=lambda item: (
            {
                "gereift_zu_robuster_feldsyntax": 0,
                "wiedergefunden_feldnah": 1,
                "wiedergefunden_verschoben": 2,
                "wiedergefunden_jung": 3,
                "nicht_wiedergefunden": 4,
            }.get(str(item["follow_status"]), 9),
            -int(item["follow_events"]),
            str(item["symbol_family"]),
        ),
    )


def _summary(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    buckets: dict[str, list[dict[str, object]]] = {}
    for row in rows:
        buckets.setdefault(str(row.get("follow_status", "-")), []).append(row)
    out = []
    for status, bucket in sorted(buckets.items()):
        origins = Counter(str(row.get("origin_present_in", "-")) for row in bucket)
        fields = Counter(str(row.get("follow_field", "-")) for row in bucket)
        out.append(
            {
                "follow_status": status,
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
    counts = Counter(str(row.get("follow_status", "-")) for row in rows)
    lines = [
        "# 2051 - Reifung lokaler Syntaxinseln in Folgewelten",
        "",
        "## Zweck",
        "",
        "Diese Auswertung nimmt die lokalen jungen Syntaxinseln aus 2049 und prüft sie gegen weitere Weltzufuhr aus 2050. Ziel ist die Unterscheidung: reift eine lokale Insel, bleibt sie lokal, oder verschwindet sie?",
        "",
        "Die Prüfung bleibt passiv. Es geht um Reife und Wiederfindung, nicht um Handlung.",
        "",
        "## Übersicht",
        "",
        f"- geprüfte lokale Inseln: `{len(rows)}`",
        f"- Statusverteilung: `{dict(sorted(counts.items()))}`",
        "",
        "## Statusklassen",
        "",
    ]
    lines.extend(_md_table(summary, ["follow_status", "families", "origin_present_in", "follow_fields", "max_follow_events"], limit=20))
    lines.extend(["", "## Stärkste gereifte oder wiedergefundene Inseln", ""])
    lines.extend(
        _md_table(
            rows,
            [
                "symbol_family",
                "follow_status",
                "origin_present_in",
                "follow_events",
                "follow_labels",
                "follow_field",
                "follow_reifung",
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
            "Wenn lokale junge Inseln in Folgewelten wieder auftauchen, sind sie nicht mehr nur lokale Reste. Sie werden zu Reifekandidaten. Wenn sie nicht wiedergefunden werden, bleiben sie vorerst weltgebundene oder zu schwache Inseln.",
            "",
            "Wichtig: Auch `nicht_wiedergefunden` ist kein Fehler. Es zeigt, dass ein Teil der Syntaxbildung wirklich situativ bleibt.",
            "",
            "## Grenze",
            "",
            "Keine Handlung, keine Richtung, kein Gate. Diese Karte beschreibt nur, welche lokalen Inseln bei weiterer Weltzufuhr wieder anschließen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollten die gereiften lokalen Inseln in die robuste Kandidatenkarte aufgenommen werden, aber nur als passive Reifespur. Danach kann geprüft werden, ob diese Reifespuren unter Stress wieder stabil bleiben.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", default="docs/befunde/2049_ROBUSTE_UND_LOKALE_FELDSYNTAX_KANDIDATEN.candidates.csv")
    parser.add_argument("--follow", default="docs/befunde/2050_FOLGEWELTEN_FELDKLASSEN_ZU_SYNTAXNAEHE.bridge.csv")
    parser.add_argument("--out-prefix", default="2051_LOKALE_SYNTAXINSELN_FOLGEWELT_REIFUNG")
    args = parser.parse_args()

    rows = _build_rows(_load_csv(Path(args.candidates)), _load_csv(Path(args.follow)))
    summary = _summary(rows)
    out_prefix = BEFUNDE / args.out_prefix
    _write_csv(
        out_prefix.with_suffix(".detail.csv"),
        rows,
        [
            "symbol_family",
            "origin_present_in",
            "origin_xrp_events",
            "origin_multi_events",
            "origin_xrp_field",
            "origin_multi_field",
            "follow_events",
            "follow_labels",
            "follow_field",
            "follow_reifung",
            "follow_status",
            "follow_mcm",
        ],
    )
    _write_csv(
        out_prefix.with_suffix(".summary.csv"),
        summary,
        ["follow_status", "families", "origin_present_in", "follow_fields", "max_follow_events"],
    )
    _write_markdown(out_prefix.with_suffix(".md"), rows, summary)
    print(f"local_islands={len(rows)}")
    print(f"status={dict(Counter(str(row.get('follow_status', '-')) for row in rows))}")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
