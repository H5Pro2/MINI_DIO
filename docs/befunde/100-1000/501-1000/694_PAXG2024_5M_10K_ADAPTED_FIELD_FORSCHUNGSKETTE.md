# Aktueller Forschungslauf

Stand: 2026-06-22 12:27:09

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_paxg_2024_5m_10k_PAXGUSDT.csv`
- Kerzen: `10000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `520` -> `520`
- Episoden: `9994` -> `9994`
- geschriebene Episodenmemory: `5` -> `5`
- MCM-Rekopplung: `0.715072` -> `0.714682`
- MCM-Tragqualitaet: `0.539893` -> `0.540284`
- Sinnes-MCM-Kopplung: `0.852646` -> `0.852276`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6, dio_1fllaqz, dio_1u5il5a`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c, dio_1fll, dio_1u5i`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `kippend`: `29`
- `stabil`: `8469`
- `tragend_unruhig`: `1496`

Episodenzustaende:

- `field_carried`: `9994`

## Artefakte

- Debug: `debug\adapted_field_paxg_2024_5m_10k`
- Memory: `bot_memory\adapted_field_paxg_2024_5m_10k.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
