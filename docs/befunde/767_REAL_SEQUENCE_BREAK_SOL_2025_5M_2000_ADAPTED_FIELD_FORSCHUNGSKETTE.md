# Aktueller Forschungslauf

Stand: 2026-06-22 23:05:57

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_real_sequence_break_sol_2025_5m_2000.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `362` -> `362`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `7` -> `7`
- MCM-Rekopplung: `0.695763` -> `0.694975`
- MCM-Tragqualitaet: `0.511784` -> `0.51256`
- Sinnes-MCM-Kopplung: `0.843739` -> `0.842999`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_0pz659c, dio_104t4us, dio_14wjmk5, dio_155c3g6`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_0pz6, dio_104t, dio_14wj, dio_155c`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `3`
- `kippend`: `19`
- `stabil`: `1624`
- `tragend_unruhig`: `348`

Episodenzustaende:

- `field_carried`: `1991`
- `field_strained`: `3`

## Artefakte

- Debug: `debug\adapted_real_sequence_break_sol_2025_5m_2000`
- Memory: `bot_memory\adapted_real_sequence_break_sol_2025_5m_2000.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
