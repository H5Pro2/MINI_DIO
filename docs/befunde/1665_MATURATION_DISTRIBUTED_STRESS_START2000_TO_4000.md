# Real-Sleep-Real Passive Reorganisation

Stand: 2026-07-06 23:27:04

## Zweck

Diese Kette prueft, was sich zwischen zwei Real-Welt-Beruehrungen veraendert,
wenn dazwischen eine entkoppelte MCM-Schlafdiagnose liegt. Real-B kann dieselbe oder eine andere Welt sein.

Wichtig: In diesem Lauf schreibt die Schlafphase eine passive Reorganisationsspur.
Diese Spur markiert nur beruehrte bestehende Rollen; sie erzeugt keine neue Weltbedeutung,
keine Richtung, kein Gate und keine Handlung.

## Kette

- Real A Welt: `data\segment_negative_stress_2023_10k_start2000_size2000.csv`
- Real B Welt: `data\segment_negative_stress_2023_10k_start4000_size2000.csv`
- gleiche Welt: `False`
- Real A Memory: `memory\real_sleep_real\maturation_distributed_stress_start2000_to_4000\memory_A_real_run.json`
- Sleep Diagnose: `debug\real_sleep_real\maturation_distributed_stress_start2000_to_4000\sleep`
- Memory nach Sleep: `memory\real_sleep_real\maturation_distributed_stress_start2000_to_4000\memory_A_after_sleep.json`
- Real B Memory: `memory\real_sleep_real\maturation_distributed_stress_start2000_to_4000\memory_B_real_run_after_sleep.json`

## Real A -> Real B

- Episoden: `1994.0` -> `1994.0`
- Unique Syntax: `314.0` -> `274.0`
- geschriebene Feldepisoden: `441.0` -> `432.0`
- MCM-Tragqualitaet: `0.518512` -> `0.523409`
- MCM-Rekopplung: `0.700541` -> `0.70178`
- MCM-Sinneskopplung: `0.848796` -> `0.848947`
- Top-Syntax-Ueberlappung: `0.6`
- Top-Familien-Ueberlappung: `0.777778`

## Sleep Diagnose

- Sleep Ticks: `300`
- Rollen im Sleep-Pool: `24`
- aktive Rollensets: `5`
- Sleep Unique Syntax: `2`
- mittlerer Nachhall: `0.027066`
- passive Sleep-Memory geschrieben: `True`
- Sleep-Rollen-Reaktivierung: `4` / `4`
- Sleep-Kombinationen voll reaktiviert: `6` / `6`
- Sleep-Kombinationen teilweise reaktiviert: `0` / `6`
- Sleep-Follow-up-Zustand: `sleep_roles_fully_reactivated`

Sleep-Zustaende:

- `sleep_rekopplung`: `300`

Sleep-Rollen im Real-B-Follow-up:

- `dio_mcm_episode_1t06mit`: `sleep_role_reactivated_in_follow_world` (`39` -> `69`)
- `dio_mcm_episode_02ktejt`: `sleep_role_reactivated_in_follow_world` (`20` -> `45`)
- `dio_mcm_episode_1ve8nle`: `sleep_role_reactivated_in_follow_world` (`17` -> `22`)
- `dio_mcm_episode_016p330`: `sleep_role_reactivated_in_follow_world` (`15` -> `23`)

Sleep-Kombinationen im Real-B-Follow-up:

- `dio_mcm_episode_02ktejt|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[25, 30]`)
- `dio_mcm_episode_02ktejt|dio_mcm_episode_1ve8nle`: `sleep_combination_fully_reactivated` (delta `[25, 5]`)
- `dio_mcm_episode_1t06mit|dio_mcm_episode_1ve8nle`: `sleep_combination_fully_reactivated` (delta `[30, 5]`)
- `dio_mcm_episode_016p330|dio_mcm_episode_02ktejt`: `sleep_combination_fully_reactivated` (delta `[8, 25]`)
- `dio_mcm_episode_016p330|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[8, 30]`)
- `dio_mcm_episode_016p330|dio_mcm_episode_1ve8nle`: `sleep_combination_fully_reactivated` (delta `[8, 5]`)

## Bewertung

Diese Stufe ist noch kein Nachweis fuer veraendertes Weltverhalten durch Schlaf.
Sie zeigt aber, dass Sleep bestehende Rollen passiv markieren kann, ohne Welt-Symbole neu zu erfinden.
Damit ist der naechste Schritt sauber messbar: eine spaetere Leseschicht darf pruefen,
ob diese passive Reorganisationsspur bei erneutem Weltkontakt wieder auftaucht oder neutral bleibt.

## Wie es weitergeht

Als naechstes wird die passive Sleep-Reorganisationsspur gegen weitere Welten geprueft.
Dann wird sichtbar, ob sie nur eine lokale Markierung bleibt oder als wiederkehrende Innenfeldspur tragfaehig ist.
