# Aktueller Forschungslauf

Stand: 2026-06-18 19:10:47

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_quiet_segment_2025_stress_5m_SOLUSDT.csv`
- Kerzen: `100`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `94` -> `94`
- Episoden: `94` -> `94`
- geschriebene Episodenmemory: `1` -> `1`
- MCM-Rekopplung: `0.639676` -> `0.639352`
- MCM-Tragqualitaet: `0.378178` -> `0.378478`
- Sinnes-MCM-Kopplung: `0.847106` -> `0.846811`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_0agty7k, dio_0dk0mc8, dio_0svg9mh, dio_0tn1l2a, dio_1clyymx, dio_1j7db8i, dio_1ry2ty5, dio_1v4v288`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_0agt, dio_0dk0, dio_0svg, dio_0tn1, dio_1cly, dio_1j7d, dio_1ry2, dio_1v4v`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `kippend`: `3`
- `stabil`: `55`
- `tragend_unruhig`: `36`

Episodenzustaende:

- `field_carried`: `94`

## Artefakte

- Debug: `debug\research_chain_quiet_segment_2025_stress_01`
- Memory: `memory\research_chain_quiet_segment_2025_stress_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
