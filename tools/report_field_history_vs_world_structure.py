from __future__ import annotations

import argparse
import csv
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "docs" / "befunde" / "216_LOKALE_WELTMERKMALE_REKOPPLUNG_DIAGNOSE.csv"
DEFAULT_OUT = ROOT / "docs" / "befunde" / "218_FELDHISTORIE_GEGEN_WELTSTRUKTUR_DIAGNOSE.md"


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _float(value: object) -> float:
    try:
        return float(value or 0.0)
    except Exception:
        return 0.0


def _fmt(value: float, digits: int = 6) -> str:
    return f"{value:.{digits}f}"


def _load_rows(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = []
        for raw in reader:
            row = dict(raw)
            for key in (
                "contrast",
                "field_strain",
                "memory_load",
                "rekopplung",
                "world_compaction",
                "drift",
                "abs_drift",
                "avg_abs_return",
                "p95_abs_return",
                "avg_range",
                "p95_range",
                "avg_volume_change",
                "direction_change_ratio",
                "direction_persistence",
            ):
                row[key] = _float(row.get(key))
            row["recoupling_loss"] = max(0.0, 0.64 - row["rekopplung"])
            row["field_history_load"] = (
                (row["field_strain"] * 0.42)
                + (row["memory_load"] * 0.34)
                + (row["recoupling_loss"] * 0.24)
            )
            rows.append(row)
        return rows


def _pair_rows(rows: list[dict]) -> list[dict]:
    pairs: list[dict] = []
    for left_index, left in enumerate(rows):
        for right in rows[left_index + 1 :]:
            compaction_gap = abs(left["world_compaction"] - right["world_compaction"])
            history_gap = abs(left["field_history_load"] - right["field_history_load"])
            contrast_gap = abs(left["contrast"] - right["contrast"])
            role_changed = left["role"] != right["role"]
            # Diagnosewert: grosse Feldabweichung bei kleiner Weltabweichung.
            # Kein Gate, keine Runtime-Regel.
            divergence = (history_gap + (contrast_gap * 0.35) + (0.08 if role_changed else 0.0)) / (1.0 + compaction_gap)
            pairs.append(
                {
                    "left": left["name"],
                    "right": right["name"],
                    "left_role": left["role"],
                    "right_role": right["role"],
                    "role_changed": role_changed,
                    "compaction_gap": compaction_gap,
                    "history_gap": history_gap,
                    "contrast_gap": contrast_gap,
                    "divergence": divergence,
                    "left_compaction": left["world_compaction"],
                    "right_compaction": right["world_compaction"],
                    "left_history": left["field_history_load"],
                    "right_history": right["field_history_load"],
                    "left_contrast": left["contrast"],
                    "right_contrast": right["contrast"],
                }
            )
    return pairs


def _write_csv(pairs: list[dict], out_path: Path) -> None:
    csv_path = out_path.with_suffix(".csv")
    fieldnames = [
        "left",
        "right",
        "left_role",
        "right_role",
        "role_changed",
        "compaction_gap",
        "history_gap",
        "contrast_gap",
        "divergence",
        "left_compaction",
        "right_compaction",
        "left_history",
        "right_history",
        "left_contrast",
        "right_contrast",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for pair in pairs:
            writer.writerow(
                {
                    key: _fmt(pair[key], 6) if isinstance(pair.get(key), float) else pair.get(key)
                    for key in fieldnames
                }
            )


def _write_markdown(rows: list[dict], pairs: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    by_compaction = sorted(pairs, key=lambda pair: pair["compaction_gap"])[:12]
    by_divergence = sorted(pairs, key=lambda pair: pair["divergence"], reverse=True)[:12]
    _write_csv(by_divergence, out_path)

    lines = [
        "# Feldhistorie gegen Weltstruktur - Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft passiv, ob aehnliche Rohweltverdichtung automatisch gleiche Rekopplungsrollen erzeugt.",
        "Die Feldhistorie wird hier nur angenaehert: aus Feldlast, Memorylast und Rekopplungsverlust.",
        "",
        "Hierarchie der Pruefung:",
        "",
        "1. Grundfrage: Wirkt die Weltstruktur allein oder entscheidet die Feldgeschichte mit?",
        "2. Unterpruefung: Aehnliche Weltverdichtung gegen Feldhistorielast, Rollenwechsel und Bindungskontrast legen.",
        "3. Folgeschritt: Wenn aehnliche Weltstruktur unterschiedlich gelesen wird, Feldhistorie als eigene MCM-Dimension weiter pruefen.",
        "",
        "## Ausgangswerte",
        "",
        "| Welt | Rolle | Weltverdichtung | Feldhistorielast | Feldlast | Memorylast | Rekopplung | Kontrast |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in sorted(rows, key=lambda item: item["world_compaction"]):
        lines.append(
            "| "
            + " | ".join(
                [
                    row["name"],
                    row["role"],
                    _fmt(row["world_compaction"], 4),
                    _fmt(row["field_history_load"], 4),
                    _fmt(row["field_strain"], 4),
                    _fmt(row["memory_load"], 4),
                    _fmt(row["rekopplung"], 6),
                    _fmt(row["contrast"], 4),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Aehnlichste Weltstruktur",
            "",
            "| Paar | Rollen | Welt-Luecke | Feldhistorie-Luecke | Kontrast-Luecke | Rollenwechsel |",
            "|---|---|---:|---:|---:|---|",
        ]
    )
    for pair in by_compaction:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"{pair['left']} / {pair['right']}",
                    f"{pair['left_role']} / {pair['right_role']}",
                    _fmt(pair["compaction_gap"], 4),
                    _fmt(pair["history_gap"], 4),
                    _fmt(pair["contrast_gap"], 4),
                    "ja" if pair["role_changed"] else "nein",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Staerkste Abweichung trotz Naehe",
            "",
            "| Paar | Rollen | Welt-Luecke | Feldhistorie-Luecke | Kontrast-Luecke | Divergenz |",
            "|---|---|---:|---:|---:|---:|",
        ]
    )
    for pair in by_divergence:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"{pair['left']} / {pair['right']}",
                    f"{pair['left_role']} / {pair['right_role']}",
                    _fmt(pair["compaction_gap"], 4),
                    _fmt(pair["history_gap"], 4),
                    _fmt(pair["contrast_gap"], 4),
                    _fmt(pair["divergence"], 4),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Diagnose-Lesart",
            "",
            "- Wenn Weltverdichtung nahe liegt und Rolle gleich bleibt, spricht das fuer weltstrukturgetragene Ordnung.",
            "- Wenn Weltverdichtung nahe liegt und Rolle kippt, spricht das fuer Feldhistorie, Memory oder Rekopplungsverlust als Mitursache.",
            "- Wenn eine Stresswelt trotz aehnlicher Verdichtung aktiv-rekoppelnd bleibt, ist Stress nicht der Name einer festen Klasse, sondern einer moeglichen Feldwirkung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes wird der Befund geschrieben.",
            "Dort wird bewertet, ob MINI_DIO bereits eine feldhistorische Lesetiefe zeigt oder ob die aktuellen Werte nur Rohweltverdichtung abbilden.",
        ]
    )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Vergleicht Feldhistorie gegen lokale Weltstruktur.")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    rows = _load_rows(_resolve(args.source))
    pairs = _pair_rows(rows)
    _write_markdown(rows, pairs, _resolve(args.out))


if __name__ == "__main__":
    main()
