from __future__ import annotations

import argparse
import csv
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
    return f"{value:.6f}"


def _total_events(family_rows: list[dict[str, str]]) -> int:
    return sum(_safe_int(row.get("events")) for row in family_rows)


def _index(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {str(row.get("symbol_family", "-")): row for row in rows if row.get("symbol_family")}


def _contrast_class(ratio: float, real_events: int, null_events: int) -> str:
    if real_events <= 0 and null_events <= 0:
        return "nicht_sichtbar"
    if real_events > 0 and null_events <= 0:
        return "nur_real_sichtbar"
    if null_events > 0 and real_events <= 0:
        return "nur_null_sichtbar"
    if ratio >= 1.50:
        return "real_deutlich_staerker"
    if ratio >= 1.15:
        return "real_leicht_staerker"
    if ratio <= 0.67:
        return "null_deutlich_staerker"
    if ratio <= 0.87:
        return "null_leicht_staerker"
    return "balanciert"


def _build_rows(
    real_bridge: list[dict[str, str]],
    null_bridge: list[dict[str, str]],
    real_total: int,
    null_total: int,
    limit: int,
    include_families: set[str],
) -> list[dict[str, object]]:
    real_index = _index(real_bridge)
    null_index = _index(null_bridge)
    families = sorted(set(real_index) | set(null_index))
    rows: list[dict[str, object]] = []
    for family in families:
        real = real_index.get(family, {})
        null = null_index.get(family, {})
        real_events = _safe_int(real.get("events"))
        null_events = _safe_int(null.get("events"))
        real_share = real_events / max(1, real_total)
        null_share = null_events / max(1, null_total)
        ratio = real_share / null_share if null_share > 0 else (999.0 if real_share > 0 else 0.0)
        same_field = (
            real.get("dominant_field_contact_class")
            and null.get("dominant_field_contact_class")
            and real.get("dominant_field_contact_class") == null.get("dominant_field_contact_class")
        )
        rows.append(
            {
                "symbol_family": family,
                "contrast_class": _contrast_class(ratio, real_events, null_events),
                "real_events": real_events,
                "null_events": null_events,
                "real_share": real_share,
                "null_share": null_share,
                "real_null_ratio": ratio,
                "real_field": real.get("dominant_field_contact_class", "-"),
                "null_field": null.get("dominant_field_contact_class", "-"),
                "same_field": int(bool(same_field)),
                "real_reifung": real.get("syntax_reifung", "-"),
                "null_reifung": null.get("syntax_reifung", "-"),
                "real_mcm": (
                    f"{_safe_float(real.get('avg_carry')):.3f}/"
                    f"{_safe_float(real.get('avg_strain')):.3f}/"
                    f"{_safe_float(real.get('avg_rekopplung')):.3f}"
                    if real
                    else "-"
                ),
                "null_mcm": (
                    f"{_safe_float(null.get('avg_carry')):.3f}/"
                    f"{_safe_float(null.get('avg_strain')):.3f}/"
                    f"{_safe_float(null.get('avg_rekopplung')):.3f}"
                    if null
                    else "-"
                ),
                "boundary": "passive_multi_family_real_null_contrast_no_action_no_direction",
            }
        )
    rows.sort(key=lambda row: (-max(_safe_float(row["real_share"]), _safe_float(row["null_share"])), str(row["symbol_family"])))
    if limit <= 0:
        return rows
    selected = rows[:limit]
    selected_families = {str(row["symbol_family"]) for row in selected}
    for row in rows[limit:]:
        if str(row["symbol_family"]) in include_families and str(row["symbol_family"]) not in selected_families:
            selected.append(row)
            selected_families.add(str(row["symbol_family"]))
    return selected


def _write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            out = dict(row)
            for key in ["real_share", "null_share", "real_null_ratio"]:
                out[key] = _fmt(_safe_float(out.get(key)))
            writer.writerow({field: out.get(field, "") for field in fields})


def _md_table(rows: list[dict[str, object]], fields: list[str], limit: int = 30) -> list[str]:
    lines = ["| " + " | ".join(fields) + " |", "| " + " | ".join("---" for _ in fields) + " |"]
    for row in rows[:limit]:
        out = dict(row)
        for key in ["real_share", "null_share", "real_null_ratio"]:
            out[key] = _fmt(_safe_float(out.get(key)))
        lines.append("| " + " | ".join(str(out.get(field, "")) for field in fields) + " |")
    return lines


def _write_markdown(path: Path, rows: list[dict[str, object]], real_total: int, null_total: int) -> None:
    counts: dict[str, int] = {}
    for row in rows:
        counts[str(row["contrast_class"])] = counts.get(str(row["contrast_class"]), 0) + 1
    dio17 = next((row for row in rows if row.get("symbol_family") == "dio_17j2"), None)
    lines = [
        "# 2062 - Multirollen-Kontrast Real gegen Null/Shuffle",
        "",
        "## Zweck",
        "",
        "Diese Auswertung vergleicht mehrere Syntaxfamilien zwischen realen Multi-Asset-Welten und Null-/Shuffle-Kontrollwelten.",
        "",
        "Die Prüfung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung, kein Gate und keinen motorischen Impuls.",
        "",
        "## Übersicht",
        "",
        f"- Real-Ereignisse gesamt: `{real_total}`",
        f"- Null-/Shuffle-Ereignisse gesamt: `{null_total}`",
        f"- geprüfte Rollen im Report: `{len(rows)}`",
        f"- Kontrastklassen: `{dict(sorted(counts.items()))}`",
        "",
    ]
    if dio17:
        lines.extend(
            [
                "## Einordnung von dio_17j2",
                "",
                f"- Klasse: `{dio17['contrast_class']}`",
                f"- Real-Anteil: `{_fmt(_safe_float(dio17['real_share']))}`",
                f"- Null-/Shuffle-Anteil: `{_fmt(_safe_float(dio17['null_share']))}`",
                f"- Verhältnis Real zu Null/Shuffle: `{_safe_float(dio17['real_null_ratio']):.3f}`",
                "",
            ]
        )
    lines.extend(["## Stärkste Rollen nach Anteil", ""])
    fields = [
        "symbol_family",
        "contrast_class",
        "real_events",
        "null_events",
        "real_share",
        "null_share",
        "real_null_ratio",
        "real_field",
        "null_field",
        "same_field",
    ]
    lines.extend(_md_table(rows, fields, limit=35))
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Wenn viele starke Rollen im Kontrollraum ähnlich stark erscheinen, ist das ein Hinweis auf feldinterne Grundformen. Dann ist nicht jede stabile Rolle automatisch realwelt-spezifisch.",
            "",
            "Interessant sind Rollen, die im Realraum deutlich stärker sind, im Kontrollraum aber nicht verschwinden. Das deutet auf eine Grundform hin, die durch reale Weltordnung zusätzlich aktiviert wird.",
            "",
            "## Grenze",
            "",
            "Die Klassierung ist eine diagnostische Lesung, keine Regel im Organismus. Sie dient nur dazu, Realweltbindung und feldinterne Grundform auseinanderzuhalten.",
            "",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--real-bridge", default="docs/befunde/2001-3000/2057_MULTI_ASSET_FELDKLASSEN_ZU_SYNTAXNAEHE.bridge.csv")
    parser.add_argument("--real-families", default="docs/befunde/2001-3000/2057_MULTI_ASSET_FELDKLASSEN_ZU_SYNTAXNAEHE.families.csv")
    parser.add_argument("--null-bridge", default="docs/befunde/2001-3000/2059_NULL_SHUFFLE_FELDKLASSEN_ZU_SYNTAXNAEHE.bridge.csv")
    parser.add_argument("--null-families", default="docs/befunde/2001-3000/2059_NULL_SHUFFLE_FELDKLASSEN_ZU_SYNTAXNAEHE.families.csv")
    parser.add_argument("--out-prefix", default="2062_MULTIROLLEN_REAL_NULL_KONTRAST")
    parser.add_argument("--limit", type=int, default=200)
    parser.add_argument("--include-family", action="append", default=["dio_17j2"])
    args = parser.parse_args()

    real_family_rows = _load_csv(Path(args.real_families))
    null_family_rows = _load_csv(Path(args.null_families))
    real_total = _total_events(real_family_rows)
    null_total = _total_events(null_family_rows)
    rows = _build_rows(
        _load_csv(Path(args.real_bridge)),
        _load_csv(Path(args.null_bridge)),
        real_total,
        null_total,
        args.limit,
        set(args.include_family or []),
    )
    fields = [
        "symbol_family",
        "contrast_class",
        "real_events",
        "null_events",
        "real_share",
        "null_share",
        "real_null_ratio",
        "real_field",
        "null_field",
        "same_field",
        "real_reifung",
        "null_reifung",
        "real_mcm",
        "null_mcm",
        "boundary",
    ]
    _write_csv(BEFUNDE / f"{args.out_prefix}.csv", rows, fields)
    _write_markdown(BEFUNDE / f"{args.out_prefix}.md", rows, real_total, null_total)
    print(f"rows={len(rows)}")
    print(f"real_total={real_total}")
    print(f"null_total={null_total}")
    print(f"wrote={BEFUNDE / (args.out_prefix + '.md')}")


if __name__ == "__main__":
    main()
