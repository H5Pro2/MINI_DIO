from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


METRIC_KEYS = [
    "hoeren_energy_tone",
    "hoeren_energy_shift",
    "sehen_form_stability",
    "sehen_form_change",
    "rezeptor_field_intake_pressure",
    "perception_auditory_loudness",
    "perception_auditory_listen_tendency",
    "mcm_feldwirkung_mcm_tension",
    "mcm_feldwirkung_mcm_coherence",
    "mcm_rekopplung_quality",
    "mcm_carry_quality",
    "mcm_strain_quality",
]


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _float(row: dict[str, str], key: str) -> float:
    try:
        value = float(row.get(key, "") or 0.0)
    except ValueError:
        return 0.0
    return 0.0 if value != value else value


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _role_from_values(values: dict[str, float]) -> str:
    tension = values.get("mcm_feldwirkung_mcm_tension", 0.0)
    coherence = values.get("mcm_feldwirkung_mcm_coherence", 0.0)
    rek = values.get("mcm_rekopplung_quality", 0.0)
    carry = values.get("mcm_carry_quality", 0.0)
    strain = values.get("mcm_strain_quality", 0.0)
    tone_shift = abs(values.get("hoeren_energy_shift", 0.0))
    form_change = abs(values.get("sehen_form_change", 0.0))

    if rek >= 0.715 and carry >= 0.54 and strain <= 0.145 and tension <= 0.10:
        return "stabilisierende_rueckbindung"
    if tension >= 0.14 or strain >= 0.17:
        return "spannungsnahe_belastung"
    if tone_shift >= 0.24 or form_change >= 0.18:
        return "uebergang_oeffnung"
    if coherence >= 0.62 and rek >= 0.70:
        return "kohaerente_bruecke"
    return "gemischte_nachbarschaft"


def _top(counter: Counter[str], limit: int = 4) -> str:
    if not counter:
        return "-"
    return ";".join(f"{name}:{count}" for name, count in counter.most_common(limit))


def _read_baseline(path: Path) -> dict[str, str]:
    rows = _load(path)
    return {row["family"]: row["field_role_reading"] for row in rows if row.get("family")}


def _episode_path(debug_dir: Path) -> Path:
    return debug_dir / "dio_mini_lauf_2" / "episodes.csv"


def _world_label(debug_dir: Path) -> str:
    return debug_dir.name.replace("follow_candidate_", "").replace("_", " ")


def _world_rows(debug_dirs: list[Path], baseline: dict[str, str]) -> list[dict[str, object]]:
    wanted = set(baseline)
    out: list[dict[str, object]] = []
    for debug_dir in debug_dirs:
        episodes_path = _episode_path(debug_dir)
        if not episodes_path.exists():
            continue
        by_family: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in _load(episodes_path):
            family = row.get("symbol_family", "") or ""
            if family in wanted:
                by_family[family].append(row)

        for family in sorted(wanted):
            items = by_family.get(family, [])
            if not items:
                out.append(
                    {
                        "world": _world_label(debug_dir),
                        "family": family,
                        "baseline_role": baseline[family],
                        "events": 0,
                        "observed_role": "nicht_aufgetreten",
                        "role_state": "nicht_aufgetreten",
                        "role_profile": "-",
                        "passive_effect_profile": "-",
                        **{key: 0.0 for key in METRIC_KEYS},
                    }
                )
                continue

            metric_avg = {key: round(_avg([_float(row, key) for row in items]), 6) for key in METRIC_KEYS}
            event_roles = Counter(_role_from_values({key: _float(row, key) for key in METRIC_KEYS}) for row in items)
            effect_classes = Counter(row.get("passive_mcm_effect_class", "-") or "-" for row in items)
            observed_role = event_roles.most_common(1)[0][0]
            if observed_role == baseline[family]:
                state = "stabil"
            elif len(items) < 4:
                state = "zu_duenn"
            else:
                state = "gekippt"

            out.append(
                {
                    "world": _world_label(debug_dir),
                    "family": family,
                    "baseline_role": baseline[family],
                    "events": len(items),
                    "observed_role": observed_role,
                    "role_state": state,
                    "role_profile": _top(event_roles),
                    "passive_effect_profile": _top(effect_classes),
                    **metric_avg,
                }
            )
    out.sort(key=lambda row: (str(row["family"]), str(row["world"])))
    return out


def _family_summary(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["family"])].append(row)

    out: list[dict[str, object]] = []
    for family, items in grouped.items():
        state_counts = Counter(str(row["role_state"]) for row in items)
        role_counts = Counter(str(row["observed_role"]) for row in items)
        total_worlds = len(items)
        active_worlds = sum(1 for row in items if int(row["events"]) > 0)
        stable_worlds = state_counts.get("stabil", 0)
        shifted_worlds = state_counts.get("gekippt", 0)
        out.append(
            {
                "family": family,
                "baseline_role": str(items[0]["baseline_role"]),
                "worlds": total_worlds,
                "active_worlds": active_worlds,
                "stable_worlds": stable_worlds,
                "shifted_worlds": shifted_worlds,
                "thin_or_missing_worlds": state_counts.get("zu_duenn", 0) + state_counts.get("nicht_aufgetreten", 0),
                "stability_ratio_active": round(stable_worlds / max(1, active_worlds), 6),
                "observed_role_profile": _top(role_counts, 6),
                "state_profile": _top(state_counts, 6),
                "events": sum(int(row["events"]) for row in items),
            }
        )
    out.sort(key=lambda row: (-float(row["stability_ratio_active"]), -int(row["active_worlds"]), str(row["family"])))
    return out


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(summary: list[dict[str, object]], out: Path) -> None:
    lines = [
        "# 1185 - Brueckennetz Biasrollen in Folgewelten",
        "",
        "## Grundfrage",
        "",
        "Bleiben die in 1182/1183 gelesenen Feldrollen der Biasfamilien in neuen Folgewelten stabil,",
        "oder kippen sie bei anderer Weltspannung in andere Rollen?",
        "",
        "Die Pruefung bleibt passiv. Keine Handlung, kein Gate, keine Strategie.",
        "",
        "## Familienuebersicht",
        "",
        "| Familie | Baseline-Rolle | aktive Welten | stabile Welten | gekippte Welten | Stabilitaet aktiv | beobachtete Rollen |",
        "|---|---|---:|---:|---:|---:|---|",
    ]
    for row in summary:
        lines.append(
            f"| {row['family']} | {row['baseline_role']} | {row['active_worlds']} | {row['stable_worlds']} | "
            f"{row['shifted_worlds']} | {float(row['stability_ratio_active']):.2f} | {row['observed_role_profile']} |"
        )

    stable = [row for row in summary if float(row["stability_ratio_active"]) >= 0.75 and int(row["active_worlds"]) >= 3]
    shifting = [row for row in summary if int(row["shifted_worlds"]) > int(row["stable_worlds"])]
    mixed = [row for row in summary if row not in stable and row not in shifting]

    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"- stabile Rollenfamilien: `{', '.join(str(row['family']) for row in stable) or '-'}`",
            f"- kippende Rollenfamilien: `{', '.join(str(row['family']) for row in shifting) or '-'}`",
            f"- gemischte / duenne Rollenfamilien: `{', '.join(str(row['family']) for row in mixed) or '-'}`",
            "",
            "## Lesart",
            "",
            "Wenn eine Familie ueber mehrere Folgewelten dieselbe Feldrolle behaelt, spricht das fuer eine robuste lokale Feldfunktion.",
            "Wenn sie kippt, ist sie wahrscheinlich kein fester Bedeutungsblock, sondern situationsabhaengig an Weltspannung und Nachbarschaft gekoppelt.",
            "",
            "Damit wird das Brueckennetz nicht als feste Symboltabelle gelesen, sondern als dynamisches Rollenfeld.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollten die stabilen und kippenden Rollenfamilien gegen konkrete Rohweltfenster gelesen werden: Welche Weltmerkmale halten eine Rolle stabil, und welche Weltmerkmale lassen sie kippen?",
        ]
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", required=True)
    parser.add_argument("--debug-dir", action="append", required=True)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--out-summary-csv", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    baseline = _read_baseline(Path(args.baseline))
    rows = _world_rows([Path(value) for value in args.debug_dir], baseline)
    summary = _family_summary(rows)
    _write_csv(rows, Path(args.out_csv))
    _write_csv(summary, Path(args.out_summary_csv))
    _write_md(summary, Path(args.out_md))
    print(f"families={len(summary)} rows={len(rows)}")
    print(f"wrote {args.out_csv}")
    print(f"wrote {args.out_summary_csv}")
    print(f"wrote {args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
