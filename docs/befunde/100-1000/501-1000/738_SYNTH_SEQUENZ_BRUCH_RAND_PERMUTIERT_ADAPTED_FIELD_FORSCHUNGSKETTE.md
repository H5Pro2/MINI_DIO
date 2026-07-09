# Aktueller Forschungslauf

Stand: 2026-06-22 18:07:30

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_synthetic_mcm_sequenz_bruch_rand_permutiert_5m.csv`
- Kerzen: `6100`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `161` -> `161`
- Episoden: `6094` -> `6094`
- geschriebene Episodenmemory: `7` -> `7`
- MCM-Rekopplung: `0.746302` -> `0.746159`
- MCM-Tragqualitaet: `0.598329` -> `0.598475`
- Sinnes-MCM-Kopplung: `0.904454` -> `0.904317`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_06er2zu, dio_0g3bu28, dio_0ly7zc9, dio_0n0i1kn, dio_13o0i6x, dio_1492fc4, dio_1fllaqz, dio_1ygxff2`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_06er, dio_0g3b, dio_0ly7, dio_0n0i, dio_13o0, dio_1492, dio_1fll, dio_1ygx`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `2`
- `kippend`: `1`
- `stabil`: `5804`
- `tragend_unruhig`: `287`

Episodenzustaende:

- `field_carried`: `6092`
- `field_strained`: `2`

## Artefakte

- Debug: `debug\adapted_synth_sequenz_bruch_rand_permutiert`
- Memory: `bot_memory\adapted_synth_sequenz_bruch_rand_permutiert.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
