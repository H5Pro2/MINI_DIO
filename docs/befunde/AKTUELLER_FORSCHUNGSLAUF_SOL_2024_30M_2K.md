# Aktueller Forschungslauf

Stand: 2026-06-18 23:08:18

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_sol_2024_30m_test1_2000_SOLUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `1919` -> `1919`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `441` -> `441`
- MCM-Rekopplung: `0.600545` -> `0.600205`
- MCM-Tragqualitaet: `0.341133` -> `0.34142`
- Sinnes-MCM-Kopplung: `0.795731` -> `0.79543`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_02egy6u, dio_0efonve, dio_0wa7wjp, dio_18hull4, dio_1lnxjd9, dio_1ne0pgm, dio_1necyk9, dio_1o8r4am`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_02eg, dio_0efo, dio_0s6i, dio_0wa7, dio_1lnx, dio_1ne0, dio_1nec, dio_1o8r`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `70`
- `gespannt`: `362`
- `kippend`: `393`
- `rekoppelnd`: `3`
- `stabil`: `390`
- `tragend_unruhig`: `776`

Episodenzustaende:

- `field_carried`: `1629`
- `field_strained`: `365`

## Artefakte

- Debug: `debug\research_chain_sol_2024_30m_2k`
- Memory: `memory\research_chain_sol_2024_30m_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
