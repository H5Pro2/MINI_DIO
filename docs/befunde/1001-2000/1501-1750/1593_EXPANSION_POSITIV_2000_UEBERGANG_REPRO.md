# Real-Sleep-Real Passive Reorganisation

Stand: 2026-07-06 01:25:10

## Zweck

Diese Kette prueft, was sich zwischen zwei Real-Welt-Beruehrungen veraendert,
wenn dazwischen eine entkoppelte MCM-Schlafdiagnose liegt. Real-B kann dieselbe oder eine andere Welt sein.

Wichtig: In diesem Lauf schreibt die Schlafphase eine passive Reorganisationsspur.
Diese Spur markiert nur beruehrte bestehende Rollen; sie erzeugt keine neue Weltbedeutung,
keine Richtung, kein Gate und keine Handlung.

## Kette

- Real A Welt: `data\scan_expansion-positiv-2023_start2000_size2000.csv`
- Real B Welt: `data\scan_expansion-positiv-2023_start2000_size2000.csv`
- gleiche Welt: `True`
- Real A Memory: `memory\real_sleep_real\expansion_positiv_2000_start2000_transition_repro\memory_A_real_run.json`
- Sleep Diagnose: `debug\real_sleep_real\expansion_positiv_2000_start2000_transition_repro\sleep`
- Memory nach Sleep: `memory\real_sleep_real\expansion_positiv_2000_start2000_transition_repro\memory_A_after_sleep.json`
- Real B Memory: `memory\real_sleep_real\expansion_positiv_2000_start2000_transition_repro\memory_B_real_run_after_sleep.json`

## Real A -> Real B

- Episoden: `1994.0` -> `1994.0`
- Unique Syntax: `358.0` -> `358.0`
- geschriebene Feldepisoden: `3.0` -> `3.0`
- MCM-Tragqualitaet: `0.51115` -> `0.511909`
- MCM-Rekopplung: `0.695816` -> `0.69505`
- MCM-Sinneskopplung: `0.843251` -> `0.84253`
- Top-Syntax-Ueberlappung: `1.0`
- Top-Familien-Ueberlappung: `1.0`

## Sleep Diagnose

- Sleep Ticks: `300`
- Rollen im Sleep-Pool: `3`
- aktive Rollensets: `3`
- Sleep Unique Syntax: `1`
- mittlerer Nachhall: `0.023855`
- passive Sleep-Memory geschrieben: `True`
- Sleep-Rollen-Reaktivierung: `3` / `3`
- Sleep-Kombinationen voll reaktiviert: `3` / `3`
- Sleep-Kombinationen teilweise reaktiviert: `0` / `3`
- Sleep-Follow-up-Zustand: `sleep_roles_fully_reactivated`

Sleep-Zustaende:

- `sleep_rekopplung`: `300`

Sleep-Rollen im Real-B-Follow-up:

- `dio_mcm_episode_1k2bqha`: `sleep_role_reactivated_in_follow_world` (`1` -> `2`)
- `dio_mcm_episode_0e7qvj1`: `sleep_role_reactivated_in_follow_world` (`1` -> `2`)
- `dio_mcm_episode_0sjrih9`: `sleep_role_reactivated_in_follow_world` (`1` -> `2`)

Sleep-Kombinationen im Real-B-Follow-up:

- `dio_mcm_episode_0e7qvj1|dio_mcm_episode_1k2bqha`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)
- `dio_mcm_episode_0e7qvj1|dio_mcm_episode_0sjrih9`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)
- `dio_mcm_episode_0sjrih9|dio_mcm_episode_1k2bqha`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)

## Bewertung

Diese Stufe ist noch kein Nachweis fuer veraendertes Weltverhalten durch Schlaf.
Sie zeigt aber, dass Sleep bestehende Rollen passiv markieren kann, ohne Welt-Symbole neu zu erfinden.
Damit ist der naechste Schritt sauber messbar: eine spaetere Leseschicht darf pruefen,
ob diese passive Reorganisationsspur bei erneutem Weltkontakt wieder auftaucht oder neutral bleibt.

## Wie es weitergeht

Als naechstes wird die passive Sleep-Reorganisationsspur gegen weitere Welten geprueft.
Dann wird sichtbar, ob sie nur eine lokale Markierung bleibt oder als wiederkehrende Innenfeldspur tragfaehig ist.
