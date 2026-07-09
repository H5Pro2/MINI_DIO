# Real-Sleep-Real Passive Reorganisation

Stand: 2026-07-06 19:00:46

## Zweck

Diese Kette prueft, was sich zwischen zwei Real-Welt-Beruehrungen veraendert,
wenn dazwischen eine entkoppelte MCM-Schlafdiagnose liegt. Real-B kann dieselbe oder eine andere Welt sein.

Wichtig: In diesem Lauf schreibt die Schlafphase eine passive Reorganisationsspur.
Diese Spur markiert nur beruehrte bestehende Rollen; sie erzeugt keine neue Weltbedeutung,
keine Richtung, kein Gate und keine Handlung.

## Kette

- Real A Welt: `data\kontrolliert_2023_positive_expansion_test1_1000_5m_SOLUSDT.csv`
- Real B Welt: `data\kontrolliert_2023_positive_expansion_test1_1000_5m_SOLUSDT.csv`
- gleiche Welt: `True`
- Real A Memory: `memory\real_sleep_real\real_positive_expansion_2023_1000_role_split_calibrated\memory_A_real_run.json`
- Sleep Diagnose: `debug\real_sleep_real\real_positive_expansion_2023_1000_role_split_calibrated\sleep`
- Memory nach Sleep: `memory\real_sleep_real\real_positive_expansion_2023_1000_role_split_calibrated\memory_A_after_sleep.json`
- Real B Memory: `memory\real_sleep_real\real_positive_expansion_2023_1000_role_split_calibrated\memory_B_real_run_after_sleep.json`

## Real A -> Real B

- Episoden: `994.0` -> `994.0`
- Unique Syntax: `219.0` -> `219.0`
- geschriebene Feldepisoden: `259.0` -> `259.0`
- MCM-Tragqualitaet: `0.503975` -> `0.504829`
- MCM-Rekopplung: `0.694509` -> `0.693637`
- MCM-Sinneskopplung: `0.846174` -> `0.845358`
- Top-Syntax-Ueberlappung: `1.0`
- Top-Familien-Ueberlappung: `1.0`

## Sleep Diagnose

- Sleep Ticks: `300`
- Rollen im Sleep-Pool: `24`
- aktive Rollensets: `8`
- Sleep Unique Syntax: `2`
- mittlerer Nachhall: `0.026155`
- passive Sleep-Memory geschrieben: `True`
- Sleep-Rollen-Reaktivierung: `5` / `5`
- Sleep-Kombinationen voll reaktiviert: `10` / `10`
- Sleep-Kombinationen teilweise reaktiviert: `0` / `10`
- Sleep-Follow-up-Zustand: `sleep_roles_fully_reactivated`

Sleep-Zustaende:

- `sleep_rekopplung`: `300`

Sleep-Rollen im Real-B-Follow-up:

- `dio_mcm_episode_1t06mit`: `sleep_role_reactivated_in_follow_world` (`22` -> `45`)
- `dio_mcm_episode_02ktejt`: `sleep_role_reactivated_in_follow_world` (`13` -> `26`)
- `dio_mcm_episode_04ovtxf`: `sleep_role_reactivated_in_follow_world` (`9` -> `16`)
- `dio_mcm_episode_016p330`: `sleep_role_reactivated_in_follow_world` (`9` -> `18`)
- `dio_mcm_episode_1lyw7zh`: `sleep_role_reactivated_in_follow_world` (`8` -> `16`)

Sleep-Kombinationen im Real-B-Follow-up:

- `dio_mcm_episode_02ktejt|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[13, 23]`)
- `dio_mcm_episode_02ktejt|dio_mcm_episode_04ovtxf`: `sleep_combination_fully_reactivated` (delta `[13, 7]`)
- `dio_mcm_episode_04ovtxf|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[7, 23]`)
- `dio_mcm_episode_016p330|dio_mcm_episode_02ktejt`: `sleep_combination_fully_reactivated` (delta `[9, 13]`)
- `dio_mcm_episode_016p330|dio_mcm_episode_04ovtxf`: `sleep_combination_fully_reactivated` (delta `[9, 7]`)
- `dio_mcm_episode_016p330|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[9, 23]`)
- `dio_mcm_episode_02ktejt|dio_mcm_episode_1lyw7zh`: `sleep_combination_fully_reactivated` (delta `[13, 8]`)
- `dio_mcm_episode_1lyw7zh|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[8, 23]`)
- `dio_mcm_episode_04ovtxf|dio_mcm_episode_1lyw7zh`: `sleep_combination_fully_reactivated` (delta `[7, 8]`)
- `dio_mcm_episode_016p330|dio_mcm_episode_1lyw7zh`: `sleep_combination_fully_reactivated` (delta `[9, 8]`)

## Bewertung

Diese Stufe ist noch kein Nachweis fuer veraendertes Weltverhalten durch Schlaf.
Sie zeigt aber, dass Sleep bestehende Rollen passiv markieren kann, ohne Welt-Symbole neu zu erfinden.
Damit ist der naechste Schritt sauber messbar: eine spaetere Leseschicht darf pruefen,
ob diese passive Reorganisationsspur bei erneutem Weltkontakt wieder auftaucht oder neutral bleibt.
