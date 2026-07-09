from __future__ import annotations

import argparse
import csv
import hashlib
import re
from pathlib import Path
from statistics import mean
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

try:
    from tools.build_equal_length_null_worlds import build_null_worlds
    from tools.run_role_family_followworld_probe import (
        _build_family_summary,
        _build_member_rows,
        _build_world_family_rows,
        _load_csv,
        _load_source_member_counts,
        _load_targets,
        _run_mini,
        _safe_float,
        _write_csv,
    )
except ModuleNotFoundError:
    from build_equal_length_null_worlds import build_null_worlds
    from run_role_family_followworld_probe import (
        _build_family_summary,
        _build_member_rows,
        _build_world_family_rows,
        _load_csv,
        _load_source_member_counts,
        _load_targets,
        _run_mini,
        _safe_float,
        _write_csv,
    )


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = ROOT / "docs" / "befunde" / "2001-3000"
DEFAULT_REAL_ARCHIVE = ROOT / "data" / "2070_role_family_followworlds.zip"
DEFAULT_REAL_DIR = ROOT / "data" / "generated" / "2070_role_family_followworlds"
DEFAULT_CONTROL_DIR = ROOT / "data" / "generated" / "2073_role_family_null_controls"
DEFAULT_CONTROL_ARCHIVE = ROOT / "data" / "2073_role_family_null_controls.zip"
DEFAULT_DEBUG_ROOT = ROOT / "debug" / "2073_role_family_null_controls"
DEFAULT_OUT_PREFIX = BEFUNDE / "2073_ROLLENFAMILIEN_REAL_NULL_KONTRAST"
DEFAULT_MEMORY = BEFUNDE / "2069_PASSIVE_ROLLENFAMILIEN_MEMORY.csv"
DEFAULT_COHESION = BEFUNDE / "2066_REALVERSTAERKTE_ROLLENFAMILIEN_KOHAESION.detail.csv"
REAL_SUMMARIES = (
    BEFUNDE / "2070_ROLLENFAMILIEN_GLEICHE_SYMBOLBASIS_FOLGEWELTEN.summary.csv",
    BEFUNDE / "2072_OFFENE_ROLLENFAMILIEN_GLEICHE_SYMBOLBASIS_FOLGEWELTEN.summary.csv",
)
REAL_WORLDS = (
    BEFUNDE / "2070_ROLLENFAMILIEN_GLEICHE_SYMBOLBASIS_FOLGEWELTEN.worlds.csv",
    BEFUNDE / "2072_OFFENE_ROLLENFAMILIEN_GLEICHE_SYMBOLBASIS_FOLGEWELTEN.worlds.csv",
)
FILENAME_RE = re.compile(
    r"kontrolliert_2070_(?P<asset>[a-z0-9]+)_2025_1h_start(?P<start>\d+)_rows(?P<rows>\d+)\.csv$"
)
METRICS = (
    "world_presence_ratio",
    "whole_family_ratio",
    "mean_member_coverage",
    "mean_family_event_share",
    "mean_phase_complete_ratio",
    "member_distribution_drift",
    "mean_afterimage_delta",
    "mean_temporal_delta",
    "family_continuity_score",
)


def _resolve(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def _ensure_real_slices(archive: Path, target_dir: Path) -> list[Path]:
    paths = sorted(target_dir.glob("kontrolliert_2070_*_rows1000.csv"))
    if len(paths) == 15:
        return paths
    target_dir.mkdir(parents=True, exist_ok=True)
    with ZipFile(archive) as handle:
        handle.extractall(target_dir)
    paths = sorted(target_dir.glob("kontrolliert_2070_*_rows1000.csv"))
    if len(paths) != 15:
        raise ValueError(f"Erwartet wurden 15 Realfenster, gefunden wurden {len(paths)}")
    return paths


def _relative(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return str(path.resolve())


def _build_controls(real_paths: list[Path], control_dir: Path) -> list[dict[str, object]]:
    controls: list[dict[str, object]] = []
    for index, source in enumerate(real_paths):
        match = FILENAME_RE.match(source.name)
        if not match:
            raise ValueError(f"Unerwarteter Realfenstername: {source.name}")
        asset = match.group("asset").upper()
        start = int(match.group("start"))
        rows = int(match.group("rows"))
        seed = 207300 + index
        prefix = control_dir / f"kontrolliert_2073_{asset.lower()}_start{start}"
        built = build_null_worlds(source, prefix, rows=rows, seed=seed)
        for kind, key in (("shuffle", "shuffle_order"), ("random_sign", "random_sign")):
            path = Path(str(built[key]))
            controls.append(
                {
                    "asset": asset,
                    "start": start,
                    "rows": rows,
                    "kind": kind,
                    "seed": seed,
                    "source": source,
                    "path": path,
                }
            )
    return controls


def _write_control_archive(path: Path, controls: list[dict[str, object]]) -> None:
    fieldnames = ["asset", "start", "rows", "kind", "seed", "source", "file", "sha256"]
    manifest_rows: list[dict[str, object]] = []
    for item in controls:
        control_path = Path(str(item["path"]))
        manifest_rows.append(
            {
                "asset": item["asset"],
                "start": item["start"],
                "rows": item["rows"],
                "kind": item["kind"],
                "seed": item["seed"],
                "source": _relative(Path(str(item["source"]))),
                "file": control_path.name,
                "sha256": hashlib.sha256(control_path.read_bytes()).hexdigest(),
            }
        )
    lines: list[str] = []
    from io import StringIO

    stream = StringIO()
    writer = csv.DictWriter(stream, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(manifest_rows)
    lines.append(stream.getvalue())
    path.parent.mkdir(parents=True, exist_ok=True)

    def write_entry(handle: ZipFile, name: str, data: bytes) -> None:
        info = ZipInfo(name, date_time=(2026, 7, 10, 0, 0, 0))
        info.compress_type = ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        handle.writestr(info, data, compress_type=ZIP_DEFLATED, compresslevel=9)

    with ZipFile(path, "w", compression=ZIP_DEFLATED, compresslevel=9) as handle:
        write_entry(handle, "manifest.csv", "".join(lines).encode("utf-8"))
        for item in controls:
            control_path = Path(str(item["path"]))
            write_entry(handle, control_path.name, control_path.read_bytes())


def _run_controls(
    controls: list[dict[str, object]],
    targets: dict[str, list[str]],
    debug_root: Path,
) -> list[dict[str, object]]:
    member_rows: list[dict[str, object]] = []
    for item in controls:
        asset = str(item["asset"])
        kind = str(item["kind"])
        start = int(item["start"])
        rows = int(item["rows"])
        path = Path(str(item["path"]))
        world_label = f"null_{kind}_{asset.lower()}_{start}_{start + rows}"
        run_dir = _run_mini(path, debug_root / world_label, world_label)
        episodes = _load_csv(run_dir / "episodes.csv")
        world = {
            "asset": asset,
            "window_start": start,
            "window_end": start + rows,
            "world_label": world_label,
            "source_path": _relative(Path(str(item["source"]))),
            "data_path": _relative(path),
            "world_events": len(episodes),
            "control_kind": kind,
            "seed": item["seed"],
        }
        member_rows.extend(_build_member_rows(world, episodes, targets))
    return member_rows


def _load_real_summaries() -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for path in REAL_SUMMARIES:
        for row in _load_csv(path):
            rows[str(row["role_family"])] = row
    return rows


def _load_real_worlds() -> dict[tuple[str, int, str], dict[str, str]]:
    rows: dict[tuple[str, int, str], dict[str, str]] = {}
    for path in REAL_WORLDS:
        for row in _load_csv(path):
            key = (str(row["asset"]), int(row["window_start"]), str(row["role_family"]))
            rows[key] = row
    return rows


def _build_paired_rows(
    real_worlds: dict[tuple[str, int, str], dict[str, str]],
    control_worlds: list[dict[str, object]],
) -> list[dict[str, object]]:
    metrics = (
        "member_coverage",
        "family_event_share",
        "phase_complete_ratio",
        "mean_afterimage_delta",
        "mean_temporal_delta",
    )
    rows: list[dict[str, object]] = []
    for control in control_worlds:
        key = (
            str(control["asset"]),
            int(control["window_start"]),
            str(control["role_family"]),
        )
        real = real_worlds.get(key)
        if real is None:
            raise ValueError(f"Reales Paarfenster fehlt: {key}")
        row: dict[str, object] = {
            "asset": key[0],
            "window_start": key[1],
            "role_family": key[2],
            "control_kind": control["control_kind"],
        }
        for metric in metrics:
            real_value = _safe_float(real.get(metric))
            control_value = _safe_float(control.get(metric))
            row[f"real_{metric}"] = real_value
            row[f"control_{metric}"] = control_value
            row[f"real_minus_control_{metric}"] = real_value - control_value
        row["real_joint_coverage_event_advantage"] = int(
            _safe_float(row["real_minus_control_member_coverage"]) > 0.0
            and _safe_float(row["real_minus_control_family_event_share"]) > 0.0
        )
        rows.append(row)
    rows.sort(
        key=lambda row: (
            str(row["role_family"]),
            str(row["control_kind"]),
            str(row["asset"]),
            int(row["window_start"]),
        )
    )
    return rows


def _comparison_sign_counts(
    comparisons: list[dict[str, object]],
    paired_rows: list[dict[str, object]],
) -> None:
    for comparison in comparisons:
        role_family = str(comparison["role_family"])
        for kind in ("shuffle", "random_sign"):
            rows = [
                row
                for row in paired_rows
                if row["role_family"] == role_family and row["control_kind"] == kind
            ]
            for metric in ("member_coverage", "family_event_share"):
                values = [_safe_float(row[f"real_minus_control_{metric}"]) for row in rows]
                comparison[f"paired_{kind}_{metric}_real_wins"] = sum(value > 0.0 for value in values)
                comparison[f"paired_{kind}_{metric}_ties"] = sum(abs(value) <= 1e-12 for value in values)
                comparison[f"paired_{kind}_{metric}_control_wins"] = sum(value < 0.0 for value in values)
            comparison[f"paired_{kind}_joint_real_advantage"] = sum(
                int(row["real_joint_coverage_event_advantage"]) for row in rows
            )


def _mean_metric(rows: list[dict[str, object]], field: str) -> float:
    return mean(_safe_float(row.get(field)) for row in rows) if rows else 0.0


def _build_comparison(
    real: dict[str, dict[str, str]],
    controls: dict[str, dict[str, dict[str, object]]],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for role_family in sorted(real):
        real_row = real[role_family]
        shuffle = controls["shuffle"][role_family]
        random_sign = controls["random_sign"][role_family]
        row: dict[str, object] = {
            "role_family": role_family,
            "target_members": real_row["target_members"],
        }
        for metric in METRICS:
            real_value = _safe_float(real_row.get(metric))
            shuffle_value = _safe_float(shuffle.get(metric))
            random_value = _safe_float(random_sign.get(metric))
            control_mean = mean((shuffle_value, random_value))
            row[f"real_{metric}"] = real_value
            row[f"shuffle_{metric}"] = shuffle_value
            row[f"random_sign_{metric}"] = random_value
            row[f"real_minus_control_mean_{metric}"] = real_value - control_mean
        row["real_minus_strongest_control_continuity"] = _safe_float(
            real_row.get("family_continuity_score")
        ) - max(
            _safe_float(shuffle.get("family_continuity_score")),
            _safe_float(random_sign.get("family_continuity_score")),
        )
        rows.append(row)
    return rows


def _fmt(value: object, digits: int = 3) -> str:
    return f"{_safe_float(value):.{digits}f}"


def _write_markdown(
    path: Path,
    comparisons: list[dict[str, object]],
    control_archive: Path,
) -> None:
    continuity_wins = sum(
        1 for row in comparisons if _safe_float(row["real_minus_strongest_control_continuity"]) > 0.0
    )
    event_share_wins = sum(
        1
        for row in comparisons
        if _safe_float(row["real_minus_control_mean_mean_family_event_share"]) > 0.0
    )
    coverage_wins = sum(
        1
        for row in comparisons
        if _safe_float(row["real_minus_control_mean_mean_member_coverage"]) > 0.0
    )
    mean_continuity = {
        "real": _mean_metric(comparisons, "real_family_continuity_score"),
        "shuffle": _mean_metric(comparisons, "shuffle_family_continuity_score"),
        "random_sign": _mean_metric(comparisons, "random_sign_family_continuity_score"),
    }
    mean_event_share = {
        "real": _mean_metric(comparisons, "real_mean_family_event_share"),
        "shuffle": _mean_metric(comparisons, "shuffle_mean_family_event_share"),
        "random_sign": _mean_metric(comparisons, "random_sign_mean_family_event_share"),
    }
    continuity_above_both = [
        str(row["role_family"])
        for row in comparisons
        if _safe_float(row["real_minus_strongest_control_continuity"]) > 0.0
    ]
    event_above_both = [
        str(row["role_family"])
        for row in comparisons
        if _safe_float(row["real_mean_family_event_share"])
        > max(
            _safe_float(row["shuffle_mean_family_event_share"]),
            _safe_float(row["random_sign_mean_family_event_share"]),
        )
    ]
    coverage_above_both = [
        str(row["role_family"])
        for row in comparisons
        if _safe_float(row["real_mean_member_coverage"])
        > max(
            _safe_float(row["shuffle_mean_member_coverage"]),
            _safe_float(row["random_sign_mean_member_coverage"]),
        )
    ]
    joint_above_both = sorted(
        set(continuity_above_both) & set(event_above_both) & set(coverage_above_both)
    )
    largest_control_advantage = min(
        comparisons,
        key=lambda row: _safe_float(row["real_minus_strongest_control_continuity"]),
    )
    lines = [
        "# 2073 - Rollenfamilien im Real-/Nullwelt-Kontrast",
        "",
        "## Zweck",
        "",
        "Dieser Versuch prüft alle acht in 2066 gebildeten Rollenfamilien gegen zeitstrukturzerstörte Kontrollwelten auf unveränderter Symbolbasis.",
        "",
        "Die Frage ist nicht, ob Nullwelten überhaupt Ordnung bilden. Frühere Befunde zeigen, dass sie das können. Geprüft wird enger, ob die in realen Folgewelten beobachtete Familienanschlussfähigkeit gegenüber zwei assetnahen Kontrollformen einen kontinuierlichen Vorsprung trägt.",
        "",
        "## Methode",
        "",
        "- reale Referenz: die 15 Folgefenster aus 2070 und 2072",
        "- Kontrollen: je Realfenster eine Shuffle-Order- und eine Random-Sign-Welt",
        "- Kontrollläufe: `30` mit jeweils `1000` Beobachtungen",
        "- Assets: `BTC;DOGE;PAXG;SOL;XRP`",
        "- pro Kontrollwelt eine frische episodische Memory",
        "- Wahrnehmungsmodus: `world_relative`",
        f"- Kontrollweltarchiv: `{_relative(control_archive)}`",
        "- Debugdaten und entpackte Kontrollwelten bleiben lokal",
        "- keine neue Familienklasse, keine Handlung, kein Gate und keine Richtung",
        "",
        "Shuffle erhält die lokalen Kerzenformen, zerstört aber ihre Reihenfolge. Random Sign erhält die Größenordnung der Körper und Dochte, verändert jedoch die Richtung der Körper. Beide Kontrollen bleiben damit asset- und längennah, ohne die reale zeitliche Folge zu bewahren.",
        "",
        "## Kontinuierlicher Familienvergleich",
        "",
        "Positive Differenzen bedeuten einen Realweltvorsprung. Negative Differenzen bedeuten, dass die gemittelte oder stärkste Kontrolle mindestens gleich hoch liegt. Es wird kein Schwellenwert zur festen Klassifikation verwendet.",
        "",
        "| Familie | Kontinuität real/shuffle/random | Real minus stärkste Kontrolle | Ereignisanteil real/shuffle/random | Abdeckung real/shuffle/random | Drift real/shuffle/random |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for row in comparisons:
        lines.append(
            f"| `{row['role_family']}` | "
            f"{_fmt(row['real_family_continuity_score'])}/{_fmt(row['shuffle_family_continuity_score'])}/{_fmt(row['random_sign_family_continuity_score'])} | "
            f"{_fmt(row['real_minus_strongest_control_continuity'])} | "
            f"{_fmt(row['real_mean_family_event_share'], 4)}/{_fmt(row['shuffle_mean_family_event_share'], 4)}/{_fmt(row['random_sign_mean_family_event_share'], 4)} | "
            f"{_fmt(row['real_mean_member_coverage'])}/{_fmt(row['shuffle_mean_member_coverage'])}/{_fmt(row['random_sign_mean_member_coverage'])} | "
            f"{_fmt(row['real_member_distribution_drift'])}/{_fmt(row['shuffle_member_distribution_drift'])}/{_fmt(row['random_sign_member_distribution_drift'])} |"
        )
    lines.extend(
        [
            "",
            "## Paarvergleich Der 15 Ausgangsfenster",
            "",
            "Jede Zahl nennt die Anzahl der Realfenster, die ihre direkt abgeleitete Kontrolle auf derselben Achse übertrifft. `gemeinsam` verlangt im selben Fenster zugleich höhere Mitgliederabdeckung und höheren Familienereignisanteil.",
            "",
            "| Familie | Ereignisanteil real > shuffle/random | Abdeckung real > shuffle/random | gemeinsam real > shuffle/random |",
            "|---|---:|---:|---:|",
        ]
    )
    for row in comparisons:
        lines.append(
            f"| `{row['role_family']}` | "
            f"{row['paired_shuffle_family_event_share_real_wins']}/15 / {row['paired_random_sign_family_event_share_real_wins']}/15 | "
            f"{row['paired_shuffle_member_coverage_real_wins']}/15 / {row['paired_random_sign_member_coverage_real_wins']}/15 | "
            f"{row['paired_shuffle_joint_real_advantage']}/15 / {row['paired_random_sign_joint_real_advantage']}/15 |"
        )
    lines.extend(
        [
            "",
            "## Gesamtprofil",
            "",
            f"- mittlere Familienkontinuität real/shuffle/random: `{_fmt(mean_continuity['real'])}` / `{_fmt(mean_continuity['shuffle'])}` / `{_fmt(mean_continuity['random_sign'])}`",
            f"- mittlerer Familienereignisanteil real/shuffle/random: `{_fmt(mean_event_share['real'], 4)}` / `{_fmt(mean_event_share['shuffle'], 4)}` / `{_fmt(mean_event_share['random_sign'], 4)}`",
            f"- Realwelt übertrifft die jeweils stärkere Kontrolle bei Kontinuität: `{continuity_wins}/8` Familien",
            f"- Realwelt liegt über dem Kontrollmittel bei Ereignisanteil: `{event_share_wins}/8` Familien",
            f"- Realwelt liegt über dem Kontrollmittel bei Mitgliederabdeckung: `{coverage_wins}/8` Familien",
            "",
            "## Befund",
            "",
            f"- Kontinuität über beiden Kontrollen: `{';'.join(continuity_above_both) or '-'}`",
            f"- Familienereignisanteil über beiden Kontrollen: `{';'.join(event_above_both) or '-'}`",
            f"- Mitgliederabdeckung über beiden Kontrollen: `{';'.join(coverage_above_both) or '-'}`",
            f"- gemeinsamer Vorsprung auf allen drei Achsen: `{';'.join(joint_above_both) or '-'}`",
            f"- stärkster Kontrollvorsprung bei Kontinuität: `{largest_control_advantage['role_family']}` mit Real minus stärkste Kontrolle `{_fmt(largest_control_advantage['real_minus_strongest_control_continuity'])}`",
            "",
            "Die reale Zeitfolge erzeugt damit keinen breiten Kontinuitätsvorsprung der acht Familien. Shuffle liegt im Gesamtmittel höher, Random Sign etwa auf Realniveau. Die Anschlussfähigkeit aus 2070 und 2072 ist daher zunächst als feldinterne Wiederkehr zu lesen, nicht als ausreichender Nachweis realweltspezifischer Bedeutung.",
            "",
            "Nur Familien, die mehrere Achsen und die direkten Paarfenster gemeinsam tragen, bleiben stärkere Kandidaten für eine spätere Weltbindungsprüfung. Auch bei ihnen ist die Nullweltnähe Teil des Befunds und darf nicht ausgeblendet werden.",
            "",
            "## Lesung",
            "",
            "Der Vergleich liest keine Familie als wahr oder falsch. Entscheidend ist das gemeinsame Profil: Eine Familie ist als realweltlich getragener Bedeutungsraum erst stärker begründet, wenn ihre Präsenz, Mitgliederabdeckung, Ereignistragung und innere Verteilung gegenüber beiden Kontrollen gemeinsam Abstand gewinnen.",
            "",
            "Wo Kontrollen gleichauf oder stärker liegen, bleibt die Familie eine feldinterne Ordnungsform ohne ausreichenden Nachweis spezifischer Weltbindung. Das ist kein Fehler des Feldes, aber eine Grenze der Bedeutungsbehauptung.",
            "",
            "## Grenze",
            "",
            "Der Versuch verwendet dieselben 15 kurzen Folgefenster wie 2070 und 2072. Er prüft Zeitordnung und Richtungsstruktur, aber noch keine völlig fremden Assets, längeren Horizonte oder sensormodal anderen Welten. Die Differenzen sind Forschungsmaße, keine Handlungswerte und keine feste Semantik der einzelnen `dio_*`-Zeichen.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Vergleicht Rollenfamilien in Real- und Nullwelten.")
    parser.add_argument("--memory", default=str(DEFAULT_MEMORY))
    parser.add_argument("--cohesion-detail", default=str(DEFAULT_COHESION))
    parser.add_argument("--real-archive", default=str(DEFAULT_REAL_ARCHIVE))
    parser.add_argument("--real-dir", default=str(DEFAULT_REAL_DIR))
    parser.add_argument("--control-dir", default=str(DEFAULT_CONTROL_DIR))
    parser.add_argument("--control-archive", default=str(DEFAULT_CONTROL_ARCHIVE))
    parser.add_argument("--debug-root", default=str(DEFAULT_DEBUG_ROOT))
    parser.add_argument("--out-prefix", default=str(DEFAULT_OUT_PREFIX))
    args = parser.parse_args()

    memory = _resolve(args.memory)
    cohesion = _resolve(args.cohesion_detail)
    real_archive = _resolve(args.real_archive)
    real_dir = _resolve(args.real_dir)
    control_dir = _resolve(args.control_dir)
    control_archive = _resolve(args.control_archive)
    debug_root = _resolve(args.debug_root)
    out_prefix = _resolve(args.out_prefix)

    targets = _load_targets(
        memory,
        ["rf_05", "rf_06", "rf_07", "rf_08", "rf_10", "rf_13", "rf_17", "rf_21"],
    )
    source_counts = _load_source_member_counts(cohesion, targets)
    real_paths = _ensure_real_slices(real_archive, real_dir)
    controls = _build_controls(real_paths, control_dir)
    _write_control_archive(control_archive, controls)
    member_rows = _run_controls(controls, targets, debug_root)

    summaries_by_kind: dict[str, list[dict[str, object]]] = {}
    all_world_rows: list[dict[str, object]] = []
    all_summary_rows: list[dict[str, object]] = []
    for kind in ("shuffle", "random_sign"):
        kind_members = [row for row in member_rows if str(row["control_kind"]) == kind]
        world_rows = _build_world_family_rows(kind_members)
        for row in world_rows:
            row["control_kind"] = kind
        summary = _build_family_summary(world_rows, kind_members, targets, source_counts)
        for row in summary:
            row["control_kind"] = kind
        summaries_by_kind[kind] = summary
        all_world_rows.extend(world_rows)
        all_summary_rows.extend(summary)

    controls_by_kind = {
        kind: {str(row["role_family"]): row for row in rows}
        for kind, rows in summaries_by_kind.items()
    }
    comparisons = _build_comparison(_load_real_summaries(), controls_by_kind)
    paired_rows = _build_paired_rows(_load_real_worlds(), all_world_rows)
    _comparison_sign_counts(comparisons, paired_rows)

    _write_csv(out_prefix.with_suffix(".controls.summary.csv"), all_summary_rows)
    _write_csv(out_prefix.with_suffix(".controls.worlds.csv"), all_world_rows)
    _write_csv(out_prefix.with_suffix(".paired.csv"), paired_rows)
    _write_csv(out_prefix.with_suffix(".comparison.csv"), comparisons)
    _write_markdown(out_prefix.with_suffix(".md"), comparisons, control_archive)

    print(f"controls={len(controls)}")
    print(f"member_rows={len(member_rows)}")
    print(f"world_rows={len(all_world_rows)}")
    print(f"comparison_rows={len(comparisons)}")
    print(f"wrote={out_prefix.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
