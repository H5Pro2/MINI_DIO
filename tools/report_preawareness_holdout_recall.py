from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean


ASSETS = ("BTC", "SOL", "DOGE", "PAXG", "XRP", "KAS")


def _load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists() or path.stat().st_size <= 0:
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _asset_from_text(value: str) -> str:
    text = str(value or "").upper()
    for asset in ASSETS:
        if asset in text:
            return asset
    return "UNK"


def _parse_counter_text(value: str) -> Counter[str]:
    counter: Counter[str] = Counter()
    for raw_part in str(value or "").split(";"):
        part = raw_part.strip()
        if not part or ":" not in part:
            continue
        key, raw_count = part.rsplit(":", 1)
        try:
            count = int(float(raw_count))
        except Exception:
            count = 0
        if key.strip():
            counter[key.strip()] += count
    return counter


def _dominant(counter: Counter[str]) -> tuple[str, float]:
    if not counter:
        return "-", 0.0
    key, count = counter.most_common(1)[0]
    return key, count / max(1, sum(counter.values()))


def _raw_window_stats(rows: list[dict[str, str]]) -> dict[str, float | str]:
    if not rows:
        return {
            "raw_net_pct": 0.0,
            "raw_range_pct": 0.0,
            "raw_avg_body_pct": 0.0,
            "raw_direction_changes": 0.0,
            "raw_direction": "offen",
        }
    opens = [_safe_float(row.get("open")) for row in rows]
    highs = [_safe_float(row.get("high")) for row in rows]
    lows = [_safe_float(row.get("low")) for row in rows]
    closes = [_safe_float(row.get("close")) for row in rows]
    base = opens[0] or closes[0] or 1.0
    signs: list[int] = []
    for open_, close in zip(opens, closes):
        diff = close - open_
        if diff > 0:
            signs.append(1)
        elif diff < 0:
            signs.append(-1)
    changes = sum(1 for left, right in zip(signs, signs[1:]) if left != right)
    net_pct = ((closes[-1] - opens[0]) / base) * 100.0 if base else 0.0
    range_pct = ((max(highs) - min(lows)) / base) * 100.0 if base else 0.0
    avg_body_pct = mean(abs(close - open_) / base * 100.0 for open_, close in zip(opens, closes)) if base else 0.0
    if net_pct > 0.18:
        direction = "steigend"
    elif net_pct < -0.18:
        direction = "fallend"
    else:
        direction = "seitwaerts"
    return {
        "raw_net_pct": net_pct,
        "raw_range_pct": range_pct,
        "raw_avg_body_pct": avg_body_pct,
        "raw_direction_changes": float(changes),
        "raw_direction": direction,
    }


def _raw_motion_class(row: dict[str, object]) -> str:
    direction = str(row.get("raw_direction") or "offen")
    range_pct = _safe_float(row.get("raw_range_pct"))
    changes = _safe_float(row.get("raw_direction_changes"))
    body = _safe_float(row.get("raw_avg_body_pct"))
    if range_pct >= 4.0 and changes >= 20:
        return f"weite_unruhige_vorphase_{direction}"
    if range_pct >= 4.0:
        return f"weite_gerichtete_vorphase_{direction}"
    if changes >= 20:
        return f"enge_unruhige_vorphase_{direction}"
    if body <= 0.035:
        return f"feine_ruhevorphase_{direction}"
    return f"mittlere_vorphase_{direction}"


def _sensory_class(row: dict[str, object]) -> str:
    visual_stability = _safe_float(row.get("sehen_form_stability"))
    visual_change = _safe_float(row.get("sehen_form_change"))
    tone = _safe_float(row.get("hoeren_energy_tone"))
    shift = abs(_safe_float(row.get("hoeren_energy_shift")))
    loudness = _safe_float(row.get("perception_auditory_loudness"))

    if tone >= 0.45 and shift >= 0.45:
        hearing = "hoch_schwingend"
    elif tone >= 0.45:
        hearing = "hell_getragen"
    elif shift >= 0.35:
        hearing = "wechselnd"
    else:
        hearing = "gedaempft"

    if visual_stability >= max(0.25, abs(visual_change)):
        visual = "sicht_stabil"
    elif visual_change <= -0.25:
        visual = "sicht_zerfaellt"
    elif abs(visual_change) >= 0.25:
        visual = "sicht_wechselt"
    else:
        visual = "sicht_offen"

    if loudness >= 0.55:
        level = "laut"
    elif loudness <= 0.25:
        level = "leise"
    else:
        level = "mittel"
    return f"{visual}_{hearing}_{level}"


def _field_contact_class(row: dict[str, object]) -> str:
    carry = _safe_float(row.get("mcm_carry_quality"))
    strain = _safe_float(row.get("mcm_strain_quality"))
    rekopplung = _safe_float(row.get("mcm_rekopplung_quality"))
    if rekopplung >= 0.62 and carry >= 0.40 and strain <= 0.24:
        return "tragende_rekopplung"
    if rekopplung >= 0.58 and strain <= 0.28:
        return "offene_rekopplung"
    if strain >= 0.28 and rekopplung <= 0.59:
        return "spannungsnahe_oeffnung"
    if carry >= 0.40:
        return "getragen_offen"
    return "offener_feldkontakt"


def _load_preawareness_roles(path: Path) -> dict[tuple[str, str, str], dict[str, str]]:
    rows = _load_csv(path)
    roles: dict[tuple[str, str, str], dict[str, str]] = {}
    for row in rows:
        roles[(row.get("lookback", "-"), row.get("target_group", "-"), row.get("chain", "-"))] = row
    return roles


def _load_symbol_targets(path: Path) -> dict[str, list[dict[str, str]]]:
    targets: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in _load_csv(path):
        symbol_counts = _parse_counter_text(row.get("symbols", ""))
        for symbol, count in symbol_counts.items():
            targets[symbol].append(
                {
                    "symbol": symbol,
                    "source_target_group": row.get("target_group", "-"),
                    "source_chain": row.get("chain", "-"),
                    "source_asset": row.get("asset", "-"),
                    "source_lookback": row.get("lookback", "-"),
                    "source_symbol_count": str(count),
                    "expected_field_contact_class": row.get("dominant_field_contact_class", "-"),
                    "expected_sensory_class": row.get("dominant_sensory_class", "-"),
                    "expected_motion_class": row.get("dominant_motion_class", "-"),
                }
            )
    return targets


def _episode_paths(debug_root: Path) -> list[Path]:
    return sorted(path for path in debug_root.glob("dio_mini_lauf_*/episodes.csv") if path.exists())


def _data_path_for_episode(episodes_path: Path) -> Path:
    report_path = episodes_path.parent / "mini_report.json"
    report = json.loads(report_path.read_text(encoding="utf-8"))
    data_path = Path(str(report["data_path"]))
    if not data_path.is_absolute():
        data_path = Path.cwd() / data_path
    return data_path


def _event_from_episode(
    *,
    holdout_label: str,
    episodes_path: Path,
    episode_row: dict[str, str],
    raw_rows: list[dict[str, str]],
    target: dict[str, str],
    lookback: int,
) -> dict[str, object]:
    tick = int(_safe_float(episode_row.get("tick")))
    start = max(0, tick - lookback - 1)
    end = max(start, tick - 1)
    raw_stats = _raw_window_stats(raw_rows[start:end])
    event: dict[str, object] = {
        "holdout_label": holdout_label,
        "holdout_asset": _asset_from_text(holdout_label),
        "run": str(episodes_path.parent),
        "tick": tick,
        "preview_symbol": target["symbol"],
        "lookback": target["source_lookback"],
        "target_group": target["source_target_group"],
        "source_chain": target["source_chain"],
        "source_asset": target["source_asset"],
        "expected_field_contact_class": target["expected_field_contact_class"],
        "expected_sensory_class": target["expected_sensory_class"],
        "expected_motion_class": target["expected_motion_class"],
        "raw_direction": raw_stats["raw_direction"],
        "raw_net_pct": raw_stats["raw_net_pct"],
        "raw_range_pct": raw_stats["raw_range_pct"],
        "raw_avg_body_pct": raw_stats["raw_avg_body_pct"],
        "raw_direction_changes": raw_stats["raw_direction_changes"],
        "sehen_form_stability": _safe_float(episode_row.get("sehen_form_stability")),
        "sehen_form_change": _safe_float(episode_row.get("sehen_form_change")),
        "hoeren_energy_tone": _safe_float(episode_row.get("hoeren_energy_tone")),
        "hoeren_energy_shift": _safe_float(episode_row.get("hoeren_energy_shift")),
        "perception_auditory_loudness": _safe_float(episode_row.get("perception_auditory_loudness")),
        "mcm_carry_quality": _safe_float(episode_row.get("mcm_carry_quality")),
        "mcm_strain_quality": _safe_float(episode_row.get("mcm_strain_quality")),
        "mcm_rekopplung_quality": _safe_float(episode_row.get("mcm_rekopplung_quality")),
    }
    event["observed_motion_class"] = _raw_motion_class(event)
    event["observed_sensory_class"] = _sensory_class(event)
    event["observed_field_contact_class"] = _field_contact_class(event)
    event["field_recalled"] = int(event["observed_field_contact_class"] == event["expected_field_contact_class"])
    event["sensory_recalled"] = int(event["observed_sensory_class"] == event["expected_sensory_class"])
    event["motion_recalled"] = int(event["observed_motion_class"] == event["expected_motion_class"])
    return event


def _collect_events(
    *,
    holdouts: dict[str, Path],
    symbol_targets: dict[str, list[dict[str, str]]],
    max_events_per_symbol_holdout: int,
) -> list[dict[str, object]]:
    events: list[dict[str, object]] = []
    wanted = set(symbol_targets)
    for label, root in holdouts.items():
        seen: Counter[str] = Counter()
        for episodes_path in _episode_paths(root):
            raw_rows = _load_csv(_data_path_for_episode(episodes_path))
            for episode_row in _load_csv(episodes_path):
                symbol = episode_row.get("mcm_field_episode_preview_symbol", "")
                if symbol not in wanted:
                    continue
                if seen[symbol] >= max_events_per_symbol_holdout:
                    continue
                seen[symbol] += 1
                for target in symbol_targets[symbol]:
                    events.append(
                        _event_from_episode(
                            holdout_label=label,
                            episodes_path=episodes_path,
                            episode_row=episode_row,
                            raw_rows=raw_rows,
                            target=target,
                            lookback=int(float(target.get("source_lookback", "lb48").replace("lb", "") or 48)),
                        )
                    )
    return events


def _build_summary(events: list[dict[str, object]]) -> list[dict[str, object]]:
    groups: dict[tuple[str, str, str], list[dict[str, object]]] = defaultdict(list)
    for event in events:
        groups[(str(event["target_group"]), str(event["source_chain"]), str(event["holdout_label"]))].append(event)
    rows: list[dict[str, object]] = []
    for (target_group, source_chain, holdout_label), items in sorted(groups.items()):
        field = Counter(str(item["observed_field_contact_class"]) for item in items)
        sensory = Counter(str(item["observed_sensory_class"]) for item in items)
        motion = Counter(str(item["observed_motion_class"]) for item in items)
        expected_field = Counter(str(item["expected_field_contact_class"]) for item in items)
        dom_field, dom_field_share = _dominant(field)
        dom_expected, dom_expected_share = _dominant(expected_field)
        rows.append(
            {
                "target_group": target_group,
                "source_chain": source_chain,
                "holdout_label": holdout_label,
                "holdout_asset": _asset_from_text(holdout_label),
                "events": len(items),
                "symbols": ";".join(f"{key}:{value}" for key, value in Counter(str(item["preview_symbol"]) for item in items).most_common()),
                "expected_field_contact_class": dom_expected,
                "expected_field_share": dom_expected_share,
                "observed_field_contact_class": dom_field,
                "observed_field_share": dom_field_share,
                "field_recall_share": _avg([float(item["field_recalled"]) for item in items]),
                "sensory_recall_share": _avg([float(item["sensory_recalled"]) for item in items]),
                "motion_recall_share": _avg([float(item["motion_recalled"]) for item in items]),
                "observed_sensory_classes": ";".join(f"{key}:{value}" for key, value in sensory.most_common(6)),
                "observed_motion_classes": ";".join(f"{key}:{value}" for key, value in motion.most_common(6)),
                "avg_carry": _avg([_safe_float(item["mcm_carry_quality"]) for item in items]),
                "avg_strain": _avg([_safe_float(item["mcm_strain_quality"]) for item in items]),
                "avg_rekopplung": _avg([_safe_float(item["mcm_rekopplung_quality"]) for item in items]),
            }
        )
    return rows


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = list(rows[0].keys()) if rows else ["target_group"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(path: Path, summary: list[dict[str, object]], events: list[dict[str, object]], holdouts: dict[str, Path]) -> None:
    recall = _avg([float(row["field_recall_share"]) for row in summary]) if summary else 0.0
    sensory = _avg([float(row["sensory_recall_share"]) for row in summary]) if summary else 0.0
    motion = _avg([float(row["motion_recall_share"]) for row in summary]) if summary else 0.0
    lines = [
        "# 2041 - Vorwahrnehmungs-Memory Holdout-Rückprüfung",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prüft die passive Vorwahrnehmungs-Memory aus `2040` gegen andere reale Weltfenster.",
        "",
        "Geprüft wird nicht, ob eine Handlung entsteht. Geprüft wird nur, ob bekannte Feldkontaktrollen in fremden Welten wieder auftauchen, driften oder neue Oberflächen tragen.",
        "",
        "## Holdout-Welten",
        "",
    ]
    for label, root in holdouts.items():
        lines.append(f"- `{label}`: `{root}`")
    lines.extend(
        [
            "",
            "## Übersicht",
            "",
            f"- Ereignisse: `{len(events)}`",
            f"- Gruppen: `{len(summary)}`",
            f"- mittlere Feldkontakt-Rückerkennung: `{recall:.3f}`",
            f"- mittlere Sinnesphasen-Rückerkennung: `{sensory:.3f}`",
            f"- mittlere Rohphasen-Rückerkennung: `{motion:.3f}`",
            "",
            "## Gruppenergebnis",
            "",
            "| Gruppe | Quelle | Holdout | Ereignisse | erwartet | beobachtet | Feld | Sinn | Roh | MCM |",
            "|---|---|---|---:|---|---|---:|---:|---:|---:|",
        ]
    )
    for row in summary:
        lines.append(
            "| "
            f"`{row['target_group']}` | "
            f"`{row['source_chain']}` | "
            f"`{row['holdout_label']}` | "
            f"{row['events']} | "
            f"`{row['expected_field_contact_class']}` | "
            f"`{row['observed_field_contact_class']}` ({float(row['observed_field_share']):.2f}) | "
            f"{float(row['field_recall_share']):.3f} | "
            f"{float(row['sensory_recall_share']):.3f} | "
            f"{float(row['motion_recall_share']):.3f} | "
            f"{float(row['avg_carry']):.3f}/{float(row['avg_strain']):.3f}/{float(row['avg_rekopplung']):.3f} |"
        )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Die Rückprüfung trennt klar zwischen Feldrolle und Oberfläche.",
            "",
            "Wenn die Feldkontakt-Rückerkennung höher bleibt als Sinnes- oder Rohphasen-Rückerkennung, spricht das dafür, dass die Vorwahrnehmungs-Memory keine bloße Kopie der Außenwelt speichert, sondern eine wiederkehrende MCM-Feldnähe.",
            "",
            "Wenn sie fällt, ist das kein Fehler: Dann zeigt der Holdout, dass die Rolle an diese neue Weltspannung nicht stabil anschließt oder sich anders organisieren muss.",
            "",
            "## Grenze",
            "",
            "Auch diese Rückprüfung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung, kein Gate und keine Entry-Mechanik.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte geprüft werden, welche Rollen trotz anderer Oberfläche feldnah wiederkehren. Daraus kann eine robuste Vorwahrnehmungs-Landkarte entstehen, ohne dass MINI_DIO hart programmiert wird.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _parse_holdouts(raw_values: list[str]) -> dict[str, Path]:
    holdouts: dict[str, Path] = {}
    for raw in raw_values:
        if "=" not in raw:
            raise SystemExit(f"Ungültiges Holdout-Format: {raw}")
        label, path = raw.split("=", 1)
        holdouts[label.strip()] = Path(path.strip())
    return holdouts


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-summary", default="docs/befunde/2039_FELDFUNKTIONSWECHSEL_VORPHASEN_ASSET_STABILITAET.summary.csv")
    parser.add_argument("--preawareness", default="docs/befunde/2040_FELDKONTAKT_VORWAHRNEHMUNG_MEMORY.roles.csv")
    parser.add_argument("--holdout", action="append", default=[
        "btc2024=debug/1996_ff_btc_2024_10k",
        "doge2024=debug/1996_ff_doge_2024_10k",
        "paxg2024=debug/1996_ff_paxg_2024_10k",
    ])
    parser.add_argument("--max-events-per-symbol-holdout", type=int, default=60)
    parser.add_argument("--out-prefix", default="2041_VORWAHRNEHMUNG_MEMORY_HOLDOUT_RUECKPRUEFUNG")
    args = parser.parse_args()

    holdouts = _parse_holdouts(args.holdout)
    symbol_targets = _load_symbol_targets(Path(args.source_summary))
    events = _collect_events(
        holdouts=holdouts,
        symbol_targets=symbol_targets,
        max_events_per_symbol_holdout=args.max_events_per_symbol_holdout,
    )
    summary = _build_summary(events)
    # Load roles to fail early if the expected preawareness artifact is missing.
    _load_preawareness_roles(Path(args.preawareness))

    out_dir = Path("docs") / "befunde"
    _write_csv(out_dir / f"{args.out_prefix}.events.csv", events)
    _write_csv(out_dir / f"{args.out_prefix}.summary.csv", summary)
    _write_markdown(out_dir / f"{args.out_prefix}.md", summary, events, holdouts)
    print(f"events={len(events)}")
    print(f"summary_rows={len(summary)}")
    print(f"wrote={out_dir / (args.out_prefix + '.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
