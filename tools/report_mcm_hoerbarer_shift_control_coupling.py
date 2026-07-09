from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

from befunde_paths import befunde_root
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mini_world import build_sensory_profile, load_candles
from tools.report_mcm_hoerbarer_shift_symbol_coupling import (
    EPISODE_MAP,
    _basename,
    _float,
    _load_episode_rows,
    _summarize_window,
)
from tools.report_worldlage_multiscale_raw_windows import _raw_window_profile


INPUT = befunde_root(ROOT) / "1351_HOERBARER_SCHMALER_SHIFT_ROLLELESUNG.csv"
OUT_CSV = befunde_root(ROOT) / "1353_HOERBARER_SCHMALER_SHIFT_KONTROLLKOPPLUNG.csv"
OUT_MD = befunde_root(ROOT) / "1353_HOERBARER_SCHMALER_SHIFT_KONTROLLKOPPLUNG.md"


def _world_path(source_file: str) -> Path:
    return ROOT / source_file.replace("\\", "/")


def _candidate_keys(rows: list[dict[str, str]]) -> set[tuple[str, int, int, int]]:
    return {
        (
            _basename(row["source_file"]),
            int(_float(row["scale"])),
            int(_float(row["start_tick"])),
            int(_float(row["end_tick"])),
        )
        for row in rows
    }


def _find_control_window(
    source_file: str,
    scale: int,
    excluded: set[tuple[str, int, int, int]],
    used: set[tuple[str, int, int, int]],
) -> tuple[int, int, dict[str, float]] | None:
    path = _world_path(source_file)
    candles = load_candles(path)
    profile = build_sensory_profile(candles, window=5)
    basename = _basename(source_file)

    for start in range(scale * 2, max(0, len(candles) - (scale * 2)), scale):
        end = start + scale
        key = (basename, scale, start, end)
        if key in excluded or key in used:
            continue
        pre = _raw_window_profile(candles, profile, start - scale, start, window=5)
        during = _raw_window_profile(candles, profile, start, end, window=5)
        if _float(during["avg_auditory"]) <= _float(pre["avg_auditory"]):
            return start, end, {
                "pre_hoeren": _float(pre["avg_auditory"]),
                "during_hoeren": _float(during["avg_auditory"]),
                "pre_druck": _float(pre["avg_field_pressure"]),
                "during_druck": _float(during["avg_field_pressure"]),
                "pre_range": _float(pre["avg_range_pct"]),
                "during_range": _float(during["avg_range_pct"]),
            }
    return None


def build_report() -> None:
    with INPUT.open("r", encoding="utf-8", newline="") as handle:
        candidate_rows = list(csv.DictReader(handle))

    excluded = _candidate_keys(candidate_rows)
    used: set[tuple[str, int, int, int]] = set()
    episode_cache: dict[str, list[dict[str, str]]] = {}
    out_rows: list[dict[str, str]] = []

    for candidate in candidate_rows:
        source_file = candidate["source_file"]
        basename = _basename(source_file)
        scale = int(_float(candidate["scale"]))
        control = _find_control_window(source_file, scale, excluded, used)
        if control is None:
            continue
        start, end, raw = control
        used.add((basename, scale, start, end))

        episode_path = EPISODE_MAP.get(basename)
        if episode_path is None:
            summary = {
                "episode_rows": "0",
                "top_symbol_family": "-",
                "top_episode_symbol": "-",
                "top_mcm_episode_symbol": "-",
                "top_preview_symbol": "-",
                "top_meaning_state": "-",
                "avg_carry": "0.000000",
                "avg_strain": "0.000000",
                "avg_rekopplung": "0.000000",
                "avg_sensory_coupling": "0.000000",
                "symbol_diversity": "0",
                "meaning_diversity": "0",
                "mapping_status": "missing_episode_mapping",
            }
        else:
            key = str(episode_path)
            if key not in episode_cache:
                episode_cache[key] = _load_episode_rows(episode_path)
            summary = _summarize_window(episode_cache[key], start, end)

        row = {
            "asset": candidate["asset"],
            "world": candidate["world"],
            "source_file": source_file,
            "scale": str(scale),
            "start_tick": str(start),
            "end_tick": str(end),
            "control_for_phase_role": candidate["phase_role"],
            "control_for_base_sequence": candidate["base_sequence"],
            "pre_hoeren": f"{raw['pre_hoeren']:.6f}",
            "during_hoeren": f"{raw['during_hoeren']:.6f}",
            "pre_druck": f"{raw['pre_druck']:.6f}",
            "during_druck": f"{raw['during_druck']:.6f}",
            "pre_range": f"{raw['pre_range']:.6f}",
            "during_range": f"{raw['during_range']:.6f}",
            "hearing_rises_vs_pre": "0",
        }
        row.update(summary)
        out_rows.append(row)

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    mapped = [row for row in out_rows if row["mapping_status"] == "mapped"]
    families = Counter(row["top_symbol_family"] for row in mapped)
    previews = Counter(row["top_preview_symbol"] for row in mapped)
    meanings = Counter(row["top_meaning_state"] for row in mapped)

    lines = [
        "# 1353 - Hoerbarer schmaler Shift: Kontrollkopplung",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft Kontrollfenster aus denselben Quellen und Fensterbreiten wie `1351`, aber ohne Hoeranstieg gegen das Vorfenster.",
        "Damit wird geprueft, ob die in `1352` beobachtete Symbolkopplung spezifisch fuer die kompakte Hoer-/Druckphase ist.",
        "",
        "## Befund",
        "",
        f"- Kontrollfenster: {len(out_rows)}",
        f"- Gemappte Kontrollfenster: {len(mapped)}",
        f"- Top-Symbolfamilien: {families.most_common(8)}",
        f"- Top-MCM-Preview-Symbole: {previews.most_common(8)}",
        f"- Top-Bedeutungszustaende: {meanings.most_common(8)}",
        f"- Rekopplung Mittel: {mean(_float(row['avg_rekopplung']) for row in mapped):.6f}",
        f"- Strain Mittel: {mean(_float(row['avg_strain']) for row in mapped):.6f}",
        "",
        "## Vergleich zu 1352",
        "",
        "`1352` zeigte bei den Hoer-/Druckfenstern eine starke Kopplung an `meaning_stable_inner_field` und mehrere rollenabhaengige Preview-Symbole.",
        "Diese Kontrollgruppe zeigt, ob aehnliche Symbole auch ohne Hoeranstieg auftreten.",
        "Wenn ja, ist die Symbolfamilie nicht exklusiv. Dann liegt die Spezifik eher in der Rollenfolge und Rohweltphase, nicht im einzelnen `dio_*`-Namen.",
        "",
        "## Wie es weitergeht",
        "",
        "Als naechstes sollten `1352` und `1353` direkt als Differenzprofil verglichen werden: Welche Symbol-, Preview- und Bedeutungsanteile bleiben gleich, und welche entstehen nur bei Hoeranstieg.",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build_report()
