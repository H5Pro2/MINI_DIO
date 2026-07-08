from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

RUNS = [
    ("BTC", "real_10k", "debug/cross_anchor_btc2024_5m_10k/dio_mini_lauf_1"),
    ("BTC", "real_17k", "debug/1837_btc_17k/dio_mini_lauf_1"),
    ("BTC", "null_random_10k", "debug/1835_null_random_sign_10k/dio_mini_lauf_1"),
    ("BTC", "null_shuffle_10k", "debug/1835_null_shuffle_10k/dio_mini_lauf_1"),
    ("BTC", "null_random_17k", "debug/1837_btc_null_random_17k/dio_mini_lauf_1"),
    ("BTC", "null_shuffle_17k", "debug/1837_btc_null_shuffle_17k/dio_mini_lauf_1"),
    ("DOGE", "real_10k", "debug/doge_2024_5m_10k/dio_mini_lauf_1"),
    ("DOGE", "real_17k", "debug/1837_doge_17k/dio_mini_lauf_1"),
    ("DOGE", "null_random_10k", "debug/1836_doge_null_random_sign_10k/dio_mini_lauf_1"),
    ("DOGE", "null_shuffle_10k", "debug/1836_doge_null_shuffle_10k/dio_mini_lauf_1"),
    ("DOGE", "null_random_17k", "debug/1837_doge_null_random_17k/dio_mini_lauf_1"),
    ("DOGE", "null_shuffle_17k", "debug/1837_doge_null_shuffle_17k/dio_mini_lauf_1"),
    ("PAXG", "real_10k", "debug/paxg_2024_5m_10k/dio_mini_lauf_1"),
    ("PAXG", "real_17k", "debug/1837_paxg_17k/dio_mini_lauf_1"),
    ("PAXG", "null_random_10k", "debug/1836_paxg_null_random_sign_10k/dio_mini_lauf_1"),
    ("PAXG", "null_shuffle_10k", "debug/1836_paxg_null_shuffle_10k/dio_mini_lauf_1"),
    ("PAXG", "null_random_17k", "debug/1837_paxg_null_random_17k/dio_mini_lauf_1"),
    ("PAXG", "null_shuffle_17k", "debug/1837_paxg_null_shuffle_17k/dio_mini_lauf_1"),
    ("XRP", "real_10k", "debug/xrp_2024_5m_10k/dio_mini_lauf_1"),
    ("XRP", "real_17k", "debug/1837_xrp_17k/dio_mini_lauf_1"),
    ("XRP", "null_random_10k", "debug/1836_xrp_null_random_sign_10k/dio_mini_lauf_1"),
    ("XRP", "null_shuffle_10k", "debug/1836_xrp_null_shuffle_10k/dio_mini_lauf_1"),
    ("XRP", "null_random_17k", "debug/1837_xrp_null_random_17k/dio_mini_lauf_1"),
    ("XRP", "null_shuffle_17k", "debug/1837_xrp_null_shuffle_17k/dio_mini_lauf_1"),
]

OUT_CSV = ROOT / "docs/befunde/1838_MCM_REIFUNGSBAHN_FAMILIENWACHSTUM.csv"
OUT_MD = ROOT / "docs/befunde/1838_MCM_REIFUNGSBAHN_FAMILIENWACHSTUM.md"


def _float(value: object) -> float:
    try:
        out = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if out != out else out


def _read_rows(run_dir: str) -> list[dict[str, str]]:
    path = ROOT / run_dir / "episodes.csv"
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _role(row: dict[str, str]) -> str:
    return (
        row.get("mcm_field_episode_role")
        or row.get("passive_mcm_effect_class")
        or row.get("mcm_field_effect_state")
        or "-"
    )


def _family(row: dict[str, str]) -> str:
    return row.get("symbol_family") or row.get("dominant_family") or "-"


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _profile(asset: str, label: str, run_dir: str) -> dict[str, object]:
    rows = _read_rows(run_dir)
    family_counter: Counter[str] = Counter()
    role_counter: Counter[str] = Counter()
    family_roles: dict[str, Counter[str]] = defaultdict(Counter)
    family_rekopplung: dict[str, list[float]] = defaultdict(list)
    family_strain: dict[str, list[float]] = defaultdict(list)
    family_afterimage: dict[str, list[float]] = defaultdict(list)
    family_temporal: dict[str, list[float]] = defaultdict(list)

    for row in rows:
        family = _family(row)
        role = _role(row)
        family_counter[family] += 1
        role_counter[role] += 1
        family_roles[family][role] += 1
        family_rekopplung[family].append(
            _float(row.get("mcm_adaptive_rekopplung_quality") or row.get("mcm_rekopplung_quality"))
        )
        family_strain[family].append(_float(row.get("mcm_strain_quality")))
        family_afterimage[family].append(_float(row.get("mini_afterimage")))
        family_temporal[family].append(_float(row.get("mini_temporal_trust_support")))

    top_families = [family for family, _ in family_counter.most_common(20)]
    top_rows = []
    for family, count in family_counter.most_common(12):
        top_rows.append(
            {
                "asset": asset,
                "label": label,
                "family": family,
                "count": count,
                "share": count / len(rows) if rows else 0.0,
                "dominant_role": family_roles[family].most_common(1)[0][0],
                "avg_rekopplung": _mean(family_rekopplung[family]),
                "avg_strain": _mean(family_strain[family]),
                "avg_afterimage": _mean(family_afterimage[family]),
                "avg_temporal_trust": _mean(family_temporal[family]),
            }
        )

    return {
        "asset": asset,
        "label": label,
        "run_dir": run_dir,
        "rows": len(rows),
        "unique_families": len(family_counter),
        "unique_roles": len(role_counter),
        "top_families": top_families,
        "top_rows": top_rows,
        "dominant_roles": dict(role_counter.most_common(8)),
    }


def _jaccard(left: list[str], right: list[str]) -> float:
    left_set = set(left)
    right_set = set(right)
    if not left_set and not right_set:
        return 0.0
    return len(left_set & right_set) / len(left_set | right_set)


def _write_csv(rows: list[dict[str, object]]) -> None:
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(profiles: dict[tuple[str, str], dict[str, object]], rows: list[dict[str, object]]) -> None:
    lines = [
        "# 1838 - MCM-Reifungsbahn: Familienwachstum 10k gegen 17k",
        "",
        "## Grundfrage",
        "",
        "Bleiben die sichtbaren Bedeutungsfamilien bei größerem Weltfenster erhalten, oder entstehen neue Rand- und Brückenrollen?",
        "",
        "## Methode",
        "",
        "Verglichen wurden BTC, DOGE, PAXG und XRP jeweils als 10k- und 17k-Realwelt.",
        "Zusätzlich wurden assetnahe Nullwelten gelesen, damit reine Stabilität nicht mit Feldzeitreife verwechselt wird.",
        "",
        "## Kerntabelle",
        "",
        "| Asset | Top20 10k/17k | Familien 10k | Familien 17k | Rollen 10k | Rollen 17k | Real/Random 17k | Real/Shuffle 17k | Lesung |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for asset in ["BTC", "DOGE", "PAXG", "XRP"]:
        real10 = profiles[(asset, "real_10k")]
        real17 = profiles[(asset, "real_17k")]
        null_random17 = profiles[(asset, "null_random_17k")]
        null_shuffle17 = profiles[(asset, "null_shuffle_17k")]
        growth = _jaccard(list(real10["top_families"]), list(real17["top_families"]))
        random_distance = 1.0 - _jaccard(list(real17["top_families"]), list(null_random17["top_families"]))
        shuffle_distance = 1.0 - _jaccard(list(real17["top_families"]), list(null_shuffle17["top_families"]))
        if growth >= 0.75 and min(random_distance, shuffle_distance) >= 0.75:
            reading = "stabile_realnahe_reifung"
        elif growth >= 0.45:
            reading = "teilweise_fortgesetzte_reifung"
        else:
            reading = "neue_familienlage"
        lines.append(
            f"| {asset} | {growth:.3f} | {real10['unique_families']} | {real17['unique_families']} | "
            f"{real10['unique_roles']} | {real17['unique_roles']} | {random_distance:.3f} | {shuffle_distance:.3f} | `{reading}` |"
        )

    lines.extend(
        [
            "",
            "## Staerkste Familien je Realwelt",
            "",
            "| Asset | Lauf | Familie | Anteil | Rolle | Rekopplung | Strain | Nachhall | Feldzeit |",
            "|---|---|---|---:|---|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        if not str(row["label"]).startswith("real"):
            continue
        lines.append(
            f"| {row['asset']} | {row['label']} | `{row['family']}` | {row['share']:.4f} | `{row['dominant_role']}` | "
            f"{row['avg_rekopplung']:.4f} | {row['avg_strain']:.4f} | {row['avg_afterimage']:.4f} | {row['avg_temporal_trust']:.4f} |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die 17k-Fenster zeigen keine einfache Kopie der 10k-Oberfläche.",
            "Ein Teil der Familien bleibt anschlussfähig, gleichzeitig wächst die Breite der Familienräume deutlich.",
            "",
            "Wichtig ist die Trennung zu den Nullwelten:",
            "",
            "- Nullwelten bleiben stabil und breit getragen.",
            "- Die reine Top-Familien-Syntax trennt Realwelt und Nullwelt nicht ausreichend; mehrere Namen tauchen in beiden Lesungen auf.",
            "- Der stärkere Unterschied liegt im Reifungsprofil: Wiederkehr, Rolle, Nachhall, Feldzeit, Kopplung und Nullabstand zusammen.",
            "- Damit ist Stabilität allein kein ausreichender Befund.",
            "",
            "## Schluss",
            "",
            "Mit größerer Weltlänge entsteht kein bloßer Datenhaufen.",
            "MINI_DIO bildet weiter unterscheidbare Bedeutungsräume, die je nach Asset unterschiedlich wachsen.",
            "Der Befund spricht aber nicht für feste Wortbedeutungen aus Namen allein.",
            "Er spricht für eine Reifungsbahn, in der Familien erst durch Rolle, Nachhall, Feldzeit und Kopplungsqualität lesbar werden.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollten die Familienrollen innerhalb der 17k-Realwelten zeitlich segmentiert werden: frühe Phase, Mittelphase, späte Phase. Dann wird sichtbar, ob Reife aus Stabilität, Drift oder Brückenbildung entsteht.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    profiles: dict[tuple[str, str], dict[str, object]] = {}
    top_rows: list[dict[str, object]] = []
    for asset, label, run_dir in RUNS:
        profile = _profile(asset, label, run_dir)
        profiles[(asset, label)] = profile
        top_rows.extend(profile["top_rows"])  # type: ignore[arg-type]
    _write_csv(top_rows)
    _write_md(profiles, top_rows)
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"wrote {OUT_CSV.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
