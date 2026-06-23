# Aktueller Forschungslauf

Stand: 2026-06-23 09:01:40

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\field_quiet_candidates\1-12_2025_5m_btcusdt_btc2025_field_quiet_03_2000.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `340` -> `340`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `3` -> `3`
- MCM-Rekopplung: `0.697676` -> `0.696932`
- MCM-Tragqualitaet: `0.512442` -> `0.513173`
- Sinnes-MCM-Kopplung: `0.847947` -> `0.847249`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_06s7dt1, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6, dio_17ctp0f`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_06s7, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c, dio_17ct`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `1`
- `kippend`: `8`
- `stabil`: `1655`
- `tragend_unruhig`: `330`

Episodenzustaende:

- `field_carried`: `1993`
- `field_strained`: `1`

## Artefakte

- Debug: `debug\field_quiet_candidates_btc2025\btc2025_field_quiet_03`
- Memory: `bot_memory\field_quiet_candidates_btc2025\btc2025_field_quiet_03.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
