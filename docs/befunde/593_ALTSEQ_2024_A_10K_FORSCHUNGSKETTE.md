# Aktueller Forschungslauf

Stand: 2026-06-21 23:35:06

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2024_altseq_a_10k_5m_SOLUSDT.csv`
- Kerzen: `10000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `647` -> `647`
- Episoden: `9994` -> `9994`
- geschriebene Episodenmemory: `25` -> `25`
- MCM-Rekopplung: `0.703785` -> `0.703361`
- MCM-Tragqualitaet: `0.534501` -> `0.534924`
- Sinnes-MCM-Kopplung: `0.844358` -> `0.843957`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6, dio_1pij39c`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c, dio_1pij`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `12`
- `kippend`: `72`
- `stabil`: `8244`
- `tragend_unruhig`: `1666`

Episodenzustaende:

- `field_carried`: `9982`
- `field_strained`: `12`

## Artefakte

- Debug: `debug\altseq_2024_a_10k`
- Memory: `memory\altseq_2024_a_10k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
