# Aktueller Forschungslauf

Stand: 2026-06-21 21:12:27

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_long_btc_2025_5m_stress_4000.csv`
- Kerzen: `4000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `477` -> `477`
- Episoden: `3994` -> `3994`
- geschriebene Episodenmemory: `25` -> `23`
- MCM-Rekopplung: `0.698865` -> `0.698237`
- MCM-Tragqualitaet: `0.521448` -> `0.522069`
- Sinnes-MCM-Kopplung: `0.844918` -> `0.844327`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_155c3g6, dio_17ctp0f, dio_1ewh8ej`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_155c, dio_17ct, dio_1ewh`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `11`
- `kippend`: `45`
- `stabil`: `3294`
- `tragend_unruhig`: `644`

Episodenzustaende:

- `field_carried`: `3983`
- `field_strained`: `11`

## Artefakte

- Debug: `debug\anchor_0e7qvj1_btc2025_5m_stress_4k`
- Memory: `memory\anchor_0e7qvj1_btc2025_5m_stress_4k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
