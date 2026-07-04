from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
BASE_NODES = ROOT / "docs" / "befunde" / "1389_BEDEUTUNGSNETZ_KNOTEN.csv"
ROLE_FAMILIES = ROOT / "docs" / "befunde" / "1394_BEDEUTUNGSNETZ_FELDROLLEN_FAMILIEN.csv"
EPISODE_FILES = {
    "HOLDOUT_2024_BRIDGE_TEST1": ROOT / "debug" / "1395_holdout_bridge_test1" / "dio_mini_lauf_2" / "episodes.csv",
    "HOLDOUT_2024_BRIDGE_TEST2": ROOT / "debug" / "1396_holdout_bridge_test2" / "dio_mini_lauf_2" / "episodes.csv",
    "HOLDOUT_QUIET_SOL2025": ROOT / "debug" / "1397_holdout_quiet_sol2025" / "dio_mini_lauf_2" / "episodes.csv",
    "HOLDOUT_SMOOTH_CONTROL": ROOT / "debug" / "1398_holdout_smooth_control" / "dio_mini_lauf_2" / "episodes.csv",
    "HOLDOUT_POSITIVE_EXPANSION": ROOT / "debug" / "1399_holdout_positive_expansion" / "dio_mini_lauf_2" / "episodes.csv",
    "HOLDOUT_QUIET_DRIFT": ROOT / "debug" / "1400_holdout_quiet_drift" / "dio_mini_lauf_2" / "episodes.csv",
    "HOLDOUT_MEDIUM_QUIET_DRIFT": ROOT / "debug" / "1401_holdout_medium_quiet_drift" / "dio_mini_lauf_2" / "episodes.csv",
    "HOLDOUT_NOISY_DRIFT": ROOT / "debug" / "1402_holdout_noisy_drift" / "dio_mini_lauf_2" / "episodes.csv",
    "HOLDOUT_HIGH_NOISY_DRIFT": ROOT / "debug" / "1403_holdout_high_noisy_drift" / "dio_mini_lauf_2" / "episodes.csv",
    "HOLDOUT_COMBINED_STRESS": ROOT / "debug" / "1404_holdout_combined_stress" / "dio_mini_lauf_2" / "episodes.csv",
    "HOLDOUT_HIGH_FREQUENCY_SWITCH": ROOT / "debug" / "1405_holdout_high_frequency_switch" / "dio_mini_lauf_2" / "episodes.csv",
    "HOLDOUT_FREQ25": ROOT / "debug" / "1406_holdout_freq25" / "dio_mini_lauf_2" / "episodes.csv",
    "HOLDOUT_FREQ50": ROOT / "debug" / "1407_holdout_freq50" / "dio_mini_lauf_2" / "episodes.csv",
    "HOLDOUT_FREQ75": ROOT / "debug" / "1408_holdout_freq75" / "dio_mini_lauf_2" / "episodes.csv",
    "HOLDOUT_FREQ100": ROOT / "debug" / "1409_holdout_freq100" / "dio_mini_lauf_2" / "episodes.csv",
    "HOLDOUT_RHYTHM_REGULAR": ROOT / "debug" / "1410_holdout_rhythm_regular" / "dio_mini_lauf_2" / "episodes.csv",
    "HOLDOUT_RHYTHM_BLOCK": ROOT / "debug" / "1411_holdout_rhythm_block" / "dio_mini_lauf_2" / "episodes.csv",
    "HOLDOUT_RHYTHM_IRREGULAR": ROOT / "debug" / "1412_holdout_rhythm_irregular" / "dio_mini_lauf_2" / "episodes.csv",
    "HOLDOUT_RHYTHM_WAVE": ROOT / "debug" / "1413_holdout_rhythm_wave" / "dio_mini_lauf_2" / "episodes.csv",
}
OUT_CSV = ROOT / "docs" / "befunde" / "1395_HOLDOUT_FELDROLLEN_STABILITAET.csv"
OUT_MD = ROOT / "docs" / "befunde" / "1395_HOLDOUT_FELDROLLEN_STABILITAET.md"

WINDOW = 100


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def _float(row: dict[str, str], key: str) -> float:
    try:
        return float(row.get(key, "0") or 0.0)
    except ValueError:
        return 0.0


def _tier(value: float, low: float, high: float, low_name: str, mid_name: str, high_name: str) -> str:
    if value <= low:
        return low_name
    if value >= high:
        return high_name
    return mid_name


def _signature(row: dict[str, float | str]) -> str:
    tone = _tier(float(row["tone"]), -0.001, 0.001, "leise", "mittlerer_ton", "laut")
    shift = _tier(abs(float(row["shift"])), 0.001, 0.006, "ruhiger_ton", "bewegter_ton", "starker_tonwechsel")
    stability = float(row["stability"])
    visual = "stabile_form" if stability >= 0.32 else "bewegte_form"
    if stability >= 0.58:
        movement = "weite_range+viel_wechsel+geringe_persistenz"
    elif stability <= 0.34:
        movement = "mittlere_range+viel_wechsel+geringe_persistenz"
    else:
        movement = "mittlere_range+mittlerer_wechsel+mittlere_persistenz"
    intake = float(row["intake"])
    tension = float(row["tension"])
    intake_name = _tier(intake, 0.02, 0.08, "gedaempfte_aufnahme", "mittlere_aufnahme", "starke_aufnahme")
    tension_name = _tier(tension, 0.02, 0.08, "geringe_feldspannung", "mittlere_feldspannung", "hohe_feldspannung")
    return f"{tone}+{shift}|{visual}|{movement}|{intake_name}+{tension_name}"


def _parts(signature: str) -> set[str]:
    parts: set[str] = set()
    for block in (signature or "").split("|"):
        parts.update(part for part in block.split("+") if part)
    return parts


def _similarity(left: str, right: str) -> float:
    a = _parts(left)
    b = _parts(right)
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def _windows(world: str, rows: list[dict[str, str]]) -> list[dict[str, float | str]]:
    out: list[dict[str, float | str]] = []
    for start in range(0, len(rows), WINDOW):
        chunk = rows[start : start + WINDOW]
        if not chunk:
            continue
        effect_counts = Counter(row.get("passive_mcm_effect_class", "") for row in chunk)
        out.append(
            {
                "world": world,
                "start_tick": chunk[0].get("tick", str(start + 1)),
                "end_tick": chunk[-1].get("tick", str(start + len(chunk))),
                "tone": mean(_float(row, "hoeren_energy_tone") for row in chunk),
                "shift": mean(_float(row, "hoeren_energy_shift") for row in chunk),
                "stability": mean(_float(row, "sehen_form_stability") for row in chunk),
                "intake": mean(_float(row, "perception_adapted_field_intake_pressure") for row in chunk),
                "tension": mean(_float(row, "mcm_feldwirkung_mcm_tension") for row in chunk),
                "carry": mean(_float(row, "mcm_carry_quality") for row in chunk),
                "strain": mean(_float(row, "mcm_strain_quality") for row in chunk),
                "rekopplung": mean(_float(row, "mcm_rekopplung_quality") for row in chunk),
                "effect": effect_counts.most_common(1)[0][0],
                "effect_mix": "|".join(f"{key}:{value}" for key, value in effect_counts.most_common() if key),
                "family": Counter(row.get("symbol_family", "") for row in chunk).most_common(1)[0][0],
            }
        )
    return out


def main() -> None:
    base_nodes = _read_rows(BASE_NODES)
    roles = {row["old_node"]: row["role_family"] for row in _read_rows(ROLE_FAMILIES)}
    old_signatures = {
        row["meaning_node"]: row["signature"]
        for row in base_nodes
        if row.get("meaning_node") in roles
    }

    out_rows: list[dict[str, str]] = []
    for world, episode_path in EPISODE_FILES.items():
        episode_rows = _read_rows(episode_path)
        for win in _windows(world, episode_rows):
            signature = _signature(win)
            ranked = sorted(
                ((node, _similarity(signature, old_sig)) for node, old_sig in old_signatures.items()),
                key=lambda item: item[1],
                reverse=True,
            )
            nearest_node, nearest_similarity = ranked[0] if ranked else ("", 0.0)
            role = roles.get(nearest_node, "")
            exact = old_signatures.get(nearest_node) == signature
            if exact:
                state = "rolle_exakt_wiedergefunden"
            elif nearest_similarity >= 0.60:
                state = "rolle_als_nachbarschaft"
            elif nearest_similarity >= 0.40:
                state = "rolle_schwach_beruehrt"
            else:
                state = "neue_holdout_lage"
            out_rows.append(
                {
                    "world": str(win["world"]),
                    "start_tick": str(win["start_tick"]),
                    "end_tick": str(win["end_tick"]),
                    "signature": signature,
                    "holdout_state": state,
                    "nearest_node": nearest_node,
                    "nearest_role_family": role,
                    "nearest_similarity": f"{nearest_similarity:.6f}",
                    "effect": str(win["effect"]),
                    "effect_mix": str(win["effect_mix"]),
                    "family": str(win["family"]),
                    "carry": f"{float(win['carry']):.6f}",
                    "strain": f"{float(win['strain']):.6f}",
                    "rekopplung": f"{float(win['rekopplung']):.6f}",
                    "tone": f"{float(win['tone']):.6f}",
                    "shift": f"{float(win['shift']):.6f}",
                    "stability": f"{float(win['stability']):.6f}",
                    "intake": f"{float(win['intake']):.6f}",
                    "tension": f"{float(win['tension']):.6f}",
                }
            )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    state_counts = Counter(row["holdout_state"] for row in out_rows)
    role_counts = Counter(row["nearest_role_family"] for row in out_rows)
    effect_counts = Counter(row["effect"] for row in out_rows)
    world_counts = Counter(f"{row['world']}:{row['holdout_state']}" for row in out_rows)
    strong_lines = [
            f"- `{row['world']}:{row['start_tick']}-{row['end_tick']}` -> `{row['nearest_role_family']}` / `{row['holdout_state']}` / Naehe `{row['nearest_similarity']}` / Wirkung `{row['effect']}` / Mix `{row['effect_mix']}`"
        for row in out_rows
        if row["holdout_state"] in {"rolle_exakt_wiedergefunden", "rolle_als_nachbarschaft"}
    ]

    lines = [
        "# 1395 - Holdout Feldrollen-Stabilitaet",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft eine neue Holdout-Welt gegen die in `1394` gebildeten Feldrollen-Familien.",
        "",
        "Die Diagnose bleibt passiv. Sie prueft Wiederkehr, Nachbarschaft oder neue Lage.",
        "",
        "## Befund",
        "",
        f"- Holdout-Fenster: `{len(out_rows)}`",
        f"- Zustaende: `{', '.join(f'{key}:{value}' for key, value in state_counts.most_common())}`",
        f"- beruehrte Rollen: `{', '.join(f'{key}:{value}' for key, value in role_counts.most_common())}`",
        f"- Innenwirkungen: `{', '.join(f'{key}:{value}' for key, value in effect_counts.most_common())}`",
        f"- Welt/Zustand: `{', '.join(f'{key}:{value}' for key, value in world_counts.most_common())}`",
        "",
        "## Starke Wiederkehr / Nachbarschaft",
        "",
        *(strong_lines or ["- keine starke Rollenwiederkehr im Holdout"]),
        "",
        "## Lesung",
        "",
        "Der Holdout prueft nicht, ob Mini-DIO eine alte Tabelle kopiert.",
        "Entscheidend ist, ob neue Weltfenster in die Naehe vorhandener Feldrollen fallen.",
        "",
        "## Wie es weitergeht",
        "",
        "Als naechstes sollte nicht nur mehr Rauschen geprueft werden. Entscheidend ist die Kombination aus Range, Wechselrate, Tonverdichtung und Rezeptoraufnahme: dort liegt vermutlich die Schwelle, ab der stabile Oberflaechenvarianz in echte Spannungsnaehe kippt.",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
