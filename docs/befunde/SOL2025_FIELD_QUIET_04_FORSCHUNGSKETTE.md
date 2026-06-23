# Aktueller Forschungslauf

Stand: 2026-06-23 08:50:35

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\field_quiet_candidates\1-12_2025_5m_solusdt_sol2025_field_quiet_04_2000.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `345` -> `345`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `3` -> `3`
- MCM-Rekopplung: `0.694886` -> `0.694066`
- MCM-Tragqualitaet: `0.51038` -> `0.511184`
- Sinnes-MCM-Kopplung: `0.841619` -> `0.840851`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6, dio_1ewh8ej`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c, dio_1ewh`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `1`
- `kippend`: `14`
- `stabil`: `1574`
- `tragend_unruhig`: `405`

Episodenzustaende:

- `field_carried`: `1993`
- `field_strained`: `1`

## Artefakte

- Debug: `debug\field_quiet_candidates_sol2025\sol2025_field_quiet_04`
- Memory: `bot_memory\field_quiet_candidates_sol2025\sol2025_field_quiet_04.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
