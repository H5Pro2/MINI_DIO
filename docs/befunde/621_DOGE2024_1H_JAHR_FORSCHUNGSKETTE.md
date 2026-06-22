# Aktueller Forschungslauf

Stand: 2026-06-22 00:27:35

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_doge_2024_1h_10k_DOGEUSDT.csv`
- Kerzen: `8784`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `655` -> `655`
- Episoden: `8778` -> `8778`
- geschriebene Episodenmemory: `35` -> `35`
- MCM-Rekopplung: `0.704027` -> `0.703611`
- MCM-Tragqualitaet: `0.534395` -> `0.534807`
- Sinnes-MCM-Kopplung: `0.844539` -> `0.844147`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00jaski, dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ja, dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `18`
- `kippend`: `96`
- `stabil`: `7230`
- `tragend_unruhig`: `1434`

Episodenzustaende:

- `field_carried`: `8760`
- `field_strained`: `18`

## Artefakte

- Debug: `debug\doge_2024_1h_year`
- Memory: `memory\doge_2024_1h_year_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
