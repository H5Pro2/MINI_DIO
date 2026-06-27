from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


PATH_ORDER = [
    "stabile_insel",
    "rekoppelnder_pfad",
    "offener_driftpfad",
    "randpfad",
    "brueckenpfad",
    "junge_oberflaeche",
    "gemischter_pfad",
]


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


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


def _zone(row: dict[str, str], prefix: str) -> str:
    return row.get(f"{prefix}_zone", "-") or "-"


def _path_class(row: dict[str, str]) -> tuple[str, str]:
    base_zone = _zone(row, "base")
    follow_zone = _zone(row, "follow")
    movement = row.get("movement", "-") or "-"
    rek_delta = _float(row, "rekopplung_delta")
    strain_delta = _float(row, "strain_delta")
    loud_delta = _float(row, "loudness_delta")
    blur_delta = _float(row, "visual_blur_delta")
    world_delta = _int(row, "world_delta")
    base_role = row.get("base_dominant_role", "-") or "-"
    follow_role = row.get("follow_dominant_role", "-") or "-"

    if base_zone == "randnahe_verdichtung" or follow_zone == "randnahe_verdichtung":
        return "randpfad", "Randnaehe ist in Basis oder Folgezone direkt beteiligt."

    if movement == "verjuengung_oberflaeche" or follow_zone == "junge_spur":
        return "junge_oberflaeche", "Token verliert Reife oder faellt in junge Oberflaeche zurueck."

    if base_zone == "hoeherer_cluster_uebergang" or follow_zone == "hoeherer_cluster_uebergang":
        if movement == "oeffnung_oder_drift" or (rek_delta < -0.008 and (strain_delta > 0.006 or blur_delta > 0.04)):
            return "offener_driftpfad", "Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe."
        return "brueckenpfad", "Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang."

    if movement == "stabil" and follow_zone == "stabile_bedeutungsinsel":
        return "stabile_insel", "Zone bleibt stabile Bedeutungsinsel."

    if movement == "stabil" and follow_zone == "rekopplungszone":
        return "rekoppelnder_pfad", "Zone bleibt Rekopplungszone."

    if movement == "reifung_oder_verdichtung":
        if follow_zone in {"rekopplungszone", "stabile_bedeutungsinsel"}:
            return "rekoppelnder_pfad", "Token verschiebt sich in stabilere oder rekoppelnde Zone."
        return "brueckenpfad", "Token reift, bleibt aber als Uebergangsform lesbar."

    if movement == "oeffnung_oder_drift":
        return "offener_driftpfad", "Token oeffnet oder driftet zwischen den Weltgruppen."

    if follow_role == "offene_variante" and base_role == "zentrum_stabil":
        return "offener_driftpfad", "Rolle kippt von Zentrum in offene Variante."

    if rek_delta > 0.003 and strain_delta <= 0.0:
        return "rekoppelnder_pfad", "Rekopplung steigt und Strain faellt oder bleibt niedrig."

    if rek_delta < -0.003 and (strain_delta > 0.0 or loud_delta > 0.0 or blur_delta > 0.0):
        return "offener_driftpfad", "Rekopplung faellt bei steigender Last oder Sinnesunschärfe."

    if movement == "stabil":
        if world_delta >= 0 and follow_zone in {"driftzone", "offene_bedeutungszone"}:
            return "gemischter_pfad", "Zone bleibt formal stabil, aber im offenen Bedeutungsraum."
        return "stabile_insel", "Token bleibt in seiner Verdichtungszone."

    return "gemischter_pfad", "Kein eindeutiges Pfadprofil aus Driftmatrix ableitbar."


def _classify(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for row in rows:
        path_class, reason = _path_class(row)
        out.append(
            {
                "token": row.get("token", "-") or "-",
                "path_class": path_class,
                "reason": reason,
                "movement": row.get("movement", "-") or "-",
                "base_zone": row.get("base_zone", "-") or "-",
                "follow_zone": row.get("follow_zone", "-") or "-",
                "base_observations": _int(row, "base_observations"),
                "follow_observations": _int(row, "follow_observations"),
                "observation_delta": _int(row, "observation_delta"),
                "base_worlds": _int(row, "base_worlds"),
                "follow_worlds": _int(row, "follow_worlds"),
                "world_delta": _int(row, "world_delta"),
                "base_role": row.get("base_dominant_role", "-") or "-",
                "follow_role": row.get("follow_dominant_role", "-") or "-",
                "rekopplung_delta": _float(row, "rekopplung_delta"),
                "strain_delta": _float(row, "strain_delta"),
                "loudness_delta": _float(row, "loudness_delta"),
                "visual_blur_delta": _float(row, "visual_blur_delta"),
            }
        )
    order = {name: index for index, name in enumerate(PATH_ORDER)}
    out.sort(
        key=lambda item: (
            order.get(str(item["path_class"]), 999),
            -abs(int(item["observation_delta"])),
            str(item["token"]),
        )
    )
    return out


def _write_csv(rows: list[dict[str, object]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        out.write_text("", encoding="utf-8")
        return
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def _write_markdown(rows: list[dict[str, object]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    counts = Counter(str(row["path_class"]) for row in rows)
    movement_counts = Counter(str(row["movement"]) for row in rows)

    lines = [
        "# MCM-Pfadklassifikation",
        "",
        "## Zweck",
        "",
        "Diese Diagnose erweitert die Verdichtungspfad-Lesart von vier Beispiel-Tokens auf alle gemeinsamen Tokens der Driftmatrix.",
        "Sie ist passiv und klassifiziert Feldbewegungen, nicht Verhalten.",
        "",
        "## Pfadklassen",
        "",
        "| Pfadklasse | Anzahl |",
        "|---|---:|",
    ]
    for name in PATH_ORDER:
        if counts.get(name, 0):
            lines.append(f"| {name} | {counts[name]} |")

    lines.extend(["", "## Ausgangsbewegungen", "", "| Bewegung aus Driftlupe | Anzahl |", "|---|---:|"])
    for movement, count in sorted(movement_counts.items()):
        lines.append(f"| {movement} | {count} |")

    lines.extend(
        [
            "",
            "## Staerkste Tokens Je Pfadklasse",
            "",
            "| Pfadklasse | Token | Bewegung | Basiszone | Folgezone | Beobachtungsdelta | Weltendelta | Grund |",
            "|---|---|---|---|---|---:|---:|---|",
        ]
    )
    for name in PATH_ORDER:
        selected = [row for row in rows if row["path_class"] == name]
        selected.sort(key=lambda row: abs(int(row["observation_delta"])), reverse=True)
        for row in selected[:8]:
            lines.append(
                f"| {name} | {row['token']} | {row['movement']} | {row['base_zone']} | {row['follow_zone']} | "
                f"{row['observation_delta']} | {row['world_delta']} | {row['reason']} |"
            )

    lines.extend(["", "## Befund", ""])
    if counts["brueckenpfad"] + counts["stabile_insel"] + counts["rekoppelnder_pfad"] > counts["offener_driftpfad"]:
        lines.append(
            "Die Mehrzahl der gemeinsamen Tokens liegt in stabilen, rekoppelnden oder brueckenartigen Pfaden. Das spricht fuer geordnete Feldbewegung statt zufaelliger Symboloberflaeche."
        )
    else:
        lines.append(
            "Offene Driftpfade sind mindestens so stark wie stabile oder rekoppelnde Pfade. Das wuerde auf eine noch stark weltgefaerbte Feldoberflaeche hinweisen."
        )

    if counts["randpfad"] <= max(2, len(rows) * 0.05):
        lines.append(
            "Randpfade bleiben selten. Das passt zum bisherigen Befund: Randnaehe entsteht lokal, aber sie dominiert die Topologie nicht."
        )

    lines.extend(
        [
            "",
            "## Bedeutung Fuer MINI_DIO",
            "",
            "Die Pfadklassifikation verschiebt die Lesart von Tokenlisten zu Feldbewegungen.",
            "Ein `dio_mcm_episode_*`-Zeichen ist damit nicht nur ein Name, sondern kann eine Insel, ein Pfad, eine Bruecke oder eine Driftbewegung tragen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese Pfadklassifikation gegen eine weitere frische Weltgruppe reproduziert werden. Ziel: pruefen, ob die Verteilung der Pfadklassen stabil bleibt oder ob neue Weltspannung andere Pfadtypen erzwingt.",
            "",
        ]
    )
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--drift", required=True)
    parser.add_argument("--out-md", required=True)
    parser.add_argument("--out-csv", required=True)
    args = parser.parse_args()

    rows = _classify(_load(Path(args.drift)))
    _write_csv(rows, Path(args.out_csv))
    _write_markdown(rows, Path(args.out_md))
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
