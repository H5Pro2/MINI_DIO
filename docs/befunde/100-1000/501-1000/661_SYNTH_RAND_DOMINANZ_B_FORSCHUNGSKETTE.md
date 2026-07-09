# Aktueller Forschungslauf

Stand: 2026-06-22 10:36:02

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_synthetic_mcm_rand_dominanz_b_5m.csv`
- Kerzen: `7000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `222` -> `222`
- Episoden: `6994` -> `6994`
- geschriebene Episodenmemory: `7` -> `7`
- MCM-Rekopplung: `0.740703` -> `0.74055`
- MCM-Tragqualitaet: `0.589693` -> `0.589848`
- Sinnes-MCM-Kopplung: `0.898051` -> `0.897905`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_06er2zu, dio_0g3bu28, dio_0n0i1kn, dio_0pz659c, dio_13o0i6x, dio_1492fc4, dio_17ctp0f, dio_1fllaqz`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_06er, dio_0g3b, dio_0n0i, dio_0pz6, dio_13o0, dio_1492, dio_17ct, dio_1fll`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `2`
- `kippend`: `13`
- `stabil`: `6557`
- `tragend_unruhig`: `422`

Episodenzustaende:

- `field_carried`: `6992`
- `field_strained`: `2`

## Artefakte

- Debug: `debug\synthetic_mcm_rand_dominanz_b_5m`
- Memory: `memory\synthetic_mcm_rand_dominanz_b_5m_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
