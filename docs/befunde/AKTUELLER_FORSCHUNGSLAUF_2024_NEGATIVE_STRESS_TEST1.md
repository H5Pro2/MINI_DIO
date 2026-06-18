# Aktueller Forschungslauf

Stand: 2026-06-18 18:00:20

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2024_negative_stress_test1_1000_5m_SOLUSDT.csv`
- Kerzen: `1000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `923` -> `923`
- Episoden: `994` -> `994`
- geschriebene Episodenmemory: `33` -> `33`
- MCM-Rekopplung: `0.631994` -> `0.631676`
- MCM-Tragqualitaet: `0.361353` -> `0.361645`
- Sinnes-MCM-Kopplung: `0.838455` -> `0.838166`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_0bmwz7u, dio_0e6t3ev, dio_0la1gim, dio_165gcgx, dio_18sw3vz, dio_1k6ccrx, dio_1xx0wlt, dio_1yvra14`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_0bmw, dio_0e6t, dio_0la1, dio_165g, dio_18sw, dio_1k6c, dio_1xx0, dio_1yvr`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `11`
- `gespannt`: `18`
- `kippend`: `35`
- `stabil`: `509`
- `tragend_unruhig`: `421`

Episodenzustaende:

- `field_carried`: `976`
- `field_strained`: `18`

## Artefakte

- Debug: `debug\research_chain_2024_negative_stress_test1_01`
- Memory: `memory\research_chain_2024_negative_stress_test1_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
