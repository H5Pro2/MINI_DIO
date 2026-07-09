import argparse
import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


DEFAULT_INPUTS = [
    "debug/multiworld_axis_map/SYN1788_BASE_TO_FOLLOW/real_a/dio_mini_lauf_1/episodes.csv",
    "debug/multiworld_axis_map/SYN1788_BASE_TO_FOLLOW/real_b/dio_mini_lauf_2/episodes.csv",
    "debug/multiworld_axis_map/SYN1788_BASE_TO_SHUFFLE/real_a/dio_mini_lauf_1/episodes.csv",
    "debug/multiworld_axis_map/SYN1788_BASE_TO_SHUFFLE/real_b/dio_mini_lauf_2/episodes.csv",
]


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _clip(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, float(value)))


def _mean(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _fmt(value: object, digits: int = 4) -> str:
    return f"{_float(value):.{digits}f}"


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _source_label(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def _role_from_values(row: dict[str, str], recoupling_factor: float) -> str:
    rec = _clip(_float(row.get("mcm_rekopplung_quality")) * recoupling_factor)
    carry = _clip(_float(row.get("mcm_carry_quality")))
    strain = _clip(_float(row.get("mcm_strain_quality")))
    sensory = _clip(_float(row.get("mcm_sensory_coupling")))
    effect = str(row.get("passive_mcm_effect_class", "") or "")
    awareness = str(row.get("passive_inner_effect_awareness_state", "") or "")

    if strain >= 0.30 and rec < 0.56:
        return "spannungsrand_kippnaehe"
    if rec >= 0.58 and strain <= 0.27 and carry >= 0.50:
        return "rekopplungsnaehe"
    if (effect == "stabil" or awareness == "inner_effect_stable") and rec >= 0.52 and strain <= 0.24:
        return "zentrum_stabil"
    if carry >= 0.46 and strain <= 0.34 and sensory >= 0.48:
        return "offene_variante"
    if rec < 0.42 and carry < 0.46:
        return "diffus_entkoppelt"
    return "gemischte_uebergangsrolle"


def _dominant(counter: Counter[str]) -> str:
    if not counter:
        return "-"
    return counter.most_common(1)[0][0]


def _role_shares(counter: Counter[str], total: int) -> dict[str, float]:
    return {
        "zentrum_share": counter.get("zentrum_stabil", 0) / max(1, total),
        "rekopplung_share": counter.get("rekopplungsnaehe", 0) / max(1, total),
        "open_share": counter.get("offene_variante", 0) / max(1, total),
        "rand_share": counter.get("spannungsrand_kippnaehe", 0) / max(1, total),
        "diffuse_share": counter.get("diffus_entkoppelt", 0) / max(1, total),
        "mixed_share": counter.get("gemischte_uebergangsrolle", 0) / max(1, total),
    }


def _top_families(rows: list[dict[str, str]], role: str, factor: float, limit: int = 8) -> set[str]:
    counter: Counter[str] = Counter()
    for row in rows:
        if _role_from_values(row, factor) == role:
            family = str(row.get("symbol_family", "") or "-")
            if family != "-":
                counter[family] += 1
    return {key for key, _ in counter.most_common(limit)}


def _jaccard(left: set[str], right: set[str]) -> float:
    if not left and not right:
        return 1.0
    return len(left & right) / max(1, len(left | right))


def _stress_state(base: dict[str, float], current: dict[str, float], family_stability: float) -> str:
    core_base = base["zentrum_share"] + base["rekopplung_share"]
    core_current = current["zentrum_share"] + current["rekopplung_share"]
    rand_delta = current["rand_share"] - base["rand_share"]
    diffuse_delta = current["diffuse_share"] - base["diffuse_share"]
    open_delta = current["open_share"] - base["open_share"]

    if core_current <= core_base * 0.45 and (rand_delta > 0.18 or diffuse_delta > 0.18):
        return "topologie_kollabiert_in_rand_oder_diffus"
    if family_stability >= 0.62 and abs(core_current - core_base) <= 0.14:
        return "topologie_stabil_mit_daempfung"
    if family_stability >= 0.45 and open_delta > 0.08:
        return "neue_offene_randvariante"
    if family_stability >= 0.45 and rand_delta > 0.08:
        return "gedaempfte_randvariante"
    if family_stability < 0.30:
        return "familienordnung_verliert_wiedererkennung"
    return "geordnete_verschiebung"


def _summarize_source(path: Path, rows: list[dict[str, str]], factors: list[float]) -> list[dict[str, object]]:
    source = _source_label(path)
    baseline_factor = 1.0
    base_counter: Counter[str] = Counter(_role_from_values(row, baseline_factor) for row in rows)
    base_shares = _role_shares(base_counter, len(rows))
    base_rekopplung_families = _top_families(rows, "rekopplungsnaehe", baseline_factor)
    base_center_families = _top_families(rows, "zentrum_stabil", baseline_factor)
    base_rand_families = _top_families(rows, "spannungsrand_kippnaehe", baseline_factor)

    out: list[dict[str, object]] = []
    for factor in factors:
        counter: Counter[str] = Counter(_role_from_values(row, factor) for row in rows)
        shares = _role_shares(counter, len(rows))
        rek_families = _top_families(rows, "rekopplungsnaehe", factor)
        center_families = _top_families(rows, "zentrum_stabil", factor)
        rand_families = _top_families(rows, "spannungsrand_kippnaehe", factor)
        family_stability = _mean(
            [
                _jaccard(base_rekopplung_families, rek_families),
                _jaccard(base_center_families, center_families),
                _jaccard(base_rand_families, rand_families),
            ]
        )
        avg_rec = _mean([_clip(_float(row.get("mcm_rekopplung_quality")) * factor) for row in rows])
        avg_static_rec = _mean([_clip(_float(row.get("mcm_rekopplung_quality"))) for row in rows])
        state = _stress_state(base_shares, shares, family_stability)
        out.append(
            {
                "source": source,
                "recoupling_factor": round(float(factor), 4),
                "episodes": len(rows),
                "stress_state": state,
                "dominant_role": _dominant(counter),
                "avg_static_rekopplung": round(avg_static_rec, 6),
                "avg_damped_rekopplung": round(avg_rec, 6),
                "zentrum_share": round(shares["zentrum_share"], 6),
                "rekopplung_share": round(shares["rekopplung_share"], 6),
                "open_share": round(shares["open_share"], 6),
                "rand_share": round(shares["rand_share"], 6),
                "diffuse_share": round(shares["diffuse_share"], 6),
                "mixed_share": round(shares["mixed_share"], 6),
                "delta_zentrum": round(shares["zentrum_share"] - base_shares["zentrum_share"], 6),
                "delta_rekopplung": round(shares["rekopplung_share"] - base_shares["rekopplung_share"], 6),
                "delta_open": round(shares["open_share"] - base_shares["open_share"], 6),
                "delta_rand": round(shares["rand_share"] - base_shares["rand_share"], 6),
                "delta_diffuse": round(shares["diffuse_share"] - base_shares["diffuse_share"], 6),
                "family_stability": round(family_stability, 6),
                "top_rekopplung_families": ";".join(sorted(rek_families)),
                "top_center_families": ";".join(sorted(center_families)),
                "top_rand_families": ";".join(sorted(rand_families)),
            }
        )
    return out


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, object]], inputs: list[Path], factors: list[float]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["source"])].append(row)

    final_by_source = [items[-1] for _, items in sorted(grouped.items()) if items]
    state_counts = Counter(str(row["stress_state"]) for row in rows if _float(row["recoupling_factor"]) < 1.0)
    lowest_rows = [row for row in rows if _float(row["recoupling_factor"]) == min(factors)]
    avg_family_stability_low = _mean([_float(row["family_stability"]) for row in lowest_rows])
    avg_rand_delta_low = _mean([_float(row["delta_rand"]) for row in lowest_rows])
    avg_open_delta_low = _mean([_float(row["delta_open"]) for row in lowest_rows])

    lines = [
        "# Wenn-Dann-Stress-Test: Rückführungsdämpfung",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Grundfrage",
        "",
        "Wenn die Rückführung/Rekopplung im Feld gedämpft wird, kollabiert die Topologie oder bildet sie eine geordnete Variante?",
        "",
        "Der Test verändert keine Laufmechanik und keine Memory. Er liest vorhandene Episoden und dämpft die Rekopplungsachse nur in der Auswertung.",
        "",
        "## Eingriff",
        "",
        f"- Faktoren: `{', '.join(_fmt(item, 2) for item in factors)}`",
        "- `1.00` ist die Referenz.",
        "- Kleinere Faktoren simulieren geringere Rückführungswirkung.",
        "- Die Faktoren sind Teststufen, keine festen Regeln.",
        "",
        "## Eingaben",
        "",
    ]
    for item in inputs:
        lines.append(f"- `{_source_label(item)}`")

    lines.extend(
        [
            "",
            "## Gesamtbefund",
            "",
            f"- Zustände unter Dämpfung: `{dict(state_counts)}`",
            f"- Familien-Wiedererkennbarkeit bei stärkster Dämpfung: `{_fmt(avg_family_stability_low)}`",
            f"- mittlere Randverschiebung bei stärkster Dämpfung: `{_fmt(avg_rand_delta_low)}`",
            f"- mittlere Offenheitsverschiebung bei stärkster Dämpfung: `{_fmt(avg_open_delta_low)}`",
            "",
            "## Quellenvergleich",
            "",
            "| Quelle | Faktor | Zustand | dominante Rolle | Zentrum | Rekopplung | Offen | Rand | Diffus | Familien-Stabilität |",
            "|---|---:|---|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        lines.append(
            "| {source} | {recoupling_factor:.2f} | `{stress_state}` | `{dominant_role}` | {zentrum_share:.4f} | {rekopplung_share:.4f} | {open_share:.4f} | {rand_share:.4f} | {diffuse_share:.4f} | {family_stability:.4f} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Dieser Test ist ein methodischer Stresstest, kein Beweis.",
            "",
            "Ein starker Befund wäre: Kernfamilien bleiben teilweise wiedererkennbar, während Rollenanteile kontrolliert in Offenheit, Rand oder Diffusität driften.",
            "",
            "Ein schwacher Befund wäre: Familienordnung verschwindet beliebig oder alle Quellen reagieren gleich, unabhängig von ihrer Ausgangsform.",
            "",
            "## Ergebnisgrenze",
            "",
            "- Der Eingriff ist aktuell eine Auswertungsdämpfung, keine echte erneute Laufberechnung.",
            "- Dadurch zeigt der Test zuerst Sensitivität der Feldlesung, nicht vollständige Systemdynamik.",
            "- Ein nächster härterer Test müsste denselben Faktor direkt in einem isolierten Testlauf anwenden.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def _parse_factors(text: str) -> list[float]:
    factors = []
    for part in str(text or "").split(","):
        part = part.strip()
        if not part:
            continue
        factors.append(_clip(float(part), 0.0, 2.0))
    return sorted(set(factors), reverse=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Passive Wenn-Dann-Stress-Test fuer Rekopplungsdaempfung.")
    parser.add_argument("--input", action="append", help="Episodes CSV. Kann mehrfach angegeben werden.")
    parser.add_argument("--factors", default="1.0,0.9,0.75,0.5")
    parser.add_argument("--out-md", default="docs/befunde/1001-2000/1751-2000/1820_RUECKFUEHRUNG_DAEMPFUNG_STRESSTEST.md")
    parser.add_argument("--out-csv", default="docs/befunde/1001-2000/1751-2000/1820_RUECKFUEHRUNG_DAEMPFUNG_STRESSTEST.csv")
    args = parser.parse_args()

    inputs = [_resolve(item) for item in (args.input or DEFAULT_INPUTS)]
    factors = _parse_factors(args.factors)
    if 1.0 not in factors:
        factors = sorted(set([1.0, *factors]), reverse=True)

    rows: list[dict[str, object]] = []
    used_inputs: list[Path] = []
    for source in inputs:
        if not source.exists():
            continue
        source_rows = _read_csv(source)
        if not source_rows:
            continue
        rows.extend(_summarize_source(source, source_rows, factors))
        used_inputs.append(source)

    out_csv = _resolve(args.out_csv)
    out_md = _resolve(args.out_md)
    _write_csv(out_csv, rows)
    _write_md(out_md, rows, used_inputs, factors)
    print({"out_md": str(out_md.relative_to(ROOT)), "out_csv": str(out_csv.relative_to(ROOT)), "rows": len(rows)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
