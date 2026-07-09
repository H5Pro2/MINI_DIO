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


def _candidate_class(*, shared: bool, same_field: bool, same_reifung: bool, left: dict[str, str], right: dict[str, str] | None) -> str:
    left_reife = str(left.get("syntax_reifung", "-"))
    right_reife = str((right or {}).get("syntax_reifung", "-"))
    left_events = _safe_int(left.get("events"))
    right_events = _safe_int((right or {}).get("events"))
    if shared and same_field and same_reifung and left_reife == "weltuebergreifend_feldstabil":
        return "robuste_feldsyntax"
    if shared and same_field:
        return "gemeinsame_feldsyntax_offen"
    if shared:
        return "gemeinsame_syntax_verschoben"
    if left_reife == "weltuebergreifend_feldstabil" and left_events >= 300:
        return "lokal_starke_feldsyntax"
    if right_reife == "weltuebergreifend_feldstabil" and right_events >= 300:
        return "lokal_starke_feldsyntax"
    return "lokale_junge_syntaxinsel"


def _mcm_string(row: dict[str, str] | None) -> str:
    if not row:
        return "-"
    return f"{_fmt(_safe_float(row.get('avg_carry')))}/{_fmt(_safe_float(row.get('avg_strain')))}/{_fmt(_safe_float(row.get('avg_rekopplung')))}"


def _build_candidates(left_rows: list[dict[str, str]], right_rows: list[dict[str, str]]) -> list[dict[str, object]]:
    left = _index(left_rows)
    right = _index(right_rows)
    rows: list[dict[str, object]] = []
    for family in sorted(set(left) | set(right)):
        lrow = left.get(family)
        rrow = right.get(family)
        shared = bool(lrow and rrow)
        lrow = lrow or {}
        rrow = rrow or {}
        same_field = shared and lrow.get("dominant_field_contact_class") == rrow.get("dominant_field_contact_class")
        same_reifung = shared and lrow.get("syntax_reifung") == rrow.get("syntax_reifung")
        candidate = _candidate_class(shared=shared, same_field=bool(same_field), same_reifung=bool(same_reifung), left=lrow, right=rrow)
        rows.append(
            {
                "symbol_family": family,
                "candidate_class": candidate,
                "present_in": "xrp_and_multi" if shared else ("xrp_only" if family in left else "multi_only"),
                "same_field": int(bool(same_field)),
                "same_reifung": int(bool(same_reifung)),
                "xrp_events": _safe_int(lrow.get("events")),
                "multi_events": _safe_int(rrow.get("events")),
                "xrp_field": lrow.get("dominant_field_contact_class", "-"),
                "multi_field": rrow.get("dominant_field_contact_class", "-"),
                "xrp_reifung": lrow.get("syntax_reifung", "-"),
                "multi_reifung": rrow.get("syntax_reifung", "-"),
                "xrp_mcm": _mcm_string(lrow),
                "multi_mcm": _mcm_string(rrow),
            }
        )
    return sorted(
        rows,
        key=lambda row: (
            {
                "robuste_feldsyntax": 0,
                "gemeinsame_feldsyntax_offen": 1,
                "gemeinsame_syntax_verschoben": 2,
                "lokal_starke_feldsyntax": 3,
                "lokale_junge_syntaxinsel": 4,
            }.get(str(row["candidate_class"]), 9),
            -max(int(row["xrp_events"]), int(row["multi_events"])),
            str(row["symbol_family"]),
        ),
    )


def _summarize(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    buckets: dict[str, list[dict[str, object]]] = {}
    for row in rows:
        buckets.setdefault(str(row.get("candidate_class", "-")), []).append(row)
    out: list[dict[str, object]] = []
    for name, bucket in sorted(buckets.items()):
        fields = Counter()
        present = Counter()
        for row in bucket:
            present[str(row.get("present_in", "-"))] += 1
            field = str(row.get("xrp_field") if row.get("xrp_field") != "-" else row.get("multi_field"))
            fields[field] += 1
        out.append(
            {
                "candidate_class": name,
                "families": len(bucket),
                "present_in": ";".join(f"{key}:{value}" for key, value in present.most_common()),
                "fields": ";".join(f"{key}:{value}" for key, value in fields.most_common()),
                "max_xrp_events": max(_safe_int(row.get("xrp_events")) for row in bucket),
                "max_multi_events": max(_safe_int(row.get("multi_events")) for row in bucket),
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
    selected = rows[:limit]
    lines = ["| " + " | ".join(fields) + " |", "| " + " | ".join("---" for _ in fields) + " |"]
    for row in selected:
        lines.append("| " + " | ".join(str(row.get(field, "")) for field in fields) + " |")
    return lines


def _write_markdown(path: Path, rows: list[dict[str, object]], summary: list[dict[str, object]]) -> None:
    class_counts = Counter(str(row.get("candidate_class", "-")) for row in rows)
    lines = [
        "# 2049 - Robuste und lokale Feldsyntax-Kandidaten",
        "",
        "## Zweck",
        "",
        "Diese Auswertung trennt die gemeinsame Feldsyntax aus 2048 von lokalen Syntaxinseln. Damit wird sichtbar, welche Familien als robuste Feldsyntax-Kandidaten gelten und welche Familien zunächst nur lokal oder jung bleiben.",
        "",
        "Die Karte bleibt passiv. Sie gibt MINI_DIO keine Handlung, sondern beschreibt nur Reife und Reichweite einer Syntaxfamilie.",
        "",
        "## Übersicht",
        "",
        f"- Kandidaten gesamt: `{len(rows)}`",
        f"- Klassenverteilung: `{dict(sorted(class_counts.items()))}`",
        "",
        "## Klassen",
        "",
    ]
    lines.extend(_md_table(summary, ["candidate_class", "families", "present_in", "fields", "max_xrp_events", "max_multi_events"], limit=20))
    lines.extend(["", "## Stärkste Kandidaten", ""])
    lines.extend(
        _md_table(
            rows,
            [
                "symbol_family",
                "candidate_class",
                "present_in",
                "same_field",
                "same_reifung",
                "xrp_events",
                "multi_events",
                "xrp_field",
                "multi_field",
                "xrp_mcm",
                "multi_mcm",
            ],
            limit=25,
        )
    )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "`robuste_feldsyntax` bedeutet: dieselbe Familie tritt in XRP und in BTC/DOGE/PAXG auf, mit gleicher Feldklasse und gleicher Reifung. Das ist der stärkste passive Kandidat für weltübergreifende Feldsyntax.",
            "",
            "`lokale_junge_syntaxinsel` bedeutet nicht wertlos. Es heißt nur: Noch nicht weltübergreifend getragen. Diese Inseln können bei weiterer Weltzufuhr reifen, sich teilen oder verschwinden.",
            "",
            "## Grenze",
            "",
            "Keine Handlung, keine Richtung, kein Gate. Diese Karte ist eine passive Reife- und Reichweitenkarte der Feldsyntax.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte geprüft werden, ob lokale starke Familien bei weiterer Weltzufuhr in `robuste_feldsyntax` übergehen oder ob sie asset-/weltgebundene Milieuinseln bleiben.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--xrp", default="docs/befunde/2046_XRP_FELDKLASSEN_ZU_NEUER_SYNTAXNAEHE.bridge.csv")
    parser.add_argument("--multi", default="docs/befunde/2047_MULTI_FELDKLASSEN_ZU_NEUER_SYNTAXNAEHE.bridge.csv")
    parser.add_argument("--out-prefix", default="2049_ROBUSTE_UND_LOKALE_FELDSYNTAX_KANDIDATEN")
    args = parser.parse_args()

    rows = _build_candidates(_load_csv(Path(args.xrp)), _load_csv(Path(args.multi)))
    summary = _summarize(rows)
    out_prefix = BEFUNDE / args.out_prefix
    _write_csv(
        out_prefix.with_suffix(".candidates.csv"),
        rows,
        [
            "symbol_family",
            "candidate_class",
            "present_in",
            "same_field",
            "same_reifung",
            "xrp_events",
            "multi_events",
            "xrp_field",
            "multi_field",
            "xrp_reifung",
            "multi_reifung",
            "xrp_mcm",
            "multi_mcm",
        ],
    )
    _write_csv(
        out_prefix.with_suffix(".summary.csv"),
        summary,
        ["candidate_class", "families", "present_in", "fields", "max_xrp_events", "max_multi_events"],
    )
    _write_markdown(out_prefix.with_suffix(".md"), rows, summary)
    print(f"candidates={len(rows)}")
    print(f"classes={dict(Counter(str(row.get('candidate_class', '-')) for row in rows))}")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
