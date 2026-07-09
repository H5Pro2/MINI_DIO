from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path

from befunde_paths import befunde_root
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = befunde_root(ROOT)


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _fmt(value: float) -> str:
    return f"{value:.3f}"


def _field_contact_class(row: dict[str, object]) -> str:
    carry = _safe_float(row.get("mcm_carry_quality"))
    strain = _safe_float(row.get("mcm_strain_quality"))
    rekopplung = _safe_float(row.get("mcm_rekopplung_quality"))
    if rekopplung >= 0.62 and carry >= 0.40 and strain <= 0.24:
        return "tragende_rekopplung"
    if rekopplung >= 0.58 and strain <= 0.28:
        return "offene_rekopplung"
    if strain >= 0.28 and rekopplung <= 0.59:
        return "spannungsnahe_oeffnung"
    if carry >= 0.40:
        return "getragen_offen"
    return "offener_feldkontakt"


def _episode_paths(root: Path) -> list[Path]:
    root = root if root.is_absolute() else ROOT / root
    return sorted(root.glob("dio_mini_lauf_*/episodes.csv"))


def _read_episodes(label: str, root: Path, max_rows: int) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for path in _episode_paths(root):
        run = path.parent.name
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for raw in reader:
                rows.append(
                    {
                        "holdout_label": label,
                        "run": run,
                        "symbol": raw.get("symbol", "-"),
                        "symbol_family": raw.get("symbol_family", "-"),
                        "field_contact_class": _field_contact_class(raw),
                        "mcm_field_effect_state": raw.get("mcm_field_effect_state", "-"),
                        "passive_mcm_effect_class": raw.get("passive_mcm_effect_class", "-"),
                        "mcm_carry_quality": _safe_float(raw.get("mcm_carry_quality")),
                        "mcm_strain_quality": _safe_float(raw.get("mcm_strain_quality")),
                        "mcm_rekopplung_quality": _safe_float(raw.get("mcm_rekopplung_quality")),
                    }
                )
                if max_rows > 0 and len(rows) >= max_rows:
                    return rows
    return rows


def _summarize_family(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    buckets: dict[tuple[str, str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        key = (
            str(row.get("holdout_label", "-")),
            str(row.get("symbol_family", "-")),
            str(row.get("field_contact_class", "-")),
        )
        buckets[key].append(row)
    out: list[dict[str, object]] = []
    for (label, family, field_class), bucket in sorted(buckets.items()):
        symbols = Counter(str(row.get("symbol", "-")) for row in bucket)
        runs = Counter(str(row.get("run", "-")) for row in bucket)
        out.append(
            {
                "holdout_label": label,
                "symbol_family": family,
                "field_contact_class": field_class,
                "events": len(bucket),
                "distinct_symbols": len(symbols),
                "runs": ";".join(f"{name}:{count}" for name, count in runs.most_common()),
                "top_symbols": ";".join(f"{name}:{count}" for name, count in symbols.most_common(5)),
                "avg_carry": mean(_safe_float(row.get("mcm_carry_quality")) for row in bucket),
                "avg_strain": mean(_safe_float(row.get("mcm_strain_quality")) for row in bucket),
                "avg_rekopplung": mean(_safe_float(row.get("mcm_rekopplung_quality")) for row in bucket),
            }
        )
    return sorted(out, key=lambda row: (-int(row["events"]), str(row["holdout_label"]), str(row["symbol_family"])))


def _build_bridge_rows(families: list[dict[str, object]]) -> list[dict[str, object]]:
    by_family: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in families:
        by_family[str(row.get("symbol_family", "-"))].append(row)

    out: list[dict[str, object]] = []
    for family, bucket in sorted(by_family.items()):
        total = sum(int(row.get("events", 0)) for row in bucket)
        labels = Counter(str(row.get("holdout_label", "-")) for row in bucket)
        field_classes = Counter()
        for row in bucket:
            field_classes[str(row.get("field_contact_class", "-"))] += int(row.get("events", 0))
        dominant, dom_count = field_classes.most_common(1)[0] if field_classes else ("-", 0)
        if len(labels) >= 2 and dom_count / max(1, total) >= 0.80:
            reife = "weltuebergreifend_feldstabil"
        elif len(labels) >= 2:
            reife = "weltuebergreifend_feldoffen"
        elif total >= 1000 and dom_count / max(1, total) >= 0.80:
            reife = "lokal_feldstabil"
        elif total >= 1000:
            reife = "lokal_feldoffen"
        else:
            reife = "junge_syntaxinsel"
        out.append(
            {
                "symbol_family": family,
                "events": total,
                "holdout_labels": ";".join(f"{name}:{count}" for name, count in labels.most_common()),
                "dominant_field_contact_class": dominant,
                "dominant_field_share": dom_count / max(1, total),
                "field_classes": ";".join(f"{name}:{count}" for name, count in field_classes.most_common()),
                "syntax_reifung": reife,
                "avg_carry": mean(_safe_float(row.get("avg_carry")) for row in bucket),
                "avg_strain": mean(_safe_float(row.get("avg_strain")) for row in bucket),
                "avg_rekopplung": mean(_safe_float(row.get("avg_rekopplung")) for row in bucket),
            }
        )
    return sorted(out, key=lambda row: (-int(row["events"]), str(row["symbol_family"])))


def _write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def _md_table(rows: list[dict[str, object]], fields: list[str], limit: int = 20) -> list[str]:
    selected = rows[:limit]
    lines = ["| " + " | ".join(fields) + " |", "| " + " | ".join("---" for _ in fields) + " |"]
    for row in selected:
        cells = []
        for field in fields:
            value = row.get(field, "")
            if isinstance(value, float):
                value = _fmt(value)
            cells.append(str(value))
        lines.append("| " + " | ".join(cells) + " |")
    return lines


def _write_markdown(path: Path, family_rows: list[dict[str, object]], bridge_rows: list[dict[str, object]]) -> None:
    reife_counts = Counter(str(row.get("syntax_reifung", "-")) for row in bridge_rows)
    field_counts = Counter()
    for row in bridge_rows:
        field_counts[str(row.get("dominant_field_contact_class", "-"))] += int(row.get("events", 0))
    lines = [
        "# 2046 - Von Feldklassen-Verfügbarkeit zu neuer Syntaxnähe",
        "",
        "## Zweck",
        "",
        "2044 zeigte keinen exakten Rückgriff auf alte Syntax. 2045 zeigte aber Feldklassen-Verfügbarkeit. Diese Auswertung prüft den nächsten Schritt: Bildet die neue Welt innerhalb dieser Feldklassen eigene stabile Syntaxfamilien?",
        "",
        "Das ist passiv. Eine neue Syntaxfamilie ist hier keine Entscheidung und keine Handlung, sondern eine mögliche Bedeutungsnähe, die aus Feldkontakt wiederholt entsteht.",
        "",
        "## Übersicht",
        "",
        f"- Familien-Feldzeilen: `{len(family_rows)}`",
        f"- Syntaxfamilien: `{len(bridge_rows)}`",
        f"- Reifungsverteilung: `{dict(sorted(reife_counts.items()))}`",
        f"- Dominante Feldklassen nach Ereignissen: `{dict(field_counts.most_common())}`",
        "",
        "## Reifere Syntaxfamilien",
        "",
    ]
    lines.extend(
        _md_table(
            bridge_rows,
            [
                "symbol_family",
                "events",
                "holdout_labels",
                "dominant_field_contact_class",
                "dominant_field_share",
                "syntax_reifung",
                "avg_carry",
                "avg_strain",
                "avg_rekopplung",
            ],
            limit=18,
        )
    )
    lines.extend(["", "## Stärkste Familien pro Welt/Feldklasse", ""])
    lines.extend(
        _md_table(
            family_rows,
            [
                "holdout_label",
                "symbol_family",
                "field_contact_class",
                "events",
                "distinct_symbols",
                "top_symbols",
                "avg_carry",
                "avg_strain",
                "avg_rekopplung",
            ],
            limit=18,
        )
    )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Wenn eine neue Welt keine alte Syntax wiederholt, aber eigene Syntaxfamilien in stabiler Feldklasse ausbildet, ist das ein anderer Reifeschritt: Nicht Erinnerung als Kopie, sondern neue Bedeutung aus ähnlicher Feldwirkung.",
            "",
            "Wichtig ist die Grenze: Diese Familien zeigen nur wiederkehrende Feldnähe innerhalb XRP. Erst wenn dieselben Familien oder verwandte Familien in weiteren Welten anschließen, entsteht daraus eine belastbarere Vorwahrnehmungsrolle.",
            "",
            "## Grenze",
            "",
            "Keine Handlung, keine Richtung, kein Gate. Die Auswertung beschreibt nur, ob Feldverfügbarkeit in neue Syntaxnähe übergeht.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte eine weitere nicht-XRP-Welt mit derselben Auswertung geprüft werden. Entscheidend ist, ob neue Syntaxfamilien feldstabil bleiben, sich teilen oder nur lokal an eine Welt gebunden sind.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def _parse_holdouts(raw_values: list[str]) -> dict[str, Path]:
    holdouts: dict[str, Path] = {}
    for raw in raw_values:
        if "=" not in raw:
            raise SystemExit(f"Ungültiges Holdout-Format: {raw}")
        label, path = raw.split("=", 1)
        holdouts[label.strip()] = Path(path.strip())
    return holdouts


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--holdout", action="append", required=True)
    parser.add_argument("--max-rows-per-holdout", type=int, default=20000)
    parser.add_argument("--out-prefix", default="2046_FELDKLASSEN_ZU_NEUER_SYNTAXNAEHE")
    args = parser.parse_args()

    all_rows: list[dict[str, object]] = []
    for label, root in _parse_holdouts(args.holdout).items():
        all_rows.extend(_read_episodes(label, root, args.max_rows_per_holdout))
    family_rows = _summarize_family(all_rows)
    bridge_rows = _build_bridge_rows(family_rows)

    out_prefix = BEFUNDE / args.out_prefix
    _write_csv(
        out_prefix.with_suffix(".families.csv"),
        family_rows,
        [
            "holdout_label",
            "symbol_family",
            "field_contact_class",
            "events",
            "distinct_symbols",
            "runs",
            "top_symbols",
            "avg_carry",
            "avg_strain",
            "avg_rekopplung",
        ],
    )
    _write_csv(
        out_prefix.with_suffix(".bridge.csv"),
        bridge_rows,
        [
            "symbol_family",
            "events",
            "holdout_labels",
            "dominant_field_contact_class",
            "dominant_field_share",
            "field_classes",
            "syntax_reifung",
            "avg_carry",
            "avg_strain",
            "avg_rekopplung",
        ],
    )
    _write_markdown(out_prefix.with_suffix(".md"), family_rows, bridge_rows)
    print(f"episode_rows={len(all_rows)}")
    print(f"families={len(family_rows)}")
    print(f"syntax_families={len(bridge_rows)}")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
