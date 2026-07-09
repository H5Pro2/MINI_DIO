from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path

from befunde_paths import befunde_root


ROOT = Path(__file__).resolve().parents[1]

DEFAULT_CORE = befunde_root(ROOT) / "1865_LOKALE_REIFEGRUPPE_HARTER_KERN.csv"
DEFAULT_OUT_CSV = befunde_root(ROOT) / "1868_SOL_HARTKERN_WELTLAGENREAKTION.csv"
DEFAULT_OUT_MD = befunde_root(ROOT) / "1868_SOL_HARTKERN_WELTLAGENREAKTION.md"


def _resolve(path: str) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return ROOT / candidate


def _read_core(path: Path, asset: str) -> dict[tuple[str, str, str], dict[str, str]]:
    rows: dict[tuple[str, str, str], dict[str, str]] = {}
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row.get("row_type") != "core_intersection_detail":
                continue
            if row.get("core_state") != "harter_kern_reproduziert":
                continue
            if row.get("asset") != asset:
                continue
            key = (row.get("asset", ""), row.get("family", ""), row.get("phase", ""))
            rows[key] = row
    return rows


def _read_followup(path: Path) -> dict[tuple[str, str, str], dict[str, str]]:
    rows: dict[tuple[str, str, str], dict[str, str]] = {}
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row.get("row_type") != "family_phase_repro_detail":
                continue
            key = (row.get("asset", ""), row.get("family", ""), row.get("phase", ""))
            rows[key] = row
    return rows


def _parse_followup(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("followup must be NAME=path.csv")
    name, path = value.split("=", 1)
    return name.strip(), _resolve(path.strip())


def _counter_text(counter: Counter[str]) -> str:
    return "; ".join(f"{key}:{value}" for key, value in counter.most_common()) or "-"


def build_rows(core_path: Path, followups: list[tuple[str, Path]], asset: str) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    core = _read_core(core_path, asset)
    detail_rows: list[dict[str, str]] = []
    summary_rows: list[dict[str, str]] = []
    for condition, path in followups:
        follow = _read_followup(path)
        state_counter: Counter[str] = Counter()
        quality_counter: Counter[str] = Counter()
        for key, core_row in sorted(core.items()):
            follow_row = follow.get(key)
            state = (follow_row or {}).get("repro_state", "fehlt_im_folgefenster")
            follow_quality = (follow_row or {}).get("followup_dominant_phase_quality", "")
            state_counter[state] += 1
            if follow_quality:
                quality_counter[follow_quality] += 1
            detail_rows.append(
                {
                    "row_type": "worldstate_core_detail",
                    "condition": condition,
                    "asset": key[0],
                    "family": key[1],
                    "phase": key[2],
                    "baseline_quality": core_row.get("baseline_dominant_phase_quality", ""),
                    "followup_state": state,
                    "followup_quality": follow_quality,
                    "first_core_quality": core_row.get("first_followup_quality", ""),
                    "second_core_quality": core_row.get("second_followup_quality", ""),
                }
            )
        summary_rows.append(
            {
                "row_type": "worldstate_core_summary",
                "condition": condition,
                "asset": asset,
                "core_pairs": str(len(core)),
                "state_profile": _counter_text(state_counter),
                "quality_profile": _counter_text(quality_counter),
            }
        )
    return summary_rows, detail_rows


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields: list[str] = []
    seen: set[str] = set()
    for row in rows:
        for key in row:
            if key not in seen:
                fields.append(key)
                seen.add(key)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, summary_rows: list[dict[str, str]], detail_rows: list[dict[str, str]], asset: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    by_condition: defaultdict[str, list[dict[str, str]]] = defaultdict(list)
    for row in detail_rows:
        by_condition[row["condition"]].append(row)
    lines = [
        f"# {asset}-Hartkern: Weltlagenreaktion",
        "",
        f"Diese Prüfung liest nur die {asset}-Paare aus dem harten Kern der lokalen Reifegruppe.",
        f"Damit wird nicht mehr die ganze Baseline verglichen, sondern die Frage: Wie reagiert der harte {asset}-Kern unter den geprüften Weltlagen?",
        "",
        "## Ergebnis",
        "",
        "| Weltlage | Kernpaare | Zustandsprofil | Qualitätsprofil |",
        "|---|---:|---|---|",
    ]
    for row in summary_rows:
        lines.append(
            f"| {row['condition']} | {row['core_pairs']} | `{row['state_profile']}` | `{row['quality_profile']}` |"
        )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Der SOL-Hartkern bleibt unter allen drei Weltlagen teilweise reproduzierbar.",
            "Stress zeigt in dieser Prüfung etwas mehr direkte lokale Reproduktion als ruhige Welt und Expansion.",
            "Expansion verschiebt stärker in Nachhall- und Kernnähe. Das spricht nicht für Kollaps, sondern für eine unterschiedliche Randantwort je Weltspannung.",
            "",
            "Wichtig: Das ist weiterhin eine passive Feldlesung. Es wird keine Handlung, kein Gate und keine Richtung daraus abgeleitet.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare hard-core local maturity pairs against worldstate followups.")
    parser.add_argument("--core", default=str(DEFAULT_CORE.relative_to(ROOT)))
    parser.add_argument("--asset", default="SOL")
    parser.add_argument("--followup", action="append", type=_parse_followup, required=True)
    parser.add_argument("--out-csv", default=str(DEFAULT_OUT_CSV.relative_to(ROOT)))
    parser.add_argument("--out-md", default=str(DEFAULT_OUT_MD.relative_to(ROOT)))
    args = parser.parse_args()

    summary_rows, detail_rows = build_rows(_resolve(args.core), args.followup, args.asset.upper())
    _write_csv(_resolve(args.out_csv), summary_rows + detail_rows)
    _write_md(_resolve(args.out_md), summary_rows, detail_rows, args.asset.upper())
    print({"summaries": summary_rows, "details": len(detail_rows)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
