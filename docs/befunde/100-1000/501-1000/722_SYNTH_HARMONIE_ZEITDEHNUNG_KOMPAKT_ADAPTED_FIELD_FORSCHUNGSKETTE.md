# Aktueller Forschungslauf

Stand: 2026-06-22 17:14:09

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_synthetic_mcm_zeitdehnung_harmonie_kompakt_5m.csv`
- Kerzen: `2700`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `47` -> `47`
- Episoden: `2694` -> `2694`
- geschriebene Episodenmemory: `2` -> `2`
- MCM-Rekopplung: `0.753475` -> `0.753471`
- MCM-Tragqualitaet: `0.609765` -> `0.609785`
- Sinnes-MCM-Kopplung: `0.915169` -> `0.915158`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_0g3bu28, dio_0gfmxqu, dio_0n0i1kn, dio_0nljypu, dio_13o0i6x, dio_13s036n, dio_1fllaqz, dio_1ygxff2`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_0g3b, dio_0gfm, dio_0n0i, dio_0nlj, dio_13o0, dio_13s0, dio_1fll, dio_1ygx`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `kippend`: `1`
- `stabil`: `2688`
- `tragend_unruhig`: `5`

Episodenzustaende:

- `field_carried`: `2694`

## Artefakte

- Debug: `debug\adapted_synth_zeitdehnung_harmonie_kompakt`
- Memory: `bot_memory\adapted_synth_zeitdehnung_harmonie_kompakt.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
