# Real-Sleep-Real Passive Reorganisation

Stand: 2026-07-06 23:27:13

## Zweck

Diese Kette prueft, was sich zwischen zwei Real-Welt-Beruehrungen veraendert,
wenn dazwischen eine entkoppelte MCM-Schlafdiagnose liegt. Real-B kann dieselbe oder eine andere Welt sein.

Wichtig: In diesem Lauf schreibt die Schlafphase eine passive Reorganisationsspur.
Diese Spur markiert nur beruehrte bestehende Rollen; sie erzeugt keine neue Weltbedeutung,
keine Richtung, kein Gate und keine Handlung.

## Kette

- Real A Welt: `data\segment_positive_expansion_2023_10k_start4000_size2000.csv`
- Real B Welt: `data\segment_positive_expansion_2023_10k_start6000_size2000.csv`
- gleiche Welt: `False`
- Real A Memory: `memory\real_sleep_real\maturation_distributed_expansion_start4000_to_6000\memory_A_real_run.json`
- Sleep Diagnose: `debug\real_sleep_real\maturation_distributed_expansion_start4000_to_6000\sleep`
- Memory nach Sleep: `memory\real_sleep_real\maturation_distributed_expansion_start4000_to_6000\memory_A_after_sleep.json`
- Real B Memory: `memory\real_sleep_real\maturation_distributed_expansion_start4000_to_6000\memory_B_real_run_after_sleep.json`

## Real A -> Real B

- Episoden: `1994.0` -> `1994.0`
- Unique Syntax: `394.0` -> `415.0`
- geschriebene Feldepisoden: `760.0` -> `703.0`
- MCM-Tragqualitaet: `0.502677` -> `0.502627`
- MCM-Rekopplung: `0.689427` -> `0.688653`
- MCM-Sinneskopplung: `0.833465` -> `0.834458`
- Top-Syntax-Ueberlappung: `0.777778`
- Top-Familien-Ueberlappung: `1.0`

## Sleep Diagnose

- Sleep Ticks: `300`
- Rollen im Sleep-Pool: `24`
- aktive Rollensets: `8`
- Sleep Unique Syntax: `2`
- mittlerer Nachhall: `0.026989`
- passive Sleep-Memory geschrieben: `True`
- Sleep-Rollen-Reaktivierung: `5` / `5`
- Sleep-Kombinationen voll reaktiviert: `10` / `10`
- Sleep-Kombinationen teilweise reaktiviert: `0` / `10`
- Sleep-Follow-up-Zustand: `sleep_roles_fully_reactivated`

Sleep-Zustaende:

- `sleep_rekopplung`: `300`

Sleep-Rollen im Real-B-Follow-up:

- `dio_mcm_episode_1t06mit`: `sleep_role_reactivated_in_follow_world` (`67` -> `119`)
- `dio_mcm_episode_02ktejt`: `sleep_role_reactivated_in_follow_world` (`32` -> `67`)
- `dio_mcm_episode_016p330`: `sleep_role_reactivated_in_follow_world` (`28` -> `58`)
- `dio_mcm_episode_18sa46n`: `sleep_role_reactivated_in_follow_world` (`26` -> `47`)
- `dio_mcm_episode_1ve8nle`: `sleep_role_reactivated_in_follow_world` (`26` -> `39`)

Sleep-Kombinationen im Real-B-Follow-up:

- `dio_mcm_episode_02ktejt|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[35, 52]`)
- `dio_mcm_episode_016p330|dio_mcm_episode_02ktejt`: `sleep_combination_fully_reactivated` (delta `[30, 35]`)
- `dio_mcm_episode_016p330|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[30, 52]`)
- `dio_mcm_episode_02ktejt|dio_mcm_episode_18sa46n`: `sleep_combination_fully_reactivated` (delta `[35, 21]`)
- `dio_mcm_episode_18sa46n|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[21, 52]`)
- `dio_mcm_episode_016p330|dio_mcm_episode_18sa46n`: `sleep_combination_fully_reactivated` (delta `[30, 21]`)
- `dio_mcm_episode_02ktejt|dio_mcm_episode_1ve8nle`: `sleep_combination_fully_reactivated` (delta `[35, 13]`)
- `dio_mcm_episode_1t06mit|dio_mcm_episode_1ve8nle`: `sleep_combination_fully_reactivated` (delta `[52, 13]`)
- `dio_mcm_episode_18sa46n|dio_mcm_episode_1ve8nle`: `sleep_combination_fully_reactivated` (delta `[21, 13]`)
- `dio_mcm_episode_016p330|dio_mcm_episode_1ve8nle`: `sleep_combination_fully_reactivated` (delta `[30, 13]`)

## Bewertung

Diese Stufe ist noch kein Nachweis fuer veraendertes Weltverhalten durch Schlaf.
Sie zeigt aber, dass Sleep bestehende Rollen passiv markieren kann, ohne Welt-Symbole neu zu erfinden.
Damit ist der naechste Schritt sauber messbar: eine spaetere Leseschicht darf pruefen,
ob diese passive Reorganisationsspur bei erneutem Weltkontakt wieder auftaucht oder neutral bleibt.
