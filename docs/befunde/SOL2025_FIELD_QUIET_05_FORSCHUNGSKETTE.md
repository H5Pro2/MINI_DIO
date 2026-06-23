# Aktueller Forschungslauf

Stand: 2026-06-23 08:50:42

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\field_quiet_candidates\1-12_2025_5m_solusdt_sol2025_field_quiet_05_2000.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `359` -> `359`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `5` -> `5`
- MCM-Rekopplung: `0.693294` -> `0.692475`
- MCM-Tragqualitaet: `0.508908` -> `0.509715`
- Sinnes-MCM-Kopplung: `0.838465` -> `0.837695`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00jaski, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_0oc3c1g, dio_104t4us, dio_155c3g6, dio_1lsuk2g`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ja, dio_0h9h, dio_0l7p, dio_0m9z, dio_0oc3, dio_104t, dio_155c, dio_1lsu`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `2`
- `kippend`: `10`
- `stabil`: `1527`
- `tragend_unruhig`: `455`

Episodenzustaende:

- `field_carried`: `1992`
- `field_strained`: `2`

## Artefakte

- Debug: `debug\field_quiet_candidates_sol2025\sol2025_field_quiet_05`
- Memory: `bot_memory\field_quiet_candidates_sol2025\sol2025_field_quiet_05.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
