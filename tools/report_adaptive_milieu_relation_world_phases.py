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


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    if result != result:
        return 0.0
    return result


def _fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"


def _mean(values: list[float]) -> float:
    return fmean(values) if values else 0.0


def _load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _family(row: dict[str, str]) -> str:
    for key in ("symbol_family", "mcm_field_episode_preview_symbol", "mcm_field_episode_symbol"):
        value = (row.get(key) or "").strip()
        if value:
            return value[:12]
    symbol = (row.get("symbol") or row.get("episode_memory_symbol") or "").strip()
    return symbol[:12] if symbol else "-"


def _by_world_family(rows: list[dict[str, str]], follow: bool = False) -> dict[str, dict[str, dict[str, str]]]:
    result: dict[str, dict[str, dict[str, str]]] = defaultdict(dict)
    for row in rows:
        world = (row.get("world") or "").replace("_FOLLOW", "").lower()
        result[world][row.get("family", "-")] = row
    return result


def _raw_by_timestamp(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {str(row.get("timestamp_ms", "")): row for row in rows if row.get("timestamp_ms")}


def _phase_metrics(episode_rows: list[dict[str, str]], raw_rows: dict[str, dict[str, str]]) -> dict[str, object]:
    matched_raw: list[dict[str, str]] = []
    ticks: list[int] = []
    for row in episode_rows:
        try:
            ticks.append(int(float(row.get("tick", 0) or 0)))
        except Exception:
            pass
        raw = raw_rows.get(str(row.get("timestamp_ms", "")))
        if raw:
            matched_raw.append(raw)

    closes = [_float(row.get("close")) for row in matched_raw if row.get("close") not in (None, "")]
    opens = [_float(row.get("open")) for row in matched_raw if row.get("open") not in (None, "")]
    highs = [_float(row.get("high")) for row in matched_raw if row.get("high") not in (None, "")]
    lows = [_float(row.get("low")) for row in matched_raw if row.get("low") not in (None, "")]
    volumes = [_float(row.get("volume")) for row in matched_raw if row.get("volume") not in (None, "")]
    body_pct: list[float] = []
    range_pct: list[float] = []
    for raw in matched_raw:
        close = _float(raw.get("close"))
        open_ = _float(raw.get("open"))
        high = _float(raw.get("high"))
        low = _float(raw.get("low"))
        base = max(abs(open_), 1e-12)
        body_pct.append(abs(close - open_) / base)
        range_pct.append((high - low) / base)

    net_return = 0.0
    if len(closes) >= 2 and abs(closes[0]) > 1e-12:
        net_return = (closes[-1] - closes[0]) / closes[0]

    return {
        "episode_count": len(episode_rows),
        "raw_match_count": len(matched_raw),
        "tick_start": min(ticks) if ticks else 0,
        "tick_end": max(ticks) if ticks else 0,
        "net_return_pct": net_return * 100.0,
        "avg_body_pct": _mean(body_pct) * 100.0,
        "avg_range_pct": _mean(range_pct) * 100.0,
        "avg_volume": _mean(volumes),
        "avg_rekopplung": _mean([_float(row.get("mcm_rekopplung_quality")) for row in episode_rows]),
        "avg_adaptive_rekopplung": _mean([_float(row.get("mcm_adaptive_rekopplung_quality")) for row in episode_rows]),
        "avg_strain": _mean([_float(row.get("mcm_strain_quality")) for row in episode_rows]),
        "avg_visual_gap": _mean([_float(row.get("mcm_visual_field_gap")) for row in episode_rows]),
        "avg_hearing_gap": _mean([_float(row.get("mcm_hearing_field_gap")) for row in episode_rows]),
        "avg_feld_coherence": _mean([_float(row.get("mcm_feldwirkung_mcm_coherence")) for row in episode_rows]),
        "avg_feld_tension": _mean([_float(row.get("mcm_feldwirkung_mcm_tension")) for row in episode_rows]),
    }


def _collect_episode_rows(path: Path) -> dict[str, list[dict[str, str]]]:
    result: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in _load_csv(path):
        result[_family(row)].append(row)
    return result


def _transition_rows(
    *,
    world: str,
    base_family: dict[str, dict[str, str]],
    follow_family: dict[str, dict[str, str]],
    base_episodes: dict[str, list[dict[str, str]]],
    follow_episodes: dict[str, list[dict[str, str]]],
    base_raw: dict[str, dict[str, str]],
    follow_raw: dict[str, dict[str, str]],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for family in sorted(set(base_family) & set(follow_family)):
        before = base_family[family]
        after = follow_family[family]
        before_relation = before.get("relation", "-")
        after_relation = after.get("relation", "-")
        if before_relation == after_relation:
            continue
        if (before_relation, after_relation) not in {
            ("offen_und_gereift", "nur_gereift"),
            ("nur_offen", "offen_und_gereift"),
            ("offen_und_gereift", "nur_offen"),
            ("nur_gereift", "offen_und_gereift"),
        }:
            continue
        base_metrics = _phase_metrics(base_episodes.get(family, []), base_raw)
        follow_metrics = _phase_metrics(follow_episodes.get(family, []), follow_raw)
        rows.append(
            {
                "world": world,
                "family": family,
                "transition": f"{before_relation}->{after_relation}",
                "base_total": int(float(before.get("total", 0) or 0)),
                "follow_total": int(float(after.get("total", 0) or 0)),
                "base_open_share": _float(before.get("open_share")),
                "follow_open_share": _float(after.get("open_share")),
                "base_mature_share": _float(before.get("mature_share")),
                "follow_mature_share": _float(after.get("mature_share")),
                **{f"base_{key}": value for key, value in base_metrics.items()},
                **{f"follow_{key}": value for key, value in follow_metrics.items()},
            }
        )
    return rows


def _write_csv(rows: list[dict[str, object]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        out_path.with_suffix(".csv").write_text("", encoding="utf-8")
        return
    fields = list(rows[0].keys())
    with out_path.with_suffix(".csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: _fmt(float(value), 6) if isinstance(value, float) else value for key, value in row.items()})


def _write_md(rows: list[dict[str, object]], out_path: Path) -> None:
    _write_csv(rows, out_path)
    by_transition = defaultdict(list)
    for row in rows:
        by_transition[str(row["transition"])].append(row)

    lines = [
        "# 1688 - Milieu-Relationswechsel und Rohweltphasen",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest starke adaptive Milieu-Relationswechsel gegen konkrete Rohweltphasen zurueck.",
        "Sie bleibt passiv: keine Handlung, kein Gate, keine Richtung.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Welche Weltphasen liegen unter starken Milieu-Wechseln?",
        "2. Unterpruefung: Familien mit `offen_und_gereift -> nur_gereift` und `nur_offen -> offen_und_gereift` vergleichen.",
        "3. Folgeschritt: Wiederkehrende Rohweltprofile als moegliche Milieu-Trigger pruefen.",
        "",
        "## Uebersicht",
        "",
        "| Transition | Anzahl | Welten |",
        "|---|---:|---|",
    ]
    for transition, items in sorted(by_transition.items()):
        worlds = ", ".join(sorted({str(item["world"]) for item in items}))
        lines.append(f"| {transition} | {len(items)} | {worlds} |")

    lines.extend(
        [
            "",
            "## Staerkste Wechsel",
            "",
            "| Welt | Familie | Wechsel | vorher | Folge | Basis Nettoverlauf % | Folge Nettoverlauf % | Basis Range % | Folge Range % | Basis Hoeren-Gap | Folge Hoeren-Gap | Basis Spannung | Folge Spannung |",
            "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    priority = {
        "offen_und_gereift->nur_gereift": 0,
        "nur_offen->offen_und_gereift": 1,
        "offen_und_gereift->nur_offen": 2,
        "nur_gereift->offen_und_gereift": 3,
    }
    top = sorted(
        rows,
        key=lambda row: (priority.get(str(row["transition"]), 9), -int(row["base_total"]) - int(row["follow_total"])),
    )[:32]
    for row in top:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["world"]),
                    str(row["family"]),
                    str(row["transition"]),
                    str(row["base_total"]),
                    str(row["follow_total"]),
                    _fmt(float(row["base_net_return_pct"])),
                    _fmt(float(row["follow_net_return_pct"])),
                    _fmt(float(row["base_avg_range_pct"])),
                    _fmt(float(row["follow_avg_range_pct"])),
                    _fmt(float(row["base_avg_hearing_gap"])),
                    _fmt(float(row["follow_avg_hearing_gap"])),
                    _fmt(float(row["base_avg_feld_tension"])),
                    _fmt(float(row["follow_avg_feld_tension"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "`offen_und_gereift -> nur_gereift` bedeutet: Eine Familie bleibt in der Folgewelt vorhanden, verliert aber ihre offene Schicht und wird enger gereift gelesen.",
            "",
            "`nur_offen -> offen_und_gereift` bedeutet: Eine zuvor nur offene Familie bekommt in der Folgewelt zusaetzliche gereifte Anteile.",
            "",
            "Die Rohweltspalten dienen als Ruecklesung, nicht als Ursachebeweis. Entscheidend ist, ob solche Wechsel wiederholt mit aehnlichen Spannungs-, Range-, Hoer- oder Feldprofilen auftreten.",
            "",
            "## Grenze",
            "",
            "Dieser Bericht zeigt Kopplungen zwischen Milieu-Wechsel und Weltphase. Er beweist noch keinen Mechanismus und erzeugt keine neue Regel.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollten die haeufigsten Wechsel-Familien einzeln ueber weitere Folgewelten verfolgt werden. Wenn dieselbe Familie wiederholt unter aehnlicher Rohweltspannung reift oder oeffnet, wird daraus ein belastbarer Milieu-Trigger-Kandidat.",
            "",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Liest adaptive Milieu-Relationswechsel gegen Rohweltphasen.")
    parser.add_argument("--base-family-csv", required=True)
    parser.add_argument("--follow-family-csv", required=True)
    parser.add_argument("--world", nargs=5, action="append", metavar=("NAME", "BASE_EPISODES", "FOLLOW_EPISODES", "BASE_DATA", "FOLLOW_DATA"), required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    base_families = _by_world_family(_load_csv(_resolve(args.base_family_csv)))
    follow_families = _by_world_family(_load_csv(_resolve(args.follow_family_csv)), follow=True)

    all_rows: list[dict[str, object]] = []
    for name, base_episode_path, follow_episode_path, base_data_path, follow_data_path in args.world:
        base_episode_rows = _collect_episode_rows(_resolve(base_episode_path))
        follow_episode_rows = _collect_episode_rows(_resolve(follow_episode_path))
        base_raw = _raw_by_timestamp(_load_csv(_resolve(base_data_path)))
        follow_raw = _raw_by_timestamp(_load_csv(_resolve(follow_data_path)))
        key = name.replace("_FOLLOW", "").lower()
        all_rows.extend(
            _transition_rows(
                world=name.replace("_FOLLOW", ""),
                base_family=base_families.get(key, {}),
                follow_family=follow_families.get(key, {}),
                base_episodes=base_episode_rows,
                follow_episodes=follow_episode_rows,
                base_raw=base_raw,
                follow_raw=follow_raw,
            )
        )

    out_path = _resolve(args.out_md)
    _write_md(all_rows, out_path)
    print({"out_md": str(out_path), "rows": len(all_rows)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
