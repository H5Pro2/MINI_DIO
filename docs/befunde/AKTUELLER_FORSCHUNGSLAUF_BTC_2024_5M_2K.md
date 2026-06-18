# Aktueller Forschungslauf

Stand: 2026-06-18 22:33:29

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_btc_2024_5m_test1_2000_BTCUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `1576` -> `1576`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `63` -> `63`
- MCM-Rekopplung: `0.636965` -> `0.636577`
- MCM-Tragqualitaet: `0.36575` -> `0.366108`
- Sinnes-MCM-Kopplung: `0.833615` -> `0.833261`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_03a3gb7, dio_07y1h7q, dio_0bqhlnm, dio_0c5pqze, dio_0nv8zkr, dio_0sf3qm1, dio_0xok66v, dio_1a4a9da`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_03a3, dio_07y1, dio_0bqh, dio_0c5p, dio_0nv8, dio_0sf3, dio_0xok, dio_1a4a`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `24`
- `gespannt`: `42`
- `kippend`: `48`
- `stabil`: `1130`
- `tragend_unruhig`: `750`

Episodenzustaende:

- `field_carried`: `1952`
- `field_strained`: `42`

## Artefakte

- Debug: `debug\research_chain_btc_2024_5m_2k`
- Memory: `memory\research_chain_btc_2024_5m_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
