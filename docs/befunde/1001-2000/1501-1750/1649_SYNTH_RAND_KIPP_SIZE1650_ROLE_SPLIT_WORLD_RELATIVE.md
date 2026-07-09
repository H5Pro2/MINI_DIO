# Real-Sleep-Real Passive Reorganisation

Stand: 2026-07-06 17:26:33

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
- Real A Memory: `memory\real_sleep_real\synth_rand_kipp_start250_size1650_role_split_world_relative\memory_A_real_run.json`
- Sleep Diagnose: `debug\real_sleep_real\synth_rand_kipp_start250_size1650_role_split_world_relative\sleep`
- Memory nach Sleep: `memory\real_sleep_real\synth_rand_kipp_start250_size1650_role_split_world_relative\memory_A_after_sleep.json`
- Real B Memory: `memory\real_sleep_real\synth_rand_kipp_start250_size1650_role_split_world_relative\memory_B_real_run_after_sleep.json`

## Real A -> Real B

- Episoden: `1644.0` -> `1644.0`
- Unique Syntax: `100.0` -> `100.0`
- geschriebene Feldepisoden: `258.0` -> `258.0`
- MCM-Tragqualitaet: `0.578412` -> `0.578558`
- MCM-Rekopplung: `0.733569` -> `0.733423`
- MCM-Sinneskopplung: `0.884737` -> `0.884599`
- Top-Syntax-Ueberlappung: `1.0`
- Top-Familien-Ueberlappung: `1.0`

## Sleep Diagnose

- Sleep Ticks: `300`
- Rollen im Sleep-Pool: `24`
- aktive Rollensets: `2`
- Sleep Unique Syntax: `1`
- mittlerer Nachhall: `0.02741`
- passive Sleep-Memory geschrieben: `True`
- Sleep-Rollen-Reaktivierung: `4` / `4`
- Sleep-Kombinationen voll reaktiviert: `6` / `6`
- Sleep-Kombinationen teilweise reaktiviert: `0` / `6`
- Sleep-Follow-up-Zustand: `sleep_roles_fully_reactivated`

Sleep-Zustaende:

- `sleep_rekopplung`: `300`

Sleep-Rollen im Real-B-Follow-up:

- `dio_mcm_episode_016p330`: `sleep_role_reactivated_in_follow_world` (`28` -> `56`)
- `dio_mcm_episode_1rx09kx`: `sleep_role_reactivated_in_follow_world` (`19` -> `38`)
- `dio_mcm_episode_1rn7x38`: `sleep_role_reactivated_in_follow_world` (`14` -> `28`)
- `dio_mcm_episode_18sa46n`: `sleep_role_reactivated_in_follow_world` (`16` -> `31`)

Sleep-Kombinationen im Real-B-Follow-up:

- `dio_mcm_episode_016p330|dio_mcm_episode_18sa46n`: `sleep_combination_fully_reactivated` (delta `[28, 15]`)
- `dio_mcm_episode_016p330|dio_mcm_episode_1rn7x38`: `sleep_combination_fully_reactivated` (delta `[28, 14]`)
- `dio_mcm_episode_016p330|dio_mcm_episode_1rx09kx`: `sleep_combination_fully_reactivated` (delta `[28, 19]`)
- `dio_mcm_episode_18sa46n|dio_mcm_episode_1rn7x38`: `sleep_combination_fully_reactivated` (delta `[15, 14]`)
- `dio_mcm_episode_18sa46n|dio_mcm_episode_1rx09kx`: `sleep_combination_fully_reactivated` (delta `[15, 19]`)
- `dio_mcm_episode_1rn7x38|dio_mcm_episode_1rx09kx`: `sleep_combination_fully_reactivated` (delta `[14, 19]`)

## Bewertung

Diese Stufe ist noch kein Nachweis fuer veraendertes Weltverhalten durch Schlaf.
Sie zeigt aber, dass Sleep bestehende Rollen passiv markieren kann, ohne Welt-Symbole neu zu erfinden.
Damit ist der naechste Schritt sauber messbar: eine spaetere Leseschicht darf pruefen,
ob diese passive Reorganisationsspur bei erneutem Weltkontakt wieder auftaucht oder neutral bleibt.

## Wie es weitergeht

Als naechstes wird die passive Sleep-Reorganisationsspur gegen weitere Welten geprueft.
Dann wird sichtbar, ob sie nur eine lokale Markierung bleibt oder als wiederkehrende Innenfeldspur tragfaehig ist.
