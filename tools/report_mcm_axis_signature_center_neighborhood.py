from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


PASSIVE_FLAGS = {
    "passive_only": 1,
    "read_by_mini_dio": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
}


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def _short(value: str) -> str:
    return str(value or "").replace("dio_mcm_episode_", "").strip()


def _axis(axis: str) -> tuple[str, str]:
    if "<->" not in axis:
        raise SystemExit(f"axis must use <->: {axis}")
    left, right = axis.split("<->", 1)
    return _short(left), _short(right)


def _float(value: str) -> float:
    try:
        return float(value or 0.0)
    except ValueError:
        return 0.0


def _counter_from_profile(profile: str) -> Counter[str]:
    counter: Counter[str] = Counter()
    for part in str(profile or "").split("|"):
        part = part.strip()
        if not part or ":" not in part:
            continue
        name, count = part.rsplit(":", 1)
        try:
            counter[name.strip()] += int(float(count.strip()))
        except ValueError:
            counter[name.strip()] += 1
    return counter


def _top(counter: Counter[str], limit: int = 7) -> str:
    return " | ".join(f"{key}:{value}" for key, value in counter.most_common(limit)) or "-"


def _node_profiles(rows: list[dict[str, str]], token: str) -> list[dict[str, str]]:
    return [row for row in rows if _short(row.get("token", "")) == token]


def _merge_profile(rows: list[dict[str, str]], key: str) -> str:
    counter: Counter[str] = Counter()
    for row in rows:
        counter.update(_counter_from_profile(row.get(key, "")))
    return _top(counter)


def _avg(rows: list[dict[str, str]], key: str) -> float:
    values = [_float(row.get(key, "")) for row in rows]
    return sum(values) / len(values) if values else 0.0


def _node_summary(rows: list[dict[str, str]], token: str) -> dict[str, object]:
    profiles = _node_profiles(rows, token)
    classes = Counter(row.get("nonbridge_class", "-") for row in profiles)
    zones = Counter(row.get("condensation_zone", "-") for row in profiles)
    roles = Counter(row.get("dominant_role", "-") for row in profiles)
    top_previous = Counter(_short(row.get("top_previous", "")) for row in profiles if row.get("top_previous"))
    top_next = Counter(_short(row.get("top_next", "")) for row in profiles if row.get("top_next"))
    return {
        "token": token,
        "profile_count": len(profiles),
        "observations": sum(int(_float(row.get("observations", ""))) for row in profiles),
        "neighbor_count": sum(int(_float(row.get("neighbor_count", ""))) for row in profiles),
        "classes": _top(classes),
        "zones": _top(zones),
        "roles": _top(roles),
        "top_previous": _top(top_previous),
        "top_next": _top(top_next),
        "evidence_roles": _merge_profile(profiles, "evidence_roles"),
        "evidence_zones": _merge_profile(profiles, "evidence_zones"),
        "evidence_worlds": _merge_profile(profiles, "evidence_worlds"),
        "avg_rekopplung": round(_avg(profiles, "avg_rekopplung"), 6),
        "avg_strain": round(_avg(profiles, "avg_strain"), 6),
        "evidence_avg_rekopplung": round(_avg(profiles, "evidence_avg_rekopplung"), 6),
        "evidence_avg_strain": round(_avg(profiles, "evidence_avg_strain"), 6),
    }


def _best_signature(rows: list[dict[str, str]], signature: str | None) -> dict[str, str]:
    if signature:
        for row in rows:
            if row.get("signature") == signature:
                return row
        raise SystemExit(f"signature not found: {signature}")
    sorted_rows = sorted(
        rows,
        key=lambda row: (
            row.get("recurrence_reading") != "wiederkehrend_rekoppelnd",
            -int(_float(row.get("count", ""))),
            -int(_float(row.get("world_count", ""))),
        ),
    )
    if not sorted_rows:
        raise SystemExit("no signature rows found")
    return sorted_rows[0]


def _build(axis_label: str, signature_rows: list[dict[str, str]], center_rows: list[dict[str, str]], signature: str | None) -> list[dict[str, object]]:
    a, b = _axis(axis_label)
    sig = _best_signature(signature_rows, signature)
    node_a = _node_summary(center_rows, a)
    node_b = _node_summary(center_rows, b)
    combined_zones = Counter()
    combined_zones.update(_counter_from_profile(str(node_a["evidence_zones"])))
    combined_zones.update(_counter_from_profile(str(node_b["evidence_zones"])))
    combined_roles = Counter()
    combined_roles.update(_counter_from_profile(str(node_a["evidence_roles"])))
    combined_roles.update(_counter_from_profile(str(node_b["evidence_roles"])))

    relation = "feldmitte_mit_rekoppelnder_nachbarschaft"
    if "randspannung" in str(node_a["evidence_roles"]) or "randspannung" in str(node_b["evidence_roles"]):
        relation = "feldmitte_mit_randspannungsanteil"
    if "rekopplungszone" in str(node_a["zones"]) and "stabile_bedeutungsinsel" in str(node_b["zones"]):
        relation = "rekopplungsfeld_zu_stabiler_bedeutungsinsel"

    return [
        {
            **PASSIVE_FLAGS,
            "axis": axis_label,
            "signature": sig.get("signature", "-"),
            "signature_count": sig.get("count", "0"),
            "signature_world_count": sig.get("world_count", "0"),
            "signature_worlds": sig.get("worlds", "-"),
            "signature_avg_pressure_delta": sig.get("avg_pressure_delta", "0"),
            "signature_avg_rekopplung_delta": sig.get("avg_rekopplung_delta", "0"),
            "node_a": a,
            "node_a_class": node_a["classes"],
            "node_a_zone": node_a["zones"],
            "node_a_role": node_a["roles"],
            "node_a_top_previous": node_a["top_previous"],
            "node_a_top_next": node_a["top_next"],
            "node_a_avg_rekopplung": node_a["avg_rekopplung"],
            "node_a_avg_strain": node_a["avg_strain"],
            "node_b": b,
            "node_b_class": node_b["classes"],
            "node_b_zone": node_b["zones"],
            "node_b_role": node_b["roles"],
            "node_b_top_previous": node_b["top_previous"],
            "node_b_top_next": node_b["top_next"],
            "node_b_avg_rekopplung": node_b["avg_rekopplung"],
            "node_b_avg_strain": node_b["avg_strain"],
            "combined_evidence_roles": _top(combined_roles),
            "combined_evidence_zones": _top(combined_zones),
            "center_neighborhood_reading": relation,
        }
    ]


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, object]]) -> None:
    row = rows[0]

    def cell(value: object) -> str:
        return str(value).replace("|", "\\|")

    lines = [
        "# MCM-Zentrumsachse: Signatur, Nachbarschaft und Feldmitte",
        "",
        "## Zweck",
        "",
        "Diese Datei liest die staerkste wiederkehrende Kontaktsegment-Signatur gegen Nachbarschaft und Feldmitte.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Ruecklesung",
        "- keine Handlung",
        "- kein Gate",
        "- keine Strategie",
        "",
        "## Achsenprofil",
        "",
        f"- Achse: `{row['axis']}`",
        f"- Signatur: `{row['signature']}`",
        f"- Wiederkehr: {row['signature_count']} Kontakte ueber {row['signature_world_count']} Welten",
        f"- Signatur-Welten: `{row['signature_worlds']}`",
        f"- Pressure-Delta: {row['signature_avg_pressure_delta']}",
        f"- Rekopplung-Delta: {row['signature_avg_rekopplung_delta']}",
        "",
        "## Knotenprofile",
        "",
        "| Knoten | Klasse | Zone | Rolle | Top Previous | Top Next | Rekopplung | Strain |",
        "|---|---|---|---|---|---|---:|---:|",
        f"| `{row['node_a']}` | `{cell(row['node_a_class'])}` | `{cell(row['node_a_zone'])}` | `{cell(row['node_a_role'])}` | `{cell(row['node_a_top_previous'])}` | `{cell(row['node_a_top_next'])}` | {row['node_a_avg_rekopplung']} | {row['node_a_avg_strain']} |",
        f"| `{row['node_b']}` | `{cell(row['node_b_class'])}` | `{cell(row['node_b_zone'])}` | `{cell(row['node_b_role'])}` | `{cell(row['node_b_top_previous'])}` | `{cell(row['node_b_top_next'])}` | {row['node_b_avg_rekopplung']} | {row['node_b_avg_strain']} |",
        "",
        "## Gemeinsame Feldnaehe",
        "",
        f"- Rollenbelege: `{row['combined_evidence_roles']}`",
        f"- Zonenbelege: `{row['combined_evidence_zones']}`",
        f"- Lesung: `{row['center_neighborhood_reading']}`",
        "",
        "## Befund",
        "",
        "Die dominante rekoppelnde Kontaktsegment-Signatur verbindet keine starre Kante,",
        "sondern ein Rekopplungsfeld mit einer zentrumsnahen stabilen Bedeutungsinsel.",
        "",
        "Arbeitsableitung:",
        "",
        "```text",
        "Die Achse wirkt wie eine lokale Mitte-Nachbarschaft:",
        "ein Knoten traegt Rekopplungsfeld, der andere traegt zentrumsnahe Stabilitaet.",
        "```",
        "",
        "## Wie es weitergeht",
        "",
        "Als naechstes sollte diese Mitte-Nachbarschaft gegen neue Folgewelten geprueft werden: bleibt die Beziehung erhalten oder verlagert sie sich erneut?",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--axis", required=True)
    parser.add_argument("--signatures", required=True, type=Path)
    parser.add_argument("--center-candidates", required=True, type=Path)
    parser.add_argument("--signature")
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    rows = _build(args.axis, _read_rows(args.signatures), _read_rows(args.center_candidates), args.signature)
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"rows={len(rows)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
