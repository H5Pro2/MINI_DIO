# Real-Sleep-Real Passive Reorganisation

Stand: 2026-07-06 13:17:44

## Zweck

Diese Kette prueft, was sich zwischen zwei Real-Welt-Beruehrungen veraendert,
wenn dazwischen eine entkoppelte MCM-Schlafdiagnose liegt. Real-B kann dieselbe oder eine andere Welt sein.

Wichtig: In diesem Lauf schreibt die Schlafphase eine passive Reorganisationsspur.
Diese Spur markiert nur beruehrte bestehende Rollen; sie erzeugt keine neue Weltbedeutung,
keine Richtung, kein Gate und keine Handlung.

## Kette

- Real A Welt: `data\scan_synth-rand-kipp-start0_start250_size1700.csv`
- Real B Welt: `data\scan_synth-rand-kipp-start0_start250_size1700.csv`
- gleiche Welt: `True`
- Real A Memory: `memory\real_sleep_real\synth_rand_kipp_start250_size1700_phase_afterimage_probe\memory_A_real_run.json`
- Sleep Diagnose: `debug\real_sleep_real\synth_rand_kipp_start250_size1700_phase_afterimage_probe\sleep`
- Memory nach Sleep: `memory\real_sleep_real\synth_rand_kipp_start250_size1700_phase_afterimage_probe\memory_A_after_sleep.json`
- Real B Memory: `memory\real_sleep_real\synth_rand_kipp_start250_size1700_phase_afterimage_probe\memory_B_real_run_after_sleep.json`

## Real A -> Real B

- Episoden: `1694.0` -> `1694.0`
- Unique Syntax: `149.0` -> `149.0`
- geschriebene Feldepisoden: `1.0` -> `1.0`
- MCM-Tragqualitaet: `0.568415` -> `0.568644`
- MCM-Rekopplung: `0.730088` -> `0.729841`
- MCM-Sinneskopplung: `0.884247` -> `0.884022`
- Top-Syntax-Ueberlappung: `1.0`
- Top-Familien-Ueberlappung: `1.0`

## Sleep Diagnose

- Sleep Ticks: `300`
- Rollen im Sleep-Pool: `1`
- aktive Rollensets: `1`
- Sleep Unique Syntax: `1`
- mittlerer Nachhall: `0.030987`
- passive Sleep-Memory geschrieben: `True`
- Sleep-Rollen-Reaktivierung: `1` / `1`
- Sleep-Kombinationen voll reaktiviert: `0` / `0`
- Sleep-Kombinationen teilweise reaktiviert: `0` / `0`
- Sleep-Follow-up-Zustand: `sleep_roles_fully_reactivated`

Sleep-Zustaende:

- `sleep_rekopplung`: `300`

Sleep-Rollen im Real-B-Follow-up:

- `dio_mcm_episode_0d9qets`: `sleep_role_reactivated_in_follow_world` (`1` -> `2`)

Sleep-Kombinationen im Real-B-Follow-up:


## Bewertung

Diese Stufe ist noch kein Nachweis fuer veraendertes Weltverhalten durch Schlaf.
Sie zeigt aber, dass Sleep bestehende Rollen passiv markieren kann, ohne Welt-Symbole neu zu erfinden.
Damit ist der naechste Schritt sauber messbar: eine spaetere Leseschicht darf pruefen,
ob diese passive Reorganisationsspur bei erneutem Weltkontakt wieder auftaucht oder neutral bleibt.
