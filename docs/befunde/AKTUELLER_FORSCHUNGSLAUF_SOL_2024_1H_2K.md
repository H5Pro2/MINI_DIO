# Aktueller Forschungslauf

Stand: 2026-06-18 23:08:14

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_sol_2024_1h_test1_2000_SOLUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `1854` -> `1854`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `643` -> `643`
- MCM-Rekopplung: `0.587399` -> `0.587027`
- MCM-Tragqualitaet: `0.333131` -> `0.333433`
- Sinnes-MCM-Kopplung: `0.774675` -> `0.77435`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_03t5leb, dio_052bfgf, dio_0qy1hrq, dio_0r8biob, dio_0sd0hkm, dio_0wc3srp, dio_1oeqrt3, dio_1yc59r0`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_03t5, dio_052b, dio_0qy1, dio_0r8b, dio_0sd0, dio_0wc3, dio_1oeq, dio_1yc5`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `71`
- `gespannt`: `625`
- `kippend`: `475`
- `rekoppelnd`: `5`
- `stabil`: `213`
- `tragend_unruhig`: `605`

Episodenzustaende:

- `field_carried`: `1364`
- `field_strained`: `630`

## Artefakte

- Debug: `debug\research_chain_sol_2024_1h_2k`
- Memory: `memory\research_chain_sol_2024_1h_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
