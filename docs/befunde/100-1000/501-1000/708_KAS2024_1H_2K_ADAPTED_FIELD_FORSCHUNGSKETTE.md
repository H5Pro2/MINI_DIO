# Aktueller Forschungslauf

Stand: 2026-06-22 12:47:10

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_kas_2024_1h_test1_2000_KASUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `356` -> `356`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `7` -> `7`
- MCM-Rekopplung: `0.693462` -> `0.692664`
- MCM-Tragqualitaet: `0.509991` -> `0.510778`
- Sinnes-MCM-Kopplung: `0.838178` -> `0.837428`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_0oc3c1g, dio_104t4us, dio_14wjmk5, dio_155c3g6`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_0oc3, dio_104t, dio_14wj, dio_155c`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `3`
- `kippend`: `19`
- `stabil`: `1533`
- `tragend_unruhig`: `439`

Episodenzustaende:

- `field_carried`: `1991`
- `field_strained`: `3`

## Artefakte

- Debug: `debug\adapted_time_kas_2024_1h_2k`
- Memory: `bot_memory\adapted_time_kas_2024_1h_2k.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
