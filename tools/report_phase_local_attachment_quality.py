from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

from update_mcm_field_role_memory import ROOT, _attachment_quality, _float


SOURCES = [
    ROOT / "docs/befunde/1001-2000/1751-2000/1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv",
    ROOT / "docs/befunde/1001-2000/1751-2000/1848_ANSCHLUSSQUALITAET_NEUE_FENSTER.csv",
    ROOT / "docs/befunde/1001-2000/1751-2000/1853_FAMILIEN_ANSCHLUSSKARTE_NEUE_WELTEN.csv",
]
OUT_CSV = ROOT / "docs/befunde/1001-2000/1751-2000/1857_PHASENLOKALE_ANSCHLUSSQUALITAET.csv"
OUT_MD = ROOT / "docs/befunde/1001-2000/1751-2000/1857_PHASENLOKALE_ANSCHLUSSQUALITAET.md"

PHASES = ("frueh", "mitte", "spaet")
METRICS = ("share", "rekopplung", "strain", "afterimage", "temporal")


def _read(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        row["source_report"] = str(path.relative_to(ROOT))
    return rows


def _read_all() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in SOURCES:
        rows.extend(_read(path))
    return rows


def _profile(counter: Counter[str]) -> str:
    return "; ".join(f"{name}:{count}" for name, count in counter.most_common()) or "-"


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames: list[str] = []
    seen: set[str] = set()
    for row in rows:
        for key in row:
            if key not in seen:
                seen.add(key)
                fieldnames.append(key)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _window_quality(rows: list[dict[str, str]]) -> dict[tuple[str, str, int], str]:
    out: dict[tuple[str, str, int], str] = {}
    for row in rows:
        if row.get("row_type") != "window_summary":
            continue
        key = (
            str(row.get("source_report") or ""),
            str(row.get("asset") or ""),
            int(_float(row.get("window_start"))),
        )
        out[key] = _attachment_quality(str(row.get("reading") or ""))
    return out


def _phase_value(row: dict[str, str], metric: str, phase: str) -> float:
    return _float(row.get(f"{metric}_{phase}"))


def _phase_count(row: dict[str, str], phase: str) -> int:
    return int(_float(row.get(f"count_{phase}")))


def _null_reference(null_rows: list[dict[str, str]], phase: str) -> dict[str, object]:
    if not null_rows:
        return {
            "null_count": 0,
            "null_kinds": "",
            "null_share": 0.0,
            "null_rekopplung": 0.0,
            "null_strain": 0.0,
            "null_afterimage": 0.0,
            "null_temporal": 0.0,
        }
    active = [row for row in null_rows if _phase_count(row, phase) > 0]
    if not active:
        active = null_rows
    return {
        "null_count": len(active),
        "null_kinds": ";".join(sorted({str(row.get("kind") or "") for row in active})),
        "null_share": max(_phase_value(row, "share", phase) for row in active),
        "null_rekopplung": max(_phase_value(row, "rekopplung", phase) for row in active),
        "null_strain": min(_phase_value(row, "strain", phase) for row in active),
        "null_afterimage": max(_phase_value(row, "afterimage", phase) for row in active),
        "null_temporal": max(_phase_value(row, "temporal", phase) for row in active),
    }


def _phase_quality(edges: dict[str, float], has_null: bool) -> str:
    if not has_null:
        return "phase_ohne_nullfamilie"
    share = edges["share_edge"]
    rekopplung = edges["rekopplung_edge"]
    afterimage = edges["afterimage_edge"]
    temporal = edges["temporal_edge"]
    if share > 0.0 and rekopplung >= 0.0 and temporal >= 0.0:
        return "phase_kernnah"
    if afterimage > 0.0 and temporal > 0.0 and share <= 0.0:
        return "phase_nachhallnah_ohne_kern"
    if share <= 0.0 and rekopplung <= 0.0 and temporal <= 0.0:
        return "phase_nullnah"
    return "phase_offen_gemischt"


def build_rows() -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    rows = _read_all()
    inherited_quality = _window_quality(rows)
    details = [row for row in rows if row.get("row_type") == "detail"]
    null_index: dict[tuple[str, str, int, str], list[dict[str, str]]] = defaultdict(list)
    for row in details:
        if row.get("kind") == "real":
            continue
        key = (
            str(row.get("source_report") or ""),
            str(row.get("asset") or ""),
            int(_float(row.get("window_start"))),
            str(row.get("family") or ""),
        )
        null_index[key].append(row)

    out: list[dict[str, object]] = []
    for row in details:
        if row.get("kind") != "real":
            continue
        source = str(row.get("source_report") or "")
        asset = str(row.get("asset") or "")
        window_start = int(_float(row.get("window_start")))
        family = str(row.get("family") or "")
        null_rows = null_index.get((source, asset, window_start, family), [])
        inherited = inherited_quality.get((source, asset, window_start), "")
        for phase in PHASES:
            count = _phase_count(row, phase)
            if count <= 0:
                continue
            null_ref = _null_reference(null_rows, phase)
            edges = {
                "share_edge": _phase_value(row, "share", phase) - _float(null_ref["null_share"]),
                "rekopplung_edge": _phase_value(row, "rekopplung", phase) - _float(null_ref["null_rekopplung"]),
                "strain_edge": _phase_value(row, "strain", phase) - _float(null_ref["null_strain"]),
                "afterimage_edge": _phase_value(row, "afterimage", phase) - _float(null_ref["null_afterimage"]),
                "temporal_edge": _phase_value(row, "temporal", phase) - _float(null_ref["null_temporal"]),
            }
            quality = _phase_quality(edges, bool(null_rows))
            out.append(
                {
                    "row_type": "phase_local_detail",
                    "source_report": source,
                    "asset": asset,
                    "window_start": window_start,
                    "family": family,
                    "phase": phase,
                    "phase_local_quality": quality,
                    "inherited_window_quality": inherited,
                    "family_reading": str(row.get("family_reading") or ""),
                    "dominant_role": str(row.get("dominant_role") or ""),
                    "count": count,
                    "share": _phase_value(row, "share", phase),
                    "rekopplung": _phase_value(row, "rekopplung", phase),
                    "strain": _phase_value(row, "strain", phase),
                    "afterimage": _phase_value(row, "afterimage", phase),
                    "temporal": _phase_value(row, "temporal", phase),
                    **null_ref,
                    **{key: round(value, 9) for key, value in edges.items()},
                    "quality_matches_window": quality.replace("phase_", "") == inherited,
                }
            )

    quality_counts = Counter(str(row["phase_local_quality"]) for row in out)
    inherited_counts = Counter(str(row["inherited_window_quality"]) for row in out)
    transition_counts = Counter(
        f"{row['inherited_window_quality']}->{row['phase_local_quality']}" for row in out
    )
    phase_counts = Counter(f"{row['phase']}::{row['phase_local_quality']}" for row in out)
    asset_counts = Counter(f"{row['asset']}::{row['phase_local_quality']}" for row in out)
    match_count = sum(1 for row in out if row["quality_matches_window"])
    summary = [
        {
            "row_type": "summary",
            "sources": "; ".join(str(path.relative_to(ROOT)) for path in SOURCES),
            "phase_rows": len(out),
            "phase_local_quality": _profile(quality_counts),
            "inherited_window_quality": _profile(inherited_counts),
            "window_to_phase_transitions": _profile(transition_counts),
            "phase_profile": _profile(phase_counts),
            "asset_profile": _profile(asset_counts),
            "quality_matches_window": match_count,
            "quality_differs_from_window": len(out) - match_count,
        }
    ]
    quality_rows = [
        {
            "row_type": "phase_quality_summary",
            "phase_local_quality": name,
            "count": count,
            "share": round(count / max(1, len(out)), 6),
        }
        for name, count in quality_counts.most_common()
    ]
    return summary, quality_rows, out


def write_md(summary: list[dict[str, object]], quality_rows: list[dict[str, object]], details: list[dict[str, object]]) -> None:
    item = summary[0]
    sample = details[:24]
    lines = [
        "# 1857 - Phasenlokale Anschlussqualität",
        "",
        "## Grundfrage",
        "",
        "Was passiert, wenn Anschlussqualität nicht mehr vom Gesamtfenster geerbt wird, sondern pro Phase gegen passende Nullwelt-Phasen gelesen wird?",
        "",
        "## Methode",
        "",
        f"- Quellen: `{item['sources']}`.",
        "- Realwelt-Phase wird gegen `null_random` und `null_shuffle` derselben Quelle, desselben Assets, desselben Fensters und derselben Familie gelesen.",
        "- Die Klassifikation ist ein Diagnose-Bucket, keine Feldregel und keine Handlungsschicht.",
        "- Positive Größen werden gegen die stärkste Nullreferenz gelesen; Strain wird gegen die niedrigste Nullreferenz protokolliert.",
        "",
        "## Kurzbefund",
        "",
        f"- Phasenzeilen: `{item['phase_rows']}`",
        f"- Phasenlokale Qualitäten: `{item['phase_local_quality']}`",
        f"- Geerbte Fensterqualitäten: `{item['inherited_window_quality']}`",
        f"- Fenster-zu-Phase-Übergänge: `{item['window_to_phase_transitions']}`",
        f"- Qualität gleich Fenster: `{item['quality_matches_window']}`",
        f"- Qualität anders als Fenster: `{item['quality_differs_from_window']}`",
        "",
        "## Phasenlokale Zustände",
        "",
        "| Zustand | Zeilen | Anteil |",
        "|---|---:|---:|",
    ]
    for row in quality_rows:
        lines.append(f"| `{row['phase_local_quality']}` | {row['count']} | {_float(row['share']):.3f} |")
    lines.extend(
        [
            "",
            "## Beispielzeilen",
            "",
            "| Quelle | Asset | Familie | Phase | Fenster | Phase lokal | Geerbt | Share-Edge | Rekopplung-Edge | Temporal-Edge |",
            "|---|---|---|---|---:|---|---|---:|---:|---:|",
        ]
    )
    for row in sample:
        lines.append(
            f"| `{row['source_report']}` | {row['asset']} | `{row['family']}` | `{row['phase']}` | "
            f"{row['window_start']} | `{row['phase_local_quality']}` | `{row['inherited_window_quality']}` | "
            f"{_float(row['share_edge']):.4f} | {_float(row['rekopplung_edge']):.4f} | {_float(row['temporal_edge']):.4f} |"
        )
    lines.extend(
        [
            "",
            "## Einordnung",
            "",
            "Diese Prüfung trennt erstmals die Frage `Welche Qualität trägt das Fenster?` von `Welche Qualität trägt diese Familie in dieser Phase?`.",
            "Damit wird sichtbar, ob eine Familie nur durch die Gesamtwelt mitgezogen wird oder ob sie lokal in Früh-, Mittel- oder Spätphase selbst Anschluss trägt.",
            "",
            "Wenn die phasenlokale Qualität deutlich von der Fensterqualität abweicht, ist das kein Fehler, sondern ein Hinweis auf mehrdimensionale Feldlesung:",
            "Fenster, Familie und Phase tragen nicht automatisch dieselbe Bedeutung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte geprüft werden, welche Familien phasenlokal stabil bleiben und welche nur durch die Fensterqualität mitgezogen wurden.",
            "Daraus lässt sich eine sauberere passive Bedeutungsreife ableiten: Familie + Phase + Nullwelt-Abstand statt Familie + Fenster allein.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    summary, quality_rows, details = build_rows()
    _write_csv(OUT_CSV, summary + quality_rows + details)
    write_md(summary, quality_rows, details)
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"wrote {OUT_CSV.relative_to(ROOT)}")
    print(summary[0])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
