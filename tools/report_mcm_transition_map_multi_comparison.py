from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAPS_DEFAULT = [
    ROOT / "docs" / "befunde" / "819_BLOCK_K_MCM_UEBERGANGSKARTE.csv",
    ROOT / "docs" / "befunde" / "822_BLOCK_K_ZWEITE_MCM_UEBERGANGSKARTE.csv",
    ROOT / "docs" / "befunde" / "826_BLOCK_K_DRITTE_MCM_UEBERGANGSKARTE.csv",
]
CSV_DEFAULT = ROOT / "docs" / "befunde" / "827_BLOCK_K_DREI_MCM_UEBERGANGSKARTEN_VERGLEICH.csv"
MD_DEFAULT = ROOT / "docs" / "befunde" / "827_BLOCK_K_DREI_MCM_UEBERGANGSKARTEN_VERGLEICH.md"


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle, delimiter=";")]


def _safe_int(value: object, default: int = 0) -> int:
    try:
        return int(float(value))
    except Exception:
        return default


def _map_label(path: Path) -> str:
    return path.stem.split("_", 1)[0]


def _edge_family(rows: list[dict[str, str]]) -> str:
    for row in rows:
        if row.get("map_role") == "randfamilie":
            return str(row.get("family") or "-")
    return "-"


def build_rows(paths: list[Path]) -> tuple[list[dict[str, object]], dict[str, object]]:
    maps = []
    role_counts: dict[str, Counter[str]] = {}
    family_roles: dict[str, dict[str, str]] = defaultdict(dict)
    family_hits: dict[str, dict[str, int]] = defaultdict(dict)
    edge_families: dict[str, str] = {}
    for path in paths:
        label = _map_label(path)
        rows = _read_csv(path)
        maps.append((label, path, rows))
        role_counts[label] = Counter(str(row.get("map_role") or "-") for row in rows)
        edge_families[label] = _edge_family(rows)
        for row in rows:
            family = str(row.get("family") or "-")
            family_roles[family][label] = str(row.get("map_role") or "-")
            family_hits[family][label] = _safe_int(row.get("hits"))
    labels = [label for label, _, _ in maps]
    rows_out: list[dict[str, object]] = []
    for family in sorted(family_roles):
        roles = family_roles[family]
        present = len(roles)
        role_values = [roles.get(label, "-") for label in labels]
        unique_roles = {role for role in role_values if role != "-"}
        if present == len(labels) and len(unique_roles) == 1:
            relation = "kartenuebergreifend_rollenstabil"
        elif present >= 2 and len(unique_roles) == 1:
            relation = "teilweise_rollenstabil"
        elif present >= 2:
            relation = "rollenverschiebung"
        else:
            relation = "lokal"
        row: dict[str, object] = {
            "family": family,
            "relation": relation,
            "present_in_maps": present,
        }
        for label in labels:
            row[f"role_{label}"] = roles.get(label, "-")
            row[f"hits_{label}"] = family_hits[family].get(label, 0)
        rows_out.append(row)
    summary = {
        "labels": labels,
        "role_counts": role_counts,
        "relation_counts": Counter(str(row["relation"]) for row in rows_out),
        "edge_families": edge_families,
    }
    return rows_out, summary


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(path: Path, rows: list[dict[str, object]], summary: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    labels: list[str] = summary["labels"]  # type: ignore[assignment]
    role_counts: dict[str, Counter[str]] = summary["role_counts"]  # type: ignore[assignment]
    relation_counts: Counter[str] = summary["relation_counts"]  # type: ignore[assignment]
    edge_families: dict[str, str] = summary["edge_families"]  # type: ignore[assignment]
    report_id = path.stem.split("_", 1)[0]
    all_roles = [
        "randfamilie",
        "vorfeldanker",
        "beidseitige_bruecke",
        "nachfeldanker",
        "instabile_kontaktzone",
        "offene_bruecke",
        "offene_kontaktzone",
        "randnahe_unruhe",
    ]
    lines = [
        f"# {report_id} - Block-K MCM-Uebergangskarten-Vergleich",
        "",
        "## Fragestellung",
        "",
        "Welche Rollen bleiben ueber mehrere Randfamilienkarten erhalten, und welche Rollen veraendern sich lokal?",
        "",
        "## Karten",
        "",
        "| Karte | Randfamilie |",
        "|---|---|",
    ]
    for label in labels:
        lines.append(f"| {label} | `{edge_families.get(label, '-')}` |")
    lines.extend(["", "## Rollenzaehlung", "", "| Rolle | " + " | ".join(labels) + " |", "|---|" + "---:|" * len(labels)])
    for role in all_roles:
        values = " | ".join(str(role_counts[label].get(role, 0)) for label in labels)
        lines.append(f"| {role} | {values} |")
    lines.extend(["", "## Familienrelationen", "", "| Relation | Anzahl |", "|---|---:|"])
    for relation, count in relation_counts.most_common():
        lines.append(f"| {relation} | {count} |")
    header = "| Familie | Relation | Vorkommen | " + " | ".join(f"Rolle {label}" for label in labels) + " |"
    separator = "|---|---|---:|" + "---|" * len(labels)
    lines.extend(["", "## Familienmatrix", "", header, separator])
    priority = {
        "kartenuebergreifend_rollenstabil": 0,
        "teilweise_rollenstabil": 1,
        "rollenverschiebung": 2,
        "lokal": 3,
    }
    for row in sorted(rows, key=lambda item: (priority.get(str(item["relation"]), 9), -int(item["present_in_maps"]), str(item["family"]))):
        roles = " | ".join(str(row.get(f"role_{label}", "-")) for label in labels)
        lines.append(f"| {row['family']} | {row['relation']} | {row['present_in_maps']} | {roles} |")
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Karten behalten dieselbe Grundordnung: Randfamilie, Bruecken, offene Anschlussbereiche und randnahe Unruhe. Die Gewichtung verschiebt sich je nach Randfamilie und Weltspannung, aber die Rollenarchitektur bleibt lesbar.",
            "",
            "Damit wird die Topologie nicht als starres Bild gelesen. Stabil wirkt die Rollenarchitektur; beweglich bleiben die lokalen Familienrollen und ihre Belastungsnaehe.",
            "",
            "## Grenze",
            "",
            "Das ist ein passiver Strukturvergleich. Er beschreibt keine Handlung und keine Vorhersage.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die Veraenderung der Rollenanteile genauer gegen die Weltspannung gelesen werden. Dann wird sichtbar, welche Aussenweltmerkmale offene Bruecken, instabile Kontaktzonen oder randnahe Unruhe verstaerken.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--maps", nargs="+", type=Path, default=MAPS_DEFAULT)
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    args = parser.parse_args()
    rows, summary = build_rows(args.maps)
    _write_csv(args.csv_out, rows)
    _write_markdown(args.md_out, rows, summary)
    print(f"maps={len(args.maps)}")
    print(f"rows={len(rows)}")
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    relation_counts: Counter[str] = summary["relation_counts"]  # type: ignore[assignment]
    for relation, count in relation_counts.most_common():
        print(f"{relation}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
