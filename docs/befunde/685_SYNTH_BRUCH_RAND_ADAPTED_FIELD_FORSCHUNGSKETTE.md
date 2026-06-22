# Aktueller Forschungslauf

Stand: 2026-06-22 11:07:07

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_synthetic_mcm_bruch_rand_a_5m.csv`
- Kerzen: `6000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `170` -> `170`
- Episoden: `5994` -> `5994`
- geschriebene Episodenmemory: `7` -> `7`
- MCM-Rekopplung: `0.746056` -> `0.745946`
- MCM-Tragqualitaet: `0.597999` -> `0.598116`
- Sinnes-MCM-Kopplung: `0.904181` -> `0.904073`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_06er2zu, dio_0g3bu28, dio_0ly7zc9, dio_0n0i1kn, dio_13o0i6x, dio_1492fc4, dio_1fllaqz, dio_1ygxff2`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_06er, dio_0g3b, dio_0ly7, dio_0n0i, dio_13o0, dio_1492, dio_1fll, dio_1ygx`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `1`
- `kippend`: `1`
- `rekoppelnd`: `1`
- `stabil`: `5713`
- `tragend_unruhig`: `278`

Episodenzustaende:

- `field_carried`: `5992`
- `field_strained`: `2`

## Artefakte

- Debug: `debug\adapted_synth_bruch_rand_a`
- Memory: `bot_memory\adapted_synth_bruch_rand_a.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
