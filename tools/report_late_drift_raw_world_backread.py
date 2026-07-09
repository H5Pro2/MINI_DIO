from __future__ import annotations

import csv
from pathlib import Path

from befunde_paths import befunde_root
from statistics import mean, pstdev


ROOT = Path(__file__).resolve().parents[1]
INPUT = befunde_root(ROOT) / "1955_SPAETE_DRIFTROLLEN_REPRODUKTION.csv"
OUT_CSV = befunde_root(ROOT) / "1956_SPAETE_DRIFTROLLEN_ROHWELT_RUECKLESUNG.csv"
OUT_MD = befunde_root(ROOT) / "1956_SPAETE_DRIFTROLLEN_ROHWELT_RUECKLESUNG.md"

WORLD_EPISODES = {
    "SOL2024_15M": ROOT / "debug" / "research_chain_sol_2024_15m_2k" / "dio_mini_lauf_2" / "episodes.csv",
    "SOL2024_30M": ROOT / "debug" / "research_chain_sol_2024_30m_2k" / "dio_mini_lauf_2" / "episodes.csv",
    "SOL2025_15M": ROOT / "debug" / "research_chain_sol_2025_15m_2k" / "dio_mini_lauf_2" / "episodes.csv",
    "SOL2025_30M": ROOT / "debug" / "research_chain_sol_2025_30m_2k" / "dio_mini_lauf_2" / "episodes.csv",
    "STABLE10K_REPRO": ROOT / "debug" / "world_relative_topology_stable_10k_repro" / "dio_mini_lauf_1" / "episodes.csv",
    "STRESS10K_REPRO": ROOT / "debug" / "world_relative_topology_stress_10k_repro" / "dio_mini_lauf_1" / "episodes.csv",
}

NUMERIC_FIELDS = [
    "sehen_form_flow",
    "sehen_form_stability",
    "sehen_form_change",
    "hoeren_energy_tone",
    "hoeren_energy_shift",
    "fuehlen_mcm_coherence",
    "fuehlen_mcm_tension",
    "fuehlen_mcm_asymmetry",
    "mcm_carry_quality",
    "mcm_strain_quality",
    "mcm_rekopplung_quality",
    "mcm_sensory_coupling",
    "mcm_visual_field_gap",
    "mcm_hearing_field_gap",
    "mini_afterimage",
    "mini_recurrence_strength",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def to_float(value: str | None) -> float | None:
    if value is None:
        return None
    value = str(value).strip()
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def avg(values: list[float]) -> str:
    return f"{mean(values):.6f}" if values else ""


def std(values: list[float]) -> str:
    return f"{pstdev(values):.6f}" if len(values) > 1 else ""


def classify_visual(row: dict[str, str]) -> str:
    flow = to_float(row.get("avg_sehen_form_flow")) or 0.0
    stability = to_float(row.get("avg_sehen_form_stability")) or 0.0
    change = to_float(row.get("avg_sehen_form_change")) or 0.0
    parts: list[str] = []
    if stability >= 0.45:
        parts.append("sichtbar_stabile_form")
    elif stability <= -0.20:
        parts.append("instabile_formaufnahme")
    else:
        parts.append("offene_formaufnahme")
    if abs(flow) >= 0.45:
        parts.append("gerichteter_formfluss")
    if abs(change) >= 0.45:
        parts.append("starker_formwechsel")
    return "+".join(parts)


def classify_hearing(row: dict[str, str]) -> str:
    tone = to_float(row.get("avg_hoeren_energy_tone")) or 0.0
    shift = to_float(row.get("avg_hoeren_energy_shift")) or 0.0
    if abs(shift) >= 0.45:
        return "starker_energie_shift"
    if abs(tone) >= 0.35:
        return "deutlicher_energieton"
    return "gedaempfte_energie"


def classify_field(row: dict[str, str]) -> str:
    tension = to_float(row.get("avg_fuehlen_mcm_tension")) or 0.0
    strain = to_float(row.get("avg_mcm_strain_quality")) or 0.0
    rekopplung = to_float(row.get("avg_mcm_rekopplung_quality")) or 0.0
    sensory = to_float(row.get("avg_mcm_sensory_coupling")) or 0.0
    source_open = to_float(row.get("source_avg_open_share")) or 0.0
    if tension >= 0.35 or strain >= 0.30:
        return "angespannte_feldwirkung"
    if rekopplung >= 0.65 and strain <= 0.20:
        return "rekoppelnd_entlastet"
    if source_open >= 0.50:
        return "offene_feldlage"
    if sensory >= 0.50:
        return "gekoppelte_feldlage"
    return "gemischte_feldlage"


def matches(row: dict[str, str], family: str, tokens: set[str]) -> bool:
    candidates = {
        row.get("symbol", ""),
        row.get("symbol_family", ""),
        row.get("episode_memory_symbol", ""),
        row.get("mcm_field_episode_symbol", ""),
        row.get("mcm_field_episode_preview_symbol", ""),
        row.get("passive_inner_awareness_symbol_family", ""),
    }
    return family in candidates or bool(tokens.intersection(candidates))


def aggregate_rows(rows: list[dict[str, str]], source: dict[str, str], world: str, path: Path) -> dict[str, str]:
    ticks = [int(v) for v in (r.get("tick", "") for r in rows) if str(v).isdigit()]
    out: dict[str, str] = {
        "family": source["family"],
        "late_role_reading": source["late_role_reading"],
        "repro_reading": source["repro_reading"],
        "world": world,
        "episode_path": str(path.relative_to(ROOT)),
        "matched_rows": str(len(rows)),
        "tick_min": str(min(ticks)) if ticks else "",
        "tick_max": str(max(ticks)) if ticks else "",
        "source_observations_total": source.get("observations_total", ""),
        "source_neighbor_count_total": source.get("neighbor_count_total", ""),
        "source_avg_rekopplung": source.get("avg_rekopplung", ""),
        "source_avg_strain": source.get("avg_strain", ""),
        "source_avg_center_share": source.get("avg_center_share", ""),
        "source_avg_open_share": source.get("avg_open_share", ""),
        "source_avg_rand_share": source.get("avg_rand_share", ""),
    }
    for field in NUMERIC_FIELDS:
        values = [value for row in rows if (value := to_float(row.get(field))) is not None]
        out[f"avg_{field}"] = avg(values)
        out[f"std_{field}"] = std(values)
        out[f"min_{field}"] = f"{min(values):.6f}" if values else ""
        out[f"max_{field}"] = f"{max(values):.6f}" if values else ""
    out["visual_reading"] = classify_visual(out)
    out["hearing_reading"] = classify_hearing(out)
    out["field_reading"] = classify_field(out)
    out["raw_backread_status"] = "ruecklesbar" if rows else "keine_passende_episode"
    return out


def build_report() -> list[dict[str, str]]:
    sources = [row for row in read_csv(INPUT) if row.get("repro_reading") != "spaet_lokal"]
    output_rows: list[dict[str, str]] = []
    episode_cache: dict[Path, list[dict[str, str]]] = {}

    for source in sources:
        family = source["family"]
        tokens = {token.strip() for token in source.get("tokens", "").split(",") if token.strip()}
        worlds = [world.strip() for world in source.get("worlds", "").split(",") if world.strip()]
        for world in worlds:
            path = WORLD_EPISODES.get(world)
            if path is None or not path.exists():
                output_rows.append(
                    {
                        "family": family,
                        "late_role_reading": source["late_role_reading"],
                        "repro_reading": source["repro_reading"],
                        "world": world,
                        "episode_path": str(path.relative_to(ROOT)) if path else "",
                        "matched_rows": "0",
                        "tick_min": "",
                        "tick_max": "",
                        "source_observations_total": source.get("observations_total", ""),
                        "source_neighbor_count_total": source.get("neighbor_count_total", ""),
                        "source_avg_rekopplung": source.get("avg_rekopplung", ""),
                        "source_avg_strain": source.get("avg_strain", ""),
                        "source_avg_center_share": source.get("avg_center_share", ""),
                        "source_avg_open_share": source.get("avg_open_share", ""),
                        "source_avg_rand_share": source.get("avg_rand_share", ""),
                        "visual_reading": "",
                        "hearing_reading": "",
                        "field_reading": "",
                        "raw_backread_status": "episode_pfad_fehlt",
                    }
                )
                continue
            episodes = episode_cache.setdefault(path, read_csv(path))
            matching_rows = [row for row in episodes if matches(row, family, tokens)]
            output_rows.append(aggregate_rows(matching_rows, source, world, path))
    return output_rows


def write_csv(rows: list[dict[str, str]]) -> None:
    base_fields = [
        "family",
        "late_role_reading",
        "repro_reading",
        "world",
        "episode_path",
        "matched_rows",
        "tick_min",
        "tick_max",
        "source_observations_total",
        "source_neighbor_count_total",
        "source_avg_rekopplung",
        "source_avg_strain",
        "source_avg_center_share",
        "source_avg_open_share",
        "source_avg_rand_share",
    ]
    numeric_fields = []
    for field in NUMERIC_FIELDS:
        numeric_fields.extend([f"avg_{field}", f"std_{field}", f"min_{field}", f"max_{field}"])
    fields = base_fields + numeric_fields + ["visual_reading", "hearing_reading", "field_reading", "raw_backread_status"]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_md(rows: list[dict[str, str]]) -> None:
    readable = [row for row in rows if row.get("raw_backread_status") == "ruecklesbar"]
    visual_counts: dict[str, int] = {}
    hearing_counts: dict[str, int] = {}
    field_counts: dict[str, int] = {}
    for row in readable:
        visual_counts[row["visual_reading"]] = visual_counts.get(row["visual_reading"], 0) + 1
        hearing_counts[row["hearing_reading"]] = hearing_counts.get(row["hearing_reading"], 0) + 1
        field_counts[row["field_reading"]] = field_counts.get(row["field_reading"], 0) + 1

    top = sorted(readable, key=lambda r: int(r.get("matched_rows") or 0), reverse=True)[:8]
    lines = [
        "# 1956 - Rohwelt-Rücklesung der späten Driftrollen",
        "",
        "## Hierarchie der Prüfung",
        "",
        "- Grundfrage: Welche Außenweltlage begleitet reproduzierte späte Driftrollen?",
        "- Unterprüfung: Sehen, Hören und Fühlen werden aus den rücklesbaren Episodenzeilen gelesen.",
        "- Folgeschritt: Erst nach weiterer Prüfung darf daraus eine Aussage entstehen, ob bestimmte Sinneslagen Driftrollen begünstigen.",
        "",
        "## Datengrundlage",
        "",
        f"- Ausgangsbefund: `{INPUT.relative_to(ROOT)}`",
        f"- Rücklese-Tabelle: `{OUT_CSV.relative_to(ROOT)}`",
        f"- geprüfte Familien/Welt-Kombinationen: {len(rows)}",
        f"- davon rücklesbar: {len(readable)}",
        "",
        "## Kurzbefund",
        "",
        "Die reproduzierten späten Driftrollen sind nicht gleichmäßig verteilt. Sie lassen sich in den verfügbaren Episoden vor allem als Kombination aus offener Feldlage, gedämpfter oder verschobener Energie und unterschiedlich stabiler Sicht zurücklesen.",
        "",
        "Das ist kein Kausalbeweis. Es ist eine passive Rücklesung: Die Tabelle zeigt, welche Rohwelt- und Sinneslage im Moment der späteren Rolle gemeinsam sichtbar war.",
        "",
        "## Verteilung der Rücklesung",
        "",
        "### Sehen",
    ]
    for key, value in sorted(visual_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- {key}: {value}")
    lines.extend(["", "### Hören"])
    for key, value in sorted(hearing_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- {key}: {value}")
    lines.extend(["", "### Feldwirkung"])
    for key, value in sorted(field_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- {key}: {value}")

    lines.extend(
        [
            "",
            "## Stärkste rücklesbare Beispiele",
            "",
            "| Familie | Welt | Treffer | Tickbereich | Sehen | Hören | Feld |",
            "|---|---:|---:|---:|---|---|---|",
        ]
    )
    for row in top:
        lines.append(
            "| {family} | {world} | {matched_rows} | {tick_min}-{tick_max} | {visual_reading} | {hearing_reading} | {field_reading} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Arbeitsdeutung",
            "",
            "- Späte offene Varianz ist häufig keine bloße Leere. Sie erscheint oft mit sichtbarer Formbewegung oder Energieverschiebung, aber noch ohne starke Zentrenbindung.",
            "- Einzelne Familien wie `dio_0nu8` werden in mehreren Welten rücklesbar und tragen damit den Charakter einer wiederkehrenden späten offenen Lage.",
            "- Zentrumskandidaten bleiben in dieser Rücklesung unterscheidbar, weil sie bei ähnlicher Außenweltspannung eine höhere Rekopplung und geringere Belastung zeigen können.",
            "- Spannungsrandnahe Kandidaten bleiben dünner und brauchen weitere Prüfung gegen größere Weltfenster.",
            "",
            "## Grenze der Aussage",
            "",
            "Diese Prüfung sagt nicht: Eine bestimmte Rohweltlage erzeugt zwingend eine Driftrolle. Sie sagt nur: Bei den reproduzierten späten Rollen ist eine strukturierte Rücklesung möglich. Damit ist die nächste Prüffrage fachlich enger.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte geprüft werden, ob diese Rohweltprofile in einer neuen Welt vor der Rollenbildung sichtbar werden. Wenn ja, wäre das ein stärkerer Hinweis darauf, dass Mini-DIO nicht nur nachträglich benennt, sondern Feldlagen früh als mögliche Driftrollen vorbereitet.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    rows = build_report()
    write_csv(rows)
    write_md(rows)
    print(f"rows={len(rows)} readable={sum(1 for row in rows if row.get('raw_backread_status') == 'ruecklesbar')}")
    print(OUT_CSV.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
