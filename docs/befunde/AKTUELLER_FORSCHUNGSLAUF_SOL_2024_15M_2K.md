# Aktueller Forschungslauf

Stand: 2026-06-18 23:05:25

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_sol_2024_15m_test1_2000_SOLUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `1921` -> `1921`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `311` -> `309`
- MCM-Rekopplung: `0.606871` -> `0.606542`
- MCM-Tragqualitaet: `0.343396` -> `0.343678`
- Sinnes-MCM-Kopplung: `0.806095` -> `0.805802`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_03t5leb, dio_07wo1u1, dio_0fknuty, dio_0gdwqm4, dio_0kfp7vv, dio_0l8vpb2, dio_18hull4, dio_19xykgo`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_03t5, dio_07wo, dio_0fkn, dio_0gdw, dio_0kfp, dio_0l8v, dio_18hu, dio_19xy`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `47`
- `gespannt`: `263`
- `kippend`: `320`
- `rekoppelnd`: `3`
- `stabil`: `470`
- `tragend_unruhig`: `891`

Episodenzustaende:

- `field_carried`: `1728`
- `field_strained`: `266`

## Artefakte

- Debug: `debug\research_chain_sol_2024_15m_2k`
- Memory: `memory\research_chain_sol_2024_15m_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
