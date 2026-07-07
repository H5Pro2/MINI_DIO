from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from statistics import fmean


ROOT = Path(__file__).resolve().parents[1]


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    if result != result:
        return 0.0
    return result


def _fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"


def _mean(values: list[float]) -> float:
    return fmean(values) if values else 0.0


def _index(rows: list[dict[str, str]]) -> dict[tuple[str, str], list[dict[str, str]]]:
    result: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        result[(row.get("family", "-"), row.get("transition", "-"))].append(row)
    return result


def _families(rows: list[dict[str, str]]) -> set[str]:
    return {row.get("family", "-") for row in rows if row.get("family")}


def _transitions(rows: list[dict[str, str]]) -> set[str]:
    return {row.get("transition", "-") for row in rows if row.get("transition")}


def _profile(rows: list[dict[str, str]], prefix: str) -> dict[str, float]:
    return {
        "count": float(len(rows)),
        "base_net": _mean([_float(row.get("base_net_return_pct")) for row in rows]),
        "follow_net": _mean([_float(row.get("follow_net_return_pct")) for row in rows]),
        "base_range": _mean([_float(row.get("base_avg_range_pct")) for row in rows]),
        "follow_range": _mean([_float(row.get("follow_avg_range_pct")) for row in rows]),
        "base_hearing_gap": _mean([_float(row.get("base_avg_hearing_gap")) for row in rows]),
        "follow_hearing_gap": _mean([_float(row.get("follow_avg_hearing_gap")) for row in rows]),
        "base_tension": _mean([_float(row.get("base_avg_feld_tension")) for row in rows]),
        "follow_tension": _mean([_float(row.get("follow_avg_feld_tension")) for row in rows]),
    } | {
        f"{prefix}_open_share": _mean([_float(row.get("base_open_share")) for row in rows]),
        f"{prefix}_mature_share": _mean([_float(row.get("base_mature_share")) for row in rows]),
    }


def _family_rows(left: list[dict[str, str]], right: list[dict[str, str]]) -> list[dict[str, object]]:
    left_index = _index(left)
    right_index = _index(right)
    rows: list[dict[str, object]] = []
    for key in sorted(set(left_index) & set(right_index)):
        family, transition = key
        left_rows = left_index[key]
        right_rows = right_index[key]
        left_profile = _profile(left_rows, "left")
        right_profile = _profile(right_rows, "right")
        rows.append(
            {
                "family": family,
                "transition": transition,
                "count_2024": int(left_profile["count"]),
                "count_2025": int(right_profile["count"]),
                "base_net_2024": left_profile["base_net"],
                "base_net_2025": right_profile["base_net"],
                "follow_net_2024": left_profile["follow_net"],
                "follow_net_2025": right_profile["follow_net"],
                "base_range_2024": left_profile["base_range"],
                "base_range_2025": right_profile["base_range"],
                "follow_range_2024": left_profile["follow_range"],
                "follow_range_2025": right_profile["follow_range"],
                "base_hearing_gap_2024": left_profile["base_hearing_gap"],
                "base_hearing_gap_2025": right_profile["base_hearing_gap"],
                "follow_hearing_gap_2024": left_profile["follow_hearing_gap"],
                "follow_hearing_gap_2025": right_profile["follow_hearing_gap"],
                "base_tension_2024": left_profile["base_tension"],
                "base_tension_2025": right_profile["base_tension"],
                "follow_tension_2024": left_profile["follow_tension"],
                "follow_tension_2025": right_profile["follow_tension"],
                "range_delta_abs": abs(right_profile["follow_range"] - left_profile["follow_range"]),
                "hearing_delta_abs": abs(right_profile["follow_hearing_gap"] - left_profile["follow_hearing_gap"]),
                "tension_delta_abs": abs(right_profile["follow_tension"] - left_profile["follow_tension"]),
            }
        )
    return rows


def _write_csv(rows: list[dict[str, object]], out_path: Path) -> None:
    csv_path = out_path.with_suffix(".csv")
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        csv_path.write_text("", encoding="utf-8")
        return
    fields = list(rows[0].keys())
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    key: _fmt(value, 6) if isinstance(value, float) else value
                    for key, value in row.items()
                }
            )


def _count_by_transition(rows: list[dict[str, str]]) -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    for row in rows:
        counts[row.get("transition", "-")] += 1
    return dict(sorted(counts.items()))


def _shared_by_transition(left: list[dict[str, str]], right: list[dict[str, str]]) -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for transition in sorted(_transitions(left) | _transitions(right)):
        left_families = {row.get("family", "-") for row in left if row.get("transition") == transition}
        right_families = {row.get("family", "-") for row in right if row.get("transition") == transition}
        shared = left_families & right_families
        union = left_families | right_families
        result.append(
            {
                "transition": transition,
                "families_2024": len(left_families),
                "families_2025": len(right_families),
                "shared": len(shared),
                "jaccard": len(shared) / max(1, len(union)),
            }
        )
    return result


def _write_md(
    *,
    out_path: Path,
    left_rows: list[dict[str, str]],
    right_rows: list[dict[str, str]],
    shared_rows: list[dict[str, object]],
) -> None:
    _write_csv(shared_rows, out_path)
    title_prefix = out_path.stem.split("_", 1)[0]
    title = (
        f"# {title_prefix} - Wiederkehrende Milieu-Wechsel-Familien"
        if title_prefix.isdigit()
        else "# Wiederkehrende Milieu-Wechsel-Familien"
    )
    left_families = _families(left_rows)
    right_families = _families(right_rows)
    shared_families = left_families & right_families
    union_families = left_families | right_families
    transition_summary = _shared_by_transition(left_rows, right_rows)
    top_stable = sorted(
        shared_rows,
        key=lambda row: (
            float(row["range_delta_abs"])
            + float(row["hearing_delta_abs"])
            + float(row["tension_delta_abs"]),
            -int(row["count_2024"]) - int(row["count_2025"]),
        ),
    )[:25]
    top_active = sorted(
        shared_rows,
        key=lambda row: (-int(row["count_2024"]) - int(row["count_2025"]), str(row["family"])),
    )[:25]

    lines = [
        title,
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose verfolgt Familien, die in 2024 und 2025 mit gleicher Milieu-Wechselrichtung wiederkehren.",
        "Sie bleibt passiv: keine Handlung, kein Gate, keine Richtung.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Welche wiederkehrenden Familien tragen denselben Milieu-Wechsel ueber Weltjahre?",
        "2. Unterpruefung: Wie aehnlich sind Range, Hoeren-Gap und Feldspannung im Folgezustand?",
        "3. Folgeschritt: Stabile Kandidaten mit weiteren Weltfenstern pruefen.",
        "",
        "## Uebersicht",
        "",
        f"- Wechsel-Familien 2024: `{len(left_families)}`",
        f"- Wechsel-Familien 2025: `{len(right_families)}`",
        f"- gemeinsame Familien: `{len(shared_families)}`",
        f"- Familien-Jaccard: `{_fmt(len(shared_families) / max(1, len(union_families)))}`",
        f"- gleiche Familie plus gleicher Wechsel: `{len(shared_rows)}`",
        "",
        "## Wechseltypen",
        "",
        "| Wechsel | Familien 2024 | Familien 2025 | gemeinsam | Jaccard |",
        "|---|---:|---:|---:|---:|",
    ]
    for item in transition_summary:
        lines.append(
            f"| {item['transition']} | {item['families_2024']} | {item['families_2025']} | {item['shared']} | {_fmt(float(item['jaccard']))} |"
        )

    lines.extend(
        [
            "",
            "## Haefigste Wiederkehrfamilien",
            "",
            "| Familie | Wechsel | 2024 | 2025 | Folge Range 2024 | Folge Range 2025 | Folge Hoeren 2024 | Folge Hoeren 2025 | Folge Spannung 2024 | Folge Spannung 2025 |",
            "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in top_active:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["family"]),
                    str(row["transition"]),
                    str(row["count_2024"]),
                    str(row["count_2025"]),
                    _fmt(float(row["follow_range_2024"])),
                    _fmt(float(row["follow_range_2025"])),
                    _fmt(float(row["follow_hearing_gap_2024"])),
                    _fmt(float(row["follow_hearing_gap_2025"])),
                    _fmt(float(row["follow_tension_2024"])),
                    _fmt(float(row["follow_tension_2025"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Rohwelt-nahe Kandidaten",
            "",
            "Diese Tabelle sortiert nach kleiner Differenz in Folge-Range, Folge-Hoeren-Gap und Folge-Feldspannung.",
            "",
            "| Familie | Wechsel | Delta Range | Delta Hoeren | Delta Spannung | 2024 | 2025 |",
            "|---|---|---:|---:|---:|---:|---:|",
        ]
    )
    for row in top_stable:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["family"]),
                    str(row["transition"]),
                    _fmt(float(row["range_delta_abs"])),
                    _fmt(float(row["hearing_delta_abs"])),
                    _fmt(float(row["tension_delta_abs"])),
                    str(row["count_2024"]),
                    str(row["count_2025"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Gleiche Familie plus gleicher Wechsel bedeutet nicht, dass die Weltphase identisch ist.",
            "Es zeigt aber, dass dieselbe interne Familienlage in unterschiedlichen Weltjahren erneut in dieselbe Milieu-Bewegung geraten kann.",
            "",
            "Die Rohwelt-nahe Kandidaten sind die naechste Pruefflaeche.",
            "Dort ist die Aehnlichkeit von Folge-Range, Hoeren-Gap und Feldspannung am hoechsten.",
            "",
            "## Grenze",
            "",
            "Dieser Bericht beweist keinen Ausloeser.",
            "Er isoliert Kandidaten fuer weitere Ruecklesung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollten die rohweltnahen Kandidaten gegen ein weiteres Jahr oder ein anderes Assetfenster verfolgt werden. Wichtig ist, ob dieselbe Familie bei aehnlichem Folgeprofil erneut dieselbe Milieu-Bewegung zeigt.",
            "",
        ]
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Vergleicht wiederkehrende adaptive Milieu-Wechsel-Familien.")
    parser.add_argument("--left", required=True)
    parser.add_argument("--right", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    left_rows = _load_csv(_resolve(args.left))
    right_rows = _load_csv(_resolve(args.right))
    shared_rows = _family_rows(left_rows, right_rows)
    _write_md(
        out_path=_resolve(args.out_md),
        left_rows=left_rows,
        right_rows=right_rows,
        shared_rows=shared_rows,
    )
    print(
        {
            "out_md": str(_resolve(args.out_md)),
            "rows": len(shared_rows),
            "left_transitions": _count_by_transition(left_rows),
            "right_transitions": _count_by_transition(right_rows),
        }
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
