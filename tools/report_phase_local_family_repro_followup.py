from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path

from update_mcm_field_role_memory import ROOT, _attachment_quality, _float


BASELINE_CSV = ROOT / "docs/befunde/1001-2000/1751-2000/1858_PHASENLOKALE_FAMILIENSTABILITAET.csv"
FOLLOWUP_CSV = ROOT / "docs/befunde/1001-2000/1751-2000/1860_PHASENLOKALE_FAMILIEN_FOLGEFENSTER.csv"
OUT_CSV = ROOT / "docs/befunde/1001-2000/1751-2000/1861_PHASENLOKALE_FAMILIEN_REPRO_FOLGEFENSTER.csv"
OUT_MD = ROOT / "docs/befunde/1001-2000/1751-2000/1861_PHASENLOKALE_FAMILIEN_REPRO_FOLGEFENSTER.md"
TITLE = "1861 - Phasenlokale Familien-Reproduktion in Folgefenstern"

PHASES = ("frueh", "mitte", "spaet")


def _resolve(value: str | Path) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = ROOT / path
    return path


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


def _window_quality(rows: list[dict[str, str]]) -> dict[tuple[str, int], str]:
    out: dict[tuple[str, int], str] = {}
    for row in rows:
        if row.get("row_type") != "window_summary":
            continue
        out[(str(row.get("asset") or ""), int(_float(row.get("window_start"))))] = _attachment_quality(
            str(row.get("reading") or "")
        )
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
    active = [row for row in null_rows if _phase_count(row, phase) > 0] or null_rows
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


def _dominant(counter: Counter[str]) -> tuple[str, int, str, int, int]:
    common = counter.most_common()
    if not common:
        return "-", 0, "-", 0, 0
    dominant, dominant_count = common[0]
    second, second_count = common[1] if len(common) > 1 else ("-", 0)
    return dominant, dominant_count, second, second_count, dominant_count - second_count


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _followup_phase_details() -> list[dict[str, object]]:
    rows = _read(FOLLOWUP_CSV)
    inherited_quality = _window_quality(rows)
    details = [row for row in rows if row.get("row_type") == "detail"]
    null_index: dict[tuple[str, int, str], list[dict[str, str]]] = defaultdict(list)
    for row in details:
        if row.get("kind") == "real":
            continue
        null_index[
            (
                str(row.get("asset") or ""),
                int(_float(row.get("window_start"))),
                str(row.get("family") or ""),
            )
        ].append(row)
    out: list[dict[str, object]] = []
    for row in details:
        if row.get("kind") != "real":
            continue
        asset = str(row.get("asset") or "")
        window_start = int(_float(row.get("window_start")))
        family = str(row.get("family") or "")
        null_rows = null_index.get((asset, window_start, family), [])
        inherited = inherited_quality.get((asset, window_start), "")
        for phase in PHASES:
            if _phase_count(row, phase) <= 0:
                continue
            null_ref = _null_reference(null_rows, phase)
            edges = {
                "share_edge": _phase_value(row, "share", phase) - _float(null_ref["null_share"]),
                "rekopplung_edge": _phase_value(row, "rekopplung", phase) - _float(null_ref["null_rekopplung"]),
                "strain_edge": _phase_value(row, "strain", phase) - _float(null_ref["null_strain"]),
                "afterimage_edge": _phase_value(row, "afterimage", phase) - _float(null_ref["null_afterimage"]),
                "temporal_edge": _phase_value(row, "temporal", phase) - _float(null_ref["null_temporal"]),
            }
            out.append(
                {
                    "asset": asset,
                    "window_start": window_start,
                    "family": family,
                    "phase": phase,
                    "phase_local_quality": _phase_quality(edges, bool(null_rows)),
                    "inherited_window_quality": inherited,
                    **{key: round(value, 9) for key, value in edges.items()},
                }
            )
    return out


def _followup_family_phase() -> dict[tuple[str, str, str], dict[str, object]]:
    grouped: dict[tuple[str, str, str], list[dict[str, object]]] = defaultdict(list)
    for row in _followup_phase_details():
        grouped[(str(row["asset"]), str(row["family"]), str(row["phase"]))].append(row)
    out: dict[tuple[str, str, str], dict[str, object]] = {}
    for key, items in grouped.items():
        counts = Counter(str(item["phase_local_quality"]) for item in items)
        dominant, dominant_count, second, second_count, gap = _dominant(counts)
        out[key] = {
            "followup_observations": len(items),
            "followup_dominant_phase_quality": dominant,
            "followup_dominant_count": dominant_count,
            "followup_second_phase_quality": second,
            "followup_second_count": second_count,
            "followup_dominance_gap": gap,
            "followup_quality_profile": _profile(counts),
            "followup_mean_rekopplung_edge": round(_mean([_float(item.get("rekopplung_edge")) for item in items]), 9),
            "followup_mean_afterimage_edge": round(_mean([_float(item.get("afterimage_edge")) for item in items]), 9),
            "followup_mean_temporal_edge": round(_mean([_float(item.get("temporal_edge")) for item in items]), 9),
        }
    return out


def _repro_state(base_quality: str, follow_quality: str, base_state: str, follow: dict[str, object]) -> str:
    if not follow:
        return "fehlt_im_folgefenster"
    if base_quality == follow_quality:
        if base_state == "phasenlokal_eigenstaendig":
            return "lokale_qualitaet_reproduziert"
        return "qualitaet_reproduziert"
    if follow_quality == "phase_offen_gemischt":
        return "lokale_qualitaet_wird_offen"
    if follow_quality == "phase_nullnah":
        return "lokale_qualitaet_wird_nullnah"
    if follow_quality == "phase_kernnah":
        return "lokale_qualitaet_wird_kernnah"
    if follow_quality == "phase_nachhallnah_ohne_kern":
        return "lokale_qualitaet_wird_nachhallnah"
    return "lokale_qualitaet_driftet"


def build_rows() -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    baseline_rows = [
        row for row in _read(BASELINE_CSV) if row.get("row_type") == "family_phase_stability_detail"
    ]
    followup = _followup_family_phase()
    compared: list[dict[str, object]] = []
    for base in baseline_rows:
        key = (str(base.get("asset") or ""), str(base.get("family") or ""), str(base.get("phase") or ""))
        follow = followup.get(key, {})
        base_quality = str(base.get("dominant_phase_quality") or "")
        follow_quality = str(follow.get("followup_dominant_phase_quality") or "")
        base_state = str(base.get("stability_state") or "")
        compared.append(
            {
                "row_type": "family_phase_repro_detail",
                "asset": key[0],
                "family": key[1],
                "phase": key[2],
                "baseline_stability_state": base_state,
                "baseline_dominant_phase_quality": base_quality,
                "baseline_quality_profile": str(base.get("local_quality_profile") or ""),
                "followup_dominant_phase_quality": follow_quality or "fehlt",
                "followup_quality_profile": str(follow.get("followup_quality_profile") or ""),
                "followup_observations": int(_float(follow.get("followup_observations"))),
                "repro_state": _repro_state(base_quality, follow_quality, base_state, follow),
                "baseline_mean_rekopplung_edge": _float(base.get("mean_rekopplung_edge")),
                "followup_mean_rekopplung_edge": _float(follow.get("followup_mean_rekopplung_edge")),
                "baseline_mean_afterimage_edge": _float(base.get("mean_afterimage_edge")),
                "followup_mean_afterimage_edge": _float(follow.get("followup_mean_afterimage_edge")),
                "baseline_mean_temporal_edge": _float(base.get("mean_temporal_edge")),
                "followup_mean_temporal_edge": _float(follow.get("followup_mean_temporal_edge")),
            }
        )
    state_counts = Counter(str(row["repro_state"]) for row in compared)
    baseline_state_counts = Counter(str(row["baseline_stability_state"]) for row in compared)
    asset_state_counts = Counter(f"{row['asset']}::{row['repro_state']}" for row in compared)
    eigen = [row for row in compared if row["baseline_stability_state"] == "phasenlokal_eigenstaendig"]
    eigen_counts = Counter(str(row["repro_state"]) for row in eigen)
    summary = [
        {
            "row_type": "summary",
            "baseline": str(BASELINE_CSV.relative_to(ROOT)),
            "followup": str(FOLLOWUP_CSV.relative_to(ROOT)),
            "compared_family_phase_pairs": len(compared),
            "repro_states": _profile(state_counts),
            "baseline_states": _profile(baseline_state_counts),
            "eigenstaendig_repro_states": _profile(eigen_counts),
            "asset_repro_profile": _profile(asset_state_counts),
        }
    ]
    state_rows = [
        {
            "row_type": "repro_state_summary",
            "repro_state": name,
            "count": count,
            "share": round(count / max(1, len(compared)), 6),
        }
        for name, count in state_counts.most_common()
    ]
    compared.sort(
        key=lambda row: (
            str(row["repro_state"]) != "lokale_qualitaet_reproduziert",
            str(row["baseline_stability_state"]) != "phasenlokal_eigenstaendig",
            str(row["asset"]),
            str(row["family"]),
            str(row["phase"]),
        )
    )
    return summary, state_rows, compared


def write_md(summary: list[dict[str, object]], state_rows: list[dict[str, object]], details: list[dict[str, object]]) -> None:
    item = summary[0]
    sample = details[:30]
    lines = [
        f"# {TITLE}",
        "",
        "## Grundfrage",
        "",
        "Tauchen phasenlokal eigenständige Familien in neuen Weltfenstern wieder mit derselben lokalen Phasenqualität auf?",
        "",
        "## Methode",
        "",
        f"- Baseline: `{item['baseline']}`.",
        f"- Folgefenster: `{item['followup']}`.",
        "- Verglichen wird Asset/Familie/Phase.",
        "- Entscheidend ist nicht nur der Familienname, sondern die wiederkehrende lokale Phasenqualität.",
        "- Keine Handlung, kein Gate, keine Richtung.",
        "",
        "## Kurzbefund",
        "",
        f"- Verglichene Familien-Phasen-Paare: `{item['compared_family_phase_pairs']}`",
        f"- Repro-Zustände: `{item['repro_states']}`",
        f"- Baseline-Zustände: `{item['baseline_states']}`",
        f"- Eigenständige Baseline-Familien: `{item['eigenstaendig_repro_states']}`",
        f"- Asset-Profil: `{item['asset_repro_profile']}`",
        "",
        "## Zustände",
        "",
        "| Zustand | Paare | Anteil |",
        "|---|---:|---:|",
    ]
    for row in state_rows:
        lines.append(f"| `{row['repro_state']}` | {row['count']} | {_float(row['share']):.3f} |")
    lines.extend(
        [
            "",
            "## Beispielzeilen",
            "",
            "| Asset | Familie | Phase | Baseline | Folge | Zustand | Baseline-Profil | Folge-Profil |",
            "|---|---|---|---|---|---|---|---|",
        ]
    )
    for row in sample:
        lines.append(
            f"| {row['asset']} | `{row['family']}` | `{row['phase']}` | "
            f"`{row['baseline_dominant_phase_quality']}` | `{row['followup_dominant_phase_quality']}` | "
            f"`{row['repro_state']}` | `{row['baseline_quality_profile']}` | `{row['followup_quality_profile']}` |"
        )
    lines.extend(
        [
            "",
            "## Einordnung",
            "",
            "Der Bericht trennt Namenswiederkehr von Qualitätswiederkehr.",
            "Eine Familie ist erst dann stärker lesbar, wenn sie nicht nur erneut auftaucht, sondern in derselben Phase eine ähnliche lokale Anschlussqualität trägt.",
            "",
            "Wenn viele phasenlokal eigenständige Familien ihre Qualität verlieren, spricht das für echte Kontextdrift.",
            "Wenn ein Teil stabil bleibt, spricht das für lokale Feldrollen, die über neue Weltfenster getragen werden können.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    global BASELINE_CSV, FOLLOWUP_CSV, OUT_CSV, OUT_MD, TITLE
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", default=str(BASELINE_CSV.relative_to(ROOT)))
    parser.add_argument("--followup", default=str(FOLLOWUP_CSV.relative_to(ROOT)))
    parser.add_argument("--out-csv", default=str(OUT_CSV.relative_to(ROOT)))
    parser.add_argument("--out-md", default=str(OUT_MD.relative_to(ROOT)))
    parser.add_argument("--title", default=TITLE)
    args = parser.parse_args()
    BASELINE_CSV = _resolve(args.baseline)
    FOLLOWUP_CSV = _resolve(args.followup)
    OUT_CSV = _resolve(args.out_csv)
    OUT_MD = _resolve(args.out_md)
    TITLE = str(args.title)
    summary, state_rows, details = build_rows()
    _write_csv(OUT_CSV, summary + state_rows + details)
    write_md(summary, state_rows, details)
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"wrote {OUT_CSV.relative_to(ROOT)}")
    print(summary[0])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
