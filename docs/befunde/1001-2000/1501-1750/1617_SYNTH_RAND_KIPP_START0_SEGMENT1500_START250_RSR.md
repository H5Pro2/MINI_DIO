# Real-Sleep-Real Passive Reorganisation

Stand: 2026-07-06 11:26:22

## Zweck

Diese Kette prueft, was sich zwischen zwei Real-Welt-Beruehrungen veraendert,
wenn dazwischen eine entkoppelte MCM-Schlafdiagnose liegt. Real-B kann dieselbe oder eine andere Welt sein.

Wichtig: In diesem Lauf schreibt die Schlafphase eine passive Reorganisationsspur.
Diese Spur markiert nur beruehrte bestehende Rollen; sie erzeugt keine neue Weltbedeutung,
keine Richtung, kein Gate und keine Handlung.

## Kette

- Real A Welt: `data\scan_synth-rand-kipp-start0_start250_size1500.csv`
- Real B Welt: `data\scan_synth-rand-kipp-start0_start250_size1500.csv`
- gleiche Welt: `True`
- Real A Memory: `memory\real_sleep_real\synth_rand_kipp_start0_segment1500_start250_role5_repro\memory_A_real_run.json`
- Sleep Diagnose: `debug\real_sleep_real\synth_rand_kipp_start0_segment1500_start250_role5_repro\sleep`
- Memory nach Sleep: `memory\real_sleep_real\synth_rand_kipp_start0_segment1500_start250_role5_repro\memory_A_after_sleep.json`
- Real B Memory: `memory\real_sleep_real\synth_rand_kipp_start0_segment1500_start250_role5_repro\memory_B_real_run_after_sleep.json`

## Real A -> Real B

- Episoden: `1494.0` -> `1494.0`
- Unique Syntax: `108.0` -> `108.0`
- geschriebene Feldepisoden: `5.0` -> `5.0`
- MCM-Tragqualitaet: `0.581598` -> `0.581675`
- MCM-Rekopplung: `0.736448` -> `0.736375`
- MCM-Sinneskopplung: `0.890758` -> `0.890687`
- Top-Syntax-Ueberlappung: `1.0`
- Top-Familien-Ueberlappung: `1.0`

## Sleep Diagnose

- Sleep Ticks: `300`
- Rollen im Sleep-Pool: `5`
- aktive Rollensets: `10`
- Sleep Unique Syntax: `1`
- mittlerer Nachhall: `0.024823`
- passive Sleep-Memory geschrieben: `True`
- Sleep-Rollen-Reaktivierung: `5` / `5`
- Sleep-Kombinationen voll reaktiviert: `10` / `10`
- Sleep-Kombinationen teilweise reaktiviert: `0` / `10`
- Sleep-Follow-up-Zustand: `sleep_roles_fully_reactivated`

Sleep-Zustaende:

- `sleep_rekopplung`: `300`

Sleep-Rollen im Real-B-Follow-up:

- `dio_mcm_episode_0mji3u6`: `sleep_role_reactivated_in_follow_world` (`1` -> `2`)
- `dio_mcm_episode_1k5qdaq`: `sleep_role_reactivated_in_follow_world` (`1` -> `2`)
- `dio_mcm_episode_1bdmoa8`: `sleep_role_reactivated_in_follow_world` (`1` -> `2`)
- `dio_mcm_episode_0qvqqtg`: `sleep_role_reactivated_in_follow_world` (`1` -> `2`)
- `dio_mcm_episode_15uimof`: `sleep_role_reactivated_in_follow_world` (`1` -> `2`)

Sleep-Kombinationen im Real-B-Follow-up:

- `dio_mcm_episode_0mji3u6|dio_mcm_episode_0qvqqtg`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)
- `dio_mcm_episode_0mji3u6|dio_mcm_episode_1bdmoa8`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)
- `dio_mcm_episode_0mji3u6|dio_mcm_episode_1k5qdaq`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)
- `dio_mcm_episode_0qvqqtg|dio_mcm_episode_1bdmoa8`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)
- `dio_mcm_episode_0qvqqtg|dio_mcm_episode_1k5qdaq`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)
- `dio_mcm_episode_1bdmoa8|dio_mcm_episode_1k5qdaq`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)
- `dio_mcm_episode_0mji3u6|dio_mcm_episode_15uimof`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)
- `dio_mcm_episode_0qvqqtg|dio_mcm_episode_15uimof`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)
- `dio_mcm_episode_15uimof|dio_mcm_episode_1bdmoa8`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)
- `dio_mcm_episode_15uimof|dio_mcm_episode_1k5qdaq`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)

## Bewertung

Diese Stufe ist noch kein Nachweis fuer veraendertes Weltverhalten durch Schlaf.
Sie zeigt aber, dass Sleep bestehende Rollen passiv markieren kann, ohne Welt-Symbole neu zu erfinden.
Damit ist der naechste Schritt sauber messbar: eine spaetere Leseschicht darf pruefen,
ob diese passive Reorganisationsspur bei erneutem Weltkontakt wieder auftaucht oder neutral bleibt.
