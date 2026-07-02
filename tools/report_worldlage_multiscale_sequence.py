from __future__ import annotations

import argparse
import csv
from pathlib import Path


DEFAULT_INPUTS = [
    ("100", "docs/befunde/1305_WELTLAGEN_FOLGEMEMORY_BLOCK100.csv"),
    ("200", "docs/befunde/1303_WELTLAGEN_FOLGEMEMORY_MEHRWELTEN.csv"),
    ("400", "docs/befunde/1306_WELTLAGEN_FOLGEMEMORY_BLOCK400.csv"),
]


def _parse_input(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("input must be SCALE=PATH")
    scale, path = value.split("=", 1)
    return scale, Path(path)


def _load_rows(inputs: list[tuple[str, Path]]) -> dict[str, dict[str, dict[str, object]]]:
    by_sequence: dict[str, dict[str, dict[str, object]]] = {}
    for scale, path in inputs:
        with path.open("r", encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                sequence = str(row["worldlage_sequence"])
                by_sequence.setdefault(sequence, {})[scale] = row
    return by_sequence


def _float(row: dict[str, object], key: str) -> float:
    try:
        return float(row.get(key, 0.0) or 0.0)
    except (TypeError, ValueError):
        return 0.0


def _int(row: dict[str, object], key: str) -> int:
    try:
        return int(float(row.get(key, 0) or 0))
    except (TypeError, ValueError):
        return 0


def _classify_scale_profile(scale_rows: dict[str, dict[str, object]]) -> str:
    outcomes = [str(row.get("dominant_outcome", "unknown")) for row in scale_rows.values()]
    if not outcomes:
        return "unknown"
    unique = set(outcomes)
    if unique == {"neutral"}:
        return "stabil_neutral"
    if unique == {"beruhigend"}:
        return "stabil_beruhigend"
    if unique <= {"neutral", "beruhigend"}:
        return "skalenabhaengig_neutral_beruhigend"
    if "verschiebend" in unique:
        return "skalenabhaengig_mit_verschiebung"
    return "gemischt"


def _sequence_row(sequence: str, scale_rows: dict[str, dict[str, object]], scales: list[str]) -> dict[str, object]:
    occurrences_total = sum(_int(row, "occurrences") for row in scale_rows.values())
    avg_delta_rand = sum(_float(row, "avg_delta_rand") for row in scale_rows.values()) / max(1, len(scale_rows))
    avg_delta_zentrum = sum(_float(row, "avg_delta_zentrum") for row in scale_rows.values()) / max(1, len(scale_rows))
    avg_delta_rekopplung = sum(_float(row, "avg_delta_rekopplung") for row in scale_rows.values()) / max(1, len(scale_rows))
    avg_delta_strain = sum(_float(row, "avg_delta_strain") for row in scale_rows.values()) / max(1, len(scale_rows))
    row: dict[str, object] = {
        "worldlage_sequence": sequence,
        "scale_presence": ",".join(scale for scale in scales if scale in scale_rows),
        "scale_count": len(scale_rows),
        "occurrences_total": occurrences_total,
        "multiscale_profile": _classify_scale_profile(scale_rows),
        "avg_delta_zentrum_over_scales": round(avg_delta_zentrum, 6),
        "avg_delta_rand_over_scales": round(avg_delta_rand, 6),
        "avg_delta_rekopplung_over_scales": round(avg_delta_rekopplung, 6),
        "avg_delta_strain_over_scales": round(avg_delta_strain, 6),
        "passive_only": 1,
        "influences_action": 0,
    }
    for scale in scales:
        scale_row = scale_rows.get(scale, {})
        row[f"outcome_{scale}"] = scale_row.get("dominant_outcome", "-")
        row[f"occurrences_{scale}"] = scale_row.get("occurrences", 0)
    return row


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    profile_counts: dict[str, int] = {}
    for row in rows:
        profile = str(row["multiscale_profile"])
        profile_counts[profile] = profile_counts.get(profile, 0) + 1

    lines = [
        "# Mehrskalige Weltlagen-Folgememory",
        "",
        "Diese Auswertung vergleicht dieselben Lagefolgen ueber mehrere zeitliche Lesetiefen.",
        "",
        "Verwendete Skalen:",
        "",
        "- Block `100`: kurze Lagebewegung",
        "- Block `200`: mittlere Lagefolge",
        "- Block `400`: laengere Feldphase",
        "",
        "## Profilverteilung",
        "",
    ]
    for profile, count in sorted(profile_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- `{profile}`: `{count}`")

    lines.extend(
        [
            "",
            "## Stabilste Folgen",
            "",
            "| Lagefolge | Skalen | Profil | Vorkommen | 100 | 200 | 400 | dRand | dRekopplung |",
            "|---|---:|---|---:|---|---|---|---:|---:|",
        ]
    )
    for row in rows[:25]:
        lines.append(
            "| {worldlage_sequence} | {scale_count} | {multiscale_profile} | {occurrences_total} | {outcome_100} | {outcome_200} | {outcome_400} | {avg_delta_rand_over_scales:.4f} | {avg_delta_rekopplung_over_scales:.4f} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Bewertung",
            "",
            "Die mehrskalige Diagnose trennt drei Lesetiefen:",
            "",
            "- kurze Lagebewegung",
            "- mittlere Lagefolge",
            "- laengere Feldphase",
            "",
            "Wenn eine Lagefolge ueber alle Skalen gleich lesbar bleibt, ist sie ein robusterer Kandidat fuer Feldzeit-Ordnung.",
            "",
            "Wenn sie je nach Skala kippt, ist sie nicht falsch, sondern zeitlich empfindlich: Die Wirkung entsteht erst ueber Dauer oder zerfaellt bei feiner Lesung.",
            "",
            "Die Auswertung bleibt passiv. Sie erzeugt keine Handlung und keine Steuerung.",
            "",
            "Wie es weitergeht: Als naechstes sollten die skalenabhaengigen Folgen gegen konkrete Rohweltfenster gelesen werden, damit sichtbar wird, welche Weltbewegung eine neutrale Kurzlage in eine beruhigende laengere Feldphase ueberfuehrt.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", action="append", type=_parse_input)
    parser.add_argument("--out", default="docs/befunde/1308_WELTLAGEN_FOLGEMEMORY_MEHRSKALIG.md")
    parser.add_argument("--csv-out", default="docs/befunde/1308_WELTLAGEN_FOLGEMEMORY_MEHRSKALIG.csv")
    args = parser.parse_args()

    inputs = args.input or [(scale, Path(path)) for scale, path in DEFAULT_INPUTS]
    scales = [scale for scale, _ in inputs]
    by_sequence = _load_rows(inputs)
    rows = [
        _sequence_row(sequence, scale_rows, scales)
        for sequence, scale_rows in by_sequence.items()
    ]
    rows.sort(key=lambda row: (-int(row["scale_count"]), -int(row["occurrences_total"]), str(row["worldlage_sequence"])))
    if not rows:
        raise RuntimeError("no multiscale sequence rows generated")
    _write_csv(rows, Path(args.csv_out))
    _write_markdown(rows, Path(args.out))
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
