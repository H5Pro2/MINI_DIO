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
    symbol = (row.get("symbol") or row.get("episode_memory_symbol") or "").strip()
    return symbol[:8] if symbol else "-"


def _group_by_family(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[_family(row)].append(row)
    return grouped


def _raw_by_timestamp(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {str(row.get("timestamp_ms", "")): row for row in rows if row.get("timestamp_ms")}


def _raw_metrics(episode_rows: list[dict[str, str]], raw_index: dict[str, dict[str, str]]) -> dict[str, float]:
    matched: list[dict[str, str]] = []
    for row in episode_rows:
        raw = raw_index.get(str(row.get("timestamp_ms", "")))
        if raw:
            matched.append(raw)

    ranges: list[float] = []
    bodies: list[float] = []
    volumes: list[float] = []
    closes: list[float] = []
    for row in matched:
        open_ = _float(row.get("open"))
        high = _float(row.get("high"))
        low = _float(row.get("low"))
        close = _float(row.get("close"))
        base = max(abs(open_), 1e-12)
        ranges.append((high - low) / base)
        bodies.append(abs(close - open_) / base)
        volumes.append(_float(row.get("volume")))
        closes.append(close)

    net = 0.0
    if len(closes) >= 2 and abs(closes[0]) > 1e-12:
        net = (closes[-1] - closes[0]) / closes[0]

    return {
        "raw_rows": float(len(matched)),
        "raw_net_pct": net * 100.0,
        "raw_range_pct": _mean(ranges) * 100.0,
        "raw_body_pct": _mean(bodies) * 100.0,
        "raw_volume": _mean(volumes),
    }


def _episode_metrics(rows: list[dict[str, str]], raw_index: dict[str, dict[str, str]]) -> dict[str, float]:
    ticks = [int(_float(row.get("tick"))) for row in rows]
    data = {
        "ticks": float(len(rows)),
        "tick_start": float(min(ticks) if ticks else 0),
        "tick_end": float(max(ticks) if ticks else 0),
        "range_ticks": float((max(ticks) - min(ticks) + 1) if ticks else 0),
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
    data.update(_raw_metrics(rows, raw_index))
    return data


def _pre_windows(
    family_rows: list[dict[str, str]],
    all_rows: list[dict[str, str]],
    raw_index: dict[str, dict[str, str]],
    lookback: int,
) -> dict[str, float]:
    by_tick = {int(_float(row.get("tick"))): idx for idx, row in enumerate(all_rows)}
    windows: list[dict[str, str]] = []
    for row in family_rows:
        tick = int(_float(row.get("tick")))
        idx = by_tick.get(tick)
        if idx is None:
            continue
        windows.extend(all_rows[max(0, idx - lookback) : idx])
    metrics = _episode_metrics(windows, raw_index)
    return {f"pre_{key}": value for key, value in metrics.items()}


def _world_arg(values: list[str]) -> tuple[str, Path, Path, Path, Path]:
    if len(values) != 5:
        raise argparse.ArgumentTypeError("--world braucht: NAME BASE_EP FOLLOW_EP BASE_RAW FOLLOW_RAW")
    return values[0], _resolve(values[1]), _resolve(values[2]), _resolve(values[3]), _resolve(values[4])


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
            writer.writerow({k: _fmt(v, 6) if isinstance(v, float) else v for k, v in row.items()})


def _build_loupe(args: argparse.Namespace) -> list[dict[str, object]]:
    hit_rows = _load_csv(_resolve(args.hit_csv))
    sorted_hits = sorted(
        hit_rows,
        key=lambda row: (
            _float(row.get("delta_2023_to_2425_range_mid"))
            + _float(row.get("delta_2023_to_2425_hearing_mid"))
            + _float(row.get("delta_2023_to_2425_tension_mid")),
            row.get("family", "-"),
        ),
    )[: args.top]

    worlds = {_world_arg(world_values)[0]: _world_arg(world_values) for world_values in args.world}
    cache: dict[str, dict[str, object]] = {}
    out: list[dict[str, object]] = []

    for hit in sorted_hits:
        world_name = hit.get("world_2023", "-")
        if world_name not in worlds:
            continue
        _, base_ep_path, follow_ep_path, base_raw_path, follow_raw_path = worlds[world_name]
        if world_name not in cache:
            base_ep = _load_csv(base_ep_path)
            follow_ep = _load_csv(follow_ep_path)
            base_raw = _raw_by_timestamp(_load_csv(base_raw_path))
            follow_raw = _raw_by_timestamp(_load_csv(follow_raw_path))
            cache[world_name] = {
                "base_ep": base_ep,
                "follow_ep": follow_ep,
                "base_groups": _group_by_family(base_ep),
                "follow_groups": _group_by_family(follow_ep),
                "base_raw": base_raw,
                "follow_raw": follow_raw,
            }

        world = cache[world_name]
        family = str(hit.get("family", "-"))
        base_rows = world["base_groups"].get(family, [])  # type: ignore[index, union-attr]
        follow_rows = world["follow_groups"].get(family, [])  # type: ignore[index, union-attr]
        base_metrics = _episode_metrics(base_rows, world["base_raw"])  # type: ignore[arg-type, index]
        follow_metrics = _episode_metrics(follow_rows, world["follow_raw"])  # type: ignore[arg-type, index]
        pre_metrics = _pre_windows(
            follow_rows,
            world["follow_ep"],  # type: ignore[arg-type, index]
            world["follow_raw"],  # type: ignore[arg-type, index]
            args.lookback,
        )

        row: dict[str, object] = {
            "family": family,
            "transition": hit.get("transition", "-"),
            "world": world_name,
            "count_2024": hit.get("count_2024", "0"),
            "count_2025": hit.get("count_2025", "0"),
            "base_total_2023": hit.get("base_total_2023", "0"),
            "follow_total_2023": hit.get("follow_total_2023", "0"),
            "delta_range_mid": _float(hit.get("delta_2023_to_2425_range_mid")),
            "delta_hearing_mid": _float(hit.get("delta_2023_to_2425_hearing_mid")),
            "delta_tension_mid": _float(hit.get("delta_2023_to_2425_tension_mid")),
        }
        row.update({f"base_{k}": v for k, v in base_metrics.items()})
        row.update({f"follow_{k}": v for k, v in follow_metrics.items()})
        row.update(pre_metrics)
        out.append(row)
    return out


def _write_md(rows: list[dict[str, object]], out_path: Path) -> None:
    _write_csv(rows, out_path)
    title_prefix = out_path.stem.split("_", 1)[0]
    title = f"# {title_prefix} - Rohwelt-Lupe fuer Drittperioden-Treffer" if title_prefix.isdigit() else "# Rohwelt-Lupe fuer Drittperioden-Treffer"
    lines = [
        title,
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Lupe liest die rohweltnaechsten Treffer aus 1695 in ihren Episodenabschnitten.",
        "Sie bleibt passiv: keine Handlung, kein Gate, keine Richtung.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Welche Welt- und Feldlage steht direkt an wiederkehrenden Milieu-Wechseln?",
        "2. Unterpruefung: Top-Treffer aus 1695 mit Basisphase, Folgephase und Vorfenster vergleichen.",
        "3. Folgeschritt: Wiederkehrende Vorfensterprofile ueber weitere Assetfenster pruefen.",
        "",
        "## Kompakte Trefferlupe",
        "",
        "| Familie | Wechsel | Welt | Folge-Ticks | Vorfenster Range | Vorfenster Hoeren | Vorfenster Spannung | Folge Range | Folge Hoeren | Folge Spannung |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["family"]),
                    str(row["transition"]),
                    str(row["world"]),
                    _fmt(float(row["follow_ticks"]), 0),
                    _fmt(float(row["pre_raw_range_pct"])),
                    _fmt(float(row["pre_hearing_gap"])),
                    _fmt(float(row["pre_mcm_tension"])),
                    _fmt(float(row["follow_raw_range_pct"])),
                    _fmt(float(row["follow_hearing_gap"])),
                    _fmt(float(row["follow_mcm_tension"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Diese Tabelle zeigt nicht, warum ein Wechsel entsteht.",
            "Sie zeigt, welche rohen Welt- und Innenfeldbedingungen direkt vor und waehrend der wiederkehrenden Familienbewegung sichtbar sind.",
            "",
            "Auffaellig sind Treffer, bei denen das Vorfenster und die Folgephase in Hoeren-Gap und Feldspannung nahe beieinander bleiben. Dort wirkt der Wechsel eher wie eine Milieu-Umlagerung derselben Familienlage, nicht wie ein komplett neuer Rohreiz.",
            "",
        ]
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Liest 1695-Drittperiodentreffer in Episoden- und Rohweltfenstern.")
    parser.add_argument("--hit-csv", required=True)
    parser.add_argument("--world", nargs=5, action="append", required=True, metavar=("NAME", "BASE_EP", "FOLLOW_EP", "BASE_RAW", "FOLLOW_RAW"))
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--lookback", type=int, default=8)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    rows = _build_loupe(args)
    _write_md(rows, _resolve(args.out_md))
    print({"out_md": str(_resolve(args.out_md)), "rows": len(rows), "top": args.top, "lookback": args.lookback})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
