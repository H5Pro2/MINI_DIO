# Aktueller Forschungslauf

Stand: 2026-06-22 13:03:53

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_synthetic_mcm_zeitdehnung_kompakt_5m.csv`
- Kerzen: `3000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `162` -> `162`
- Episoden: `2994` -> `2994`
- geschriebene Episodenmemory: `4` -> `4`
- MCM-Rekopplung: `0.740601` -> `0.740408`
- MCM-Tragqualitaet: `0.586059` -> `0.586249`
- Sinnes-MCM-Kopplung: `0.901166` -> `0.900985`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_06er2zu, dio_0g3bu28, dio_0ly7zc9, dio_0n0i1kn, dio_0pz659c, dio_13o0i6x, dio_1492fc4, dio_1fllaqz`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_06er, dio_0g3b, dio_0ly7, dio_0n0i, dio_0pz6, dio_13o0, dio_1492, dio_1fll`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `kippend`: `2`
- `rekoppelnd`: `1`
- `stabil`: `2851`
- `tragend_unruhig`: `140`

Episodenzustaende:

- `field_carried`: `2993`
- `field_strained`: `1`

## Artefakte

- Debug: `debug\adapted_synth_zeitdehnung_kompakt`
- Memory: `bot_memory\adapted_synth_zeitdehnung_kompakt.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
