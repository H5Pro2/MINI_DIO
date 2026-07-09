# Aktueller Forschungslauf

Stand: 2026-06-22 11:07:12

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_synthetic_mcm_rand_dominanz_a_5m.csv`
- Kerzen: `7000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `226` -> `226`
- Episoden: `6994` -> `6994`
- geschriebene Episodenmemory: `6` -> `6`
- MCM-Rekopplung: `0.741164` -> `0.741013`
- MCM-Tragqualitaet: `0.590449` -> `0.590601`
- Sinnes-MCM-Kopplung: `0.897203` -> `0.89706`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_06er2zu, dio_0g3bu28, dio_0n0i1kn, dio_0pz659c, dio_13o0i6x, dio_1492fc4, dio_17ctp0f, dio_1fllaqz`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_06er, dio_0g3b, dio_0n0i, dio_0pz6, dio_13o0, dio_1492, dio_17ct, dio_1fll`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `1`
- `kippend`: `4`
- `stabil`: `6513`
- `tragend_unruhig`: `476`

Episodenzustaende:

- `field_carried`: `6993`
- `field_strained`: `1`

## Artefakte

- Debug: `debug\adapted_synth_rand_dominanz_a`
- Memory: `bot_memory\adapted_synth_rand_dominanz_a.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
