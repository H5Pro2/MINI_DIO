# Aktueller Forschungslauf

Stand: 2026-06-23 09:01:27

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\field_quiet_candidates\1-12_2025_5m_btcusdt_btc2025_field_quiet_01_2000.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `348` -> `348`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `1` -> `1`
- MCM-Rekopplung: `0.696407` -> `0.695723`
- MCM-Tragqualitaet: `0.511257` -> `0.511931`
- Sinnes-MCM-Kopplung: `0.845545` -> `0.844902`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00jaski, dio_00lyjkf, dio_06s7dt1, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_155c3g6`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ja, dio_00ly, dio_06s7, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_155c`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `kippend`: `16`
- `stabil`: `1613`
- `tragend_unruhig`: `365`

Episodenzustaende:

- `field_carried`: `1994`

## Artefakte

- Debug: `debug\field_quiet_candidates_btc2025\btc2025_field_quiet_01`
- Memory: `bot_memory\field_quiet_candidates_btc2025\btc2025_field_quiet_01.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
