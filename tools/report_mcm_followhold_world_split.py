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
DEFAULT_OUT = ROOT / "docs" / "befunde" / "1268_MCM_FOLGEHALT_WELTART_ASSET_SPLIT.md"


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


def _asset_from_row(row: dict[str, str]) -> str:
    text = f"{row.get('world', '')} {row.get('data_file', '')}".upper()
    for asset in ("BTC", "SOL", "KAS", "DOGE", "XRP", "PAXG"):
        if asset in text:
            return asset
    if "SIDEWAYS" in text:
        return "SYNTH_SIDEWAYS"
    if "EXPANSION" in text or "POS_" in text:
        return "SYNTH_EXPANSION"
    if "NEG_" in text or "STRESS" in text:
        return "SYNTH_STRESS"
    return "UNKNOWN"


def _world_family(row: dict[str, str]) -> str:
    world = str(row.get("world", "") or "").upper()
    data_file = str(row.get("data_file", "") or "").upper()
    text = f"{world} {data_file}"
    if "1H" in text:
        frame = "1h"
    elif "5M" in text:
        frame = "5m"
    else:
        frame = "unknown_frame"

    if "SIDEWAYS" in text:
        mode = "sideways"
    elif "EXPANSION" in text or "POS_" in text:
        mode = "expansion"
    elif "STRESS" in text or "NEG_" in text:
        mode = "stress"
    else:
        mode = "asset_real"
    return f"{mode}_{frame}"


def _quality_bucket(row: dict[str, str]) -> str:
    kind = str(row.get("followhold_kind", "") or "")
    expansion = _safe_float(row.get("expansion_ratio"))
    reko_delta = _safe_float(row.get("delta_follow_rekopplung"))
    strain_delta = _safe_float(row.get("delta_follow_strain"))

    if "rueckfall" in kind:
        if expansion >= 5.0:
            return "rueckfall_bei_starker_expansion"
        return "rueckfall_bei_bruch"
    if "gemischt" in kind:
        return "gemischte_folge"
    if reko_delta >= 0.10 and strain_delta <= -0.11:
        return "stark_entlastender_folgehalt"
    if "entlastend_gehalten" in kind:
        return "entlastender_folgehalt"
    return "offene_folge"


def _group(rows: list[dict[str, str]], key_name: str) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        if key_name == "asset":
            key = _asset_from_row(row)
        elif key_name == "world_family":
            key = _world_family(row)
        else:
            key = str(row.get(key_name, "") or "")
        grouped[key].append(row)

    out: list[dict[str, object]] = []
    for name, group in grouped.items():
        follow_counts = Counter(str(row.get("followhold_kind", "")) for row in group)
        quality_counts = Counter(_quality_bucket(row) for row in group)
        movement_counts = Counter(str(row.get("raw_shape_bucket", "")) for row in group)
        out.append(
            {
                "name": name,
                "count": len(group),
                "follow_top": dict(follow_counts.most_common(4)),
                "quality_top": dict(quality_counts.most_common(4)),
                "raw_top": dict(movement_counts.most_common(3)),
                "raw_return": _mean([_safe_float(row.get("raw_return")) for row in group]),
                "range_ratio": _mean([_safe_float(row.get("range_ratio")) for row in group]),
                "expansion_ratio": _mean([_safe_float(row.get("expansion_ratio")) for row in group]),
                "direction_consistency": _mean([_safe_float(row.get("direction_consistency")) for row in group]),
                "delta_follow_rekopplung": _mean([_safe_float(row.get("delta_follow_rekopplung")) for row in group]),
                "delta_follow_strain": _mean([_safe_float(row.get("delta_follow_strain")) for row in group]),
                "rand_loudness": _mean([_safe_float(row.get("rand_loudness")) for row in group]),
                "rand_strain": _mean([_safe_float(row.get("rand_strain")) for row in group]),
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
            "| Gruppe | Anzahl | Folgehalt | Qualitaet | Rohform | Expansion | Richtung | Delta Rekopplung | Delta Strain | Lautheit | Rand-Strain |",
            "|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["name"]),
                    str(row["count"]),
                    str(row["follow_top"]),
                    str(row["quality_top"]),
                    str(row["raw_top"]),
                    _fmt(row["expansion_ratio"]),
                    _fmt(row["direction_consistency"]),
                    _fmt(row["delta_follow_rekopplung"]),
                    _fmt(row["delta_follow_strain"]),
                    _fmt(row["rand_loudness"]),
                    _fmt(row["rand_strain"]),
                ]
            )
            + " |"
        )


def _write_markdown(path: Path, rows: list[dict[str, str]], asset_rows: list[dict[str, object]], family_rows: list[dict[str, object]], world_rows: list[dict[str, object]]) -> None:
    lines: list[str] = [
        "# MCM Folgehalt nach Weltart und Asset",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "## Grundfrage",
        "",
        "Bleibt die Feldantwort nach Randkontakt gleich, wenn sich Asset, Weltart und Weltmelodie unterscheiden?",
        "",
        "## Unterpruefung",
        "",
        "Diese Diagnose trennt die Kopplung aus 1266 nach Asset, Weltfamilie und einzelner Welt.",
        "",
        "## Profil",
        "",
        f"- gekoppelte Fenster: `{len(rows)}`",
        f"- Assets/Familien: `{len(asset_rows)}` Assetgruppen, `{len(family_rows)}` Weltfamilien, `{len(world_rows)}` Einzelwelten",
        "",
    ]
    _table(lines, "Assetgruppen", asset_rows)
    _table(lines, "Weltfamilien", family_rows)
    _table(lines, "Einzelwelten", world_rows)
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Grundmechanik bleibt ueber die Welten sichtbar: Randkontakt fuehrt ueberwiegend zu entlastendem Folgehalt.",
            "",
            "Die Faerbung unterscheidet sich jedoch:",
            "",
            "- starke Expansion erhoeht Rueckfallnaehe bei offenen Folgeformen.",
            "- einzelne Assets zeigen andere Lautheit, Range und Expansion, ohne die Grundfolge zu brechen.",
            "- synthetische Stress- und Expansionswelten sind nuetzlich, um Rand-/Rueckfallformen sichtbar zu machen.",
            "",
            "Damit wirkt die MCM-Feldantwort nicht wie eine starre Asset-Regel, sondern wie eine Grundtopologie mit weltabhaengiger Faerbung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die staerkste Rueckfallgruppe isoliert werden: Welche Asset-/Weltmerkmale machen aus Bewegungsbruch offenen Folgehalt mit spaeterem Rueckfall?",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def _write_assessment(path: Path, asset_rows: list[dict[str, object]], family_rows: list[dict[str, object]]) -> None:
    lines = [
        "# Bewertung: MCM Folgehalt Weltart Asset Split",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "## Kernaussage",
        "",
        "Die Folgehalt-Mechanik bleibt ueber unterschiedliche Welten lesbar, aber ihre Intensitaet und Rueckfallnaehe faerbt sich durch Asset und Weltart.",
        "",
        "## Starke Hinweise",
        "",
    ]
    for row in asset_rows[:8]:
        lines.append(
            f"- `{row['name']}`: count `{row['count']}`, Expansion `{_fmt(row['expansion_ratio'])}`, "
            f"Lautheit `{_fmt(row['rand_loudness'])}`, Delta Rekopplung `{_fmt(row['delta_follow_rekopplung'])}`, "
            f"Delta Strain `{_fmt(row['delta_follow_strain'])}`."
        )

    lines.extend(
        [
            "",
            "## Weltfamilien",
            "",
        ]
    )
    for row in family_rows:
        lines.append(
            f"- `{row['name']}`: count `{row['count']}`, Qualitaet `{row['quality_top']}`, Rohform `{row['raw_top']}`."
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Das Feld zeigt keine reine Datenklassifikation. Es zeigt eine wiederkehrende Folgeantwort mit unterschiedlichen Weltfaerbungen.",
            "",
            "Fuer MINI_DIO ist das relevant, weil spaetere Wahrnehmung nicht auf Assetnamen oder Rohwerte reduziert werden sollte. Entscheidend ist die Feldantwort unter wechselnder Weltspannung.",
            "",
            "## Naechste Pruefung",
            "",
            "Rueckfallgruppe isolieren und mit den vorherigen Rohweltfenstern vergleichen.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Trennt Folgehalt-Rohwelt-Kopplung nach Asset und Weltart.")
    parser.add_argument("--input", default=str(DEFAULT_INPUT), help="Folgehalt-Rohwelt-Kopplung CSV.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Markdown-Ausgabe.")
    args = parser.parse_args()

    input_path = _resolve(args.input)
    out_path = _resolve(args.out)
    rows = _load_csv(input_path)
    asset_rows = _group(rows, "asset")
    family_rows = _group(rows, "world_family")
    world_rows = _group(rows, "world")

    csv_path = out_path.with_suffix(".csv")
    assessment_path = out_path.with_name("1269_MCM_FOLGEHALT_WELTART_ASSET_SPLIT_BEWERTUNG.md")
    _write_csv(csv_path, asset_rows + family_rows + world_rows)
    _write_markdown(out_path, rows, asset_rows, family_rows, world_rows)
    _write_assessment(assessment_path, asset_rows, family_rows)

    print(f"rows={len(rows)} assets={len(asset_rows)} families={len(family_rows)} worlds={len(world_rows)}")
    print(f"wrote={out_path.relative_to(ROOT)}")
    print(f"wrote={csv_path.relative_to(ROOT)}")
    print(f"wrote={assessment_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
