# Aktueller Forschungslauf

Stand: 2026-06-21 23:55:34

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_paxg_2025_5m_10k_PAXGUSDT.csv`
- Kerzen: `10000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `593` -> `593`
- Episoden: `9994` -> `9994`
- geschriebene Episodenmemory: `23` -> `23`
- MCM-Rekopplung: `0.714382` -> `0.713988`
- MCM-Tragqualitaet: `0.54102` -> `0.541415`
- Sinnes-MCM-Kopplung: `0.85609` -> `0.855717`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00lyjkf, dio_0h9h06p, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6, dio_1fllaqz, dio_1u5il5a`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ly, dio_0h9h, dio_0m9z, dio_104t, dio_14wj, dio_155c, dio_1fll, dio_1u5i`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `10`
- `kippend`: `62`
- `stabil`: `8719`
- `tragend_unruhig`: `1203`

Episodenzustaende:

- `field_carried`: `9984`
- `field_strained`: `10`

## Artefakte

- Debug: `debug\paxg_2025_5m_10k`
- Memory: `memory\paxg_2025_5m_10k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
