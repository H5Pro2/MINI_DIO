# Aktueller Forschungslauf

Stand: 2026-06-22 12:47:57

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_paxg_2024_1h_10k_PAXGUSDT.csv`
- Kerzen: `8784`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `677` -> `677`
- Episoden: `8778` -> `8778`
- geschriebene Episodenmemory: `8` -> `8`
- MCM-Rekopplung: `0.704927` -> `0.704468`
- MCM-Tragqualitaet: `0.532557` -> `0.533015`
- Sinnes-MCM-Kopplung: `0.841193` -> `0.840759`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6, dio_1lsuk2g`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c, dio_1lsu`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `1`
- `kippend`: `53`
- `stabil`: `6951`
- `tragend_unruhig`: `1773`

Episodenzustaende:

- `field_carried`: `8776`
- `field_fragmented`: `1`
- `field_strained`: `1`

## Artefakte

- Debug: `debug\adapted_time_paxg_2024_1h_10k`
- Memory: `bot_memory\adapted_time_paxg_2024_1h_10k.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
