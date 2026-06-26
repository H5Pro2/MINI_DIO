from __future__ import annotations

import argparse
import csv
import math
from collections import Counter, defaultdict
from pathlib import Path


DEFAULT_INPUTS = [
    ("KAS_2024_5M", "debug/post_clean_diverse_kas_2024_5m/dio_mini_lauf_2/episodes.csv"),
    ("PAXG_2025_5M", "debug/post_clean_asset_tf_paxg_2025_5m/dio_mini_lauf_2/episodes.csv"),
    ("DOGE_2025_5M", "debug/post_clean_diverse_doge_2025_5m/dio_mini_lauf_2/episodes.csv"),
    ("XRP_2025_5M", "debug/post_clean_diverse_xrp_2025_5m/dio_mini_lauf_2/episodes.csv"),
    ("SYNTH_HARMONIC", "debug/post_clean_synth_harmonic_a/dio_mini_lauf_2/episodes.csv"),
    ("SYNTH_BRUCH_RAND", "debug/post_clean_synth_bruch_rand_a/dio_mini_lauf_2/episodes.csv"),
    ("SYNTH_RAND", "debug/post_clean_diverse_synth_rand_a/dio_mini_lauf_2/episodes.csv"),
]


def _float(row: dict[str, str], key: str) -> float:
    try:
        value = float(row.get(key, "") or 0.0)
    except ValueError:
        return 0.0
    if value != value:
        return 0.0
    return value


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _entropy(counter: Counter[str]) -> float:
    total = sum(counter.values())
    if total <= 0:
        return 0.0
    return -sum((count / total) * math.log2(count / total) for count in counter.values() if count > 0)


def _percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = (len(ordered) - 1) * q
    low = int(index)
    high = min(len(ordered) - 1, low + 1)
    if low == high:
        return ordered[low]
    return ordered[low] * (high - index) + ordered[high] * (index - low)


def _dominant(counter: Counter[str]) -> str:
    return counter.most_common(1)[0][0] if counter else "-"


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _token(row: dict[str, str]) -> str:
    for key in ("mcm_field_episode_preview_symbol", "mcm_field_episode_symbol", "symbol_family", "symbol"):
        value = str(row.get(key, "") or "").strip()
        if value and value != "-":
            return value
    return "-"


def _role(row: dict[str, str]) -> str:
    effect_class = str(row.get("passive_mcm_effect_class", "-") or "-")
    awareness = str(row.get("passive_inner_effect_awareness_state", "-") or "-")
    strain = _float(row, "mcm_strain_quality")
    rekopplung = _float(row, "mcm_rekopplung_quality")
    sensory = _float(row, "mcm_sensory_coupling")
    pressure = _float(row, "mcm_feldwirkung_mcm_tension") or _float(row, "perception_adapted_field_intake_pressure")

    if effect_class == "stabil" or awareness == "inner_effect_stable":
        return "zentrum_stabil"
    if effect_class in {"kippend", "gespannt"}:
        return "spannungsrand_kippnaehe"
    if pressure >= 0.44 or strain >= 0.28:
        return "spannungsrand_kippnaehe"
    if effect_class in {"tragend_unruhig", "diffus"}:
        return "offene_variante"
    if rekopplung >= 0.58 and strain <= 0.26 and sensory >= 0.70:
        return "rekopplungsnaehe"
    return "offene_variante"


def _parse_inputs(args: list[str], root: Path) -> list[tuple[str, Path]]:
    if not args:
        return [(name, root / path) for name, path in DEFAULT_INPUTS if (root / path).exists()]
    parsed: list[tuple[str, Path]] = []
    for item in args:
        if "=" in item:
            name, path_text = item.split("=", 1)
        else:
            path = Path(item)
            name = path.parent.parent.name if path.name == "episodes.csv" else path.stem
            path_text = item
        path = Path(path_text)
        if not path.is_absolute():
            path = root / path
        parsed.append((name, path))
    return parsed


def _classify(row: dict[str, object], cuts: dict[str, float]) -> str:
    observations = float(row["observations"])
    worlds = float(row["worlds"])
    role_entropy = float(row["role_entropy"])
    neighbor_count = float(row["neighbor_count"])
    center_share = float(row["center_share"])
    open_share = float(row["open_share"])
    rand_share = float(row["rand_share"])
    avg_rekopplung = float(row["avg_rekopplung"])
    avg_strain = float(row["avg_strain"])

    if observations <= cuts["obs_low"]:
        return "junge_spur"
    if rand_share >= cuts["rand_high"] and rand_share > center_share:
        return "randnahe_verdichtung"
    if worlds >= 2 and neighbor_count >= cuts["neighbor_high"] and role_entropy >= cuts["entropy_high"]:
        return "hoeherer_cluster_uebergang"
    if avg_rekopplung >= cuts["rekopplung_high"] and avg_strain <= cuts["strain_mid"]:
        return "rekopplungszone"
    if observations >= cuts["obs_high"] and center_share >= open_share and center_share >= rand_share:
        return "stabile_bedeutungsinsel"
    if role_entropy >= cuts["entropy_high"] or neighbor_count >= cuts["neighbor_high"]:
        return "driftzone"
    return "offene_bedeutungszone"


def _summarize(inputs: list[tuple[str, Path]]) -> tuple[list[dict[str, object]], list[dict[str, object]], list[str]]:
    buckets: dict[str, dict[str, object]] = {}
    transitions: Counter[tuple[str, str]] = Counter()
    missing: list[str] = []

    for world, path in inputs:
        if not path.exists():
            missing.append(f"{world}={path}")
            continue
        rows = sorted(_load(path), key=lambda row: int(float(row.get("tick", "0") or 0)))
        previous = "-"
        for row in rows:
            token = _token(row)
            if token == "-":
                previous = token
                continue
            role = _role(row)
            bucket = buckets.setdefault(
                token,
                {
                    "token": token,
                    "observations": 0,
                    "world_set": set(),
                    "roles": Counter(),
                    "families": Counter(),
                    "previews": Counter(),
                    "previous": Counter(),
                    "next": Counter(),
                    "rekopplung": [],
                    "carry": [],
                    "strain": [],
                    "sensory": [],
                    "tension": [],
                    "coherence": [],
                    "raw_field": [],
                    "adapted_field": [],
                    "loudness": [],
                    "visual_blur": [],
                },
            )
            bucket["observations"] = int(bucket["observations"]) + 1
            bucket["world_set"].add(world)  # type: ignore[union-attr]
            bucket["roles"][role] += 1  # type: ignore[index]
            bucket["families"][str(row.get("symbol_family", "-") or "-")] += 1  # type: ignore[index]
            bucket["previews"][str(row.get("mcm_field_episode_preview_symbol", "-") or "-")] += 1  # type: ignore[index]
            if previous != "-" and previous != token:
                bucket["previous"][previous] += 1  # type: ignore[index]
                transitions[(previous, token)] += 1
                prev_bucket = buckets.get(previous)
                if prev_bucket is not None:
                    prev_bucket["next"][token] += 1  # type: ignore[index]
            for target, key in [
                ("rekopplung", "mcm_rekopplung_quality"),
                ("carry", "mcm_carry_quality"),
                ("strain", "mcm_strain_quality"),
                ("sensory", "mcm_sensory_coupling"),
                ("tension", "mcm_feldwirkung_mcm_tension"),
                ("coherence", "mcm_feldwirkung_mcm_coherence"),
                ("raw_field", "perception_raw_field_intake_pressure"),
                ("adapted_field", "perception_adapted_field_intake_pressure"),
                ("loudness", "perception_auditory_loudness"),
                ("visual_blur", "perception_visual_blur"),
            ]:
                bucket[target].append(_float(row, key))  # type: ignore[union-attr]
            previous = token

    rows: list[dict[str, object]] = []
    total_by_role_keys = ["zentrum_stabil", "rekopplungsnaehe", "offene_variante", "spannungsrand_kippnaehe"]
    for token, bucket in buckets.items():
        observations = int(bucket["observations"])
        role_counts: Counter[str] = bucket["roles"]  # type: ignore[assignment]
        prev_counts: Counter[str] = bucket["previous"]  # type: ignore[assignment]
        next_counts: Counter[str] = bucket["next"]  # type: ignore[assignment]
        world_set: set[str] = bucket["world_set"]  # type: ignore[assignment]
        row: dict[str, object] = {
            "token": token,
            "observations": observations,
            "worlds": len(world_set),
            "world_names": ",".join(sorted(world_set)),
            "dominant_role": _dominant(role_counts),
            "dominant_family": _dominant(bucket["families"]),  # type: ignore[arg-type]
            "role_entropy": round(_entropy(role_counts), 6),
            "neighbor_count": len(set(prev_counts) | set(next_counts)),
            "incoming_count": sum(prev_counts.values()),
            "outgoing_count": sum(next_counts.values()),
            "top_previous": _dominant(prev_counts),
            "top_next": _dominant(next_counts),
            "avg_rekopplung": round(_avg(bucket["rekopplung"]), 6),  # type: ignore[arg-type]
            "avg_carry": round(_avg(bucket["carry"]), 6),  # type: ignore[arg-type]
            "avg_strain": round(_avg(bucket["strain"]), 6),  # type: ignore[arg-type]
            "avg_sensory": round(_avg(bucket["sensory"]), 6),  # type: ignore[arg-type]
            "avg_tension": round(_avg(bucket["tension"]), 6),  # type: ignore[arg-type]
            "avg_coherence": round(_avg(bucket["coherence"]), 6),  # type: ignore[arg-type]
            "avg_raw_field": round(_avg(bucket["raw_field"]), 6),  # type: ignore[arg-type]
            "avg_adapted_field": round(_avg(bucket["adapted_field"]), 6),  # type: ignore[arg-type]
            "avg_loudness": round(_avg(bucket["loudness"]), 6),  # type: ignore[arg-type]
            "avg_visual_blur": round(_avg(bucket["visual_blur"]), 6),  # type: ignore[arg-type]
        }
        for role in total_by_role_keys:
            key = {
                "zentrum_stabil": "center_share",
                "rekopplungsnaehe": "recoupling_share",
                "offene_variante": "open_share",
                "spannungsrand_kippnaehe": "rand_share",
            }[role]
            row[key] = round(role_counts[role] / max(1, observations), 6)
        rows.append(row)

    if rows:
        cuts = {
            "obs_low": _percentile([float(row["observations"]) for row in rows], 0.20),
            "obs_high": _percentile([float(row["observations"]) for row in rows], 0.75),
            "rand_high": _percentile([float(row["rand_share"]) for row in rows], 0.75),
            "neighbor_high": _percentile([float(row["neighbor_count"]) for row in rows], 0.75),
            "entropy_high": _percentile([float(row["role_entropy"]) for row in rows], 0.75),
            "rekopplung_high": _percentile([float(row["avg_rekopplung"]) for row in rows], 0.75),
            "strain_mid": _percentile([float(row["avg_strain"]) for row in rows], 0.50),
        }
        for row in rows:
            row["condensation_zone"] = _classify(row, cuts)
    rows.sort(key=lambda row: (str(row["condensation_zone"]), -int(row["observations"]), str(row["token"])))

    transition_rows = [
        {"from": source, "to": target, "count": count}
        for (source, target), count in transitions.most_common(50)
    ]
    return rows, transition_rows, missing


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object, digits: int = 4) -> str:
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    try:
        return f"{float(value):.{digits}f}"
    except (TypeError, ValueError):
        return str(value)


def _write_markdown(rows: list[dict[str, object]], transitions: list[dict[str, object]], missing: list[str], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    class_counts = Counter(str(row.get("condensation_zone", "-")) for row in rows)
    lines = [
        "# MCM-Verdichtungszonen",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest vorhandene MINI_DIO-Episoden als Verdichtungszonen.",
        "Sie prueft, ob Feldzeichen eher stabile Inseln, Driftzonen, Randnaehe, Rekopplungszonen oder Uebergaenge in hoehere Clusterordnung bilden.",
        "",
        "Die Diagnose ist passiv: kein Gate, keine Handlung, keine Runtime-Regel.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Welche Verdichtungsformen bildet das MCM-Feld aus wiederkehrender Weltwirkung?",
        "2. Unterpruefung: Welche Zeichen wirken stabil, driftend, randnah, rekoppelnd oder clusterbildend?",
        "3. Folgeschritt: Verdichtungszonen gegen neue Welten pruefen, ohne daraus Handlung abzuleiten.",
        "",
        "## Klassenuebersicht",
        "",
        "| Verdichtungszone | Anzahl |",
        "|---|---:|",
    ]
    for name, count in class_counts.most_common():
        lines.append(f"| {name} | {count} |")
    if missing:
        lines.extend(["", "## Fehlende Eingaben", ""])
        for item in missing:
            lines.append(f"- `{item}`")

    lines.extend(
        [
            "",
            "## Staerkste Zonen",
            "",
            "| Zone | Token | Beobachtungen | Welten | Rolle | Nachbarn | Zentrum | Offen | Rand | Rekopplung | Strain | Top-Next |",
            "|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in rows[:40]:
        lines.append(
            "| {condensation_zone} | {token} | {observations} | {worlds} | {dominant_role} | {neighbor_count} | {center_share:.4f} | {open_share:.4f} | {rand_share:.4f} | {avg_rekopplung:.4f} | {avg_strain:.4f} | {top_next} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Staerkste Uebergaenge",
            "",
            "| Von | Nach | Anzahl |",
            "|---|---|---:|",
        ]
    )
    for row in transitions[:20]:
        lines.append(f"| {row['from']} | {row['to']} | {row['count']} |")

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Verdichtung erscheint nicht als einzelner Absolutwert.",
            "Sie entsteht aus Wiederkehr, Rollenanteil, Nachbarschaft, Rekopplung, Strain und Weltuebergreifung.",
            "",
            "Damit passt die Diagnose zum Theorieanker der MCM-Verdichtung: Eine starke Innenfeldspur kann stabil bleiben, driften, randnah werden, rekoppeln oder als Uebergang in eine groessere Clusterordnung wirken.",
            "",
            "Wichtig: Diese Zonen sind Lesarten der vorhandenen Feldorganisation. Sie schreiben MINI_DIO keine Form vor.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die Verdichtungszonen-Matrix gegen eine frische Weltgruppe laufen. Ziel: pruefen, ob dieselben Zonen wiederkehren oder ob neue Uebergangscluster entstehen.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", action="append", default=[], help="Eingabe als NAME=pfad oder pfad. Mehrfach erlaubt.")
    parser.add_argument("--out", default="docs/befunde/854_MCM_VERDICHTUNGSZONEN.md")
    parser.add_argument("--csv-out", default="docs/befunde/854_MCM_VERDICHTUNGSZONEN.csv")
    parser.add_argument("--transitions-out", default="docs/befunde/854_MCM_VERDICHTUNGSZONEN_TRANSITIONS.csv")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    inputs = _parse_inputs(args.input, root)
    rows, transitions, missing = _summarize(inputs)
    _write_csv(rows, root / args.csv_out)
    _write_csv(transitions, root / args.transitions_out)
    _write_markdown(rows, transitions, missing, root / args.out)
    print(f"inputs={len(inputs)} zones={len(rows)} transitions={len(transitions)}")
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
