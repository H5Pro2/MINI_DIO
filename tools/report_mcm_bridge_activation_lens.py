from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


DEFAULT_INPUTS = [
    ("SOL2024", "debug/post_feature_cleanup_sol_2024_5m/dio_mini_lauf_2/episodes.csv"),
    ("BTC2024", "debug/post_feature_cleanup_btc_2024_5m/dio_mini_lauf_2/episodes.csv"),
    ("KAS2024", "debug/post_feature_cleanup_kas_2024_5m/dio_mini_lauf_2/episodes.csv"),
    ("PAXG2024", "debug/post_feature_cleanup_paxg_2024_5m/dio_mini_lauf_2/episodes.csv"),
    ("QUIET2026", "debug/post_feature_cleanup_long_quiet_2026_sideways/dio_mini_lauf_2/episodes.csv"),
    ("STRESS2025", "debug/post_feature_cleanup_long_stress_2025/dio_mini_lauf_2/episodes.csv"),
    ("EXPANSION2023", "debug/post_feature_cleanup_long_expansion_2023_positive/dio_mini_lauf_2/episodes.csv"),
]


METRICS = [
    "perception_auditory_loudness",
    "perception_auditory_softening",
    "perception_visual_sharpness",
    "perception_visual_blur",
    "perception_focus_strength",
    "perception_distance_need",
    "perception_adapted_field_intake_pressure",
    "rezeptor_visual_contact",
    "rezeptor_auditory_contact",
    "rezeptor_contact_pressure",
    "mcm_rekopplung_quality",
    "mcm_strain_quality",
    "mcm_sensory_coupling",
    "mcm_feldwirkung_mcm_coherence",
    "mcm_feldwirkung_mcm_tension",
    "mcm_feldwirkung_mcm_asymmetry",
]


def _load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _float(row: dict[str, str], key: str) -> float:
    try:
        value = float(row.get(key, "") or 0.0)
    except ValueError:
        return 0.0
    return 0.0 if value != value else value


def _int(row: dict[str, str], key: str) -> int:
    try:
        return int(float(row.get(key, "") or 0))
    except ValueError:
        return 0


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _token(row: dict[str, str]) -> str:
    for key in ("mcm_field_episode_preview_symbol", "mcm_field_episode_symbol", "episode_memory_symbol"):
        value = str(row.get(key, "") or "").strip()
        if value and value != "-":
            return value
    return "-"


def _parse_inputs(items: list[str], root: Path) -> list[tuple[str, Path]]:
    if not items:
        return [(name, root / rel) for name, rel in DEFAULT_INPUTS if (root / rel).exists()]
    parsed: list[tuple[str, Path]] = []
    for item in items:
        if "=" in item:
            name, text = item.split("=", 1)
        else:
            path = Path(item)
            name = path.parent.parent.name if path.name == "episodes.csv" else path.stem
            text = item
        path = Path(text)
        if not path.is_absolute():
            path = root / path
        parsed.append((name, path))
    return parsed


def _token_groups(role_rows: list[dict[str, str]]) -> dict[str, set[str]]:
    groups: dict[str, set[str]] = {
        "stable_bridge": set(),
        "stable_young_surface": set(),
        "maturing_young_surface": set(),
    }
    for row in role_rows:
        token = row.get("token", "-") or "-"
        relation = row.get("relation", "-") or "-"
        class_864 = row.get("class_864", "-") or "-"
        class_868 = row.get("class_868", "-") or "-"
        if relation == "rollenstabil" and class_864 == "brueckenpfad" and class_868 == "brueckenpfad":
            groups["stable_bridge"].add(token)
        elif relation == "rollenstabil" and class_864 == "junge_oberflaeche" and class_868 == "junge_oberflaeche":
            groups["stable_young_surface"].add(token)
        elif relation == "junge_spur_reift" and class_864 == "junge_oberflaeche":
            groups["maturing_young_surface"].add(token)
    return groups


def _segment_indices(rows: list[dict[str, str]], token: str) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    start: int | None = None
    for index, row in enumerate(rows):
        if _token(row) == token:
            if start is None:
                start = index
        elif start is not None:
            out.append((start, index - 1))
            start = None
    if start is not None:
        out.append((start, len(rows) - 1))
    return out


def _direction(rows: list[dict[str, str]]) -> str:
    if len(rows) < 2:
        return "-"
    first = _float(rows[0], "close_reward")
    last = _float(rows[-1], "close_reward")
    diff = last - first
    if diff > 0.004:
        return "steigend"
    if diff < -0.004:
        return "fallend"
    return "seitwaerts"


def _dominant(rows: list[dict[str, str]], key: str) -> str:
    counter = Counter(str(row.get(key, "-") or "-") for row in rows)
    return counter.most_common(1)[0][0] if counter else "-"


def _collect_segments(inputs: list[tuple[str, Path]], groups: dict[str, set[str]]) -> list[dict[str, object]]:
    token_to_group: dict[str, str] = {}
    for group, tokens in groups.items():
        for token in tokens:
            token_to_group[token] = group

    out: list[dict[str, object]] = []
    for world, path in inputs:
        if not path.exists():
            continue
        rows = sorted(_load_csv(path), key=lambda row: _int(row, "tick"))
        for token, group in token_to_group.items():
            for segment_index, (start, end) in enumerate(_segment_indices(rows, token), start=1):
                current = rows[start : end + 1]
                item: dict[str, object] = {
                    "group": group,
                    "token": token,
                    "world": world,
                    "segment": segment_index,
                    "start_tick": _int(rows[start], "tick"),
                    "end_tick": _int(rows[end], "tick"),
                    "duration": end - start + 1,
                    "direction": _direction(current),
                    "dominant_effect": _dominant(current, "passive_mcm_effect_class"),
                    "dominant_awareness": _dominant(current, "passive_inner_effect_awareness_state"),
                    "dominant_family": _dominant(current, "symbol_family"),
                }
                for key in METRICS:
                    item[key] = round(_avg([_float(row, key) for row in current]), 6)
                out.append(item)
    out.sort(key=lambda row: (str(row["group"]), str(row["token"]), str(row["world"]), int(row["start_tick"])))
    return out


def _write_csv(rows: list[dict[str, object]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        out.write_text("", encoding="utf-8")
        return
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _group_rows(rows: list[dict[str, object]]) -> dict[str, list[dict[str, object]]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["group"])].append(row)
    return dict(grouped)


def _metric_avg(rows: list[dict[str, object]], key: str) -> float:
    return _avg([float(row.get(key, 0.0) or 0.0) for row in rows])


def _write_markdown(rows: list[dict[str, object]], groups: dict[str, set[str]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    grouped = _group_rows(rows)
    lines = [
        "# MCM-Brueckenaktivierung Lupe",
        "",
        "## Zweck",
        "",
        "Diese Diagnose isoliert stabile Brueckenpfade aus der Rollenreproduktion und vergleicht ihre Weltkontakte mit jungen Oberflaechen.",
        "Sie liest passiv, welche Sinnes- und Feldmerkmale eine Brueckenrolle aktiv halten.",
        "",
        "## Token-Gruppen",
        "",
        "| Gruppe | Tokens aus Rollenlupe | Kontaktsegmente | Welten |",
        "|---|---:|---:|---:|",
    ]
    for group in ("stable_bridge", "stable_young_surface", "maturing_young_surface"):
        group_rows = grouped.get(group, [])
        worlds = {str(row["world"]) for row in group_rows}
        lines.append(f"| {group} | {len(groups.get(group, set()))} | {len(group_rows)} | {len(worlds)} |")

    lines.extend(
        [
            "",
            "## Kontaktmittelwerte",
            "",
            "| Gruppe | Dauer | Lautheit | Hoer-Daempfung | Schaerfe | Unschaerfe | Fokus | Abstand | Feldaufnahme | Rekopplung | Strain | Spannung | Sensorik |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for group in ("stable_bridge", "stable_young_surface", "maturing_young_surface"):
        group_rows = grouped.get(group, [])
        lines.append(
            "| {group} | {duration:.2f} | {loud:.4f} | {soft:.4f} | {sharp:.4f} | {blur:.4f} | {focus:.4f} | {dist:.4f} | {intake:.4f} | {rek:.4f} | {strain:.4f} | {tension:.4f} | {sensory:.4f} |".format(
                group=group,
                duration=_metric_avg(group_rows, "duration"),
                loud=_metric_avg(group_rows, "perception_auditory_loudness"),
                soft=_metric_avg(group_rows, "perception_auditory_softening"),
                sharp=_metric_avg(group_rows, "perception_visual_sharpness"),
                blur=_metric_avg(group_rows, "perception_visual_blur"),
                focus=_metric_avg(group_rows, "perception_focus_strength"),
                dist=_metric_avg(group_rows, "perception_distance_need"),
                intake=_metric_avg(group_rows, "perception_adapted_field_intake_pressure"),
                rek=_metric_avg(group_rows, "mcm_rekopplung_quality"),
                strain=_metric_avg(group_rows, "mcm_strain_quality"),
                tension=_metric_avg(group_rows, "mcm_feldwirkung_mcm_tension"),
                sensory=_metric_avg(group_rows, "mcm_sensory_coupling"),
            )
        )

    lines.extend(["", "## Stabile Brueckentokens", ""])
    for token in sorted(groups.get("stable_bridge", set())):
        token_rows = [row for row in rows if row["token"] == token]
        worlds = Counter(str(row["world"]) for row in token_rows)
        effects = Counter(str(row["dominant_effect"]) for row in token_rows)
        lines.append(
            f"- `{token}`: Segmente `{len(token_rows)}`, Welten `{len(worlds)}`, "
            f"dominanter Effekt `{effects.most_common(1)[0][0] if effects else '-'}`"
        )

    bridge_rows = grouped.get("stable_bridge", [])
    young_rows = grouped.get("stable_young_surface", [])
    maturing_rows = grouped.get("maturing_young_surface", [])
    bridge_rek = _metric_avg(bridge_rows, "mcm_rekopplung_quality")
    young_rek = _metric_avg(young_rows, "mcm_rekopplung_quality")
    bridge_blur = _metric_avg(bridge_rows, "perception_visual_blur")
    young_blur = _metric_avg(young_rows, "perception_visual_blur")
    bridge_soft = _metric_avg(bridge_rows, "perception_auditory_softening")
    young_soft = _metric_avg(young_rows, "perception_auditory_softening")

    lines.extend(["", "## Befund", ""])
    lines.append(
        f"Stabile Bruecken zeigen im Mittel Rekopplung `{bridge_rek:.4f}` gegenueber `{young_rek:.4f}` bei stabil jungen Oberflaechen."
    )
    lines.append(
        f"Ihre visuelle Unschaerfe liegt bei `{bridge_blur:.4f}` gegenueber `{young_blur:.4f}`; ihre Hoer-Daempfung bei `{bridge_soft:.4f}` gegenueber `{young_soft:.4f}`."
    )
    if bridge_rek >= young_rek and bridge_blur <= young_blur:
        lines.append(
            "Das spricht dafuer, dass Bruecken nicht durch maximale Reizstaerke entstehen, sondern durch besser gehaltene Kopplung bei klarerer Aufnahme."
        )
    else:
        lines.append(
            "Die Bruecken unterscheiden sich nicht einfach durch mehr Ordnung. Sie muessen in der naechsten Diagnose ueber Eintritt/Austritt und Weltbreite gelesen werden."
        )
    if maturing_rows:
        lines.append(
            "Nachreifende junge Oberflaechen bilden die Zwischenklasse: Sie sind noch nicht Bruecke, zeigen aber bereits genug Kontaktqualitaet, um in tragendere Rollen zu wechseln."
        )

    lines.extend(
        [
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte fuer die stabilen Bruecken der Eintritt und Austritt gelesen werden: bleibt die Bruecke offen, weil sie zwischen zwei Bedeutungsraeumen vermittelt, oder weil sie eine stabile Mitte zwischen Weltspannung und Rekopplung bildet?",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--roles", required=True)
    parser.add_argument("--input", action="append", default=[])
    parser.add_argument("--out-md", required=True)
    parser.add_argument("--out-csv", required=True)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    groups = _token_groups(_load_csv(Path(args.roles)))
    rows = _collect_segments(_parse_inputs(args.input, root), groups)
    _write_csv(rows, Path(args.out_csv))
    _write_markdown(rows, groups, Path(args.out_md))
    print(f"segments={len(rows)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
