from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

from update_mcm_field_role_memory import ROOT, _float


SOURCE_CSV = ROOT / "docs/befunde/1857_PHASENLOKALE_ANSCHLUSSQUALITAET.csv"
OUT_CSV = ROOT / "docs/befunde/1858_PHASENLOKALE_FAMILIENSTABILITAET.csv"
OUT_MD = ROOT / "docs/befunde/1858_PHASENLOKALE_FAMILIENSTABILITAET.md"


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


def _dominant(counter: Counter[str]) -> tuple[str, int, str, int, int]:
    common = counter.most_common()
    if not common:
        return "-", 0, "-", 0, 0
    dominant, dominant_count = common[0]
    second, second_count = common[1] if len(common) > 1 else ("-", 0)
    return dominant, dominant_count, second, second_count, dominant_count - second_count


def _stability_state(observations: int, gap: int, matches: int, differs: int) -> str:
    if observations <= 1:
        return "einzelbeleg"
    if gap <= 0:
        return "geteilt_offen"
    if differs > matches:
        return "phasenlokal_eigenstaendig"
    return "fenstergetragen_stabil"


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def build_rows() -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    detail_rows = [row for row in _read(SOURCE_CSV) if row.get("row_type") == "phase_local_detail"]
    grouped: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in detail_rows:
        grouped[(str(row.get("asset") or ""), str(row.get("family") or ""), str(row.get("phase") or ""))].append(row)

    family_rows: list[dict[str, object]] = []
    for (asset, family, phase), items in grouped.items():
        local_counts = Counter(str(item.get("phase_local_quality") or "") for item in items)
        inherited_counts = Counter(str(item.get("inherited_window_quality") or "") for item in items)
        dominant, dominant_count, second, second_count, gap = _dominant(local_counts)
        matches = sum(1 for item in items if str(item.get("quality_matches_window") or "").lower() == "true")
        differs = len(items) - matches
        family_rows.append(
            {
                "row_type": "family_phase_stability_detail",
                "asset": asset,
                "family": family,
                "phase": phase,
                "observations": len(items),
                "dominant_phase_quality": dominant,
                "dominant_count": dominant_count,
                "second_phase_quality": second,
                "second_count": second_count,
                "dominance_gap": gap,
                "matches_window": matches,
                "differs_from_window": differs,
                "stability_state": _stability_state(len(items), gap, matches, differs),
                "local_quality_profile": _profile(local_counts),
                "inherited_quality_profile": _profile(inherited_counts),
                "mean_share_edge": round(_mean([_float(item.get("share_edge")) for item in items]), 9),
                "mean_rekopplung_edge": round(_mean([_float(item.get("rekopplung_edge")) for item in items]), 9),
                "mean_afterimage_edge": round(_mean([_float(item.get("afterimage_edge")) for item in items]), 9),
                "mean_temporal_edge": round(_mean([_float(item.get("temporal_edge")) for item in items]), 9),
            }
        )

    state_counts = Counter(str(row["stability_state"]) for row in family_rows)
    dominant_counts = Counter(str(row["dominant_phase_quality"]) for row in family_rows)
    asset_state_counts = Counter(f"{row['asset']}::{row['stability_state']}" for row in family_rows)
    phase_state_counts = Counter(f"{row['phase']}::{row['stability_state']}" for row in family_rows)
    summary = [
        {
            "row_type": "summary",
            "source": str(SOURCE_CSV.relative_to(ROOT)),
            "family_phase_pairs": len(family_rows),
            "stability_states": _profile(state_counts),
            "dominant_phase_qualities": _profile(dominant_counts),
            "asset_state_profile": _profile(asset_state_counts),
            "phase_state_profile": _profile(phase_state_counts),
        }
    ]
    state_rows = [
        {
            "row_type": "stability_state_summary",
            "stability_state": name,
            "count": count,
            "share": round(count / max(1, len(family_rows)), 6),
        }
        for name, count in state_counts.most_common()
    ]
    family_rows.sort(
        key=lambda row: (
            str(row["stability_state"]) != "phasenlokal_eigenstaendig",
            -int(row["dominance_gap"]),
            str(row["asset"]),
            str(row["family"]),
            str(row["phase"]),
        )
    )
    return summary, state_rows, family_rows


def write_md(summary: list[dict[str, object]], state_rows: list[dict[str, object]], details: list[dict[str, object]]) -> None:
    item = summary[0]
    sample = details[:28]
    lines = [
        "# 1858 - Phasenlokale Familienstabilität",
        "",
        "## Grundfrage",
        "",
        "Welche Familien bleiben phasenlokal stabil, und welche wirken eher nur durch die geerbte Fensterqualität getragen?",
        "",
        "## Methode",
        "",
        f"- Quelle: `{item['source']}`.",
        "- Gruppierung: Asset/Familie/Phase.",
        "- Gelesen wird die Verteilung phasenlokaler Anschlussqualitäten aus 1857.",
        "- Die Zustände beschreiben passive Lesbarkeit, keine Handlung und kein Gate.",
        "",
        "## Kurzbefund",
        "",
        f"- Familien-Phasen-Paare: `{item['family_phase_pairs']}`",
        f"- Stabilitätszustände: `{item['stability_states']}`",
        f"- Dominante Phasenqualitäten: `{item['dominant_phase_qualities']}`",
        f"- Asset-Profil: `{item['asset_state_profile']}`",
        f"- Phasen-Profil: `{item['phase_state_profile']}`",
        "",
        "## Zustände",
        "",
        "| Zustand | Paare | Anteil |",
        "|---|---:|---:|",
    ]
    for row in state_rows:
        lines.append(f"| `{row['stability_state']}` | {row['count']} | {_float(row['share']):.3f} |")
    lines.extend(
        [
            "",
            "## Beispielzeilen",
            "",
            "| Asset | Familie | Phase | Zustand | Dominant | Profil | Fensterabweichung | Rekopplung-Edge | Temporal-Edge |",
            "|---|---|---|---|---|---|---:|---:|---:|",
        ]
    )
    for row in sample:
        lines.append(
            f"| {row['asset']} | `{row['family']}` | `{row['phase']}` | `{row['stability_state']}` | "
            f"`{row['dominant_phase_quality']}` | `{row['local_quality_profile']}` | {row['differs_from_window']} | "
            f"{_float(row['mean_rekopplung_edge']):.5f} | {_float(row['mean_temporal_edge']):.5f} |"
        )
    lines.extend(
        [
            "",
            "## Einordnung",
            "",
            "Der Bericht trennt zwei Fälle:",
            "",
            "- `phasenlokal_eigenstaendig`: Die Familie hat innerhalb einer Phase eine erkennbare lokale Qualität und weicht häufiger vom Fensterprofil ab.",
            "- `fenstergetragen_stabil`: Die Familie ist stabil, wird aber stärker vom Gesamtfenster mitgetragen.",
            "",
            "Damit wird die passive Bedeutungsreife präziser. Eine Familie ist nicht nur ein Name und nicht nur eine Fensterrolle.",
            "Sie kann als lokaler Phasenanker gelesen werden, wenn sie unter mehreren Weltfenstern eine eigene Phasenqualität trägt.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte geprüft werden, ob diese phasenlokal eigenständigen Familien über neue Weltfenster wiederkehren.",
            "Wichtig ist dabei nicht mehr nur `taucht der Name wieder auf`, sondern `taucht dieselbe lokale Phasenqualität wieder auf`.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    summary, state_rows, details = build_rows()
    _write_csv(OUT_CSV, summary + state_rows + details)
    write_md(summary, state_rows, details)
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"wrote {OUT_CSV.relative_to(ROOT)}")
    print(summary[0])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
