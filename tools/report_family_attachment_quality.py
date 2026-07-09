from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

from update_mcm_field_role_memory import (
    ROOT,
    _attachment_quality,
    _float,
    _read_attachment_rows,
)


OUT_CSV = ROOT / "docs/befunde/1001-2000/1751-2000/1851_FAMILIEN_ANSCHLUSSQUALITAET.csv"
OUT_MD = ROOT / "docs/befunde/1001-2000/1751-2000/1851_FAMILIEN_ANSCHLUSSQUALITAET.md"


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


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _dominant(counter: Counter[str]) -> tuple[str, int, str, int, int]:
    common = counter.most_common()
    if not common:
        return "-", 0, "-", 0, 0
    dominant_name, dominant_count = common[0]
    second_name, second_count = common[1] if len(common) > 1 else ("-", 0)
    return dominant_name, dominant_count, second_name, second_count, dominant_count - second_count


def _profile_state(appearances: int, gap: int) -> str:
    if appearances <= 1:
        return "einzelbeleg"
    if gap >= 2:
        return "familienanschluss_deutlich"
    if gap == 1:
        return "familienanschluss_leicht"
    return "familienanschluss_offen_gemischt"


def _window_attachment_map(rows: list[dict[str, str]]) -> dict[tuple[str, str, int], dict[str, object]]:
    out: dict[tuple[str, str, int], dict[str, object]] = {}
    for row in rows:
        if row.get("row_type") != "window_summary":
            continue
        source_report = str(row.get("source_report") or "")
        asset = str(row.get("asset") or "")
        window_start = int(_float(row.get("window_start")))
        source_reading = str(row.get("reading") or "")
        out[(source_report, asset, window_start)] = {
            "source_report": source_report,
            "asset": asset,
            "window_start": window_start,
            "attachment_quality": _attachment_quality(source_reading),
            "attachment_source_reading": source_reading,
            "source_edge": _float(row.get("source_edge")),
            "kern_edge": _float(row.get("kern_edge")),
            "afterimage_edge": _float(row.get("afterimage_edge")),
            "temporal_edge": _float(row.get("temporal_edge")),
            "field_edge_score": _float(row.get("field_edge_score")),
        }
    return out


def _real_family_rows(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    attachment_map = _window_attachment_map(rows)
    out: list[dict[str, object]] = []
    for row in rows:
        if row.get("row_type") != "detail" or row.get("kind") != "real":
            continue
        source_report = str(row.get("source_report") or "")
        asset = str(row.get("asset") or "")
        window_start = int(_float(row.get("window_start")))
        attachment = attachment_map.get((source_report, asset, window_start), {})
        out.append(
            {
                "source_report": source_report,
                "asset": asset,
                "window_start": window_start,
                "family": str(row.get("family") or ""),
                "family_reading": str(row.get("family_reading") or ""),
                "dominant_role": str(row.get("dominant_role") or ""),
                "total_count": int(_float(row.get("total_count"))),
                "phase_presence": int(_float(row.get("phase_presence"))),
                "afterimage_delta_spaet_frueh": _float(row.get("afterimage_delta_spaet_frueh")),
                "temporal_delta_spaet_frueh": _float(row.get("temporal_delta_spaet_frueh")),
                "strain_delta_spaet_frueh": _float(row.get("strain_delta_spaet_frueh")),
                **attachment,
            }
        )
    return out


def _aggregate_family(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get("family") or "")].append(row)

    out: list[dict[str, object]] = []
    for family, items in grouped.items():
        quality_counts = Counter(str(item.get("attachment_quality") or "-") for item in items)
        reading_counts = Counter(str(item.get("family_reading") or "-") for item in items)
        role_counts = Counter(str(item.get("dominant_role") or "-") for item in items)
        asset_counts = Counter(str(item.get("asset") or "-") for item in items)
        dominant_quality, dominant_count, second_quality, second_count, gap = _dominant(quality_counts)
        dominant_reading, _, _, _, _ = _dominant(reading_counts)
        dominant_role, _, _, _, _ = _dominant(role_counts)
        appearances = len(items)
        out.append(
            {
                "row_type": "family_attachment_summary",
                "family": family,
                "appearances": appearances,
                "asset_count": len(asset_counts),
                "window_count": len({(item.get("source_report"), item.get("asset"), item.get("window_start")) for item in items}),
                "dominant_attachment_quality": dominant_quality,
                "dominant_attachment_count": dominant_count,
                "second_attachment_quality": second_quality,
                "second_attachment_count": second_count,
                "attachment_quality_gap": gap,
                "attachment_profile_state": _profile_state(appearances, gap),
                "attachment_profile": _profile(quality_counts),
                "dominant_family_reading": dominant_reading,
                "family_reading_profile": _profile(reading_counts),
                "dominant_role": dominant_role,
                "role_profile": _profile(role_counts),
                "asset_profile": _profile(asset_counts),
                "mean_total_count": round(_mean([_float(item.get("total_count")) for item in items]), 6),
                "mean_phase_presence": round(_mean([_float(item.get("phase_presence")) for item in items]), 6),
                "mean_afterimage_delta": round(_mean([_float(item.get("afterimage_delta_spaet_frueh")) for item in items]), 6),
                "mean_temporal_delta": round(_mean([_float(item.get("temporal_delta_spaet_frueh")) for item in items]), 6),
                "mean_strain_delta": round(_mean([_float(item.get("strain_delta_spaet_frueh")) for item in items]), 6),
                "mean_field_edge_score": round(_mean([_float(item.get("field_edge_score")) for item in items]), 6),
            }
        )
    out.sort(
        key=lambda row: (
            int(row["appearances"]),
            int(row["asset_count"]),
            int(row["attachment_quality_gap"]),
            float(row["mean_total_count"]),
        ),
        reverse=True,
    )
    return out


def _aggregate_asset_family(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row.get("asset") or ""), str(row.get("family") or ""))].append(row)

    out: list[dict[str, object]] = []
    for (asset, family), items in grouped.items():
        quality_counts = Counter(str(item.get("attachment_quality") or "-") for item in items)
        dominant_quality, dominant_count, second_quality, second_count, gap = _dominant(quality_counts)
        out.append(
            {
                "row_type": "asset_family_attachment_summary",
                "asset": asset,
                "family": family,
                "appearances": len(items),
                "dominant_attachment_quality": dominant_quality,
                "dominant_attachment_count": dominant_count,
                "second_attachment_quality": second_quality,
                "second_attachment_count": second_count,
                "attachment_quality_gap": gap,
                "attachment_profile_state": _profile_state(len(items), gap),
                "attachment_profile": _profile(quality_counts),
                "mean_total_count": round(_mean([_float(item.get("total_count")) for item in items]), 6),
                "mean_field_edge_score": round(_mean([_float(item.get("field_edge_score")) for item in items]), 6),
            }
        )
    out.sort(
        key=lambda row: (
            int(row["appearances"]),
            int(row["attachment_quality_gap"]),
            float(row["mean_total_count"]),
        ),
        reverse=True,
    )
    return out


def build_rows() -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    source_rows = _read_attachment_rows()
    real_rows = _real_family_rows(source_rows)
    family_rows = _aggregate_family(real_rows)
    asset_family_rows = _aggregate_asset_family(real_rows)
    state_counts = Counter(str(row["attachment_profile_state"]) for row in family_rows)
    quality_counts = Counter(str(row["dominant_attachment_quality"]) for row in family_rows)
    summary = [
        {
            "row_type": "summary",
            "sources": "; ".join(sorted({str(row.get("source_report") or "") for row in real_rows})),
            "real_family_observations": len(real_rows),
            "families": len(family_rows),
            "asset_family_pairs": len(asset_family_rows),
            "profile_states": _profile(state_counts),
            "dominant_qualities": _profile(quality_counts),
        }
    ]
    return summary, family_rows, asset_family_rows, real_rows


def write_md(
    summary: list[dict[str, object]],
    family_rows: list[dict[str, object]],
    asset_family_rows: list[dict[str, object]],
) -> None:
    item = summary[0]
    top_families = family_rows[:16]
    stable_asset_families = [
        row
        for row in asset_family_rows
        if str(row.get("attachment_profile_state")) in {"familienanschluss_deutlich", "familienanschluss_leicht"}
    ][:16]
    lines = [
        "# 1851 - Familiengenaue Anschlussqualität",
        "",
        "## Grundfrage",
        "",
        "Hängt Anschlussqualität nur grob am Asset/Fenster, oder taucht sie familiengenau wieder auf?",
        "",
        "## Methode",
        "",
        "- Quellen: `1846` und `1848`.",
        "- Gelesen werden nur Realwelt-Detailzeilen pro Symbolfamilie.",
        "- Jede Familie erbt die passive Anschlussqualität ihres Weltfensters.",
        "- Danach wird geprüft, ob dieselbe Familie wiederholt in ähnlichen Anschlussqualitäten erscheint.",
        "- Keine Handlung, kein Gate, keine Richtung.",
        "",
        "## Kurzbefund",
        "",
        f"- Realwelt-Familienbeobachtungen: `{item['real_family_observations']}`",
        f"- Unterschiedliche Familien: `{item['families']}`",
        f"- Asset/Familien-Paare: `{item['asset_family_pairs']}`",
        f"- Profilzustände: `{item['profile_states']}`",
        f"- Dominante Anschlussqualitäten: `{item['dominant_qualities']}`",
        "",
        "## Stärkste Familienprofile",
        "",
        "| Familie | Vorkommen | Assets | Dominante Anschlussqualität | Profilzustand | Anschlussprofil | Familienlesung | Feldvorsprung Ø |",
        "|---|---:|---:|---|---|---|---|---:|",
    ]
    for row in top_families:
        lines.append(
            f"| `{row['family']}` | {row['appearances']} | {row['asset_count']} | "
            f"`{row['dominant_attachment_quality']}` | `{row['attachment_profile_state']}` | "
            f"`{row['attachment_profile']}` | `{row['dominant_family_reading']}` | "
            f"{_float(row['mean_field_edge_score']):.4f} |"
        )
    lines.extend(
        [
            "",
            "## Stärkste Asset/Familien-Profile",
            "",
            "| Asset | Familie | Vorkommen | Dominante Anschlussqualität | Profilzustand | Anschlussprofil | Feldvorsprung Ø |",
            "|---|---|---:|---|---|---|---:|",
        ]
    )
    for row in stable_asset_families:
        lines.append(
            f"| {row['asset']} | `{row['family']}` | {row['appearances']} | "
            f"`{row['dominant_attachment_quality']}` | `{row['attachment_profile_state']}` | "
            f"`{row['attachment_profile']}` | {_float(row['mean_field_edge_score']):.4f} |"
        )
    lines.extend(
        [
            "",
            "## Einordnung",
            "",
            "Die Prüfung zeigt eine wichtige Grenze: familienübergreifend bleibt Anschlussqualität oft gemischt,",
            "weil dieselben Symbolfamilien in mehreren Assets und Fenstern auftauchen.",
            "Das spricht gegen eine einfache feste Bedeutung pro Wort.",
            "",
            "Auf Asset/Familien-Ebene wird die Lesung schärfer.",
            "Dort erscheinen einige Familien wiederholt in ähnlichen Anschlussqualitäten.",
            "Damit liegt die Bedeutung näher an `Familie + Weltkontext + Anschlussqualität` als an einer isolierten Symboltabelle.",
            "",
            "Das passt zur bisherigen MCM-Lesung:",
            "Bedeutung ist keine starre Benennung, sondern ein Feldprofil aus Wiederkehr, Kontext, Nachhall, Feldzeit und Anschluss.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    summary, family_rows, asset_family_rows, real_rows = build_rows()
    _write_csv(OUT_CSV, summary + family_rows + asset_family_rows + real_rows)
    write_md(summary, family_rows, asset_family_rows)
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"wrote {OUT_CSV.relative_to(ROOT)}")
    print(summary[0])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
