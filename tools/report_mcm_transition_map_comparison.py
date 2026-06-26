from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAP_A_DEFAULT = ROOT / "docs" / "befunde" / "819_BLOCK_K_MCM_UEBERGANGSKARTE.csv"
MAP_B_DEFAULT = ROOT / "docs" / "befunde" / "822_BLOCK_K_ZWEITE_MCM_UEBERGANGSKARTE.csv"
CSV_DEFAULT = ROOT / "docs" / "befunde" / "823_BLOCK_K_MCM_UEBERGANGSKARTEN_VERGLEICH.csv"
MD_DEFAULT = ROOT / "docs" / "befunde" / "823_BLOCK_K_MCM_UEBERGANGSKARTEN_VERGLEICH.md"


def _safe_float(value: object, default: float = 0.0) -> float:
    try:
        result = float(value)
    except Exception:
        return default
    if result != result:
        return default
    return result


def _safe_int(value: object, default: int = 0) -> int:
    try:
        return int(float(value))
    except Exception:
        return default


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle, delimiter=";")]


def _fmt(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def _map_by_family(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {str(row.get("family") or "-"): row for row in rows}


def build_comparison_rows(map_a: Path, map_b: Path) -> tuple[list[dict[str, object]], dict[str, object]]:
    rows_a = _read_csv(map_a)
    rows_b = _read_csv(map_b)
    by_a = _map_by_family(rows_a)
    by_b = _map_by_family(rows_b)
    families = sorted(set(by_a) | set(by_b))
    comparison: list[dict[str, object]] = []
    for family in families:
        left = by_a.get(family, {})
        right = by_b.get(family, {})
        role_a = str(left.get("map_role") or "-")
        role_b = str(right.get("map_role") or "-")
        hits_a = _safe_int(left.get("hits")) if left else 0
        hits_b = _safe_int(right.get("hits")) if right else 0
        stable_a = _safe_float(left.get("stable_share")) if left else 0.0
        stable_b = _safe_float(right.get("stable_share")) if right else 0.0
        unrest_a = _safe_float(left.get("unrest_share")) if left else 0.0
        unrest_b = _safe_float(right.get("unrest_share")) if right else 0.0
        strain_a = _safe_float(left.get("avg_strain")) if left else 0.0
        strain_b = _safe_float(right.get("avg_strain")) if right else 0.0
        trust_a = _safe_float(left.get("avg_trust")) if left else 0.0
        trust_b = _safe_float(right.get("avg_trust")) if right else 0.0
        present_a = bool(left)
        present_b = bool(right)
        if present_a and present_b and role_a == role_b:
            relation = "rollenstabil"
        elif present_a and present_b:
            relation = "rollenverschiebung"
        elif present_a:
            relation = "nur_karte_a"
        else:
            relation = "nur_karte_b"
        comparison.append(
            {
                "family": family,
                "relation": relation,
                "role_a": role_a,
                "role_b": role_b,
                "hits_a": hits_a,
                "hits_b": hits_b,
                "stable_delta_b_minus_a": stable_b - stable_a,
                "unrest_delta_b_minus_a": unrest_b - unrest_a,
                "strain_delta_b_minus_a": strain_b - strain_a,
                "trust_delta_b_minus_a": trust_b - trust_a,
                "bridge_type_a": left.get("bridge_type", "-") if left else "-",
                "bridge_type_b": right.get("bridge_type", "-") if right else "-",
            }
        )
    role_counts_a = Counter(str(row.get("map_role") or "-") for row in rows_a)
    role_counts_b = Counter(str(row.get("map_role") or "-") for row in rows_b)
    relation_counts = Counter(str(row["relation"]) for row in comparison)
    summary = {
        "map_a_rows": len(rows_a),
        "map_b_rows": len(rows_b),
        "shared_families": sum(1 for row in comparison if row["relation"] in {"rollenstabil", "rollenverschiebung"}),
        "role_counts_a": role_counts_a,
        "role_counts_b": role_counts_b,
        "relation_counts": relation_counts,
    }
    return comparison, summary


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(path: Path, rows: list[dict[str, object]], summary: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    report_id = path.stem.split("_", 1)[0]
    role_counts_a: Counter[str] = summary["role_counts_a"]  # type: ignore[assignment]
    role_counts_b: Counter[str] = summary["role_counts_b"]  # type: ignore[assignment]
    relation_counts: Counter[str] = summary["relation_counts"]  # type: ignore[assignment]
    lines = [
        f"# {report_id} - Block-K MCM-Uebergangskarten-Vergleich",
        "",
        "## Fragestellung",
        "",
        "Welche Rollenordnung kehrt wieder, wenn zwei unabhaengig gelesene Randfamilien miteinander verglichen werden?",
        "",
        "## Kartenvergleich",
        "",
        "| Merkmal | Karte 819 `dio_1un4` | Karte 822 `dio_1yoi` |",
        "|---|---:|---:|",
        f"| Familien gesamt | {summary['map_a_rows']} | {summary['map_b_rows']} |",
        f"| beidseitige Bruecken | {role_counts_a.get('beidseitige_bruecke', 0)} | {role_counts_b.get('beidseitige_bruecke', 0)} |",
        f"| Vorfeldanker | {role_counts_a.get('vorfeldanker', 0)} | {role_counts_b.get('vorfeldanker', 0)} |",
        f"| Nachfeldanker | {role_counts_a.get('nachfeldanker', 0)} | {role_counts_b.get('nachfeldanker', 0)} |",
        f"| instabile Kontaktzonen | {role_counts_a.get('instabile_kontaktzone', 0)} | {role_counts_b.get('instabile_kontaktzone', 0)} |",
        f"| offene Bruecken | {role_counts_a.get('offene_bruecke', 0)} | {role_counts_b.get('offene_bruecke', 0)} |",
        f"| offene Kontaktzonen | {role_counts_a.get('offene_kontaktzone', 0)} | {role_counts_b.get('offene_kontaktzone', 0)} |",
        f"| randnahe Unruhe | {role_counts_a.get('randnahe_unruhe', 0)} | {role_counts_b.get('randnahe_unruhe', 0)} |",
        "",
        "## Familienrelationen",
        "",
        "| Relation | Anzahl |",
        "|---|---:|",
    ]
    for relation, count in relation_counts.most_common():
        lines.append(f"| {relation} | {count} |")
    lines.extend(
        [
            "",
            "## Gemeinsame und verschobene Familien",
            "",
            "| Familie | Relation | Rolle 819 | Rolle 822 | Hits 819 | Hits 822 | Stabil-Delta | Unruhe-Delta | Strain-Delta | Trust-Delta |",
            "|---|---|---|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    priority = {"rollenstabil": 0, "rollenverschiebung": 1, "nur_karte_a": 2, "nur_karte_b": 3}
    for row in sorted(rows, key=lambda item: (priority.get(str(item["relation"]), 9), str(item["family"]))):
        lines.append(
            f"| {row['family']} | {row['relation']} | {row['role_a']} | {row['role_b']} | "
            f"{row['hits_a']} | {row['hits_b']} | {_fmt(row['stable_delta_b_minus_a'])} | "
            f"{_fmt(row['unrest_delta_b_minus_a'])} | {_fmt(row['strain_delta_b_minus_a'])} | "
            f"{_fmt(row['trust_delta_b_minus_a'])} |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Beide Karten zeigen dieselbe Grundform: Randfamilie, stabile Anker, stabile Bruecken und offene Anschlussbereiche. Das spricht gegen eine reine Einzelinsel und fuer eine wiederkehrende passive Uebergangstopologie.",
            "",
            "Der Unterschied liegt in der lokalen Auspraegung: `dio_1un4` enthaelt instabile Kontaktzonen, waehrend `dio_1yoi` staerker ueber stabile Bruecken, einen Nachfeldanker und eine offene Bruecke gelesen wird. Damit ist die Topologie nicht starr kopiert, sondern rollenaehnlich reproduziert.",
            "",
            "## Grenze",
            "",
            "Der Vergleich ist passiv. Er beweist keine universelle MCM-Topologie, zeigt aber eine wiederkehrende Rollenordnung in zwei Randfamilienkarten.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese Rollenordnung gegen eine dritte Randfamilie oder gegen eine bewusst andere Weltspannung geprueft werden. Dann wird sichtbar, ob die Ordnung weiter stabil bleibt oder neue Randrollen entstehen.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--map-a", type=Path, default=MAP_A_DEFAULT)
    parser.add_argument("--map-b", type=Path, default=MAP_B_DEFAULT)
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    args = parser.parse_args()

    rows, summary = build_comparison_rows(args.map_a, args.map_b)
    _write_csv(args.csv_out, rows)
    _write_markdown(args.md_out, rows, summary)
    print(f"map_a={args.map_a}")
    print(f"map_b={args.map_b}")
    print(f"rows={len(rows)}")
    print(f"shared_families={summary['shared_families']}")
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    relation_counts: Counter[str] = summary["relation_counts"]  # type: ignore[assignment]
    for relation, count in relation_counts.most_common():
        print(f"{relation}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
