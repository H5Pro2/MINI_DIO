# Aktueller Forschungslauf

Stand: 2026-06-23 13:21:04

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_real_sequence_break_btc_2025_5m_2000.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `344` -> `344`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `5` -> `3`
- MCM-Rekopplung: `0.695645` -> `0.694857`
- MCM-Tragqualitaet: `0.511813` -> `0.512588`
- Sinnes-MCM-Kopplung: `0.84273` -> `0.84199`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6, dio_17ctp0f`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c, dio_17ct`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `1`
- `kippend`: `18`
- `stabil`: `1607`
- `tragend_unruhig`: `368`

Episodenzustaende:

- `field_carried`: `1993`
- `field_strained`: `1`

## Artefakte

- Debug: `debug\memory_architecture_action_store_check`
- Memory: `bot_memory\memory_architecture_action_store_check.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
