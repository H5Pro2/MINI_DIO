# Real-Sleep-Real Passive Reorganisation

Stand: 2026-07-06 16:22:05

## Zweck

Diese Kette prueft, was sich zwischen zwei Real-Welt-Beruehrungen veraendert,
wenn dazwischen eine entkoppelte MCM-Schlafdiagnose liegt. Real-B kann dieselbe oder eine andere Welt sein.

Wichtig: In diesem Lauf schreibt die Schlafphase eine passive Reorganisationsspur.
Diese Spur markiert nur beruehrte bestehende Rollen; sie erzeugt keine neue Weltbedeutung,
keine Richtung, kein Gate und keine Handlung.

## Kette

- Real A Welt: `data\scan_synth-rand-kipp-start0_start250_size1650.csv`
- Real B Welt: `data\scan_synth-rand-kipp-start0_start250_size1650.csv`
- gleiche Welt: `True`
- Real A Memory: `memory\real_sleep_real\synth_rand_kipp_start250_size1650_role_split_calibrated\memory_A_real_run.json`
- Sleep Diagnose: `debug\real_sleep_real\synth_rand_kipp_start250_size1650_role_split_calibrated\sleep`
- Memory nach Sleep: `memory\real_sleep_real\synth_rand_kipp_start250_size1650_role_split_calibrated\memory_A_after_sleep.json`
- Real B Memory: `memory\real_sleep_real\synth_rand_kipp_start250_size1650_role_split_calibrated\memory_B_real_run_after_sleep.json`

## Real A -> Real B

- Episoden: `1644.0` -> `1644.0`
- Unique Syntax: `186.0` -> `186.0`
- geschriebene Feldepisoden: `226.0` -> `228.0`
- MCM-Tragqualitaet: `0.558102` -> `0.558328`
- MCM-Rekopplung: `0.717178` -> `0.716934`
- MCM-Sinneskopplung: `0.855309` -> `0.855087`
- Top-Syntax-Ueberlappung: `1.0`
- Top-Familien-Ueberlappung: `1.0`

## Sleep Diagnose

- Sleep Ticks: `300`
- Rollen im Sleep-Pool: `24`
- aktive Rollensets: `18`
- Sleep Unique Syntax: `3`
- mittlerer Nachhall: `0.024675`
- passive Sleep-Memory geschrieben: `True`
- Sleep-Rollen-Reaktivierung: `9` / `9`
- Sleep-Kombinationen voll reaktiviert: `27` / `27`
- Sleep-Kombinationen teilweise reaktiviert: `0` / `27`
- Sleep-Follow-up-Zustand: `sleep_roles_fully_reactivated`

Sleep-Zustaende:

- `sleep_rekopplung`: `300`

Sleep-Rollen im Real-B-Follow-up:

- `dio_mcm_episode_0yh3tum`: `sleep_role_reactivated_in_follow_world` (`9` -> `18`)
- `dio_mcm_episode_1d7pbl5`: `sleep_role_reactivated_in_follow_world` (`9` -> `19`)
- `dio_mcm_episode_1gs06ww`: `sleep_role_reactivated_in_follow_world` (`8` -> `16`)
- `dio_mcm_episode_0y7485n`: `sleep_role_reactivated_in_follow_world` (`7` -> `14`)
- `dio_mcm_episode_02vsba2`: `sleep_role_reactivated_in_follow_world` (`6` -> `12`)
- `dio_mcm_episode_0uuhgpo`: `sleep_role_reactivated_in_follow_world` (`6` -> `12`)
- `dio_mcm_episode_1qc0pbr`: `sleep_role_reactivated_in_follow_world` (`5` -> `10`)
- `dio_mcm_episode_148dasc`: `sleep_role_reactivated_in_follow_world` (`5` -> `10`)
- `dio_mcm_episode_1cdvvlz`: `sleep_role_reactivated_in_follow_world` (`5` -> `9`)

Sleep-Kombinationen im Real-B-Follow-up:

- `dio_mcm_episode_0yh3tum|dio_mcm_episode_1d7pbl5`: `sleep_combination_fully_reactivated` (delta `[9, 10]`)
- `dio_mcm_episode_0yh3tum|dio_mcm_episode_1gs06ww`: `sleep_combination_fully_reactivated` (delta `[9, 8]`)
- `dio_mcm_episode_1d7pbl5|dio_mcm_episode_1gs06ww`: `sleep_combination_fully_reactivated` (delta `[10, 8]`)
- `dio_mcm_episode_0y7485n|dio_mcm_episode_0yh3tum`: `sleep_combination_fully_reactivated` (delta `[7, 9]`)
- `dio_mcm_episode_0y7485n|dio_mcm_episode_1d7pbl5`: `sleep_combination_fully_reactivated` (delta `[7, 10]`)
- `dio_mcm_episode_0y7485n|dio_mcm_episode_1gs06ww`: `sleep_combination_fully_reactivated` (delta `[7, 8]`)
- `dio_mcm_episode_02vsba2|dio_mcm_episode_0yh3tum`: `sleep_combination_fully_reactivated` (delta `[6, 9]`)
- `dio_mcm_episode_02vsba2|dio_mcm_episode_1d7pbl5`: `sleep_combination_fully_reactivated` (delta `[6, 10]`)
- `dio_mcm_episode_02vsba2|dio_mcm_episode_1gs06ww`: `sleep_combination_fully_reactivated` (delta `[6, 8]`)
- `dio_mcm_episode_02vsba2|dio_mcm_episode_0y7485n`: `sleep_combination_fully_reactivated` (delta `[6, 7]`)
- `dio_mcm_episode_0uuhgpo|dio_mcm_episode_0yh3tum`: `sleep_combination_fully_reactivated` (delta `[6, 9]`)
- `dio_mcm_episode_0uuhgpo|dio_mcm_episode_1d7pbl5`: `sleep_combination_fully_reactivated` (delta `[6, 10]`)

## Bewertung

Diese Stufe ist noch kein Nachweis fuer veraendertes Weltverhalten durch Schlaf.
Sie zeigt aber, dass Sleep bestehende Rollen passiv markieren kann, ohne Welt-Symbole neu zu erfinden.
Damit ist der naechste Schritt sauber messbar: eine spaetere Leseschicht darf pruefen,
ob diese passive Reorganisationsspur bei erneutem Weltkontakt wieder auftaucht oder neutral bleibt.
