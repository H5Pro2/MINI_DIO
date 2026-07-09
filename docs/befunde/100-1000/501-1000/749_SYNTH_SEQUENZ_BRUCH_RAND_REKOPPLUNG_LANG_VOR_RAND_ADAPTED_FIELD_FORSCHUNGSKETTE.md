# Aktueller Forschungslauf

Stand: 2026-06-22 20:29:28

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_synthetic_mcm_sequenz_bruch_rand_rekopplung_lang_vor_rand_5m.csv`
- Kerzen: `7500`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `175` -> `175`
- Episoden: `7494` -> `7494`
- geschriebene Episodenmemory: `7` -> `7`
- MCM-Rekopplung: `0.748565` -> `0.748469`
- MCM-Tragqualitaet: `0.602852` -> `0.602952`
- Sinnes-MCM-Kopplung: `0.906433` -> `0.90634`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_06er2zu, dio_0g3bu28, dio_0n0i1kn, dio_13o0i6x, dio_1492fc4, dio_1fe0qb2, dio_1fllaqz, dio_1ygxff2`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_06er, dio_0g3b, dio_0n0i, dio_13o0, dio_1492, dio_1fe0, dio_1fll, dio_1ygx`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `2`
- `kippend`: `3`
- `stabil`: `7187`
- `tragend_unruhig`: `302`

Episodenzustaende:

- `field_carried`: `7492`
- `field_strained`: `2`

## Artefakte

- Debug: `debug\adapted_synth_sequenz_bruch_rand_rekopplung_lang_vor_rand`
- Memory: `bot_memory\adapted_synth_sequenz_bruch_rand_rekopplung_lang_vor_rand.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
