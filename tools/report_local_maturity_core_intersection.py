from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DEFAULT_FIRST = ROOT / "docs" / "befunde" / "1861_PHASENLOKALE_FAMILIEN_REPRO_FOLGEFENSTER.csv"
DEFAULT_SECOND = ROOT / "docs" / "befunde" / "1864_LOKALE_REIFEGRUPPE_REPRO_WEITERE_FENSTER.csv"
DEFAULT_OUT_CSV = ROOT / "docs" / "befunde" / "1865_LOKALE_REIFEGRUPPE_HARTER_KERN.csv"
DEFAULT_OUT_MD = ROOT / "docs" / "befunde" / "1865_LOKALE_REIFEGRUPPE_HARTER_KERN.md"


CORE_STATE = "lokale_qualitaet_reproduziert"
BASELINE_STATE = "phasenlokal_eigenstaendig"


def _resolve(path: str) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return ROOT / candidate


def _read_details(path: Path) -> dict[tuple[str, str, str], dict[str, str]]:
    rows: dict[tuple[str, str, str], dict[str, str]] = {}
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row.get("row_type") != "family_phase_repro_detail":
                continue
            if row.get("baseline_stability_state") != BASELINE_STATE:
                continue
            key = (row.get("asset", ""), row.get("family", ""), row.get("phase", ""))
            rows[key] = row
    return rows


def _reproduces(row: dict[str, str] | None) -> bool:
    if not row:
        return False
    if row.get("repro_state") != CORE_STATE:
        return False
    return row.get("baseline_dominant_phase_quality") == row.get("followup_dominant_phase_quality")


def _row_state(first: dict[str, str] | None, second: dict[str, str] | None) -> str:
    first_ok = _reproduces(first)
    second_ok = _reproduces(second)
    if first_ok and second_ok:
        return "harter_kern_reproduziert"
    if first_ok:
        return "nur_erste_folge_reproduziert"
    if second_ok:
        return "nur_zweite_folge_reproduziert"
    if first is None or second is None:
        return "fehlt_in_einer_folge"
    return "kein_harter_kern"


def _safe_float(value: str) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def build_rows(first_path: Path, second_path: Path) -> list[dict[str, object]]:
    first = _read_details(first_path)
    second = _read_details(second_path)
    keys = sorted(set(first) | set(second))
    rows: list[dict[str, object]] = []
    for key in keys:
        asset, family, phase = key
        first_row = first.get(key)
        second_row = second.get(key)
        baseline_quality = ""
        if first_row:
            baseline_quality = first_row.get("baseline_dominant_phase_quality", "")
        elif second_row:
            baseline_quality = second_row.get("baseline_dominant_phase_quality", "")
        rows.append(
            {
                "row_type": "core_intersection_detail",
                "asset": asset,
                "family": family,
                "phase": phase,
                "baseline_dominant_phase_quality": baseline_quality,
                "core_state": _row_state(first_row, second_row),
                "first_repro_state": (first_row or {}).get("repro_state", "fehlt"),
                "second_repro_state": (second_row or {}).get("repro_state", "fehlt"),
                "first_followup_quality": (first_row or {}).get("followup_dominant_phase_quality", ""),
                "second_followup_quality": (second_row or {}).get("followup_dominant_phase_quality", ""),
                "first_observations": (first_row or {}).get("followup_observations", ""),
                "second_observations": (second_row or {}).get("followup_observations", ""),
                "first_mean_rekopplung_edge": _safe_float((first_row or {}).get("followup_mean_rekopplung_edge", "")),
                "second_mean_rekopplung_edge": _safe_float((second_row or {}).get("followup_mean_rekopplung_edge", "")),
                "first_mean_afterimage_edge": _safe_float((first_row or {}).get("followup_mean_afterimage_edge", "")),
                "second_mean_afterimage_edge": _safe_float((second_row or {}).get("followup_mean_afterimage_edge", "")),
                "first_mean_temporal_edge": _safe_float((first_row or {}).get("followup_mean_temporal_edge", "")),
                "second_mean_temporal_edge": _safe_float((second_row or {}).get("followup_mean_temporal_edge", "")),
            }
        )
    return rows


def _counter_text(counter: Counter[str]) -> str:
    return "; ".join(f"{key}:{value}" for key, value in counter.most_common()) or "-"


def _write_csv(path: Path, rows: list[dict[str, object]], summary: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "row_type",
        "first",
        "second",
        "baseline_pairs",
        "core_state_profile",
        "asset_core_profile",
        "quality_core_profile",
        "asset",
        "family",
        "phase",
        "baseline_dominant_phase_quality",
        "core_state",
        "first_repro_state",
        "second_repro_state",
        "first_followup_quality",
        "second_followup_quality",
        "first_observations",
        "second_observations",
        "first_mean_rekopplung_edge",
        "second_mean_rekopplung_edge",
        "first_mean_afterimage_edge",
        "second_mean_afterimage_edge",
        "first_mean_temporal_edge",
        "second_mean_temporal_edge",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerow({"row_type": "summary", **summary})
        for row in rows:
            writer.writerow(row)


def _write_md(path: Path, rows: list[dict[str, object]], summary: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    core_rows = [row for row in rows if row["core_state"] == "harter_kern_reproduziert"]
    lines = [
        "# 1865 - Lokale Reifegruppe: harter Kern",
        "",
        "Diese Prüfung vergleicht zwei unabhängige Folgeprüfungen der phasenlokalen Familienqualität.",
        "Gesucht wird nicht jede Wiederkehr, sondern die Schnittmenge: Familien-Phasen-Paare, die in beiden Folgeprüfungen dieselbe lokale Qualität halten.",
        "",
        "## Ergebnis",
        "",
        f"- Baseline-Paare: `{summary['baseline_pairs']}`",
        f"- Zustandsprofil: `{summary['core_state_profile']}`",
        f"- Asset-Profil: `{summary['asset_core_profile']}`",
        f"- Qualitätsprofil: `{summary['quality_core_profile']}`",
        "",
        "## Lesung",
        "",
        "Der harte Kern ist kleiner als die einzelne Reproduktion, aber fachlich stärker.",
        "Er beschreibt die Paare, die nicht nur in einem Folgefenster stabil erscheinen, sondern über zwei verschiedene Folgeprüfungen dieselbe lokale Qualität tragen.",
        "Damit wird die lokale Reifegruppe als Kern mit Randdrift lesbar: Der Kern hält, während Randbereiche offen, nullnah, nachhallnah oder kontextabhängig werden.",
        "",
        "Das bleibt passiv. Der Befund erzeugt keine Handlung und keine Regel. Er markiert nur eine stabilere Innenfeldgruppe innerhalb der bisherigen Bedeutungsverdichtung.",
        "",
        "## Top-Kernpaare",
        "",
        "| Asset | Familie | Phase | Qualität | Folge 1 | Folge 2 |",
        "|---|---|---|---|---|---|",
    ]
    for row in core_rows[:40]:
        lines.append(
            "| {asset} | {family} | {phase} | {quality} | {first} | {second} |".format(
                asset=row["asset"],
                family=row["family"],
                phase=row["phase"],
                quality=row["baseline_dominant_phase_quality"],
                first=row["first_observations"],
                second=row["second_observations"],
            )
        )
    lines.extend(
        [
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte geprüft werden, ob dieser harte Kern bei neuen Welten nur stabil bleibt oder ob einzelne Kernpaare unter Stress/Expansion gezielt in Randdrift wechseln. Das wäre der nächste Test für Reife statt bloßer Wiederholung.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build hard-core intersection for local maturity repro reports.")
    parser.add_argument("--first", default=str(DEFAULT_FIRST.relative_to(ROOT)))
    parser.add_argument("--second", default=str(DEFAULT_SECOND.relative_to(ROOT)))
    parser.add_argument("--out-csv", default=str(DEFAULT_OUT_CSV.relative_to(ROOT)))
    parser.add_argument("--out-md", default=str(DEFAULT_OUT_MD.relative_to(ROOT)))
    args = parser.parse_args()

    first_path = _resolve(args.first)
    second_path = _resolve(args.second)
    out_csv = _resolve(args.out_csv)
    out_md = _resolve(args.out_md)
    rows = build_rows(first_path, second_path)

    state_counter = Counter(str(row["core_state"]) for row in rows)
    asset_counter = Counter(
        f"{row['asset']}::{row['core_state']}" for row in rows if row["core_state"] == "harter_kern_reproduziert"
    )
    quality_counter = Counter(
        str(row["baseline_dominant_phase_quality"])
        for row in rows
        if row["core_state"] == "harter_kern_reproduziert"
    )
    summary = {
        "first": str(first_path.relative_to(ROOT)),
        "second": str(second_path.relative_to(ROOT)),
        "baseline_pairs": len(rows),
        "core_state_profile": _counter_text(state_counter),
        "asset_core_profile": _counter_text(asset_counter),
        "quality_core_profile": _counter_text(quality_counter),
    }
    _write_csv(out_csv, rows, summary)
    _write_md(out_md, rows, summary)
    print(summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
