from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


def _read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _float(row: dict[str, str], key: str, default: float = 0.0) -> float:
    try:
        return float(row.get(key, "") or default)
    except ValueError:
        return default


def _int(row: dict[str, str], key: str, default: int = 0) -> int:
    try:
        return int(float(row.get(key, "") or default))
    except ValueError:
        return default


def _classify(row: dict[str, str]) -> tuple[str, str]:
    zone = row.get("condensation_zone", "")
    role = row.get("dominant_role", "")
    observations = _int(row, "observations")
    worlds = _int(row, "worlds")
    center = _float(row, "center_share")
    open_share = _float(row, "open_share")
    rand = _float(row, "rand_share")
    rekopplung = _float(row, "avg_rekopplung")
    strain = _float(row, "avg_strain")
    sensory = _float(row, "avg_sensory")
    loudness = _float(row, "avg_loudness")
    blur = _float(row, "avg_visual_blur")
    entropy = _float(row, "role_entropy")
    neighbors = _int(row, "neighbor_count")

    if observations >= 50 and worlds >= 3 and center >= 0.70 and strain <= 0.18:
        return "nichtbruecke_zentrum_getragen", "zentral, wiederkehrend, geringe Last"
    if observations >= 20 and worlds >= 2 and open_share >= 0.55 and sensory >= 0.70:
        return "nichtbruecke_offene_wahrnehmungsinsel", "offene Lage mit hoher Sinnesaufnahme"
    if rand >= 0.20 or strain >= 0.30:
        return "nichtbruecke_randspannung", "Rand- oder Lastnaehe ohne Brueckenbindung"
    if rekopplung >= 0.65 and strain <= 0.22 and neighbors >= 8:
        return "nichtbruecke_rekopplungsfeld", "Rekopplung sichtbar, aber nicht als Bruecke organisiert"
    if loudness >= 0.34 or blur >= 0.62:
        return "nichtbruecke_sinnesrauschen", "Ton-/Sichtlast dominiert die Oberflaeche"
    if entropy >= 1.0:
        return "nichtbruecke_mehrdeutige_oberflaeche", "Rollenmischung ohne stabile Anschlussrolle"
    if zone == "driftzone":
        return "nichtbruecke_driftfeld", "Driftzone ohne Anschlussanker"
    if role == "zentrum_stabil":
        return "nichtbruecke_zentrum_schwach", "Zentrumsrolle vorhanden, aber nicht brueckenbildend"
    return "nichtbruecke_offen", "Ordnung sichtbar, aber noch nicht klassifiziert"


def _enrich(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for row in rows:
        order_class, note = _classify(row)
        out.append(
            {
                "token": row.get("token", ""),
                "short_token": row.get("token", "").replace("dio_mcm_episode_", ""),
                "nonbridge_class": order_class,
                "condensation_zone": row.get("condensation_zone", ""),
                "dominant_role": row.get("dominant_role", ""),
                "dominant_family": row.get("dominant_family", ""),
                "observations": row.get("observations", "0"),
                "worlds": row.get("worlds", "0"),
                "neighbor_count": row.get("neighbor_count", "0"),
                "avg_rekopplung": row.get("avg_rekopplung", "0"),
                "avg_strain": row.get("avg_strain", "0"),
                "avg_sensory": row.get("avg_sensory", "0"),
                "avg_tension": row.get("avg_tension", "0"),
                "avg_loudness": row.get("avg_loudness", "0"),
                "avg_visual_blur": row.get("avg_visual_blur", "0"),
                "center_share": row.get("center_share", "0"),
                "open_share": row.get("open_share", "0"),
                "rand_share": row.get("rand_share", "0"),
                "role_entropy": row.get("role_entropy", "0"),
                "top_previous": row.get("top_previous", ""),
                "top_next": row.get("top_next", ""),
                "classification_note": note,
            }
        )
    out.sort(
        key=lambda row: (
            row["nonbridge_class"],
            -float(row["observations"] or 0),
            row["short_token"],
        )
    )
    return out


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _avg(rows: list[dict[str, str]], key: str) -> float:
    if not rows:
        return 0.0
    return sum(float(row.get(key, "0") or 0.0) for row in rows) / len(rows)


def _write_md(path: Path, rows: list[dict[str, str]]) -> None:
    counts = Counter(row["nonbridge_class"] for row in rows)
    by_class: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_class[row["nonbridge_class"]].append(row)

    lines: list[str] = [
        "# MCM-Nicht-Bruecken-Lesung",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest eine Weltgruppe, in der die bisherige Brueckenlogik keine Brueckenlandschaft bildet.",
        "Sie fragt nicht nach Anschlussankern, sondern nach passiver Ordnung ohne Bruecke.",
        "",
        "## Klassenprofil",
        "",
        "| Klasse | Anzahl | mittlere Last | mittlere Sinnesaufnahme | mittlere Rekopplung |",
        "|---|---:|---:|---:|---:|",
    ]
    for key, count in counts.most_common():
        subset = by_class[key]
        lines.append(
            f"| `{key}` | {count} | {_avg(subset, 'avg_strain'):.4f} | {_avg(subset, 'avg_sensory'):.4f} | {_avg(subset, 'avg_rekopplung'):.4f} |"
        )

    lines.extend(
        [
            "",
            "## Staerkste Nicht-Bruecken-Zeichen",
            "",
            "| Token | Klasse | Zone | Rolle | Beobachtungen | Welten | Note |",
            "|---|---|---|---|---:|---:|---|",
        ]
    )
    strongest = sorted(rows, key=lambda row: int(float(row["observations"] or 0)), reverse=True)[:20]
    for row in strongest:
        lines.append(
            f"| `{row['short_token']}` | `{row['nonbridge_class']}` | `{row['condensation_zone']}` | `{row['dominant_role']}` | {row['observations']} | {row['worlds']} | {row['classification_note']} |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Eine Welt ohne Brueckenlandschaft ist nicht automatisch ungeordnet.",
            "Sie kann Verdichtung, Wiederkehr, Zentrumsnaehe, offene Wahrnehmungsinseln oder Randspannung tragen, ohne daraus stabile Anschlussanker zu bilden.",
            "",
            "Fachlich ist das wichtig, weil MINI_DIO damit zwei Ordnungsarten unterscheiden kann:",
            "",
            "- Ordnung mit Bruecken: Bedeutungen verbinden sich topologisch ueber Anschlussrollen.",
            "- Ordnung ohne Bruecken: Bedeutungen bleiben als Inseln, Driftfelder oder Sinnesoberflaechen sichtbar, koppeln aber nicht stabil weiter.",
            "",
            "## Schlussfolgerung",
            "",
            "Diese Welt sollte nicht mit Brueckenlogik erzwungen werden.",
            "Sie braucht eine eigene passive Lesung fuer Nicht-Bruecken-Ordnung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese Nicht-Bruecken-Karte gegen die zugehoerigen Verdichtungszonen und Pfadklassen synthetisiert werden.",
            "Entscheidend ist, ob die Welt eher offene Wahrnehmungsinseln, Zentrumsinseln, Randspannung oder Sinnesrauschen bildet.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--zones", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    rows = _enrich(_read(args.zones))
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"rows={len(rows)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
