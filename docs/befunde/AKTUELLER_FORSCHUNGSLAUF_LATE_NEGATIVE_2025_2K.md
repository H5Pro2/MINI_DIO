# Aktueller Forschungslauf

Stand: 2026-06-18 22:18:55

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2025_late_negative_test1_2000_5m_SOLUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `1823` -> `1823`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `119` -> `117`
- MCM-Rekopplung: `0.630526` -> `0.630192`
- MCM-Tragqualitaet: `0.362981` -> `0.363286`
- Sinnes-MCM-Kopplung: `0.836533` -> `0.83623`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_05qywi1, dio_0q3pgvg, dio_0q3vyom, dio_10dctxu, dio_12zq38o, dio_1g35sz0, dio_1rsllrx, dio_1x4byoo`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_03ic, dio_05qy, dio_0q3p, dio_0q3v, dio_10dc, dio_1g35, dio_1rsl, dio_1x4b`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `28`
- `gespannt`: `68`
- `kippend`: `69`
- `stabil`: `1013`
- `tragend_unruhig`: `816`

Episodenzustaende:

- `field_carried`: `1926`
- `field_strained`: `68`

## Artefakte

- Debug: `debug\research_chain_late_negative_2025_2k`
- Memory: `memory\research_chain_late_negative_2025_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
