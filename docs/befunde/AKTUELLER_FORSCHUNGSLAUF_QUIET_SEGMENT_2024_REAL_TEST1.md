# Aktueller Forschungslauf

Stand: 2026-06-18 19:01:16

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_quiet_segment_2024_real_test1_5m_SOLUSDT.csv`
- Kerzen: `100`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `94` -> `94`
- Episoden: `94` -> `94`
- geschriebene Episodenmemory: `5` -> `5`
- MCM-Rekopplung: `0.631027` -> `0.630744`
- MCM-Tragqualitaet: `0.361769` -> `0.362024`
- Sinnes-MCM-Kopplung: `0.840973` -> `0.840718`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_0bqhlnm, dio_0gh72cb, dio_11cbit0, dio_13t9hu2, dio_13u4b3n, dio_1dbjuxs, dio_1gepwh7, dio_1jkutel`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_0bqh, dio_0gh7, dio_11cb, dio_13t9, dio_13u4, dio_1dbj, dio_1gep, dio_1jku`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `1`
- `gespannt`: `2`
- `kippend`: `3`
- `stabil`: `53`
- `tragend_unruhig`: `35`

Episodenzustaende:

- `field_carried`: `92`
- `field_strained`: `2`

## Artefakte

- Debug: `debug\research_chain_quiet_segment_2024_real_test1_01`
- Memory: `memory\research_chain_quiet_segment_2024_real_test1_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
