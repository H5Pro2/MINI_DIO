# Aktueller Forschungslauf

Stand: 2026-06-23 08:50:28

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\field_quiet_candidates\1-12_2025_5m_solusdt_sol2025_field_quiet_03_2000.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `329` -> `329`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `3` -> `3`
- MCM-Rekopplung: `0.693875` -> `0.693038`
- MCM-Tragqualitaet: `0.509887` -> `0.510715`
- Sinnes-MCM-Kopplung: `0.839302` -> `0.838514`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00jaski, dio_0g2rowx, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_0pz659c, dio_104t4us, dio_155c3g6`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ja, dio_0g2r, dio_0h9h, dio_0l7p, dio_0m9z, dio_0pz6, dio_104t, dio_155c`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `1`
- `kippend`: `10`
- `stabil`: `1474`
- `tragend_unruhig`: `509`

Episodenzustaende:

- `field_carried`: `1993`
- `field_strained`: `1`

## Artefakte

- Debug: `debug\field_quiet_candidates_sol2025\sol2025_field_quiet_03`
- Memory: `bot_memory\field_quiet_candidates_sol2025\sol2025_field_quiet_03.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
