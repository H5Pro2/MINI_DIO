# Aktueller Forschungslauf

Stand: 2026-06-22 17:16:57

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_synthetic_mcm_zeitdehnung_rand_dominanz_kompakt_5m.csv`
- Kerzen: `3300`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `199` -> `199`
- Episoden: `3294` -> `3294`
- geschriebene Episodenmemory: `4` -> `4`
- MCM-Rekopplung: `0.734059` -> `0.733805`
- MCM-Tragqualitaet: `0.575585` -> `0.575836`
- Sinnes-MCM-Kopplung: `0.892606` -> `0.892368`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_06er2zu, dio_0g3bu28, dio_0n0i1kn, dio_0pz659c, dio_10yy01h, dio_1492fc4, dio_17ctp0f, dio_1fllaqz`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_06er, dio_0g3b, dio_0n0i, dio_0pz6, dio_10yy, dio_1492, dio_17ct, dio_1fll`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `1`
- `kippend`: `5`
- `stabil`: `3022`
- `tragend_unruhig`: `266`

Episodenzustaende:

- `field_carried`: `3293`
- `field_strained`: `1`

## Artefakte

- Debug: `debug\adapted_synth_zeitdehnung_rand_dominanz_kompakt`
- Memory: `bot_memory\adapted_synth_zeitdehnung_rand_dominanz_kompakt.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
