from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

from report_family_attachment_quality import _dominant, _mean, _profile, _profile_state
from update_mcm_field_role_memory import ROOT, _attachment_quality, _float


BASELINE_CSV = ROOT / "docs/befunde/1001-2000/1751-2000/1851_FAMILIEN_ANSCHLUSSQUALITAET.csv"
FOLLOWUP_CSV = ROOT / "docs/befunde/1001-2000/1751-2000/1853_FAMILIEN_ANSCHLUSSKARTE_NEUE_WELTEN.csv"
OUT_CSV = ROOT / "docs/befunde/1001-2000/1751-2000/1854_FAMILIEN_ANSCHLUSSKARTE_REPRO_NEUE_WELTEN.csv"
OUT_MD = ROOT / "docs/befunde/1001-2000/1751-2000/1854_FAMILIEN_ANSCHLUSSKARTE_REPRO_NEUE_WELTEN.md"


def _read_rows(path: Path) -> list[dict[str, str]]:
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


def _baseline_asset_family(rows: list[dict[str, str]]) -> dict[tuple[str, str], dict[str, str]]:
    out: dict[tuple[str, str], dict[str, str]] = {}
    for row in rows:
        if row.get("row_type") != "asset_family_attachment_summary":
            continue
        out[(str(row.get("asset") or ""), str(row.get("family") or ""))] = row
    return out


def _window_quality(rows: list[dict[str, str]]) -> dict[tuple[str, int], dict[str, object]]:
    out: dict[tuple[str, int], dict[str, object]] = {}
    for row in rows:
        if row.get("row_type") != "window_summary":
            continue
        asset = str(row.get("asset") or "")
        window_start = int(_float(row.get("window_start")))
        reading = str(row.get("reading") or "")
        out[(asset, window_start)] = {
            "attachment_quality": _attachment_quality(reading),
            "source_reading": reading,
            "field_edge_score": _float(row.get("field_edge_score")),
            "kern_edge": _float(row.get("kern_edge")),
            "afterimage_edge": _float(row.get("afterimage_edge")),
            "temporal_edge": _float(row.get("temporal_edge")),
        }
    return out


def _followup_asset_family(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    qualities = _window_quality(rows)
    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        if row.get("row_type") != "detail" or row.get("kind") != "real":
            continue
        asset = str(row.get("asset") or "")
        family = str(row.get("family") or "")
        window_start = int(_float(row.get("window_start")))
        quality = qualities.get((asset, window_start), {})
        grouped[(asset, family)].append(
            {
                "asset": asset,
                "family": family,
                "window_start": window_start,
                "family_reading": str(row.get("family_reading") or ""),
                "dominant_role": str(row.get("dominant_role") or ""),
                "total_count": int(_float(row.get("total_count"))),
                **quality,
            }
        )

    out: list[dict[str, object]] = []
    for (asset, family), items in grouped.items():
        counts = Counter(str(item.get("attachment_quality") or "-") for item in items)
        dominant, dominant_count, second, second_count, gap = _dominant(counts)
        out.append(
            {
                "asset": asset,
                "family": family,
                "appearances": len(items),
                "dominant_attachment_quality": dominant,
                "dominant_attachment_count": dominant_count,
                "second_attachment_quality": second,
                "second_attachment_count": second_count,
                "attachment_quality_gap": gap,
                "attachment_profile_state": _profile_state(len(items), gap),
                "attachment_profile": _profile(counts),
                "mean_total_count": round(_mean([_float(item.get("total_count")) for item in items]), 6),
                "mean_field_edge_score": round(_mean([_float(item.get("field_edge_score")) for item in items]), 6),
            }
        )
    out.sort(
        key=lambda row: (
            str(row["asset"]),
            -int(row["appearances"]),
            -int(row["attachment_quality_gap"]),
            str(row["family"]),
        )
    )
    return out


def build_rows() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    baseline = _baseline_asset_family(_read_rows(BASELINE_CSV))
    followup = _followup_asset_family(_read_rows(FOLLOWUP_CSV))
    compared: list[dict[str, object]] = []
    for row in followup:
        key = (str(row["asset"]), str(row["family"]))
        base = baseline.get(key)
        baseline_quality = str(base.get("dominant_attachment_quality")) if base else "neu_ohne_baseline"
        follow_quality = str(row["dominant_attachment_quality"])
        if baseline_quality == "neu_ohne_baseline":
            repro_state = "neu_ohne_baseline"
        elif baseline_quality == follow_quality:
            repro_state = "anschlussqualitaet_reproduziert"
        elif baseline_quality == "offen_gemischt" or follow_quality == "offen_gemischt":
            repro_state = "anschlussqualitaet_driftet_offen"
        else:
            repro_state = "anschlussqualitaet_driftet"
        compared.append(
            {
                "row_type": "asset_family_repro",
                **row,
                "baseline_attachment_quality": baseline_quality,
                "baseline_attachment_profile": str(base.get("attachment_profile") if base else ""),
                "repro_state": repro_state,
            }
        )
    state_counts = Counter(str(row["repro_state"]) for row in compared)
    quality_counts = Counter(str(row["dominant_attachment_quality"]) for row in compared)
    asset_states = Counter(f"{row['asset']}::{row['repro_state']}" for row in compared)
    summary = [
        {
            "row_type": "summary",
            "baseline_source": str(BASELINE_CSV.relative_to(ROOT)),
            "followup_source": str(FOLLOWUP_CSV.relative_to(ROOT)),
            "asset_family_pairs": len(compared),
            "repro_states": _profile(state_counts),
            "followup_qualities": _profile(quality_counts),
            "asset_repro_states": _profile(asset_states),
        }
    ]
    return summary, compared


def write_md(summary: list[dict[str, object]], rows: list[dict[str, object]]) -> None:
    item = summary[0]
    top_repro = [row for row in rows if row["repro_state"] == "anschlussqualitaet_reproduziert"][:20]
    top_drift = [row for row in rows if str(row["repro_state"]).startswith("anschlussqualitaet_driftet")][:20]
    lines = [
        "# 1854 - Familien-Anschlusskarte gegen neue Welten",
        "",
        "## Grundfrage",
        "",
        "Taucht die passive Familien-Anschlusskarte aus `1851/1852` in neuen Weltfenstern wieder auf, oder driftet sie?",
        "",
        "## Methode",
        "",
        "- Baseline: Asset/Familien-Anschlussprofile aus `1851`.",
        "- Folge: neue Fenster aus `1853`.",
        "- Verglichen wird pro Asset/Familie die dominante Anschlussqualität.",
        "- Keine Handlung, kein Gate, keine Richtung.",
        "",
        "## Kurzbefund",
        "",
        f"- Asset/Familien-Paare: `{item['asset_family_pairs']}`",
        f"- Reproduktionszustände: `{item['repro_states']}`",
        f"- Folge-Qualitäten: `{item['followup_qualities']}`",
        "",
        "## Wiederkehrende Profile",
        "",
        "| Asset | Familie | Baseline | Folge | Profil | Zustand |",
        "|---|---|---|---|---|---|",
    ]
    for row in top_repro:
        lines.append(
            f"| {row['asset']} | `{row['family']}` | `{row['baseline_attachment_quality']}` | "
            f"`{row['dominant_attachment_quality']}` | `{row['attachment_profile']}` | `{row['repro_state']}` |"
        )
    lines.extend(
        [
            "",
            "## Driftende Profile",
            "",
            "| Asset | Familie | Baseline | Folge | Profil | Zustand |",
            "|---|---|---|---|---|---|",
        ]
    )
    for row in top_drift:
        lines.append(
            f"| {row['asset']} | `{row['family']}` | `{row['baseline_attachment_quality']}` | "
            f"`{row['dominant_attachment_quality']}` | `{row['attachment_profile']}` | `{row['repro_state']}` |"
        )
    lines.extend(
        [
            "",
            "## Einordnung",
            "",
            "Die passive Familien-Anschlusskarte zeigt Wiederkehr, aber keine starre Kopie.",
            "Ein Teil der Asset/Familien-Paare reproduziert seine Anschlussqualität, ein größerer Teil driftet offen.",
            "Das ist methodisch sinnvoll: Das Feld speichert keinen festen Symbolwert, sondern eine kontextabhängige Anschlusslage.",
            "",
            "Damit bleibt die bisherige Linie erhalten:",
            "`Familie + Weltkontext + Anschlussqualität` ist tragfähiger als eine isolierte Familienbedeutung.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    summary, rows = build_rows()
    _write_csv(OUT_CSV, summary + rows)
    write_md(summary, rows)
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"wrote {OUT_CSV.relative_to(ROOT)}")
    print(summary[0])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
