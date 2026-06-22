# Aktueller Forschungslauf

Stand: 2026-06-21 23:35:52

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2025_altseq_a_10k_5m_SOLUSDT.csv`
- Kerzen: `10000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `659` -> `659`
- Episoden: `9994` -> `9994`
- geschriebene Episodenmemory: `49` -> `49`
- MCM-Rekopplung: `0.70367` -> `0.703242`
- MCM-Tragqualitaet: `0.534942` -> `0.535368`
- Sinnes-MCM-Kopplung: `0.842975` -> `0.842571`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00jaski, dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ja, dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `24`
- `kippend`: `64`
- `stabil`: `8150`
- `tragend_unruhig`: `1756`

Episodenzustaende:

- `field_carried`: `9970`
- `field_strained`: `24`

## Artefakte

- Debug: `debug\altseq_2025_a_10k`
- Memory: `memory\altseq_2025_a_10k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
