# Aktueller Forschungslauf

Stand: 2026-06-18 19:01:16

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_stress_segment_2024_real_test1_5m_SOLUSDT.csv`
- Kerzen: `100`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `92` -> `92`
- Episoden: `94` -> `94`
- geschriebene Episodenmemory: `23` -> `23`
- MCM-Rekopplung: `0.601985` -> `0.601652`
- MCM-Tragqualitaet: `0.355754` -> `0.356035`
- Sinnes-MCM-Kopplung: `0.800758` -> `0.800464`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00cfh2t, dio_0e5c15c, dio_176dvgq, dio_1cgk5ac, dio_1felqxw, dio_1kos4qn, dio_1ne0pgm, dio_1un2v0m`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00cf, dio_0e5c, dio_176d, dio_1cgk, dio_1fel, dio_1kos, dio_1ne0, dio_1un2`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `3`
- `gespannt`: `22`
- `kippend`: `18`
- `stabil`: `18`
- `tragend_unruhig`: `33`

Episodenzustaende:

- `field_carried`: `72`
- `field_strained`: `22`

## Artefakte

- Debug: `debug\research_chain_stress_segment_2024_real_test1_01`
- Memory: `memory\research_chain_stress_segment_2024_real_test1_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
