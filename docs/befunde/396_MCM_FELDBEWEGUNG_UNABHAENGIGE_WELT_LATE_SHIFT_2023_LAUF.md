# Aktueller Forschungslauf

Stand: 2026-06-20 09:43:40

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2023_late_shift_test_1000_5m_SOLUSDT.csv`
- Kerzen: `1000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `912` -> `912`
- Episoden: `994` -> `994`
- geschriebene Episodenmemory: `5` -> `5`
- MCM-Rekopplung: `0.644835` -> `0.644448`
- MCM-Tragqualitaet: `0.399768` -> `0.400129`
- Sinnes-MCM-Kopplung: `0.866547` -> `0.866192`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_0gyy2cc, dio_0p47bcy, dio_0pev589, dio_0s8oy1f, dio_0wq8i4b, dio_16j24f1, dio_183xqf7, dio_1yf7pdr`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_0gyy, dio_0p47, dio_0pev, dio_0s8o, dio_0wq8, dio_16j2, dio_183x, dio_1yf7`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `2`
- `kippend`: `24`
- `stabil`: `812`
- `tragend_unruhig`: `156`

Episodenzustaende:

- `field_carried`: `992`
- `field_strained`: `2`

## Artefakte

- Debug: `debug\regmemory_independent_late_shift_2023`
- Memory: `memory\regmemory_independent_late_shift_2023.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
