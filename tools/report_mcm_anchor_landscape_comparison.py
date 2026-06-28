from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


def _read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def _int(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def _float(value: str) -> float:
    try:
        return float(value or 0.0)
    except ValueError:
        return 0.0


def _profile(rows: list[dict[str, str]]) -> dict[str, object]:
    class_counts = Counter(row.get("anchor_class", "-") for row in rows)
    strong = [row for row in rows if row.get("anchor_class") == "starker_anschlussanker"]
    cores = [row for row in rows if row.get("anchor_class") == "brueckenkern"]
    locals_ = [row for row in rows if row.get("anchor_class") == "lokaler_anschlussanker"]
    return {
        "total": len(rows),
        "class_counts": class_counts,
        "strong": sorted(strong, key=lambda row: _int(row.get("total_weight", "0")), reverse=True),
        "cores": sorted(cores, key=lambda row: _int(row.get("total_weight", "0")), reverse=True),
        "locals": sorted(locals_, key=lambda row: _int(row.get("total_weight", "0")), reverse=True),
    }


def _short(row: dict[str, str]) -> str:
    return row.get("short_token") or row.get("token", "").replace("dio_mcm_episode_", "")


def _class_line(counter: Counter[str]) -> str:
    return "; ".join(f"{name}:{count}" for name, count in counter.most_common())


def _token_table(rows: list[dict[str, str]], limit: int = 8) -> list[str]:
    lines = ["| Token | Klasse | Gewicht | Welten | Dauer | Pfadklasse | Bewegung |", "|---|---|---:|---:|---:|---|---|"]
    for row in rows[:limit]:
        lines.append(
            f"| `{_short(row)}` | {row.get('anchor_class', '-')} | {row.get('total_weight', '0')} | {row.get('max_world_span', '0')} | {_float(row.get('weighted_duration', '0')):.2f} | {row.get('path_class', '-')} | {row.get('movement', '-')} |"
        )
    return lines


def _write_md(path: Path, base_rows: list[dict[str, str]], compare_rows: list[dict[str, str]]) -> None:
    base = _profile(base_rows)
    compare = _profile(compare_rows)
    base_tokens = {row.get("token", "") for row in base_rows}
    compare_tokens = {row.get("token", "") for row in compare_rows}
    overlap = base_tokens & compare_tokens

    lines: list[str] = []
    lines.append("# MCM-Anschlussanker Landschaftsvergleich")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append("Diese Diagnose vergleicht die moderne Anschlussanker-Landschaft aus 894 mit einer zweiten, nach gleicher Pipeline erzeugten Vergleichsgruppe aus 864/898/899/900/901.")
    lines.append("Damit wird Rollenanalogie durch echte Netzwerk-Topologie ergaenzt.")
    lines.append("")
    lines.append("## Gesamtvergleich")
    lines.append("")
    lines.append("| Landschaft | Tokens | Klassenprofil | Starke Anschlussanker | Brueckenkerne | Lokale Anschlussanker |")
    lines.append("|---|---:|---|---:|---:|---:|")
    lines.append(
        f"| 894 | {base['total']} | {_class_line(base['class_counts'])} | {len(base['strong'])} | {len(base['cores'])} | {len(base['locals'])} |"
    )
    lines.append(
        f"| 901 | {compare['total']} | {_class_line(compare['class_counts'])} | {len(compare['strong'])} | {len(compare['cores'])} | {len(compare['locals'])} |"
    )
    lines.append("")
    lines.append(f"- Token-Ueberlappung: `{len(overlap)}`")
    lines.append("")
    lines.append("## Staerkste Rollen In 894")
    lines.append("")
    lines.extend(_token_table(base["cores"][:5] + base["strong"][:5]))
    lines.append("")
    lines.append("## Staerkste Rollen In 901")
    lines.append("")
    lines.extend(_token_table(compare["cores"][:8] + compare["strong"][:4]))
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append("Die Anschlussanker-Familien tauchen in der Vergleichsgruppe nicht einfach identisch auf, sondern verschieben ihre Rolle.")
    lines.append("")
    lines.append("- In 894 wirkt `0b7nep9` als starker verteilender Anschlussanker.")
    lines.append("- In 901 ist `0b7nep9` Teil der Kernlandschaft und koppelt stark mit `0ykar6i`.")
    lines.append("- `1jx2k4i` war in 894 kernnaher Inselanker; in 901 liegt es ebenfalls im Brueckenkernbereich.")
    lines.append("")
    lines.append("Das ist ein wichtiger Befund: dieselben Feldzeichen koennen unter anderer Weltgruppe von Anschlussrolle in Kernrolle wandern.")
    lines.append("Damit wird die MCM-Topologie nicht als starres Koordinatensystem gelesen, sondern als dynamische Feldordnung.")
    lines.append("")
    lines.append("## Konsequenz")
    lines.append("")
    lines.append("Die letzten Untersuchungen stuetzen drei Punkte:")
    lines.append("")
    lines.append("1. Anschlussanker sind reproduzierbare Rollenformen.")
    lines.append("2. Diese Rollen haben Unterfamilien: kernnah, verteilend, uebergangsartig.")
    lines.append("3. Rollen koennen zwischen Weltgruppen wandern: ein Anschlussanker kann in einer anderen Weltgruppe zum Kernbestandteil werden.")
    lines.append("")
    lines.append("Das spricht fuer eine lebendige Topologie: stabil genug, um wiederkehrende Rollen zu zeigen, aber flexibel genug, um Rollen je nach Weltspannung anders zu organisieren.")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    lines.append("Als naechstes sollte genau diese Rollenwanderung untersucht werden: Welche Weltmerkmale lassen `0b7nep9` vom verteilenden Anschlussanker zum Kernpartner von `0ykar6i` werden?")
    path.write_text("\n".join(lines), encoding="utf-8")


def _write_csv(path: Path, base_rows: list[dict[str, str]], compare_rows: list[dict[str, str]]) -> None:
    rows: list[dict[str, str]] = []
    by_token: dict[str, dict[str, str]] = {}
    for row in base_rows:
        by_token.setdefault(row.get("token", ""), {})["base_class"] = row.get("anchor_class", "-")
        by_token.setdefault(row.get("token", ""), {})["base_weight"] = row.get("total_weight", "0")
        by_token.setdefault(row.get("token", ""), {})["base_duration"] = row.get("weighted_duration", "0")
        by_token.setdefault(row.get("token", ""), {})["short_token"] = _short(row)
    for row in compare_rows:
        by_token.setdefault(row.get("token", ""), {})["compare_class"] = row.get("anchor_class", "-")
        by_token.setdefault(row.get("token", ""), {})["compare_weight"] = row.get("total_weight", "0")
        by_token.setdefault(row.get("token", ""), {})["compare_duration"] = row.get("weighted_duration", "0")
        by_token.setdefault(row.get("token", ""), {})["short_token"] = _short(row)
    for token, data in by_token.items():
        rows.append(
            {
                "token": token,
                "short_token": data.get("short_token", token.replace("dio_mcm_episode_", "")),
                "base_class": data.get("base_class", "-"),
                "compare_class": data.get("compare_class", "-"),
                "base_weight": data.get("base_weight", "0"),
                "compare_weight": data.get("compare_weight", "0"),
                "base_duration": data.get("base_duration", "0"),
                "compare_duration": data.get("compare_duration", "0"),
                "role_changed": "1" if data.get("base_class", "-") != data.get("compare_class", "-") else "0",
            }
        )
    rows.sort(key=lambda row: (-_int(row["role_changed"]), row["short_token"]))
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True, type=Path)
    parser.add_argument("--compare", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    base_rows = _read(args.base)
    compare_rows = _read(args.compare)
    _write_csv(args.out_csv, base_rows, compare_rows)
    _write_md(args.out_md, base_rows, compare_rows)
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
