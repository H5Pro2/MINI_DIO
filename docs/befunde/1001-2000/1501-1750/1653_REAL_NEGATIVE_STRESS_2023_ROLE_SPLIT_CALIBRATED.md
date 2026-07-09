# Real-Sleep-Real Passive Reorganisation

Stand: 2026-07-06 19:00:41

## Zweck

Diese Kette prueft, was sich zwischen zwei Real-Welt-Beruehrungen veraendert,
wenn dazwischen eine entkoppelte MCM-Schlafdiagnose liegt. Real-B kann dieselbe oder eine andere Welt sein.

Wichtig: In diesem Lauf schreibt die Schlafphase eine passive Reorganisationsspur.
Diese Spur markiert nur beruehrte bestehende Rollen; sie erzeugt keine neue Weltbedeutung,
keine Richtung, kein Gate und keine Handlung.

## Kette

- Real A Welt: `data\kontrolliert_2023_negative_stress_test1_1000_5m_SOLUSDT.csv`
- Real B Welt: `data\kontrolliert_2023_negative_stress_test1_1000_5m_SOLUSDT.csv`
- gleiche Welt: `True`
- Real A Memory: `memory\real_sleep_real\real_negative_stress_2023_1000_role_split_calibrated\memory_A_real_run.json`
- Sleep Diagnose: `debug\real_sleep_real\real_negative_stress_2023_1000_role_split_calibrated\sleep`
- Memory nach Sleep: `memory\real_sleep_real\real_negative_stress_2023_1000_role_split_calibrated\memory_A_after_sleep.json`
- Real B Memory: `memory\real_sleep_real\real_negative_stress_2023_1000_role_split_calibrated\memory_B_real_run_after_sleep.json`

## Real A -> Real B

- Episoden: `994.0` -> `994.0`
- Unique Syntax: `257.0` -> `257.0`
- geschriebene Feldepisoden: `347.0` -> `348.0`
- MCM-Tragqualitaet: `0.496802` -> `0.497647`
- MCM-Rekopplung: `0.68908` -> `0.688219`
- MCM-Sinneskopplung: `0.838753` -> `0.837946`
- Top-Syntax-Ueberlappung: `1.0`
- Top-Familien-Ueberlappung: `1.0`

## Sleep Diagnose

- Sleep Ticks: `300`
- Rollen im Sleep-Pool: `24`
- aktive Rollensets: `2`
- Sleep Unique Syntax: `1`
- mittlerer Nachhall: `0.027092`
- passive Sleep-Memory geschrieben: `True`
- Sleep-Rollen-Reaktivierung: `2` / `2`
- Sleep-Kombinationen voll reaktiviert: `1` / `1`
- Sleep-Kombinationen teilweise reaktiviert: `0` / `1`
- Sleep-Follow-up-Zustand: `sleep_roles_fully_reactivated`

Sleep-Zustaende:

- `sleep_rekopplung`: `300`

Sleep-Rollen im Real-B-Follow-up:

- `dio_mcm_episode_1t06mit`: `sleep_role_reactivated_in_follow_world` (`40` -> `80`)
- `dio_mcm_episode_016p330`: `sleep_role_reactivated_in_follow_world` (`18` -> `36`)

Sleep-Kombinationen im Real-B-Follow-up:

- `dio_mcm_episode_016p330|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[18, 40]`)

## Bewertung

Diese Stufe ist noch kein Nachweis fuer veraendertes Weltverhalten durch Schlaf.
Sie zeigt aber, dass Sleep bestehende Rollen passiv markieren kann, ohne Welt-Symbole neu zu erfinden.
Damit ist der naechste Schritt sauber messbar: eine spaetere Leseschicht darf pruefen,
ob diese passive Reorganisationsspur bei erneutem Weltkontakt wieder auftaucht oder neutral bleibt.

## Wie es weitergeht

Als naechstes wird die passive Sleep-Reorganisationsspur gegen weitere Welten geprueft.
Dann wird sichtbar, ob sie nur eine lokale Markierung bleibt oder als wiederkehrende Innenfeldspur tragfaehig ist.
