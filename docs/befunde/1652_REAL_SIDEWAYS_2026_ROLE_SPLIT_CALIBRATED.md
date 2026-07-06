# Real-Sleep-Real Passive Reorganisation

Stand: 2026-07-06 19:00:35

## Zweck

Diese Kette prueft, was sich zwischen zwei Real-Welt-Beruehrungen veraendert,
wenn dazwischen eine entkoppelte MCM-Schlafdiagnose liegt. Real-B kann dieselbe oder eine andere Welt sein.

Wichtig: In diesem Lauf schreibt die Schlafphase eine passive Reorganisationsspur.
Diese Spur markiert nur beruehrte bestehende Rollen; sie erzeugt keine neue Weltbedeutung,
keine Richtung, kein Gate und keine Handlung.

## Kette

- Real A Welt: `data\kontrolliert_2026_sideways_test1_1000_5m_SOLUSDT.csv`
- Real B Welt: `data\kontrolliert_2026_sideways_test1_1000_5m_SOLUSDT.csv`
- gleiche Welt: `True`
- Real A Memory: `memory\real_sleep_real\real_sideways_2026_1000_role_split_calibrated\memory_A_real_run.json`
- Sleep Diagnose: `debug\real_sleep_real\real_sideways_2026_1000_role_split_calibrated\sleep`
- Memory nach Sleep: `memory\real_sleep_real\real_sideways_2026_1000_role_split_calibrated\memory_A_after_sleep.json`
- Real B Memory: `memory\real_sleep_real\real_sideways_2026_1000_role_split_calibrated\memory_B_real_run_after_sleep.json`

## Real A -> Real B

- Episoden: `994.0` -> `994.0`
- Unique Syntax: `223.0` -> `223.0`
- geschriebene Feldepisoden: `241.0` -> `241.0`
- MCM-Tragqualitaet: `0.504968` -> `0.505818`
- MCM-Rekopplung: `0.694865` -> `0.693999`
- MCM-Sinneskopplung: `0.849476` -> `0.848665`
- Top-Syntax-Ueberlappung: `1.0`
- Top-Familien-Ueberlappung: `1.0`

## Sleep Diagnose

- Sleep Ticks: `300`
- Rollen im Sleep-Pool: `24`
- aktive Rollensets: `14`
- Sleep Unique Syntax: `1`
- mittlerer Nachhall: `0.024766`
- passive Sleep-Memory geschrieben: `True`
- Sleep-Rollen-Reaktivierung: `7` / `7`
- Sleep-Kombinationen voll reaktiviert: `21` / `21`
- Sleep-Kombinationen teilweise reaktiviert: `0` / `21`
- Sleep-Follow-up-Zustand: `sleep_roles_fully_reactivated`

Sleep-Zustaende:

- `sleep_rekopplung`: `300`

Sleep-Rollen im Real-B-Follow-up:

- `dio_mcm_episode_1t06mit`: `sleep_role_reactivated_in_follow_world` (`15` -> `30`)
- `dio_mcm_episode_1lyw7zh`: `sleep_role_reactivated_in_follow_world` (`10` -> `20`)
- `dio_mcm_episode_02ktejt`: `sleep_role_reactivated_in_follow_world` (`9` -> `19`)
- `dio_mcm_episode_09627ba`: `sleep_role_reactivated_in_follow_world` (`9` -> `18`)
- `dio_mcm_episode_0hv1uu1`: `sleep_role_reactivated_in_follow_world` (`9` -> `18`)
- `dio_mcm_episode_07iaozp`: `sleep_role_reactivated_in_follow_world` (`9` -> `18`)
- `dio_mcm_episode_1ctchld`: `sleep_role_reactivated_in_follow_world` (`8` -> `16`)

Sleep-Kombinationen im Real-B-Follow-up:

- `dio_mcm_episode_1lyw7zh|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[10, 15]`)
- `dio_mcm_episode_02ktejt|dio_mcm_episode_1lyw7zh`: `sleep_combination_fully_reactivated` (delta `[10, 10]`)
- `dio_mcm_episode_02ktejt|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[10, 15]`)
- `dio_mcm_episode_09627ba|dio_mcm_episode_1lyw7zh`: `sleep_combination_fully_reactivated` (delta `[9, 10]`)
- `dio_mcm_episode_09627ba|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[9, 15]`)
- `dio_mcm_episode_0hv1uu1|dio_mcm_episode_1lyw7zh`: `sleep_combination_fully_reactivated` (delta `[9, 10]`)
- `dio_mcm_episode_0hv1uu1|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[9, 15]`)
- `dio_mcm_episode_02ktejt|dio_mcm_episode_09627ba`: `sleep_combination_fully_reactivated` (delta `[10, 9]`)
- `dio_mcm_episode_02ktejt|dio_mcm_episode_0hv1uu1`: `sleep_combination_fully_reactivated` (delta `[10, 9]`)
- `dio_mcm_episode_09627ba|dio_mcm_episode_0hv1uu1`: `sleep_combination_fully_reactivated` (delta `[9, 9]`)
- `dio_mcm_episode_07iaozp|dio_mcm_episode_1lyw7zh`: `sleep_combination_fully_reactivated` (delta `[9, 10]`)
- `dio_mcm_episode_07iaozp|dio_mcm_episode_1t06mit`: `sleep_combination_fully_reactivated` (delta `[9, 15]`)

## Bewertung

Diese Stufe ist noch kein Nachweis fuer veraendertes Weltverhalten durch Schlaf.
Sie zeigt aber, dass Sleep bestehende Rollen passiv markieren kann, ohne Welt-Symbole neu zu erfinden.
Damit ist der naechste Schritt sauber messbar: eine spaetere Leseschicht darf pruefen,
ob diese passive Reorganisationsspur bei erneutem Weltkontakt wieder auftaucht oder neutral bleibt.

## Wie es weitergeht

Als naechstes wird die passive Sleep-Reorganisationsspur gegen weitere Welten geprueft.
Dann wird sichtbar, ob sie nur eine lokale Markierung bleibt oder als wiederkehrende Innenfeldspur tragfaehig ist.
