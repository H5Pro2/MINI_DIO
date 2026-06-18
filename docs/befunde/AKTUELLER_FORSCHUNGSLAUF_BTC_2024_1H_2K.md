# Aktueller Forschungslauf

Stand: 2026-06-18 22:33:51

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_btc_2024_1h_test1_2000_BTCUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `1911` -> `1911`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `329` -> `329`
- MCM-Rekopplung: `0.610687` -> `0.610376`
- MCM-Tragqualitaet: `0.344736` -> `0.345005`
- Sinnes-MCM-Kopplung: `0.812267` -> `0.811991`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_03t5leb, dio_0efonve, dio_0ifwpgc, dio_0tyr1me, dio_0z5xztt, dio_159kdq9, dio_1g35sz0, dio_1iuouyj`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_03t5, dio_0efo, dio_0ifw, dio_0tyr, dio_0z5x, dio_159k, dio_1g35, dio_1iuo`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `48`
- `gespannt`: `271`
- `kippend`: `246`
- `rekoppelnd`: `6`
- `stabil`: `584`
- `tragend_unruhig`: `839`

Episodenzustaende:

- `field_carried`: `1717`
- `field_strained`: `277`

## Artefakte

- Debug: `debug\research_chain_btc_2024_1h_2k`
- Memory: `memory\research_chain_btc_2024_1h_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
