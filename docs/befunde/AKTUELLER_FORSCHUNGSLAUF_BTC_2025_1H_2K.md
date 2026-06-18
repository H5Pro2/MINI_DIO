# Aktueller Forschungslauf

Stand: 2026-06-18 22:41:22

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_btc_2025_1h_test1_2000_BTCUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `1908` -> `1908`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `349` -> `347`
- MCM-Rekopplung: `0.611547` -> `0.61124`
- MCM-Tragqualitaet: `0.346753` -> `0.347018`
- Sinnes-MCM-Kopplung: `0.812647` -> `0.812374`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_02thfip, dio_03t5leb, dio_081d3sf, dio_0efonve, dio_0gw2xjz, dio_0kr1ewa, dio_1ne0pgm, dio_1rbifpo`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_02th, dio_081d, dio_0efo, dio_0gw2, dio_0kr1, dio_0uy5, dio_1ne0, dio_1rbi`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `41`
- `gespannt`: `275`
- `kippend`: `248`
- `rekoppelnd`: `7`
- `stabil`: `578`
- `tragend_unruhig`: `845`

Episodenzustaende:

- `field_carried`: `1712`
- `field_strained`: `282`

## Artefakte

- Debug: `debug\research_chain_btc_2025_1h_2k`
- Memory: `memory\research_chain_btc_2025_1h_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
