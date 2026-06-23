# Aktueller Forschungslauf

Stand: 2026-06-22 17:14:25

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_synthetic_mcm_zeitdehnung_harmonie_gedehnt_5m.csv`
- Kerzen: `10800`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `44` -> `44`
- Episoden: `10794` -> `10794`
- geschriebene Episodenmemory: `6` -> `6`
- MCM-Rekopplung: `0.758045` -> `0.758085`
- MCM-Tragqualitaet: `0.619834` -> `0.619815`
- Sinnes-MCM-Kopplung: `0.917231` -> `0.917259`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_02n3w6a, dio_0g3bu28, dio_0gfmxqu, dio_0n0i1kn, dio_13o0i6x, dio_13s036n, dio_1fllaqz, dio_1ygxff2`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_02n3, dio_0g3b, dio_0gfm, dio_0n0i, dio_13o0, dio_13s0, dio_1fll, dio_1ygx`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `kippend`: `1`
- `stabil`: `10789`
- `tragend_unruhig`: `4`

Episodenzustaende:

- `field_carried`: `10794`

## Artefakte

- Debug: `debug\adapted_synth_zeitdehnung_harmonie_gedehnt`
- Memory: `bot_memory\adapted_synth_zeitdehnung_harmonie_gedehnt.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
