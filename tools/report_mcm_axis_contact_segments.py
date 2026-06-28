from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


PASSIVE_FLAGS = {
    "passive_only": 1,
    "read_by_mini_dio": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
}


def _read_rows(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    if not text.strip():
        return []
    try:
        dialect = csv.Sniffer().sniff(text[:4096], delimiters=",;")
    except csv.Error:
        dialect = csv.excel
    return list(csv.DictReader(text.splitlines(), dialect=dialect))


def _short(value: str) -> str:
    return str(value or "").replace("dio_mcm_episode_", "").strip()


def _axis(axis: str) -> tuple[str, str]:
    if "<->" not in axis:
        raise SystemExit(f"axis must use <->: {axis}")
    left, right = axis.split("<->", 1)
    return _short(left), _short(right)


def _joined(row: dict[str, str]) -> str:
    return " ".join(str(value or "") for value in row.values())


def _float(row: dict[str, str], *keys: str) -> float:
    for key in keys:
        value = row.get(key)
        if value in (None, ""):
            continue
        try:
            return float(str(value).replace(",", "."))
        except ValueError:
            continue
    return 0.0


def _value(row: dict[str, str], *keys: str, default: str = "-") -> str:
    for key in keys:
        value = str(row.get(key, "") or "").strip()
        if value:
            return value
    return default


def _tick(row: dict[str, str]) -> str:
    return _value(row, "event_tick", "start_tick", "tick", "start", default="-")


def _match_kind(text: str, a: str, b: str) -> str:
    has_a = a in text
    has_b = b in text
    if has_a and has_b:
        if f"{a}->{b}" in text or f"{b}->{a}" in text:
            return "paar_gerichtet"
        return "paar_gemeinsam"
    if has_a:
        return "nur_a"
    if has_b:
        return "nur_b"
    return "kein_kontakt"


def _top(counter: Counter[str], limit: int = 6) -> str:
    return " | ".join(f"{key}:{value}" for key, value in counter.most_common(limit)) or "-"


def _segment_row(axis_label: str, a: str, b: str, source: Path, row: dict[str, str]) -> dict[str, object] | None:
    text = _joined(row)
    match_kind = _match_kind(text, a, b)
    if match_kind == "kein_kontakt":
        return None
    return {
        **PASSIVE_FLAGS,
        "axis": axis_label,
        "axis_a": a,
        "axis_b": b,
        "source": source.name,
        "world": _value(row, "world", "source_world", "dataset", "source_debug"),
        "tick": _tick(row),
        "end_tick": _value(row, "end_tick", default=_tick(row)),
        "duration": _value(row, "duration", default="1"),
        "match_kind": match_kind,
        "effect": _value(row, "dominant_effect", "movement_effect", "switch_class", "field_memory_quality"),
        "before_class": _value(row, "before_class", default="-"),
        "switch_class": _value(row, "switch_class", default="-"),
        "after_class": _value(row, "after_class", "post_state", default="-"),
        "dominant_family": _value(row, "dominant_family", default="-"),
        "mcm_preview": _value(row, "dominant_mcm_episode_preview", "pair", "movement_key", default="-"),
        "avg_pressure": round(_float(row, "avg_pressure"), 6),
        "avg_alignment": round(_float(row, "avg_alignment"), 6),
        "avg_coherence": round(_float(row, "avg_coherence"), 6),
        "avg_strain": round(_float(row, "avg_strain", "strain"), 6),
        "avg_rekopplung": round(_float(row, "avg_rekopplung", "rekopplung"), 6),
        "pressure_delta": round(_float(row, "pressure_delta", "avg_pressure_delta"), 6),
        "rekopplung_delta": round(_float(row, "rekopplung_delta", "avg_rekopplung_delta"), 6),
        "pre8_rekopplung": round(_float(row, "pre8_rekopplung"), 6),
        "post8_rekopplung": round(_float(row, "post8_rekopplung"), 6),
        "pre8_strain": round(_float(row, "pre8_strain"), 6),
        "post8_strain": round(_float(row, "post8_strain"), 6),
        "segment_reading": _segment_reading(row, match_kind),
    }


def _segment_reading(row: dict[str, str], match_kind: str) -> str:
    rek = _float(row, "avg_rekopplung", "rekopplung")
    strain = _float(row, "avg_strain", "strain")
    rek_delta = _float(row, "rekopplung_delta", "avg_rekopplung_delta")
    pressure_delta = _float(row, "pressure_delta", "avg_pressure_delta")
    effect = _value(row, "dominant_effect", "movement_effect", "switch_class", "field_memory_quality")
    if match_kind.startswith("paar") and "rekoppel" in effect:
        return "paarsegment_rekoppelnd"
    if match_kind.startswith("paar") and rek > strain and rek > 0:
        return "paarsegment_getragen"
    if match_kind.startswith("paar") and pressure_delta > 0 and rek_delta < 0:
        return "paarsegment_spannungswechsel"
    if match_kind == "nur_a":
        return "a_knoten_kontakt"
    if match_kind == "nur_b":
        return "b_knoten_kontakt"
    return "kontaktsegment_offen"


def _collect(axis_label: str, files: list[Path]) -> list[dict[str, object]]:
    a, b = _axis(axis_label)
    rows: list[dict[str, object]] = []
    for path in files:
        if not path.exists():
            continue
        for row in _read_rows(path):
            segment = _segment_row(axis_label, a, b, path, row)
            if segment is not None:
                rows.append(segment)
    rows.sort(key=lambda row: (str(row["match_kind"]), str(row["world"]), float(str(row["tick"]).replace("-", "0"))))
    return rows


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else [*PASSIVE_FLAGS.keys(), "axis", "source", "world", "tick", "match_kind"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _avg(rows: list[dict[str, object]], key: str) -> float:
    values = [float(row.get(key) or 0.0) for row in rows]
    return sum(values) / len(values) if values else 0.0


def _write_md(path: Path, axis_label: str, rows: list[dict[str, object]], max_rows: int) -> None:
    by_kind = Counter(str(row["match_kind"]) for row in rows)
    by_reading = Counter(str(row["segment_reading"]) for row in rows)
    by_world = Counter(str(row["world"]) for row in rows)
    pair_rows = [row for row in rows if str(row["match_kind"]).startswith("paar")]
    lines = [
        "# MCM-Zentrumsachse: lokale Kontaktsegmente",
        "",
        "## Zweck",
        "",
        "Diese Datei liest konkrete Kontaktsegmente der staerksten Zentrumsachse.",
        "Getrennt wird zwischen echtem Paarsegment und Einzelknoten-Kontakt.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Ruecklesung",
        "- keine Handlung",
        "- kein Gate",
        "- keine Strategie",
        "",
        "## Zusammenfassung",
        "",
        f"- Achse: `{axis_label}`",
        f"- Kontaktsegmente gesamt: {len(rows)}",
        f"- Paarsegmente: {len(pair_rows)}",
        f"- Kontaktarten: `{_top(by_kind)}`",
        f"- Segmentlesung: `{_top(by_reading)}`",
        f"- Welten: `{_top(by_world)}`",
        f"- Paarsegmente Rekopplung: {round(_avg(pair_rows, 'avg_rekopplung'), 6)}",
        f"- Paarsegmente Strain: {round(_avg(pair_rows, 'avg_strain'), 6)}",
        f"- Paarsegmente Pressure-Delta: {round(_avg(pair_rows, 'pressure_delta'), 6)}",
        f"- Paarsegmente Rekopplung-Delta: {round(_avg(pair_rows, 'rekopplung_delta'), 6)}",
        "",
        "## Paarsegmente",
        "",
        "| Welt | Tick | Quelle | Effekt | Klassen | Rekopplung | Strain | Pressure Delta | Rekopplung Delta | Lesung |",
        "|---|---:|---|---|---|---:|---:|---:|---:|---|",
    ]
    for row in pair_rows[:max_rows]:
        classes = f"{row['before_class']} / {row['switch_class']} / {row['after_class']}"
        lines.append(
            f"| `{row['world']}` | {row['tick']} | `{row['source']}` | `{row['effect']}` | `{classes}` | "
            f"{row['avg_rekopplung']} | {row['avg_strain']} | {row['pressure_delta']} | {row['rekopplung_delta']} | `{row['segment_reading']}` |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Paarsegmente zeigen, wo die Achse lokal wirklich gekoppelt auftritt.",
            "Einzelknoten-Kontakte zeigen dagegen breite Feldnaehe ohne zwingende Achsenkopplung.",
            "",
            "Arbeitsableitung:",
            "",
            "```text",
            "Die Zentrumsachse ist nicht nur ein globaler Name.",
            "Sie besitzt lokale Kontaktsegmente, in denen Weltlage, MCM-Wirkung und Rollennaehe zusammenfallen.",
            "```",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte geprueft werden, welche dieser Kontaktsegmente reproduzierbar wiederkehren und welche nur situationsbedingt auftreten.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--axis", required=True)
    parser.add_argument("--event-file", action="append", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    parser.add_argument("--max-rows", type=int, default=40)
    args = parser.parse_args()

    rows = _collect(args.axis, args.event_file)
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, args.axis, rows, args.max_rows)
    print(f"segments={len(rows)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
