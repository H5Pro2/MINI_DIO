# Aktueller Forschungslauf

Stand: 2026-06-23 09:01:54

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\field_quiet_candidates\1-12_2025_5m_btcusdt_btc2025_field_quiet_05_2000.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `362` -> `362`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `1` -> `1`
- MCM-Rekopplung: `0.695981` -> `0.695231`
- MCM-Tragqualitaet: `0.51064` -> `0.511378`
- Sinnes-MCM-Kopplung: `0.844322` -> `0.843618`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00jaski, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_0pz659c, dio_104t4us, dio_14wjmk5, dio_155c3g6`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ja, dio_0h9h, dio_0l7p, dio_0m9z, dio_0pz6, dio_104t, dio_14wj, dio_155c`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `kippend`: `13`
- `stabil`: `1593`
- `tragend_unruhig`: `388`

Episodenzustaende:

- `field_carried`: `1994`

## Artefakte

- Debug: `debug\field_quiet_candidates_btc2025\btc2025_field_quiet_05`
- Memory: `bot_memory\field_quiet_candidates_btc2025\btc2025_field_quiet_05.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
