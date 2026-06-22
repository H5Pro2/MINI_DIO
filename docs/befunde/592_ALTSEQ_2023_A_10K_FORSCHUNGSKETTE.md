# Aktueller Forschungslauf

Stand: 2026-06-21 23:34:19

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2023_altseq_a_10k_5m_SOLUSDT.csv`
- Kerzen: `10000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `695` -> `695`
- Episoden: `9994` -> `9994`
- geschriebene Episodenmemory: `65` -> `60`
- MCM-Rekopplung: `0.704752` -> `0.704344`
- MCM-Tragqualitaet: `0.534678` -> `0.535084`
- Sinnes-MCM-Kopplung: `0.845` -> `0.844614`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6, dio_1ewh8ej`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c, dio_1ewh`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `29`
- `kippend`: `103`
- `stabil`: `8306`
- `tragend_unruhig`: `1556`

Episodenzustaende:

- `field_carried`: `9965`
- `field_strained`: `29`

## Artefakte

- Debug: `debug\altseq_2023_a_10k`
- Memory: `memory\altseq_2023_a_10k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
