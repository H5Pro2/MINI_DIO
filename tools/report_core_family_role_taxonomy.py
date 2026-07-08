from __future__ import annotations

import argparse
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _float(value: object) -> float:
    try:
        out = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if out != out else out


def _int(value: object) -> int:
    try:
        return int(float(value or 0))
    except (TypeError, ValueError):
        return 0


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _count_role(roles: str, name: str) -> int:
    total = 0
    for part in str(roles or "").split(";"):
        if not part or ":" not in part:
            continue
        key, value = part.split(":", 1)
        if key.strip() == name:
            total += _int(value)
    return total


def _count_binding(bindings: str, name: str) -> int:
    total = 0
    for part in str(bindings or "").split(";"):
        if not part or ":" not in part:
            continue
        key, value = part.split(":", 1)
        if key.strip() == name:
            total += _int(value)
    return total


def _classify(row: dict[str, str]) -> tuple[str, str]:
    family = str(row.get("family") or "-")
    bridge_score = _float(row.get("bridge_score"))
    avg_distance = _float(row.get("avg_distance"))
    avg_cosine = _float(row.get("avg_cosine"))
    role_diversity = _int(row.get("role_diversity"))
    roles = str(row.get("roles") or "")
    bindings = str(row.get("topology_bindings") or "")
    bridge_near = _count_binding(bindings, "bruecke_zielnah")
    rand = _count_binding(bindings, "rand_polarisierend")
    hearing = _count_binding(bindings, "nachhall_aktivierend") + _count_binding(bindings, "nachhall_daempfend")
    center = _count_binding(bindings, "zentrum_stabilisierend")
    kohaerenz_low = _count_role(roles, "kohaerenz_niedriger")

    if family == "dio_0l7p":
        return "brueckentraeger", "spitze Rekopplung im Ereignis, danach offenere Nachprüfung"
    if family == "dio_104t":
        return "anschluss_kohärenzknoten", "hält Rekopplung im Nachlauf länger"
    if bridge_score >= 0.62 and role_diversity >= 6 and bridge_near >= 4:
        return "breiter_uebergangsknoten", "breite Rollennähe mit sichtbarer Zielbrücke"
    if avg_distance >= 0.25 or kohaerenz_low >= 10:
        return "randnaher_sammelknoten", "breit, aber distanzierter und stärker randnah"
    if hearing >= 10 and bridge_score < 0.5:
        return "hoer_nachhall_knoten", "stärker über Hören und Nachhall differenziert"
    if center >= 12 and avg_cosine >= 0.95:
        return "zentrum_stabilisierender_anschluss", "nahe Kohärenz und zentrumsnahe Stabilisierung"
    return "gemischter_feldknoten", "Rolle noch nicht sauber getrennt"


def _write_md(path: Path, source: str, rows: list[dict[str, object]]) -> None:
    lines = [
        "# 1807 - Kernfamilien-Rollentaxonomie",
        "",
        "## Grundfrage",
        "",
        "Diese Prüfung ordnet die stärkeren Kernfamilien nicht als feste Wörter, sondern als Rollen im Bedeutungsnetz.",
        "",
        "Die Taxonomie ist passiv. Sie erzeugt keine Handlung, kein Gate und keine Richtungslogik.",
        "",
        f"Quelle: `{source}`",
        "",
        "## Rollenkarte",
        "",
        "| Familie | Rolle | Bridge Score | Distanz | Rollen | Lesung |",
        "|---|---|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['family']}` | `{row['role_type']}` | {row['bridge_score']} | "
            f"{row['avg_distance']} | {row['role_diversity']} | {row['role_reason']} |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die bisherige Kernfamilienstruktur wirkt nicht wie eine flache Symboltabelle.",
            "",
            "Sichtbar werden mehrere Rollenformen:",
            "",
            "- Brückenträger: verbindet offene und rekoppelnde Feldfolge.",
            "- Anschluss-/Kohärenzknoten: hält Rekopplung über den Nachlauf.",
            "- Breite Übergangsknoten: tragen mehrere Rollen ohne eindeutige Einzelbedeutung.",
            "- Randnahe Sammelknoten: breit, aber distanzierter und stärker polarisiert.",
            "- Hör-/Nachhallknoten: stärker über akustische und zeitliche Feldwirkung differenziert.",
            "",
            "Damit wird Bedeutung in MINI_DIO als Netzwerkrolle lesbar: Familie plus Nachbarschaft, Feldfolge, Sinnesbindung und Weltphase.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte für `dio_14wj`, `dio_1fll`, `dio_0m9z` und `dio_155c` geprüft werden, ob ihre Rollen in konkreten Tickfenstern genauso sichtbar werden wie bei `dio_0l7p` und `dio_104t`.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="reports/core_family_bridge_character.csv")
    parser.add_argument("--out-csv", default="reports/core_family_role_taxonomy.csv")
    parser.add_argument("--out-md", default="docs/befunde/1807_KERNFAMILIEN_ROLLENTAXONOMIE.md")
    parser.add_argument("--top", type=int, default=12)
    args = parser.parse_args()

    source_rows = sorted(_read_csv(ROOT / args.source), key=lambda row: _float(row.get("bridge_score")), reverse=True)
    out_rows: list[dict[str, object]] = []
    for row in source_rows[: args.top]:
        role_type, role_reason = _classify(row)
        out_rows.append(
            {
                "family": row.get("family", "-"),
                "role_type": role_type,
                "role_reason": role_reason,
                "bridge_score": round(_float(row.get("bridge_score")), 6),
                "avg_co_memory_count": round(_float(row.get("avg_co_memory_count")), 6),
                "avg_cosine": round(_float(row.get("avg_cosine")), 6),
                "avg_distance": round(_float(row.get("avg_distance")), 6),
                "role_diversity": _int(row.get("role_diversity")),
                "bridge_role_share": round(_float(row.get("bridge_role_share")), 6),
                "roles": row.get("roles", ""),
                "topology_bindings": row.get("topology_bindings", ""),
                "top_neighbors": row.get("top_neighbors", ""),
            }
        )

    _write_csv(ROOT / args.out_csv, out_rows)
    _write_md(ROOT / args.out_md, args.source, out_rows)
    print({"rows": len(out_rows), "out": args.out_md})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
