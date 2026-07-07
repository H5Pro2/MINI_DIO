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
    return 0.0 if result != result else result


def _fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"


def _mean(values: list[float]) -> float:
    return fmean(values) if values else 0.0


def _family(row: dict[str, str]) -> str:
    value = (row.get("symbol_family") or "").strip()
    if value:
        return value
    symbol = (row.get("symbol") or "").strip()
    return symbol[:8] if symbol else "-"


def _raw_by_timestamp(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {str(row.get("timestamp_ms", "")): row for row in rows if row.get("timestamp_ms")}


def _raw_metrics(rows: list[dict[str, str]], raw_index: dict[str, dict[str, str]]) -> dict[str, float]:
    ranges: list[float] = []
    bodies: list[float] = []
    volumes: list[float] = []
    closes: list[float] = []
    for row in rows:
        raw = raw_index.get(str(row.get("timestamp_ms", "")))
        if not raw:
            continue
        open_ = _float(raw.get("open"))
        high = _float(raw.get("high"))
        low = _float(raw.get("low"))
        close = _float(raw.get("close"))
        base = max(abs(open_), 1e-12)
        ranges.append((high - low) / base)
        bodies.append(abs(close - open_) / base)
        volumes.append(_float(raw.get("volume")))
        closes.append(close)
    net = 0.0
    if len(closes) >= 2 and abs(closes[0]) > 1e-12:
        net = (closes[-1] - closes[0]) / closes[0]
    return {
        "raw_net_pct": net * 100.0,
        "raw_range_pct": _mean(ranges) * 100.0,
        "raw_body_pct": _mean(bodies) * 100.0,
        "raw_volume": _mean(volumes),
    }


def _window_metrics(rows: list[dict[str, str]], raw_index: dict[str, dict[str, str]]) -> dict[str, float]:
    metrics = {
        "count": float(len(rows)),
        "rekopplung": _mean([_float(row.get("mcm_rekopplung_quality")) for row in rows]),
        "adaptive_rekopplung": _mean([_float(row.get("mcm_adaptive_rekopplung_quality")) for row in rows]),
        "strain": _mean([_float(row.get("mcm_strain_quality")) for row in rows]),
        "carry": _mean([_float(row.get("mcm_carry_quality")) for row in rows]),
        "visual_gap": _mean([_float(row.get("mcm_visual_field_gap")) for row in rows]),
        "hearing_gap": _mean([_float(row.get("mcm_hearing_field_gap")) for row in rows]),
        "form_stability": _mean([_float(row.get("sehen_form_stability")) for row in rows]),
        "form_change": _mean([_float(row.get("sehen_form_change")) for row in rows]),
        "tone": _mean([_float(row.get("hoeren_energy_tone")) for row in rows]),
        "tone_shift_abs": _mean([abs(_float(row.get("hoeren_energy_shift"))) for row in rows]),
        "felt_pressure": _mean([_float(row.get("perception_felt_pressure")) for row in rows]),
        "adapted_intake": _mean([_float(row.get("perception_adapted_field_intake_pressure")) for row in rows]),
        "mcm_coherence": _mean([_float(row.get("mcm_feldwirkung_mcm_coherence")) for row in rows]),
        "mcm_tension": _mean([_float(row.get("mcm_feldwirkung_mcm_tension")) for row in rows]),
        "mcm_asymmetry": _mean([_float(row.get("mcm_feldwirkung_mcm_asymmetry")) for row in rows]),
    }
    metrics.update(_raw_metrics(rows, raw_index))
    return metrics


def _world_arg(values: list[str]) -> tuple[str, Path, Path]:
    if len(values) != 3:
        raise argparse.ArgumentTypeError("--world braucht: NAME FOLLOW_EP FOLLOW_RAW")
    return values[0], _resolve(values[1]), _resolve(values[2])


def _target_rows(relation_rows: list[dict[str, str]], families: set[str], transition: str) -> list[dict[str, str]]:
    return [
        row
        for row in relation_rows
        if row.get("family") in families and row.get("transition") == transition
    ]


def _collect(args: argparse.Namespace) -> list[dict[str, object]]:
    relation_rows = _load_csv(_resolve(args.relation_csv))
    families = set(args.family)
    targets = _target_rows(relation_rows, families, args.transition)
    worlds = {world[0]: world for world in (_world_arg(value) for value in args.world)}
    cache: dict[str, tuple[list[dict[str, str]], dict[str, dict[str, str]]]] = {}
    result: list[dict[str, object]] = []
    for target in targets:
        world_name = str(target.get("world", "-"))
        if world_name not in worlds:
            continue
        if world_name not in cache:
            _, ep_path, raw_path = worlds[world_name]
            cache[world_name] = (_load_csv(ep_path), _raw_by_timestamp(_load_csv(raw_path)))
        episodes, raw_index = cache[world_name]
        by_tick = {int(_float(row.get("tick"))): idx for idx, row in enumerate(episodes)}
        target_family = str(target.get("family", "-"))
        occurrence_rows = [row for row in episodes if _family(row) == target_family]
        pre_rows: list[dict[str, str]] = []
        for occurrence in occurrence_rows:
            idx = by_tick.get(int(_float(occurrence.get("tick"))))
            if idx is None:
                continue
            pre_rows.extend(episodes[max(0, idx - args.lookback) : idx])
        occurrence_metrics = _window_metrics(occurrence_rows, raw_index)
        pre_metrics = _window_metrics(pre_rows, raw_index)
        row: dict[str, object] = {
            "world": world_name,
            "family": target_family,
            "transition": target.get("transition", "-"),
            "relation_base_total": target.get("base_total", "0"),
            "relation_follow_total": target.get("follow_total", "0"),
        }
        row.update({f"pre_{key}": value for key, value in pre_metrics.items()})
        row.update({f"open_{key}": value for key, value in occurrence_metrics.items()})
        result.append(row)
    return result


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
            writer.writerow({key: _fmt(value, 6) if isinstance(value, float) else value for key, value in row.items()})


def _write_md(rows: list[dict[str, object]], out_path: Path) -> None:
    _write_csv(rows, out_path)
    title_prefix = out_path.stem.split("_", 1)[0]
    title = f"# {title_prefix} - Ziel-Familien Rohweltfenster" if title_prefix.isdigit() else "# Ziel-Familien Rohweltfenster"
    lines = [
        title,
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest die robusten Ziel-Familien in ihren Asset-Folgefenstern.",
        "Sie bleibt passiv: keine Handlung, kein Gate, keine Richtung.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Welche Vorbedingungen stehen vor erneuter Milieu-Oeffnung?",
        "2. Unterpruefung: Vorfenster und Oeffnungsfamilie in Weltspannung, Hoeren und Feldspannung vergleichen.",
        "3. Folgeschritt: Gemeinsame Vorbedingungsform als Kandidat fuer robuste Milieu-Bewegung pruefen.",
        "",
        "## Ziel-Fenster",
        "",
        "| Familie | Welt | Oeffnungs-Ticks | Vor Range | Vor Hoeren | Vor Spannung | Open Range | Open Hoeren | Open Spannung |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["family"]),
                    str(row["world"]),
                    _fmt(float(row["open_count"]), 0),
                    _fmt(float(row["pre_raw_range_pct"])),
                    _fmt(float(row["pre_hearing_gap"])),
                    _fmt(float(row["pre_mcm_tension"])),
                    _fmt(float(row["open_raw_range_pct"])),
                    _fmt(float(row["open_hearing_gap"])),
                    _fmt(float(row["open_mcm_tension"])),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "`dio_0ly7` und `dio_01hu` werden hier nicht als Bedeutung gesetzt.",
            "Sie werden als robuste Kandidaten gelesen, weil dieselbe Familienbewegung in mehreren Weltfenstern erneut erscheint.",
            "",
            "Die wichtige Frage ist, ob vor der Oeffnung eine gemeinsame Vorform liegt: moderate Range, Hoerprofil-Entlastung, stabile Feldspannung oder ein anderer wiederkehrender Zustand.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollten diese Vorfenster aggregiert werden: Gibt es eine gemeinsame Oeffnungs-Vorform fuer `dio_0ly7` und `dio_01hu`, oder sind es zwei getrennte Kandidaten?",
            "",
        ]
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Liest robuste Milieu-Zielfamilien in Asset-Rohweltfenstern.")
    parser.add_argument("--relation-csv", required=True)
    parser.add_argument("--family", action="append", required=True)
    parser.add_argument("--transition", default="nur_gereift->offen_und_gereift")
    parser.add_argument("--world", nargs=3, action="append", required=True, metavar=("NAME", "FOLLOW_EP", "FOLLOW_RAW"))
    parser.add_argument("--lookback", type=int, default=8)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()
    rows = _collect(args)
    _write_md(rows, _resolve(args.out_md))
    print({"out_md": str(_resolve(args.out_md)), "rows": len(rows), "families": args.family})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
