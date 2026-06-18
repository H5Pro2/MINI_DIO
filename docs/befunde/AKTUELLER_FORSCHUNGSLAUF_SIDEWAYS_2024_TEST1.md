# Aktueller Forschungslauf

Stand: 2026-06-18 21:44:24

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2024_moderate_sideways_test1_1000_5m_SOLUSDT.csv`
- Kerzen: `1000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `922` -> `922`
- Episoden: `994` -> `994`
- geschriebene Episodenmemory: `43` -> `43`
- MCM-Rekopplung: `0.630871` -> `0.630554`
- MCM-Tragqualitaet: `0.358991` -> `0.35928`
- Sinnes-MCM-Kopplung: `0.835003` -> `0.834716`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_050rb29, dio_07y1h7q, dio_0c5pqze, dio_14vuuvy, dio_17crgiy, dio_17whstn, dio_1ozs4xu, dio_1w5jqhx`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_050r, dio_07y1, dio_0c5p, dio_14vu, dio_17cr, dio_17wh, dio_1ozs, dio_1w5j`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `11`
- `gespannt`: `24`
- `kippend`: `28`
- `rekoppelnd`: `1`
- `stabil`: `515`
- `tragend_unruhig`: `415`

Episodenzustaende:

- `field_carried`: `969`
- `field_strained`: `25`

## Artefakte

- Debug: `debug\research_chain_sideways_2024_test1`
- Memory: `memory\research_chain_sideways_2024_test1_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
