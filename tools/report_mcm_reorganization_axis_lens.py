from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


TARGET_STATUSES = {
    "reorganisation_oder_drift",
    "rollendrift",
    "entlastung",
    "neue_vierte_welt_insel",
}


def _read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _short(token: str) -> str:
    return token.replace("dio_mcm_episode_", "")


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _by_short(rows: list[dict[str, str]], token_key: str = "token") -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for row in rows:
        token = row.get("short_token") or _short(row.get(token_key, ""))
        if token:
            out[token] = row
    return out


def _axis_profile(drift: dict[str, str] | None, diff: dict[str, str]) -> tuple[str, str]:
    if drift is None:
        return "neu_ohne_basisdrift", "Token erscheint in der vierten Landschaft, ist aber nicht in der Basis-Driftmatrix enthalten."
    rek = _float(drift.get("rekopplung_delta"))
    strain = _float(drift.get("strain_delta"))
    loud = _float(drift.get("loudness_delta"))
    blur = _float(drift.get("visual_blur_delta"))
    tension = _float(drift.get("tension_delta"))
    sensory = _float(drift.get("sensory_delta"))
    movement = drift.get("movement", "-")
    base_zone = drift.get("base_zone", "-")
    follow_zone = drift.get("follow_zone", "-")

    if follow_zone == "junge_spur":
        return "oberflaechen_verjuengung", "Hoeherer Uebergang faellt in junge Spur; eher Entlastung/Oberflaeche als neue Reife."
    if base_zone == "junge_spur" and follow_zone == "driftzone":
        return "junge_drift_oeffnung", "Junge Spur oeffnet zur Driftzone; neue Insel ist sichtbar, aber noch nicht gereift."
    if rek < -0.006 and strain > 0.006 and blur > 0.035:
        return "rekopplung_verliert_unschaerfe_steigt", "Rekopplung sinkt, Strain und visuelle Unschaerfe steigen; typisches Reorganisationssignal."
    if diff.get("status") == "reorganisation_oder_drift" and movement == "stabil":
        return "rollenverlust_in_stabiler_zone", "Zone bleibt stabil, aber die Rollenqualitaet verliert Bindung; Reorganisation liegt in Rolle, nicht in Zone."
    if sensory > 0.10 and rek > 0.05 and tension < -0.05:
        return "sensorische_rekopplung_entlastet", "Sinneskopplung und Rekopplung steigen, Spannung faellt; neue Spur wirkt entlastend."
    if loud > 0.04 and blur < -0.04:
        return "tonische_aktivierung_schaerfung", "Lautheit steigt und Unschaerfe faellt; Aktivierung wird schaerfer statt chaotischer."
    return "offene_achsenmischung", "Keine dominante Einzelachse; vermutlich gemischte Feldbewegung."


def _rows(diff_rows: list[dict[str, str]], drift_rows: list[dict[str, str]], landscape_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    drift = _by_short(drift_rows)
    landscape = _by_short(landscape_rows)
    out: list[dict[str, str]] = []
    for diff in diff_rows:
        if diff.get("status") not in TARGET_STATUSES:
            continue
        short = diff.get("short_token", "")
        drift_row = drift.get(short)
        landscape_row = landscape.get(short, {})
        axis_profile, axis_reason = _axis_profile(drift_row, diff)
        out.append(
            {
                "short_token": short,
                "status": diff.get("status", "-"),
                "trend": diff.get("trend", "-"),
                "read_state": diff.get("read_state", "-"),
                "axis_profile": axis_profile,
                "axis_reason": axis_reason,
                "current_class": landscape_row.get("anchor_class", diff.get("L923_class", "-")),
                "current_weight": landscape_row.get("total_weight", diff.get("L923_weight", "0")),
                "base_zone": (drift_row or {}).get("base_zone", "-"),
                "follow_zone": (drift_row or {}).get("follow_zone", "-"),
                "movement": (drift_row or {}).get("movement", "-"),
                "observation_delta": (drift_row or {}).get("observation_delta", "0"),
                "world_delta": (drift_row or {}).get("world_delta", "0"),
                "rekopplung_delta": f"{_float((drift_row or {}).get('rekopplung_delta')):.6f}",
                "strain_delta": f"{_float((drift_row or {}).get('strain_delta')):.6f}",
                "sensory_delta": f"{_float((drift_row or {}).get('sensory_delta')):.6f}",
                "tension_delta": f"{_float((drift_row or {}).get('tension_delta')):.6f}",
                "loudness_delta": f"{_float((drift_row or {}).get('loudness_delta')):.6f}",
                "visual_blur_delta": f"{_float((drift_row or {}).get('visual_blur_delta')):.6f}",
            }
        )
    out.sort(key=lambda row: (row["axis_profile"], row["short_token"]))
    return out


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, str]]) -> None:
    counts = Counter(row["axis_profile"] for row in rows)
    lines: list[str] = []
    lines.append("# MCM-Reorganisationsachsen der vierten Welt")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append("Diese Diagnose isoliert Tokens, die in der vierten Welt neu erscheinen, entlasten, driften oder reorganisieren.")
    lines.append("Gelesen werden die Achsen der Driftmatrix: Rekopplung, Strain, Sinneskopplung, Spannung, Lautheit und visuelle Unschaerfe.")
    lines.append("")
    lines.append("## Achsenprofil")
    lines.append("")
    lines.append("| Achsenprofil | Anzahl |")
    lines.append("|---|---:|")
    for name, count in counts.most_common():
        lines.append(f"| {name} | {count} |")
    lines.append("")
    lines.append("## Tokens")
    lines.append("")
    lines.append("| Token | Status | Aktuelle Rolle | Achsenprofil | Bewegung | Zonen | Rekopplung | Strain | Lautheit | Blur |")
    lines.append("|---|---|---|---|---|---|---:|---:|---:|---:|")
    for row in rows:
        lines.append(
            f"| `{row['short_token']}` | {row['status']} | {row['current_class']} | {row['axis_profile']} | {row['movement']} | {row['base_zone']} -> {row['follow_zone']} | {row['rekopplung_delta']} | {row['strain_delta']} | {row['loudness_delta']} | {row['visual_blur_delta']} |"
        )
    lines.append("")
    lines.append("## Befund")
    lines.append("")
    lines.append("Die Reorganisationsgruppe ist klein und nicht homogen.")
    lines.append("Es gibt mindestens drei unterschiedliche Lesarten: junge Drift/Oberflaeche, Rollenverlust innerhalb stabiler Zone und echte Achsenreorganisation mit sinkender Rekopplung bei steigender Unschaerfe.")
    lines.append("Damit ist Reorganisation im MCM-Feld nicht gleich Fehler oder Kollaps. Sie kann neue Spur, Entlastung oder Umbau einer bestehenden Rolle sein.")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    lines.append("Als naechstes sollte diese Achsenlupe gegen eine weitere Folgewelt gelesen werden: Bleiben die neuen jungen Spuren jung, verschwinden sie, oder reifen sie zu Anschlussankern?")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--differentiation", required=True, type=Path)
    parser.add_argument("--drift", required=True, type=Path)
    parser.add_argument("--landscape", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    rows = _rows(_read(args.differentiation), _read(args.drift), _read(args.landscape))
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
