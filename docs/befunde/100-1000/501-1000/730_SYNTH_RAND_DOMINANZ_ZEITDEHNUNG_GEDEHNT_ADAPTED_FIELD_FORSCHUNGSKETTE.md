# Aktueller Forschungslauf

Stand: 2026-06-22 17:17:33

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_synthetic_mcm_zeitdehnung_rand_dominanz_gedehnt_5m.csv`
- Kerzen: `13200`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `262` -> `262`
- Episoden: `13194` -> `13194`
- geschriebene Episodenmemory: `8` -> `8`
- MCM-Rekopplung: `0.743688` -> `0.74357`
- MCM-Tragqualitaet: `0.595572` -> `0.595695`
- Sinnes-MCM-Kopplung: `0.896545` -> `0.896431`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_0g3bu28, dio_0n0i1kn, dio_0pz659c, dio_13o0i6x, dio_1492fc4, dio_14wjmk5, dio_1fllaqz, dio_1ygxff2`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_0g3b, dio_0n0i, dio_0pz6, dio_13o0, dio_1492, dio_14wj, dio_1fll, dio_1ygx`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `1`
- `kippend`: `5`
- `stabil`: `12239`
- `tragend_unruhig`: `949`

Episodenzustaende:

- `field_carried`: `13193`
- `field_strained`: `1`

## Artefakte

- Debug: `debug\adapted_synth_zeitdehnung_rand_dominanz_gedehnt`
- Memory: `bot_memory\adapted_synth_zeitdehnung_rand_dominanz_gedehnt.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
