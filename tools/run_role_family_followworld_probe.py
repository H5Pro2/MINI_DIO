from __future__ import annotations

import argparse
import csv
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

from create_csv_slice import create_slice


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = ROOT / "docs" / "befunde"

DEFAULT_WORLDS = [
    ("BTC", "data/1-12_2025_1h_BTCUSDT.csv"),
    ("SOL", "data/1-12_2025_1h_SOLUSDT.csv"),
    ("DOGE", "data/kontrolliert_doge_2025_1h_10k_DOGEUSDT.csv"),
    ("PAXG", "data/kontrolliert_paxg_2025_1h_10k_PAXGUSDT.csv"),
    ("XRP", "data/kontrolliert_xrp_2025_1h_10k_XRPUSDT.csv"),
]
DEFAULT_TARGETS = ["rf_07", "rf_21", "rf_05"]
PHASES = ["frueh", "mitte", "spaet"]


def _resolve(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def _relative_or_absolute(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def _safe_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _clip01(value: float) -> float:
    return max(0.0, min(1.0, value))


def _split_symbols(value: object) -> list[str]:
    return [part.strip() for part in str(value or "").split(";") if part.strip() and part.strip() != "-"]


def _safe_name(value: object) -> str:
    return "".join(char.lower() if char.isalnum() else "_" for char in str(value)).strip("_")


def _phase(index: int, total: int) -> str:
    ratio = index / total if total else 0.0
    if ratio < 1 / 3:
        return "frueh"
    if ratio < 2 / 3:
        return "mitte"
    return "spaet"


def _field_contact_class(row: dict[str, str]) -> str:
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


def _load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fields: list[str] = []
    seen: set[str] = set()
    for row in rows:
        for field in row:
            if field not in seen:
                seen.add(field)
                fields.append(field)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def _load_targets(path: Path, selected: list[str]) -> dict[str, list[str]]:
    by_role = {str(row.get("role_family", "")): row for row in _load_csv(path)}
    targets: dict[str, list[str]] = {}
    for role_family in selected:
        row = by_role.get(role_family)
        if row is None:
            raise ValueError(f"Rollenfamilie fehlt in {path}: {role_family}")
        symbols = _split_symbols(row.get("member_symbols"))
        expected = _safe_int(row.get("members"))
        if len(symbols) != expected:
            raise ValueError(
                f"Unvollstaendige Symbolbasis fuer {role_family}: {len(symbols)} von {expected} Mitgliedern"
            )
        targets[role_family] = symbols
    return targets


def _load_source_member_counts(
    path: Path,
    targets: dict[str, list[str]],
) -> dict[str, Counter[str]]:
    out = {role_family: Counter() for role_family in targets}
    for row in _load_csv(path):
        role_family = str(row.get("role_family", "") or "")
        symbol_family = str(row.get("symbol_family", "") or "")
        if role_family in targets and symbol_family in targets[role_family]:
            out[role_family][symbol_family] += _safe_int(row.get("follow_events"))
    for role_family, members in targets.items():
        missing = [symbol for symbol in members if out[role_family][symbol] <= 0]
        if missing:
            raise ValueError(f"Quellenprofil fuer {role_family} unvollstaendig: {';'.join(missing)}")
    return out


def _parse_world(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("world spec must be ASSET=path.csv")
    asset, raw_path = value.split("=", 1)
    return asset.strip().upper(), _resolve(raw_path.strip())


def _ensure_slice(asset: str, source: Path, start: int, rows: int, data_dir: Path) -> Path:
    target = data_dir / f"kontrolliert_2070_{_safe_name(asset)}_2025_1h_start{start}_rows{rows}.csv"
    if target.exists():
        with target.open(newline="", encoding="utf-8") as handle:
            existing_rows = sum(1 for _ in csv.DictReader(handle))
        if existing_rows == rows:
            return target
    result = create_slice(source, target, start=start, rows=rows)
    if _safe_int(result.get("rows_written")) != rows:
        raise ValueError(f"{source} schrieb {result.get('rows_written')} statt {rows} Zeilen")
    return target


def _run_mini(data_path: Path, debug_root: Path, world_label: str) -> Path:
    run_dir = debug_root / "dio_mini_lauf_1"
    report_path = run_dir / "mini_report.json"
    if report_path.exists() and (run_dir / "episodes.csv").exists():
        return run_dir
    memory_path = debug_root / "memory.json"
    command = [
        sys.executable,
        "-m",
        "mini_dio.run_mini",
        "--data",
        _relative_or_absolute(data_path),
        "--runs",
        "1",
        "--reset-memory",
        "--memory",
        _relative_or_absolute(memory_path),
        "--debug-root",
        _relative_or_absolute(debug_root),
        "--world-label",
        world_label,
        "--sense-mode",
        "world_relative",
    ]
    subprocess.run(command, cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
    return run_dir


def _phase_mean(rows: list[dict[str, str]], field: str, fallback: str = "") -> float:
    values = [_safe_float(row.get(field) or (row.get(fallback) if fallback else 0.0)) for row in rows]
    return _mean(values)


def _build_member_rows(
    world: dict[str, object],
    episodes: list[dict[str, str]],
    targets: dict[str, list[str]],
) -> list[dict[str, object]]:
    by_symbol: dict[str, list[tuple[str, dict[str, str]]]] = defaultdict(list)
    phase_totals: Counter[str] = Counter()
    for index, episode in enumerate(episodes):
        phase = _phase(index, len(episodes))
        phase_totals[phase] += 1
        by_symbol[str(episode.get("symbol_family", "-") or "-")].append((phase, episode))

    out: list[dict[str, object]] = []
    for role_family, members in targets.items():
        for symbol_family in members:
            entries = by_symbol.get(symbol_family, [])
            all_rows = [row for _, row in entries]
            phase_rows = {
                phase: [row for row_phase, row in entries if row_phase == phase]
                for phase in PHASES
            }
            field_classes = Counter(_field_contact_class(row) for row in all_rows)
            row: dict[str, object] = {
                **world,
                "role_family": role_family,
                "symbol_family": symbol_family,
                "target_members": len(members),
                "event_count": len(all_rows),
                "world_event_share": len(all_rows) / max(1, len(episodes)),
                "phase_presence": sum(1 for phase in PHASES if phase_rows[phase]),
                "dominant_field_contact_class": field_classes.most_common(1)[0][0] if field_classes else "-",
                "avg_carry": _phase_mean(all_rows, "mcm_carry_quality"),
                "avg_strain": _phase_mean(all_rows, "mcm_strain_quality"),
                "avg_rekopplung": _phase_mean(
                    all_rows,
                    "mcm_adaptive_rekopplung_quality",
                    "mcm_rekopplung_quality",
                ),
            }
            for phase in PHASES:
                values = phase_rows[phase]
                row[f"count_{phase}"] = len(values)
                row[f"share_{phase}"] = len(values) / max(1, phase_totals[phase])
                row[f"rekopplung_{phase}"] = _phase_mean(
                    values,
                    "mcm_adaptive_rekopplung_quality",
                    "mcm_rekopplung_quality",
                )
                row[f"strain_{phase}"] = _phase_mean(values, "mcm_strain_quality")
                row[f"afterimage_{phase}"] = _phase_mean(values, "mini_afterimage")
                row[f"temporal_{phase}"] = _phase_mean(values, "mini_temporal_trust_support")
            row["share_delta_spaet_frueh"] = _safe_float(row["share_spaet"]) - _safe_float(row["share_frueh"])
            row["afterimage_delta_spaet_frueh"] = _safe_float(row["afterimage_spaet"]) - _safe_float(row["afterimage_frueh"])
            row["temporal_delta_spaet_frueh"] = _safe_float(row["temporal_spaet"]) - _safe_float(row["temporal_frueh"])
            row["strain_delta_spaet_frueh"] = _safe_float(row["strain_spaet"]) - _safe_float(row["strain_frueh"])
            row["boundary"] = "passive_same_basis_family_followworld_member_no_action_no_direction"
            out.append(row)
    return out


def _event_balance(counts: list[int]) -> float:
    if not counts or sum(counts) <= 0:
        return 0.0
    if len(counts) == 1:
        return 1.0
    concentration = max(counts) / sum(counts)
    equal_concentration = 1.0 / len(counts)
    return _clip01((1.0 - concentration) / (1.0 - equal_concentration))


def _weighted_mean(rows: list[dict[str, object]], value_field: str, weight_field: str) -> float:
    total_weight = sum(_safe_float(row.get(weight_field)) for row in rows)
    if total_weight <= 0.0:
        return 0.0
    return sum(
        _safe_float(row.get(value_field)) * _safe_float(row.get(weight_field))
        for row in rows
    ) / total_weight


def _build_world_family_rows(member_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in member_rows:
        grouped[(str(row["world_label"]), str(row["role_family"]))].append(row)

    out: list[dict[str, object]] = []
    for (_, role_family), rows in grouped.items():
        found = [row for row in rows if _safe_int(row.get("event_count")) > 0]
        counts = [_safe_int(row.get("event_count")) for row in rows]
        total_events = sum(counts)
        found_symbols = [str(row["symbol_family"]) for row in found]
        missing_symbols = [str(row["symbol_family"]) for row in rows if row not in found]
        target_members = len(rows)
        coverage = len(found) / max(1, target_members)
        if len(found) == target_members:
            reading = "familie_als_ganzes_lesbar"
        elif found:
            reading = "familie_fragmentarisch_lesbar"
        else:
            reading = "familie_nicht_gelesen"
        dominant = max(rows, key=lambda row: _safe_int(row.get("event_count")))
        early_events = sum(_safe_int(row.get("count_frueh")) for row in rows)
        late_events = sum(_safe_int(row.get("count_spaet")) for row in rows)
        afterimage_early = _weighted_mean(rows, "afterimage_frueh", "count_frueh")
        afterimage_late = _weighted_mean(rows, "afterimage_spaet", "count_spaet")
        temporal_early = _weighted_mean(rows, "temporal_frueh", "count_frueh")
        temporal_late = _weighted_mean(rows, "temporal_spaet", "count_spaet")
        out.append(
            {
                "asset": rows[0]["asset"],
                "window_start": rows[0]["window_start"],
                "window_end": rows[0]["window_end"],
                "world_label": rows[0]["world_label"],
                "source_path": rows[0]["source_path"],
                "data_path": rows[0]["data_path"],
                "world_events": rows[0]["world_events"],
                "role_family": role_family,
                "target_members": target_members,
                "found_members": len(found),
                "member_coverage": coverage,
                "found_symbols": ";".join(found_symbols),
                "missing_symbols": ";".join(missing_symbols),
                "total_family_events": total_events,
                "family_event_share": total_events / max(1, _safe_int(rows[0]["world_events"])),
                "event_concentration": max(counts) / max(1, total_events),
                "event_balance": _event_balance(counts),
                "dominant_member": str(dominant["symbol_family"]) if total_events else "-",
                "phase_complete_members": sum(1 for row in rows if _safe_int(row.get("phase_presence")) == 3),
                "phase_complete_ratio": sum(1 for row in rows if _safe_int(row.get("phase_presence")) == 3) / max(1, target_members),
                "early_family_events": early_events,
                "late_family_events": late_events,
                "mean_rekopplung_spaet": _weighted_mean(rows, "rekopplung_spaet", "count_spaet"),
                "mean_strain_spaet": _weighted_mean(rows, "strain_spaet", "count_spaet"),
                "mean_afterimage_delta": afterimage_late - afterimage_early,
                "mean_temporal_delta": temporal_late - temporal_early,
                "source_follow_reading": reading,
                "boundary": "passive_same_basis_family_followworld_summary_no_action_no_direction",
            }
        )
    out.sort(key=lambda row: (str(row["asset"]), _safe_int(row["window_start"]), str(row["role_family"])))
    return out


def _followworld_reading(
    total_events: int,
    global_coverage: float,
    world_presence: float,
    mean_coverage: float,
    whole_ratio: float,
    event_balance: float,
) -> str:
    if total_events <= 0:
        return "familie_nicht_wiedergefunden"
    if global_coverage < 1.0:
        return "fragmentarischer_folgeweltanschluss"
    if event_balance < 0.35:
        return "kernlastiger_folgeweltanschluss"
    if world_presence >= 0.80 and mean_coverage >= 0.80 and whole_ratio >= 0.60:
        return "familienraum_konsistent_anschlussfaehig"
    if world_presence >= 0.70 and mean_coverage >= 0.60:
        return "familienraum_breit_anschlussfaehig"
    if world_presence >= 0.40:
        return "familienraum_offen_anschlussfaehig"
    return "familienraum_lokal_anschlussfaehig"


def _distribution_drift(
    members: list[str],
    source_counts: Counter[str],
    follow_counts: Counter[str],
) -> float:
    source_total = sum(source_counts[symbol] for symbol in members)
    follow_total = sum(follow_counts[symbol] for symbol in members)
    if source_total <= 0 or follow_total <= 0:
        return 1.0
    return 0.5 * sum(
        abs(
            (source_counts[symbol] / source_total)
            - (follow_counts[symbol] / follow_total)
        )
        for symbol in members
    )


def _internal_role_reading(drift: float, source_dominant: str, follow_dominant: str) -> str:
    dominant_shift = source_dominant != follow_dominant
    if dominant_shift and drift >= 0.30:
        return "starker_innerer_dominanzwechsel"
    if dominant_shift and drift >= 0.15:
        return "offener_innerer_dominanzwechsel"
    if dominant_shift:
        return "leichter_dominanzwechsel_bei_naher_verteilung"
    if drift >= 0.30:
        return "rollenverteilung_stark_verschoben"
    if drift >= 0.15:
        return "rollenverteilung_verschoben"
    return "rollenverteilung_nahe_stabil"


def _build_family_summary(
    world_rows: list[dict[str, object]],
    member_rows: list[dict[str, object]],
    targets: dict[str, list[str]],
    source_counts_by_role: dict[str, Counter[str]],
) -> list[dict[str, object]]:
    by_role: dict[str, list[dict[str, object]]] = defaultdict(list)
    member_by_role: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in world_rows:
        by_role[str(row["role_family"])].append(row)
    for row in member_rows:
        member_by_role[str(row["role_family"])].append(row)

    out: list[dict[str, object]] = []
    for role_family, target_symbols in targets.items():
        rows = by_role[role_family]
        detail = member_by_role[role_family]
        present = [row for row in rows if _safe_int(row.get("found_members")) > 0]
        late_present = [row for row in present if _safe_int(row.get("late_family_events")) > 0]
        whole = [row for row in rows if _safe_int(row.get("found_members")) == len(target_symbols)]
        partial = [row for row in rows if 0 < _safe_int(row.get("found_members")) < len(target_symbols)]
        symbol_counts = Counter()
        for row in detail:
            symbol_counts[str(row["symbol_family"])] += _safe_int(row.get("event_count"))
        source_counts = source_counts_by_role[role_family]
        global_found = [symbol for symbol in target_symbols if symbol_counts[symbol] > 0]
        total_events = sum(symbol_counts.values())
        source_total_events = sum(source_counts[symbol] for symbol in target_symbols)
        world_presence = len(present) / max(1, len(rows))
        mean_coverage = _mean([_safe_float(row.get("member_coverage")) for row in rows])
        whole_ratio = len(whole) / max(1, len(rows))
        balance = _event_balance([symbol_counts[symbol] for symbol in target_symbols])
        global_coverage = len(global_found) / max(1, len(target_symbols))
        source_dominant = max(target_symbols, key=lambda symbol: source_counts[symbol])
        follow_dominant = max(target_symbols, key=lambda symbol: symbol_counts[symbol])
        distribution_drift = _distribution_drift(target_symbols, source_counts, symbol_counts)
        continuity_score = (
            (0.35 * world_presence)
            + (0.35 * mean_coverage)
            + (0.20 * whole_ratio)
            + (0.10 * balance)
        )
        out.append(
            {
                "role_family": role_family,
                "target_members": len(target_symbols),
                "member_symbols": ";".join(target_symbols),
                "global_found_members": len(global_found),
                "global_member_coverage": global_coverage,
                "worlds": len(rows),
                "worlds_present": len(present),
                "world_presence_ratio": world_presence,
                "whole_family_worlds": len(whole),
                "whole_family_ratio": whole_ratio,
                "partial_family_worlds": len(partial),
                "missing_worlds": len(rows) - len(present),
                "assets_present": len({str(row["asset"]) for row in present}),
                "mean_member_coverage": mean_coverage,
                "total_follow_events": total_events,
                "source_total_events": source_total_events,
                "source_event_concentration": max(source_counts.values(), default=0) / max(1, source_total_events),
                "family_event_concentration": max(symbol_counts.values(), default=0) / max(1, total_events),
                "family_event_balance": balance,
                "source_dominant_member": source_dominant,
                "follow_dominant_member": follow_dominant,
                "dominant_member_shift": (
                    f"{source_dominant}->{follow_dominant}"
                    if source_dominant != follow_dominant
                    else f"stabil:{source_dominant}"
                ),
                "member_distribution_drift": distribution_drift,
                "internal_role_reading": _internal_role_reading(
                    distribution_drift,
                    source_dominant,
                    follow_dominant,
                ),
                "source_member_event_profile": ";".join(
                    f"{symbol}:{source_counts[symbol]}" for symbol in target_symbols
                ),
                "member_event_profile": ";".join(
                    f"{symbol}:{symbol_counts[symbol]}" for symbol in target_symbols
                ),
                "mean_family_event_share": _mean(
                    [_safe_float(row.get("family_event_share")) for row in rows]
                ),
                "mean_phase_complete_ratio": _mean(
                    [_safe_float(row.get("phase_complete_ratio")) for row in rows]
                ),
                "mean_rekopplung_spaet": _mean(
                    [_safe_float(row.get("mean_rekopplung_spaet")) for row in late_present]
                ),
                "mean_strain_spaet": _mean(
                    [_safe_float(row.get("mean_strain_spaet")) for row in late_present]
                ),
                "mean_afterimage_delta": _mean(
                    [_safe_float(row.get("mean_afterimage_delta")) for row in present]
                ),
                "mean_temporal_delta": _mean(
                    [_safe_float(row.get("mean_temporal_delta")) for row in present]
                ),
                "family_continuity_score": continuity_score,
                "followworld_reading": _followworld_reading(
                    total_events,
                    global_coverage,
                    world_presence,
                    mean_coverage,
                    whole_ratio,
                    balance,
                ),
                "boundary": "passive_same_basis_family_followworld_family_no_action_no_direction",
            }
        )
    return out


def _fmt(value: object, digits: int = 3) -> str:
    return f"{_safe_float(value):.{digits}f}"


def _write_markdown(
    path: Path,
    summary: list[dict[str, object]],
    world_rows: list[dict[str, object]],
    targets: dict[str, list[str]],
    starts: list[int],
    rows_per_world: int,
) -> None:
    worlds = sorted(
        {(str(row["asset"]), _safe_int(row["window_start"]), str(row["world_label"])) for row in world_rows},
        key=lambda item: (item[0], item[1]),
    )
    by_world_role = {
        (str(row["world_label"]), str(row["role_family"])): row
        for row in world_rows
    }
    lines = [
        "# 2070 - Rollenfamilien in neuen Folgewelten auf gleicher Symbolbasis",
        "",
        "## Zweck",
        "",
        "Diese Auswertung startet neue reale Folgeweltlaeufe und liest die vollstaendigen Mitglieder von `rf_07`, `rf_21` und `rf_05` direkt aus der passiven Rollenfamilien-Memory 2069 zurueck.",
        "",
        "Die Symbolbasis wird nicht neu gruppiert. Geprueft werden exakt die in 2066 gebildeten `dio_*`-Mitglieder.",
        "",
        "## Methode",
        "",
        f"- reale 1h-Folgewelten: `{len(worlds)}`",
        f"- Assets: `{';'.join(sorted({asset for asset, _, _ in worlds}))}`",
        f"- Startpunkte pro Asset: `{starts}`",
        f"- Beobachtungen pro Welt: `{rows_per_world}` Rohzeilen",
        "- veroeffentlichtes Weltarchiv: `data/2070_role_family_followworlds.zip`",
        "- entpackte Weltdateien und Debug-Ausgaben bleiben lokal und werden nicht gepusht",
        "- pro Welt ein Lauf mit frischer episodischer Memory",
        "- Wahrnehmungsmodus: `world_relative`",
        "- keine Nullwelt in diesem Durchlauf; geprueft wird die reale spaete Anschlussfaehigkeit",
        "- keine Handlung, keine Richtung, kein Gate und kein motorischer Impuls",
        "",
        "## Familienbefund",
        "",
        "| role_family | Basis | global gefunden | Welten mit Anschluss | ganze Familie | mittlere Abdeckung | Ereignisbalance | Ereignisse | Kontinuitaet | Lesung |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in summary:
        lines.append(
            f"| {row['role_family']} | {row['target_members']} | {row['global_found_members']} | "
            f"{row['worlds_present']}/{row['worlds']} | {row['whole_family_worlds']}/{row['worlds']} | "
            f"{_fmt(row['mean_member_coverage'])} | {_fmt(row['family_event_balance'])} | "
            f"{row['total_follow_events']} | {_fmt(row['family_continuity_score'])} | {row['followworld_reading']} |"
        )
    lines.extend(
        [
            "",
            "## Innere Rollenbewegung",
            "",
            "Die Verteilungsdrift vergleicht die Ereignisanteile der Mitglieder zwischen 2066 und den neuen Folgewelten. `0` bedeutet gleiche Verteilung, `1` vollstaendige Verschiebung.",
            "",
            "| role_family | Dominanz 2066 | Dominanz 2070 | Verteilungsdrift | innere Lesung | Profil 2066 | Profil 2070 |",
            "|---|---|---|---:|---|---|---|",
        ]
    )
    for row in summary:
        lines.append(
            f"| {row['role_family']} | {row['source_dominant_member']} | {row['follow_dominant_member']} | "
            f"{_fmt(row['member_distribution_drift'])} | {row['internal_role_reading']} | "
            f"{row['source_member_event_profile']} | {row['member_event_profile']} |"
        )
    lines.extend(
        [
            "",
            "## Folgeweltmatrix",
            "",
            "Jede Zelle zeigt `gefundene Mitglieder/Basis (Ereignisse)`.",
            "",
            "| Welt | " + " | ".join(targets) + " |",
            "|---|" + "|".join("---:" for _ in targets) + "|",
        ]
    )
    for asset, start, label in worlds:
        cells = []
        for role_family in targets:
            row = by_world_role[(label, role_family)]
            cells.append(
                f"{row['found_members']}/{row['target_members']} ({row['total_family_events']})"
            )
        lines.append(f"| {asset} {start}-{start + rows_per_world} | " + " | ".join(cells) + " |")
    lines.extend(
        [
            "",
            "## Feldzeit und Nachhall",
            "",
            "| role_family | Rekopplung spaet | Strain spaet | Nachhall-Delta | Feldzeit-Delta | Phasenbreite | Mitgliedsprofil |",
            "|---|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in summary:
        lines.append(
            f"| {row['role_family']} | {_fmt(row['mean_rekopplung_spaet'])} | {_fmt(row['mean_strain_spaet'])} | "
            f"{_fmt(row['mean_afterimage_delta'])} | {_fmt(row['mean_temporal_delta'])} | "
            f"{_fmt(row['mean_phase_complete_ratio'])} | {row['member_event_profile']} |"
        )
    lines.extend(["", "## Lesung", ""])
    for row in summary:
        lines.append(
            f"- `{row['role_family']}`: `{row['followworld_reading']}`; "
            f"{row['worlds_present']} von {row['worlds']} Welten mit Anschluss, "
            f"{row['whole_family_worlds']} davon mit vollstaendiger Familie; "
            f"innere Bewegung: `{row['internal_role_reading']}`."
        )
    lines.extend(
        [
            "",
            "Die Lesung ist diagnostisch. Sie beschreibt, ob ein Bedeutungsraum in spaeten realen Fenstern als Familie weiterlebt, ob er kernlastig wird oder in Fragmente zerfaellt.",
            "",
            "## Grenze",
            "",
            "Die Kennzahlen duerfen nicht als Strategie, Entry-Signal, Richtungsvorgabe oder Handlungsgate verwendet werden. Auch eine konsistente Familie bleibt eine passive Feldbedeutung.",
            "",
            "Wie es weitergeht: Die neuen Folgeweltbefunde sollten als naechstes in die passive Rollenfamilien-Memory rueckgekoppelt werden. Danach koennen die bisher ungelesenen Familien `rf_06`, `rf_13`, `rf_10`, `rf_08` und `rf_17` mit derselben Methode folgen.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Prueft passive Rollenfamilien in neuen realen Folgewelten.")
    parser.add_argument("--memory", default="docs/befunde/2069_PASSIVE_ROLLENFAMILIEN_MEMORY.csv")
    parser.add_argument(
        "--cohesion-detail",
        default="docs/befunde/2066_REALVERSTAERKTE_ROLLENFAMILIEN_KOHAESION.detail.csv",
    )
    parser.add_argument("--target-family", action="append", default=None)
    parser.add_argument("--world", action="append", type=_parse_world, default=None, help="ASSET=CSV")
    parser.add_argument("--start", action="append", type=int, default=None)
    parser.add_argument("--rows", type=int, default=1000)
    parser.add_argument("--data-dir", default="data/generated/2070_role_family_followworlds")
    parser.add_argument("--debug-root", default="debug/2070_role_family_followworlds")
    parser.add_argument("--out-prefix", default="2070_ROLLENFAMILIEN_GLEICHE_SYMBOLBASIS_FOLGEWELTEN")
    args = parser.parse_args()

    selected = args.target_family or list(DEFAULT_TARGETS)
    targets = _load_targets(_resolve(args.memory), selected)
    source_counts = _load_source_member_counts(_resolve(args.cohesion_detail), targets)
    specs = args.world or [(asset, _resolve(path)) for asset, path in DEFAULT_WORLDS]
    starts = args.start or [5000, 6000, 7000]
    data_dir = _resolve(args.data_dir)
    debug_root = _resolve(args.debug_root)

    member_rows: list[dict[str, object]] = []
    for asset, source in specs:
        if not source.exists():
            raise FileNotFoundError(source)
        for start in starts:
            data_path = _ensure_slice(asset, source, start, args.rows, data_dir)
            world_label = f"{asset.lower()}_2025_1h_{start}_{start + args.rows}"
            run_root = debug_root / world_label
            run_dir = _run_mini(data_path, run_root, world_label)
            episodes = _load_csv(run_dir / "episodes.csv")
            world = {
                "asset": asset,
                "window_start": start,
                "window_end": start + args.rows,
                "world_label": world_label,
                "source_path": _relative_or_absolute(source),
                "data_path": _relative_or_absolute(data_path),
                "world_events": len(episodes),
            }
            member_rows.extend(_build_member_rows(world, episodes, targets))

    world_rows = _build_world_family_rows(member_rows)
    summary_rows = _build_family_summary(world_rows, member_rows, targets, source_counts)
    prefix = BEFUNDE / args.out_prefix
    _write_csv(prefix.with_suffix(".detail.csv"), member_rows)
    _write_csv(prefix.with_suffix(".worlds.csv"), world_rows)
    _write_csv(prefix.with_suffix(".summary.csv"), summary_rows)
    _write_markdown(prefix.with_suffix(".md"), summary_rows, world_rows, targets, starts, args.rows)
    print(f"worlds={len(specs) * len(starts)}")
    print(f"member_rows={len(member_rows)}")
    print(f"family_summary={len(summary_rows)}")
    print(f"wrote={prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
