# Aktueller Forschungslauf

Stand: 2026-06-18 23:13:52

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_sol_2025_1h_test1_2000_SOLUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `1860` -> `1860`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `591` -> `591`
- MCM-Rekopplung: `0.589436` -> `0.589067`
- MCM-Tragqualitaet: `0.335186` -> `0.335489`
- Sinnes-MCM-Kopplung: `0.777196` -> `0.776872`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_03t5leb, dio_0ii5dg3, dio_0u0su7t, dio_0wy2411, dio_11cyi5u, dio_18hull4, dio_1e046mi, dio_1muqv00`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_03t5, dio_0ii5, dio_0u0s, dio_0wy2, dio_11cy, dio_18hu, dio_1e04, dio_1muq`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `76`
- `gespannt`: `584`
- `kippend`: `466`
- `rekoppelnd`: `3`
- `stabil`: `235`
- `tragend_unruhig`: `630`

Episodenzustaende:

- `field_carried`: `1407`
- `field_strained`: `587`

## Artefakte

- Debug: `debug\research_chain_sol_2025_1h_2k`
- Memory: `memory\research_chain_sol_2025_1h_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
