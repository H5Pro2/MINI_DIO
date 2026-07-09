# Aktueller Forschungslauf

Stand: 2026-06-22 00:03:32

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
- Unique Syntaxsymbole: `694` -> `694`
- Episoden: `8778` -> `8778`
- geschriebene Episodenmemory: `36` -> `36`
- MCM-Rekopplung: `0.703662` -> `0.703219`
- MCM-Tragqualitaet: `0.530588` -> `0.531029`
- Sinnes-MCM-Kopplung: `0.843785` -> `0.843367`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00jaski, dio_00lyjkf, dio_0h9h06p, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6, dio_1ewh8ej`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ja, dio_00ly, dio_0h9h, dio_0m9z, dio_104t, dio_14wj, dio_155c, dio_1ewh`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `18`
- `kippend`: `82`
- `stabil`: `7194`
- `tragend_unruhig`: `1484`

Episodenzustaende:

- `field_carried`: `8760`
- `field_strained`: `18`

## Artefakte

- Debug: `debug\paxg_2024_1h_year`
- Memory: `memory\paxg_2024_1h_year_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
