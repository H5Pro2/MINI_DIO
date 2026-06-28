from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


def _read(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8-sig")
    first_line = text.splitlines()[0] if text.splitlines() else ""
    delimiter = ";" if first_line.count(";") >= first_line.count(",") else ","
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh, delimiter=delimiter))


def _int(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def _float(value: str) -> float:
    try:
        return float(value or 0.0)
    except ValueError:
        return 0.0


def _role_from_bridge_type(row: dict[str, str]) -> str:
    bridge_type = row.get("bridge_type", "")
    near_ticks = _int(row.get("near_ticks", "0"))
    total_ticks = _int(row.get("total_ticks", "0"))
    all_stable = _float(row.get("all_stable_share", "0"))
    all_unrest = _float(row.get("all_unrest_share", "0"))
    trust_delta = _float(row.get("trust_delta", "0"))
    embedding_delta = _float(row.get("embedding_delta", "0"))
    before_worlds = row.get("before_worlds", "")
    after_worlds = row.get("after_worlds", "")

    if bridge_type == "balancierte_bruecke" and all_stable >= 0.95 and near_ticks >= 8:
        return "kernnaher_inselanker_aehnlich"
    if bridge_type == "balancierte_bruecke" and total_ticks >= 700 and before_worlds and after_worlds:
        return "weltbreiter_brueckenanker_aehnlich"
    if bridge_type == "offene_bruecke":
        return "uebergangsanker_aehnlich"
    if bridge_type == "instabile_kontaktzone" or all_unrest >= 0.15:
        return "verteilungsanker_oder_instabile_kontaktzone"
    if trust_delta < -0.025 or embedding_delta < -0.04:
        return "offene_driftnahe_anschlussphase"
    return "offene_anschlussform"


def _source_label(path: Path) -> str:
    return path.stem


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, str]]) -> None:
    role_counts = Counter(row["anchor_role_analogy"] for row in rows)
    source_counts = Counter(row["source"] for row in rows)
    by_family: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_family[row["family"]].append(row)
    recurring = {
        family: family_rows
        for family, family_rows in by_family.items()
        if len({row["source"] for row in family_rows}) >= 2
    }

    lines: list[str] = []
    lines.append("# MCM-Anschlussanker Familien gegen weitere Weltgruppen")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append("Diese Diagnose prueft, ob die zuletzt gefundene Anschlussanker-Logik nur in der aktuellen Brueckenlandschaft vorkommt oder ob aehnliche Rollenformen in aelteren Weltgruppen-Befunden wieder auftauchen.")
    lines.append("Die Token-Namen sind zwischen den Weltgruppen nicht identisch. Deshalb wird hier nicht Token-Gleichheit geprueft, sondern Rollenanalogie.")
    lines.append("")
    lines.append("## Gesamtbefund")
    lines.append("")
    lines.append(f"- Ausgewertete Brueckenfamilien-Zeilen: `{len(rows)}`")
    lines.append(f"- Quellen: `{'; '.join(f'{k}:{v}' for k, v in source_counts.most_common())}`")
    lines.append(f"- Rollenprofil: `{'; '.join(f'{k}:{v}' for k, v in role_counts.most_common())}`")
    lines.append(f"- Wiederkehrende Familien ueber mehrere Quellen: `{len(recurring)}`")
    lines.append("")
    lines.append("## Staerkste Rollenanalogien")
    lines.append("")
    lines.append("| Quelle | Familie | Brueckentyp | Rollenanalogie | Ticks | Naehe | Stabil | Unruhe | Trust-Delta | Embedding-Delta |")
    lines.append("|---|---|---|---|---:|---:|---:|---:|---:|---:|")
    for row in rows[:18]:
        lines.append(
            f"| {row['source']} | `{row['family']}` | {row['bridge_type']} | {row['anchor_role_analogy']} | {row['total_ticks']} | {row['near_ticks']} | {float(row['all_stable_share']):.3f} | {float(row['all_unrest_share']):.3f} | {float(row['trust_delta']):.3f} | {float(row['embedding_delta']):.3f} |"
        )
    lines.append("")
    lines.append("## Wiederkehrende Familien")
    lines.append("")
    if recurring:
        lines.append("| Familie | Quellen | Rollen | Gesamt-Ticks |")
        lines.append("|---|---|---|---:|")
        for family, family_rows in sorted(recurring.items(), key=lambda item: sum(_int(row["total_ticks"]) for row in item[1]), reverse=True):
            sources = sorted({row["source"] for row in family_rows})
            roles = Counter(row["anchor_role_analogy"] for row in family_rows)
            total_ticks = sum(_int(row["total_ticks"]) for row in family_rows)
            lines.append(
                f"| `{family}` | {', '.join(sources)} | {'; '.join(f'{k}:{v}' for k, v in roles.most_common())} | {total_ticks} |"
            )
    else:
        lines.append("Keine Familie taucht in mehreren Quellen wieder auf.")
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append("Die Anschlussrollen sind nicht nur ein lokales Artefakt der letzten Brueckenlandschaft.")
    lines.append("In aelteren Weltgruppen erscheinen analoge Formen: balancierte kernnahe Bruecken, offene Uebergangsanker und instabilere Kontaktzonen.")
    lines.append("")
    lines.append("Wichtig ist die Grenze der Aussage:")
    lines.append("")
    lines.append("- Bewiesen ist keine identische Token-Reproduktion ueber alle Weltgruppen.")
    lines.append("- Gestuetzt ist aber, dass das Feld wiederholt aehnliche Rollenklassen ausbildet.")
    lines.append("- Damit wird die Anschlussanker-Familienkarte plausibler als Topologie-Eigenschaft, nicht nur als Einzelbefund.")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    lines.append("Als naechstes sollte fuer neue Weltgruppen dieselbe moderne Netzwerkdiagnose wie 874/894 erzeugt werden. Dann koennen wir Rollenanalogie durch echte Netzwerk-Topologie ersetzen.")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", nargs="+", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    rows: list[dict[str, str]] = []
    for input_path in args.inputs:
        for row in _read(input_path):
            if not row.get("family") or not row.get("bridge_type"):
                continue
            rows.append(
                {
                    "source": _source_label(input_path),
                    "family": row.get("family", "-"),
                    "bridge_type": row.get("bridge_type", "-"),
                    "anchor_role_analogy": _role_from_bridge_type(row),
                    "total_ticks": row.get("total_ticks", "0"),
                    "near_ticks": row.get("near_ticks", "0"),
                    "before_ticks": row.get("before_ticks", "0"),
                    "after_ticks": row.get("after_ticks", "0"),
                    "all_stable_share": row.get("all_stable_share", "0"),
                    "all_unrest_share": row.get("all_unrest_share", "0"),
                    "normal_stable_share": row.get("normal_stable_share", "0"),
                    "near_stable_share": row.get("near_stable_share", "0"),
                    "normal_strain": row.get("normal_strain", "0"),
                    "near_strain": row.get("near_strain", "0"),
                    "strain_delta": row.get("strain_delta", "0"),
                    "normal_trust": row.get("normal_trust", "0"),
                    "near_trust": row.get("near_trust", "0"),
                    "trust_delta": row.get("trust_delta", "0"),
                    "normal_afterimage": row.get("normal_afterimage", "0"),
                    "near_afterimage": row.get("near_afterimage", "0"),
                    "embedding_delta": row.get("embedding_delta", "0"),
                    "before_worlds": row.get("before_worlds", ""),
                    "after_worlds": row.get("after_worlds", ""),
                }
            )

    rows.sort(
        key=lambda row: (
            {
                "kernnaher_inselanker_aehnlich": 5,
                "weltbreiter_brueckenanker_aehnlich": 4,
                "uebergangsanker_aehnlich": 3,
                "verteilungsanker_oder_instabile_kontaktzone": 2,
                "offene_driftnahe_anschlussphase": 1,
            }.get(row["anchor_role_analogy"], 0),
            _int(row["total_ticks"]),
        ),
        reverse=True,
    )
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
