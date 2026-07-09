# Aktueller Forschungslauf

Stand: 2026-06-22 12:33:53

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2024_negative_stress_10k_5m_SOLUSDT.csv`
- Kerzen: `10000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `675` -> `675`
- Episoden: `9994` -> `9994`
- geschriebene Episodenmemory: `7` -> `7`
- MCM-Rekopplung: `0.705575` -> `0.705167`
- MCM-Tragqualitaet: `0.537071` -> `0.537481`
- Sinnes-MCM-Kopplung: `0.842523` -> `0.842137`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_0oc3c1g, dio_104t4us, dio_14wjmk5, dio_155c3g6, dio_17ctp0f`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_0h9h, dio_0l7p, dio_0m9z, dio_0oc3, dio_104t, dio_14wj, dio_155c, dio_17ct`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `1`
- `kippend`: `63`
- `stabil`: `8024`
- `tragend_unruhig`: `1906`

Episodenzustaende:

- `field_carried`: `9993`
- `field_strained`: `1`

## Artefakte

- Debug: `debug\adapted_state_negative_stress_2024_5m_10k`
- Memory: `bot_memory\adapted_state_negative_stress_2024_5m_10k.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
