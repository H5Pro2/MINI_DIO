# Aktueller Forschungslauf

Stand: 2026-06-22 01:04:58

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_xrp_2025_5m_10k_XRPUSDT.csv`
- Kerzen: `10000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `679` -> `679`
- Episoden: `9994` -> `9994`
- geschriebene Episodenmemory: `35` -> `35`
- MCM-Rekopplung: `0.704777` -> `0.704364`
- MCM-Tragqualitaet: `0.535899` -> `0.536309`
- Sinnes-MCM-Kopplung: `0.845653` -> `0.845264`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6, dio_1pij39c`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c, dio_1pij`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `17`
- `kippend`: `86`
- `stabil`: `8375`
- `tragend_unruhig`: `1516`

Episodenzustaende:

- `field_carried`: `9977`
- `field_strained`: `17`

## Artefakte

- Debug: `debug\xrp_2025_5m_10k`
- Memory: `memory\xrp_2025_5m_10k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
