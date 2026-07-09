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
    return f"{value:.6f}"


def _index(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {str(row.get("symbol_family", "-")): row for row in rows if row.get("symbol_family")}


def _follow_status(seed: dict[str, str], follow: dict[str, str] | None) -> str:
    if not follow:
        return "folge_nicht_wiedergefunden"
    same_field = seed.get("real_field") == follow.get("dominant_field_contact_class")
    reifung = str(follow.get("syntax_reifung", "-"))
    events = _safe_int(follow.get("events"))
    if same_field and reifung == "weltuebergreifend_feldstabil":
        return "folge_stabil_feldgleich"
    if same_field and reifung in {"weltuebergreifend_feldoffen", "lokal_feldstabil"}:
        return "folge_offen_feldgleich"
    if same_field and events > 0:
        return "folge_jung_feldgleich"
    if events > 0:
        return "folge_verschoben"
    return "folge_nicht_wiedergefunden"


def _build_rows(seed_rows: list[dict[str, str]], follow_rows: list[dict[str, str]]) -> list[dict[str, object]]:
    follow_index = _index(follow_rows)
    rows: list[dict[str, object]] = []
    for seed in seed_rows:
        if seed.get("contrast_class") != "real_deutlich_staerker":
            continue
        family = str(seed.get("symbol_family", "-"))
        follow = follow_index.get(family)
        rows.append(
            {
                "symbol_family": family,
                "seed_class": seed.get("contrast_class", "-"),
                "seed_real_events": _safe_int(seed.get("real_events")),
                "seed_null_events": _safe_int(seed.get("null_events")),
                "seed_ratio": _fmt(_safe_float(seed.get("real_null_ratio"))),
                "seed_field": seed.get("real_field", "-"),
                "follow_status": _follow_status(seed, follow),
                "follow_events": _safe_int((follow or {}).get("events")),
                "follow_labels": (follow or {}).get("holdout_labels", "-"),
                "follow_field": (follow or {}).get("dominant_field_contact_class", "-"),
                "follow_reifung": (follow or {}).get("syntax_reifung", "-"),
                "follow_field_share": _fmt(_safe_float((follow or {}).get("dominant_field_share"))),
                "follow_mcm": (
                    f"{_safe_float((follow or {}).get('avg_carry')):.3f}/"
                    f"{_safe_float((follow or {}).get('avg_strain')):.3f}/"
                    f"{_safe_float((follow or {}).get('avg_rekopplung')):.3f}"
                    if follow
                    else "-"
                ),
                "boundary": "passive_real_strengthened_followworld_trace_no_action_no_direction",
            }
        )
    order = {
        "folge_stabil_feldgleich": 0,
        "folge_offen_feldgleich": 1,
        "folge_jung_feldgleich": 2,
        "folge_verschoben": 3,
        "folge_nicht_wiedergefunden": 4,
    }
    rows.sort(key=lambda row: (order.get(str(row["follow_status"]), 9), -_safe_int(row["follow_events"]), str(row["symbol_family"])))
    return rows


def _summary(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    buckets: dict[str, list[dict[str, object]]] = {}
    for row in rows:
        buckets.setdefault(str(row["follow_status"]), []).append(row)
    out: list[dict[str, object]] = []
    for status, bucket in sorted(buckets.items()):
        fields = Counter(str(row.get("follow_field", "-")) for row in bucket)
        out.append(
            {
                "follow_status": status,
                "families": len(bucket),
                "follow_fields": ";".join(f"{key}:{value}" for key, value in fields.most_common()),
                "max_follow_events": max(_safe_int(row.get("follow_events")) for row in bucket),
            }
        )
    return out


def _write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def _md_table(rows: list[dict[str, object]], fields: list[str], limit: int = 30) -> list[str]:
    lines = ["| " + " | ".join(fields) + " |", "| " + " | ".join("---" for _ in fields) + " |"]
    for row in rows[:limit]:
        lines.append("| " + " | ".join(str(row.get(field, "")) for field in fields) + " |")
    return lines


def _write_markdown(path: Path, rows: list[dict[str, object]], summary: list[dict[str, object]]) -> None:
    counts = Counter(str(row["follow_status"]) for row in rows)
    lines = [
        "# 2064 - Realverstärkte Rollen in echten Folgewelten",
        "",
        "## Zweck",
        "",
        "Diese Auswertung nimmt die Rollen aus 2062, die im Realraum deutlich stärker als im Null-/Shuffle-Raum waren, und prüft sie gegen weitere echte Folgewelten.",
        "",
        "Die Prüfung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung, kein Gate und keinen motorischen Impuls.",
        "",
        "## Übersicht",
        "",
        f"- geprüfte realverstärkte Rollen: `{len(rows)}`",
        f"- Statusverteilung: `{dict(sorted(counts.items()))}`",
        "",
        "## Statusklassen",
        "",
    ]
    lines.extend(_md_table(summary, ["follow_status", "families", "follow_fields", "max_follow_events"], limit=20))
    lines.extend(["", "## Stärkste feldgleiche Folgewelt-Wiederfunde", ""])
    lines.extend(
        _md_table(
            rows,
            [
                "symbol_family",
                "follow_status",
                "seed_ratio",
                "seed_real_events",
                "seed_null_events",
                "follow_events",
                "follow_labels",
                "follow_field",
                "follow_reifung",
                "follow_mcm",
            ],
            limit=35,
        )
    )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Wenn realverstärkte Rollen in echten Folgewelten feldgleich wiederkehren, spricht das für eine belastbarere Bedeutungsrolle: feldinterne Grundform plus reale Aktivierung plus Folgewelt-Tragfähigkeit.",
            "",
            "Wenn sie in Folgewelten verschwinden, bleiben sie im bisherigen Realraum situativ. Wenn sie verschoben wiederkehren, ist die Rolle wahrscheinlich weltspannungsabhängig.",
            "",
            "## Grenze",
            "",
            "Die Auswertung bleibt diagnostisch. Sie beschreibt keine Strategie und keinen Handlungsmechanismus.",
            "",
            "Wie es weitergeht: Als nächstes sollten die stabil feldgleichen Folgewelt-Rollen auf Rollenfamilien geprüft werden: bilden sie nur Einzelzeichen oder entstehen daraus mehrere nahe Bedeutungen mit gemeinsamer Feldfunktion?",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", default="docs/befunde/2062_MULTIROLLEN_REAL_NULL_KONTRAST.csv")
    parser.add_argument("--follow-bridge", default="docs/befunde/2063_FOLGEWELTEN_REALVERSTAERKTE_ROLLEN_FELDKLASSEN.bridge.csv")
    parser.add_argument("--out-prefix", default="2064_REALVERSTAERKTE_ROLLEN_IN_FOLGEWELTEN")
    args = parser.parse_args()

    rows = _build_rows(_load_csv(Path(args.seeds)), _load_csv(Path(args.follow_bridge)))
    summary = _summary(rows)
    detail_fields = [
        "symbol_family",
        "seed_class",
        "seed_real_events",
        "seed_null_events",
        "seed_ratio",
        "seed_field",
        "follow_status",
        "follow_events",
        "follow_labels",
        "follow_field",
        "follow_reifung",
        "follow_field_share",
        "follow_mcm",
        "boundary",
    ]
    summary_fields = ["follow_status", "families", "follow_fields", "max_follow_events"]
    _write_csv(BEFUNDE / f"{args.out_prefix}.detail.csv", rows, detail_fields)
    _write_csv(BEFUNDE / f"{args.out_prefix}.summary.csv", summary, summary_fields)
    _write_markdown(BEFUNDE / f"{args.out_prefix}.md", rows, summary)
    print(f"checked={len(rows)}")
    print(f"wrote={BEFUNDE / (args.out_prefix + '.md')}")


if __name__ == "__main__":
    main()
