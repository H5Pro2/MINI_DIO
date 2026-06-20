from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from statistics import fmean


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_IN = ROOT / "docs" / "befunde" / "334_PREVIEW_UEBERGANGSPAARE_DIAGNOSE.csv"
DEFAULT_OUT = ROOT / "docs" / "befunde" / "335_PREVIEW_UEBERGANGSPAARE_KLASSIFIKATION.md"


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


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


def _load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _movement_class(row: dict[str, str]) -> str:
    worlds = int(_float(row.get("worlds")))
    count = int(_float(row.get("count")))
    pressure = _float(row.get("pressure_delta"))
    sharpness = _float(row.get("sharpness_delta"))
    rekopplung = _float(row.get("rekopplung_delta"))
    role_shift = str(row.get("dominant_role_shift", "-") or "-")

    if worlds >= 4 and count >= 20 and abs(pressure) <= 0.02 and abs(rekopplung) <= 0.02:
        return "grundinsel_wechsel"
    if rekopplung > 0.008 and pressure <= 0.0:
        return "rekopplungsbogen"
    if pressure > 0.04 and rekopplung < -0.02:
        return "druck_rueckfuehrung"
    if "offene_variante" in role_shift and pressure > 0.0:
        return "offener_uebergang"
    if sharpness > 0.06 and abs(pressure) <= 0.04:
        return "schaerfungsuebergang"
    if worlds <= 2 and count <= 5:
        return "lokale_einzelkante"
    return "gemischte_feldbewegung"


def _summarize(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row in rows:
        movement_class = _movement_class(row)
        result.append(
            {
                "pair": row.get("pair", "-") or "-",
                "count": int(_float(row.get("count"))),
                "worlds": int(_float(row.get("worlds"))),
                "dominant_world": row.get("dominant_world", "-") or "-",
                "dominant_role_shift": row.get("dominant_role_shift", "-") or "-",
                "movement_class": movement_class,
                "pressure_delta": _float(row.get("pressure_delta")),
                "sharpness_delta": _float(row.get("sharpness_delta")),
                "focus_delta": _float(row.get("focus_delta")),
                "rekopplung_delta": _float(row.get("rekopplung_delta")),
                "loudness_delta": _float(row.get("loudness_delta")),
            }
        )
    return result


def _class_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["movement_class"])].append(row)

    result: list[dict[str, object]] = []
    for movement_class, items in sorted(grouped.items(), key=lambda entry: len(entry[1]), reverse=True):
        result.append(
            {
                "movement_class": movement_class,
                "pairs": len(items),
                "events": sum(int(item["count"]) for item in items),
                "worlds_sum": sum(int(item["worlds"]) for item in items),
                "top_pair": Counter(str(item["pair"]) for item in items).most_common(1)[0][0],
                "pressure_delta": _mean([float(item["pressure_delta"]) for item in items]),
                "sharpness_delta": _mean([float(item["sharpness_delta"]) for item in items]),
                "rekopplung_delta": _mean([float(item["rekopplung_delta"]) for item in items]),
            }
        )
    return result


def _write_csv(rows: list[dict[str, object]], class_rows: list[dict[str, object]], out_path: Path) -> None:
    pair_path = out_path.with_suffix(".csv")
    pair_fields = [
        "pair",
        "count",
        "worlds",
        "movement_class",
        "dominant_world",
        "dominant_role_shift",
        "pressure_delta",
        "sharpness_delta",
        "focus_delta",
        "rekopplung_delta",
        "loudness_delta",
    ]
    pair_path.parent.mkdir(parents=True, exist_ok=True)
    with pair_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=pair_fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    key: _fmt(float(row[key]), 6) if isinstance(row.get(key), float) else row.get(key, "")
                    for key in pair_fields
                }
            )

    class_path = out_path.with_name(out_path.stem + "_klassen.csv")
    class_fields = [
        "movement_class",
        "pairs",
        "events",
        "worlds_sum",
        "top_pair",
        "pressure_delta",
        "sharpness_delta",
        "rekopplung_delta",
    ]
    with class_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=class_fields)
        writer.writeheader()
        for row in class_rows:
            writer.writerow(
                {
                    key: _fmt(float(row[key]), 6) if isinstance(row.get(key), float) else row.get(key, "")
                    for key in class_fields
                }
            )


def _write_md(rows: list[dict[str, object]], class_rows: list[dict[str, object]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    _write_csv(rows, class_rows, out_path)

    lines = [
        "# Preview-Uebergangspaare Klassifikation",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose klassifiziert konkrete MCM-Preview-Uebergangspaare als passive Feldbewegungen.",
        "Sie bleibt passiv: keine Handlung, kein Gate, kein Entry-Signal.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Welche Bewegungsarten entstehen zwischen Bedeutungsinseln?",
        "2. Unterpruefung: Paare nach Weltbreite, Druck, Schaerfe, Rekopplung und Rollenwechsel klassifizieren.",
        "3. Folgeschritt: stabile Bewegungsarten ueber weitere Welten validieren.",
        "",
        "## Bewegungsarten",
        "",
        "- `grundinsel_wechsel`: breiter, ruhiger Wechsel zwischen stabilen Inseln.",
        "- `rekopplungsbogen`: Druck sinkt und Rekopplung steigt.",
        "- `druck_rueckfuehrung`: Druck steigt und Rekopplung sinkt beim Rueckweg.",
        "- `offener_uebergang`: Wechsel mit offener Variante und leichtem Druck.",
        "- `schaerfungsuebergang`: Schaerfe steigt ohne starken Druckanstieg.",
        "- `lokale_einzelkante`: seltene lokale Kante.",
        "- `gemischte_feldbewegung`: noch nicht klar genug getrennte Bewegung.",
        "",
        "## Klassenuebersicht",
        "",
        "| Klasse | Paare | Events | Welten-Summe | Top-Paar | dDruck | dSchaerfe | dRekopplung |",
        "|---|---:|---:|---:|---|---:|---:|---:|",
    ]
    for row in class_rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["movement_class"]),
                    str(row["pairs"]),
                    str(row["events"]),
                    str(row["worlds_sum"]),
                    str(row["top_pair"]),
                    _fmt(float(row["pressure_delta"])),
                    _fmt(float(row["sharpness_delta"])),
                    _fmt(float(row["rekopplung_delta"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Paarmatrix",
            "",
            "| Paar | Klasse | Anzahl | Welten | Rollenwechsel | dDruck | dSchaerfe | dRekopplung |",
            "|---|---|---:|---:|---|---:|---:|---:|",
        ]
    )
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["pair"]),
                    str(row["movement_class"]),
                    str(row["count"]),
                    str(row["worlds"]),
                    str(row["dominant_role_shift"]),
                    _fmt(float(row["pressure_delta"])),
                    _fmt(float(row["sharpness_delta"])),
                    _fmt(float(row["rekopplung_delta"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Klassifikation ist ein erster Ordnungsversuch, keine endgueltige Ontologie.",
            "Sie zeigt aber, dass die Uebergaenge nicht gleichartig sind.",
            "",
            "Der wichtigste bisherige Bewegungsbefund bleibt:",
            "",
            "```text",
            "1t5bcxp -> 183drjy = rekoppelnde Richtung",
            "183drjy -> 1t5bcxp = Rueckfuehrung mit mehr Druck/offener Variante",
            "```",
            "",
            "Damit entsteht eine passive Feldbewegung zwischen Grundinsel und rekoppelnder Innenzone.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes wird geprueft, ob diese Bewegungsarten in weiteren Welten stabil bleiben oder neue Klassen benoetigen.",
            "",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_IN)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    input_path = args.input if args.input.is_absolute() else ROOT / args.input
    out = args.out if args.out.is_absolute() else ROOT / args.out
    rows = _summarize(_load_rows(input_path))
    classes = _class_rows(rows)
    _write_md(rows, classes, out)
    print(f"wrote {out}")
    print(f"wrote {out.with_suffix('.csv')}")
    print(f"wrote {out.with_name(out.stem + '_klassen.csv')}")


if __name__ == "__main__":
    main()
