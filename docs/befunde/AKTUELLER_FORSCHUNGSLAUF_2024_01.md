# Aktueller Forschungslauf

Stand: 2026-06-18 16:44:08

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2024_real_test1_1000_5m_SOLUSDT.csv`
- Kerzen: `1000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `967` -> `967`
- Episoden: `994` -> `994`
- geschriebene Episodenmemory: `81` -> `81`
- MCM-Rekopplung: `0.622613` -> `0.622297`
- MCM-Tragqualitaet: `0.357809` -> `0.358091`
- Sinnes-MCM-Kopplung: `0.829571` -> `0.829287`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_0epwh5e, dio_0jik3rd, dio_0tyz3xh, dio_134jty4, dio_165gcgx, dio_1ccca5j, dio_1k0rwi1, dio_1pmi8g1`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_0epw, dio_0jik, dio_0tyz, dio_134j, dio_165g, dio_1ccc, dio_1k0r, dio_1pmi`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `11`
- `gespannt`: `60`
- `kippend`: `68`
- `rekoppelnd`: `2`
- `stabil`: `400`
- `tragend_unruhig`: `453`

Episodenzustaende:

- `field_carried`: `932`
- `field_strained`: `62`

## Artefakte

- Debug: `debug\research_chain_2024_01`
- Memory: `memory\research_chain_2024_01.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
