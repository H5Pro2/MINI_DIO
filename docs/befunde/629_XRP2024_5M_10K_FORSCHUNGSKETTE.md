# Aktueller Forschungslauf

Stand: 2026-06-22 01:05:01

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
- Unique Syntaxsymbole: `685` -> `685`
- Episoden: `9994` -> `9994`
- geschriebene Episodenmemory: `39` -> `39`
- MCM-Rekopplung: `0.704621` -> `0.704198`
- MCM-Tragqualitaet: `0.535223` -> `0.535644`
- Sinnes-MCM-Kopplung: `0.844817` -> `0.844417`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00jaski, dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ja, dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `19`
- `kippend`: `120`
- `stabil`: `8275`
- `tragend_unruhig`: `1580`

Episodenzustaende:

- `field_carried`: `9975`
- `field_strained`: `19`

## Artefakte

- Debug: `debug\xrp_2024_5m_10k`
- Memory: `memory\xrp_2024_5m_10k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
