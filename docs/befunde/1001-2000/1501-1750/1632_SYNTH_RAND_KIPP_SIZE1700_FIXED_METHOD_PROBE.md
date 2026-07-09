# Real-Sleep-Real Passive Reorganisation

Stand: 2026-07-06 12:12:30

## Zweck

Diese Kette prueft, was sich zwischen zwei Real-Welt-Beruehrungen veraendert,
wenn dazwischen eine entkoppelte MCM-Schlafdiagnose liegt. Real-B kann dieselbe oder eine andere Welt sein.

Wichtig: In diesem Lauf schreibt die Schlafphase eine passive Reorganisationsspur.
Diese Spur markiert nur beruehrte bestehende Rollen; sie erzeugt keine neue Weltbedeutung,
keine Richtung, kein Gate und keine Handlung.

## Kette

- Real A Welt: `data\scan_synth-rand-kipp-start0_start250_size1700.csv`
- Real B Welt: `data\scan_synth-rand-kipp-start0_start250_size1700.csv`
- gleiche Welt: `True`
- Real A Memory: `memory\real_sleep_real\synth_rand_kipp_start250_size1700_fixed_method_probe\memory_A_real_run.json`
- Sleep Diagnose: `debug\real_sleep_real\synth_rand_kipp_start250_size1700_fixed_method_probe\sleep`
- Memory nach Sleep: `memory\real_sleep_real\synth_rand_kipp_start250_size1700_fixed_method_probe\memory_A_after_sleep.json`
- Real B Memory: `memory\real_sleep_real\synth_rand_kipp_start250_size1700_fixed_method_probe\memory_B_real_run_after_sleep.json`

## Real A -> Real B

- Episoden: `1694.0` -> `1694.0`
- Unique Syntax: `200.0` -> `200.0`
- geschriebene Feldepisoden: `5.0` -> `5.0`
- MCM-Tragqualitaet: `0.562804` -> `0.563026`
- MCM-Rekopplung: `0.724774` -> `0.724538`
- MCM-Sinneskopplung: `0.875627` -> `0.87541`
- Top-Syntax-Ueberlappung: `1.0`
- Top-Familien-Ueberlappung: `1.0`

## Sleep Diagnose

- Sleep Ticks: `300`
- Rollen im Sleep-Pool: `5`
- aktive Rollensets: `6`
- Sleep Unique Syntax: `1`
- mittlerer Nachhall: `0.024778`
- passive Sleep-Memory geschrieben: `True`
- Sleep-Rollen-Reaktivierung: `5` / `5`
- Sleep-Kombinationen voll reaktiviert: `10` / `10`
- Sleep-Kombinationen teilweise reaktiviert: `0` / `10`
- Sleep-Follow-up-Zustand: `sleep_roles_fully_reactivated`

Sleep-Zustaende:

- `sleep_rekopplung`: `300`

Sleep-Rollen im Real-B-Follow-up:

- `dio_mcm_episode_1hx59nd`: `sleep_role_reactivated_in_follow_world` (`1` -> `2`)
- `dio_mcm_episode_0opcw3b`: `sleep_role_reactivated_in_follow_world` (`1` -> `2`)
- `dio_mcm_episode_10anbr4`: `sleep_role_reactivated_in_follow_world` (`1` -> `2`)
- `dio_mcm_episode_14fzhly`: `sleep_role_reactivated_in_follow_world` (`1` -> `2`)
- `dio_mcm_episode_0r5qcif`: `sleep_role_reactivated_in_follow_world` (`1` -> `2`)

Sleep-Kombinationen im Real-B-Follow-up:

- `dio_mcm_episode_0opcw3b|dio_mcm_episode_10anbr4`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)
- `dio_mcm_episode_0opcw3b|dio_mcm_episode_14fzhly`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)
- `dio_mcm_episode_0opcw3b|dio_mcm_episode_1hx59nd`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)
- `dio_mcm_episode_10anbr4|dio_mcm_episode_14fzhly`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)
- `dio_mcm_episode_10anbr4|dio_mcm_episode_1hx59nd`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)
- `dio_mcm_episode_14fzhly|dio_mcm_episode_1hx59nd`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)
- `dio_mcm_episode_0opcw3b|dio_mcm_episode_0r5qcif`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)
- `dio_mcm_episode_0r5qcif|dio_mcm_episode_10anbr4`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)
- `dio_mcm_episode_0r5qcif|dio_mcm_episode_14fzhly`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)
- `dio_mcm_episode_0r5qcif|dio_mcm_episode_1hx59nd`: `sleep_combination_fully_reactivated` (delta `[1, 1]`)

## Bewertung

Diese Stufe ist noch kein Nachweis fuer veraendertes Weltverhalten durch Schlaf.
Sie zeigt aber, dass Sleep bestehende Rollen passiv markieren kann, ohne Welt-Symbole neu zu erfinden.
Damit ist der naechste Schritt sauber messbar: eine spaetere Leseschicht darf pruefen,
ob diese passive Reorganisationsspur bei erneutem Weltkontakt wieder auftaucht oder neutral bleibt.

## Wie es weitergeht

Als naechstes wird die passive Sleep-Reorganisationsspur gegen weitere Welten geprueft.
Dann wird sichtbar, ob sie nur eine lokale Markierung bleibt oder als wiederkehrende Innenfeldspur tragfaehig ist.
