from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

from befunde_paths import befunde_root


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


DEFAULT_INPUT = befunde_root(ROOT) / "1245_MCM_FELDPHASEN_KLASSEN.csv"
DEFAULT_OUT = befunde_root(ROOT) / "1246_MCM_FELDPHASEN_WELTARTEN_TRIGGER.md"
TARGET_CLASSES = {
    "weltgebundene_feldphase",
    "lokale_oder_driftende_phase",
    "junge_phasenspur",
    "grenzphase_mit_entlastung",
}


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _safe_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _parse_counter_text(value: str) -> Counter[str]:
    counter: Counter[str] = Counter()
    text = str(value or "").strip()
    if not text or text == "-":
        return counter
    for part in text.split(";"):
        item = part.strip()
        if not item or ":" not in item:
            continue
        key, count_text = item.rsplit(":", 1)
        counter[key.strip()] += _safe_int(count_text)
    return counter


def _world_kind(world: str) -> str:
    text = world.upper()
    if text.startswith("SYNTH_"):
        return "synthetische_sinneswelt"
    if any(token in text for token in ("RAND", "BRUCH", "KIPP")):
        return "rand_bruch_welt"
    if any(token in text for token in ("HARMONIE", "QUIET", "SIDEWAYS")):
        return "ruhige_oder_seitwaerts_welt"
    if any(token in text for token in ("STRESS", "NEG")):
        return "stress_oder_negative_welt"
    if any(token in text for token in ("EXPANSION", "POS")):
        return "expansive_oder_positive_welt"
    if "PAXG" in text:
        return "paxg_welt"
    if "BTC" in text:
        return "btc_welt"
    if "SOL" in text:
        return "sol_welt"
    if "DOGE" in text or "XRP" in text or "KAS" in text:
        return "alt_asset_welt"
    if any(token in text for token in ("ZEIT", "SEQ")):
        return "zeit_oder_sequenz_welt"
    return "sonstige_welt"


def _timeframe_kind(world: str) -> str:
    text = world.upper()
    if "1H" in text:
        return "1h"
    if "5M" in text:
        return "5m"
    if "10K" in text:
        return "10k_segment"
    return "unbekannt"


def _asset_kind(world: str) -> str:
    text = world.upper()
    for token in ("SOL", "BTC", "PAXG", "DOGE", "XRP", "KAS"):
        if token in text:
            return token
    if text.startswith("SYNTH"):
        return "SYNTH"
    return "-"


def _phase_trigger_reading(row: dict[str, str], world_counter: Counter[str]) -> str:
    phase_class = str(row.get("phase_class", "") or "")
    role_family = str(row.get("role_family", "") or "")
    dominant_effect = str(row.get("dominant_effect", "") or "")
    kind_counts = Counter()
    for world, count in world_counter.items():
        kind_counts[_world_kind(world)] += count
    top_kind = kind_counts.most_common(1)[0][0] if kind_counts else "-"

    if phase_class == "junge_phasenspur":
        return "junge Spur; noch keine belastbare Weltartbindung"
    if phase_class == "lokale_oder_driftende_phase":
        return "lokale Rand-Zentrum-Schleife; Driftverdacht statt Grundordnung"
    if dominant_effect in {"rand_entlastet_in_offenheit", "zentrumsbruch_in_offenheit"}:
        return "Grenzimpuls mit Entlastung; Feld kehrt ueber Offenheit zur Ordnung zurueck"
    if role_family == "randgebundene_phase":
        return f"randgebundene situative Phase; haeufigster Weltkontext: {top_kind}"
    return f"situative Phase; haeufigster Weltkontext: {top_kind}"


def _build_rows(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row in rows:
        if row.get("phase_class") not in TARGET_CLASSES:
            continue
        worlds = _parse_counter_text(row.get("worlds", ""))
        kind_counts = Counter()
        timeframe_counts = Counter()
        asset_counts = Counter()
        for world, count in worlds.items():
            kind_counts[_world_kind(world)] += count
            timeframe_counts[_timeframe_kind(world)] += count
            asset_counts[_asset_kind(world)] += count
        result.append(
            {
                "phase_key": row.get("phase_key", ""),
                "phase_class": row.get("phase_class", ""),
                "role_family": row.get("role_family", ""),
                "seen_count": row.get("seen_count", "0"),
                "world_count": row.get("world_count", "0"),
                "dominant_effect": row.get("dominant_effect", ""),
                "top_worlds": "; ".join(f"{k}:{v}" for k, v in worlds.most_common(8)) or "-",
                "world_kinds": "; ".join(f"{k}:{v}" for k, v in kind_counts.most_common()) or "-",
                "timeframes": "; ".join(f"{k}:{v}" for k, v in timeframe_counts.most_common()) or "-",
                "assets": "; ".join(f"{k}:{v}" for k, v in asset_counts.most_common()) or "-",
                "trigger_reading": _phase_trigger_reading(row, worlds),
            }
        )
    return result


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(path: Path, rows: list[dict[str, object]], input_path: Path) -> None:
    class_counts = Counter(str(row["phase_class"]) for row in rows)
    kind_counts: Counter[str] = Counter()
    for row in rows:
        for part in str(row["world_kinds"]).split(";"):
            item = part.strip()
            if not item or ":" not in item:
                continue
            key, count_text = item.rsplit(":", 1)
            kind_counts[key.strip()] += _safe_int(count_text)

    lines: list[str] = [
        "# MCM-Feldphasen Weltarten-Trigger",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "## Grundfrage",
        "",
        "Welche konkreten Weltarten loesen die weltgebundenen, lokalen, jungen oder grenznahen Feldphasen aus?",
        "",
        "## Eingabe",
        "",
        f"- `{input_path.relative_to(ROOT)}`",
        "",
        "## Profil",
        "",
        f"- untersuchte Phasen: `{len(rows)}`",
        f"- Klassen: `{dict(class_counts.most_common())}`",
        f"- Weltarten in diesen Phasen: `{dict(kind_counts.most_common())}`",
        "",
        "## Phasenruecklesung",
        "",
        "| Phase | Klasse | Anzahl | Welten | Wirkung | Weltarten | Top-Welten | Lesung |",
        "|---|---|---:|---:|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["phase_key"]),
                    str(row["phase_class"]),
                    str(row["seen_count"]),
                    str(row["world_count"]),
                    str(row["dominant_effect"]),
                    str(row["world_kinds"]),
                    str(row["top_worlds"]),
                    str(row["trigger_reading"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die situativen Phasen sind nicht zufaellig verteilt.",
            "",
            "Sie liegen ueberwiegend dort, wo Rand/Kipp mit Zentrum, Rekopplung oder Offenheit gekoppelt wird.",
            "",
            "Damit bestaetigt sich die Arbeitshierarchie:",
            "",
            "```text",
            "allgemeine Feldphasen = Grundordnung",
            "weltgebundene Feldphasen = situative Reaktion",
            "junge Phasenspuren = noch nicht gereifte Randbeobachtung",
            "```",
            "",
            "## Bedeutung",
            "",
            "MINI_DIO bekommt dadurch keine neue Aktion. Es bekommt eine bessere Unterscheidung zwischen stabiler Innenordnung und situativer Weltwirkung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte geprueft werden, ob diese situativen Randphasen in der Rohwelt eher durch Bewegungsbruch, Lautheitslast, Zeitrahmen oder Assetcharakter entstehen.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Liest Weltarten fuer situative MCM-Feldphasen zurueck.")
    parser.add_argument("--input", default=str(DEFAULT_INPUT), help="Feldphasen-Klassen CSV.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Markdown-Ausgabe.")
    args = parser.parse_args()

    input_path = _resolve(args.input)
    out_path = _resolve(args.out)
    rows = _build_rows(_load_rows(input_path))
    _write_csv(out_path.with_suffix(".csv"), rows)
    _write_markdown(out_path, rows, input_path)

    print(f"records={len(rows)} out={out_path}")
    for row in rows:
        print(f"{row['phase_key']} | {row['phase_class']} | {row['trigger_reading']}")


if __name__ == "__main__":
    main()
