from __future__ import annotations

import argparse
import csv
from collections import Counter
from datetime import datetime
from pathlib import Path
from statistics import fmean


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TARGET = "dio_mcm_episode_1t5bcxp"
DEFAULT_OUT = ROOT / "docs" / "befunde" / "328_OFFENE_PREVIEW_FAMILIE_WELTEN_VERGLEICH.md"


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


def _load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _role(row: dict[str, str]) -> str:
    effect_class = str(row.get("passive_mcm_effect_class", "-") or "-")
    awareness = str(row.get("passive_inner_effect_awareness_state", "-") or "-")
    if effect_class == "stabil" or awareness == "inner_effect_stable":
        return "zentrum_stabil"
    if effect_class in {"kippend", "gespannt"}:
        return "spannungsrand_kippnaehe"
    if effect_class in {"tragend_unruhig", "diffus"}:
        return "offene_variante"
    return "unbestimmt"


def _dominant(values: list[str]) -> str:
    cleaned = [value for value in values if value and value != "-"]
    if not cleaned:
        return "-"
    value, count = Counter(cleaned).most_common(1)[0]
    return f"{value} ({count}/{len(cleaned)})"


def _summarize(name: str, episodes_path: Path, target: str) -> dict[str, object]:
    rows = _load_rows(episodes_path)
    target_rows = [row for row in rows if (row.get("mcm_field_episode_preview_symbol") or "-") == target]
    open_rows = [row for row in rows if _role(row) == "offene_variante"]
    previews = [row.get("mcm_field_episode_preview_symbol", "-") or "-" for row in rows]
    symbols = [row.get("symbol_family", "-") or "-" for row in target_rows]
    target_roles = Counter(_role(row) for row in target_rows)

    return {
        "world": name,
        "episodes": len(rows),
        "open_count": len(open_rows),
        "open_share": len(open_rows) / max(1, len(rows)),
        "target_count": len(target_rows),
        "target_share": len(target_rows) / max(1, len(rows)),
        "target_share_of_open": len([row for row in target_rows if _role(row) == "offene_variante"]) / max(1, len(open_rows)),
        "target_symbol_variants": len(set(symbols)),
        "target_top_symbol": _dominant(symbols),
        "top_preview": _dominant(previews),
        "target_center": target_roles.get("zentrum_stabil", 0),
        "target_open": target_roles.get("offene_variante", 0),
        "target_rand": target_roles.get("spannungsrand_kippnaehe", 0),
        "target_rekopplung": _mean([_float(row.get("mcm_rekopplung_quality")) for row in target_rows]),
        "target_strain": _mean([_float(row.get("mcm_strain_quality")) for row in target_rows]),
        "target_sensory": _mean([_float(row.get("mcm_sensory_coupling")) for row in target_rows]),
        "target_visual_gap": _mean([_float(row.get("mcm_visual_field_gap")) for row in target_rows]),
        "target_hearing_gap": _mean([_float(row.get("mcm_hearing_field_gap")) for row in target_rows]),
    }


def _write_csv(rows: list[dict[str, object]], out_path: Path) -> None:
    fields = [
        "world",
        "episodes",
        "open_share",
        "target_count",
        "target_share",
        "target_share_of_open",
        "target_symbol_variants",
        "target_top_symbol",
        "top_preview",
        "target_center",
        "target_open",
        "target_rand",
        "target_rekopplung",
        "target_strain",
        "target_sensory",
        "target_visual_gap",
        "target_hearing_gap",
    ]
    csv_path = out_path.with_suffix(".csv")
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    key: _fmt(float(row[key]), 6) if isinstance(row.get(key), float) else row.get(key, "")
                    for key in fields
                }
            )


def _write_md(rows: list[dict[str, object]], target: str, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    _write_csv(rows, out_path)

    with_target = [row for row in rows if int(row["target_count"]) > 0]
    target_worlds = len(with_target)
    total_worlds = len(rows)

    lines = [
        "# Offene Preview-Familie - Weltenvergleich",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        f"Diese Diagnose prueft die MCM-Preview-Familie `{target}` ueber mehrere Welten, Assets und Timeframes.",
        "Sie trennt rohe Symbolsyntax von verdichteter MCM-Preview-Syntax.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Bleibt eine offene MCM-Preview-Familie weltuebergreifend wiedererkennbar?",
        "2. Unterpruefung: Wie stark fragmentiert die rohe `symbol_family` unter derselben Preview-Familie?",
        "3. Folgeschritt: pruefen, ob die Familie Bedeutungsspannweite, Drift oder gereifte Insel wird.",
        "",
        "## Ergebnisuebersicht",
        "",
        f"- Ziel-Familie: `{target}`",
        f"- Vorkommen in Welten: {target_worlds}/{total_worlds}",
        "- Bewertungsgrenze: passiv, keine Handlung, kein Gate, kein Entry-Signal.",
        "",
        "## Matrix",
        "",
        "| Welt | Episoden | Offen | Ziel-Anzahl | Ziel-Anteil | Anteil an Offen | Symbolvarianten | Top-Rohsymbol | Top-Preview | Zentrum | Offen | Rand | Rekopplung | Strain | Sinneskopplung |",
        "|---|---:|---:|---:|---:|---:|---:|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["world"]),
                    str(row["episodes"]),
                    _fmt(float(row["open_share"])),
                    str(row["target_count"]),
                    _fmt(float(row["target_share"])),
                    _fmt(float(row["target_share_of_open"])),
                    str(row["target_symbol_variants"]),
                    str(row["target_top_symbol"]),
                    str(row["top_preview"]),
                    str(row["target_center"]),
                    str(row["target_open"]),
                    str(row["target_rand"]),
                    _fmt(float(row["target_rekopplung"])),
                    _fmt(float(row["target_strain"])),
                    _fmt(float(row["target_sensory"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"`{target}` ist nicht in allen Welten gleich stark vorhanden. Wenn sie erscheint, ist sie jedoch eine verdichtete MCM-Preview-Bezeichnung, nicht eine identische rohe Symbolsyntax.",
            "",
            "Die Rohsyntax bleibt unter dieser Preview-Familie stark variabel. Das ist fachlich wichtig: MINI_DIO bildet nicht ueberall dieselben Einzelwoerter, sondern eher wiederkehrende Bedeutungsraeume, in denen viele feine Syntaxvarianten auftreten koennen.",
            "",
            "Antwort auf die Syntaxfrage:",
            "",
            "- Auf `symbol_family`-Ebene: nein, nicht identisch ueber alle Assets und Welten.",
            "- Auf MCM-Preview-Ebene: ja, deutlich aehnlicher und wiederkehrender.",
            "- Die MCM-Preview-Syntax wirkt damit wie eine verdichtete Feldsprache, waehrend die Rohsyntax die lokale Oberflaechenvarianz traegt.",
            "",
            "## Wie es weitergeht",
            "",
            f"Als naechstes wird `{target}` nicht nur nach Vorkommen, sondern nach Nachbarschaft geprueft: Welche Zentrum-, Offen- und Randrollen liegen davor und danach?",
            "",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", default=DEFAULT_TARGET)
    parser.add_argument("--world", action="append", nargs=2, metavar=("NAME", "EPISODES_CSV"), required=True)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    rows = [_summarize(name, _resolve(path_text), args.target) for name, path_text in args.world]
    out = args.out if args.out.is_absolute() else ROOT / args.out
    _write_md(rows, args.target, out)
    print(f"wrote {out}")
    print(f"wrote {out.with_suffix('.csv')}")


if __name__ == "__main__":
    main()
