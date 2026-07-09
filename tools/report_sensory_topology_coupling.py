from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


DEFAULT_INPUTS = [
    "docs/befunde/1001-2000/1001-1500/1225_AKTUELLE_REZEPTORSCHICHT_STRESS_QUIET_FELDPHASEN_SEGMENTE.csv",
    "docs/befunde/1001-2000/1001-1500/1227_AKTUELLE_REZEPTORSCHICHT_STRESS_QUIET_FELDPHASEN_1H_SEGMENTE.csv",
    "docs/befunde/1001-2000/1001-1500/1229_SYNTHETISCHE_SINNESACHSEN_STRESS_FELDPHASEN_SEGMENTE.csv",
]


def _float(row: dict[str, str], key: str) -> float:
    try:
        value = float(row.get(key, "") or 0.0)
    except ValueError:
        return 0.0
    return 0.0 if value != value else value


def _int(row: dict[str, str], key: str) -> int:
    try:
        return int(float(row.get(key, "") or 0.0))
    except ValueError:
        return 0


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _source_label(path: Path) -> str:
    name = path.stem
    if name.startswith("1225_"):
        return "REAL_5M_RECEPTOR"
    if name.startswith("1227_"):
        return "REAL_1H_RECEPTOR"
    if name.startswith("1229_"):
        return "SYNTH_SENSORY_AXES"
    return name


def _empty_bucket() -> dict[str, float]:
    return {
        "segments": 0.0,
        "duration": 0.0,
        "raw_field": 0.0,
        "auditory": 0.0,
        "visual": 0.0,
        "rekopplung": 0.0,
        "strain": 0.0,
    }


def _add(bucket: dict[str, float], row: dict[str, str]) -> None:
    duration = max(1, _int(row, "duration"))
    bucket["segments"] += 1.0
    bucket["duration"] += float(duration)
    bucket["raw_field"] += _float(row, "avg_raw_field_intake") * duration
    bucket["auditory"] += _float(row, "avg_auditory_loudness") * duration
    bucket["visual"] += _float(row, "avg_visual_sharpness") * duration
    bucket["rekopplung"] += _float(row, "avg_rekopplung") * duration
    bucket["strain"] += _float(row, "avg_strain") * duration


def _finish(label: str, source: str, bucket: dict[str, float]) -> dict[str, object]:
    duration = max(1.0, bucket["duration"])
    raw = bucket["raw_field"] / duration
    auditory = bucket["auditory"] / duration
    visual = bucket["visual"] / duration
    rekopplung = bucket["rekopplung"] / duration
    strain = bucket["strain"] / duration
    return {
        "source": source,
        "role": label,
        "segments": int(bucket["segments"]),
        "duration": int(bucket["duration"]),
        "avg_raw_field_intake": round(raw, 6),
        "avg_auditory_loudness": round(auditory, 6),
        "avg_visual_sharpness": round(visual, 6),
        "avg_rekopplung": round(rekopplung, 6),
        "avg_strain": round(strain, 6),
        "sensory_signature": _signature(raw, auditory, visual, rekopplung, strain),
    }


def _signature(raw: float, auditory: float, visual: float, rekopplung: float, strain: float) -> str:
    parts: list[str] = []
    if auditory >= 0.24:
        parts.append("laut")
    elif auditory <= 0.16:
        parts.append("leise")
    else:
        parts.append("mittelton")

    if visual >= 0.67:
        parts.append("scharf")
    elif visual <= 0.62:
        parts.append("unscharf")
    else:
        parts.append("mittelsicht")

    if raw >= 0.18:
        parts.append("feldstark")
    elif raw <= 0.10:
        parts.append("feldduenn")
    else:
        parts.append("feldmittel")

    if rekopplung >= 0.70 and strain <= 0.17:
        parts.append("getragen")
    elif strain >= 0.24:
        parts.append("angespannt")
    else:
        parts.append("offen")
    return "_".join(parts)


def _collect(paths: list[Path]) -> list[dict[str, object]]:
    buckets: dict[tuple[str, str], dict[str, float]] = defaultdict(_empty_bucket)
    for path in paths:
        source = _source_label(path)
        for row in _load(path):
            role = str(row.get("role", "") or "unknown")
            _add(buckets[(source, role)], row)
    rows = [_finish(role, source, bucket) for (source, role), bucket in sorted(buckets.items())]
    return rows


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    by_role: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        by_role[str(row["role"])].append(row)

    lines = [
        "# Sinnesaufnahme gegen Topologie",
        "",
        "Passive Kopplungspruefung: Welche Hoer-/Seh-/Fuehl-Konstellationen begleiten welche Feldrollen?",
        "",
        "Quelle sind Feldphasen-Segmentdateien. Es wird keine Handlung, kein Gate und keine Richtung abgeleitet.",
        "",
        "## Rollenmatrix",
        "",
        "| Quelle | Rolle | Segmente | Dauer | Lautheit | Sicht | Rohfeld | Rekopplung | Strain | Signatur |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            "| {source} | {role} | {segments} | {duration} | {avg_auditory_loudness:.4f} | {avg_visual_sharpness:.4f} | {avg_raw_field_intake:.4f} | {avg_rekopplung:.4f} | {avg_strain:.4f} | {sensory_signature} |".format(
                **row
            )
        )

    lines.extend(["", "## Rollenlesung", ""])
    for role, items in sorted(by_role.items()):
        strongest_raw = max(items, key=lambda item: float(item["avg_raw_field_intake"]))
        strongest_rec = max(items, key=lambda item: float(item["avg_rekopplung"]))
        sharpest = max(items, key=lambda item: float(item["avg_visual_sharpness"]))
        loudest = max(items, key=lambda item: float(item["avg_auditory_loudness"]))
        lines.extend(
            [
                f"### {role}",
                "",
                f"- Staerkster Feldkontakt: `{strongest_raw['source']}` mit `{float(strongest_raw['avg_raw_field_intake']):.4f}`.",
                f"- Staerkste Rekopplung: `{strongest_rec['source']}` mit `{float(strongest_rec['avg_rekopplung']):.4f}`.",
                f"- Schaerfste Sicht: `{sharpest['source']}` mit `{float(sharpest['avg_visual_sharpness']):.4f}`.",
                f"- Lauteste Aufnahme: `{loudest['source']}` mit `{float(loudest['avg_auditory_loudness']):.4f}`.",
                "",
            ]
        )

    lines.extend(
        [
            "## Befund",
            "",
            "Die Feldrollen tragen unterschiedliche Sinnesprofile. Damit ist die Topologie nicht nur eine abstrakte Rolle, sondern mit Aufnahmequalitaet gekoppelt.",
            "",
            "Zentrum und Rekopplungsnaehe muessen nicht maximal laut sein. Sie entstehen eher dort, wo Feldkontakt, Sicht und Rekopplung zusammen tragbar bleiben.",
            "",
            "Rand/Kipp entsteht nicht nur aus Lautheit. Entscheidend ist die Kombination aus Feldaufnahme, Strain und schwacherer Tragfaehigkeit.",
            "",
            "## Bewertung",
            "",
            "Die Sinnesregulation ist dadurch fachlich enger gefasst: Sie muss nicht das MCM-Feld selbst steuern, sondern die Aufnahmequalitaet vor dem Feld lesbar machen.",
            "",
            "Das passt zur aktuellen Trennung:",
            "",
            "```text",
            "Sehen / Hoeren / Fuehlen -> Rezeptorschicht -> MCM-Feldtopologie",
            "```",
            "",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", action="append")
    parser.add_argument("--out", default="docs/befunde/1001-2000/1001-1500/1274_SINNESAUFNAHME_TOPOLOGIE_KOPPLUNG.md")
    parser.add_argument("--csv-out", default="docs/befunde/1001-2000/1001-1500/1274_SINNESAUFNAHME_TOPOLOGIE_KOPPLUNG.csv")
    args = parser.parse_args()

    paths = [Path(item) for item in (args.input or DEFAULT_INPUTS)]
    rows = _collect(paths)
    _write_csv(rows, Path(args.csv_out))
    _write_markdown(rows, Path(args.out))
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
