# Aktueller Forschungslauf

Stand: 2026-06-23 00:09:55

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_real_quiet_sol_2025_5m_2000.csv`
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

- Debug: `debug\adapted_real_quiet_sol_2025_5m_2000`
- Memory: `bot_memory\adapted_real_quiet_sol_2025_5m_2000.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
