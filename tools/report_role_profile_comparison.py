from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


FIELDS = (
    ("avg_raw_field_intake", "raw"),
    ("avg_auditory_loudness", "loudness"),
    ("avg_visual_sharpness", "sharpness"),
    ("avg_rekopplung", "rekopplung"),
    ("avg_strain", "strain"),
)


def _float(row: dict[str, str], key: str) -> float:
    try:
        return float(row.get(key, "") or 0.0)
    except ValueError:
        return 0.0


def _int(row: dict[str, str], key: str) -> int:
    try:
        return int(float(row.get(key, "") or 0))
    except ValueError:
        return 0


def _parse_segments(value: str) -> tuple[str, Path]:
    parts = value.split("=", 1)
    if len(parts) != 2:
        raise argparse.ArgumentTypeError("segment source must use LABEL=CSV")
    return parts[0], Path(parts[1])


def _load(source_label: str, path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            role = row.get("role") or row.get("role_group") or "-"
            world = row.get("world", "-") or "-"
            duration = max(1, _int(row, "duration"))
            rows.append(
                {
                    "source": source_label,
                    "world": world,
                    "role": role,
                    "duration": duration,
                    "raw": _float(row, "avg_raw_field_intake"),
                    "loudness": _float(row, "avg_auditory_loudness"),
                    "sharpness": _float(row, "avg_visual_sharpness"),
                    "rekopplung": _float(row, "avg_rekopplung"),
                    "strain": _float(row, "avg_strain"),
                }
            )
    return rows


def _aggregate(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    totals: dict[tuple[str, str], int] = defaultdict(int)
    grouped: dict[tuple[str, str, str], dict[str, float]] = defaultdict(
        lambda: {
            "segments": 0.0,
            "duration": 0.0,
            "raw": 0.0,
            "loudness": 0.0,
            "sharpness": 0.0,
            "rekopplung": 0.0,
            "strain": 0.0,
        }
    )
    for row in rows:
        source = str(row["source"])
        world = str(row["world"])
        role = str(row["role"])
        duration = int(row["duration"])
        totals[(source, world)] += duration
        item = grouped[(source, world, role)]
        item["segments"] += 1
        item["duration"] += duration
        for _field_name, short in FIELDS:
            item[short] += float(row[short]) * duration

    out: list[dict[str, object]] = []
    for (source, world, role), item in sorted(grouped.items()):
        duration = max(1.0, item["duration"])
        total = max(1, totals[(source, world)])
        raw = item["raw"] / duration
        loudness = item["loudness"] / duration
        sharpness = item["sharpness"] / duration
        rekopplung = item["rekopplung"] / duration
        strain = item["strain"] / duration
        out.append(
            {
                "source": source,
                "world": world,
                "role": role,
                "segments": int(item["segments"]),
                "duration": int(duration),
                "duration_share": round(duration / total, 6),
                "avg_raw_field_intake": round(raw, 6),
                "avg_auditory_loudness": round(loudness, 6),
                "avg_visual_sharpness": round(sharpness, 6),
                "avg_rekopplung": round(rekopplung, 6),
                "avg_strain": round(strain, 6),
                "load_signature": _signature(raw, loudness, sharpness, rekopplung, strain),
            }
        )
    return out


def _signature(raw: float, loudness: float, sharpness: float, rekopplung: float, strain: float) -> str:
    if loudness >= 0.60 and sharpness >= 0.70:
        return "hoerlast_bei_lesbarer_form"
    if loudness >= 0.60 and raw >= 0.34 and rekopplung <= 0.63 and strain >= 0.25:
        return "gekoppelte_feldlast"
    if sharpness <= 0.58 and loudness < 0.60:
        return "formbruch_ohne_starke_hoerlast"
    if rekopplung >= 0.71 and strain <= 0.15:
        return "rekopplung_zentrumsnah"
    if raw <= 0.10 and loudness <= 0.16:
        return "ruhige_feldnaehe"
    return "gemischte_feldlage"


def _write_csv(rows: list[dict[str, object]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(rows: list[dict[str, object]], out: Path, title: str) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    rand_rows = [row for row in rows if row["role"] == "spannungsrand_kippnaehe"]
    strongest_loud = sorted(rand_rows, key=lambda row: float(row["avg_auditory_loudness"]), reverse=True)[:6]
    strongest_strain = sorted(rand_rows, key=lambda row: float(row["avg_strain"]), reverse=True)[:6]

    lines = [
        f"# {title}",
        "",
        "## Grundfrage",
        "",
        "Liegen reale Rand/Kipp-Rollen naeher an Hoerlast, Formbruch oder gekoppelter Feldlast?",
        "",
        "Diese Diagnose vergleicht aggregierte Rollenprofile aus synthetischen und realen Segmentdateien. Sie ist passiv und erzeugt keine Runtime-Regel.",
        "",
        "## Rollenprofile",
        "",
        "| Quelle | Welt | Rolle | Daueranteil | Rohfeld | Lautheit | Schaerfe | Rekopplung | Strain | Signatur |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            "| {source} | {world} | {role} | {duration_share:.4f} | {avg_raw_field_intake:.4f} | {avg_auditory_loudness:.4f} | {avg_visual_sharpness:.4f} | {avg_rekopplung:.4f} | {avg_strain:.4f} | {load_signature} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Staerkste Rand/Kipp-Lautheit",
            "",
        ]
    )
    for row in strongest_loud:
        lines.append(
            "- `{source}` / `{world}`: Lautheit `{avg_auditory_loudness:.4f}`, Rohfeld `{avg_raw_field_intake:.4f}`, Schaerfe `{avg_visual_sharpness:.4f}`, Rekopplung `{avg_rekopplung:.4f}`, Strain `{avg_strain:.4f}`, Signatur `{load_signature}`".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Staerkster Rand/Kipp-Strain",
            "",
        ]
    )
    for row in strongest_strain:
        lines.append(
            "- `{source}` / `{world}`: Strain `{avg_strain:.4f}`, Lautheit `{avg_auditory_loudness:.4f}`, Rohfeld `{avg_raw_field_intake:.4f}`, Schaerfe `{avg_visual_sharpness:.4f}`, Signatur `{load_signature}`".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Ableitung",
            "",
            "Wenn Rand/Kipp hohe Lautheit, hohes Rohfeld, sinkende Rekopplung und hohen Strain gemeinsam zeigt, ist die Rolle als gekoppelte Feldlast zu lesen.",
            "",
            "Wenn Lautheit hoch bleibt, die visuelle Schaerfe aber ebenfalls hoch bleibt, spricht das fuer Hoerlast bei lesbarer Form.",
            "",
            "Wenn visuelle Schaerfe niedrig ist, aber Lautheit nicht stark steigt, spricht das eher fuer Formbruch ohne starke Hoerlast.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollten die realen `gekoppelte_feldlast`-Fenster gegen die Rohweltsequenz gelesen werden. Ziel ist zu sehen, ob diese Rolle an Bewegungsbruch, Expansion oder Rekopplungsversuch gebunden ist.",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--segments", action="append", required=True, type=_parse_segments)
    parser.add_argument("--out", required=True)
    parser.add_argument("--csv-out", required=True)
    parser.add_argument("--title", default="Rollenprofil Vergleich")
    args = parser.parse_args()

    all_rows: list[dict[str, object]] = []
    for label, path in args.segments:
        all_rows.extend(_load(label, path))
    rows = _aggregate(all_rows)
    _write_csv(rows, Path(args.csv_out))
    _write_md(rows, Path(args.out), args.title)
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
