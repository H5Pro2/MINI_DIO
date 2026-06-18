# Aktueller Forschungslauf

Stand: 2026-06-18 23:05:22

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_sol_2024_5m_test1_2000_SOLUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `1887` -> `1887`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `149` -> `149`
- MCM-Rekopplung: `0.623103` -> `0.622776`
- MCM-Tragqualitaet: `0.357745` -> `0.358038`
- Sinnes-MCM-Kopplung: `0.829327` -> `0.829033`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_09ir2g8, dio_0bqhlnm, dio_0jik3rd, dio_0tyz3xh, dio_165gcgx, dio_1ccca5j, dio_1k0rwi1, dio_1qh29qz`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_0bqh, dio_0jik, dio_0tyz, dio_12du, dio_165g, dio_1ccc, dio_1k0r, dio_1qh2`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `23`
- `gespannt`: `102`
- `kippend`: `137`
- `rekoppelnd`: `3`
- `stabil`: `811`
- `tragend_unruhig`: `918`

Episodenzustaende:

- `field_carried`: `1889`
- `field_strained`: `105`

## Artefakte

- Debug: `debug\research_chain_sol_2024_5m_2k`
- Memory: `memory\research_chain_sol_2024_5m_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
