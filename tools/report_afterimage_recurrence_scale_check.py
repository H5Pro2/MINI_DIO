from __future__ import annotations

import csv
from pathlib import Path
from statistics import mean

from report_late_drift_profile_holdout_scan import HOLDOUT_EPISODES


ROOT = Path(__file__).resolve().parents[1]
ANCHORS = ROOT / "docs" / "befunde" / "1961_MEHRWELTLICHE_PREVIEW_ANKER_KONTEXT.csv"
OUT_CSV = ROOT / "docs" / "befunde" / "1963_NACHHALL_REKURRENZ_SKALIERUNG.csv"
OUT_MD = ROOT / "docs" / "befunde" / "1963_NACHHALL_REKURRENZ_SKALIERUNG.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def to_float(value: str | None) -> float:
    try:
        return float(value or 0.0)
    except ValueError:
        return 0.0


def quantile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    idx = min(len(ordered) - 1, max(0, int(round((len(ordered) - 1) * q))))
    return ordered[idx]


def world_stats(world: str, rows: list[dict[str, str]]) -> dict[str, str]:
    afterimage = [to_float(row.get("mini_afterimage")) for row in rows]
    recurrence = [to_float(row.get("mini_recurrence_strength")) for row in rows]
    return {
        "world": world,
        "rows": str(len(rows)),
        "world_avg_afterimage": f"{mean(afterimage):.6f}" if afterimage else "0.000000",
        "world_p90_afterimage": f"{quantile(afterimage, 0.90):.6f}",
        "world_p99_afterimage": f"{quantile(afterimage, 0.99):.6f}",
        "world_avg_recurrence": f"{mean(recurrence):.6f}" if recurrence else "0.000000",
        "world_p90_recurrence": f"{quantile(recurrence, 0.90):.6f}",
        "world_p99_recurrence": f"{quantile(recurrence, 0.99):.6f}",
    }


def collect() -> list[dict[str, str]]:
    anchor_rows = read_csv(ANCHORS)
    by_anchor = {(row["preview_symbol"], row["world"]): row for row in anchor_rows}
    out: list[dict[str, str]] = []
    for world, path in HOLDOUT_EPISODES.items():
        rows = read_csv(path)
        stats = world_stats(world, rows)
        for (symbol, anchor_world), anchor in by_anchor.items():
            if anchor_world != world:
                continue
            anchor_afterimage = to_float(anchor.get("anchor_avg_afterimage"))
            anchor_recurrence = to_float(anchor.get("anchor_avg_recurrence"))
            p90_after = to_float(stats["world_p90_afterimage"])
            p90_rec = to_float(stats["world_p90_recurrence"])
            afterimage_relative = anchor_afterimage / p90_after if p90_after else 0.0
            recurrence_relative = anchor_recurrence / p90_rec if p90_rec else 0.0
            if p90_after == 0.0 and p90_rec == 0.0:
                reading = "skala_praktisch_leer"
            elif afterimage_relative < 0.25 and recurrence_relative < 0.65:
                reading = "anker_unter_weltskala"
            elif afterimage_relative < 0.25:
                reading = "nachhall_unter_weltskala"
            elif recurrence_relative < 0.65:
                reading = "rekurrenz_unter_weltskala"
            else:
                reading = "anker_in_weltskala"
            out.append(
                {
                    "preview_symbol": symbol,
                    **stats,
                    "anchor_avg_afterimage": anchor.get("anchor_avg_afterimage", ""),
                    "anchor_afterimage_vs_p90": f"{afterimage_relative:.6f}",
                    "anchor_avg_recurrence": anchor.get("anchor_avg_recurrence", ""),
                    "anchor_recurrence_vs_p90": f"{recurrence_relative:.6f}",
                    "scale_reading": reading,
                }
            )
    return out


def write_csv(rows: list[dict[str, str]]) -> None:
    fields = list(rows[0].keys()) if rows else []
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_md(rows: list[dict[str, str]]) -> None:
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["scale_reading"]] = counts.get(row["scale_reading"], 0) + 1
    lines = [
        "# 1963 - Nachhall/Rekurrenz-Skalierung",
        "",
        "## Hierarchie der Prüfung",
        "",
        "- Grundfrage: Sind die Preview-Anker oberflächlich, weil Nachhall/Rekurrenz grundsätzlich zu flach sind?",
        "- Unterprüfung: Ankerwerte werden gegen die jeweilige Weltverteilung gelesen.",
        "- Folgeschritt: Nur wenn die Anker unter der Weltskala liegen, ist eine organische Differenzierungsmechanik sinnvoll.",
        "",
        "## Datengrundlage",
        "",
        f"- Quelle: `{ANCHORS.relative_to(ROOT)}`",
        f"- Ergebnis-Tabelle: `{OUT_CSV.relative_to(ROOT)}`",
        "",
        "## Ergebnis",
        "",
        f"- geprüfte Anker/Welt-Kombinationen: {len(rows)}",
        f"- Skalierungslesung: {', '.join(f'{key}:{value}' for key, value in sorted(counts.items()))}",
        "",
        "| Preview | Welt | Lesung | Nachhall/P90 | Rekurrenz/P90 | Welt P90 Nachhall | Welt P90 Rekurrenz |",
        "|---|---|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['preview_symbol']} | {row['world']} | {row['scale_reading']} | {row['anchor_afterimage_vs_p90']} | {row['anchor_recurrence_vs_p90']} | {row['world_p90_afterimage']} | {row['world_p90_recurrence']} |"
        )
    lines.extend(
        [
            "",
            "## Arbeitsdeutung",
            "",
            "Die Anker liegen nicht deshalb oberflächlich, weil die gesamte Welt keine Nachhall-/Rekurrenzskala hätte. Sie liegen selbst unter der jeweiligen Weltskala. Das spricht gegen eine pauschale Feldverstärkung und für spezifische Differenzierung.",
            "",
            "Organisch gelesen: Mini-DIO hat breite wiederkehrende Oberflächenzeichen, aber diese Zeichen bleiben zu wenig an eigene Nachhalltiefe und Rekurrenz gebunden.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes kann eine sanfte organische Erweiterung vorbereitet werden: Preview-Anker sollen nicht härter bewertet werden, sondern eine eigene Tiefenspur bekommen, wenn sie über mehrere Welten wiederkehren und zugleich Profilnähe tragen.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    rows = collect()
    write_csv(rows)
    write_md(rows)
    print(f"rows={len(rows)}")
    for row in rows[:12]:
        print(row["preview_symbol"], row["world"], row["scale_reading"], row["anchor_afterimage_vs_p90"], row["anchor_recurrence_vs_p90"])


if __name__ == "__main__":
    main()
