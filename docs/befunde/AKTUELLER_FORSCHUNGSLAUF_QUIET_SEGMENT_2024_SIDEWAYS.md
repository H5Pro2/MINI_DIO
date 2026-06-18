# Aktueller Forschungslauf

Stand: 2026-06-18 19:41:37

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_quiet_segment_2024_sideways_5m_SOLUSDT.csv`
- Kerzen: `100`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `91` -> `91`
- Episoden: `94` -> `94`
- geschriebene Episodenmemory: `5` -> `5`
- MCM-Rekopplung: `0.63996` -> `0.639653`
- MCM-Tragqualitaet: `0.364895` -> `0.365178`
- Sinnes-MCM-Kopplung: `0.841948` -> `0.841669`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_0dj8kpz, dio_0j9avio, dio_0v269si, dio_0yixz0z, dio_1dfft2z, dio_1l6ac6k, dio_1udwjmb, dio_1utxco6`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_0dj8, dio_0j9a, dio_0v26, dio_0yix, dio_1dff, dio_1l6a, dio_1udw, dio_1utx`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `2`
- `stabil`: `59`
- `tragend_unruhig`: `33`

Episodenzustaende:

- `field_carried`: `92`
- `field_strained`: `2`

## Artefakte

- Debug: `debug\research_chain_quiet_segment_2024_sideways_01`
- Memory: `memory\research_chain_quiet_segment_2024_sideways_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
