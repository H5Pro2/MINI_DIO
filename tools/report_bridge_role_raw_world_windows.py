from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


EPISODE_KEYS = [
    "hoeren_energy_tone",
    "hoeren_energy_shift",
    "sehen_form_stability",
    "sehen_form_change",
    "rezeptor_field_intake_pressure",
    "perception_auditory_loudness",
    "mcm_feldwirkung_mcm_tension",
    "mcm_feldwirkung_mcm_coherence",
    "mcm_rekopplung_quality",
    "mcm_carry_quality",
    "mcm_strain_quality",
]


def _load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _float(row: dict[str, str], key: str) -> float:
    try:
        value = float(row.get(key, "") or 0.0)
    except ValueError:
        return 0.0
    return 0.0 if value != value else value


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _world_label(debug_dir: Path) -> str:
    return debug_dir.name.replace("follow_candidate_", "").replace("_", " ")


def _load_data_path(debug_dir: Path) -> Path | None:
    report_path = debug_dir / "dio_mini_lauf_2" / "mini_report.json"
    if not report_path.exists():
        return None
    report = json.loads(report_path.read_text(encoding="utf-8"))
    data_path = report.get("data_path")
    if not data_path:
        return None
    return Path(data_path)


def _raw_metrics(rows: list[dict[str, str]], center_tick: int, radius: int, volume_baseline: float) -> dict[str, float]:
    start = max(0, center_tick - radius - 1)
    end = min(len(rows), center_tick + radius)
    window = rows[start:end]
    if not window:
        return {
            "raw_window_rows": 0,
            "raw_return": 0.0,
            "raw_range_ratio": 0.0,
            "raw_body_ratio": 0.0,
            "raw_volume_to_world": 0.0,
            "raw_direction_consistency": 0.0,
        }

    first_open = _float(window[0], "open")
    last_close = _float(window[-1], "close")
    highs = [_float(row, "high") for row in window]
    lows = [_float(row, "low") for row in window]
    volumes = [_float(row, "volume") for row in window]
    bodies = [abs(_float(row, "close") - _float(row, "open")) for row in window]
    ranges = [max(0.0, _float(row, "high") - _float(row, "low")) for row in window]
    closes = [_float(row, "close") for row in window]
    deltas = [closes[idx] - closes[idx - 1] for idx in range(1, len(closes))]
    positive = sum(1 for value in deltas if value > 0.0)
    negative = sum(1 for value in deltas if value < 0.0)
    direction_consistency = abs(positive - negative) / max(1, positive + negative)
    price_base = max(abs(first_open), 1e-9)

    return {
        "raw_window_rows": len(window),
        "raw_return": round((last_close - first_open) / price_base, 8),
        "raw_range_ratio": round((max(highs) - min(lows)) / price_base, 8),
        "raw_body_ratio": round(_avg(bodies) / price_base, 8),
        "raw_volume_to_world": round(_avg(volumes) / max(1e-9, volume_baseline), 8),
        "raw_direction_consistency": round(direction_consistency, 6),
    }


def _target_rows(debug_dirs: list[Path], role_rows: list[dict[str, str]], root: Path, radius: int) -> list[dict[str, object]]:
    role_by_world_family = {
        (row.get("world", "") or "", row.get("family", "") or ""): row
        for row in role_rows
        if row.get("family")
    }
    out: list[dict[str, object]] = []
    for debug_dir in debug_dirs:
        world = _world_label(debug_dir)
        episodes_path = debug_dir / "dio_mini_lauf_2" / "episodes.csv"
        data_path = _load_data_path(debug_dir)
        if not episodes_path.exists() or data_path is None:
            continue
        resolved_data = data_path if data_path.is_absolute() else root / data_path
        if not resolved_data.exists():
            continue
        raw_rows = _load_csv(resolved_data)
        volume_baseline = _avg([_float(row, "volume") for row in raw_rows])
        for episode in _load_csv(episodes_path):
            family = episode.get("symbol_family", "") or ""
            role_row = role_by_world_family.get((world, family))
            if not role_row:
                continue
            tick = int(_float(episode, "tick"))
            item: dict[str, object] = {
                "world": world,
                "family": family,
                "baseline_role": role_row.get("baseline_role", "-"),
                "observed_role": role_row.get("observed_role", "-"),
                "role_state": role_row.get("role_state", "-"),
                "tick": tick,
                "timestamp_ms": episode.get("timestamp_ms", ""),
                "passive_mcm_effect_class": episode.get("passive_mcm_effect_class", "-") or "-",
            }
            for key in EPISODE_KEYS:
                item[key] = round(_float(episode, key), 6)
            item.update(_raw_metrics(raw_rows, tick, radius, volume_baseline))
            out.append(item)
    return out


def _summary(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["family"]), str(row["baseline_role"]), str(row["role_state"]))].append(row)

    out: list[dict[str, object]] = []
    for (family, baseline_role, role_state), items in grouped.items():
        effect_counts = Counter(str(row["passive_mcm_effect_class"]) for row in items)
        observed_counts = Counter(str(row["observed_role"]) for row in items)
        out_row: dict[str, object] = {
            "family": family,
            "baseline_role": baseline_role,
            "role_state": role_state,
            "events": len(items),
            "worlds": len(set(str(row["world"]) for row in items)),
            "observed_role_profile": ";".join(f"{name}:{count}" for name, count in observed_counts.most_common(5)),
            "effect_profile": ";".join(f"{name}:{count}" for name, count in effect_counts.most_common(5)),
        }
        for key in EPISODE_KEYS:
            out_row[key] = round(_avg([float(row[key]) for row in items]), 6)
        for key in [
            "raw_return",
            "raw_range_ratio",
            "raw_body_ratio",
            "raw_volume_to_world",
            "raw_direction_consistency",
        ]:
            out_row[key] = round(_avg([float(row[key]) for row in items]), 8)
        out.append(out_row)

    out.sort(key=lambda row: (str(row["family"]), str(row["role_state"])))
    return out


def _write_csv(rows: list[dict[str, object]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        out.write_text("", encoding="utf-8")
        return
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(summary_rows: list[dict[str, object]], out: Path) -> None:
    stable = [row for row in summary_rows if row["role_state"] == "stabil"]
    shifted = [row for row in summary_rows if row["role_state"] == "gekippt"]
    lines = [
        "# 1187 - Brueckenrollen Rohweltfenster",
        "",
        "## Grundfrage",
        "",
        "Welche konkreten Weltmerkmale halten eine Brueckenrolle stabil, und welche Merkmale begleiten ein Kippen der Rolle?",
        "",
        "Die Auswertung bindet die passiven Rollen aus 1184/1185 an OHLCV-Fenster zurueck.",
        "Sie bleibt Diagnose: keine Handlung, kein Gate, keine Strategie.",
        "",
        "## Stabile Rollen",
        "",
        "| Familie | Rolle | Ereignisse | Welten | Return | Range | Body | Volumen | Richtung | Rekopplung | Strain | Tension |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in stable:
        lines.append(
            f"| {row['family']} | {row['baseline_role']} | {row['events']} | {row['worlds']} | "
            f"{float(row['raw_return']):+.5f} | {float(row['raw_range_ratio']):.5f} | "
            f"{float(row['raw_body_ratio']):.5f} | {float(row['raw_volume_to_world']):.3f} | "
            f"{float(row['raw_direction_consistency']):.3f} | {float(row['mcm_rekopplung_quality']):.4f} | "
            f"{float(row['mcm_strain_quality']):.4f} | {float(row['mcm_feldwirkung_mcm_tension']):.4f} |"
        )

    lines.extend(
        [
            "",
            "## Gekippte Rollen",
            "",
            "| Familie | Baseline | Beobachtet | Ereignisse | Welten | Return | Range | Body | Volumen | Richtung | Rekopplung | Strain | Tension |",
            "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in shifted:
        lines.append(
            f"| {row['family']} | {row['baseline_role']} | {row['observed_role_profile']} | {row['events']} | {row['worlds']} | "
            f"{float(row['raw_return']):+.5f} | {float(row['raw_range_ratio']):.5f} | "
            f"{float(row['raw_body_ratio']):.5f} | {float(row['raw_volume_to_world']):.3f} | "
            f"{float(row['raw_direction_consistency']):.3f} | {float(row['mcm_rekopplung_quality']):.4f} | "
            f"{float(row['mcm_strain_quality']):.4f} | {float(row['mcm_feldwirkung_mcm_tension']):.4f} |"
        )

    avg_stable_range = _avg([float(row["raw_range_ratio"]) for row in stable])
    avg_shifted_range = _avg([float(row["raw_range_ratio"]) for row in shifted])
    avg_stable_tension = _avg([float(row["mcm_feldwirkung_mcm_tension"]) for row in stable])
    avg_shifted_tension = _avg([float(row["mcm_feldwirkung_mcm_tension"]) for row in shifted])
    avg_stable_strain = _avg([float(row["mcm_strain_quality"]) for row in stable])
    avg_shifted_strain = _avg([float(row["mcm_strain_quality"]) for row in shifted])

    lines.extend(
        [
            "",
            "## Vergleich",
            "",
            f"- durchschnittliche Roh-Range stabil: `{avg_stable_range:.5f}`",
            f"- durchschnittliche Roh-Range gekippt: `{avg_shifted_range:.5f}`",
            f"- durchschnittliche MCM-Spannung stabil: `{avg_stable_tension:.5f}`",
            f"- durchschnittliche MCM-Spannung gekippt: `{avg_shifted_tension:.5f}`",
            f"- durchschnittliche Strain stabil: `{avg_stable_strain:.5f}`",
            f"- durchschnittliche Strain gekippt: `{avg_shifted_strain:.5f}`",
            "",
            "## Lesart",
            "",
            "Stabile Rollen sind nicht einfach haeufige Symbole, sondern erscheinen in Rohweltfenstern mit eigener MCM-Rueckbindung.",
            "Kippende Rollen zeigen, dass eine Familie ihre lokale Bedeutung unter anderer Weltspannung verschieben kann.",
            "",
            "Damit wird die MCM-Lesung konkreter: Die Rolle haengt nicht nur am Zeichen, sondern an Weltfenster, Ton, Form, Rezeptoraufnahme und Feldwirkung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte aus diesen Rohweltmerkmalen eine passive Rollenkarte entstehen: stabile Rueckbindung, belastete Randnaehe, Uebergangsoeffnung und gemischte Nachbarschaft als Feldzonen.",
        ]
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--roles", required=True)
    parser.add_argument("--debug-dir", action="append", required=True)
    parser.add_argument("--root", default=".")
    parser.add_argument("--radius", type=int, default=6)
    parser.add_argument("--out-events", required=True)
    parser.add_argument("--out-summary", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    root = Path(args.root).resolve()
    role_rows = _load_csv(Path(args.roles))
    debug_dirs = [Path(value) for value in args.debug_dir]
    events = _target_rows(debug_dirs, role_rows, root, args.radius)
    summary = _summary(events)
    _write_csv(events, Path(args.out_events))
    _write_csv(summary, Path(args.out_summary))
    _write_md(summary, Path(args.out_md))
    print(f"events={len(events)} summary_rows={len(summary)}")
    print(f"wrote {args.out_events}")
    print(f"wrote {args.out_summary}")
    print(f"wrote {args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
