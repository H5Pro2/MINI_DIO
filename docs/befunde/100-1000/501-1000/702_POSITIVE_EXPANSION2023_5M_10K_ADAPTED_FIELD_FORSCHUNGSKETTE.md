# Aktueller Forschungslauf

Stand: 2026-06-22 12:33:50

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2023_positive_expansion_10k_5m_SOLUSDT.csv`
- Kerzen: `10000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `668` -> `668`
- Episoden: `9994` -> `9994`
- geschriebene Episodenmemory: `12` -> `12`
- MCM-Rekopplung: `0.705378` -> `0.704915`
- MCM-Tragqualitaet: `0.536223` -> `0.536685`
- Sinnes-MCM-Kopplung: `0.841914` -> `0.841476`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6, dio_1lsuk2g`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c, dio_1lsu`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `4`
- `kippend`: `78`
- `stabil`: `7910`
- `tragend_unruhig`: `2002`

Episodenzustaende:

- `field_carried`: `9990`
- `field_strained`: `4`

## Artefakte

- Debug: `debug\adapted_state_positive_expansion_2023_5m_10k`
- Memory: `bot_memory\adapted_state_positive_expansion_2023_5m_10k.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
