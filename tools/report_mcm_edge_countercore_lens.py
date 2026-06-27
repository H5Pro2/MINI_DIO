from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


EDGE_CLASSES = {"randpfad", "junge_oberflaeche", "offener_driftpfad"}


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def _float(value: str, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _int(value: str, default: int = 0) -> int:
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return default


def _short(token: str) -> str:
    return token.replace("dio_mcm_episode_", "")


def _token_set(rows: list[dict[str, str]]) -> set[str]:
    tokens: set[str] = set()
    for row in rows:
        if row.get("path_class") in EDGE_CLASSES:
            tokens.add(row["token"])
    return tokens


def _classify_countercore(path_row: dict[str, str], neigh_row: dict[str, str] | None) -> str:
    path_class = path_row.get("path_class", "")
    movement = path_row.get("movement", "")
    worlds = max(
        _int(path_row.get("base_worlds")),
        _int(path_row.get("follow_worlds")),
        _int((neigh_row or {}).get("worlds")),
    )
    observations = max(_int(path_row.get("base_observations")), _int(path_row.get("follow_observations")))
    has_neighbor_coverage = bool(neigh_row)
    contacts = _int((neigh_row or {}).get("contacts"))
    self_prev = _float((neigh_row or {}).get("self_prev_share"))
    self_next = _float((neigh_row or {}).get("self_next_share"))
    self_share = min(self_prev, self_next)

    if not has_neighbor_coverage:
        if path_class == "randpfad" and movement == "stabil":
            return "rand_stabil_ohne_nachbarschaftsabdeckung"
        if path_class == "randpfad" and "rekoppelt" in movement:
            return "rand_rekoppelt_ohne_nachbarschaftsabdeckung"
        if path_class == "junge_oberflaeche":
            return "junge_oberflaeche_ohne_nachbarschaftsabdeckung"
        if path_class == "offener_driftpfad":
            return "offener_drift_ohne_nachbarschaftsabdeckung"
        return "ohne_nachbarschaftsabdeckung"

    if path_class == "offener_driftpfad" and contacts >= 500 and worlds >= 3 and self_share >= 0.80:
        return "starker_driftkern_kandidat"
    if path_class == "junge_oberflaeche" and contacts >= 100 and self_share >= 0.80:
        return "lokale_junge_selbstinsel"
    if path_class == "randpfad" and movement == "stabil" and contacts >= 5 and worlds >= 3 and self_share < 0.20:
        return "randstabil_ohne_selbstkern"
    if path_class == "randpfad" and movement == "stabil" and worlds >= 2 and observations >= 40 and self_share >= 0.55:
        return "moeglicher_randkern"
    if path_class == "randpfad" and "rekoppelt" in movement:
        return "rand_rekoppelt"
    if path_class == "junge_oberflaeche" and movement == "stabil" and contacts >= 20 and self_share >= 0.5:
        return "stabile_oberflaeche_ohne_kern"
    if path_class == "junge_oberflaeche":
        return "kurzlebige_oberflaeche"
    if path_class == "offener_driftpfad":
        return "offener_drift"
    return "unklar"


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "token",
        "path_class",
        "movement",
        "base_zone",
        "follow_zone",
        "base_role",
        "follow_role",
        "base_worlds",
        "follow_worlds",
        "base_observations",
        "follow_observations",
        "contacts",
        "worlds",
        "dominant_prev",
        "dominant_prev_count",
        "dominant_next",
        "dominant_next_count",
        "current_role_profile",
        "neighbor_role_profile",
        "self_prev_share",
        "self_next_share",
        "neighbor_coverage",
        "countercore_class",
    ]
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def _write_md(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    class_counts = Counter(row["countercore_class"] for row in rows)
    path_counts = Counter(row["path_class"] for row in rows)

    lines: list[str] = []
    lines.append("# MCM-Randpfade Gegenkern-Lupe")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append(
        "Diese Diagnose prueft, ob Randpfade eigene stabile Gegenkerne bilden oder ob Randnaehe vor allem als kurzlebige Oberflaeche, Drift oder Austrittsphaenomen erscheint."
    )
    lines.append("")
    lines.append("## Rohumfang")
    lines.append("")
    lines.append(f"- Untersuchte Tokens: `{len(rows)}`")
    lines.append(f"- Pfadklassen: `{', '.join(f'{k}={v}' for k, v in path_counts.items())}`")
    lines.append(f"- Gegenkernklassen: `{', '.join(f'{k}={v}' for k, v in class_counts.items())}`")
    lines.append("")

    lines.append("## Tokenlupe")
    lines.append("")
    lines.append("| Token | Pfadklasse | Bewegung | Zone vorher | Zone nachher | Kontakte | Welten | Selbstbindung | Gegenkernklasse |")
    lines.append("|---|---|---|---|---|---:|---:|---:|---|")
    for row in rows:
        self_share = min(_float(row.get("self_prev_share")), _float(row.get("self_next_share")))
        lines.append(
            f"| `{_short(row['token'])}` | {row['path_class']} | {row['movement']} | {row['base_zone']} | {row['follow_zone']} | {row.get('contacts', '0')} | {row.get('worlds', '0')} | {self_share:.3f} | {row['countercore_class']} |"
        )
    lines.append("")

    possible = [row for row in rows if row["countercore_class"] == "moeglicher_randkern"]
    drift_cores = [row for row in rows if row["countercore_class"] == "starker_driftkern_kandidat"]
    local_young = [row for row in rows if row["countercore_class"] == "lokale_junge_selbstinsel"]
    lines.append("## Befund")
    lines.append("")
    missing_coverage = [row for row in rows if row.get("neighbor_coverage") != "1"]
    if possible:
        lines.append("Es gibt Randtokens, die als moegliche Randkerne gelesen werden koennen.")
        lines.append("Sie sind aber nicht mit den zentralen Brueckenkernen gleichzusetzen, solange ihre Netzwerkbindung und Weltspanne schwaecher bleibt.")
    elif missing_coverage:
        lines.append("In dieser Weltgruppe laesst sich aus der vorhandenen Nachbarschaftsmatrix noch kein belastbarer Rand-Gegenkern ableiten.")
        lines.append("Die Randtokens sind in der Pfadklassifikation sichtbar, aber in der verwendeten Nachbarschaftsmatrix nicht abgedeckt.")
        lines.append("Damit ist das Ergebnis kein Beweis fuer fehlende Kontakte, sondern ein Befund zur aktuellen Datenabdeckung.")
    else:
        lines.append("In dieser Weltgruppe bildet Randnaehe keinen klaren Gegenkern.")
        lines.append("Randnaehe erscheint eher als Oberflaeche, Drift, Rekopplung oder kurzlebige Austrittsnaehe.")
    lines.append("")
    lines.append("Die klare Brueckenhierarchie bleibt damit aktuell staerker als eine eigenstaendige Randkern-Hierarchie.")
    if drift_cores or local_young:
        lines.append("")
        lines.append("Zusaetzlich sichtbar:")
        if drift_cores:
            lines.append(f"- `{len(drift_cores)}` starker Driftkern-Kandidat mit hoher Selbstbindung.")
        if local_young:
            lines.append(f"- `{len(local_young)}` lokale junge Selbstinsel mit hoher Selbstbindung.")
        lines.append("Das ist nicht dasselbe wie ein Rand-Gegenkern, zeigt aber, dass Rand-/Driftnaehe eigene Verdichtungsformen ausbilden kann.")
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append("Fachlich bedeutet das:")
    lines.append("")
    lines.append("- Das Zentrum/Bruecken-System besitzt wiederkehrende Kerne.")
    lines.append("- Randnahe Tokens koennen stabil auftreten, wirken aber bisher duenner und weniger netzwerkbildend.")
    lines.append("- Junge Oberflaechen sind nicht automatisch neue Bedeutungsinseln.")
    lines.append("- Rand ist damit eher ein Spannungs- und Oeffnungsbereich als ein eigener stabiler Pol.")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    lines.append(
        "Als naechstes sollte die Randlupe gegen synthetische Randwelten und reale Stresswelten gelegt werden. Ziel: pruefen, ob Randkerne nur unter staerkerer Randdominanz entstehen oder ob sie grundsaetzlich kurzlebig bleiben."
    )
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--paths", required=True, type=Path)
    parser.add_argument("--neighbors", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    path_rows = _read_rows(args.paths)
    neighbor_rows = {row["token"]: row for row in _read_rows(args.neighbors)}
    tokens = _token_set(path_rows)

    out_rows: list[dict[str, str]] = []
    for path_row in path_rows:
        token = path_row.get("token", "")
        if token not in tokens:
            continue
        neigh_row = neighbor_rows.get(token, {})
        row = dict(path_row)
        row.update({k: v for k, v in neigh_row.items() if k not in row})
        row["contacts"] = neigh_row.get("contacts", "")
        row["worlds"] = neigh_row.get("worlds", "")
        row["neighbor_coverage"] = "1" if neigh_row else "0"
        row["countercore_class"] = _classify_countercore(path_row, neigh_row)
        out_rows.append(row)

    out_rows.sort(
        key=lambda row: (
            row["countercore_class"],
            row["path_class"],
            -_int(row.get("contacts")),
            row["token"],
        )
    )
    _write_csv(args.out_csv, out_rows)
    _write_md(args.out_md, out_rows)
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
