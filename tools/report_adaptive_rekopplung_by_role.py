from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


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


def _rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _fmt(value: object, digits: int = 4) -> str:
    return f"{_float(value):.{digits}f}"


def _key(row: dict[str, str], mode: str) -> str:
    if mode == "family":
        return str(row.get("symbol_family", "") or "-")
    if mode == "role_family":
        return f"{row.get('mcm_field_episode_role', '-') or '-'}::{row.get('symbol_family', '-') or '-'}"
    return str(row.get("mcm_field_episode_role", "") or row.get("passive_mcm_effect_class", "") or "-")


def _summarize(rows: list[dict[str, str]], mode: str, min_count: int) -> list[dict[str, object]]:
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[_key(row, mode)].append(row)

    output: list[dict[str, object]] = []
    for key, items in groups.items():
        if len(items) < min_count:
            continue
        static_values = [_float(item.get("mcm_rekopplung_quality")) for item in items]
        adaptive_values = [_float(item.get("mcm_adaptive_rekopplung_quality")) for item in items]
        experience_values = [_float(item.get("mcm_adaptive_rekopplung_experience")) for item in items]
        role_experience_values = [_float(item.get("mcm_adaptive_role_experience")) for item in items]
        path_experience_values = [_float(item.get("mcm_adaptive_path_experience")) for item in items]
        carry_weights = [_float(item.get("mcm_adaptive_weight_carry")) for item in items]
        alignment_weights = [_float(item.get("mcm_adaptive_weight_alignment")) for item in items]
        strain_weights = [_float(item.get("mcm_adaptive_weight_strain_relief")) for item in items]
        sensory_weights = [_float(item.get("mcm_adaptive_weight_sensory")) for item in items]
        effect_classes = defaultdict(int)
        states = defaultdict(int)
        for item in items:
            effect_classes[str(item.get("passive_mcm_effect_class", "") or "-")] += 1
            states[str(item.get("mcm_adaptive_rekopplung_state", "") or "-")] += 1
        milieus = defaultdict(int)
        for item in items:
            milieus[str(item.get("mcm_adaptive_milieu_state", "") or "-")] += 1
        static_avg = sum(static_values) / len(static_values)
        adaptive_avg = sum(adaptive_values) / len(adaptive_values)
        row = {
            "key": key,
            "count": len(items),
            "dominant_effect": max(effect_classes.items(), key=lambda item: item[1])[0],
            "dominant_adaptive_state": max(states.items(), key=lambda item: item[1])[0],
            "avg_static_rekopplung": round(static_avg, 6),
            "avg_adaptive_rekopplung": round(adaptive_avg, 6),
            "avg_adaptive_delta": round(adaptive_avg - static_avg, 6),
            "avg_experience": round(sum(experience_values) / len(experience_values), 6),
            "avg_role_experience": round(sum(role_experience_values) / len(role_experience_values), 6),
            "avg_path_experience": round(sum(path_experience_values) / len(path_experience_values), 6),
            "dominant_milieu": max(milieus.items(), key=lambda item: item[1])[0],
            "avg_weight_carry": round(sum(carry_weights) / len(carry_weights), 6),
            "avg_weight_alignment": round(sum(alignment_weights) / len(alignment_weights), 6),
            "avg_weight_strain_relief": round(sum(strain_weights) / len(strain_weights), 6),
            "avg_weight_sensory": round(sum(sensory_weights) / len(sensory_weights), 6),
            "weight_carry_span": round(max(carry_weights) - min(carry_weights), 6),
            "weight_alignment_span": round(max(alignment_weights) - min(alignment_weights), 6),
            "weight_strain_relief_span": round(max(strain_weights) - min(strain_weights), 6),
            "weight_sensory_span": round(max(sensory_weights) - min(sensory_weights), 6),
        }
        row["max_weight_span"] = round(
            max(
                row["weight_carry_span"],
                row["weight_alignment_span"],
                row["weight_strain_relief_span"],
                row["weight_sensory_span"],
            ),
            6,
        )
        output.append(row)
    return sorted(output, key=lambda row: (-float(row["count"]), -float(row["avg_adaptive_delta"])))


def _spread(rows: list[dict[str, object]], key: str) -> float:
    values = [_float(row.get(key)) for row in rows]
    return (max(values) - min(values)) if values else 0.0


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(path: Path, rows: list[dict[str, object]], source: Path, mode: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    carry_spread = _spread(rows, "avg_weight_carry")
    alignment_spread = _spread(rows, "avg_weight_alignment")
    strain_spread = _spread(rows, "avg_weight_strain_relief")
    sensory_spread = _spread(rows, "avg_weight_sensory")
    role_experience_spread = _spread(rows, "avg_role_experience")
    path_experience_spread = _spread(rows, "avg_path_experience")
    max_spread = max(carry_spread, alignment_spread, strain_spread, sensory_spread)
    if not rows:
        reading = "adaptive_rollenlesung_leer"
    elif max_spread <= 0.01:
        reading = "adaptive_gewichte_innerhalb_der_gruppen_noch_flach"
    elif max_spread <= 0.04:
        reading = "adaptive_gewichte_beginnen_zu_differenzieren"
    else:
        reading = "adaptive_gewichte_deutlich_rollenselektiv"

    lines = [
        "# Adaptive Rekopplung nach Rolle und Familie",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft, ob adaptive Rekopplung nur global anhebt oder ob sie nach Feldrolle und Symbolfamilie unterschiedlich gewichtet.",
        "",
        "Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.",
        "",
        "## Eingabe",
        "",
        f"- Quelle: `{source.relative_to(ROOT)}`",
        f"- Gruppierung: `{mode}`",
        "",
        "## Gesamtlesung",
        "",
        f"- Lesung: `{reading}`",
        f"- Gruppen: `{len(rows)}`",
        "",
        "| Gewicht | Spanne zwischen Gruppen |",
        "|---|---:|",
        f"| carry | {_fmt(carry_spread)} |",
        f"| alignment | {_fmt(alignment_spread)} |",
        f"| strain_relief | {_fmt(strain_spread)} |",
        f"| sensory | {_fmt(sensory_spread)} |",
        f"| role_experience | {_fmt(role_experience_spread)} |",
        f"| path_experience | {_fmt(path_experience_spread)} |",
        "",
        "## Gruppen",
        "",
        "| Gruppe | Anzahl | Wirkung | Milieu | Adaptiv | Delta | Erfahrung | Rolle | Pfad | Carry | Align | StrainRelief | Sensory | MaxSpan |",
        "|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows[:40]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["key"]),
                    str(row["count"]),
                    str(row["dominant_effect"]),
                    str(row["dominant_milieu"]),
                    _fmt(row["avg_adaptive_rekopplung"]),
                    _fmt(row["avg_adaptive_delta"]),
                    _fmt(row["avg_experience"]),
                    _fmt(row["avg_role_experience"]),
                    _fmt(row["avg_path_experience"]),
                    _fmt(row["avg_weight_carry"]),
                    _fmt(row["avg_weight_alignment"]),
                    _fmt(row["avg_weight_strain_relief"]),
                    _fmt(row["avg_weight_sensory"]),
                    _fmt(row["max_weight_span"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Diese Diagnose trennt die adaptive Rueckfuehrung von der globalen Mittelung.",
            "Wenn die Spannen klein bleiben, liegt die Gleichfoermigkeit nicht nur am Mehrweltmittel, sondern auch innerhalb der Rollen-/Familiengruppen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die adaptive Erfahrung nicht nur aus Durchschnittswerten, sondern aus Rollenmilieu und Zustandspfad gebildet werden. Dann koennen stabile, randnahe, offene und rekoppelnde Lagen eigene Gewichtungsprofile ausbilden.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Passive adaptive recoupling grouped by role/family.")
    parser.add_argument("--episodes", required=True)
    parser.add_argument("--mode", choices=("role", "family", "role_family"), default="role")
    parser.add_argument("--min-count", type=int, default=20)
    parser.add_argument("--out-md", default="docs/befunde/1001-2000/1501-1750/1681_ADAPTIVE_REKOPPLUNG_ROLLEN_FAMILIEN.md")
    parser.add_argument("--out-csv", default="docs/befunde/1001-2000/1501-1750/1681_ADAPTIVE_REKOPPLUNG_ROLLEN_FAMILIEN.csv")
    args = parser.parse_args()

    source = _resolve(args.episodes)
    rows = _summarize(_rows(source), mode=str(args.mode), min_count=int(args.min_count))
    out_md = _resolve(args.out_md)
    out_csv = _resolve(args.out_csv)
    _write_csv(out_csv, rows)
    _write_markdown(out_md, rows, source, str(args.mode))
    print({"out_md": str(out_md.relative_to(ROOT)), "out_csv": str(out_csv.relative_to(ROOT)), "rows": len(rows)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
