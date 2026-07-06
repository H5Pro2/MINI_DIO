# Real-Sleep-Real Passive Reorganisation

Stand: 2026-07-06 20:50:42

## Zweck

Diese Kette prueft, was sich zwischen zwei Real-Welt-Beruehrungen veraendert,
wenn dazwischen eine entkoppelte MCM-Schlafdiagnose liegt. Real-B kann dieselbe oder eine andere Welt sein.

Wichtig: In diesem Lauf schreibt die Schlafphase eine passive Reorganisationsspur.
Diese Spur markiert nur beruehrte bestehende Rollen; sie erzeugt keine neue Weltbedeutung,
keine Richtung, kein Gate und keine Handlung.

## Kette

- Real A Welt: `data\kontrolliert_2026_sideways_10k_5m_SOLUSDT.csv`
- Real B Welt: `data\kontrolliert_2026_sideways_10k_5m_SOLUSDT.csv`
- gleiche Welt: `True`
- Real A Memory: `memory\real_sleep_real\real_sideways_2026_10k_role_split_calibrated\memory_A_real_run.json`
- Sleep Diagnose: `debug\real_sleep_real\real_sideways_2026_10k_role_split_calibrated\sleep`
- Memory nach Sleep: `memory\real_sleep_real\real_sideways_2026_10k_role_split_calibrated\memory_A_after_sleep.json`
- Real B Memory: `memory\real_sleep_real\real_sideways_2026_10k_role_split_calibrated\memory_B_real_run_after_sleep.json`

## Real A -> Real B

- Episoden: `9994.0` -> `9994.0`
- Unique Syntax: `395.0` -> `395.0`
- geschriebene Feldepisoden: `1427.0` -> `1437.0`
- MCM-Tragqualitaet: `0.548368` -> `0.548655`
- MCM-Rekopplung: `0.713662` -> `0.713379`
- MCM-Sinneskopplung: `0.855553` -> `0.855283`
- Top-Syntax-Ueberlappung: `1.0`
- Top-Familien-Ueberlappung: `1.0`

## Sleep Diagnose

- Sleep Ticks: `300`
- Rollen im Sleep-Pool: `24`
- aktive Rollensets: `2`
- Sleep Unique Syntax: `1`
- mittlerer Nachhall: `0.026367`
- passive Sleep-Memory geschrieben: `True`
- Sleep-Rollen-Reaktivierung: `4` / `4`
- Sleep-Kombinationen voll reaktiviert: `6` / `6`
- Sleep-Kombinationen teilweise reaktiviert: `0` / `6`
- Sleep-Follow-up-Zustand: `sleep_roles_fully_reactivated`

Sleep-Zustaende:

- `sleep_rekopplung`: `300`

Sleep-Rollen im Real-B-Follow-up:

- `dio_mcm_episode_1j3mt4v`: `sleep_role_reactivated_in_follow_world` (`155` -> `313`)
- `dio_mcm_episode_02az5yl`: `sleep_role_reactivated_in_follow_world` (`113` -> `226`)
- `dio_mcm_episode_02ktejt`: `sleep_role_reactivated_in_follow_world` (`94` -> `189`)
- `dio_mcm_episode_1t06mit`: `sleep_role_reactivated_in_follow_world` (`56` -> `113`)

Sleep-Kombinationen im Real-B-Follow-up:

- `dio_mcm_episode_02az5yl|dio_mcm_episode_02ktejt`: `sleep_combination_fully_reactivated` (delta `[113, 95]`)
- `dio_mcm_episode_02az5yl|dio_mcm_episode_1j3mt4v`: `sleep_combination_fully_reactivated` (delta `[113, 158]`)
- `dio_mcm_episode_02ktejt|dio_mcm_episode_1j3mt4v`: `sleep_combination_fully_reactivated` (delta `[95, 158]`)
- `dio_mcm_episode_02az5yl|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[113, 57]`)
- `dio_mcm_episode_02ktejt|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[95, 57]`)
- `dio_mcm_episode_1j3mt4v|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[158, 57]`)

## Bewertung

Diese Stufe ist noch kein Nachweis fuer veraendertes Weltverhalten durch Schlaf.
Sie zeigt aber, dass Sleep bestehende Rollen passiv markieren kann, ohne Welt-Symbole neu zu erfinden.
Damit ist der naechste Schritt sauber messbar: eine spaetere Leseschicht darf pruefen,
ob diese passive Reorganisationsspur bei erneutem Weltkontakt wieder auftaucht oder neutral bleibt.

## Wie es weitergeht

Als naechstes wird die passive Sleep-Reorganisationsspur gegen weitere Welten geprueft.
Dann wird sichtbar, ob sie nur eine lokale Markierung bleibt oder als wiederkehrende Innenfeldspur tragfaehig ist.
