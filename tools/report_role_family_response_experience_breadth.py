from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
from statistics import mean, median, pstdev

try:
    from tools.report_role_family_response_memory import _fmt, _resolve, _write_csv
    from tools.run_role_family_matched_pseudo_controls import _empirical_percentile
except ModuleNotFoundError:
    from report_role_family_response_memory import _fmt, _resolve, _write_csv
    from run_role_family_matched_pseudo_controls import _empirical_percentile


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = ROOT / "docs" / "befunde" / "2001-3000"
DEFAULT_MEMORY = BEFUNDE / "2087_PASSIVE_ANTWORT_MEMORY_WIDERSPRUCHSREIFUNG.csv"
DEFAULT_OUT_PREFIX = BEFUNDE / "2088_PASSIVE_ANTWORT_ERFAHRUNGSBREITE"
AXES = (
    ("continuity", "delta_continuity", "percentile_continuity"),
    ("event_share", "delta_event_share", "percentile_event_share"),
    ("member_coverage", "delta_member_coverage", "percentile_member_coverage"),
)
FORBIDDEN_FIELDS = {
    "observed_relation",
    "expected_relation",
    "response_class",
    "meaning",
    "confirmed",
    "prediction",
}
ACTIVE_FLAGS = (
    "read_by_mini_dio",
    "influences_action",
    "is_gate",
    "is_motoric",
    "is_entry_signal",
    "is_direction_signal",
)


def _load_csv(path: Path) -> list[dict[str, str]]:
    import csv

    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _sign(value: float) -> int:
    if value > 0.0:
        return 1
    if value < 0.0:
        return -1
    return 0


def _persistence(signs: list[int]) -> float:
    return abs(sum(signs)) / len(signs) if signs else 0.0


def _axis_rows(memory_rows: list[dict[str, str]]) -> list[dict[str, object]]:
    by_response: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in memory_rows:
        by_response[str(row["response_symbol"])].append(row)
    out: list[dict[str, object]] = []
    for response_symbol, observations in sorted(by_response.items()):
        first = observations[0]
        by_source: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in observations:
            by_source[str(row["evidence_id"])].append(row)
        source_ids = sorted(by_source)
        for axis, value_field, percentile_field in AXES:
            values = [_safe_float(row[value_field]) for row in observations]
            percentiles = [
                _safe_float(row[percentile_field]) for row in observations
            ]
            center = median(values)
            signs = [_sign(value) for value in values]
            source_means = [
                mean(_safe_float(row[value_field]) for row in by_source[source_id])
                for source_id in source_ids
            ]
            source_signs = [_sign(value) for value in source_means]
            out.append(
                {
                    "role_family": first["role_family"],
                    "component": first["component"],
                    "response_symbol": response_symbol,
                    "response_axis": axis,
                    "observations": len(values),
                    "evidence_sources": len(source_ids),
                    "mean_value": mean(values),
                    "median_value": center,
                    "population_stdev": pstdev(values),
                    "median_absolute_deviation": median(
                        abs(value - center) for value in values
                    ),
                    "minimum_value": min(values),
                    "maximum_value": max(values),
                    "positive_observations": signs.count(1),
                    "negative_observations": signs.count(-1),
                    "zero_observations": signs.count(0),
                    "positive_share": signs.count(1) / len(signs),
                    "negative_share": signs.count(-1) / len(signs),
                    "observation_directional_persistence": _persistence(signs),
                    "mean_null_percentile": mean(percentiles),
                    "source_positive_means": source_signs.count(1),
                    "source_negative_means": source_signs.count(-1),
                    "source_zero_means": source_signs.count(0),
                    "source_directional_persistence": _persistence(source_signs),
                    "source_mean_range": max(source_means) - min(source_means),
                    "source_sign_switches": sum(
                        left != right
                        for left, right in zip(source_signs, source_signs[1:])
                    ),
                    "source_ids": ";".join(source_ids),
                    "source_mean_path": ";".join(_fmt(value, 6) for value in source_means),
                    "source_sign_path": ";".join(str(value) for value in source_signs),
                }
            )
    for axis, _, _ in AXES:
        selected = [row for row in out if row["response_axis"] == axis]
        observation_persistence = [
            _safe_float(row["observation_directional_persistence"])
            for row in selected
        ]
        source_persistence = [
            _safe_float(row["source_directional_persistence"]) for row in selected
        ]
        deviations = [
            _safe_float(row["median_absolute_deviation"]) for row in selected
        ]
        source_ranges = [_safe_float(row["source_mean_range"]) for row in selected]
        for row in selected:
            row["axis_observation_persistence_percentile"] = _empirical_percentile(
                observation_persistence,
                _safe_float(row["observation_directional_persistence"]),
            )
            row["axis_source_persistence_percentile"] = _empirical_percentile(
                source_persistence,
                _safe_float(row["source_directional_persistence"]),
            )
            row["axis_mad_percentile"] = _empirical_percentile(
                deviations, _safe_float(row["median_absolute_deviation"])
            )
            row["axis_source_range_percentile"] = _empirical_percentile(
                source_ranges, _safe_float(row["source_mean_range"])
            )
    return out


def _identity_rows(axis_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    by_response: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in axis_rows:
        by_response[str(row["response_symbol"])].append(row)
    out: list[dict[str, object]] = []
    for response_symbol, rows in sorted(by_response.items()):
        first = rows[0]
        ordered = sorted(rows, key=lambda row: str(row["response_axis"]))
        highest = max(
            ordered,
            key=lambda row: (
                _safe_float(row["observation_directional_persistence"]),
                str(row["response_axis"]),
            ),
        )
        lowest = min(
            ordered,
            key=lambda row: (
                _safe_float(row["observation_directional_persistence"]),
                str(row["response_axis"]),
            ),
        )
        out.append(
            {
                "role_family": first["role_family"],
                "component": first["component"],
                "response_symbol": response_symbol,
                "observations": first["observations"],
                "evidence_sources": first["evidence_sources"],
                "mean_observation_directional_persistence": mean(
                    _safe_float(row["observation_directional_persistence"])
                    for row in rows
                ),
                "minimum_observation_directional_persistence": min(
                    _safe_float(row["observation_directional_persistence"])
                    for row in rows
                ),
                "maximum_observation_directional_persistence": max(
                    _safe_float(row["observation_directional_persistence"])
                    for row in rows
                ),
                "mean_source_directional_persistence": mean(
                    _safe_float(row["source_directional_persistence"])
                    for row in rows
                ),
                "total_source_sign_switches": sum(
                    int(row["source_sign_switches"]) for row in rows
                ),
                "highest_persistence_axis": highest["response_axis"],
                "lowest_persistence_axis": lowest["response_axis"],
            }
        )
    return out


def _write_markdown(
    path: Path,
    axis_rows: list[dict[str, object]],
    identity_rows: list[dict[str, object]],
) -> None:
    rf05 = [
        row
        for row in axis_rows
        if row["role_family"] == "rf_05" and row["component"] == "volume"
    ]
    rf05_by_axis = {str(row["response_axis"]): row for row in rf05}
    event = rf05_by_axis["event_share"]
    continuity = rf05_by_axis["continuity"]
    coverage = rf05_by_axis["member_coverage"]
    one_direction = sum(
        _safe_float(row["observation_directional_persistence"]) == 1.0
        for row in axis_rows
    )
    source_one_direction = sum(
        _safe_float(row["source_directional_persistence"]) == 1.0
        for row in axis_rows
    )
    switching_axes = sum(int(row["source_sign_switches"]) > 0 for row in axis_rows)
    shallow_axes = sum(
        int(row["observations"]) == 6 and int(row["evidence_sources"]) == 2
        for row in axis_rows
    )
    medium_axes = sum(
        int(row["observations"]) == 11 and int(row["evidence_sources"]) == 3
        for row in axis_rows
    )
    deep_axes = sum(
        int(row["observations"]) == 21 and int(row["evidence_sources"]) == 5
        for row in axis_rows
    )
    perfect_event_axes = sum(
        row["response_axis"] == "event_share"
        and _safe_float(row["observation_directional_persistence"]) == 1.0
        for row in axis_rows
    )
    deep_fully_persistent = sum(
        int(row["observations"]) >= 21
        and int(row["evidence_sources"]) >= 5
        and _safe_float(row["observation_directional_persistence"]) == 1.0
        and _safe_float(row["source_directional_persistence"]) == 1.0
        for row in axis_rows
    )
    top_axes = sorted(
        axis_rows,
        key=lambda row: (
            -_safe_float(row["observation_directional_persistence"]),
            -_safe_float(row["source_directional_persistence"]),
            str(row["role_family"]),
            str(row["component"]),
            str(row["response_axis"]),
        ),
    )[:10]
    lines = [
        "# 2088 - Passive Antwort-Erfahrungsbreite",
        "",
        "## Zweck",
        "",
        "Die passive Antwort-Memory enthält nach Befund 2087 insgesamt 222 Beobachtungen in 32 Familien-Komponenten-Identitäten. Dieser Lauf vermisst ihre innere Breite, ohne aus Streuung oder Richtung neue Klassen zu bilden.",
        "",
        "Beobachtungspersistenz ist der Betrag der Vorzeichenbilanz aller Einzelwerte. Quellenpersistenz berechnet dieselbe Bilanz aus den Mittelwerten der Evidenzquellen. Beide liegen kontinuierlich zwischen `0` und `1`; sie sind Forschungsmaße, keine Reifeschwellen.",
        "",
        "## Gesamtprofil",
        "",
        f"- Antwortidentitäten: `{len(identity_rows)}`",
        f"- vermessene Antwortachsen: `{len(axis_rows)}`",
        f"- vollständig gleichgerichtete Beobachtungsachsen: `{one_direction}`",
        f"- vollständig gleichgerichtete Quellenachsen: `{source_one_direction}`",
        f"- Achsen mit mindestens einem Quellen-Vorzeichenwechsel: `{switching_axes}`",
        f"- Achsen mit 6 Beobachtungen aus 2 Quellen: `{shallow_axes}`",
        f"- Achsen mit 11 Beobachtungen aus 3 Quellen: `{medium_axes}`",
        f"- Achsen mit 21 Beobachtungen aus 5 Quellen: `{deep_axes}`",
        "- Memory- oder Runtime-Änderung: `0`",
        "",
        "## rf_05:volume",
        "",
        "| Achse | positiv/negativ/null | Beobachtungspersistenz | Quellenpfad | Quellenpersistenz | MAD | Persistenzperzentil |",
        "|---|---:|---:|---|---:|---:|---:|",
    ]
    for row in (continuity, event, coverage):
        lines.append(
            f"| `{row['response_axis']}` | "
            f"{row['positive_observations']}/{row['negative_observations']}/{row['zero_observations']} | "
            f"{_fmt(row['observation_directional_persistence'])} | "
            f"`{row['source_sign_path']}` | "
            f"{_fmt(row['source_directional_persistence'])} | "
            f"{_fmt(row['median_absolute_deviation'], 4)} | "
            f"{_fmt(row['axis_observation_persistence_percentile'])} |"
        )
    lines.extend(
        [
            "",
            "## Höchste Richtungsbilanzen",
            "",
            "Die Tabelle ist nur eine Sortierung kontinuierlicher Werte und keine Auswahl tragender Klassen.",
            "",
            "| Familie | Komponente | Achse | Beobachtungen/Quellen | Beobachtungspersistenz | Quellenpersistenz | positiv/negativ |",
            "|---|---|---|---:|---:|---:|---:|",
        ]
    )
    for row in top_axes:
        lines.append(
            f"| `{row['role_family']}` | `{row['component']}` | `{row['response_axis']}` | "
            f"{row['observations']}/{row['evidence_sources']} | "
            f"{_fmt(row['observation_directional_persistence'])} | "
            f"{_fmt(row['source_directional_persistence'])} | "
            f"{row['positive_observations']}/{row['negative_observations']} |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"`rf_05:volume` trägt auf der Ereignisanteil-Achse `{event['positive_observations']}/{event['observations']}` positive Beobachtungen und den Quellenpfad `{event['source_sign_path']}`. Beobachtungs- und Quellenpersistenz liegen bei `{_fmt(event['observation_directional_persistence'])}` und `{_fmt(event['source_directional_persistence'])}`. Innerhalb der 32 Ereignisanteil-Achsen liegt seine Beobachtungspersistenz am Perzentil `{_fmt(event['axis_observation_persistence_percentile'])}`.",
            "",
            f"Vollständige Ereignisanteil-Persistenz ist nicht allein `rf_05` vorbehalten: `{perfect_event_axes}/32` Ereignisanteil-Achsen erreichen den Wert `1.000`. Die Evidenztiefe ist jedoch ungleich verteilt. `{shallow_axes}/96` Achsen beruhen nur auf sechs Beobachtungen aus zwei Quellen; lediglich `{deep_axes}/96` besitzen 21 Beobachtungen aus fünf Quellen. Unter diesen tief vermessenen Achsen bleibt genau `{deep_fully_persistent}` auf Beobachtungs- und Quellenebene vollständig gleichgerichtet: `rf_05:volume:event_share`.",
            "",
            f"Kontinuität und Mitgliederabdeckung tragen jeweils `{continuity['positive_observations']}/{continuity['negative_observations']}` beziehungsweise `{coverage['positive_observations']}/{coverage['negative_observations']}` positive/negative Beobachtungen. Ihre Beobachtungspersistenzen liegen nur bei `{_fmt(continuity['observation_directional_persistence'])}` und `{_fmt(coverage['observation_directional_persistence'])}`; die widersprechende Erfahrung aus 2086 bleibt damit als reale Breite sichtbar und wird nicht durch den positiven Mittelwert verdeckt.",
            "",
            f"Über die gesamte Memory sind `{one_direction}/{len(axis_rows)}` Achsen auf Beobachtungsebene und `{source_one_direction}/{len(axis_rows)}` auf Quellenebene vollständig gleichgerichtet. Die heutige Memory erlaubt daher eine belastbarere Aussage zur inneren Breite von `rf_05:volume` als zum Vergleich mit den übrigen 31 Identitäten. Deren Evidenztiefe muss erst wachsen, bevor gleiche Persistenzwerte gleichgewichtig verglichen werden können.",
            "",
            "## Organische Grenze",
            "",
            "Die Karte ergänzt keine Memory-Felder und wird nicht von MINI_DIO gelesen. Vorzeichenbalance, Streuung und Quellenpfade bleiben Auswertungen vorhandener Erfahrung. Es entstehen keine Kategorien wie stabil oder plastisch, keine Schwellen und keine Handlungswirkung.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Vermisst die kontinuierliche Erfahrungsbreite passiver Antwortidentitäten."
    )
    parser.add_argument("--memory", default=str(DEFAULT_MEMORY))
    parser.add_argument("--out-prefix", default=str(DEFAULT_OUT_PREFIX))
    args = parser.parse_args()

    memory_path = _resolve(args.memory)
    out_prefix = _resolve(args.out_prefix)
    memory_rows = _load_csv(memory_path)
    if not memory_rows:
        raise ValueError("Antwort-Memory ist leer")
    header = set(memory_rows[0])
    forbidden = sorted(header & FORBIDDEN_FIELDS)
    if forbidden:
        raise ValueError(f"Verbotene Memory-Felder: {';'.join(forbidden)}")
    active = [
        row
        for row in memory_rows
        if any(int(float(row.get(flag, 0) or 0)) != 0 for flag in ACTIVE_FLAGS)
    ]
    if active:
        raise ValueError(f"Aktive Antwort-Memory-Zeilen: {len(active)}")

    axis_rows = _axis_rows(memory_rows)
    identity_rows = _identity_rows(axis_rows)
    if len(axis_rows) != 96 or len(identity_rows) != 32:
        raise ValueError(
            f"Erwartet 96 Achsen und 32 Identitäten, gefunden {len(axis_rows)}/{len(identity_rows)}"
        )
    _write_csv(out_prefix.with_suffix(".axes.csv"), axis_rows)
    _write_csv(out_prefix.with_suffix(".identities.csv"), identity_rows)
    _write_markdown(out_prefix.with_suffix(".md"), axis_rows, identity_rows)

    print(f"memory_observations={len(memory_rows)}")
    print(f"response_identities={len(identity_rows)}")
    print(f"response_axes={len(axis_rows)}")
    print(f"active_rows={len(active)}")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
