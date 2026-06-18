# Aktueller Forschungslauf

Stand: 2026-06-18 23:13:55

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_sol_2025_30m_test1_2000_SOLUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `1920` -> `1920`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `434` -> `434`
- MCM-Rekopplung: `0.601254` -> `0.600912`
- MCM-Tragqualitaet: `0.343063` -> `0.343351`
- Sinnes-MCM-Kopplung: `0.796666` -> `0.796364`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_03t5leb, dio_05zorfo, dio_0a5lpk8, dio_0efonve, dio_0hs3wpy, dio_0u0su7t, dio_0ve8vsl, dio_17shqdn`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_03t5, dio_0a5l, dio_0efo, dio_0u0s, dio_0uy5, dio_0ve8, dio_17sh, dio_1ar1`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `61`
- `gespannt`: `402`
- `kippend`: `342`
- `stabil`: `396`
- `tragend_unruhig`: `793`

Episodenzustaende:

- `field_carried`: `1592`
- `field_strained`: `402`

## Artefakte

- Debug: `debug\research_chain_sol_2025_30m_2k`
- Memory: `memory\research_chain_sol_2025_30m_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
