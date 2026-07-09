# Aktueller Forschungslauf

Stand: 2026-06-22 12:27:18

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_doge_2024_5m_10k_DOGEUSDT.csv`
- Kerzen: `10000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `666` -> `666`
- Episoden: `9994` -> `9994`
- geschriebene Episodenmemory: `11` -> `11`
- MCM-Rekopplung: `0.705392` -> `0.704956`
- MCM-Tragqualitaet: `0.536767` -> `0.537202`
- Sinnes-MCM-Kopplung: `0.841729` -> `0.841317`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6, dio_17ctp0f`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c, dio_17ct`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `4`
- `kippend`: `65`
- `stabil`: `7958`
- `tragend_unruhig`: `1967`

Episodenzustaende:

- `field_carried`: `9990`
- `field_strained`: `4`

## Artefakte

- Debug: `debug\adapted_field_doge_2024_5m_10k`
- Memory: `bot_memory\adapted_field_doge_2024_5m_10k.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
