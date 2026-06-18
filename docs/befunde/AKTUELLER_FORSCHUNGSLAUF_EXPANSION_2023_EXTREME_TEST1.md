# Aktueller Forschungslauf

Stand: 2026-06-18 21:15:03

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2023_extreme_expansion_test1_1000_5m_SOLUSDT.csv`
- Kerzen: `1000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `947` -> `947`
- Episoden: `994` -> `994`
- geschriebene Episodenmemory: `87` -> `87`
- MCM-Rekopplung: `0.623338` -> `0.623022`
- MCM-Tragqualitaet: `0.352757` -> `0.353039`
- Sinnes-MCM-Kopplung: `0.829906` -> `0.829622`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_01x2707, dio_0f10dj6, dio_14n0zjd, dio_15uox40, dio_1epgj1e, dio_1jnclbr, dio_1mviffh, dio_1pmi8g1`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_01x2, dio_0f10, dio_14n0, dio_15uo, dio_1epg, dio_1jnc, dio_1mvi, dio_1pmi`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `11`
- `gespannt`: `60`
- `kippend`: `69`
- `stabil`: `466`
- `tragend_unruhig`: `388`

Episodenzustaende:

- `field_carried`: `934`
- `field_strained`: `60`

## Artefakte

- Debug: `debug\research_chain_expansion_2023_extreme_test1`
- Memory: `memory\research_chain_expansion_2023_extreme_test1_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
