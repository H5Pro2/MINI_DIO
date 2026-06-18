# Aktueller Forschungslauf

Stand: 2026-06-18 21:33:42

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2023_positive_expansion_10k_5m_SOLUSDT.csv`
- Kerzen: `10000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `7733` -> `7733`
- Episoden: `9994` -> `9994`
- geschriebene Episodenmemory: `575` -> `571`
- MCM-Rekopplung: `0.632877` -> `0.632556`
- MCM-Tragqualitaet: `0.367042` -> `0.367342`
- Sinnes-MCM-Kopplung: `0.833248` -> `0.832954`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_01ufvm3, dio_0lm0hoi, dio_0nv8zkr, dio_14m381g, dio_1mhjaxf, dio_1q7hcfy, dio_1qkm3eo, dio_1xx0wlt`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_01uf, dio_0j34, dio_0lm0, dio_0nv8, dio_14m3, dio_1mhj, dio_1qkm, dio_1xx0`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `99`
- `gespannt`: `364`
- `kippend`: `491`
- `rekoppelnd`: `2`
- `stabil`: `5399`
- `tragend_unruhig`: `3639`

Episodenzustaende:

- `field_carried`: `9628`
- `field_strained`: `366`

## Artefakte

- Debug: `debug\research_chain_expansion_2023_positive_10k`
- Memory: `memory\research_chain_expansion_2023_positive_10k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
