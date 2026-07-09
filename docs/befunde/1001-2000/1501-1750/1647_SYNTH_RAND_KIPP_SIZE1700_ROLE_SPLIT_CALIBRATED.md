# Real-Sleep-Real Passive Reorganisation

Stand: 2026-07-06 16:22:05

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
- Real A Memory: `memory\real_sleep_real\synth_rand_kipp_start250_size1700_role_split_calibrated\memory_A_real_run.json`
- Sleep Diagnose: `debug\real_sleep_real\synth_rand_kipp_start250_size1700_role_split_calibrated\sleep`
- Memory nach Sleep: `memory\real_sleep_real\synth_rand_kipp_start250_size1700_role_split_calibrated\memory_A_after_sleep.json`
- Real B Memory: `memory\real_sleep_real\synth_rand_kipp_start250_size1700_role_split_calibrated\memory_B_real_run_after_sleep.json`

## Real A -> Real B

- Episoden: `1694.0` -> `1694.0`
- Unique Syntax: `193.0` -> `193.0`
- geschriebene Feldepisoden: `249.0` -> `251.0`
- MCM-Tragqualitaet: `0.555687` -> `0.555921`
- MCM-Rekopplung: `0.715072` -> `0.714818`
- MCM-Sinneskopplung: `0.851309` -> `0.851078`
- Top-Syntax-Ueberlappung: `1.0`
- Top-Familien-Ueberlappung: `1.0`

## Sleep Diagnose

- Sleep Ticks: `300`
- Rollen im Sleep-Pool: `24`
- aktive Rollensets: `12`
- Sleep Unique Syntax: `2`
- mittlerer Nachhall: `0.025624`
- passive Sleep-Memory geschrieben: `True`
- Sleep-Rollen-Reaktivierung: `8` / `8`
- Sleep-Kombinationen voll reaktiviert: `22` / `22`
- Sleep-Kombinationen teilweise reaktiviert: `0` / `22`
- Sleep-Follow-up-Zustand: `sleep_roles_fully_reactivated`

Sleep-Zustaende:

- `sleep_rekopplung`: `300`

Sleep-Rollen im Real-B-Follow-up:

- `dio_mcm_episode_1d7pbl5`: `sleep_role_reactivated_in_follow_world` (`11` -> `23`)
- `dio_mcm_episode_0yh3tum`: `sleep_role_reactivated_in_follow_world` (`10` -> `20`)
- `dio_mcm_episode_1gs06ww`: `sleep_role_reactivated_in_follow_world` (`8` -> `16`)
- `dio_mcm_episode_0uuhgpo`: `sleep_role_reactivated_in_follow_world` (`8` -> `16`)
- `dio_mcm_episode_0y7485n`: `sleep_role_reactivated_in_follow_world` (`7` -> `14`)
- `dio_mcm_episode_02vsba2`: `sleep_role_reactivated_in_follow_world` (`6` -> `12`)
- `dio_mcm_episode_0fug2ke`: `sleep_role_reactivated_in_follow_world` (`6` -> `12`)
- `dio_mcm_episode_148dasc`: `sleep_role_reactivated_in_follow_world` (`6` -> `12`)

Sleep-Kombinationen im Real-B-Follow-up:

- `dio_mcm_episode_0yh3tum|dio_mcm_episode_1d7pbl5`: `sleep_combination_fully_reactivated` (delta `[10, 12]`)
- `dio_mcm_episode_0yh3tum|dio_mcm_episode_1gs06ww`: `sleep_combination_fully_reactivated` (delta `[10, 8]`)
- `dio_mcm_episode_1d7pbl5|dio_mcm_episode_1gs06ww`: `sleep_combination_fully_reactivated` (delta `[12, 8]`)
- `dio_mcm_episode_0uuhgpo|dio_mcm_episode_0yh3tum`: `sleep_combination_fully_reactivated` (delta `[8, 10]`)
- `dio_mcm_episode_0uuhgpo|dio_mcm_episode_1d7pbl5`: `sleep_combination_fully_reactivated` (delta `[8, 12]`)
- `dio_mcm_episode_0uuhgpo|dio_mcm_episode_1gs06ww`: `sleep_combination_fully_reactivated` (delta `[8, 8]`)
- `dio_mcm_episode_0y7485n|dio_mcm_episode_0yh3tum`: `sleep_combination_fully_reactivated` (delta `[7, 10]`)
- `dio_mcm_episode_0y7485n|dio_mcm_episode_1d7pbl5`: `sleep_combination_fully_reactivated` (delta `[7, 12]`)
- `dio_mcm_episode_0y7485n|dio_mcm_episode_1gs06ww`: `sleep_combination_fully_reactivated` (delta `[7, 8]`)
- `dio_mcm_episode_0uuhgpo|dio_mcm_episode_0y7485n`: `sleep_combination_fully_reactivated` (delta `[8, 7]`)
- `dio_mcm_episode_02vsba2|dio_mcm_episode_0uuhgpo`: `sleep_combination_fully_reactivated` (delta `[6, 8]`)
- `dio_mcm_episode_02vsba2|dio_mcm_episode_0yh3tum`: `sleep_combination_fully_reactivated` (delta `[6, 10]`)

## Bewertung

Diese Stufe ist noch kein Nachweis fuer veraendertes Weltverhalten durch Schlaf.
Sie zeigt aber, dass Sleep bestehende Rollen passiv markieren kann, ohne Welt-Symbole neu zu erfinden.
Damit ist der naechste Schritt sauber messbar: eine spaetere Leseschicht darf pruefen,
ob diese passive Reorganisationsspur bei erneutem Weltkontakt wieder auftaucht oder neutral bleibt.

## Wie es weitergeht

Als naechstes wird die passive Sleep-Reorganisationsspur gegen weitere Welten geprueft.
Dann wird sichtbar, ob sie nur eine lokale Markierung bleibt oder als wiederkehrende Innenfeldspur tragfaehig ist.
