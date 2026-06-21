# Aktueller Forschungslauf

Stand: 2026-06-21 21:28:40

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_kas_2024_5m_test1_2000_KASUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `350` -> `350`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `9` -> `9`
- MCM-Rekopplung: `0.692998` -> `0.692242`
- MCM-Tragqualitaet: `0.508703` -> `0.50945`
- Sinnes-MCM-Kopplung: `0.842964` -> `0.842252`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00jaski, dio_00lyjkf, dio_0h9h06p, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6, dio_1ewh8ej`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ja, dio_00ly, dio_0h9h, dio_0m9z, dio_104t, dio_14wj, dio_155c, dio_1ewh`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `4`
- `kippend`: `20`
- `stabil`: `1612`
- `tragend_unruhig`: `358`

Episodenzustaende:

- `field_carried`: `1990`
- `field_strained`: `4`

## Artefakte

- Debug: `debug\cross_anchor_kas2024_5m_2k`
- Memory: `memory\cross_anchor_kas2024_5m_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
