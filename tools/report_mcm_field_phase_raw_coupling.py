from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

from befunde_paths import befunde_root


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


DEFAULT_PHASES = befunde_root(ROOT) / "1245_MCM_FELDPHASEN_KLASSEN.csv"
DEFAULT_TRIGGERS = befunde_root(ROOT) / "1246_MCM_FELDPHASEN_WELTARTEN_TRIGGER.csv"
DEFAULT_OUT = befunde_root(ROOT) / "1248_MCM_FELDPHASEN_ROHFELD_KOPPLUNG.md"


TARGET_CLASSES = {
    "grenzphase_mit_entlastung",
    "weltgebundene_feldphase",
    "lokale_oder_driftende_phase",
    "junge_phasenspur",
}


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _parse_counter_text(value: str) -> Counter[str]:
    counter: Counter[str] = Counter()
    text = str(value or "").strip()
    if not text or text == "-":
        return counter
    for part in text.split(";"):
        item = part.strip()
        if not item or ":" not in item:
            continue
        key, count_text = item.rsplit(":", 1)
        try:
            count = int(float(count_text))
        except ValueError:
            count = 0
        counter[key.strip()] += count
    return counter


def _load_trigger_index(path: Path) -> dict[str, dict[str, str]]:
    return {row.get("phase_key", ""): row for row in _load(path)}


def _coupling_class(row: dict[str, str]) -> str:
    intake = _safe_float(row.get("avg_current_intake"))
    strain = _safe_float(row.get("avg_current_strain"))
    rekopplung = _safe_float(row.get("avg_current_rekopplung"))
    d_reko = _safe_float(row.get("avg_rekopplung_delta_to_next"))
    d_strain = _safe_float(row.get("avg_strain_delta_to_next"))

    if strain >= 0.25 and d_reko > 0.04 and d_strain < -0.04:
        return "last_mit_entlastender_folge"
    if intake >= 0.35 and strain >= 0.25:
        return "hohe_rohfeldlast"
    if rekopplung >= 0.70 and d_strain > 0.08:
        return "rekopplung_vor_belastung"
    if d_reko > 0.04 and d_strain < -0.03:
        return "rekopplung_nach_entlastung"
    if d_reko < -0.04 and d_strain > 0.04:
        return "entkopplung_in_last"
    return "gemischte_rohfeldkopplung"


def _build_rows(phase_rows: list[dict[str, str]], trigger_rows: dict[str, dict[str, str]]) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for row in phase_rows:
        if row.get("phase_class") not in TARGET_CLASSES:
            continue
        phase_key = row.get("phase_key", "")
        trigger = trigger_rows.get(phase_key, {})
        assets = _parse_counter_text(trigger.get("assets", ""))
        timeframes = _parse_counter_text(trigger.get("timeframes", ""))
        world_kinds = _parse_counter_text(trigger.get("world_kinds", ""))
        out.append(
            {
                "phase_key": phase_key,
                "phase_class": row.get("phase_class", ""),
                "role_family": row.get("role_family", ""),
                "seen_count": row.get("seen_count", "0"),
                "world_count": row.get("world_count", "0"),
                "dominant_effect": row.get("dominant_effect", ""),
                "coupling_class": _coupling_class(row),
                "avg_current_intake": row.get("avg_current_intake", "0"),
                "avg_current_rekopplung": row.get("avg_current_rekopplung", "0"),
                "avg_current_strain": row.get("avg_current_strain", "0"),
                "avg_next_rekopplung": row.get("avg_next_rekopplung", "0"),
                "avg_next_strain": row.get("avg_next_strain", "0"),
                "avg_rekopplung_delta_to_next": row.get("avg_rekopplung_delta_to_next", "0"),
                "avg_strain_delta_to_next": row.get("avg_strain_delta_to_next", "0"),
                "top_world_kind": world_kinds.most_common(1)[0][0] if world_kinds else "-",
                "top_asset": assets.most_common(1)[0][0] if assets else "-",
                "top_timeframe": timeframes.most_common(1)[0][0] if timeframes else "-",
                "world_kinds": trigger.get("world_kinds", "-"),
                "assets": trigger.get("assets", "-"),
                "timeframes": trigger.get("timeframes", "-"),
            }
        )
    return out


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object) -> str:
    try:
        return f"{float(value):.4f}"
    except (TypeError, ValueError):
        return str(value)


def _write_markdown(path: Path, rows: list[dict[str, object]], phase_path: Path, trigger_path: Path) -> None:
    coupling_counts = Counter(str(row["coupling_class"]) for row in rows)
    class_counts = Counter(str(row["phase_class"]) for row in rows)
    lines: list[str] = [
        "# MCM-Feldphasen Rohfeld-Kopplung",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "## Grundfrage",
        "",
        "Sind situative Randphasen eher durch Rohfeldlast, Rekopplungsbruch, Entlastung, Zeitrahmen oder Assetcharakter lesbar?",
        "",
        "## Eingaben",
        "",
        f"- `{phase_path.relative_to(ROOT)}`",
        f"- `{trigger_path.relative_to(ROOT)}`",
        "",
        "## Profil",
        "",
        f"- untersuchte Phasen: `{len(rows)}`",
        f"- Phasenklassen: `{dict(class_counts.most_common())}`",
        f"- Kopplungsklassen: `{dict(coupling_counts.most_common())}`",
        "",
        "## Rohfeld-Kopplung",
        "",
        "| Phase | Klasse | Kopplung | Intake | Rekopplung | Strain | Delta Rekopplung | Delta Strain | Top-Weltart | Top-Asset | Zeit |",
        "|---|---|---|---:|---:|---:|---:|---:|---|---|---|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["phase_key"]),
                    str(row["phase_class"]),
                    str(row["coupling_class"]),
                    _fmt(row["avg_current_intake"]),
                    _fmt(row["avg_current_rekopplung"]),
                    _fmt(row["avg_current_strain"]),
                    _fmt(row["avg_rekopplung_delta_to_next"]),
                    _fmt(row["avg_strain_delta_to_next"]),
                    str(row["top_world_kind"]),
                    str(row["top_asset"]),
                    str(row["top_timeframe"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die situativen Randphasen sind rohfeldseitig vor allem als Kopplungsereignisse lesbar.",
            "",
            "Wichtig ist die Trennung:",
            "",
            "```text",
            "Rand/Kipp als Zustand ist nicht automatisch Kollaps.",
            "Entscheidend ist, ob danach Rekopplung steigt und Strain faellt.",
            "```",
            "",
            "Grenzphasen mit Entlastung zeigen genau diese Richtung: Belastung wird sichtbar, danach nimmt Rekopplung zu und Strain faellt.",
            "",
            "Weltgebundene Randphasen sind uneinheitlicher. Sie koennen aus Stress-/Negativwelt, Alt-Asset-Kontext, ruhigen/seitwaerts Welten oder synthetischen Sinneswelten kommen.",
            "",
            "## Bedeutung",
            "",
            "Damit wird die MCM-Lesung genauer:",
            "",
            "```text",
            "Nicht die Randnaehe allein ist entscheidend.",
            "Entscheidend ist die Feldbewegung nach der Randnaehe.",
            "```",
            "",
            "## Grenze",
            "",
            "Diese Diagnose nutzt aggregierte Feldphasenwerte. Fuer eine vollstaendige Rohwelt-Erklaerung muessen spaeter OHLCV-Fenster, Ton-/Lautheitsprofile und Rezeptorprofile direkt pro Phase angebunden werden.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Liest situative Feldphasen gegen Rohfeld-/Sensorikwerte.")
    parser.add_argument("--phases", default=str(DEFAULT_PHASES), help="Feldphasen-Klassen CSV.")
    parser.add_argument("--triggers", default=str(DEFAULT_TRIGGERS), help="Weltarten-Trigger CSV.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Markdown-Ausgabe.")
    args = parser.parse_args()

    phase_path = _resolve(args.phases)
    trigger_path = _resolve(args.triggers)
    out_path = _resolve(args.out)
    rows = _build_rows(_load(phase_path), _load_trigger_index(trigger_path))
    _write_csv(out_path.with_suffix(".csv"), rows)
    _write_markdown(out_path, rows, phase_path, trigger_path)

    print(f"records={len(rows)} out={out_path}")
    for name, count in Counter(str(row["coupling_class"]) for row in rows).most_common():
        print(f"{name}: {count}")


if __name__ == "__main__":
    main()
