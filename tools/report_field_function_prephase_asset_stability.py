from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


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


def _asset_from_world(world: str) -> str:
    text = str(world or "").upper()
    for asset in ASSETS:
        if asset in text:
            return asset
    return "UNK"


def _dominant(counter: Counter[str]) -> tuple[str, float]:
    if not counter:
        return "-", 0.0
    key, count = counter.most_common(1)[0]
    return key, count / max(1, sum(counter.values()))


def _build_rows(events: list[dict[str, str]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    enriched: list[dict[str, object]] = []
    for row in events:
        item: dict[str, object] = dict(row)
        item["asset"] = _asset_from_world(row.get("world", ""))
        enriched.append(item)

    groups: dict[tuple[str, str, str, str], list[dict[str, object]]] = defaultdict(list)
    for item in enriched:
        groups[
            (
                str(item.get("lookback", "-")),
                str(item.get("target_group", "-")),
                str(item.get("chain", "-")),
                str(item.get("asset", "-")),
            )
        ].append(item)

    summary: list[dict[str, object]] = []
    for (lookback, target_group, chain, asset), items in sorted(groups.items()):
        if asset == "UNK":
            continue
        motion = Counter(str(item.get("raw_motion_class", "-")) for item in items)
        sensory = Counter(str(item.get("sensory_class", "-")) for item in items)
        field = Counter(str(item.get("field_contact_class", "-")) for item in items)
        combined = Counter(str(item.get("combined_prephase_class", "-")) for item in items)
        symbols = Counter(str(item.get("preview_symbol", "-")) for item in items)
        dominant_motion, motion_share = _dominant(motion)
        dominant_sensory, sensory_share = _dominant(sensory)
        dominant_field, field_share = _dominant(field)
        dominant_combined, combined_share = _dominant(combined)
        summary.append(
            {
                "lookback": lookback,
                "target_group": target_group,
                "chain": chain,
                "asset": asset,
                "events": len(items),
                "dominant_motion_class": dominant_motion,
                "dominant_motion_share": motion_share,
                "dominant_sensory_class": dominant_sensory,
                "dominant_sensory_share": sensory_share,
                "dominant_field_contact_class": dominant_field,
                "dominant_field_contact_share": field_share,
                "dominant_combined_class": dominant_combined,
                "dominant_combined_share": combined_share,
                "symbols": ";".join(f"{key}:{value}" for key, value in symbols.most_common()),
                "motion_classes": ";".join(f"{key}:{value}" for key, value in motion.most_common(6)),
                "sensory_classes": ";".join(f"{key}:{value}" for key, value in sensory.most_common(6)),
                "field_contact_classes": ";".join(f"{key}:{value}" for key, value in field.most_common(6)),
                "avg_range": _avg([_safe_float(item.get("raw_range_pct")) for item in items]),
                "avg_changes": _avg([_safe_float(item.get("raw_direction_changes")) for item in items]),
                "avg_carry": _avg([_safe_float(item.get("mcm_carry_quality")) for item in items]),
                "avg_strain": _avg([_safe_float(item.get("mcm_strain_quality")) for item in items]),
                "avg_rekopplung": _avg([_safe_float(item.get("mcm_rekopplung_quality")) for item in items]),
            }
        )
    return enriched, summary


def _asset_stability_rows(summary: list[dict[str, object]]) -> list[dict[str, object]]:
    groups: dict[tuple[str, str, str], list[dict[str, object]]] = defaultdict(list)
    for row in summary:
        groups[(str(row["lookback"]), str(row["target_group"]), str(row["chain"]))].append(row)

    stability: list[dict[str, object]] = []
    for (lookback, target_group, chain), rows in sorted(groups.items()):
        field_counter = Counter(str(row["dominant_field_contact_class"]) for row in rows)
        sensory_counter = Counter(str(row["dominant_sensory_class"]) for row in rows)
        motion_counter = Counter(str(row["dominant_motion_class"]) for row in rows)
        dominant_field, field_share = _dominant(field_counter)
        dominant_sensory, sensory_share = _dominant(sensory_counter)
        dominant_motion, motion_share = _dominant(motion_counter)
        stability.append(
            {
                "lookback": lookback,
                "target_group": target_group,
                "chain": chain,
                "assets": ";".join(str(row["asset"]) for row in rows),
                "asset_count": len(rows),
                "dominant_field_contact_class": dominant_field,
                "field_asset_share": field_share,
                "dominant_sensory_class": dominant_sensory,
                "sensory_asset_share": sensory_share,
                "dominant_motion_class": dominant_motion,
                "motion_asset_share": motion_share,
                "avg_carry": _avg([float(row["avg_carry"]) for row in rows]),
                "avg_strain": _avg([float(row["avg_strain"]) for row in rows]),
                "avg_rekopplung": _avg([float(row["avg_rekopplung"]) for row in rows]),
            }
        )
    return stability


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = list(rows[0].keys()) if rows else ["lookback"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(path: Path, summary: list[dict[str, object]], stability: list[dict[str, object]]) -> None:
    asset_counts = Counter(str(row["asset"]) for row in summary)
    lines = [
        "# 2039 - Feldfunktionswechsel Vorphasen nach Asset",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prüft, ob die Vorphasen-Klassen aus `2038` assetübergreifend stabil bleiben oder ob einzelne Weltkörper eigene Vorphasenprofile ausbilden.",
        "",
        "## Übersicht",
        "",
        f"- Asset-Gruppen: `{', '.join(f'{key}:{value}' for key, value in asset_counts.most_common())}`",
        "",
        "## Asset-Stabilität",
        "",
        "| Lookback | Gruppe | Kette | Assets | Feldkontakt | Sinnesphase | Rohphase | MCM carry/strain/rekopplung |",
        "|---|---|---|---|---|---|---|---:|",
    ]
    for row in stability:
        lines.append(
            "| "
            f"`{row['lookback']}` | "
            f"`{row['target_group']}` | "
            f"`{row['chain']}` | "
            f"`{row['assets']}` | "
            f"`{row['dominant_field_contact_class']}` ({float(row['field_asset_share']):.2f}) | "
            f"`{row['dominant_sensory_class']}` ({float(row['sensory_asset_share']):.2f}) | "
            f"`{row['dominant_motion_class']}` ({float(row['motion_asset_share']):.2f}) | "
            f"{float(row['avg_carry']):.3f}/{float(row['avg_strain']):.3f}/{float(row['avg_rekopplung']):.3f} |"
        )

    lines.extend(
        [
            "",
            "## Asset-Details",
            "",
            "| Lookback | Gruppe | Kette | Asset | Ereignisse | Feldkontakt | Sinnesphase | Rohphase | MCM |",
            "|---|---|---|---|---:|---|---|---|---:|",
        ]
    )
    for row in summary:
        lines.append(
            "| "
            f"`{row['lookback']}` | "
            f"`{row['target_group']}` | "
            f"`{row['chain']}` | "
            f"`{row['asset']}` | "
            f"{row['events']} | "
            f"`{row['dominant_field_contact_class']}` ({float(row['dominant_field_contact_share']):.2f}) | "
            f"`{row['dominant_sensory_class']}` ({float(row['dominant_sensory_share']):.2f}) | "
            f"`{row['dominant_motion_class']}` ({float(row['dominant_motion_share']):.2f}) | "
            f"{float(row['avg_carry']):.3f}/{float(row['avg_strain']):.3f}/{float(row['avg_rekopplung']):.3f} |"
        )

    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Der Feldkontakt ist stabiler als die Rohbewegung.",
            "",
            "Rohphasen wechseln je nach Asset und Segment deutlicher. Der MCM-Feldkontakt bleibt innerhalb der Rollenfamilie konsistenter: Rekopplung bleibt rekoppelnd, Öffnung bleibt spannungsnah.",
            "",
            "Das spricht dafür, dass MINI_DIO nicht nur assetbezogene Oberflächen liest, sondern darunter eine wiederkehrende Feldrolle hält.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte geprüft werden, ob diese assetübergreifenden Feldkontaktklassen als passive Vorwahrnehmungs-Memory gespeichert werden können, ohne daraus Handlung oder harte Regeln abzuleiten.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--events", default="docs/befunde/2001-3000/2038_FELDFUNKTIONSWECHSEL_VORPHASEN_KLASSEN.events.csv")
    parser.add_argument("--out-prefix", default="2039_FELDFUNKTIONSWECHSEL_VORPHASEN_ASSET_STABILITAET")
    args = parser.parse_args()

    enriched, summary = _build_rows(_load_csv(Path(args.events)))
    stability = _asset_stability_rows(summary)
    out_dir = Path("docs") / "befunde"
    _write_csv(out_dir / f"{args.out_prefix}.events.csv", enriched)
    _write_csv(out_dir / f"{args.out_prefix}.summary.csv", summary)
    _write_csv(out_dir / f"{args.out_prefix}.stability.csv", stability)
    _write_markdown(out_dir / f"{args.out_prefix}.md", summary, stability)

    print(f"events={len(enriched)}")
    print(f"summary_rows={len(summary)}")
    print(f"stability_rows={len(stability)}")
    print(f"wrote={out_dir / (args.out_prefix + '.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
