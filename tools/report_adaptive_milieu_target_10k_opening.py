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
    symbol = (row.get("symbol") or "").strip()
    return symbol[:8] if symbol else "-"


def _raw_by_timestamp(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {str(row.get("timestamp_ms", "")): row for row in rows if row.get("timestamp_ms")}


def _raw_metrics(rows: list[dict[str, str]], raw_index: dict[str, dict[str, str]]) -> dict[str, float]:
    ranges: list[float] = []
    bodies: list[float] = []
    volumes: list[float] = []
    closes: list[float] = []
    for row in rows:
        raw = raw_index.get(str(row.get("timestamp_ms", "")))
        if not raw:
            continue
        open_ = _float(raw.get("open"))
        high = _float(raw.get("high"))
        low = _float(raw.get("low"))
        close = _float(raw.get("close"))
        base = max(abs(open_), 1e-12)
        ranges.append((high - low) / base)
        bodies.append(abs(close - open_) / base)
        volumes.append(_float(raw.get("volume")))
        closes.append(close)
    net = 0.0
    if len(closes) >= 2 and abs(closes[0]) > 1e-12:
        net = (closes[-1] - closes[0]) / closes[0]
    return {
        "raw_net_pct": net * 100.0,
        "raw_range_pct": _mean(ranges) * 100.0,
        "raw_body_pct": _mean(bodies) * 100.0,
        "raw_volume": _mean(volumes),
    }


def _metrics(rows: list[dict[str, str]], raw_index: dict[str, dict[str, str]]) -> dict[str, float]:
    result = {
        "count": float(len(rows)),
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
    result.update(_raw_metrics(rows, raw_index))
    return result


def _world_arg(values: list[str]) -> tuple[str, Path, Path]:
    if len(values) != 3:
        raise argparse.ArgumentTypeError("--world braucht: NAME EPISODES RAW")
    return values[0], _resolve(values[1]), _resolve(values[2])


def _collect(args: argparse.Namespace) -> list[dict[str, object]]:
    families = set(args.family)
    rows_out: list[dict[str, object]] = []
    for world_name, episode_path, raw_path in (_world_arg(value) for value in args.world):
        episodes = _load_csv(episode_path)
        raw_index = _raw_by_timestamp(_load_csv(raw_path))
        by_tick = {int(_float(row.get("tick"))): idx for idx, row in enumerate(episodes)}
        for family in sorted(families):
            occurrences = [row for row in episodes if _family(row) == family]
            pre_rows: list[dict[str, str]] = []
            for row in occurrences:
                idx = by_tick.get(int(_float(row.get("tick"))))
                if idx is None:
                    continue
                pre_rows.extend(episodes[max(0, idx - args.lookback) : idx])
            pre = _metrics(pre_rows, raw_index)
            hit = _metrics(occurrences, raw_index)
            if not occurrences:
                rows_out.append(
                    {
                        "world": world_name,
                        "family": family,
                        "occurrences": 0,
                        "pre_count": 0,
                        "hit_count": 0,
                        "hearing_delta_hit_minus_pre": 0.0,
                        "tension_delta_hit_minus_pre": 0.0,
                        "range_delta_hit_minus_pre": 0.0,
                    }
                )
                continue
            row: dict[str, object] = {
                "world": world_name,
                "family": family,
                "occurrences": len(occurrences),
                "pre_count": int(pre["count"]),
                "hit_count": int(hit["count"]),
                "hearing_delta_hit_minus_pre": hit["hearing_gap"] - pre["hearing_gap"],
                "tension_delta_hit_minus_pre": hit["mcm_tension"] - pre["mcm_tension"],
                "range_delta_hit_minus_pre": hit["raw_range_pct"] - pre["raw_range_pct"],
            }
            row.update({f"pre_{key}": value for key, value in pre.items()})
            row.update({f"hit_{key}": value for key, value in hit.items()})
            rows_out.append(row)
    return rows_out


def _aggregate(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    grouped["ALLE"] = [row for row in rows if int(row.get("occurrences", 0) or 0) > 0]
    for row in rows:
        if int(row.get("occurrences", 0) or 0) > 0:
            grouped[str(row["family"])].append(row)
    out: list[dict[str, object]] = []
    for family, items in grouped.items():
        out.append(
            {
                "family": family,
                "world_hits": len(items),
                "occurrences": sum(int(item.get("occurrences", 0) or 0) for item in items),
                "pre_hearing": _mean([float(item.get("pre_hearing_gap", 0.0) or 0.0) for item in items]),
                "hit_hearing": _mean([float(item.get("hit_hearing_gap", 0.0) or 0.0) for item in items]),
                "pre_tension": _mean([float(item.get("pre_mcm_tension", 0.0) or 0.0) for item in items]),
                "hit_tension": _mean([float(item.get("hit_mcm_tension", 0.0) or 0.0) for item in items]),
                "pre_range": _mean([float(item.get("pre_raw_range_pct", 0.0) or 0.0) for item in items]),
                "hit_range": _mean([float(item.get("hit_raw_range_pct", 0.0) or 0.0) for item in items]),
                "hearing_delta": _mean([float(item.get("hearing_delta_hit_minus_pre", 0.0) or 0.0) for item in items]),
                "tension_delta": _mean([float(item.get("tension_delta_hit_minus_pre", 0.0) or 0.0) for item in items]),
                "range_delta": _mean([float(item.get("range_delta_hit_minus_pre", 0.0) or 0.0) for item in items]),
            }
        )
    return sorted(out, key=lambda row: str(row["family"]))


def _write_csv(rows: list[dict[str, object]], out_path: Path) -> None:
    csv_path = out_path.with_suffix(".csv")
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        csv_path.write_text("", encoding="utf-8")
        return
    fields: list[str] = []
    seen: set[str] = set()
    for row in rows:
        for key in row.keys():
            if key not in seen:
                seen.add(key)
                fields.append(key)
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    key: _fmt(row.get(key), 6) if isinstance(row.get(key), float) else row.get(key, "")
                    for key in fields
                }
            )


def _write_md(rows: list[dict[str, object]], summary: list[dict[str, object]], out_path: Path) -> None:
    _write_csv(rows, out_path)
    summary_path = out_path.with_name(out_path.stem + "_summary.csv")
    _write_csv(summary, summary_path)
    title_prefix = out_path.stem.split("_", 1)[0]
    family_names = [str(row.get("family", "")) for row in summary if str(row.get("family", "")) not in {"", "ALLE"}]
    family_label = ", ".join(family_names) if family_names else "Ziel-Familie"
    family_occurrences = sum(int(row.get("occurrences", 0) or 0) for row in summary if str(row.get("family", "")) not in {"", "ALLE"})
    stem_upper = out_path.stem.upper()
    is_axis_report = "ACHSENISOLATION" in stem_upper
    is_pair_report = "ZWEIERKOPPLUNG" in stem_upper
    if is_axis_report:
        report_name = "Synthetische Achsenisolation der Oeffnungs-Vorform"
    elif is_pair_report:
        report_name = "Synthetische Zweierkopplung der Oeffnungs-Vorform"
    else:
        report_name = "10k-Pruefung der Oeffnungs-Vorform"
    title = f"# {title_prefix} - {report_name}" if title_prefix.isdigit() else f"# {report_name}"
    if is_axis_report:
        purpose = (
            "Diese Diagnose prueft, ob die Oeffnungs-Vorform bei isolierten synthetischen "
            "Sinnesachsen sichtbar bleibt oder erst durch gekoppelte Last bricht."
        )
        hierarchy = [
            "1. Grundfrage: Traegt `dio_0ly7` unter einzelner Achsenstoerung weiter?",
            "2. Unterpruefung: Hoer-, Spannungs- und Range-Delta je isolierter Welt lesen.",
            "3. Folgeschritt: Gegen gekoppelte Lastwelten vergleichen.",
        ]
        next_step = (
            "Als naechstes sollte die Achsenisolation gegen gekoppelte Lastwelten gehalten werden: "
            "kippt `dio_0ly7` erst, wenn Range, Hoeren und Spannung gemeinsam steigen?"
        )
    elif is_pair_report:
        purpose = (
            "Diese Diagnose prueft, ob die Oeffnungs-Vorform bei synthetischen Zweierkopplungen "
            "getragen bleibt oder bereits vor der vollen Dreierlast kippt."
        )
        hierarchy = [
            f"1. Grundfrage: Welche gekoppelte Stoerung bricht `{family_label}`?",
            "2. Unterpruefung: Range+Hoeren, Range+Spannung und Hoeren+Spannung getrennt lesen.",
            "3. Folgeschritt: Gegen Einzelachsen und volle gekoppelte Last verdichten.",
        ]
        if family_occurrences < 10:
            next_step = (
                "Als naechstes sollte fuer diese Familie zuerst eine passendere synthetische Welt gesucht werden, "
                "weil die aktuelle Zweierkopplung zu wenig Sichtbarkeit erzeugt."
            )
        else:
            next_step = (
                "Als naechstes sollte die Zweierkopplung direkt gegen Einzelachsen und Dreierlast "
                "zusammengefasst werden: ist Range der kritische Kopplungsanteil?"
            )
    else:
        purpose = (
            "Diese Diagnose prueft, ob die in 1702 beschriebene Entlastungsbewegung in "
            "durchlaufenden 10k-Welten wiederkehrt."
        )
        hierarchy = [
            "1. Grundfrage: Ist `milieu_oeffnet_nach_entlastung` auch ohne 5000er Split sichtbar?",
            "2. Unterpruefung: `dio_0ly7` und `dio_01hu` in frischen 10k-Welten gegen Vorfenster lesen.",
            "3. Folgeschritt: Falls stabil, laengere Weltgruppen und weitere Jahre pruefen.",
        ]
        next_step = (
            "Als naechstes sollte der Befund gegen andere Jahre und gegen synthetische Kontrollwelten "
            "gehalten werden, falls die 10k-Pruefung die Entlastungsform traegt."
        )
    lines = [
        title,
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        purpose,
        "Sie bleibt passiv: keine Handlung, kein Gate, keine Richtung.",
        "",
        "## Hierarchie",
        "",
        *hierarchy,
        "",
        "## Aggregat",
        "",
        "| Familie | Welten mit Treffer | Vorkommen | Vor Hoeren | Hit Hoeren | Delta Hoeren | Vor Spannung | Hit Spannung | Delta Spannung |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summary:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["family"]),
                    str(row["world_hits"]),
                    str(row["occurrences"]),
                    _fmt(float(row["pre_hearing"])),
                    _fmt(float(row["hit_hearing"])),
                    _fmt(float(row["hearing_delta"])),
                    _fmt(float(row["pre_tension"])),
                    _fmt(float(row["hit_tension"])),
                    _fmt(float(row["tension_delta"])),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Einzelwelten",
            "",
            "| Welt | Familie | Vorkommen | Vor Hoeren | Hit Hoeren | Delta Hoeren | Vor Spannung | Hit Spannung | Delta Spannung |",
            "|---|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["world"]),
                    str(row["family"]),
                    str(row["occurrences"]),
                    _fmt(float(row.get("pre_hearing_gap", 0.0) or 0.0)),
                    _fmt(float(row.get("hit_hearing_gap", 0.0) or 0.0)),
                    _fmt(float(row.get("hearing_delta_hit_minus_pre", 0.0) or 0.0)),
                    _fmt(float(row.get("pre_mcm_tension", 0.0) or 0.0)),
                    _fmt(float(row.get("hit_mcm_tension", 0.0) or 0.0)),
                    _fmt(float(row.get("tension_delta_hit_minus_pre", 0.0) or 0.0)),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            (
                f"`{family_label}` ist in dieser Zweierkopplungspruefung zu selten sichtbar. "
                "Die Kopplungsqualitaet bleibt deshalb offen."
                if is_pair_report and family_occurrences < 10
                else "Wenn Range+Hoeren oder Range+Spannung kippen, aber Hoeren+Spannung getragen bleibt, "
                "spricht das fuer Range als kritischen Kopplungsanteil."
                if is_pair_report
                else "Wenn Delta Hoeren und Delta Spannung negativ bleiben, stuetzt das die Entlastungslesung aus 1702."
            ),
            (
                "Der Befund wird dokumentiert, aber nicht als Bruch- oder Tragfaehigkeitsaussage gewertet."
                if is_pair_report and family_occurrences < 10
                else "Die Form wird dann nicht durch jede Zweierlast gebrochen, sondern durch bestimmte Kopplungsqualitaeten."
                if is_pair_report
                else "Wenn sie kippen oder verschwinden, war die 5000er-Oeffnungsform eher fensterspezifisch."
            ),
            "",
            "## Wie es weitergeht",
            "",
            next_step,
            "",
        ]
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Prueft robuste Ziel-Familien in durchlaufenden 10k-Welten.")
    parser.add_argument("--family", action="append", required=True)
    parser.add_argument("--world", nargs=3, action="append", required=True, metavar=("NAME", "EPISODES", "RAW"))
    parser.add_argument("--lookback", type=int, default=8)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()
    rows = _collect(args)
    summary = _aggregate(rows)
    _write_md(rows, summary, _resolve(args.out_md))
    print({"out_md": str(_resolve(args.out_md)), "rows": len(rows), "summary": len(summary)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
