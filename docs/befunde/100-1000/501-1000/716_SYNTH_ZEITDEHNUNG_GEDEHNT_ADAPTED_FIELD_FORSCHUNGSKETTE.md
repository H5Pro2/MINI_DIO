# Aktueller Forschungslauf

Stand: 2026-06-22 13:04:14

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_synthetic_mcm_zeitdehnung_gedehnt_5m.csv`
- Kerzen: `12000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `168` -> `168`
- Episoden: `11994` -> `11994`
- geschriebene Episodenmemory: `8` -> `8`
- MCM-Rekopplung: `0.749459` -> `0.749375`
- MCM-Tragqualitaet: `0.605372` -> `0.605462`
- Sinnes-MCM-Kopplung: `0.905993` -> `0.90591`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_06er2zu, dio_0g3bu28, dio_0gfmxqu, dio_0n0i1kn, dio_13o0i6x, dio_1492fc4, dio_1fllaqz, dio_1ygxff2`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_06er, dio_0g3b, dio_0gfm, dio_0n0i, dio_13o0, dio_1492, dio_1fll, dio_1ygx`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `1`
- `kippend`: `2`
- `stabil`: `11439`
- `tragend_unruhig`: `552`

Episodenzustaende:

- `field_carried`: `11993`
- `field_strained`: `1`

## Artefakte

- Debug: `debug\adapted_synth_zeitdehnung_gedehnt`
- Memory: `bot_memory\adapted_synth_zeitdehnung_gedehnt.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
