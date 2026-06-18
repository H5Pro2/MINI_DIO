# Aktueller Forschungslauf

Stand: 2026-06-18 18:48:04

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_stress_segment_2023_test4_5m_SOLUSDT.csv`
- Kerzen: `100`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `94` -> `94`
- Episoden: `94` -> `94`
- geschriebene Episodenmemory: `23` -> `23`
- MCM-Rekopplung: `0.597217` -> `0.596927`
- MCM-Tragqualitaet: `0.337918` -> `0.338154`
- Sinnes-MCM-Kopplung: `0.79821` -> `0.797956`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_0kkk9tz, dio_0qajh9d, dio_0skkwmh, dio_0sxbo1m, dio_0uv2mfc, dio_1ceogz1, dio_1o11ilq, dio_1qmksr6`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_0kkk, dio_0qaj, dio_0skk, dio_0sxb, dio_0uv2, dio_1ceo, dio_1o11, dio_1qmk`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `4`
- `gespannt`: `25`
- `kippend`: `16`
- `stabil`: `13`
- `tragend_unruhig`: `36`

Episodenzustaende:

- `field_carried`: `69`
- `field_strained`: `25`

## Artefakte

- Debug: `debug\research_chain_stress_segment_2023_test4_01`
- Memory: `memory\research_chain_stress_segment_2023_test4_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
