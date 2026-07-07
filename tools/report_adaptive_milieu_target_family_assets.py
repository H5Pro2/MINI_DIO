from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _write_csv(rows: list[dict[str, object]], out_path: Path) -> None:
    csv_path = out_path.with_suffix(".csv")
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        csv_path.write_text("", encoding="utf-8")
        return
    fields = list(rows[0].keys())
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def _build_rows(targets: list[dict[str, str]], asset_rows: list[dict[str, str]]) -> list[dict[str, object]]:
    by_family: dict[str, list[dict[str, str]]] = defaultdict(list)
    by_key: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in asset_rows:
        family = row.get("family", "-")
        transition = row.get("transition", "-")
        by_family[family].append(row)
        by_key[(family, transition)].append(row)

    out: list[dict[str, object]] = []
    for target in targets:
        family = target.get("family", "-")
        transition = target.get("transition", "-")
        exact = by_key.get((family, transition), [])
        family_rows = by_family.get(family, [])
        out.append(
            {
                "family": family,
                "target_transition": transition,
                "target_world": target.get("world", "-"),
                "target_profile": target.get("profile", "-"),
                "exact_asset_hit_count": len(exact),
                "exact_asset_worlds": ", ".join(sorted({row.get("world", "-") for row in exact})) or "-",
                "family_asset_relation_count": len(family_rows),
                "family_asset_transitions": ", ".join(sorted({row.get("transition", "-") for row in family_rows})) or "-",
                "family_asset_worlds": ", ".join(sorted({row.get("world", "-") for row in family_rows})) or "-",
            }
        )
    return out


def _write_md(rows: list[dict[str, object]], asset_rows: list[dict[str, str]], out_path: Path) -> None:
    _write_csv(rows, out_path)
    title_prefix = out_path.stem.split("_", 1)[0]
    title = f"# {title_prefix} - Ziel-Familien gegen Assetfenster" if title_prefix.isdigit() else "# Ziel-Familien gegen Assetfenster"
    exact_hits = sum(1 for row in rows if int(row["exact_asset_hit_count"]) > 0)
    family_hits = sum(1 for row in rows if int(row["family_asset_relation_count"]) > 0)
    transitions = Counter(row.get("transition", "-") for row in asset_rows)

    lines = [
        title,
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft die `milieu_umlagert_nahe`-Familien aus 1697 gegen andere Assetfenster.",
        "Sie bleibt passiv: keine Handlung, kein Gate, keine Richtung.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Kehren innerfeldnahe Milieu-Umlagerungen in anderen Welten wieder?",
        "2. Unterpruefung: Gleiche Familie plus gleiche Wechselrichtung gegen BTC, DOGE, XRP und PAXG pruefen.",
        "3. Folgeschritt: Exakte Treffer als robuste Kandidaten tiefer gegen Rohweltfenster lesen.",
        "",
        "## Uebersicht",
        "",
        f"- Zielzeilen aus 1697: `{len(rows)}`",
        f"- Exakte Asset-Treffer: `{exact_hits}`",
        f"- Ziel-Familien mit irgendeinem Asset-Relationswechsel: `{family_hits}`",
        f"- Asset-Relationswechsel gesamt: `{len(asset_rows)}`",
        "",
        "## Asset-Relationswechsel gesamt",
        "",
        "| Wechsel | Anzahl |",
        "|---|---:|",
    ]
    for transition, count in sorted(transitions.items()):
        lines.append(f"| {transition} | {count} |")

    lines.extend(
        [
            "",
            "## Ziel-Familien",
            "",
            "| Familie | Zielwechsel | Zielwelt | Exakte Asset-Treffer | Asset-Welten | Familienwechsel in Assets |",
            "|---|---|---|---:|---|---|",
        ]
    )
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["family"]),
                    str(row["target_transition"]),
                    str(row["target_world"]),
                    str(row["exact_asset_hit_count"]),
                    str(row["exact_asset_worlds"]),
                    str(row["family_asset_transitions"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Drei der fuenf Zielzeilen zeigen gleiche Familie plus gleiche Wechselrichtung in anderen Assetfenstern.",
            "Das ist kein Beweis fuer eine feste Bedeutung, aber ein staerkerer Hinweis als reine Namensgleichheit.",
            "",
            "`dio_0ly7` und `dio_01hu` sind aktuell die interessantesten Kandidaten, weil sie die gleiche Bewegung `nur_gereift -> offen_und_gereift` ausserhalb der 2023-Pruefung erneut zeigen.",
            "",
            "`dio_0dd2` taucht zwar in Assets auf, aber mit Gegenrichtung. `dio_10dv` taucht in dieser Assetpruefung nicht auf.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollten `dio_0ly7` und `dio_01hu` als robuste Kandidaten gegen ihre Asset-Rohweltfenster gelesen werden: Welche Weltspannung, Hoerform und Feldspannung liegen direkt vor der erneuten Oeffnung?",
            "",
        ]
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Prueft nahe Milieu-Umlagerungsfamilien gegen Asset-Relationswechsel.")
    parser.add_argument("--target-csv", required=True)
    parser.add_argument("--asset-relation-csv", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    targets = [row for row in _load_csv(_resolve(args.target_csv)) if row.get("profile") == "milieu_umlagert_nahe"]
    asset_rows = _load_csv(_resolve(args.asset_relation_csv))
    rows = _build_rows(targets, asset_rows)
    _write_md(rows, asset_rows, _resolve(args.out_md))
    print(
        {
            "out_md": str(_resolve(args.out_md)),
            "targets": len(rows),
            "exact_hits": sum(1 for row in rows if int(row["exact_asset_hit_count"]) > 0),
            "family_hits": sum(1 for row in rows if int(row["family_asset_relation_count"]) > 0),
        }
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
