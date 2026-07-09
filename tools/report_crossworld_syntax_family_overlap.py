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


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _safe_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _fmt(value: float) -> str:
    return f"{value:.3f}"


def _index(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {str(row.get("symbol_family", "-")): row for row in rows if row.get("symbol_family")}


def _build_overlap(left_rows: list[dict[str, str]], right_rows: list[dict[str, str]]) -> tuple[dict[str, object], list[dict[str, object]]]:
    left = _index(left_rows)
    right = _index(right_rows)
    left_keys = set(left)
    right_keys = set(right)
    shared = sorted(left_keys & right_keys)
    union = left_keys | right_keys
    overlap_rows: list[dict[str, object]] = []
    for family in shared:
        lrow = left[family]
        rrow = right[family]
        same_field = lrow.get("dominant_field_contact_class") == rrow.get("dominant_field_contact_class")
        same_reife = lrow.get("syntax_reifung") == rrow.get("syntax_reifung")
        overlap_rows.append(
            {
                "symbol_family": family,
                "xrp_events": _safe_int(lrow.get("events")),
                "multi_events": _safe_int(rrow.get("events")),
                "xrp_field": lrow.get("dominant_field_contact_class", "-"),
                "multi_field": rrow.get("dominant_field_contact_class", "-"),
                "same_field": int(same_field),
                "xrp_reifung": lrow.get("syntax_reifung", "-"),
                "multi_reifung": rrow.get("syntax_reifung", "-"),
                "same_reifung": int(same_reife),
                "xrp_field_share": _safe_float(lrow.get("dominant_field_share")),
                "multi_field_share": _safe_float(rrow.get("dominant_field_share")),
                "xrp_mcm": f"{_fmt(_safe_float(lrow.get('avg_carry')))}/{_fmt(_safe_float(lrow.get('avg_strain')))}/{_fmt(_safe_float(lrow.get('avg_rekopplung')))}",
                "multi_mcm": f"{_fmt(_safe_float(rrow.get('avg_carry')))}/{_fmt(_safe_float(rrow.get('avg_strain')))}/{_fmt(_safe_float(rrow.get('avg_rekopplung')))}",
            }
        )
    overlap_rows.sort(key=lambda row: (-min(int(row["xrp_events"]), int(row["multi_events"])), str(row["symbol_family"])))
    summary = {
        "xrp_families": len(left_keys),
        "multi_families": len(right_keys),
        "shared_families": len(shared),
        "union_families": len(union),
        "jaccard": len(shared) / max(1, len(union)),
        "shared_same_field": sum(int(row["same_field"]) for row in overlap_rows),
        "shared_same_reifung": sum(int(row["same_reifung"]) for row in overlap_rows),
        "shared_field_counts": dict(Counter(str(row["xrp_field"]) for row in overlap_rows)),
        "xrp_only": len(left_keys - right_keys),
        "multi_only": len(right_keys - left_keys),
    }
    return summary, overlap_rows


def _write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def _md_table(rows: list[dict[str, object]], fields: list[str], limit: int = 24) -> list[str]:
    selected = rows[:limit]
    lines = ["| " + " | ".join(fields) + " |", "| " + " | ".join("---" for _ in fields) + " |"]
    for row in selected:
        lines.append("| " + " | ".join(str(row.get(field, "")) for field in fields) + " |")
    return lines


def _write_markdown(path: Path, summary: dict[str, object], rows: list[dict[str, object]]) -> None:
    lines = [
        "# 2048 - Weltübergreifende Syntaxfamilien-Überlappung",
        "",
        "## Zweck",
        "",
        "Diese Auswertung vergleicht die neue XRP-Syntaxnähe aus 2046 mit der Multi-Welt-Syntaxnähe aus 2047. Geprüft wird, ob Familien nur lokal entstehen oder ob dieselben Familien in unterschiedlichen Weltspannungen wieder auftauchen.",
        "",
        "## Übersicht",
        "",
        f"- XRP-Syntaxfamilien: `{summary['xrp_families']}`",
        f"- Multi-Syntaxfamilien: `{summary['multi_families']}`",
        f"- gemeinsame Familien: `{summary['shared_families']}`",
        f"- Jaccard-Überlappung: `{_fmt(float(summary['jaccard']))}`",
        f"- gemeinsame Familien mit gleicher Feldklasse: `{summary['shared_same_field']}`",
        f"- gemeinsame Familien mit gleicher Reifung: `{summary['shared_same_reifung']}`",
        f"- XRP-only: `{summary['xrp_only']}`",
        f"- Multi-only: `{summary['multi_only']}`",
        f"- Feldklassen in gemeinsamen Familien: `{summary['shared_field_counts']}`",
        "",
        "## Stärkste gemeinsame Familien",
        "",
    ]
    lines.extend(
        _md_table(
            rows,
            [
                "symbol_family",
                "xrp_events",
                "multi_events",
                "xrp_field",
                "multi_field",
                "same_field",
                "xrp_reifung",
                "multi_reifung",
                "same_reifung",
                "xrp_mcm",
                "multi_mcm",
            ],
        )
    )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Der Befund trennt zwei Dinge: lokale Syntaxbildung und weltübergreifende Feldsyntax. Wenn dieselbe Familie in XRP und in BTC/DOGE/PAXG mit gleicher Feldklasse auftaucht, spricht das für eine wiederkehrende innere Feldform, nicht nur für assetgebundene Oberfläche.",
            "",
            "Die Jaccard-Überlappung ist dabei bewusst konservativ: Sie misst nur exakte Familiennamen. Bedeutungsnähe ohne identischen Namen wird hier noch nicht gezählt.",
            "",
            "## Grenze",
            "",
            "Auch diese Überlappung ist passiv. Sie beweist keine Handlung und keine Absicht. Sie zeigt, ob Syntaxfamilien über unterschiedliche Weltkontakte hinweg feldnah wiederkehren.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollten wir die gemeinsamen Familien von den lokalen Familien trennen und prüfen, ob lokale Familien bei weiterer Weltzufuhr in gemeinsame Familien übergehen oder wieder zerfallen.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--xrp", default="docs/befunde/2001-3000/2046_XRP_FELDKLASSEN_ZU_NEUER_SYNTAXNAEHE.bridge.csv")
    parser.add_argument("--multi", default="docs/befunde/2001-3000/2047_MULTI_FELDKLASSEN_ZU_NEUER_SYNTAXNAEHE.bridge.csv")
    parser.add_argument("--out-prefix", default="2048_WELTUEBERGREIFENDE_SYNTAXFAMILIEN_UEBERLAPPUNG")
    args = parser.parse_args()

    summary, rows = _build_overlap(_load_csv(Path(args.xrp)), _load_csv(Path(args.multi)))
    out_prefix = BEFUNDE / args.out_prefix
    _write_csv(
        out_prefix.with_suffix(".shared.csv"),
        rows,
        [
            "symbol_family",
            "xrp_events",
            "multi_events",
            "xrp_field",
            "multi_field",
            "same_field",
            "xrp_reifung",
            "multi_reifung",
            "same_reifung",
            "xrp_field_share",
            "multi_field_share",
            "xrp_mcm",
            "multi_mcm",
        ],
    )
    _write_csv(out_prefix.with_suffix(".summary.csv"), [summary], list(summary.keys()))
    _write_markdown(out_prefix.with_suffix(".md"), summary, rows)
    print(f"shared={summary['shared_families']}")
    print(f"jaccard={summary['jaccard']:.3f}")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
