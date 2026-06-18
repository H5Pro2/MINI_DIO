# Aktueller Forschungslauf

Stand: 2026-06-18 22:40:49

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_btc_2025_5m_test1_2000_BTCUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `1440` -> `1440`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `87` -> `87`
- MCM-Rekopplung: `0.638796` -> `0.63838`
- MCM-Tragqualitaet: `0.368136` -> `0.368524`
- Sinnes-MCM-Kopplung: `0.828092` -> `0.827711`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_06wtifz, dio_0c5pqze, dio_0dttdhz, dio_0f10dj6, dio_0mjo3h9, dio_1a1178d, dio_1bfooar, dio_1lb5y78`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_06wt, dio_0c5p, dio_0f10, dio_0mjo, dio_0p04, dio_1a11, dio_1bfo, dio_1lb5`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `20`
- `gespannt`: `44`
- `kippend`: `46`
- `stabil`: `1139`
- `tragend_unruhig`: `745`

Episodenzustaende:

- `field_carried`: `1950`
- `field_strained`: `44`

## Artefakte

- Debug: `debug\research_chain_btc_2025_5m_2k`
- Memory: `memory\research_chain_btc_2025_5m_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
