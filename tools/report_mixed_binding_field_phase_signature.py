from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


SIGNATURE_KEYS = [
    "avg_carry",
    "avg_strain",
    "avg_rekopplung",
    "avg_sensory",
    "avg_visual_gap",
    "avg_hearing_gap",
    "avg_coherence",
    "avg_tension",
    "avg_asymmetry",
]

EPISODE_KEY_MAP = {
    "avg_carry": "mcm_carry_quality",
    "avg_strain": "mcm_strain_quality",
    "avg_rekopplung": "mcm_rekopplung_quality",
    "avg_sensory": "mcm_sensory_coupling",
    "avg_visual_gap": "mcm_visual_field_gap",
    "avg_hearing_gap": "mcm_hearing_field_gap",
    "avg_coherence": "mcm_feldwirkung_mcm_coherence",
    "avg_tension": "mcm_feldwirkung_mcm_tension",
    "avg_asymmetry": "mcm_feldwirkung_mcm_asymmetry",
}


def _float(value: object) -> float:
    try:
        result = float(value)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists() or path.stat().st_size <= 0:
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _iter_episode_files(debug_roots: list[Path]):
    for root in debug_roots:
        if root.is_file() and root.name == "episodes.csv":
            yield root
        elif root.exists():
            yield from sorted(root.glob("dio_mini_lauf_*/episodes.csv"))


def _build_signature(rows: list[dict[str, str]]) -> dict[str, float]:
    positive = [row for row in rows if _float(row.get("count")) > 0.0]
    if not positive:
        raise RuntimeError("signature csv has no positive rows")
    return {key: _avg([_float(row.get(key)) for row in positive]) for key in SIGNATURE_KEYS}


def _proximity(row: dict[str, str], signature: dict[str, float]) -> float:
    distances: list[float] = []
    for key in SIGNATURE_KEYS:
        value = _float(row.get(EPISODE_KEY_MAP[key]))
        target = signature[key]
        distances.append(abs(value - target))
    # This is a passive distance score: 1.0 means close to the observed positive phase.
    return max(0.0, 1.0 - (_avg(distances) * 2.5))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--signature-csv", required=True)
    parser.add_argument("--debug-root", action="append", required=True)
    parser.add_argument("--out-prefix", required=True)
    parser.add_argument("--top-n", type=int, default=40)
    args = parser.parse_args()

    signature_rows = _read_csv(Path(args.signature_csv))
    signature = _build_signature(signature_rows)
    debug_roots = [Path(value) for value in args.debug_root]

    samples: list[dict[str, object]] = []
    symbol_buckets: dict[str, dict[str, object]] = defaultdict(
        lambda: {
            "count": 0,
            "score_sum": 0.0,
            "worlds": Counter(),
            "effects": Counter(),
            "states": Counter(),
            "families": Counter(),
        }
    )

    for episode_file in _iter_episode_files(debug_roots):
        for row in _read_csv(episode_file):
            symbol = row.get("mcm_field_episode_preview_symbol", "") or "-"
            score = _proximity(row, signature)
            if score <= 0.0:
                continue
            world = row.get("passive_world_label", "") or "-"
            effect = row.get("passive_mcm_effect_class", "") or "-"
            state = row.get("mcm_preview_anchor_depth_state", "") or "-"
            family = row.get("symbol_family", "") or "-"
            bucket = symbol_buckets[symbol]
            bucket["count"] = int(bucket["count"]) + 1
            bucket["score_sum"] = float(bucket["score_sum"]) + score
            bucket["worlds"][world] += 1
            bucket["effects"][effect] += 1
            bucket["states"][state] += 1
            bucket["families"][family] += 1
            samples.append(
                {
                    "source_file": str(episode_file),
                    "world": world,
                    "preview_symbol": symbol,
                    "symbol_family": family,
                    "field_effect": effect,
                    "depth_state": state,
                    "positive_phase_proximity": round(score, 6),
                    **{episode_key: row.get(episode_key, "") for episode_key in EPISODE_KEY_MAP.values()},
                }
            )

    out_dir = Path("docs") / "befunde"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / f"{args.out_prefix}.csv"
    out_md = out_dir / f"{args.out_prefix}.md"

    samples = sorted(samples, key=lambda item: float(item["positive_phase_proximity"]), reverse=True)
    if samples:
        with out_csv.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(samples[0].keys()))
            writer.writeheader()
            writer.writerows(samples[: max(args.top_n, 1)])
    else:
        out_csv.write_text("", encoding="utf-8")

    ranked_symbols = []
    for symbol, bucket in symbol_buckets.items():
        count = int(bucket["count"])
        avg_score = float(bucket["score_sum"]) / max(1, count)
        ranked_symbols.append((symbol, count, avg_score, bucket))
    ranked_symbols.sort(key=lambda item: (item[2], item[1]), reverse=True)

    lines = [
        f"# {args.out_prefix} - Positive Feldphasen-Signatur",
        "",
        "## Zweck",
        "",
        "Diese Diagnose sucht passiv nach Nähe zur positiven Mixed-Binding-Zielwelt aus Befund 2009.",
        "",
        "Die Signatur wird aus den tatsächlich getroffenen Rollen berechnet. Sie ist keine Handlungsregel und kein Gate.",
        "",
        "## Signaturmittel",
        "",
    ]
    for key in SIGNATURE_KEYS:
        lines.append(f"- `{key}`: `{signature[key]:.6f}`")
    score_bands = {
        ">=0.95": sum(1 for item in samples if float(item["positive_phase_proximity"]) >= 0.95),
        ">=0.90": sum(1 for item in samples if float(item["positive_phase_proximity"]) >= 0.90),
        ">=0.85": sum(1 for item in samples if float(item["positive_phase_proximity"]) >= 0.85),
        ">=0.75": sum(1 for item in samples if float(item["positive_phase_proximity"]) >= 0.75),
    }
    strong_symbols = {
        str(item["preview_symbol"])
        for item in samples
        if float(item["positive_phase_proximity"]) >= 0.90
    }
    very_strong_symbols = {
        str(item["preview_symbol"])
        for item in samples
        if float(item["positive_phase_proximity"]) >= 0.95
    }

    lines.extend(
        [
            "",
            "## Trefferübersicht",
            "",
            f"- Episoden mit positiver Signaturnähe: `{len(samples)}`",
            f"- unterschiedliche Preview-Symbole: `{len(ranked_symbols)}`",
            f"- starke Episoden `>=0.90`: `{score_bands['>=0.90']}`",
            f"- sehr starke Episoden `>=0.95`: `{score_bands['>=0.95']}`",
            f"- starke Preview-Symbole `>=0.90`: `{len(strong_symbols)}`",
            f"- sehr starke Preview-Symbole `>=0.95`: `{len(very_strong_symbols)}`",
            "",
            "Nähebänder:",
            "",
            f"- `>=0.95`: `{score_bands['>=0.95']}`",
            f"- `>=0.90`: `{score_bands['>=0.90']}`",
            f"- `>=0.85`: `{score_bands['>=0.85']}`",
            f"- `>=0.75`: `{score_bands['>=0.75']}`",
            "",
            "## Top-Symbole",
            "",
        ]
    )
    for symbol, count, avg_score, bucket in ranked_symbols[:12]:
        worlds = "; ".join(f"{key}:{value}" for key, value in bucket["worlds"].most_common(4))
        effects = "; ".join(f"{key}:{value}" for key, value in bucket["effects"].most_common(4))
        states = "; ".join(f"{key}:{value}" for key, value in bucket["states"].most_common(4))
        lines.extend(
            [
                f"### `{symbol}`",
                "",
                f"- Nähe-Treffer: `{count}`",
                f"- mittlere Signaturnähe: `{avg_score:.6f}`",
                f"- Welten: {worlds}",
                f"- Effekte: {effects}",
                f"- Depth-States: {states}",
                "",
            ]
        )

    lines.extend(
        [
            "## Lesung",
            "",
            "Wenn dieselbe Signatur in anderen Welten wieder auftaucht, kann MINI_DIO die positive Reifungsphase nicht nur an einem Symbolnamen, sondern an einer Feldphasenqualität wiederfinden.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte diese Signatur gegen Gegenproben und neue Welten gelesen werden. Entscheidend ist, ob sie nur im PAXG-Zielfenster bleibt oder auch in anderen Weltlagen als ähnliche Feldphase erscheint.",
        ]
    )
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"wrote={out_csv}")
    print(f"wrote={out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
