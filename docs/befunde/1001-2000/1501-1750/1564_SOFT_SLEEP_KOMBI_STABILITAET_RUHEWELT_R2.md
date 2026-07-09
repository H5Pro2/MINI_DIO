# Real-Sleep-Real Passive Reorganisation

Stand: 2026-07-05 20:01:46

## Zweck

Diese Kette prueft, was sich zwischen zwei Real-Welt-Beruehrungen veraendert,
wenn dazwischen eine entkoppelte MCM-Schlafdiagnose liegt. Real-B kann dieselbe oder eine andere Welt sein.

Wichtig: In diesem Lauf schreibt die Schlafphase eine passive Reorganisationsspur.
Diese Spur markiert nur beruehrte bestehende Rollen; sie erzeugt keine neue Weltbedeutung,
keine Richtung, kein Gate und keine Handlung.

## Kette

- Real A Welt: `data\kontrolliert_sol_2024_5m_test1_2000_SOLUSDT.csv`
- Real B Welt: `data\kontrolliert_real_quiet_sol_2025_5m_2000.csv`
- gleiche Welt: `False`
- Real A Memory: `memory\real_sleep_real\sol2024_soft_sleep_combo_quiet2025_r2\memory_A_real_run.json`
- Sleep Diagnose: `debug\real_sleep_real\sol2024_soft_sleep_combo_quiet2025_r2\sleep`
- Memory nach Sleep: `memory\real_sleep_real\sol2024_soft_sleep_combo_quiet2025_r2\memory_A_after_sleep.json`
- Real B Memory: `memory\real_sleep_real\sol2024_soft_sleep_combo_quiet2025_r2\memory_B_real_run_after_sleep.json`

## Real A -> Real B

- Episoden: `1994.0` -> `1994.0`
- Unique Syntax: `351.0` -> `337.0`
- geschriebene Feldepisoden: `5.0` -> `3.0`
- MCM-Tragqualitaet: `0.509901` -> `0.510752`
- MCM-Rekopplung: `0.693318` -> `0.693279`
- MCM-Sinneskopplung: `0.83793` -> `0.83895`
- Top-Syntax-Ueberlappung: `0.777778`
- Top-Familien-Ueberlappung: `1.0`

## Sleep Diagnose

- Sleep Ticks: `300`
- Rollen im Sleep-Pool: `5`
- aktive Rollensets: `10`
- Sleep Unique Syntax: `1`
- mittlerer Nachhall: `0.024052`
- passive Sleep-Memory geschrieben: `True`
- Sleep-Rollen-Reaktivierung: `2` / `5`
- Sleep-Kombinationen voll reaktiviert: `1` / `10`
- Sleep-Kombinationen teilweise reaktiviert: `6` / `10`
- Sleep-Follow-up-Zustand: `sleep_roles_partly_reactivated`

Sleep-Zustaende:

- `sleep_rekopplung`: `300`

Sleep-Rollen im Real-B-Follow-up:

- `dio_mcm_episode_1k2bqha`: `sleep_role_reactivated_in_follow_world` (`1` -> `2`)
- `dio_mcm_episode_0e7qvj1`: `sleep_role_reactivated_in_follow_world` (`1` -> `2`)
- `dio_mcm_episode_1wra2fc`: `sleep_role_unchanged_in_follow_world` (`1` -> `1`)
- `dio_mcm_episode_0eghs1d`: `sleep_role_unchanged_in_follow_world` (`1` -> `1`)
- `dio_mcm_episode_0qrlave`: `sleep_role_unchanged_in_follow_world` (`1` -> `1`)

Sleep-Kombinationen im Real-B-Follow-up:

- `dio_mcm_episode_0e7qvj1|dio_mcm_episode_1k2bqha`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)
- `dio_mcm_episode_0e7qvj1|dio_mcm_episode_1wra2fc`: `sleep_combination_partly_reactivated` (delta `[1, 0]`)
- `dio_mcm_episode_1k2bqha|dio_mcm_episode_1wra2fc`: `sleep_combination_partly_reactivated` (delta `[1, 0]`)
- `dio_mcm_episode_0e7qvj1|dio_mcm_episode_0eghs1d`: `sleep_combination_partly_reactivated` (delta `[1, 0]`)
- `dio_mcm_episode_0eghs1d|dio_mcm_episode_1k2bqha`: `sleep_combination_partly_reactivated` (delta `[0, 1]`)
- `dio_mcm_episode_0eghs1d|dio_mcm_episode_1wra2fc`: `sleep_combination_not_reactivated` (delta `[0, 0]`)
- `dio_mcm_episode_0e7qvj1|dio_mcm_episode_0qrlave`: `sleep_combination_partly_reactivated` (delta `[1, 0]`)
- `dio_mcm_episode_0qrlave|dio_mcm_episode_1k2bqha`: `sleep_combination_partly_reactivated` (delta `[0, 1]`)
- `dio_mcm_episode_0qrlave|dio_mcm_episode_1wra2fc`: `sleep_combination_not_reactivated` (delta `[0, 0]`)
- `dio_mcm_episode_0eghs1d|dio_mcm_episode_0qrlave`: `sleep_combination_not_reactivated` (delta `[0, 0]`)

## Bewertung

Diese Stufe ist noch kein Nachweis fuer veraendertes Weltverhalten durch Schlaf.
Sie zeigt aber, dass Sleep bestehende Rollen passiv markieren kann, ohne Welt-Symbole neu zu erfinden.
Damit ist der naechste Schritt sauber messbar: eine spaetere Leseschicht darf pruefen,
ob diese passive Reorganisationsspur bei erneutem Weltkontakt wieder auftaucht oder neutral bleibt.

## Wie es weitergeht

Als naechstes wird die passive Sleep-Reorganisationsspur gegen weitere Welten geprueft.
Dann wird sichtbar, ob sie nur eine lokale Markierung bleibt oder als wiederkehrende Innenfeldspur tragfaehig ist.
