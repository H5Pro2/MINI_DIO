# Aktueller Forschungslauf

Stand: 2026-06-21 21:04:27

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_sol_2025_1h_test1_2000_SOLUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `356` -> `356`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `15` -> `15`
- MCM-Rekopplung: `0.693962` -> `0.693221`
- MCM-Tragqualitaet: `0.509793` -> `0.510519`
- Sinnes-MCM-Kopplung: `0.844059` -> `0.843365`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6, dio_1ewh8ej`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c, dio_1ewh`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `7`
- `kippend`: `29`
- `stabil`: `1617`
- `tragend_unruhig`: `341`

Episodenzustaende:

- `field_carried`: `1987`
- `field_strained`: `7`

## Artefakte

- Debug: `debug\independent_sol2025_1h_2k`
- Memory: `memory\independent_sol2025_1h_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
