from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NEIGHBOR_CSV_DEFAULT = ROOT / "docs" / "befunde" / "816_BLOCK_K_RANDFAMILIE_NACHBARSCHAFT_BRUECKE.csv"
BRIDGE_CSV_DEFAULT = ROOT / "docs" / "befunde" / "818_BLOCK_K_BRUECKENTYPEN_VERGLEICH.csv"
CSV_DEFAULT = ROOT / "docs" / "befunde" / "819_BLOCK_K_MCM_UEBERGANGSKARTE.csv"
MD_DEFAULT = ROOT / "docs" / "befunde" / "819_BLOCK_K_MCM_UEBERGANGSKARTE.md"
EDGE_FAMILY_DEFAULT = "dio_1un4"


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


def _role_from_neighbor(row: dict[str, str]) -> str:
    before = _safe_int(row.get("before_hits"))
    after = _safe_int(row.get("after_hits"))
    stable = _safe_float(row.get("stable_share"))
    unrest = _safe_float(row.get("unrest_share"))
    bridge_role = str(row.get("bridge_role") or "")
    if bridge_role == "randnahe_unruhe" or unrest >= 0.70:
        return "randnahe_unruhe"
    if before > 0 and after == 0 and stable >= 0.70:
        return "vorfeldanker"
    if before == 0 and after > 0 and stable >= 0.70:
        return "nachfeldanker"
    if before > 0 and after > 0 and stable >= 0.70:
        return "beidseitige_bruecke"
    if before > 0 and after > 0:
        return "instabile_kontaktzone"
    return "offene_kontaktzone"


def build_transition_rows(neighbor_csv: Path, bridge_csv: Path, edge_family: str) -> list[dict[str, object]]:
    neighbor_rows = _read_csv(neighbor_csv)
    bridge_rows = {row["family"]: row for row in _read_csv(bridge_csv)}
    rows: list[dict[str, object]] = []
    target = next((row for row in neighbor_rows if row.get("type") == "target_summary"), None)
    if target:
        rows.append(
            {
                "map_role": "randfamilie",
                "family": edge_family,
                "source_role": "target",
                "hits": _safe_int(target.get("total_neighbor_hits")),
                "before_hits": "",
                "after_hits": "",
                "stable_share": 0.0,
                "unrest_share": 1.0,
                "avg_strain": _safe_float(target.get("target_avg_strain")),
                "avg_trust": _safe_float(target.get("target_avg_trust")),
                "fieldtime_embedding": _safe_float(target.get("target_embedding")),
                "bridge_type": "randspannung",
                "trust_delta": "",
                "strain_delta": "",
                "interpretation": "randnahe Spannungsfamilie und Ausgangspunkt der Karte",
            }
        )
    for row in neighbor_rows:
        if row.get("type") != "neighbor_summary":
            continue
        family = str(row.get("family") or "-")
        map_role = _role_from_neighbor(row)
        bridge = bridge_rows.get(family, {})
        bridge_type = str(bridge.get("bridge_type") or row.get("bridge_role") or "-")
        if bridge_type == "instabile_kontaktzone":
            map_role = "instabile_kontaktzone"
        elif bridge_type == "offene_bruecke":
            map_role = "offene_bruecke"
        elif bridge_type == "nachfeld_anker":
            map_role = "nachfeldanker"
        elif bridge_type == "vorfeld_anker":
            map_role = "vorfeldanker"
        interpretation = {
            "vorfeldanker": "stabiler Vorfeldanker vor der Randfamilie",
            "nachfeldanker": "stabiler Nachfeldanker nach der Randfamilie",
            "beidseitige_bruecke": "beidseitige stabile Bruecke",
            "instabile_kontaktzone": "gemischte Kontaktzone mit instabiler Naehe",
            "offene_bruecke": "offene Bruecke mit stabiler Naehe, aber noch offener Rollenbindung",
            "randnahe_unruhe": "weitere randnahe Unruhefamilie",
            "offene_kontaktzone": "offene Kontaktzone ohne klare Rollenreife",
        }.get(map_role, "offene Kontaktrolle")
        rows.append(
            {
                "map_role": map_role,
                "family": family,
                "source_role": row.get("bridge_role") or "-",
                "hits": _safe_int(row.get("neighbor_hits")),
                "before_hits": _safe_int(row.get("before_hits")),
                "after_hits": _safe_int(row.get("after_hits")),
                "stable_share": _safe_float(row.get("stable_share")),
                "unrest_share": _safe_float(row.get("unrest_share")),
                "avg_strain": _safe_float(row.get("avg_strain")),
                "avg_trust": _safe_float(row.get("avg_trust")),
                "fieldtime_embedding": _safe_float(row.get("fieldtime_embedding")),
                "bridge_type": bridge_type,
                "trust_delta": _safe_float(bridge.get("trust_delta"), 0.0) if bridge else "",
                "strain_delta": _safe_float(bridge.get("strain_delta"), 0.0) if bridge else "",
                "interpretation": interpretation,
            }
        )
    return rows


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(path: Path, rows: list[dict[str, object]], edge_family: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    role_counts = Counter(str(row["map_role"]) for row in rows)
    report_id = path.stem.split("_", 1)[0]
    lines = [
        f"# {report_id} - Block-K MCM-Uebergangskarte",
        "",
        "## Fragestellung",
        "",
        f"Welche kompakte Rollenkarte entsteht um die Randfamilie `{edge_family}` aus Randfamilie, Ankern, Bruecken, Kontaktzone und stabiler Mitte?",
        "",
        "## Rollenuebersicht",
        "",
        "| Rolle | Anzahl |",
        "|---|---:|",
    ]
    for role, count in role_counts.most_common():
        lines.append(f"| {role} | {count} |")
    lines.extend(
        [
            "",
            "## Karte",
            "",
            "| Rolle | Familie | Hits | Vorher | Nachher | Stabil | Unruhe | Strain | Trust | Einbettung | Brueckentyp |",
            "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    role_order = {
        "randfamilie": 0,
        "vorfeldanker": 1,
        "beidseitige_bruecke": 2,
        "instabile_kontaktzone": 3,
        "offene_bruecke": 4,
        "nachfeldanker": 5,
        "randnahe_unruhe": 6,
        "offene_kontaktzone": 7,
    }
    for row in sorted(rows, key=lambda item: (role_order.get(str(item["map_role"]), 99), -_safe_int(item["hits"]))):
        lines.append(
            f"| {row['map_role']} | {row['family']} | {row['hits']} | {row['before_hits']} | "
            f"{row['after_hits']} | {_fmt(row['stable_share'])} | {_fmt(row['unrest_share'])} | "
            f"{_fmt(row['avg_strain'])} | {_fmt(row['avg_trust'])} | "
            f"{_fmt(row['fieldtime_embedding'])} | {row['bridge_type']} |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die MCM-Uebergangskarte zeigt keine flache Wolke. Um die Randfamilie entsteht eine gegliederte Rollenordnung:",
            "",
            "- eine randnahe Spannungsfamilie als Ausgangspunkt,",
        ]
    )
    if role_counts.get("vorfeldanker"):
        lines.append("- stabile Vorfeldanker, die vor der Randspannung haeufig auftreten,")
    if role_counts.get("beidseitige_bruecke"):
        lines.append("- beidseitige Bruecken, die Randnaehe beruehren und stabil bleiben,")
    if role_counts.get("instabile_kontaktzone"):
        lines.append("- instabile Kontaktzonen, die zwischen stabil und unruhig mischen,")
    if role_counts.get("offene_bruecke"):
        lines.append("- offene Bruecken, die stabil beruehren, aber noch keine geschlossene Rollenbindung zeigen,")
    if role_counts.get("nachfeldanker"):
        lines.append("- stabile Nachfeldanker, die nach der Randspannung weitertragen,")
    if role_counts.get("offene_kontaktzone") or role_counts.get("randnahe_unruhe"):
        lines.append("- offene Folgezonen und weitere Randunruhe als Anschlussbereiche.")
    lines.extend(
        [
            "",
            "Damit wirkt das Feld topologisch gegliedert: Rand, Kontakt, Bruecke und stabile Umgebung sind passiv unterscheidbar.",
            "",
            "## Grenze",
            "",
            "Die Karte ist eine passive Innenfeldkarte. Sie ist keine Handlungskarte, keine Strategie und keine Richtungsvorhersage.",
            "",
            "## Wie es weitergeht",
            "",
        ]
    )
    if edge_family == EDGE_FAMILY_DEFAULT:
        lines.append(
            "Als naechstes sollte diese Karte gegen eine zweite Randfamilie geprueft werden. Nur dann sehen wir, ob die Rollenordnung allgemein ist oder spezifisch um `dio_1un4` entsteht."
        )
    else:
        lines.append(
            "Als naechstes sollten die Uebergangskarten der Randfamilien direkt verglichen werden. Dann sehen wir, welche Rollenordnung wiederkehrt und welche nur lokal zur jeweiligen Randfamilie gehoert."
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--neighbor-csv", type=Path, default=NEIGHBOR_CSV_DEFAULT)
    parser.add_argument("--bridge-csv", type=Path, default=BRIDGE_CSV_DEFAULT)
    parser.add_argument("--edge-family", default=EDGE_FAMILY_DEFAULT)
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    args = parser.parse_args()

    rows = build_transition_rows(args.neighbor_csv, args.bridge_csv, args.edge_family)
    _write_csv(args.csv_out, rows)
    _write_markdown(args.md_out, rows, args.edge_family)
    print(f"edge_family={args.edge_family}")
    print(f"rows={len(rows)}")
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    counts = Counter(str(row["map_role"]) for row in rows)
    for role, count in counts.most_common():
        print(f"{role}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
