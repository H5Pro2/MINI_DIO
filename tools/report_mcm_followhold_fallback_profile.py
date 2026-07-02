from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


DEFAULT_INPUT = ROOT / "docs" / "befunde" / "1266_MCM_FOLGEHALT_ROHWELT_KOPPLUNG.csv"
DEFAULT_OUT = ROOT / "docs" / "befunde" / "1270_MCM_FOLGEHALT_RUECKFALLPROFIL.md"


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _fmt(value: object) -> str:
    try:
        return f"{float(value):.4f}"
    except (TypeError, ValueError):
        return str(value)


def _asset(row: dict[str, str]) -> str:
    text = f"{row.get('world', '')} {row.get('data_file', '')}".upper()
    for name in ("BTC", "SOL", "KAS", "DOGE", "XRP", "PAXG"):
        if name in text:
            return name
    if "SIDEWAYS" in text:
        return "SYNTH_SIDEWAYS"
    if "EXPANSION" in text or "POS_" in text:
        return "SYNTH_EXPANSION"
    if "NEG_" in text or "STRESS" in text:
        return "SYNTH_STRESS"
    return "UNKNOWN"


def _kind_group(row: dict[str, str]) -> str:
    kind = str(row.get("followhold_kind", "") or "")
    if "rueckfall" in kind:
        return "rueckfall"
    if "gemischt" in kind:
        return "gemischt"
    if "entlastend_gehalten" in kind:
        return "getragen"
    return "offen"


def _strength(row: dict[str, str]) -> float:
    expansion = _safe_float(row.get("expansion_ratio"))
    range_ratio = _safe_float(row.get("range_ratio"))
    body_ratio = _safe_float(row.get("body_ratio"))
    reko_gain = _safe_float(row.get("delta_follow_rekopplung"))
    strain_release = max(0.0, -_safe_float(row.get("delta_follow_strain")))
    return expansion + (range_ratio * 20.0) + (body_ratio * 50.0) - reko_gain - strain_release


def _group(rows: list[dict[str, str]], key_fn) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[key_fn(row)].append(row)

    out: list[dict[str, object]] = []
    for name, group in grouped.items():
        out.append(
            {
                "name": name,
                "count": len(group),
                "followhold": dict(Counter(str(row.get("followhold_kind", "")) for row in group).most_common(5)),
                "asset": dict(Counter(_asset(row) for row in group).most_common(6)),
                "raw_shape": dict(Counter(str(row.get("raw_shape_bucket", "")) for row in group).most_common(4)),
                "raw_return": _mean([_safe_float(row.get("raw_return")) for row in group]),
                "range_ratio": _mean([_safe_float(row.get("range_ratio")) for row in group]),
                "body_ratio": _mean([_safe_float(row.get("body_ratio")) for row in group]),
                "expansion_ratio": _mean([_safe_float(row.get("expansion_ratio")) for row in group]),
                "direction_consistency": _mean([_safe_float(row.get("direction_consistency")) for row in group]),
                "rand_loudness": _mean([_safe_float(row.get("rand_loudness")) for row in group]),
                "rand_strain": _mean([_safe_float(row.get("rand_strain")) for row in group]),
                "delta_follow_rekopplung": _mean([_safe_float(row.get("delta_follow_rekopplung")) for row in group]),
                "delta_follow_strain": _mean([_safe_float(row.get("delta_follow_strain")) for row in group]),
                "follow_duration": _mean([_safe_float(row.get("follow_duration")) for row in group]),
            }
        )
    out.sort(key=lambda item: (-int(item["count"]), str(item["name"])))
    return out


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _table(lines: list[str], title: str, rows: list[dict[str, object]]) -> None:
    lines.extend(
        [
            "",
            f"## {title}",
            "",
            "| Gruppe | Anzahl | Folgehalt | Assets | Rohform | Expansion | Range | Body | Richtung | Lautheit | Delta Rekopplung | Delta Strain | Folge-Dauer |",
            "|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["name"]),
                    str(row["count"]),
                    str(row["followhold"]),
                    str(row["asset"]),
                    str(row["raw_shape"]),
                    _fmt(row["expansion_ratio"]),
                    _fmt(row["range_ratio"]),
                    _fmt(row["body_ratio"]),
                    _fmt(row["direction_consistency"]),
                    _fmt(row["rand_loudness"]),
                    _fmt(row["delta_follow_rekopplung"]),
                    _fmt(row["delta_follow_strain"]),
                    _fmt(row["follow_duration"]),
                ]
            )
            + " |"
        )


def _write_markdown(path: Path, rows: list[dict[str, str]], fallback_rows: list[dict[str, str]]) -> None:
    by_group = _group(rows, _kind_group)
    by_asset = _group(fallback_rows, _asset)
    by_shape = _group(fallback_rows, lambda row: str(row.get("raw_shape_bucket", "") or ""))
    strongest = sorted(fallback_rows, key=_strength, reverse=True)[:24]

    lines: list[str] = [
        "# MCM Folgehalt Rueckfallprofil",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "## Grundfrage",
        "",
        "Welche Weltmerkmale machen aus Randkontakt zuerst Folgeordnung, danach aber wieder Rueckfall in Rand/Kipp?",
        "",
        "## Unterpruefung",
        "",
        "Diese Diagnose trennt Rueckfallfenster aus der Folgehalt-Rohwelt-Kopplung und vergleicht sie gegen gehaltene Folgeformen.",
        "",
        "## Profil",
        "",
        f"- gekoppelte Fenster gesamt: `{len(rows)}`",
        f"- Rueckfallfenster: `{len(fallback_rows)}`",
        f"- Rueckfallarten: `{dict(Counter(str(row.get('followhold_kind', '')) for row in fallback_rows).most_common())}`",
        "",
    ]
    _table(lines, "Gesamtvergleich", by_group)
    _table(lines, "Rueckfall nach Asset", by_asset)
    _table(lines, "Rueckfall nach Rohform", by_shape)

    lines.extend(
        [
            "",
            "## Staerkste Rueckfallfenster",
            "",
            "| Welt | Tick | Art | Rohform | Return | Range | Expansion | Richtung | Lautheit | Delta Rekopplung | Delta Strain | Folge-Dauer |",
            "|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in strongest:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row.get("world", "")),
                    str(row.get("rand_start_tick", "")),
                    str(row.get("followhold_kind", "")),
                    str(row.get("raw_shape_bucket", "")),
                    _fmt(row.get("raw_return")),
                    _fmt(row.get("range_ratio")),
                    _fmt(row.get("expansion_ratio")),
                    _fmt(row.get("direction_consistency")),
                    _fmt(row.get("rand_loudness")),
                    _fmt(row.get("delta_follow_rekopplung")),
                    _fmt(row.get("delta_follow_strain")),
                    _fmt(row.get("follow_duration")),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Rueckfall ist kein eigener Rohwelt-Typ. Er entsteht vor allem dort, wo Bruch- oder Expansionsspannung hoch bleibt, obwohl das Feld kurzfristig entlastet.",
            "",
            "Das Feld kann also kurz entlasten, ohne dass die Weltspannung schon wirklich getragen ist.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte geprueft werden, ob Rueckfallfenster im Feld eine eigene Vorwarnspur bilden: gibt es vor dem Rueckfall bereits ein messbares Drift- oder Nachhallzeichen?",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def _write_assessment(path: Path, fallback_rows: list[dict[str, str]]) -> None:
    by_asset = _group(fallback_rows, _asset)
    by_shape = _group(fallback_rows, lambda row: str(row.get("raw_shape_bucket", "") or ""))
    lines = [
        "# Bewertung: MCM Folgehalt Rueckfallprofil",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "## Kernaussage",
        "",
        "Rueckfall entsteht nicht, weil das Feld keine Entlastung kann. Rueckfall entsteht, wenn die Entlastung gegen eine weiter aktive Weltspannung nicht lange getragen wird.",
        "",
        "## Rueckfall nach Asset",
        "",
    ]
    for row in by_asset:
        lines.append(
            f"- `{row['name']}`: count `{row['count']}`, Expansion `{_fmt(row['expansion_ratio'])}`, "
            f"Range `{_fmt(row['range_ratio'])}`, Lautheit `{_fmt(row['rand_loudness'])}`, "
            f"Delta Rekopplung `{_fmt(row['delta_follow_rekopplung'])}`, Delta Strain `{_fmt(row['delta_follow_strain'])}`."
        )

    lines.extend(["", "## Rueckfall nach Rohform", ""])
    for row in by_shape:
        lines.append(
            f"- `{row['name']}`: count `{row['count']}`, Assets `{row['asset']}`, Folgehalt `{row['followhold']}`."
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Die Feldantwort ist zweistufig lesbar: erst Entlastung, dann Pruefung des Folgehalts.",
            "",
            "Damit wird ein wichtiger MCM-Mechanismus sichtbar: Nicht jeder entlastende Kontakt ist schon stabile Ordnung.",
            "",
            "## Naechste Pruefung",
            "",
            "Vorwarnspur vor Rueckfall messen: Drift, Nachhall oder schwaecher werdende Rekopplung vor dem erneuten Randkontakt.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Isoliert Rueckfallprofile aus Folgehalt-Rohwelt-Kopplung.")
    parser.add_argument("--input", default=str(DEFAULT_INPUT), help="Folgehalt-Rohwelt-Kopplung CSV.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Markdown-Ausgabe.")
    args = parser.parse_args()

    input_path = _resolve(args.input)
    out_path = _resolve(args.out)
    rows = _load_csv(input_path)
    fallback_rows = [row for row in rows if "rueckfall" in str(row.get("followhold_kind", ""))]
    csv_path = out_path.with_suffix(".csv")
    assessment_path = out_path.with_name("1271_MCM_FOLGEHALT_RUECKFALLPROFIL_BEWERTUNG.md")

    _write_csv(csv_path, fallback_rows)
    _write_markdown(out_path, rows, fallback_rows)
    _write_assessment(assessment_path, fallback_rows)

    print(f"rows={len(rows)} fallback={len(fallback_rows)}")
    print(f"wrote={out_path.relative_to(ROOT)}")
    print(f"wrote={csv_path.relative_to(ROOT)}")
    print(f"wrote={assessment_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
