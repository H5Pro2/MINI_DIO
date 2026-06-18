# Aktueller Forschungslauf

Stand: 2026-06-18 19:41:37

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_stress_segment_2024_sideways_5m_SOLUSDT.csv`
- Kerzen: `100`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `93` -> `93`
- Episoden: `94` -> `94`
- geschriebene Episodenmemory: `5` -> `5`
- MCM-Rekopplung: `0.629888` -> `0.629551`
- MCM-Tragqualitaet: `0.369351` -> `0.369655`
- Sinnes-MCM-Kopplung: `0.842422` -> `0.842118`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_02vdywx, dio_06kqbqm, dio_0bqhlnm, dio_0n6q38j, dio_1ew3c1p, dio_1jhvv9u, dio_1lbwuhe, dio_1lvwjn2`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_02vd, dio_06kq, dio_0bqh, dio_0n6q, dio_1ew3, dio_1jhv, dio_1lbw, dio_1lvw`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `5`
- `kippend`: `4`
- `stabil`: `55`
- `tragend_unruhig`: `30`

Episodenzustaende:

- `field_carried`: `89`
- `field_strained`: `5`

## Artefakte

- Debug: `debug\research_chain_stress_segment_2024_sideways_01`
- Memory: `memory\research_chain_stress_segment_2024_sideways_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
