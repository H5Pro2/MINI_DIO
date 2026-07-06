# Real-Sleep-Real Passive Reorganisation

Stand: 2026-07-06 20:51:43

## Zweck

Diese Kette prueft, was sich zwischen zwei Real-Welt-Beruehrungen veraendert,
wenn dazwischen eine entkoppelte MCM-Schlafdiagnose liegt. Real-B kann dieselbe oder eine andere Welt sein.

Wichtig: In diesem Lauf schreibt die Schlafphase eine passive Reorganisationsspur.
Diese Spur markiert nur beruehrte bestehende Rollen; sie erzeugt keine neue Weltbedeutung,
keine Richtung, kein Gate und keine Handlung.

## Kette

- Real A Welt: `data\kontrolliert_2023_negative_stress_10k_5m_SOLUSDT.csv`
- Real B Welt: `data\kontrolliert_2023_negative_stress_10k_5m_SOLUSDT.csv`
- gleiche Welt: `True`
- Real A Memory: `memory\real_sleep_real\real_negative_stress_2023_10k_role_split_calibrated\memory_A_real_run.json`
- Sleep Diagnose: `debug\real_sleep_real\real_negative_stress_2023_10k_role_split_calibrated\sleep`
- Memory nach Sleep: `memory\real_sleep_real\real_negative_stress_2023_10k_role_split_calibrated\memory_A_after_sleep.json`
- Real B Memory: `memory\real_sleep_real\real_negative_stress_2023_10k_role_split_calibrated\memory_B_real_run_after_sleep.json`

## Real A -> Real B

- Episoden: `9994.0` -> `9994.0`
- Unique Syntax: `789.0` -> `789.0`
- geschriebene Feldepisoden: `3540.0` -> `3543.0`
- MCM-Tragqualitaet: `0.530401` -> `0.530911`
- MCM-Rekopplung: `0.700974` -> `0.700462`
- MCM-Sinneskopplung: `0.832592` -> `0.832108`
- Top-Syntax-Ueberlappung: `1.0`
- Top-Familien-Ueberlappung: `1.0`

## Sleep Diagnose

- Sleep Ticks: `300`
- Rollen im Sleep-Pool: `24`
- aktive Rollensets: `5`
- Sleep Unique Syntax: `1`
- mittlerer Nachhall: `0.02766`
- passive Sleep-Memory geschrieben: `True`
- Sleep-Rollen-Reaktivierung: `4` / `4`
- Sleep-Kombinationen voll reaktiviert: `6` / `6`
- Sleep-Kombinationen teilweise reaktiviert: `0` / `6`
- Sleep-Follow-up-Zustand: `sleep_roles_fully_reactivated`

Sleep-Zustaende:

- `sleep_rekopplung`: `300`

Sleep-Rollen im Real-B-Follow-up:

- `dio_mcm_episode_1t06mit`: `sleep_role_reactivated_in_follow_world` (`286` -> `572`)
- `dio_mcm_episode_016p330`: `sleep_role_reactivated_in_follow_world` (`156` -> `311`)
- `dio_mcm_episode_02ktejt`: `sleep_role_reactivated_in_follow_world` (`128` -> `258`)
- `dio_mcm_episode_1sq70tu`: `sleep_role_reactivated_in_follow_world` (`136` -> `270`)

Sleep-Kombinationen im Real-B-Follow-up:

- `dio_mcm_episode_016p330|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[155, 286]`)
- `dio_mcm_episode_016p330|dio_mcm_episode_02ktejt`: `sleep_combination_fully_reactivated` (delta `[155, 130]`)
- `dio_mcm_episode_02ktejt|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[130, 286]`)
- `dio_mcm_episode_016p330|dio_mcm_episode_1sq70tu`: `sleep_combination_fully_reactivated` (delta `[155, 134]`)
- `dio_mcm_episode_1sq70tu|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[134, 286]`)
- `dio_mcm_episode_02ktejt|dio_mcm_episode_1sq70tu`: `sleep_combination_fully_reactivated` (delta `[130, 134]`)

## Bewertung

Diese Stufe ist noch kein Nachweis fuer veraendertes Weltverhalten durch Schlaf.
Sie zeigt aber, dass Sleep bestehende Rollen passiv markieren kann, ohne Welt-Symbole neu zu erfinden.
Damit ist der naechste Schritt sauber messbar: eine spaetere Leseschicht darf pruefen,
ob diese passive Reorganisationsspur bei erneutem Weltkontakt wieder auftaucht oder neutral bleibt.

## Wie es weitergeht

Als naechstes wird die passive Sleep-Reorganisationsspur gegen weitere Welten geprueft.
Dann wird sichtbar, ob sie nur eine lokale Markierung bleibt oder als wiederkehrende Innenfeldspur tragfaehig ist.
