from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

from befunde_paths import befunde_root
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
BASE_NODES = befunde_root(ROOT) / "1389_BEDEUTUNGSNETZ_KNOTEN.csv"
OUT_CSV = befunde_root(ROOT) / "1390_BEDEUTUNGSNETZ_FOLGEWELTEN.csv"
OUT_MD = befunde_root(ROOT) / "1390_BEDEUTUNGSNETZ_FOLGEWELTEN.md"

EPISODE_FILES = {
    "SYNTH_PURE_HEARING": ROOT / "debug" / "1390_follow_pure_hearing" / "dio_mini_lauf_2" / "episodes.csv",
    "SYNTH_VISUAL_BREAKS_STABLE_PULSE": ROOT
    / "debug"
    / "1390_follow_visual_breaks_stable_pulse"
    / "dio_mini_lauf_2"
    / "episodes.csv",
    "SYNTH_VISUAL_RECOUPLING_CHAOTIC_TONE": ROOT
    / "debug"
    / "1390_follow_visual_recoupling_chaotic_tone"
    / "dio_mini_lauf_2"
    / "episodes.csv",
}

PASSIVE_FLAGS = {
    "passive_only": 1,
    "read_by_mini_dio": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
}


def _float(row: dict[str, str], key: str) -> float:
    try:
        value = float(row.get(key, "0") or 0.0)
    except ValueError:
        return 0.0
    return 0.0 if value != value else value


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _avg(rows: list[dict[str, str]], key: str) -> float:
    return mean(_float(row, key) for row in rows) if rows else 0.0


def _quantiles(values: list[float]) -> tuple[float, float]:
    if not values:
        return 0.0, 0.0
    values = sorted(values)
    return values[int((len(values) - 1) * 0.33)], values[int((len(values) - 1) * 0.66)]


def _tier(value: float, lo: float, hi: float, low: str, mid: str, high: str) -> str:
    if value <= lo:
        return low
    if value >= hi:
        return high
    return mid


def _signature_parts(signature: str) -> list[str]:
    return [part.strip() for part in str(signature or "").split("|") if part.strip()]


def _signature_similarity(left: str, right: str) -> float:
    left_parts = set(_signature_parts(left))
    right_parts = set(_signature_parts(right))
    if not left_parts and not right_parts:
        return 1.0
    return len(left_parts & right_parts) / max(1, len(left_parts | right_parts))


def _window_rows(path: Path, world: str, window: int = 100) -> list[dict[str, object]]:
    rows = _read_csv(path)
    out: list[dict[str, object]] = []
    for start in range(0, len(rows), window):
        chunk = rows[start : start + window]
        if len(chunk) < max(8, window // 4):
            continue
        out.append(
            {
                "world": world,
                "source": str(path.relative_to(ROOT)),
                "start_tick": int(_float(chunk[0], "tick")),
                "end_tick": int(_float(chunk[-1], "tick")),
                "hoeren_energy_tone": _avg(chunk, "hoeren_energy_tone"),
                "hoeren_energy_shift": _avg(chunk, "hoeren_energy_shift"),
                "sehen_form_stability": _avg(chunk, "sehen_form_stability"),
                "sehen_form_change": _avg(chunk, "sehen_form_change"),
                "perception_adapted_field_intake_pressure": _avg(
                    chunk, "perception_adapted_field_intake_pressure"
                ),
                "mcm_feldwirkung_mcm_tension": _avg(chunk, "mcm_feldwirkung_mcm_tension"),
                "mcm_carry_quality": _avg(chunk, "mcm_carry_quality"),
                "mcm_strain_quality": _avg(chunk, "mcm_strain_quality"),
                "mcm_rekopplung_quality": _avg(chunk, "mcm_rekopplung_quality"),
                "mcm_sensory_coupling": _avg(chunk, "mcm_sensory_coupling"),
                "top_family": Counter(row.get("symbol_family", "-") for row in chunk).most_common(1)[0][0],
                "top_preview": Counter(row.get("mcm_field_episode_preview_symbol", "-") for row in chunk).most_common(1)[0][0],
                "top_effect": Counter(row.get("passive_mcm_effect_class", "-") for row in chunk).most_common(1)[0][0],
            }
        )
    return out


def _attach_signatures(rows: list[dict[str, object]]) -> None:
    q_keys = [
        "hoeren_energy_tone",
        "hoeren_energy_shift",
        "perception_adapted_field_intake_pressure",
        "mcm_feldwirkung_mcm_tension",
    ]
    quantiles = {key: _quantiles([float(row[key]) for row in rows]) for key in q_keys}

    for row in rows:
        tone_lo, tone_hi = quantiles["hoeren_energy_tone"]
        shift_lo, shift_hi = quantiles["hoeren_energy_shift"]
        intake_lo, intake_hi = quantiles["perception_adapted_field_intake_pressure"]
        tension_lo, tension_hi = quantiles["mcm_feldwirkung_mcm_tension"]

        tone = _tier(float(row["hoeren_energy_tone"]), tone_lo, tone_hi, "leise", "mittlerer_ton", "laut")
        shift = _tier(
            float(row["hoeren_energy_shift"]),
            shift_lo,
            shift_hi,
            "ruhiger_ton",
            "bewegter_ton",
            "starker_tonwechsel",
        )
        stability = float(row["sehen_form_stability"])
        visual_change = float(row["sehen_form_change"])
        if stability > visual_change:
            visual = "stabile_form"
        elif visual_change > stability:
            visual = "bewegte_form"
        else:
            visual = "balancierte_form"

        # For follow-world comparison we do not have the original raw candle
        # range tiers in episodes.csv, so movement is read as a sensory stability
        # proxy. This keeps the report passive and avoids reinterpreting the world.
        if stability >= 0.58:
            movement = "weite_range+viel_wechsel+geringe_persistenz"
        elif stability <= 0.34:
            movement = "mittlere_range+viel_wechsel+geringe_persistenz"
        else:
            movement = "mittlere_range+mittlerer_wechsel+mittlere_persistenz"

        intake = _tier(
            float(row["perception_adapted_field_intake_pressure"]),
            intake_lo,
            intake_hi,
            "gedaempfte_aufnahme",
            "mittlere_aufnahme",
            "starke_aufnahme",
        )
        tension = _tier(
            float(row["mcm_feldwirkung_mcm_tension"]),
            tension_lo,
            tension_hi,
            "geringe_feldspannung",
            "mittlere_feldspannung",
            "hohe_feldspannung",
        )
        row["mischlinien_signature"] = "|".join(
            [
                f"{tone}+{shift}",
                visual,
                movement,
                f"{intake}+{tension}",
            ]
        )


def build_report() -> None:
    base_nodes = _read_csv(BASE_NODES)
    old_signatures = {row["signature"]: row for row in base_nodes}
    strong_old = {
        row["signature"]: row
        for row in base_nodes
        if row.get("node_state") in {"tragende_bedeutungsnaehe", "verdichtete_bedeutungsnaehe"}
    }

    windows: list[dict[str, object]] = []
    for world, path in EPISODE_FILES.items():
        if path.exists():
            windows.extend(_window_rows(path, world))
    if not windows:
        raise RuntimeError("no follow-world windows found")
    _attach_signatures(windows)

    out_rows: list[dict[str, object]] = []
    for row in windows:
        signature = str(row["mischlinien_signature"])
        exact = old_signatures.get(signature)
        best_signature = ""
        best_node = ""
        best_state = ""
        best_similarity = 0.0
        for old_signature, old in old_signatures.items():
            similarity = _signature_similarity(signature, old_signature)
            if similarity > best_similarity:
                best_similarity = similarity
                best_signature = old_signature
                best_node = old.get("meaning_node", "")
                best_state = old.get("node_state", "")
        if exact:
            follow_state = "starker_knoten_taucht_wieder_auf" if signature in strong_old else "bekannter_knoten_taucht_wieder_auf"
        elif best_similarity >= 0.60:
            follow_state = "neue_nachbarschaft_zu_altem_knoten"
        else:
            follow_state = "neue_bedeutungsinsel"
        out_rows.append(
            {
                **PASSIVE_FLAGS,
                **row,
                "follow_state": follow_state,
                "exact_old_node": exact.get("meaning_node", "") if exact else "",
                "exact_old_state": exact.get("node_state", "") if exact else "",
                "nearest_old_node": best_node,
                "nearest_old_state": best_state,
                "nearest_similarity": round(best_similarity, 6),
                "nearest_old_signature": best_signature,
            }
        )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    state_counts = Counter(str(row["follow_state"]) for row in out_rows)
    world_states: dict[str, Counter[str]] = defaultdict(Counter)
    exact_nodes = Counter(str(row["exact_old_node"]) for row in out_rows if row.get("exact_old_node"))
    near_nodes = Counter(str(row["nearest_old_node"]) for row in out_rows if row.get("nearest_old_node"))
    signature_counter = Counter(str(row["mischlinien_signature"]) for row in out_rows)
    for row in out_rows:
        world_states[str(row["world"])][str(row["follow_state"])] += 1

    split_candidates = []
    by_nearest: dict[str, set[str]] = defaultdict(set)
    for row in out_rows:
        if float(row["nearest_similarity"]) >= 0.60 and not row.get("exact_old_node"):
            by_nearest[str(row["nearest_old_node"])].add(str(row["mischlinien_signature"]))
    for node, signatures in sorted(by_nearest.items(), key=lambda item: len(item[1]), reverse=True):
        if len(signatures) >= 2:
            split_candidates.append((node, len(signatures)))

    top_world_lines = [
        f"- `{world}`: " + " | ".join(f"{key}:{value}" for key, value in counter.most_common())
        for world, counter in sorted(world_states.items())
    ]
    top_signature_lines = [
        f"- `{signature}`: `{count}`"
        for signature, count in signature_counter.most_common(8)
    ]
    split_lines = [
        f"- `{node}`: `{count}` neue Nachbarschaftssignaturen"
        for node, count in split_candidates[:8]
    ] or ["- keine deutliche Teilung im aktuellen Folgewelt-Set"]
    exact_node_lines = [
        f"- `{node}`: `{count}`" for node, count in exact_nodes.most_common(8)
    ] or ["- keine exakte Wiederkehr"]

    lines = [
        "# 1390 - Bedeutungsnetz ueber Folgewelten",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft das in `1389` gebildete Bedeutungsnetz gegen neue passive Folgewelten.",
        "",
        "Geprueft wird:",
        "",
        "```text",
        "Tauchen starke Knoten wieder auf, teilen sie sich, oder entstehen neue Nachbarschaften?",
        "```",
        "",
        "Die Diagnose bleibt passiv. Keine Handlung, keine Richtung, keine Strategie.",
        "",
        "## Befund",
        "",
        f"- alte Bedeutungsnetz-Knoten: `{len(base_nodes)}`",
        f"- starke alte Knoten: `{len(strong_old)}`",
        f"- neue Fenster: `{len(out_rows)}`",
        f"- Folgezustaende: `{', '.join(f'{k}:{v}' for k, v in state_counts.most_common())}`",
        f"- exakt wiedergefundene alte Knoten: `{len(exact_nodes)}`",
        f"- alte Knoten mit Nachbarschaft: `{len(near_nodes)}`",
        "",
        "## Nach Welten",
        "",
        *top_world_lines,
        "",
        "## Wiedergefundene alte Knoten",
        "",
        *exact_node_lines,
        "",
        "## Moegliche Teilung / Erweiterung",
        "",
        *split_lines,
        "",
        "## Dominante neue Signaturen",
        "",
        *top_signature_lines,
        "",
        "## Lesung",
        "",
        "Die Folgewelten bestaetigen nicht einfach eine feste Symboltabelle.",
        "Sie zeigen, ob eine vorhandene Bedeutungsnaehe als Knoten wiederkehrt oder ob sie in neue Nachbarschaften ausweicht.",
        "",
        "Exakte Wiederkehr spricht fuer stabile Feldnaehe.",
        "Nachbarschaft ohne Exakttreffer spricht fuer Erweiterung oder Teilung.",
        "Neue Inseln sprechen fuer neue Weltspannung, die noch nicht in der alten Karte enthalten war.",
        "",
        "## Grenze",
        "",
        "Die Folgewelt-Signatur nutzt eine relative Fensterklassifikation aus `episodes.csv`.",
        "Sie ist eine passive Vergleichsschicht, kein neues Lexikon und keine Handlungslogik.",
        "",
        "## Wie es weitergeht",
        "",
        "Als naechstes sollten die Nachbarschaftsknoten isoliert werden. Entscheidend ist, ob sie bei weiteren Welten stabil neben demselben alten Knoten bleiben oder in eigenstaendige Knotenfamilien auseinanderdriften.",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build_report()
