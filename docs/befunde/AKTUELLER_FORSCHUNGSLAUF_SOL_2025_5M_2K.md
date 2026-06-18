# Aktueller Forschungslauf

Stand: 2026-06-18 23:10:50

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_sol_2025_5m_test1_2000_SOLUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `1680` -> `1680`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `55` -> `55`
- MCM-Rekopplung: `0.636861` -> `0.636504`
- MCM-Tragqualitaet: `0.365316` -> `0.365647`
- Sinnes-MCM-Kopplung: `0.838817` -> `0.838491`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_07y1h7q, dio_0la1gim, dio_0lm0hoi, dio_16rb7op, dio_17jjxav, dio_1egx9si, dio_1rsllrx, dio_1xx0wlt`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_07y1, dio_0la1, dio_0lm0, dio_16rb, dio_17jj, dio_1egx, dio_1rsl, dio_1xx0`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `19`
- `gespannt`: `28`
- `kippend`: `35`
- `stabil`: `1145`
- `tragend_unruhig`: `767`

Episodenzustaende:

- `field_carried`: `1966`
- `field_strained`: `28`

## Artefakte

- Debug: `debug\research_chain_sol_2025_5m_2k`
- Memory: `memory\research_chain_sol_2025_5m_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
