from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

from befunde_paths import befunde_root
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
OUT_CSV = befunde_root(ROOT) / "1381_FELDFUNKTIONSKARTE_GLOBALE_PROBE.csv"
OUT_MD = befunde_root(ROOT) / "1381_FELDFUNKTIONSKARTE_GLOBALE_PROBE.md"

EPISODE_SETS = [
    ("BTC_2024_5M", ROOT / "debug" / "adapted_field_btc_2024_5m_2k" / "dio_mini_lauf_2" / "episodes.csv"),
    ("SOL_2024_5M", ROOT / "debug" / "adapted_field_sol_2024_5m_2k" / "dio_mini_lauf_2" / "episodes.csv"),
    ("PAXG_2024_5M", ROOT / "debug" / "adapted_field_paxg_2024_5m_10k" / "dio_mini_lauf_2" / "episodes.csv"),
    ("XRP_2024_5M", ROOT / "debug" / "adapted_field_xrp_2024_5m_10k" / "dio_mini_lauf_2" / "episodes.csv"),
    ("DOGE_2024_5M", ROOT / "debug" / "adapted_field_doge_2024_5m_10k" / "dio_mini_lauf_2" / "episodes.csv"),
]


def _float(row: dict[str, str], key: str) -> float:
    try:
        value = float(row.get(key, "0") or 0.0)
    except ValueError:
        return 0.0
    return 0.0 if value != value else value


def _read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _mode(values: list[str]) -> str:
    if not values:
        return "-"
    return Counter(values).most_common(1)[0][0]


def _quantile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = int(round((len(ordered) - 1) * q))
    return ordered[max(0, min(index, len(ordered) - 1))]


def _window_rows(rows: list[dict[str, str]], size: int = 100) -> list[dict[str, object]]:
    windows: list[dict[str, object]] = []
    for start in range(0, len(rows), size):
        chunk = rows[start : start + size]
        if len(chunk) < max(20, size // 2):
            continue
        ticks = [int(float(row.get("tick", "0") or 0)) for row in chunk]
        windows.append(
            {
                "start_tick": min(ticks),
                "end_tick": max(ticks),
                "rekopplung": mean(_float(row, "mcm_rekopplung_quality") for row in chunk),
                "carry": mean(_float(row, "mcm_carry_quality") for row in chunk),
                "strain": mean(_float(row, "mcm_strain_quality") for row in chunk),
                "sensory": mean(_float(row, "mcm_sensory_coupling") for row in chunk),
                "visual_gap": mean(_float(row, "mcm_visual_field_gap") for row in chunk),
                "hearing_gap": mean(_float(row, "mcm_hearing_field_gap") for row in chunk),
                "preview": _mode([row.get("mcm_field_episode_preview_symbol", "-") for row in chunk]),
                "family": _mode([row.get("symbol_family", "-") for row in chunk]),
                "effect_class": _mode([row.get("passive_mcm_effect_class", "-") for row in chunk]),
            }
        )
    return windows


def _label(value: float, low: float, high: float) -> str:
    if value <= low:
        return "low"
    if value >= high:
        return "high"
    return "mid"


def _phase_rows(world: str, path: Path) -> list[dict[str, object]]:
    rows = _read(path)
    windows = _window_rows(rows)
    if len(windows) < 3:
        return []

    quantiles: dict[str, tuple[float, float]] = {}
    for key in ["rekopplung", "carry", "strain", "sensory", "visual_gap", "hearing_gap"]:
        values = [float(window[key]) for window in windows]
        quantiles[key] = (_quantile(values, 0.33), _quantile(values, 0.67))

    out: list[dict[str, object]] = []
    for index, current in enumerate(windows):
        previous = windows[index - 1] if index > 0 else None
        following = windows[index + 1] if index + 1 < len(windows) else None

        labels = {
            key: _label(float(current[key]), *quantiles[key])
            for key in ["rekopplung", "carry", "strain", "sensory", "visual_gap", "hearing_gap"]
        }
        sensory_delta = float(current["sensory"]) - (float(previous["sensory"]) if previous else float(current["sensory"]))
        rekopplung_delta = float(current["rekopplung"]) - (
            float(previous["rekopplung"]) if previous else float(current["rekopplung"])
        )
        strain_delta_next = (float(following["strain"]) if following else float(current["strain"])) - float(current["strain"])
        rekopplung_delta_next = (float(following["rekopplung"]) if following else float(current["rekopplung"])) - float(
            current["rekopplung"]
        )
        preview_carry_next = int(bool(following and current["preview"] == following["preview"]))

        bridge_near = sensory_delta > 0 and rekopplung_delta >= -0.002 and labels["sensory"] in {"mid", "high"}
        center_near = labels["rekopplung"] == "high" and labels["carry"] in {"mid", "high"} and labels["strain"] == "low"
        edge_near = labels["strain"] == "high" and labels["sensory"] == "high" and labels["rekopplung"] in {"low", "mid"}
        release_near = strain_delta_next < 0 and rekopplung_delta_next < 0 and labels["strain"] in {"mid", "high"}

        hits = [
            name
            for name, active in [
                ("brueckennaehe", bridge_near),
                ("zentrumsnaehe", center_near),
                ("randdrucknaehe", edge_near),
                ("entlastungsnaehe", release_near),
            ]
            if active
        ]
        if len(hits) > 1:
            passive_role_near = "mischrolle_" + "_".join(hits)
        elif hits:
            passive_role_near = hits[0]
        else:
            passive_role_near = "keine_naehe"

        out.append(
            {
                "world": world,
                "source": str(path.relative_to(ROOT)),
                "start_tick": current["start_tick"],
                "end_tick": current["end_tick"],
                "passive_role_near": passive_role_near,
                "rekopplung_level": labels["rekopplung"],
                "carry_level": labels["carry"],
                "strain_level": labels["strain"],
                "sensory_level": labels["sensory"],
                "visual_gap_level": labels["visual_gap"],
                "hearing_gap_level": labels["hearing_gap"],
                "sensory_delta": round(sensory_delta, 6),
                "rekopplung_delta": round(rekopplung_delta, 6),
                "strain_delta_next": round(strain_delta_next, 6),
                "rekopplung_delta_next": round(rekopplung_delta_next, 6),
                "preview_carry_next": preview_carry_next,
                "preview": current["preview"],
                "family": current["family"],
                "effect_class": current["effect_class"],
                "passive_only": 1,
                "influences_action": 0,
            }
        )
    return out


def build_report() -> None:
    rows: list[dict[str, object]] = []
    missing: list[str] = []
    for world, path in EPISODE_SETS:
        if not path.exists():
            missing.append(str(path.relative_to(ROOT)))
            continue
        rows.extend(_phase_rows(world, path))
    if not rows:
        raise RuntimeError("no rows for global fieldfunction probe")

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    role_counts = Counter(str(row["passive_role_near"]) for row in rows)
    world_role_counts: dict[str, Counter[str]] = {}
    for row in rows:
        world_role_counts.setdefault(str(row["world"]), Counter())[str(row["passive_role_near"])] += 1
    preview_carry = Counter(str(row["passive_role_near"]) for row in rows if int(row["preview_carry_next"]))

    lines = [
        "# 1381 - Feldfunktionskarte: globale passive Probe",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest groessere vorhandene `episodes.csv` rollenneutral in lokale Feldphasen.",
        "",
        "Erst danach wird nur eine Naehe zu bekannten Feldfunktionen markiert:",
        "",
        "- Brueckennaehe",
        "- Zentrumsnaehe",
        "- Randdrucknaehe",
        "- Entlastungsnaehe",
        "- Mischrolle",
        "",
        "Wichtig: Diese Naehen sind keine neuen Rollen und keine Handlung. Sie sind eine passive Gegenprobe fuer `1378`.",
        "",
        "## Datengrundlage",
        "",
        f"- gelesene Weltfenster: `{len(rows)}`",
    ]
    if missing:
        lines.append(f"- fehlende Episodensets: `{', '.join(missing)}`")
    lines.extend(["", "## Rollennaehe gesamt", ""])
    for role, count in role_counts.most_common():
        lines.append(f"- `{role}`: `{count}`")
    lines.extend(["", "## Rollennaehe je Welt", ""])
    for world, counts in sorted(world_role_counts.items()):
        text = " | ".join(f"{key}:{value}" for key, value in counts.most_common())
        lines.append(f"- `{world}`: {text}")
    lines.extend(["", "## Nachhallhinweis", ""])
    for role, count in preview_carry.most_common():
        lines.append(f"- `{role}` mit Preview-Folgecarry: `{count}`")
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Die globale Probe erzeugt bewusst keine harte Rollenentscheidung.",
            "",
            "Wenn eine bekannte Naehe in groesseren Episodensets wieder auftaucht, spricht das fuer eine allgemeinere Feldfunktion.",
            "Wenn Mischrollen oder `keine_naehe` dominieren, bleibt die bisherige Karte eher mikrophasen- oder weltspannungsgebunden.",
            "",
            "## Grenze",
            "",
            "Die Naeheklassifikation ist relativ je Welt kalibriert. Sie vergleicht also nicht BTC, SOL, PAXG usw. mit festen absoluten Werten.",
            "",
            "Das verhindert eine mechanische Uebertragung, ersetzt aber keine spaetere Positiv-/Negativkontrolle.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build_report()
