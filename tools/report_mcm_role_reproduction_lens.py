from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


TARGET_CLASSES = [
    "brueckenpfad",
    "randpfad",
    "junge_oberflaeche",
    "stabile_insel",
    "rekoppelnder_pfad",
    "offener_driftpfad",
]

MATURITY_CLASSES = {"stabile_insel", "rekoppelnder_pfad", "brueckenpfad"}
OPEN_CLASSES = {"offener_driftpfad", "gemischter_pfad"}


def _load(path: Path) -> dict[str, dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return {row.get("token", "-") or "-": row for row in csv.DictReader(handle)}


def _float(row: dict[str, str], key: str) -> float:
    try:
        value = float(row.get(key, "") or 0.0)
    except ValueError:
        return 0.0
    return 0.0 if value != value else value


def _int(row: dict[str, str], key: str) -> int:
    try:
        return int(float(row.get(key, "") or 0))
    except ValueError:
        return 0


def _cls(row: dict[str, str] | None) -> str:
    if not row:
        return "-"
    return row.get("path_class", "-") or "-"


def _relation(first_class: str, second_class: str) -> str:
    if first_class == "-" and second_class != "-":
        return "neu_aufgetaucht"
    if first_class != "-" and second_class == "-":
        return "verschwunden"
    if first_class == second_class:
        return "rollenstabil"
    if first_class == "junge_oberflaeche" and second_class in MATURITY_CLASSES:
        return "junge_spur_reift"
    if first_class in OPEN_CLASSES and second_class in MATURITY_CLASSES:
        return "offenheit_rekoppelt"
    if first_class in MATURITY_CLASSES and second_class in OPEN_CLASSES:
        return "reife_oeffnet"
    if second_class == "randpfad":
        return "wandert_an_rand"
    if first_class == "randpfad":
        return "verlaesst_rand"
    return "rollenwechsel"


def _build_rows(first: dict[str, dict[str, str]], second: dict[str, dict[str, str]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for token in sorted(set(first) | set(second)):
        first_row = first.get(token)
        second_row = second.get(token)
        first_class = _cls(first_row)
        second_class = _cls(second_row)
        relation = _relation(first_class, second_class)
        rows.append(
            {
                "token": token,
                "class_864": first_class,
                "class_868": second_class,
                "relation": relation,
                "movement_864": (first_row or {}).get("movement", "-") or "-",
                "movement_868": (second_row or {}).get("movement", "-") or "-",
                "zone_864": (first_row or {}).get("follow_zone", "-") or "-",
                "zone_868": (second_row or {}).get("follow_zone", "-") or "-",
                "world_delta_864": _int(first_row or {}, "world_delta"),
                "world_delta_868": _int(second_row or {}, "world_delta"),
                "rekopplung_delta_864": _float(first_row or {}, "rekopplung_delta"),
                "rekopplung_delta_868": _float(second_row or {}, "rekopplung_delta"),
                "strain_delta_864": _float(first_row or {}, "strain_delta"),
                "strain_delta_868": _float(second_row or {}, "strain_delta"),
                "loudness_delta_864": _float(first_row or {}, "loudness_delta"),
                "loudness_delta_868": _float(second_row or {}, "loudness_delta"),
                "visual_blur_delta_864": _float(first_row or {}, "visual_blur_delta"),
                "visual_blur_delta_868": _float(second_row or {}, "visual_blur_delta"),
            }
        )
    rows.sort(key=lambda row: (str(row["relation"]), str(row["class_864"]), str(row["class_868"]), str(row["token"])))
    return rows


def _write_csv(rows: list[dict[str, object]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        out.write_text("", encoding="utf-8")
        return
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _tokens(rows: list[dict[str, object]], relation: str | None = None, first_class: str | None = None, second_class: str | None = None) -> list[str]:
    selected = []
    for row in rows:
        if relation is not None and row["relation"] != relation:
            continue
        if first_class is not None and row["class_864"] != first_class:
            continue
        if second_class is not None and row["class_868"] != second_class:
            continue
        selected.append(str(row["token"]))
    return selected


def _class_counts(rows_by_token: dict[str, dict[str, str]]) -> Counter[str]:
    return Counter(_cls(row) for row in rows_by_token.values())


def _write_markdown(
    rows: list[dict[str, object]],
    first: dict[str, dict[str, str]],
    second: dict[str, dict[str, str]],
    out: Path,
) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    first_counts = _class_counts(first)
    second_counts = _class_counts(second)
    relation_counts = Counter(str(row["relation"]) for row in rows)

    stable_bridge = _tokens(rows, relation="rollenstabil", first_class="brueckenpfad", second_class="brueckenpfad")
    stable_edge = _tokens(rows, relation="rollenstabil", first_class="randpfad", second_class="randpfad")
    young_maturing = _tokens(rows, relation="junge_spur_reift", first_class="junge_oberflaeche")
    young_stable = _tokens(rows, relation="rollenstabil", first_class="junge_oberflaeche", second_class="junge_oberflaeche")

    class_transition: dict[str, Counter[str]] = defaultdict(Counter)
    for row in rows:
        if row["class_864"] != "-" and row["class_868"] != "-":
            class_transition[str(row["class_864"])][str(row["class_868"])] += 1

    lines = [
        "# MCM-Rollenreproduktion Lupe",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest nicht mehr die globale Pfadverteilung, sondern die konkrete Rollenwiederkehr einzelner Tokens zwischen `864` und `868`.",
        "Sie prueft passiv, welche Bruecken, Randlagen und jungen Oberflaechen ihre Rolle behalten, wechseln oder nachreifen.",
        "",
        "## Klassenbestand",
        "",
        "| Pfadklasse | 864 | 868 |",
        "|---|---:|---:|",
    ]
    for name in TARGET_CLASSES + ["gemischter_pfad"]:
        if first_counts.get(name, 0) or second_counts.get(name, 0):
            lines.append(f"| {name} | {first_counts.get(name, 0)} | {second_counts.get(name, 0)} |")

    lines.extend(["", "## Rollenbeziehungen", "", "| Beziehung | Anzahl |", "|---|---:|"])
    for relation, count in sorted(relation_counts.items()):
        lines.append(f"| {relation} | {count} |")

    lines.extend(
        [
            "",
            "## Zielrollen",
            "",
            f"- Stabile Brueckenpfade: `{len(stable_bridge)}`",
            f"- Stabile Randpfade: `{len(stable_edge)}`",
            f"- Junge Oberflaechen bleiben jung: `{len(young_stable)}`",
            f"- Junge Oberflaechen reifen in tragendere Rollen: `{len(young_maturing)}`",
            "",
            "### Stabile Brueckenpfade",
            "",
        ]
    )
    if stable_bridge:
        for token in stable_bridge[:20]:
            lines.append(f"- `{token}`")
    else:
        lines.append("- keine")

    lines.extend(["", "### Stabile Randpfade", ""])
    if stable_edge:
        for token in stable_edge[:20]:
            lines.append(f"- `{token}`")
    else:
        lines.append("- keine")

    lines.extend(["", "### Nachreifende Junge Oberflaechen", ""])
    if young_maturing:
        for token in young_maturing[:20]:
            second_class = next(row["class_868"] for row in rows if row["token"] == token)
            lines.append(f"- `{token}` -> `{second_class}`")
    else:
        lines.append("- keine")

    lines.extend(["", "## Klassenuebergaenge", "", "| 864 | 868 | Anzahl |", "|---|---|---:|"])
    for source in sorted(class_transition):
        for target, count in sorted(class_transition[source].items()):
            lines.append(f"| {source} | {target} | {count} |")

    lines.extend(["", "## Befund", ""])
    if stable_edge:
        lines.append(
            "Randrollen bleiben konkret reproduzierbar: dieselben Tokens koennen erneut randnah bleiben. Das stuetzt die Lesart, dass Randnaehe nicht bloss Rauschen ist."
        )
    else:
        lines.append(
            "Randrollen bleiben global selten, aber dieselben Tokens halten den Rand nicht durchgehend. Das wuerde eher fuer situative Randbindung sprechen."
        )

    if stable_bridge:
        lines.append(
            "Brueckenrollen sind nicht nur global stabil, sondern auch teilweise tokenstabil. Das ist ein starker Hinweis auf wiederkehrende Uebergangsfunktionen im MCM-Feld."
        )

    if young_maturing:
        lines.append(
            "Ein Teil junger Oberflaechen reift in stabilere, rekoppelnde oder brueckenartige Rollen. Das passt zur Idee, dass Oberflaeche nicht wertlos ist, sondern Vorform spaeterer Bedeutung sein kann."
        )

    lines.extend(
        [
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die Lupe an den stabilen Brueckenpfaden ansetzen: Welche Weltmerkmale halten diese Bruecken aktiv, und unterscheiden sie sich von jungen Oberflaechen, die nicht nachreifen?",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--first", required=True)
    parser.add_argument("--second", required=True)
    parser.add_argument("--out-md", required=True)
    parser.add_argument("--out-csv", required=True)
    args = parser.parse_args()

    first = _load(Path(args.first))
    second = _load(Path(args.second))
    rows = _build_rows(first, second)
    _write_csv(rows, Path(args.out_csv))
    _write_markdown(rows, first, second, Path(args.out_md))
    print(f"tokens={len(rows)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
