# Real-Sleep-Real Passive Reorganisation

Stand: 2026-07-05 23:31:25

## Zweck

Diese Kette prueft, was sich zwischen zwei Real-Welt-Beruehrungen veraendert,
wenn dazwischen eine entkoppelte MCM-Schlafdiagnose liegt. Real-B kann dieselbe oder eine andere Welt sein.

Wichtig: In diesem Lauf schreibt die Schlafphase eine passive Reorganisationsspur.
Diese Spur markiert nur beruehrte bestehende Rollen; sie erzeugt keine neue Weltbedeutung,
keine Richtung, kein Gate und keine Handlung.

## Kette

- Real A Welt: `data\kontrolliert_doge2024_sleep_origin_1000_5m.csv`
- Real B Welt: `data\kontrolliert_doge2024_sleep_same_1000_5m.csv`
- gleiche Welt: `False`
- Real A Memory: `memory\real_sleep_real\doge1000_multirole_probe_fresh\memory_A_real_run.json`
- Sleep Diagnose: `debug\real_sleep_real\doge1000_multirole_probe_fresh\sleep`
- Memory nach Sleep: `memory\real_sleep_real\doge1000_multirole_probe_fresh\memory_A_after_sleep.json`
- Real B Memory: `memory\real_sleep_real\doge1000_multirole_probe_fresh\memory_B_real_run_after_sleep.json`

## Real A -> Real B

- Episoden: `994.0` -> `994.0`
- Unique Syntax: `249.0` -> `249.0`
- geschriebene Feldepisoden: `1.0` -> `1.0`
- MCM-Tragqualitaet: `0.500428` -> `0.50124`
- MCM-Rekopplung: `0.691151` -> `0.690323`
- MCM-Sinneskopplung: `0.843061` -> `0.842285`
- Top-Syntax-Ueberlappung: `1.0`
- Top-Familien-Ueberlappung: `1.0`

## Sleep Diagnose

- Sleep Ticks: `300`
- Rollen im Sleep-Pool: `1`
- aktive Rollensets: `1`
- Sleep Unique Syntax: `1`
- mittlerer Nachhall: `0.026362`
- passive Sleep-Memory geschrieben: `True`
- Sleep-Rollen-Reaktivierung: `1` / `1`
- Sleep-Kombinationen voll reaktiviert: `0` / `0`
- Sleep-Kombinationen teilweise reaktiviert: `0` / `0`
- Sleep-Follow-up-Zustand: `sleep_roles_fully_reactivated`

Sleep-Zustaende:

- `sleep_rekopplung`: `300`

Sleep-Rollen im Real-B-Follow-up:

- `dio_mcm_episode_1joiyc3`: `sleep_role_reactivated_in_follow_world` (`1` -> `2`)

Sleep-Kombinationen im Real-B-Follow-up:


## Bewertung

Diese Stufe ist noch kein Nachweis fuer veraendertes Weltverhalten durch Schlaf.
Sie zeigt aber, dass Sleep bestehende Rollen passiv markieren kann, ohne Welt-Symbole neu zu erfinden.
Damit ist der naechste Schritt sauber messbar: eine spaetere Leseschicht darf pruefen,
ob diese passive Reorganisationsspur bei erneutem Weltkontakt wieder auftaucht oder neutral bleibt.

## Wie es weitergeht

Als naechstes wird die passive Sleep-Reorganisationsspur gegen weitere Welten geprueft.
Dann wird sichtbar, ob sie nur eine lokale Markierung bleibt oder als wiederkehrende Innenfeldspur tragfaehig ist.
