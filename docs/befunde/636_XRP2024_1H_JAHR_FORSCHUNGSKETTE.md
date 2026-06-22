# Aktueller Forschungslauf

Stand: 2026-06-22 01:11:53

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_xrp_2024_1h_10k_XRPUSDT.csv`
- Kerzen: `8784`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `655` -> `655`
- Episoden: `8778` -> `8778`
- geschriebene Episodenmemory: `39` -> `37`
- MCM-Rekopplung: `0.705138` -> `0.70475`
- MCM-Tragqualitaet: `0.535629` -> `0.536015`
- Sinnes-MCM-Kopplung: `0.846388` -> `0.846021`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00lyjkf, dio_0dd2ogm, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ly, dio_0dd2, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `19`
- `kippend`: `99`
- `stabil`: `7356`
- `tragend_unruhig`: `1304`

Episodenzustaende:

- `field_carried`: `8759`
- `field_strained`: `19`

## Artefakte

- Debug: `debug\xrp_2024_1h_10k`
- Memory: `memory\xrp_2024_1h_10k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
