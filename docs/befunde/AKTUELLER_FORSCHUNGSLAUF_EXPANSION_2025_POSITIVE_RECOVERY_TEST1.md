# Aktueller Forschungslauf

Stand: 2026-06-18 21:20:23

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2025_positive_recovery_test1_1000_5m_SOLUSDT.csv`
- Kerzen: `1000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `924` -> `924`
- Episoden: `994` -> `994`
- geschriebene Episodenmemory: `59` -> `57`
- MCM-Rekopplung: `0.6308` -> `0.630474`
- MCM-Tragqualitaet: `0.359072` -> `0.359369`
- Sinnes-MCM-Kopplung: `0.837001` -> `0.836705`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_07y1h7q, dio_0qbo7v1, dio_18sw3vz, dio_1np6fxr, dio_1ozs4xu, dio_1w35kr6, dio_1wtaepk, dio_1xx0wlt`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_07y1, dio_0qbo, dio_18sw, dio_1np6, dio_1ozs, dio_1w35, dio_1wta, dio_1xx0`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `11`
- `gespannt`: `32`
- `kippend`: `30`
- `rekoppelnd`: `1`
- `stabil`: `511`
- `tragend_unruhig`: `409`

Episodenzustaende:

- `field_carried`: `961`
- `field_strained`: `33`

## Artefakte

- Debug: `debug\research_chain_expansion_2025_positive_recovery_test1`
- Memory: `memory\research_chain_expansion_2025_positive_recovery_test1_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
