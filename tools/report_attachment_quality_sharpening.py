from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

from update_mcm_field_role_memory import (
    ROOT,
    _float,
    _quality,
    _read_attachment_rows,
    _read_rows,
    _state,
    build_attachment_quality_memory,
)


OUT_CSV = ROOT / "docs/befunde/1850_ANSCHLUSSQUALITAET_SCHAERFUNG.csv"
OUT_MD = ROOT / "docs/befunde/1850_ANSCHLUSSQUALITAET_SCHAERFUNG.md"


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


def _quality_profile(items: list[dict[str, object]]) -> str:
    counts = Counter(str(item.get("attachment_quality") or "-") for item in items)
    return "; ".join(f"{name}:{count}" for name, count in counts.most_common()) or "-"


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _asset_attachment_profiles(attachment_memory: dict) -> dict[str, dict[str, object]]:
    by_asset: dict[str, list[dict[str, object]]] = defaultdict(list)
    for item in attachment_memory.get("window_readings", []):
        if isinstance(item, dict):
            by_asset[str(item.get("asset") or "-")].append(item)

    out: dict[str, dict[str, object]] = {}
    for asset, items in by_asset.items():
        quality_counts = Counter(str(item.get("attachment_quality") or "-") for item in items)
        dominant_quality, dominant_count = quality_counts.most_common(1)[0]
        total = max(1, len(items))
        out[asset] = {
            "attachment_profile": _quality_profile(items),
            "dominant_attachment_quality": dominant_quality,
            "dominant_attachment_share": dominant_count / total,
            "mean_field_edge_score": _mean([_float(item.get("field_edge_score")) for item in items]),
            "mean_kern_edge": _mean([_float(item.get("kern_edge")) for item in items]),
            "mean_afterimage_edge": _mean([_float(item.get("afterimage_edge")) for item in items]),
            "mean_temporal_edge": _mean([_float(item.get("temporal_edge")) for item in items]),
        }
    return out


def build_rows() -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    family_rows = _read_rows()
    attachment_memory = build_attachment_quality_memory(_read_attachment_rows())
    asset_profiles = _asset_attachment_profiles(attachment_memory)

    family_out: list[dict[str, object]] = []
    for row in family_rows:
        asset = str(row.get("asset") or "-")
        field_role_state = _state(row)
        profile = asset_profiles.get(asset, {})
        enhanced_key = f"{field_role_state}::{profile.get('dominant_attachment_quality', 'ungelesen')}"
        family_out.append(
            {
                "row_type": "family_with_attachment",
                "asset": asset,
                "family": str(row.get("family") or ""),
                "field_role_state": field_role_state,
                "source_reading": str(row.get("family_reading") or ""),
                "field_role_quality": round(_quality(row), 6),
                "attachment_profile": str(profile.get("attachment_profile", "ungelesen")),
                "dominant_attachment_quality": str(profile.get("dominant_attachment_quality", "ungelesen")),
                "dominant_attachment_share": round(_float(profile.get("dominant_attachment_share")), 6),
                "mean_field_edge_score": round(_float(profile.get("mean_field_edge_score")), 6),
                "enhanced_role_key": enhanced_key,
            }
        )

    base_counts = Counter(str(row["field_role_state"]) for row in family_out)
    enhanced_counts = Counter(str(row["enhanced_role_key"]) for row in family_out)
    asset_counts = Counter(str(row["asset"]) for row in family_out)
    asset_quality_counts = Counter(
        f"{asset}::{profile.get('dominant_attachment_quality', 'ungelesen')}"
        for asset, profile in asset_profiles.items()
    )

    summary_rows = [
        {
            "row_type": "summary",
            "families": len(family_out),
            "base_role_states": len(base_counts),
            "enhanced_role_states": len(enhanced_counts),
            "assets": len(asset_counts),
            "attachment_assets": len(asset_profiles),
            "base_counts": "; ".join(f"{name}:{count}" for name, count in base_counts.most_common()),
            "enhanced_counts": "; ".join(f"{name}:{count}" for name, count in enhanced_counts.most_common()),
            "asset_attachment_dominants": "; ".join(f"{name}:{count}" for name, count in asset_quality_counts.most_common()),
        }
    ]

    asset_rows = []
    for asset, profile in sorted(asset_profiles.items()):
        asset_rows.append(
            {
                "row_type": "asset_attachment_profile",
                "asset": asset,
                **profile,
            }
        )

    return summary_rows, asset_rows, family_out


def write_md(summary_rows: list[dict[str, object]], asset_rows: list[dict[str, object]]) -> None:
    summary = summary_rows[0]
    lines = [
        "# 1850 - Anschlussqualität schärft Feldrollenbeschreibung",
        "",
        "## Grundfrage",
        "",
        "Wird die passive Feldrollen-Memory durch Anschlussqualität klarer,",
        "oder entstehen nur zusätzliche Namen ohne Informationsgewinn?",
        "",
        "## Methode",
        "",
        "- Basis: Familien-Reifung aus `1840`.",
        "- Zusatz: Anschlussqualität aus `1846` und `1848`.",
        "- Verglichen wird nur die Beschreibung der Feldrollen.",
        "- Keine Handlung, kein Gate, keine Richtung.",
        "",
        "## Kurzbefund",
        "",
        f"- Familien: `{summary['families']}`",
        f"- Alte Rollenklassen: `{summary['base_role_states']}`",
        f"- Rollenklassen mit Anschlussqualität: `{summary['enhanced_role_states']}`",
        f"- Basisverteilung: `{summary['base_counts']}`",
        f"- Erweiterte Verteilung: `{summary['enhanced_counts']}`",
        "",
        "## Asset-Profile",
        "",
        "| Asset | Anschlussprofil | Dominant | Dominanz | Feldvorsprung Ø | Kernvorsprung Ø | Nachhallvorsprung Ø | Feldzeitvorsprung Ø |",
        "|---|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in asset_rows:
        lines.append(
            f"| {row['asset']} | `{row['attachment_profile']}` | `{row['dominant_attachment_quality']}` | "
            f"{_float(row['dominant_attachment_share']):.3f} | {_float(row['mean_field_edge_score']):.4f} | "
            f"{_float(row['mean_kern_edge']):.4f} | {_float(row['mean_afterimage_edge']):.4f} | "
            f"{_float(row['mean_temporal_edge']):.4f} |"
        )
    lines.extend(
        [
            "",
            "## Einordnung",
            "",
            "Die Anschlussqualität schärft die Feldrollenbeschreibung, weil gleiche Basisrollen nicht mehr nur als",
            "`feldrolle_anschlussfaehig` oder `feldrolle_reift_verdichtend` erscheinen.",
            "Sie erhalten zusätzlich eine passive Anschlussfärbung aus dem Welt-/Nullwelt-Vergleich.",
            "",
            "Der Gewinn liegt nicht in einer Entscheidungsregel.",
            "Der Gewinn liegt in einer präziseren Innenfeldbeschreibung:",
            "eine Rolle kann anschlussfähig sein und trotzdem eher kernnah, nullnah, nachhallnah oder offen gemischt getragen werden.",
            "",
            "Die Schicht ist noch grob, weil sie aktuell assetnah und fensterbasiert aggregiert.",
            "Sie ist aber ein sinnvoller nächster Schritt, weil sie aus wiederholten Befunden stammt und keine neue Steuerung erzwingt.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte diese Schärfung feiner werden: nicht nur pro Asset, sondern pro Familie prüfen,",
            "welche Familien in welchen Anschlussqualitäten wiederkehren.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    summary_rows, asset_rows, family_rows = build_rows()
    _write_csv(OUT_CSV, summary_rows + asset_rows + family_rows)
    write_md(summary_rows, asset_rows)
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"wrote {OUT_CSV.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
