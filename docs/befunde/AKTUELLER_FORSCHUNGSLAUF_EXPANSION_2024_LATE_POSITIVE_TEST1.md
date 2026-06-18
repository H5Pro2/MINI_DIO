# Aktueller Forschungslauf

Stand: 2026-06-18 21:27:01

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2024_late_positive_test1_1000_5m_SOLUSDT.csv`
- Kerzen: `1000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `954` -> `954`
- Episoden: `994` -> `994`
- geschriebene Episodenmemory: `57` -> `57`
- MCM-Rekopplung: `0.62673` -> `0.626417`
- MCM-Tragqualitaet: `0.356908` -> `0.357191`
- Sinnes-MCM-Kopplung: `0.834282` -> `0.833999`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_03uss6l, dio_07y1h7q, dio_0g5y5gc, dio_0gymjx5, dio_0npt6ik, dio_14n0zjd, dio_1bg1014, dio_1lb5y78`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00n1, dio_03us, dio_07y1, dio_0g5y, dio_0gym, dio_14n0, dio_1bg1, dio_1lb5`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `11`
- `gespannt`: `29`
- `kippend`: `49`
- `rekoppelnd`: `2`
- `stabil`: `414`
- `tragend_unruhig`: `489`

Episodenzustaende:

- `field_carried`: `963`
- `field_strained`: `31`

## Artefakte

- Debug: `debug\research_chain_expansion_2024_late_positive_test1`
- Memory: `memory\research_chain_expansion_2024_late_positive_test1_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
