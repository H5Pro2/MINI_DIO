# Real-Sleep-Real Passive Reorganisation

Stand: 2026-07-06 20:52:43

## Zweck

Diese Kette prueft, was sich zwischen zwei Real-Welt-Beruehrungen veraendert,
wenn dazwischen eine entkoppelte MCM-Schlafdiagnose liegt. Real-B kann dieselbe oder eine andere Welt sein.

Wichtig: In diesem Lauf schreibt die Schlafphase eine passive Reorganisationsspur.
Diese Spur markiert nur beruehrte bestehende Rollen; sie erzeugt keine neue Weltbedeutung,
keine Richtung, kein Gate und keine Handlung.

## Kette

- Real A Welt: `data\kontrolliert_2023_positive_expansion_10k_5m_SOLUSDT.csv`
- Real B Welt: `data\kontrolliert_2023_positive_expansion_10k_5m_SOLUSDT.csv`
- gleiche Welt: `True`
- Real A Memory: `memory\real_sleep_real\real_positive_expansion_2023_10k_role_split_calibrated\memory_A_real_run.json`
- Sleep Diagnose: `debug\real_sleep_real\real_positive_expansion_2023_10k_role_split_calibrated\sleep`
- Memory nach Sleep: `memory\real_sleep_real\real_positive_expansion_2023_10k_role_split_calibrated\memory_A_after_sleep.json`
- Real B Memory: `memory\real_sleep_real\real_positive_expansion_2023_10k_role_split_calibrated\memory_B_real_run_after_sleep.json`

## Real A -> Real B

- Episoden: `9994.0` -> `9994.0`
- Unique Syntax: `801.0` -> `801.0`
- geschriebene Feldepisoden: `3614.0` -> `3614.0`
- MCM-Tragqualitaet: `0.529789` -> `0.530337`
- MCM-Rekopplung: `0.700854` -> `0.700304`
- MCM-Sinneskopplung: `0.833644` -> `0.833125`
- Top-Syntax-Ueberlappung: `1.0`
- Top-Familien-Ueberlappung: `1.0`

## Sleep Diagnose

- Sleep Ticks: `300`
- Rollen im Sleep-Pool: `24`
- aktive Rollensets: `5`
- Sleep Unique Syntax: `1`
- mittlerer Nachhall: `0.027334`
- passive Sleep-Memory geschrieben: `True`
- Sleep-Rollen-Reaktivierung: `6` / `6`
- Sleep-Kombinationen voll reaktiviert: `14` / `14`
- Sleep-Kombinationen teilweise reaktiviert: `0` / `14`
- Sleep-Follow-up-Zustand: `sleep_roles_fully_reactivated`

Sleep-Zustaende:

- `sleep_rekopplung`: `300`

Sleep-Rollen im Real-B-Follow-up:

- `dio_mcm_episode_1t06mit`: `sleep_role_reactivated_in_follow_world` (`240` -> `481`)
- `dio_mcm_episode_02ktejt`: `sleep_role_reactivated_in_follow_world` (`159` -> `318`)
- `dio_mcm_episode_016p330`: `sleep_role_reactivated_in_follow_world` (`166` -> `328`)
- `dio_mcm_episode_1sq70tu`: `sleep_role_reactivated_in_follow_world` (`127` -> `253`)
- `dio_mcm_episode_18sa46n`: `sleep_role_reactivated_in_follow_world` (`89` -> `179`)
- `dio_mcm_episode_00wphe1`: `sleep_role_reactivated_in_follow_world` (`81` -> `160`)

Sleep-Kombinationen im Real-B-Follow-up:

- `dio_mcm_episode_016p330|dio_mcm_episode_02ktejt`: `sleep_combination_fully_reactivated` (delta `[162, 159]`)
- `dio_mcm_episode_016p330|dio_mcm_episode_1sq70tu`: `sleep_combination_fully_reactivated` (delta `[162, 126]`)
- `dio_mcm_episode_016p330|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[162, 241]`)
- `dio_mcm_episode_02ktejt|dio_mcm_episode_1sq70tu`: `sleep_combination_fully_reactivated` (delta `[159, 126]`)
- `dio_mcm_episode_02ktejt|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[159, 241]`)
- `dio_mcm_episode_1sq70tu|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[126, 241]`)
- `dio_mcm_episode_016p330|dio_mcm_episode_18sa46n`: `sleep_combination_fully_reactivated` (delta `[162, 90]`)
- `dio_mcm_episode_02ktejt|dio_mcm_episode_18sa46n`: `sleep_combination_fully_reactivated` (delta `[159, 90]`)
- `dio_mcm_episode_18sa46n|dio_mcm_episode_1sq70tu`: `sleep_combination_fully_reactivated` (delta `[90, 126]`)
- `dio_mcm_episode_18sa46n|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[90, 241]`)
- `dio_mcm_episode_00wphe1|dio_mcm_episode_016p330`: `sleep_combination_fully_reactivated` (delta `[79, 162]`)
- `dio_mcm_episode_00wphe1|dio_mcm_episode_02ktejt`: `sleep_combination_fully_reactivated` (delta `[79, 159]`)

## Bewertung

Diese Stufe ist noch kein Nachweis fuer veraendertes Weltverhalten durch Schlaf.
Sie zeigt aber, dass Sleep bestehende Rollen passiv markieren kann, ohne Welt-Symbole neu zu erfinden.
Damit ist der naechste Schritt sauber messbar: eine spaetere Leseschicht darf pruefen,
ob diese passive Reorganisationsspur bei erneutem Weltkontakt wieder auftaucht oder neutral bleibt.
