from __future__ import annotations

import argparse
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LONG_DEFAULT = ROOT / "docs" / "befunde" / "806_BLOCK_K_FELDEPISODEN_ZEITREIHE.csv"
STRESS_DEFAULT = ROOT / "docs" / "befunde" / "807_BLOCK_K_STRESS_FELDEPISODEN_ZEITREIHE.csv"
CSV_DEFAULT = ROOT / "docs" / "befunde" / "808_BLOCK_K_FELDZEIT_10K_VS_STRESS.csv"
MD_DEFAULT = ROOT / "docs" / "befunde" / "808_BLOCK_K_FELDZEIT_10K_VS_STRESS.md"


def _safe_float(value: object, default: float = 0.0) -> float:
    try:
        result = float(str(value).replace(",", "."))
    except Exception:
        return default
    if result != result:
        return default
    return result


def _read_rows(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8-sig")
    return [dict(row) for row in csv.DictReader(text.splitlines(), delimiter=";")]


def _avg(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def _weighted_avg(rows: list[dict[str, str]], key: str) -> float:
    weighted_sum = 0.0
    total_weight = 0.0
    for row in rows:
        weight = max(0.0, _safe_float(row.get("duration")))
        weighted_sum += _safe_float(row.get(key)) * weight
        total_weight += weight
    if total_weight <= 0.0:
        return 0.0
    return weighted_sum / total_weight


def _summary(label: str, rows: list[dict[str, str]]) -> dict[str, object]:
    durations = [_safe_float(row.get("duration")) for row in rows]
    long_rows = [row for row in rows if _safe_float(row.get("duration")) >= 1000.0]
    carried_rows = [row for row in rows if str(row.get("mcm_field_effect_state")) == "field_carried"]
    strained_rows = [row for row in rows if str(row.get("mcm_field_effect_state")) != "field_carried"]
    total_ticks = sum(durations)
    carried_ticks = sum(_safe_float(row.get("duration")) for row in carried_rows)
    return {
        "group": label,
        "segments": len(rows),
        "total_ticks": total_ticks,
        "avg_duration": _avg(durations),
        "max_duration": max(durations) if durations else 0.0,
        "long_segments": len(long_rows),
        "strained_segments": len(strained_rows),
        "carried_tick_share": carried_ticks / max(1.0, total_ticks),
        "avg_carry": _weighted_avg(rows, "avg_carry"),
        "avg_rekopplung": _weighted_avg(rows, "avg_rekopplung"),
        "avg_strain": _weighted_avg(rows, "avg_strain"),
        "avg_afterimage": _weighted_avg(rows, "avg_afterimage"),
        "avg_temporal_trust": _weighted_avg(rows, "avg_temporal_trust"),
    }


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def _write_markdown(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    long_row = rows[0]
    stress_row = rows[1]
    delta_trust = float(long_row["avg_temporal_trust"]) - float(stress_row["avg_temporal_trust"])
    delta_afterimage = float(long_row["avg_afterimage"]) - float(stress_row["avg_afterimage"])
    delta_max_duration = float(long_row["max_duration"]) - float(stress_row["max_duration"])
    lines = [
        "# 808 - Block-K Feldzeit 10k vs Stress",
        "",
        "## Fragestellung",
        "",
        "Traegt laengere Weltzeit die MCM-Feldintegration sichtbar anders als eine kurze Stresswelt?",
        "",
        "## Vergleich",
        "",
        "| Gruppe | Segmente | Ticks | Max-Dauer | lange Segmente | gespannte Segmente | Carry-Anteil | Carry | Rekopplung | Strain | Nachhall | Feldzeit/Trust |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['group']} | {row['segments']} | {_fmt(row['total_ticks'])} | "
            f"{_fmt(row['max_duration'])} | {row['long_segments']} | {row['strained_segments']} | "
            f"{_fmt(row['carried_tick_share'])} | {_fmt(row['avg_carry'])} | "
            f"{_fmt(row['avg_rekopplung'])} | {_fmt(row['avg_strain'])} | "
            f"{_fmt(row['avg_afterimage'])} | {_fmt(row['avg_temporal_trust'])} |"
        )
    lines.extend(
        [
            "",
            "## Delta 10k minus Stress",
            "",
            f"- Max-Dauer: `{delta_max_duration:.4f}` Ticks",
            f"- Nachhall: `{delta_afterimage:.4f}`",
            f"- Feldzeit/Trust: `{delta_trust:.4f}`",
            "",
            "## Befund",
            "",
            "Die 10k-Welt zeigt nicht nur mehr Datenlaenge, sondern eine andere Feldzeit-Qualitaet:",
            "",
            "- mehrere lange Integrationsphasen,",
            "- kurze Spannungsbrueche zwischen getragenen Phasen,",
            "- hoeherer Nachhall,",
            "- deutlich hoeherer temporaler Trust,",
            "- laenger getragene Rekopplung.",
            "",
            "Die kurze Stresswelt bleibt zwar stabil getragen, bekommt aber keine lange Feldzeit zur Reifung. Damit wirkt Feldzeit hier nicht als programmierte Zusatzachse, sondern als aus der laengeren Feldwirkung lesbare Integrationsqualitaet.",
            "",
            "## Grenze",
            "",
            "Dies ist ein Vergleich von zwei konkreten Zeitreihen. Er zeigt eine klare Differenz, aber noch keine allgemeine Aussage fuer alle Stress- oder 10k-Welten.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese Feldzeit-Lupe ueber mehrere 10k-Welten laufen. Dann sehen wir, ob die erhoehte Feldzeit/Integration allgemein mit Laenge entsteht oder nur in dieser einen 10k-Welt.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--long", type=Path, default=LONG_DEFAULT)
    parser.add_argument("--stress", type=Path, default=STRESS_DEFAULT)
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    args = parser.parse_args()
    rows = [
        _summary("lang_10k", _read_rows(args.long)),
        _summary("kurz_stress", _read_rows(args.stress)),
    ]
    _write_csv(args.csv_out, rows)
    _write_markdown(args.md_out, rows)
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    for row in rows:
        print(f"{row['group']}: max_duration={float(row['max_duration']):.1f} trust={float(row['avg_temporal_trust']):.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
