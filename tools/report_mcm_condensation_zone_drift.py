from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


ZONE_ORDER = {
    "junge_spur": 0,
    "offene_bedeutungszone": 1,
    "driftzone": 2,
    "rekopplungszone": 3,
    "stabile_bedeutungsinsel": 4,
    "hoeherer_cluster_uebergang": 5,
    "randnahe_verdichtung": 6,
}


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _int(row: dict[str, str], key: str) -> int:
    try:
        return int(float(row.get(key, "") or 0))
    except ValueError:
        return 0


def _float(row: dict[str, str], key: str) -> float:
    try:
        return float(row.get(key, "") or 0.0)
    except ValueError:
        return 0.0


def _zone(row: dict[str, str]) -> str:
    return row.get("condensation_zone", "-") or "-"


def _movement(base: dict[str, str], follow: dict[str, str]) -> str:
    base_zone = _zone(base)
    follow_zone = _zone(follow)
    if base_zone == follow_zone:
        return "stabil"
    if follow_zone == "randnahe_verdichtung":
        return "randnaehe_entsteht"
    if base_zone == "randnahe_verdichtung" and follow_zone != base_zone:
        return "randnaehe_rekoppelt"
    if follow_zone in {"rekopplungszone", "stabile_bedeutungsinsel", "hoeherer_cluster_uebergang"}:
        return "reifung_oder_verdichtung"
    if follow_zone in {"offene_bedeutungszone", "driftzone"}:
        return "oeffnung_oder_drift"
    if follow_zone == "junge_spur":
        return "verjuengung_oberflaeche"

    base_rank = ZONE_ORDER.get(base_zone, 0)
    follow_rank = ZONE_ORDER.get(follow_zone, 0)
    if follow_rank > base_rank:
        return "aufwaertsverschiebung"
    if follow_rank < base_rank:
        return "ruecknahme"
    return "wechsel"


def _score_delta(base: dict[str, str], follow: dict[str, str], key: str) -> float:
    return round(_float(follow, key) - _float(base, key), 6)


def _build_rows(base_rows: list[dict[str, str]], follow_rows: list[dict[str, str]]) -> list[dict[str, object]]:
    base_map = {row.get("token", "-") or "-": row for row in base_rows}
    follow_map = {row.get("token", "-") or "-": row for row in follow_rows}
    shared = sorted(set(base_map) & set(follow_map))
    rows: list[dict[str, object]] = []

    for token in shared:
        base = base_map[token]
        follow = follow_map[token]
        rows.append(
            {
                "token": token,
                "base_zone": _zone(base),
                "follow_zone": _zone(follow),
                "movement": _movement(base, follow),
                "base_observations": _int(base, "observations"),
                "follow_observations": _int(follow, "observations"),
                "observation_delta": _int(follow, "observations") - _int(base, "observations"),
                "base_worlds": _int(base, "worlds"),
                "follow_worlds": _int(follow, "worlds"),
                "world_delta": _int(follow, "worlds") - _int(base, "worlds"),
                "base_dominant_role": base.get("dominant_role", "-") or "-",
                "follow_dominant_role": follow.get("dominant_role", "-") or "-",
                "base_top_next": base.get("top_next", "-") or "-",
                "follow_top_next": follow.get("top_next", "-") or "-",
                "rekopplung_delta": _score_delta(base, follow, "avg_rekopplung"),
                "strain_delta": _score_delta(base, follow, "avg_strain"),
                "sensory_delta": _score_delta(base, follow, "avg_sensory"),
                "tension_delta": _score_delta(base, follow, "avg_tension"),
                "loudness_delta": _score_delta(base, follow, "avg_loudness"),
                "visual_blur_delta": _score_delta(base, follow, "avg_visual_blur"),
            }
        )
    rows.sort(
        key=lambda row: (
            row["movement"] == "stabil",
            -abs(int(row["observation_delta"])),
            str(row["token"]),
        )
    )
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


def _top_rows(rows: list[dict[str, object]], movement: str, limit: int = 12) -> list[dict[str, object]]:
    selected = [row for row in rows if row["movement"] == movement]
    selected.sort(key=lambda row: abs(int(row["observation_delta"])), reverse=True)
    return selected[:limit]


def _write_markdown(
    rows: list[dict[str, object]],
    base_name: str,
    follow_name: str,
    out: Path,
) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    movement_counts = Counter(str(row["movement"]) for row in rows)
    zone_pairs = Counter((str(row["base_zone"]), str(row["follow_zone"])) for row in rows)
    by_follow_zone: dict[str, Counter[str]] = defaultdict(Counter)
    for base_zone, follow_zone in zone_pairs:
        by_follow_zone[follow_zone][base_zone] += zone_pairs[(base_zone, follow_zone)]

    stable = movement_counts["stabil"]
    changed = len(rows) - stable
    stable_ratio = stable / max(1, len(rows))

    lines = [
        "# MCM-Verdichtungszonen Driftlupe",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest gemeinsame Tokens zweier Verdichtungszonen-Laeufe.",
        "Sie prueft, ob ein Token seine Verdichtungszone behaelt, driftet, reift, rekoppelt oder in Randnaehe kippt.",
        "",
        "## Basis",
        "",
        f"- Basislauf: `{base_name}`",
        f"- Folgelauf: `{follow_name}`",
        f"- gemeinsame Tokens: `{len(rows)}`",
        f"- stabile Tokens: `{stable}`",
        f"- wechselnde Tokens: `{changed}`",
        f"- Stabilitaetsquote: `{stable_ratio:.4f}`",
        "",
        "## Bewegungsarten",
        "",
        "| Bewegung | Anzahl |",
        "|---|---:|",
    ]
    for movement, count in sorted(movement_counts.items()):
        lines.append(f"| {movement} | {count} |")

    lines.extend(
        [
            "",
            "## Staerkste Wechsel nach Beobachtungsdelta",
            "",
            "| Token | Bewegung | Basiszone | Folgezone | Beobachtungen | Welten | Rekopplung | Strain | Lautheit | Unschaerfe |",
            "|---|---|---|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    changed_rows = [row for row in rows if row["movement"] != "stabil"]
    changed_rows.sort(key=lambda row: abs(int(row["observation_delta"])), reverse=True)
    for row in changed_rows[:20]:
        lines.append(
            "| {token} | {movement} | {base_zone} | {follow_zone} | {obs_delta:+d} | {world_delta:+d} | {rek:+.4f} | {strain:+.4f} | {loud:+.4f} | {blur:+.4f} |".format(
                token=row["token"],
                movement=row["movement"],
                base_zone=row["base_zone"],
                follow_zone=row["follow_zone"],
                obs_delta=int(row["observation_delta"]),
                world_delta=int(row["world_delta"]),
                rek=float(row["rekopplung_delta"]),
                strain=float(row["strain_delta"]),
                loud=float(row["loudness_delta"]),
                blur=float(row["visual_blur_delta"]),
            )
        )

    lines.extend(["", "## Befund", ""])
    if stable_ratio >= 0.55:
        lines.append(
            "Die Mehrheit der gemeinsamen Tokens behaelt ihre Verdichtungszone. Das spricht fuer stabile Rollenordnung mit variabler Oberflaeche."
        )
    else:
        lines.append(
            "Weniger als die Haelfte der gemeinsamen Tokens behaelt ihre Verdichtungszone. Das wuerde auf staerkere Weltfaerbung oder noch unreife Oberflaechenbindung hinweisen."
        )

    if movement_counts["reifung_oder_verdichtung"] > movement_counts["oeffnung_oder_drift"]:
        lines.append(
            "Mehr wechselnde Tokens gehen in Richtung Reifung/Verdichtung als in Oeffnung/Drift. Das deutet auf nachtraegliche Stabilisierung einzelner Feldzeichen."
        )
    elif movement_counts["oeffnung_oder_drift"] > 0:
        lines.append(
            "Ein relevanter Teil der Wechsel geht in Oeffnung/Drift. Diese Tokens sind Kandidaten fuer echte Bedeutungsbewegung statt blosser Wiederholung."
        )

    if movement_counts["randnaehe_entsteht"] or movement_counts["randnaehe_rekoppelt"]:
        lines.append(
            "Randnaehe tritt als kleine, aber gesonderte Bewegung auf. Das passt zur bisherigen Lesart: Rand ist lokal und selten, nicht die Grundform des Feldes."
        )

    lines.extend(
        [
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollten die wechselnden Tokens gegen ihre Rohweltabschnitte gelesen werden. Ziel: unterscheiden, ob Zonenwechsel aus Weltphase, Sinnesaufnahme, Rekopplung oder echter MCM-Drift entsteht.",
            "",
        ]
    )
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True)
    parser.add_argument("--follow", required=True)
    parser.add_argument("--base-name", default="base")
    parser.add_argument("--follow-name", default="follow")
    parser.add_argument("--out-md", required=True)
    parser.add_argument("--out-csv", required=True)
    args = parser.parse_args()

    rows = _build_rows(_load(Path(args.base)), _load(Path(args.follow)))
    _write_csv(rows, Path(args.out_csv))
    _write_markdown(rows, args.base_name, args.follow_name, Path(args.out_md))
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
