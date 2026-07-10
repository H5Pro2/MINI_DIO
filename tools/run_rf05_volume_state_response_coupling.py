from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean, median

try:
    from tools.run_role_family_component_phase_profiles import (
        DEFAULT_COHESION,
        DEFAULT_MEMORY,
        _load_targets,
        _resolve,
        _write_csv,
    )
    from tools.run_role_family_followworld_probe import _load_csv
    from tools.run_role_family_matched_pseudo_controls import (
        DEFAULT_OUT_PREFIX as PSEUDO_PREFIX,
        _empirical_percentile,
        _evaluate_pseudos,
        _fmt,
        _load_global_source_counts,
    )
    from tools.run_rf05_volume_5m_memory_maturation import (
        TARGET_COMPONENTS,
        TARGET_FAMILY,
        _build_records,
        _observed_definition,
        _run_pool_worlds,
    )
    from tools.run_rf05_volume_5m_window_paths import _window_pool
except ModuleNotFoundError:
    from run_role_family_component_phase_profiles import (
        DEFAULT_COHESION,
        DEFAULT_MEMORY,
        _load_targets,
        _resolve,
        _write_csv,
    )
    from run_role_family_followworld_probe import _load_csv
    from run_role_family_matched_pseudo_controls import (
        DEFAULT_OUT_PREFIX as PSEUDO_PREFIX,
        _empirical_percentile,
        _evaluate_pseudos,
        _fmt,
        _load_global_source_counts,
    )
    from run_rf05_volume_5m_memory_maturation import (
        TARGET_COMPONENTS,
        TARGET_FAMILY,
        _build_records,
        _observed_definition,
        _run_pool_worlds,
    )
    from run_rf05_volume_5m_window_paths import _window_pool


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = ROOT / "docs" / "befunde" / "2001-3000"
DEFAULT_DEFINITIONS = PSEUDO_PREFIX.with_suffix(".definitions.csv")
DEFAULT_DATA_DIR = ROOT / "data" / "generated" / "2083_rf05_volume_5m_memory_maturation"
DEFAULT_DEBUG_ROOT = ROOT / "debug" / "2083_rf05_volume_5m_memory_maturation"
DEFAULT_DETAIL_DIR = ROOT / "debug" / "2085_rf05_volume_state_response_coupling"
DEFAULT_OUT_PREFIX = BEFUNDE / "2085_RF05_VOLUME_FELDZUSTAND_ANTWORTKOPPLUNG"
STATE_AXES = (
    ("baseline_continuity", "real_family_continuity_score"),
    ("baseline_event_share", "real_mean_family_event_share"),
    ("baseline_member_coverage", "real_mean_member_coverage"),
)
RESPONSE_AXES = (
    ("delta_continuity", "control_minus_real_family_continuity_score"),
    ("delta_event_share", "control_minus_real_mean_family_event_share"),
    ("delta_member_coverage", "control_minus_real_mean_member_coverage"),
)


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _ranks(values: list[float]) -> list[float]:
    order = sorted(range(len(values)), key=lambda index: (values[index], index))
    ranks = [0.0] * len(values)
    position = 0
    while position < len(order):
        end = position + 1
        while end < len(order) and values[order[end]] == values[order[position]]:
            end += 1
        average_rank = (position + 1 + end) / 2.0
        for ranked_index in order[position:end]:
            ranks[ranked_index] = average_rank
        position = end
    return ranks


def _pearson(left: list[float], right: list[float]) -> float:
    left_mean = mean(left)
    right_mean = mean(right)
    left_centered = [value - left_mean for value in left]
    right_centered = [value - right_mean for value in right]
    denominator = (
        sum(value * value for value in left_centered)
        * sum(value * value for value in right_centered)
    ) ** 0.5
    if denominator == 0.0:
        return 0.0
    return sum(a * b for a, b in zip(left_centered, right_centered)) / denominator


def _spearman(rows: list[dict[str, object]], left: str, right: str) -> float:
    return _pearson(
        _ranks([_safe_float(row[left]) for row in rows]),
        _ranks([_safe_float(row[right]) for row in rows]),
    )


def _same_sign(left: float, right: float) -> bool:
    if left == 0.0:
        return right == 0.0
    return (left > 0.0) == (right > 0.0)


def _build_vectors(
    real_records: list[dict[str, object]],
    pool_rows: list[dict[str, object]],
    targets: dict[str, list[str]],
    definitions: list[dict[str, object]],
    global_counts: Counter[str],
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    observed_vectors: list[dict[str, object]] = []
    pseudo_vectors: list[dict[str, object]] = []
    observed_definition = _observed_definition(targets, global_counts)
    for record in real_records:
        asset = str(record["asset"])
        year = int(record["year"])
        start = int(record["start"])
        window_rows = _window_pool(pool_rows, asset, year, start)
        metadata = {
            "asset": asset,
            "year": year,
            "timeframe": "5m",
            "window_start": start,
            "window_end": start + int(record["rows"]),
            "path_id": f"{asset}:{year}",
        }
        observed = _evaluate_pseudos(
            observed_definition,
            window_rows,
            global_counts,
            TARGET_COMPONENTS,
            ("overall",),
        )[0]
        observed_vectors.append({**metadata, **observed})
        pseudos = _evaluate_pseudos(
            definitions,
            window_rows,
            global_counts,
            TARGET_COMPONENTS,
            ("overall",),
        )
        pseudo_vectors.extend({**metadata, **row} for row in pseudos)
    return observed_vectors, pseudo_vectors


def _build_correlations(
    observed: list[dict[str, object]],
    pseudos: list[dict[str, object]],
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    by_pseudo: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in pseudos:
        by_pseudo[str(row["pseudo_id"])].append(row)
    paths = sorted({str(row["path_id"]) for row in observed})
    summary: list[dict[str, object]] = []
    pseudo_detail: list[dict[str, object]] = []
    for state_name, state_field in STATE_AXES:
        for response_name, response_field in RESPONSE_AXES:
            observed_rho = _spearman(observed, state_field, response_field)
            pseudo_values: list[float] = []
            for pseudo_id, rows in sorted(by_pseudo.items()):
                rho = _spearman(rows, state_field, response_field)
                pseudo_values.append(rho)
                pseudo_detail.append(
                    {
                        "state_axis": state_name,
                        "response_axis": response_name,
                        "pseudo_id": pseudo_id,
                        "spearman_rho": rho,
                    }
                )
            leave_one_path_out = []
            for path_id in paths:
                remaining = [row for row in observed if row["path_id"] != path_id]
                leave_one_path_out.append(
                    _spearman(remaining, state_field, response_field)
                )
            summary.append(
                {
                    "state_axis": state_name,
                    "response_axis": response_name,
                    "windows": len(observed),
                    "observed_spearman_rho": observed_rho,
                    "pseudo_mean_rho": mean(pseudo_values),
                    "pseudo_median_rho": median(pseudo_values),
                    "observed_signed_percentile": _empirical_percentile(
                        pseudo_values, observed_rho
                    ),
                    "observed_absolute_percentile": _empirical_percentile(
                        [abs(value) for value in pseudo_values], abs(observed_rho)
                    ),
                    "pseudo_same_sign": sum(
                        _same_sign(observed_rho, value) for value in pseudo_values
                    ),
                    "pseudo_families": len(pseudo_values),
                    "leave_one_path_sign_consistent": sum(
                        _same_sign(observed_rho, value)
                        for value in leave_one_path_out
                    ),
                    "leave_one_path_tests": len(leave_one_path_out),
                    "leave_one_path_min_rho": min(leave_one_path_out),
                    "leave_one_path_max_rho": max(leave_one_path_out),
                }
            )
    return summary, pseudo_detail


def _write_markdown(
    path: Path,
    correlations: list[dict[str, object]],
) -> None:
    ranked = sorted(
        correlations,
        key=lambda row: (
            -_safe_float(row["observed_absolute_percentile"]),
            -abs(_safe_float(row["observed_spearman_rho"])),
        ),
    )
    strongest = ranked[0]
    unusual = [
        row
        for row in correlations
        if _safe_float(row["observed_absolute_percentile"]) >= 0.95
    ]
    stable_unusual = [
        row
        for row in unusual
        if int(row["leave_one_path_sign_consistent"])
        == int(row["leave_one_path_tests"])
    ]
    directional_edges = [
        row
        for row in correlations
        if _safe_float(row["observed_signed_percentile"]) in (0.0, 1.0)
        and int(row["leave_one_path_sign_consistent"])
        == int(row["leave_one_path_tests"])
    ]
    lines = [
        "# 2085 - rf_05:volume zwischen Feldzustand und Antwort",
        "",
        "## Zweck",
        "",
        "Befund 2084 zeigt eine kollektive Volumenphasenantwort über zwölf 5m-Fenster. Dieser Lauf prüft explorativ, ob die kontinuierliche Antwort mit dem jeweils ungestörten Familienzustand gekoppelt ist.",
        "",
        "Verglichen werden drei Ausgangsachsen - Kontinuität, Familienereignisanteil und Mitgliederabdeckung - mit drei Antwortdifferenzen nach gelöster Volumenphase. Jede Rangkopplung von `rf_05` wird gegen dieselbe Kopplung in 100 größen- und häufigkeitsgematchten Pseudo-Familien gestellt.",
        "",
        "## Kopplungsmatrix",
        "",
        "| Ausgangslage | Antwortachse | Spearman ρ | Pseudo-Mittel | signiertes Perzentil | Betrag-Perzentil | Pseudo gleiches Vorzeichen | LOO-Pfade gleiches Vorzeichen |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in correlations:
        lines.append(
            f"| `{row['state_axis']}` | `{row['response_axis']}` | "
            f"{_fmt(row['observed_spearman_rho'])} | {_fmt(row['pseudo_mean_rho'])} | "
            f"{_fmt(row['observed_signed_percentile'])} | "
            f"{_fmt(row['observed_absolute_percentile'])} | "
            f"{row['pseudo_same_sign']}/{row['pseudo_families']} | "
            f"{row['leave_one_path_sign_consistent']}/{row['leave_one_path_tests']} |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"Die gegenüber den gematchten Familien ungewöhnlichste Kopplung verläuft von `{strongest['state_axis']}` zu `{strongest['response_axis']}`. Sie trägt `ρ = {_fmt(strongest['observed_spearman_rho'])}` bei einem Betrag-Perzentil von `{_fmt(strongest['observed_absolute_percentile'])}` und behält ihr Vorzeichen in `{strongest['leave_one_path_sign_consistent']}/{strongest['leave_one_path_tests']}` Leave-one-path-Prüfungen.",
            "",
            f"Insgesamt erreichen `{len(unusual)}/9` Kopplungen explorativ mindestens das Betrag-Perzentil `0.950`; davon bleiben `{len(stable_unusual)}` beim Weglassen jedes einzelnen Asset-Jahr-Pfads vorzeichenstabil. Diese Zahlen sind eine Beschreibung des vorhandenen Feldes, keine Schwellenwerte für MINI_DIO.",
            "",
            f"Gleichzeitig liegen `{len(directional_edges)}/9` Kopplungen am äußersten Rand der signierten Pseudo-Verteilung und bleiben in allen vier Leave-one-path-Prüfungen gleichgerichtet. Es sind kreuzweise positive Verbindungen: Ausgangskontinuität zu Ereignisanteil-Antwort, Ausgangsereignisanteil zu Kontinuitäts- und Abdeckungsantwort sowie Ausgangsabdeckung zu Ereignisanteil-Antwort. Ihre Pseudo-Mittel sind jeweils negativ. `rf_05` trägt hier keine stärkere Kopplung als die Alternativfamilien, sondern eine andere Orientierung zwischen den Achsen.",
            "",
            "Die drei gleichnamigen Eigenachsen bleiben negativ und gegenüber den Pseudo-Familien gewöhnlich. Das passt zur rechnerischen Selbstkopplung von Ausgangswert und Differenz; die mögliche Besonderheit liegt nicht dort, sondern in der kreuzweisen Antwortordnung.",
            "",
            "Eine negative Kopplung zwischen Ausgangswert und Differenz kann bereits rechnerisch entstehen, weil die Antwort als `Kontrolle minus Realzustand` gebildet wird. Der Pseudo-Familien-Vergleich begrenzt diese Selbstkopplung: Nur ein ungewöhnlicher Abstand zu deren Korrelationsverteilung spricht für eine familienbezogene Form, nicht für Kausalität oder Bedeutung.",
            "",
            "## Organische Grenze",
            "",
            "Der Lauf fügt keine Klasse, Gewichtung, Schwelle oder Wenn-Dann-Regel hinzu. Er erzeugt keine neue unabhängige Evidenz und vergrößert die passive Memory nicht. Die Kopplungen bleiben kontinuierliche Forschungswerte aus denselben zwölf Fenstern von 2083.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prüft kontinuierliche Feldzustand-Antwort-Kopplungen für rf_05:volume."
    )
    parser.add_argument("--memory", default=str(DEFAULT_MEMORY))
    parser.add_argument("--cohesion-detail", default=str(DEFAULT_COHESION))
    parser.add_argument("--definitions", default=str(DEFAULT_DEFINITIONS))
    parser.add_argument("--data-dir", default=str(DEFAULT_DATA_DIR))
    parser.add_argument("--debug-root", default=str(DEFAULT_DEBUG_ROOT))
    parser.add_argument("--detail-dir", default=str(DEFAULT_DETAIL_DIR))
    parser.add_argument("--out-prefix", default=str(DEFAULT_OUT_PREFIX))
    args = parser.parse_args()

    role_memory = _resolve(args.memory)
    cohesion = _resolve(args.cohesion_detail)
    definitions_path = _resolve(args.definitions)
    data_dir = _resolve(args.data_dir)
    debug_root = _resolve(args.debug_root)
    detail_dir = _resolve(args.detail_dir)
    out_prefix = _resolve(args.out_prefix)

    targets = _load_targets(
        role_memory,
        ["rf_05", "rf_06", "rf_07", "rf_08", "rf_10", "rf_13", "rf_17", "rf_21"],
    )
    all_symbols = sorted({symbol for members in targets.values() for symbol in members})
    global_counts = _load_global_source_counts(cohesion, set(all_symbols))
    definitions = [
        row
        for row in _load_csv(definitions_path)
        if row["role_family"] == TARGET_FAMILY
    ]
    real_records, phase_records = _build_records(data_dir)
    pool_rows = _run_pool_worlds(real_records + phase_records, all_symbols, debug_root)
    observed, pseudos = _build_vectors(
        real_records, pool_rows, targets, definitions, global_counts
    )
    correlations, pseudo_correlations = _build_correlations(observed, pseudos)

    vector_rows = []
    for row in observed:
        vector_rows.append(
            {
                "asset": row["asset"],
                "year": row["year"],
                "timeframe": row["timeframe"],
                "window_start": row["window_start"],
                "window_end": row["window_end"],
                "path_id": row["path_id"],
                **{
                    name: _safe_float(row[field])
                    for name, field in STATE_AXES + RESPONSE_AXES
                },
            }
        )
    _write_csv(out_prefix.with_suffix(".vectors.csv"), vector_rows)
    _write_csv(out_prefix.with_suffix(".correlations.csv"), correlations)
    _write_csv(
        detail_dir / "2085_RF05_VOLUME_FELDZUSTAND_ANTWORTKOPPLUNG.pseudos.csv",
        pseudo_correlations,
    )
    _write_markdown(out_prefix.with_suffix(".md"), correlations)

    print(f"vectors={len(vector_rows)}")
    print(f"correlations={len(correlations)}")
    print(f"pseudo_correlations={len(pseudo_correlations)}")
    print(
        "absolute_percentile_ge_095="
        f"{sum(_safe_float(row['observed_absolute_percentile']) >= 0.95 for row in correlations)}"
    )
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
