# Aktueller Forschungslauf

Stand: 2026-06-22 12:47:53

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_doge_2024_1h_10k_DOGEUSDT.csv`
- Kerzen: `8784`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `630` -> `630`
- Episoden: `8778` -> `8778`
- geschriebene Episodenmemory: `9` -> `9`
- MCM-Rekopplung: `0.705351` -> `0.704916`
- MCM-Tragqualitaet: `0.536627` -> `0.537059`
- Sinnes-MCM-Kopplung: `0.841983` -> `0.841572`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6, dio_17ctp0f`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c, dio_17ct`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `2`
- `kippend`: `55`
- `stabil`: `6986`
- `tragend_unruhig`: `1735`

Episodenzustaende:

- `field_carried`: `8776`
- `field_strained`: `2`

## Artefakte

- Debug: `debug\adapted_time_doge_2024_1h_10k`
- Memory: `bot_memory\adapted_time_doge_2024_1h_10k.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
