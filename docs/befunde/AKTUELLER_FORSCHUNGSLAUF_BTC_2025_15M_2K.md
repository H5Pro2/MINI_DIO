# Aktueller Forschungslauf

Stand: 2026-06-18 22:53:04

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_btc_2025_15m_test1_2000_BTCUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `1726` -> `1726`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `125` -> `125`
- MCM-Rekopplung: `0.631779` -> `0.631429`
- MCM-Tragqualitaet: `0.363073` -> `0.363392`
- Sinnes-MCM-Kopplung: `0.83537` -> `0.835053`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_06g1s0o, dio_081d3sf, dio_0bqhlnm, dio_0dttdhz, dio_0g20gum, dio_11q4ueg, dio_1egx9si, dio_1fhx1gw`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_06g1, dio_081d, dio_0bqh, dio_0dtt, dio_0g20, dio_11q4, dio_1egx, dio_1fhx`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `18`
- `gespannt`: `79`
- `kippend`: `92`
- `stabil`: `1023`
- `tragend_unruhig`: `782`

Episodenzustaende:

- `field_carried`: `1915`
- `field_strained`: `79`

## Artefakte

- Debug: `debug\research_chain_btc_2025_15m_2k`
- Memory: `memory\research_chain_btc_2025_15m_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
