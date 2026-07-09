from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

from update_mcm_field_role_memory import ROOT, _float


SOURCE_CSV = ROOT / "docs/befunde/1854_FAMILIEN_ANSCHLUSSKARTE_REPRO_NEUE_WELTEN.csv"
WINDOW_CSV = ROOT / "docs/befunde/1853_FAMILIEN_ANSCHLUSSKARTE_NEUE_WELTEN.csv"
OUT_CSV = ROOT / "docs/befunde/1855_FAMILIEN_ANSCHLUSSKARTE_DRIFTQUELLEN.csv"
OUT_MD = ROOT / "docs/befunde/1855_FAMILIEN_ANSCHLUSSKARTE_DRIFTQUELLEN.md"


def _read(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


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


def _profile(counter: Counter[str]) -> str:
    return "; ".join(f"{name}:{count}" for name, count in counter.most_common()) or "-"


def _drift_source(row: dict[str, str]) -> str:
    baseline = str(row.get("baseline_attachment_quality") or "")
    follow = str(row.get("dominant_attachment_quality") or "")
    if baseline == "neu_ohne_baseline":
        return "neue_familienlage"
    if baseline == follow:
        return "reproduktion"
    if baseline == "offen_gemischt" and follow != "offen_gemischt":
        return "baseline_offen_wird_spezifisch"
    if baseline != "offen_gemischt" and follow == "offen_gemischt":
        return "spezifisch_wird_offen"
    if baseline == "nachhallnah_ohne_kern" and follow == "kernnah":
        return "nachhall_wird_kernnah"
    if baseline == "kernnah" and follow == "nullnah":
        return "kernnah_wird_nullnah"
    if baseline == "kernnah_ohne_feldzeit" and follow == "nullnah":
        return "kern_ohne_feldzeit_wird_nullnah"
    return "spezifische_qualitaet_driftet"


def build_rows() -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    source_rows = [row for row in _read(SOURCE_CSV) if row.get("row_type") == "asset_family_repro"]
    window_rows = [row for row in _read(WINDOW_CSV) if row.get("row_type") == "window_summary"]

    detailed: list[dict[str, object]] = []
    for row in source_rows:
        detailed.append(
            {
                "row_type": "drift_detail",
                "asset": str(row.get("asset") or ""),
                "family": str(row.get("family") or ""),
                "baseline_attachment_quality": str(row.get("baseline_attachment_quality") or ""),
                "followup_attachment_quality": str(row.get("dominant_attachment_quality") or ""),
                "repro_state": str(row.get("repro_state") or ""),
                "drift_source": _drift_source(row),
                "attachment_profile": str(row.get("attachment_profile") or ""),
                "mean_field_edge_score": round(_float(row.get("mean_field_edge_score")), 6),
            }
        )

    source_counts = Counter(str(row["drift_source"]) for row in detailed)
    asset_source_counts = Counter(f"{row['asset']}::{row['drift_source']}" for row in detailed)
    transition_counts = Counter(
        f"{row['baseline_attachment_quality']}->{row['followup_attachment_quality']}" for row in detailed
    )
    window_readings = Counter(str(row.get("reading") or "") for row in window_rows)

    summary = [
        {
            "row_type": "summary",
            "asset_family_pairs": len(detailed),
            "drift_sources": _profile(source_counts),
            "quality_transitions": _profile(transition_counts),
            "asset_drift_sources": _profile(asset_source_counts),
            "window_readings": _profile(window_readings),
            "mean_window_field_edge": round(
                sum(_float(row.get("field_edge_score")) for row in window_rows) / max(1, len(window_rows)),
                6,
            ),
        }
    ]
    source_rows_out = [
        {
            "row_type": "drift_source_summary",
            "drift_source": name,
            "count": count,
            "share": round(count / max(1, len(detailed)), 6),
        }
        for name, count in source_counts.most_common()
    ]
    return summary, source_rows_out, detailed


def write_md(summary: list[dict[str, object]], source_rows: list[dict[str, object]], details: list[dict[str, object]]) -> None:
    item = summary[0]
    top_by_source: dict[str, list[dict[str, object]]] = {}
    for row in details:
        top_by_source.setdefault(str(row["drift_source"]), []).append(row)
    lines = [
        "# 1855 - Driftquellen der Familien-Anschlusskarte",
        "",
        "## Grundfrage",
        "",
        "Kommt die offene Drift aus neuer Weltspannung, oder war die Baseline selbst zu breit gemischt?",
        "",
        "## Methode",
        "",
        "- Quelle: `1854` Asset/Familien-Reproduktionsvergleich.",
        "- Jede Veränderung wird als Driftquelle klassifiziert.",
        "- Es bleibt eine passive Lesung ohne Handlung, Gate oder Richtung.",
        "",
        "## Kurzbefund",
        "",
        f"- Asset/Familien-Paare: `{item['asset_family_pairs']}`",
        f"- Driftquellen: `{item['drift_sources']}`",
        f"- Qualitätsübergänge: `{item['quality_transitions']}`",
        f"- Fensterlesungen: `{item['window_readings']}`",
        "",
        "## Driftquellen",
        "",
        "| Driftquelle | Paare | Anteil |",
        "|---|---:|---:|",
    ]
    for row in source_rows:
        lines.append(f"| `{row['drift_source']}` | {row['count']} | {_float(row['share']):.3f} |")
    lines.extend(
        [
            "",
            "## Beispiele",
            "",
            "| Driftquelle | Asset | Familie | Baseline | Folge | Profil |",
            "|---|---|---|---|---|---|",
        ]
    )
    for source_name, rows in top_by_source.items():
        for row in rows[:5]:
            lines.append(
                f"| `{source_name}` | {row['asset']} | `{row['family']}` | "
                f"`{row['baseline_attachment_quality']}` | `{row['followup_attachment_quality']}` | "
                f"`{row['attachment_profile']}` |"
            )
    lines.extend(
        [
            "",
            "## Einordnung",
            "",
            "Die Drift ist nicht einheitlich.",
            "",
            "- Der größte Block ist `baseline_offen_wird_spezifisch`: eine zuvor offene Baseline wird in neuen Fenstern konkreter.",
            "- Der zweite Block ist `spezifisch_wird_offen`: eine zuvor spezifische Qualität verliert im neuen Kontext ihre Schärfe.",
            "- BTC zeigt einen eigenen geschlossenen Übergang: `nachhallnah_ohne_kern -> kernnah`.",
            "",
            "Damit liegt der Engpass nicht nur in der neuen Weltspannung.",
            "Ein Teil der Drift kommt wahrscheinlich daher, dass die ursprüngliche Baseline noch zu breit gemischt war.",
            "Ein anderer Teil ist echte Kontextdrift: dieselbe Familie wird unter anderer Weltspannung anders angeschlossen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte die Baseline enger gebaut werden: nicht nur Asset/Familie, sondern Asset/Familie/Fensterphase.",
            "Dann lässt sich prüfen, ob offene Drift sinkt und echte Kontextdrift klarer übrig bleibt.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    summary, source_rows, details = build_rows()
    _write_csv(OUT_CSV, summary + source_rows + details)
    write_md(summary, source_rows, details)
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"wrote {OUT_CSV.relative_to(ROOT)}")
    print(summary[0])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
