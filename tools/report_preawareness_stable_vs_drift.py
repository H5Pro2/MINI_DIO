from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path

from befunde_paths import befunde_root
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = befunde_root(ROOT)
DEFAULT_SOURCE = BEFUNDE / "2041_VORWAHRNEHMUNG_MEMORY_HOLDOUT_RUECKPRUEFUNG.summary.csv"
DEFAULT_OUT_PREFIX = BEFUNDE / "2042_VORWAHRNEHMUNG_STABIL_DRIFT_LANDKARTE"


def _load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists() or path.stat().st_size <= 0:
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _fmt(value: float) -> str:
    return f"{value:.3f}"


def _relation(expected: str, observed: str) -> str:
    if expected == observed:
        return "feldrolle_identisch"
    if expected == "spannungsnahe_oeffnung" and "rekopplung" in observed:
        return "spannung_rekoppelt_um"
    if "rekopplung" in expected and "rekopplung" in observed:
        return "rekopplungsqualitaet_verschoben"
    if expected.startswith("getragen") and "rekopplung" in observed:
        return "tragung_rekoppelt_um"
    return "offene_felddrift"


def _landkarte_class(row: dict[str, str]) -> str:
    expected = row.get("expected_field_contact_class", "-")
    observed = row.get("observed_field_contact_class", "-")
    field = _safe_float(row.get("field_recall_share"))
    sensory = _safe_float(row.get("sensory_recall_share"))
    motion = _safe_float(row.get("motion_recall_share"))
    relation = _relation(expected, observed)

    if expected == observed and field >= 0.75:
        return "stabil_wiederkehrend"
    if expected == observed:
        return "teilstabil_wiederkehrend"
    if relation == "spannung_rekoppelt_um":
        return "umorganisierte_rekopplung"
    if relation == "rekopplungsqualitaet_verschoben":
        return "verschobene_rekopplungsqualitaet"
    if field <= 0.25 and motion <= 0.25 and sensory >= 0.5:
        return "sinnesnah_felddriftend"
    if field <= 0.25:
        return "offen_driftend"
    return "offene_umordnung"


def _classification_rows(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for row in rows:
        expected = row.get("expected_field_contact_class", "-")
        observed = row.get("observed_field_contact_class", "-")
        out.append(
            {
                "target_group": row.get("target_group", "-"),
                "source_chain": row.get("source_chain", "-"),
                "holdout_label": row.get("holdout_label", "-"),
                "holdout_asset": row.get("holdout_asset", "-"),
                "events": row.get("events", "0"),
                "expected_field_contact_class": expected,
                "observed_field_contact_class": observed,
                "field_relation": _relation(expected, observed),
                "landkarte_class": _landkarte_class(row),
                "field_recall_share": _safe_float(row.get("field_recall_share")),
                "sensory_recall_share": _safe_float(row.get("sensory_recall_share")),
                "motion_recall_share": _safe_float(row.get("motion_recall_share")),
                "avg_carry": _safe_float(row.get("avg_carry")),
                "avg_strain": _safe_float(row.get("avg_strain")),
                "avg_rekopplung": _safe_float(row.get("avg_rekopplung")),
                "symbols": row.get("symbols", ""),
                "observed_sensory_classes": row.get("observed_sensory_classes", ""),
                "observed_motion_classes": row.get("observed_motion_classes", ""),
            }
        )
    return out


def _aggregate(rows: list[dict[str, object]], fields: list[str]) -> list[dict[str, object]]:
    buckets: dict[tuple[object, ...], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        buckets[tuple(row.get(field, "-") for field in fields)].append(row)

    out: list[dict[str, object]] = []
    for key, bucket in sorted(buckets.items()):
        item: dict[str, object] = {field: value for field, value in zip(fields, key)}
        item["rows"] = len(bucket)
        item["events"] = sum(int(float(row.get("events", 0) or 0)) for row in bucket)
        item["avg_field_recall"] = mean(_safe_float(row.get("field_recall_share")) for row in bucket)
        item["avg_sensory_recall"] = mean(_safe_float(row.get("sensory_recall_share")) for row in bucket)
        item["avg_motion_recall"] = mean(_safe_float(row.get("motion_recall_share")) for row in bucket)
        item["avg_carry"] = mean(_safe_float(row.get("avg_carry")) for row in bucket)
        item["avg_strain"] = mean(_safe_float(row.get("avg_strain")) for row in bucket)
        item["avg_rekopplung"] = mean(_safe_float(row.get("avg_rekopplung")) for row in bucket)
        classes = Counter(str(row.get("landkarte_class", "-")) for row in bucket)
        relations = Counter(str(row.get("field_relation", "-")) for row in bucket)
        item["landkarte_classes"] = ";".join(f"{name}:{count}" for name, count in classes.most_common())
        item["field_relations"] = ";".join(f"{name}:{count}" for name, count in relations.most_common())
        out.append(item)
    return out


def _md_table(rows: list[dict[str, object]], fields: list[str], limit: int | None = None) -> list[str]:
    selected = rows[:limit] if limit else rows
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


def _write_markdown(
    out_prefix: Path,
    rows: list[dict[str, object]],
    class_summary: list[dict[str, object]],
    group_summary: list[dict[str, object]],
    source_path: Path,
) -> None:
    total_events = sum(int(float(row.get("events", 0) or 0)) for row in rows)
    avg_field = mean(_safe_float(row.get("field_recall_share")) for row in rows) if rows else 0.0
    avg_sensory = mean(_safe_float(row.get("sensory_recall_share")) for row in rows) if rows else 0.0
    avg_motion = mean(_safe_float(row.get("motion_recall_share")) for row in rows) if rows else 0.0
    class_counts = Counter(str(row.get("landkarte_class", "-")) for row in rows)
    stable_rows = class_counts["stabil_wiederkehrend"] + class_counts["teilstabil_wiederkehrend"]
    drift_rows = len(rows) - stable_rows

    lines: list[str] = [
        "# Vorwahrnehmung: stabile Wiederkehr, Drift und Umorganisation",
        "",
        "Diese Auswertung liest die Holdout-Rückprüfung aus 2041 passiv weiter. Ziel ist nicht Handlung, sondern eine Landkarte: Welche Vorwahrnehmungsrollen kehren stabil wieder, welche verschieben ihre Feldqualität, und welche organisieren sich unter neuer Weltspannung um?",
        "",
        "## Kurzbefund",
        "",
        f"- Quelle: `{source_path}`",
        f"- Ausgewertete Zeilen: {len(rows)}",
        f"- Ausgewertete Ereignisse: {total_events}",
        f"- Durchschnittliche Feld-Rücklesung: {_fmt(avg_field)}",
        f"- Durchschnittliche Sinnes-Rücklesung: {_fmt(avg_sensory)}",
        f"- Durchschnittliche Rohbewegungs-Rücklesung: {_fmt(avg_motion)}",
        f"- Stabile/teilstabile Zeilen: {stable_rows}",
        f"- Driftende oder umorganisierte Zeilen: {drift_rows}",
        "",
        "Die Rohbewegung bleibt deutlich schwächer rücklesbar als Feld- und Sinnesnähe. Das spricht gegen eine reine Kopie der Oberfläche und für eine passive Feldnähe-Landkarte.",
        "",
        "## Klassen",
        "",
    ]
    lines.extend(
        _md_table(
            class_summary,
            [
                "landkarte_class",
                "rows",
                "events",
                "avg_field_recall",
                "avg_sensory_recall",
                "avg_motion_recall",
                "avg_carry",
                "avg_strain",
                "avg_rekopplung",
            ],
        )
    )
    lines.extend(
        [
            "",
            "## Gruppenlesung",
            "",
        ]
    )
    lines.extend(
        _md_table(
            group_summary,
            [
                "target_group",
                "source_chain",
                "rows",
                "events",
                "avg_field_recall",
                "avg_sensory_recall",
                "avg_motion_recall",
                "landkarte_classes",
            ],
        )
    )
    lines.extend(
        [
            "",
            "## Fachliche Lesung",
            "",
            "- `oberflaeche_rekoppelt_spaet` bleibt über DOGE und PAXG besonders stabil. Die Oberfläche ist anders, aber die offene Rekopplungsrolle bleibt lesbar.",
            "- `rekopplung_oeffnet` bleibt bei BTC und DOGE spannungsnah wiederkehrend, kippt bei PAXG aber in `offene_rekopplung`. Das ist keine einfache Loeschung, sondern eine Umorganisation der Feldrolle.",
            "- `oberflaeche_rekoppelt` zeigt zwischen BTC, DOGE und Multiasset eine Verschiebung der Rekopplungsqualität. Das Feld erkennt Nähe, aber die Tragqualität ist nicht identisch.",
            "- Die niedrige Rohbewegungs-Rücklesung zeigt: Die Vorwahrnehmung hängt nicht primär an identischen Kursbewegungen, sondern an wiederkehrender Feld- und Sinnesnähe.",
            "",
            "## Grenze",
            "",
            "Diese Landkarte ist passiv. Sie erzeugt keine Handlung, keine Richtung, keinen Entry und kein Gate. Sie beschreibt nur, ob eine frühere Feldnähe in einer neuen Welt stabil, verschoben oder umorganisiert wieder auftaucht.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte diese Landkarte in die passive Vorwahrnehmungs-Memory als Zustandsqualität zurückgeschrieben werden: `stabil`, `teilstabil`, `umorganisiert`, `driftend`. Danach ein weiterer Holdout mit anderer Weltspannung, ohne Handlung und ohne harte Regeln.",
            "",
        ]
    )
    out_prefix.with_suffix(".md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(DEFAULT_SOURCE))
    parser.add_argument("--out-prefix", default=str(DEFAULT_OUT_PREFIX))
    args = parser.parse_args()

    source_path = Path(args.source)
    if not source_path.is_absolute():
        source_path = ROOT / source_path
    out_prefix = Path(args.out_prefix)
    if not out_prefix.is_absolute():
        out_prefix = ROOT / out_prefix

    source_rows = _load_csv(source_path)
    rows = _classification_rows(source_rows)

    detail_fields = [
        "target_group",
        "source_chain",
        "holdout_label",
        "holdout_asset",
        "events",
        "expected_field_contact_class",
        "observed_field_contact_class",
        "field_relation",
        "landkarte_class",
        "field_recall_share",
        "sensory_recall_share",
        "motion_recall_share",
        "avg_carry",
        "avg_strain",
        "avg_rekopplung",
        "symbols",
        "observed_sensory_classes",
        "observed_motion_classes",
    ]
    _write_csv(out_prefix.with_suffix(".detail.csv"), rows, detail_fields)

    class_summary = _aggregate(rows, ["landkarte_class"])
    group_summary = _aggregate(rows, ["target_group", "source_chain"])

    summary_fields = [
        "landkarte_class",
        "rows",
        "events",
        "avg_field_recall",
        "avg_sensory_recall",
        "avg_motion_recall",
        "avg_carry",
        "avg_strain",
        "avg_rekopplung",
        "field_relations",
    ]
    _write_csv(out_prefix.with_suffix(".classes.csv"), class_summary, summary_fields)

    group_fields = [
        "target_group",
        "source_chain",
        "rows",
        "events",
        "avg_field_recall",
        "avg_sensory_recall",
        "avg_motion_recall",
        "avg_carry",
        "avg_strain",
        "avg_rekopplung",
        "landkarte_classes",
        "field_relations",
    ]
    _write_csv(out_prefix.with_suffix(".groups.csv"), group_summary, group_fields)
    _write_markdown(out_prefix, rows, class_summary, group_summary, source_path)

    print(f"written {out_prefix.name}.*")


if __name__ == "__main__":
    main()
