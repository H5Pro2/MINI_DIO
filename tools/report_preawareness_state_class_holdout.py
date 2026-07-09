from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path

from befunde_paths import befunde_root
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = befunde_root(ROOT)


def _load_csv(path: Path) -> list[dict[str, str]]:
    path = path if path.is_absolute() else ROOT / path
    if not path.exists() or path.stat().st_size <= 0:
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _fmt(value: float) -> str:
    return f"{value:.3f}"


def _field_contact_class(row: dict[str, object]) -> str:
    carry = _safe_float(row.get("mcm_carry_quality"))
    strain = _safe_float(row.get("mcm_strain_quality"))
    rekopplung = _safe_float(row.get("mcm_rekopplung_quality"))
    if rekopplung >= 0.62 and carry >= 0.40 and strain <= 0.24:
        return "tragende_rekopplung"
    if rekopplung >= 0.58 and strain <= 0.28:
        return "offene_rekopplung"
    if strain >= 0.28 and rekopplung <= 0.59:
        return "spannungsnahe_oeffnung"
    if carry >= 0.40:
        return "getragen_offen"
    return "offener_feldkontakt"


def _sensory_class(row: dict[str, object]) -> str:
    visual_gap = _safe_float(row.get("mcm_visual_field_gap"))
    hearing_gap = _safe_float(row.get("mcm_hearing_field_gap"))
    coupling = _safe_float(row.get("mcm_sensory_coupling"))
    if coupling >= 0.74 and visual_gap <= 0.08 and hearing_gap <= 0.16:
        return "sinnesfeld_gekoppelt_klar"
    if coupling >= 0.60:
        return "sinnesfeld_gekoppelt_offen"
    if visual_gap > hearing_gap:
        return "sehen_feldferner"
    if hearing_gap > visual_gap:
        return "hoeren_feldferner"
    return "sinnesfeld_offen"


def _episode_paths(root: Path) -> list[Path]:
    root = root if root.is_absolute() else ROOT / root
    return sorted(root.glob("dio_mini_lauf_*/episodes.csv"))


def _read_holdout(label: str, root: Path, max_rows: int) -> dict[str, object]:
    rows_seen = 0
    field_counts: Counter[str] = Counter()
    sensory_counts: Counter[str] = Counter()
    carry_values: list[float] = []
    strain_values: list[float] = []
    rekopplung_values: list[float] = []
    for path in _episode_paths(root):
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                field_counts[_field_contact_class(row)] += 1
                sensory_counts[_sensory_class(row)] += 1
                carry_values.append(_safe_float(row.get("mcm_carry_quality")))
                strain_values.append(_safe_float(row.get("mcm_strain_quality")))
                rekopplung_values.append(_safe_float(row.get("mcm_rekopplung_quality")))
                rows_seen += 1
                if max_rows > 0 and rows_seen >= max_rows:
                    break
        if max_rows > 0 and rows_seen >= max_rows:
            break
    total = max(1, rows_seen)
    return {
        "holdout_label": label,
        "holdout_root": str(root),
        "rows": rows_seen,
        "field_counts": field_counts,
        "sensory_counts": sensory_counts,
        "avg_carry": mean(carry_values) if carry_values else 0.0,
        "avg_strain": mean(strain_values) if strain_values else 0.0,
        "avg_rekopplung": mean(rekopplung_values) if rekopplung_values else 0.0,
        "field_shares": {key: count / total for key, count in field_counts.items()},
        "sensory_shares": {key: count / total for key, count in sensory_counts.items()},
    }


def _state_relation(expected: str, observed: str, field_shares: dict[str, float]) -> tuple[str, float, float]:
    expected_share = field_shares.get(expected, 0.0)
    observed_share = field_shares.get(observed, 0.0)
    if observed_share > 0 and expected_share > 0:
        return "erwartung_und_beobachtung_im_feld_verfuegbar", expected_share, observed_share
    if observed_share > 0:
        return "beobachtete_umorganisation_verfuegbar", expected_share, observed_share
    if expected_share > 0:
        return "nur_ausgangsrolle_verfuegbar", expected_share, observed_share
    return "zustand_nicht_feldnah_verfuegbar", expected_share, observed_share


def _build_state_rows(states: list[dict[str, str]], holdouts: dict[str, dict[str, object]]) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for state in states:
        expected = str(state.get("expected_field_contact_class") or "-")
        observed = str(state.get("observed_field_contact_class") or "-")
        for holdout_label, holdout in sorted(holdouts.items()):
            field_shares = dict(holdout.get("field_shares", {}) or {})
            relation, expected_share, observed_share = _state_relation(expected, observed, field_shares)
            out.append(
                {
                    "source_state_quality": state.get("preawareness_state_quality", "-"),
                    "source_target_group": state.get("target_group", "-"),
                    "source_chain": state.get("chain", "-"),
                    "source_holdout_asset": state.get("holdout_asset", "-"),
                    "new_holdout_label": holdout_label,
                    "new_holdout_rows": holdout.get("rows", 0),
                    "expected_field_contact_class": expected,
                    "observed_field_contact_class": observed,
                    "new_holdout_relation": relation,
                    "expected_class_share": expected_share,
                    "observed_class_share": observed_share,
                    "new_avg_carry": holdout.get("avg_carry", 0.0),
                    "new_avg_strain": holdout.get("avg_strain", 0.0),
                    "new_avg_rekopplung": holdout.get("avg_rekopplung", 0.0),
                }
            )
    return out


def _summaries(rows: list[dict[str, object]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    by_relation: dict[str, list[dict[str, object]]] = defaultdict(list)
    by_quality: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        by_relation[str(row.get("new_holdout_relation", "-"))].append(row)
        by_quality[str(row.get("source_state_quality", "-"))].append(row)

    def summarize(groups: dict[str, list[dict[str, object]]], name_field: str) -> list[dict[str, object]]:
        out: list[dict[str, object]] = []
        for name, bucket in sorted(groups.items()):
            out.append(
                {
                    name_field: name,
                    "rows": len(bucket),
                    "avg_expected_class_share": mean(_safe_float(row.get("expected_class_share")) for row in bucket),
                    "avg_observed_class_share": mean(_safe_float(row.get("observed_class_share")) for row in bucket),
                    "avg_carry": mean(_safe_float(row.get("new_avg_carry")) for row in bucket),
                    "avg_strain": mean(_safe_float(row.get("new_avg_strain")) for row in bucket),
                    "avg_rekopplung": mean(_safe_float(row.get("new_avg_rekopplung")) for row in bucket),
                }
            )
        return out

    return summarize(by_relation, "new_holdout_relation"), summarize(by_quality, "source_state_quality")


def _md_table(rows: list[dict[str, object]], fields: list[str]) -> list[str]:
    lines = ["| " + " | ".join(fields) + " |", "| " + " | ".join("---" for _ in fields) + " |"]
    for row in rows:
        cells = []
        for field in fields:
            value = row.get(field, "")
            if isinstance(value, float):
                value = _fmt(value)
            cells.append(str(value))
        lines.append("| " + " | ".join(cells) + " |")
    return lines


def _write_markdown(
    path: Path,
    *,
    state_rows: list[dict[str, object]],
    relation_summary: list[dict[str, object]],
    quality_summary: list[dict[str, object]],
    holdouts: dict[str, dict[str, object]],
) -> None:
    relation_counts = Counter(str(row.get("new_holdout_relation", "-")) for row in state_rows)
    lines = [
        "# 2045 - Vorwahrnehmungs-Zustandsmemory gegen neue Feldklassen-Holdouts",
        "",
        "## Zweck",
        "",
        "Diese Prüfung setzt nach dem exakten Symbol-Holdout aus 2044 an. XRP erzeugte dort keine identische Syntax-Wiederkehr. Deshalb wird hier eine tiefere Ebene geprüft: Tauchen die Feldklassen der bekannten Zustände trotzdem in einer neuen Weltspannung auf?",
        "",
        "Das ist passiv. Es geht nicht um Handlung, sondern um Feldverfügbarkeit: Ist die erwartete oder beobachtete Feldrolle in der neuen Welt überhaupt vorhanden?",
        "",
        "## Holdouts",
        "",
    ]
    for label, holdout in sorted(holdouts.items()):
        field_counts = ";".join(f"{key}:{value}" for key, value in Counter(holdout.get("field_counts", {})).most_common())
        lines.append(
            f"- `{label}`: rows `{holdout.get('rows', 0)}`, MCM `{_fmt(float(holdout.get('avg_carry', 0.0)))}/"
            f"{_fmt(float(holdout.get('avg_strain', 0.0)))}/{_fmt(float(holdout.get('avg_rekopplung', 0.0)))}`, Feldklassen `{field_counts}`"
        )
    lines.extend(
        [
            "",
            "## Übersicht",
            "",
            f"- Zustandsprüfungen: `{len(state_rows)}`",
            f"- Relationsverteilung: `{dict(sorted(relation_counts.items()))}`",
            "",
            "## Relationsklassen",
            "",
        ]
    )
    lines.extend(
        _md_table(
            relation_summary,
            [
                "new_holdout_relation",
                "rows",
                "avg_expected_class_share",
                "avg_observed_class_share",
                "avg_carry",
                "avg_strain",
                "avg_rekopplung",
            ],
        )
    )
    lines.extend(["", "## Nach alter Zustandsqualität", ""])
    lines.extend(
        _md_table(
            quality_summary,
            [
                "source_state_quality",
                "rows",
                "avg_expected_class_share",
                "avg_observed_class_share",
                "avg_carry",
                "avg_strain",
                "avg_rekopplung",
            ],
        )
    )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Der Nulltreffer in 2044 bedeutet: Die alte Syntax taucht in XRP nicht identisch wieder auf. Die Feldklassenprüfung zeigt dagegen, ob darunter trotzdem Feldnähe vorhanden ist.",
            "",
            "Wenn `beobachtete_umorganisation_verfuegbar` oder `erwartung_und_beobachtung_im_feld_verfuegbar` auftaucht, ist das kein Beweis für dieselbe Bedeutung. Es zeigt nur, dass die neue Welt die passende Feldqualität bereitstellt, auf der spätere Bedeutungsreifung aufsetzen kann.",
            "",
            "## Grenze",
            "",
            "Diese Prüfung erzeugt keine neue Rolle, keine Handlung und keine Richtung. Sie ist eine passive Prüfung der Feldverfügbarkeit unter neuer Weltspannung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte geprüft werden, ob aus Feldverfügbarkeit über mehrere neue Welten wieder eine echte Syntax- oder Bedeutungsnähe entsteht. Erst dann wäre aus einer verfügbaren Feldklasse eine gereifte neue Vorwahrnehmungsrolle geworden.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def _parse_holdouts(raw_values: list[str]) -> dict[str, Path]:
    holdouts: dict[str, Path] = {}
    for raw in raw_values:
        if "=" not in raw:
            raise SystemExit(f"Ungültiges Holdout-Format: {raw}")
        label, path = raw.split("=", 1)
        holdouts[label.strip()] = Path(path.strip())
    return holdouts


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--states", default="docs/befunde/2001-3000/2043_VORWAHRNEHMUNG_ZUSTANDSQUALITAET_MEMORY.states.csv")
    parser.add_argument("--holdout", action="append", required=True)
    parser.add_argument("--max-rows-per-holdout", type=int, default=20000)
    parser.add_argument("--out-prefix", default="2045_VORWAHRNEHMUNG_ZUSTANDSMEMORY_FELDKLASSEN_HOLDOUT")
    args = parser.parse_args()

    states = _load_csv(Path(args.states))
    holdout_paths = _parse_holdouts(args.holdout)
    holdouts = {
        label: _read_holdout(label, root, args.max_rows_per_holdout)
        for label, root in sorted(holdout_paths.items())
    }
    state_rows = _build_state_rows(states, holdouts)
    relation_summary, quality_summary = _summaries(state_rows)

    out_prefix = BEFUNDE / args.out_prefix
    detail_fields = [
        "source_state_quality",
        "source_target_group",
        "source_chain",
        "source_holdout_asset",
        "new_holdout_label",
        "new_holdout_rows",
        "expected_field_contact_class",
        "observed_field_contact_class",
        "new_holdout_relation",
        "expected_class_share",
        "observed_class_share",
        "new_avg_carry",
        "new_avg_strain",
        "new_avg_rekopplung",
    ]
    _write_csv(out_prefix.with_suffix(".detail.csv"), state_rows, detail_fields)
    _write_csv(
        out_prefix.with_suffix(".relations.csv"),
        relation_summary,
        [
            "new_holdout_relation",
            "rows",
            "avg_expected_class_share",
            "avg_observed_class_share",
            "avg_carry",
            "avg_strain",
            "avg_rekopplung",
        ],
    )
    _write_csv(
        out_prefix.with_suffix(".qualities.csv"),
        quality_summary,
        [
            "source_state_quality",
            "rows",
            "avg_expected_class_share",
            "avg_observed_class_share",
            "avg_carry",
            "avg_strain",
            "avg_rekopplung",
        ],
    )
    _write_markdown(
        out_prefix.with_suffix(".md"),
        state_rows=state_rows,
        relation_summary=relation_summary,
        quality_summary=quality_summary,
        holdouts=holdouts,
    )
    print(f"state_checks={len(state_rows)}")
    print(f"holdouts={len(holdouts)}")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
