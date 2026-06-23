# Aktueller Forschungslauf

Stand: 2026-06-23 08:50:14

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\field_quiet_candidates\1-12_2025_5m_solusdt_sol2025_field_quiet_01_2000.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `337` -> `337`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `3` -> `3`
- MCM-Rekopplung: `0.693964` -> `0.693142`
- MCM-Tragqualitaet: `0.510083` -> `0.510893`
- Sinnes-MCM-Kopplung: `0.839589` -> `0.838818`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00jaski, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_0oc3c1g, dio_104t4us, dio_14wjmk5, dio_155c3g6`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ja, dio_0h9h, dio_0l7p, dio_0m9z, dio_0oc3, dio_104t, dio_14wj, dio_155c`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `1`
- `kippend`: `20`
- `stabil`: `1536`
- `tragend_unruhig`: `437`

Episodenzustaende:

- `field_carried`: `1993`
- `field_strained`: `1`

## Artefakte

- Debug: `debug\field_quiet_candidates_sol2025\sol2025_field_quiet_01`
- Memory: `bot_memory\field_quiet_candidates_sol2025\sol2025_field_quiet_01.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
