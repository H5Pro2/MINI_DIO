from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

from update_mcm_field_role_memory import ROOT, _attachment_quality, _float


BASELINE_SOURCES = [
    ROOT / "docs/befunde/1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv",
    ROOT / "docs/befunde/1848_ANSCHLUSSQUALITAET_NEUE_FENSTER.csv",
]
FOLLOWUP_CSV = ROOT / "docs/befunde/1853_FAMILIEN_ANSCHLUSSKARTE_NEUE_WELTEN.csv"
OUT_CSV = ROOT / "docs/befunde/1856_FAMILIEN_ANSCHLUSS_PHASE_BASELINE.csv"
OUT_MD = ROOT / "docs/befunde/1856_FAMILIEN_ANSCHLUSS_PHASE_BASELINE.md"

PHASES = ("frueh", "mitte", "spaet")


def _read(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _read_many(paths: list[Path]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in paths:
        for row in _read(path):
            row["source_report"] = str(path.relative_to(ROOT))
            rows.append(row)
    return rows


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


def _phase_rows_from_report(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    quality_by_window = _window_quality(rows)
    out: list[dict[str, object]] = []
    for row in rows:
        if row.get("row_type") != "detail" or row.get("kind") != "real":
            continue
        asset = str(row.get("asset") or "")
        window_start = int(_float(row.get("window_start")))
        quality = quality_by_window.get((asset, window_start), "")
        if not quality:
            continue
        for phase in PHASES:
            count = int(_float(row.get(f"count_{phase}")))
            if count <= 0:
                continue
            out.append(
                {
                    "asset": str(row.get("asset") or ""),
                    "family": str(row.get("family") or ""),
                    "phase": phase,
                    "window_start": window_start,
                    "attachment_quality": quality,
                    "family_reading": str(row.get("family_reading") or ""),
                    "dominant_role": str(row.get("dominant_role") or ""),
                    "count": count,
                    "share": _float(row.get(f"share_{phase}")),
                    "rekopplung": _float(row.get(f"rekopplung_{phase}")),
                    "strain": _float(row.get(f"strain_{phase}")),
                    "afterimage": _float(row.get(f"afterimage_{phase}")),
                    "temporal": _float(row.get(f"temporal_{phase}")),
                    "field_edge_score": _float(row.get("field_edge_score")),
                }
            )
    return out


def _window_quality(rows: list[dict[str, str]]) -> dict[tuple[str, int], str]:
    out: dict[tuple[str, int], str] = {}
    for row in rows:
        if row.get("row_type") != "window_summary":
            continue
        out[(str(row.get("asset") or ""), int(_float(row.get("window_start"))))] = _attachment_quality(
            str(row.get("reading") or "")
        )
    return out


def _phase_rows_from_followup(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    return _phase_rows_from_report(rows)


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _aggregate(rows: list[dict[str, object]]) -> dict[tuple[str, str, str], dict[str, object]]:
    grouped: dict[tuple[str, str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["asset"]), str(row["family"]), str(row["phase"]))].append(row)
    out: dict[tuple[str, str, str], dict[str, object]] = {}
    for key, items in grouped.items():
        quality_counts = Counter(str(item["attachment_quality"]) for item in items)
        dominant, dominant_count, second, second_count, gap = _dominant(quality_counts)
        out[key] = {
            "asset": key[0],
            "family": key[1],
            "phase": key[2],
            "observations": len(items),
            "dominant_attachment_quality": dominant,
            "dominant_attachment_count": dominant_count,
            "second_attachment_quality": second,
            "second_attachment_count": second_count,
            "attachment_quality_gap": gap,
            "attachment_profile": _profile(quality_counts),
            "mean_share": round(_mean([_float(item["share"]) for item in items]), 6),
            "mean_rekopplung": round(_mean([_float(item["rekopplung"]) for item in items]), 6),
            "mean_strain": round(_mean([_float(item["strain"]) for item in items]), 6),
            "mean_afterimage": round(_mean([_float(item["afterimage"]) for item in items]), 6),
            "mean_temporal": round(_mean([_float(item["temporal"]) for item in items]), 6),
        }
    return out


def _drift_state(base: str, follow: str) -> str:
    if not base:
        return "neu_ohne_phasenbaseline"
    if base == follow:
        return "phase_reproduziert"
    if base == "offen_gemischt" and follow != "offen_gemischt":
        return "phase_offen_wird_spezifisch"
    if base != "offen_gemischt" and follow == "offen_gemischt":
        return "phase_spezifisch_wird_offen"
    if base == "nachhallnah_ohne_kern" and follow == "kernnah":
        return "phase_nachhall_wird_kernnah"
    return "phase_kontextdrift"


def build_rows() -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    baseline = _aggregate(_phase_rows_from_report(_read_many(BASELINE_SOURCES)))
    followup = _aggregate(_phase_rows_from_followup(_read(FOLLOWUP_CSV)))
    compared: list[dict[str, object]] = []
    for key, follow in followup.items():
        base = baseline.get(key, {})
        base_quality = str(base.get("dominant_attachment_quality") or "")
        follow_quality = str(follow.get("dominant_attachment_quality") or "")
        compared.append(
            {
                "row_type": "phase_repro_detail",
                "asset": key[0],
                "family": key[1],
                "phase": key[2],
                "baseline_attachment_quality": base_quality or "neu_ohne_phasenbaseline",
                "followup_attachment_quality": follow_quality,
                "phase_repro_state": _drift_state(base_quality, follow_quality),
                "baseline_profile": str(base.get("attachment_profile") or ""),
                "followup_profile": str(follow.get("attachment_profile") or ""),
                "baseline_observations": int(_float(base.get("observations"))),
                "followup_observations": int(_float(follow.get("observations"))),
                "baseline_share": _float(base.get("mean_share")),
                "followup_share": _float(follow.get("mean_share")),
                "baseline_rekopplung": _float(base.get("mean_rekopplung")),
                "followup_rekopplung": _float(follow.get("mean_rekopplung")),
                "baseline_afterimage": _float(base.get("mean_afterimage")),
                "followup_afterimage": _float(follow.get("mean_afterimage")),
                "baseline_temporal": _float(base.get("mean_temporal")),
                "followup_temporal": _float(follow.get("mean_temporal")),
            }
        )
    state_counts = Counter(str(row["phase_repro_state"]) for row in compared)
    transition_counts = Counter(
        f"{row['baseline_attachment_quality']}->{row['followup_attachment_quality']}" for row in compared
    )
    phase_counts = Counter(f"{row['phase']}::{row['phase_repro_state']}" for row in compared)
    summary = [
        {
            "row_type": "summary",
            "phase_pairs": len(compared),
            "baseline_sources": "; ".join(str(path.relative_to(ROOT)) for path in BASELINE_SOURCES),
            "baseline_phase_keys": len(baseline),
            "followup_phase_keys": len(followup),
            "phase_repro_states": _profile(state_counts),
            "phase_transitions": _profile(transition_counts),
            "phase_state_profile": _profile(phase_counts),
        }
    ]
    state_rows = [
        {
            "row_type": "phase_state_summary",
            "phase_repro_state": name,
            "count": count,
            "share": round(count / max(1, len(compared)), 6),
        }
        for name, count in state_counts.most_common()
    ]
    return summary, state_rows, compared


def write_md(summary: list[dict[str, object]], state_rows: list[dict[str, object]], details: list[dict[str, object]]) -> None:
    item = summary[0]
    sample_rows = details[:24]
    lines = [
        "# 1856 - Phasengenaue Familien-Anschlussbaseline",
        "",
        "## Grundfrage",
        "",
        "Sinkt die offene Drift, wenn die Baseline nicht nur nach Asset/Familie, sondern nach Asset/Familie/Phase gelesen wird?",
        "",
        "## Methode",
        "",
        f"- Baseline-Quellen: `{item['baseline_sources']}`, aufgeteilt in `frueh`, `mitte`, `spaet`.",
        "- Folge: `1853`, ebenfalls phasengenau gelesen.",
        "- Vergleich pro Asset/Familie/Phase.",
        "- Keine Handlung, kein Gate, keine Richtung.",
        "",
        "## Kurzbefund",
        "",
        f"- Phasen-Paare: `{item['phase_pairs']}`",
        f"- Baseline-Phasenschlüssel: `{item['baseline_phase_keys']}`",
        f"- Folge-Phasenschlüssel: `{item['followup_phase_keys']}`",
        f"- Phasen-Zustände: `{item['phase_repro_states']}`",
        f"- Phasen-Übergänge: `{item['phase_transitions']}`",
        "",
        "## Zustände",
        "",
        "| Zustand | Paare | Anteil |",
        "|---|---:|---:|",
    ]
    for row in state_rows:
        lines.append(f"| `{row['phase_repro_state']}` | {row['count']} | {_float(row['share']):.3f} |")
    lines.extend(
        [
            "",
            "## Beispielzeilen",
            "",
            "| Asset | Familie | Phase | Baseline | Folge | Zustand |",
            "|---|---|---|---|---|---|",
        ]
    )
    for row in sample_rows:
        lines.append(
            f"| {row['asset']} | `{row['family']}` | `{row['phase']}` | "
            f"`{row['baseline_attachment_quality']}` | `{row['followup_attachment_quality']}` | "
            f"`{row['phase_repro_state']}` |"
        )
    lines.extend(
        [
            "",
            "## Einordnung",
            "",
            "Die phasengenaue Lesung verringert die offene Drift nicht automatisch.",
            "Das spricht dafür, dass die bisherige Anschlussqualität noch zu stark auf Fensterqualität basiert.",
            "Phase allein reicht nicht, wenn die Qualität selbst noch nicht phasenlokal berechnet wird.",
            "",
            "Der wichtige Befund ist methodisch:",
            "Eine engere Baseline muss nicht nur Phasen trennen, sondern die Anschlussqualität innerhalb der Phase neu lesen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte Anschlussqualität nicht mehr nur vom Gesamtfenster geerbt werden.",
            "Sie muss phasenlokal berechnet werden: Frueh/Mitte/Spaet jeweils gegen passende Nullwelt-Phasen.",
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
