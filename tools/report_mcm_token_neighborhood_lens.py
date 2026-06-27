from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


DEFAULT_TOKENS = [
    "dio_mcm_episode_0v5p8er",
    "dio_mcm_episode_14l8khu",
    "dio_mcm_episode_1xx3u1e",
    "dio_mcm_episode_1q3us3f",
]

DEFAULT_INPUTS = [
    ("KAS_2024_5M", "debug/post_clean_diverse_kas_2024_5m/dio_mini_lauf_2/episodes.csv"),
    ("PAXG_2025_5M", "debug/post_clean_asset_tf_paxg_2025_5m/dio_mini_lauf_2/episodes.csv"),
    ("DOGE_2025_5M", "debug/post_clean_diverse_doge_2025_5m/dio_mini_lauf_2/episodes.csv"),
    ("XRP_2025_5M", "debug/post_clean_diverse_xrp_2025_5m/dio_mini_lauf_2/episodes.csv"),
    ("SYNTH_BRUCH_RAND", "debug/post_clean_synth_bruch_rand_a/dio_mini_lauf_2/episodes.csv"),
    ("SYNTH_RAND", "debug/post_clean_diverse_synth_rand_a/dio_mini_lauf_2/episodes.csv"),
    ("BTC_2024_5M", "debug/post_feature_cleanup_btc_2024_5m/dio_mini_lauf_2/episodes.csv"),
    ("SOL_2024_5M", "debug/post_feature_cleanup_sol_2024_5m/dio_mini_lauf_2/episodes.csv"),
    ("PAXG_2024_5M", "debug/post_feature_cleanup_paxg_2024_5m/dio_mini_lauf_2/episodes.csv"),
    ("DOGE_2024_5M", "debug/adapted_field_doge_2024_5m_10k/dio_mini_lauf_2/episodes.csv"),
    ("XRP_2024_5M", "debug/adapted_field_xrp_2024_5m_10k/dio_mini_lauf_2/episodes.csv"),
]


def _float(row: dict[str, str] | None, key: str) -> float:
    if row is None:
        return 0.0
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


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _token(row: dict[str, str] | None) -> str:
    if row is None:
        return "-"
    for key in ("mcm_field_episode_preview_symbol", "mcm_field_episode_symbol"):
        value = str(row.get(key, "") or "").strip()
        if value and value != "-":
            return value
    return "-"


def _role(row: dict[str, str] | None) -> str:
    if row is None:
        return "-"
    effect_class = str(row.get("passive_mcm_effect_class", "-") or "-")
    awareness = str(row.get("passive_inner_effect_awareness_state", "-") or "-")
    strain = _float(row, "mcm_strain_quality")
    rekopplung = _float(row, "mcm_rekopplung_quality")
    tension = _float(row, "mcm_feldwirkung_mcm_tension") or _float(row, "perception_adapted_field_intake_pressure")
    if effect_class == "stabil" or awareness == "inner_effect_stable":
        return "zentrum_stabil"
    if effect_class in {"kippend", "gespannt"} or tension >= 0.44 or strain >= 0.28:
        return "spannungsrand_kippnaehe"
    if effect_class in {"tragend_unruhig", "diffus"}:
        return "offene_variante"
    if rekopplung >= 0.58 and strain <= 0.26:
        return "rekopplungsnaehe"
    return "offene_variante"


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


def _collect(inputs: list[tuple[str, Path]], tokens: list[str]) -> list[dict[str, object]]:
    rows_out: list[dict[str, object]] = []
    token_set = set(tokens)
    for world, path in inputs:
        if not path.exists():
            continue
        rows = sorted(_load(path), key=lambda row: _int(row, "tick"))
        for index, row in enumerate(rows):
            token = _token(row)
            if token not in token_set:
                continue
            prev_row = rows[index - 1] if index > 0 else None
            next_row = rows[index + 1] if index + 1 < len(rows) else None
            prev_token = _token(prev_row)
            next_token = _token(next_row)
            prev_role = _role(prev_row)
            current_role = _role(row)
            next_role = _role(next_row)
            rows_out.append(
                {
                    "token": token,
                    "world": world,
                    "tick": _int(row, "tick"),
                    "prev_token": prev_token,
                    "next_token": next_token,
                    "prev_role": prev_role,
                    "current_role": current_role,
                    "next_role": next_role,
                    "prev_same": int(prev_token == token),
                    "next_same": int(next_token == token),
                    "prev_next_pair": f"{prev_token}->{next_token}",
                    "current_rekopplung": _float(row, "mcm_rekopplung_quality"),
                    "prev_rekopplung": _float(prev_row, "mcm_rekopplung_quality"),
                    "next_rekopplung": _float(next_row, "mcm_rekopplung_quality"),
                    "current_strain": _float(row, "mcm_strain_quality"),
                    "prev_strain": _float(prev_row, "mcm_strain_quality"),
                    "next_strain": _float(next_row, "mcm_strain_quality"),
                    "current_loudness": _float(row, "perception_auditory_loudness"),
                    "prev_loudness": _float(prev_row, "perception_auditory_loudness"),
                    "next_loudness": _float(next_row, "perception_auditory_loudness"),
                    "current_blur": _float(row, "perception_visual_blur"),
                    "prev_blur": _float(prev_row, "perception_visual_blur"),
                    "next_blur": _float(next_row, "perception_visual_blur"),
                    "current_tension": _float(row, "mcm_feldwirkung_mcm_tension"),
                    "prev_tension": _float(prev_row, "mcm_feldwirkung_mcm_tension"),
                    "next_tension": _float(next_row, "mcm_feldwirkung_mcm_tension"),
                }
            )
    rows_out.sort(key=lambda row: (str(row["token"]), str(row["world"]), int(row["tick"])))
    return rows_out


def _summaries(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["token"])].append(row)
    summaries: list[dict[str, object]] = []
    for token, items in sorted(grouped.items()):
        prev_counter = Counter(str(row["prev_token"]) for row in items if str(row["prev_token"]) != "-")
        next_counter = Counter(str(row["next_token"]) for row in items if str(row["next_token"]) != "-")
        pair_counter = Counter(str(row["prev_next_pair"]) for row in items)
        world_counter = Counter(str(row["world"]) for row in items)
        current_roles = Counter(str(row["current_role"]) for row in items)
        neighbor_roles = Counter(
            [str(row["prev_role"]) for row in items if str(row["prev_role"]) != "-"]
            + [str(row["next_role"]) for row in items if str(row["next_role"]) != "-"]
        )
        summaries.append(
            {
                "token": token,
                "contacts": len(items),
                "worlds": len(world_counter),
                "world_profile": "; ".join(f"{name}:{count}" for name, count in world_counter.most_common(8)),
                "dominant_prev": prev_counter.most_common(1)[0][0] if prev_counter else "-",
                "dominant_prev_count": prev_counter.most_common(1)[0][1] if prev_counter else 0,
                "dominant_next": next_counter.most_common(1)[0][0] if next_counter else "-",
                "dominant_next_count": next_counter.most_common(1)[0][1] if next_counter else 0,
                "dominant_pair": pair_counter.most_common(1)[0][0] if pair_counter else "-",
                "dominant_pair_count": pair_counter.most_common(1)[0][1] if pair_counter else 0,
                "current_role_profile": "; ".join(f"{name}:{count}" for name, count in current_roles.most_common(4)),
                "neighbor_role_profile": "; ".join(f"{name}:{count}" for name, count in neighbor_roles.most_common(4)),
                "self_prev_share": sum(int(row["prev_same"]) for row in items) / max(1, len(items)),
                "self_next_share": sum(int(row["next_same"]) for row in items) / max(1, len(items)),
                "rekopplung_delta_next": _avg([float(row["next_rekopplung"]) - float(row["current_rekopplung"]) for row in items]),
                "strain_delta_next": _avg([float(row["next_strain"]) - float(row["current_strain"]) for row in items]),
                "loudness_delta_next": _avg([float(row["next_loudness"]) - float(row["current_loudness"]) for row in items]),
                "blur_delta_next": _avg([float(row["next_blur"]) - float(row["current_blur"]) for row in items]),
                "tension_delta_next": _avg([float(row["next_tension"]) - float(row["current_tension"]) for row in items]),
            }
        )
    return summaries


def _write_csv(rows: list[dict[str, object]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        out.write_text("", encoding="utf-8")
        return
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def _write_markdown(summary_rows: list[dict[str, object]], detail_rows: list[dict[str, object]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# MCM-Token Nachbarschaftslupe",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft, welche MCM-Episodentokens vor und nach den Ziel-Tokens auftreten.",
        "Damit wird unterschieden, ob ein Zonenwechsel am Token selbst haengt oder an veraenderter Nachbarschaft im Feld.",
        "",
        "## Uebersicht",
        "",
        "| Token | Kontakte | Welten | Dominant davor | Dominant danach | Dominantes Paar | Selbstbindung vorher/nachher | Nachbarrollen |",
        "|---|---:|---:|---|---|---|---|---|",
    ]
    for row in summary_rows:
        lines.append(
            f"| {row['token']} | {row['contacts']} | {row['worlds']} | "
            f"{row['dominant_prev']} ({row['dominant_prev_count']}) | "
            f"{row['dominant_next']} ({row['dominant_next_count']}) | "
            f"{row['dominant_pair']} ({row['dominant_pair_count']}) | "
            f"{_fmt(row['self_prev_share'])}/{_fmt(row['self_next_share'])} | "
            f"{row['neighbor_role_profile']} |"
        )
    lines.extend(["", "## Bewegungsachsen Zum Nachfolger", "", "| Token | Rekopplung | Strain | Lautheit | Unschaerfe | Spannung |", "|---|---:|---:|---:|---:|---:|"])
    for row in summary_rows:
        lines.append(
            f"| {row['token']} | {_fmt(row['rekopplung_delta_next'])} | {_fmt(row['strain_delta_next'])} | "
            f"{_fmt(row['loudness_delta_next'])} | {_fmt(row['blur_delta_next'])} | {_fmt(row['tension_delta_next'])} |"
        )

    lines.extend(["", "## Befund", ""])
    for row in summary_rows:
        token = str(row["token"])
        self_next = float(row["self_next_share"])
        next_rek = float(row["rekopplung_delta_next"])
        next_strain = float(row["strain_delta_next"])
        if self_next >= 0.75:
            relation = "starke Selbstnachbarschaft"
        elif next_rek > 0 and next_strain <= 0:
            relation = "rekoppelnde Nachbarschaft"
        elif next_rek < 0 and next_strain > 0:
            relation = "oeffnende Nachbarschaft"
        else:
            relation = "gemischte Nachbarschaft"
        lines.append(f"- `{token}`: {relation}; dominanter Nachfolger `{row['dominant_next']}`.")

    lines.extend(
        [
            "",
            "## Gesamtlesart",
            "",
            "Wenn ein Token in eine stabile oder rekoppelnde Nachbarschaft eingebettet ist, wirkt sein Zonenwechsel weniger wie isolierter Kontakt und mehr wie Feldbewegung.",
            "Wenn die Nachbarschaft wechselhaft wird oder die Selbstbindung sinkt, ist Drift eher als Veraenderung des lokalen Feldraums zu lesen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollten die Nachbarschaftsmuster gegen die Verdichtungszonen klassifiziert werden: stabile Insel, rekoppelnder Pfad, offene Drift oder Randpfad.",
            "",
        ]
    )
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", action="append", default=[])
    parser.add_argument("--input", action="append", default=[])
    parser.add_argument("--out-md", required=True)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--detail-csv", required=True)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    detail_rows = _collect(_parse_inputs(args.input, root), args.token or DEFAULT_TOKENS)
    summary_rows = _summaries(detail_rows)
    _write_csv(summary_rows, Path(args.out_csv))
    _write_csv(detail_rows, Path(args.detail_csv))
    _write_markdown(summary_rows, detail_rows, Path(args.out_md))
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")
    print(f"wrote {args.detail_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
