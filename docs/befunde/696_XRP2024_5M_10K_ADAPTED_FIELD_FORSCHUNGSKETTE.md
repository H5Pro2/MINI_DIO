# Aktueller Forschungslauf

Stand: 2026-06-22 12:27:19

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_xrp_2024_5m_10k_XRPUSDT.csv`
- Kerzen: `10000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `673` -> `673`
- Episoden: `9994` -> `9994`
- geschriebene Episodenmemory: `12` -> `10`
- MCM-Rekopplung: `0.705845` -> `0.705409`
- MCM-Tragqualitaet: `0.53719` -> `0.537625`
- Sinnes-MCM-Kopplung: `0.842293` -> `0.841881`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6, dio_1q85toi`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c, dio_1q85`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `3`
- `kippend`: `79`
- `stabil`: `7955`
- `tragend_unruhig`: `1957`

Episodenzustaende:

- `field_carried`: `9991`
- `field_strained`: `3`

## Artefakte

- Debug: `debug\adapted_field_xrp_2024_5m_10k`
- Memory: `bot_memory\adapted_field_xrp_2024_5m_10k.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
