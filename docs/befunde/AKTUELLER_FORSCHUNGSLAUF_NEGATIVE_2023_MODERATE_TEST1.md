# Aktueller Forschungslauf

Stand: 2026-06-18 21:48:42

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2023_moderate_negative_test1_1000_5m_SOLUSDT.csv`
- Kerzen: `1000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `932` -> `932`
- Episoden: `994` -> `994`
- geschriebene Episodenmemory: `45` -> `45`
- MCM-Rekopplung: `0.631387` -> `0.631065`
- MCM-Tragqualitaet: `0.36175` -> `0.362044`
- Sinnes-MCM-Kopplung: `0.836736` -> `0.836444`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_077izt7, dio_0c3o0fd, dio_0chknce, dio_0nv8zkr, dio_165gcgx, dio_1ckin4c, dio_1vcmi04, dio_1xx0wlt`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_0c3o, dio_0chk, dio_0ft1, dio_0j34, dio_0nv8, dio_165g, dio_1vcm, dio_1xx0`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `7`
- `gespannt`: `26`
- `kippend`: `39`
- `stabil`: `553`
- `tragend_unruhig`: `369`

Episodenzustaende:

- `field_carried`: `968`
- `field_strained`: `26`

## Artefakte

- Debug: `debug\research_chain_negative_2023_moderate_test1`
- Memory: `memory\research_chain_negative_2023_moderate_test1_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
