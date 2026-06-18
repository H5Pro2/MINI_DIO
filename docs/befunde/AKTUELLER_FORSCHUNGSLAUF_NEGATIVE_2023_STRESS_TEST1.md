# Aktueller Forschungslauf

Stand: 2026-06-18 21:49:35

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2023_negative_stress_test1_1000_5m_SOLUSDT.csv`
- Kerzen: `1000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `927` -> `927`
- Episoden: `994` -> `994`
- geschriebene Episodenmemory: `59` -> `59`
- MCM-Rekopplung: `0.630701` -> `0.630398`
- MCM-Tragqualitaet: `0.356624` -> `0.356899`
- Sinnes-MCM-Kopplung: `0.835973` -> `0.835699`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_0lm0hoi, dio_0m37fco, dio_0zxjtq3, dio_14n0zjd, dio_18iup2i, dio_1ibbib2, dio_1stv3ak, dio_1xow9nd`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_0lm0, dio_0m37, dio_0zxj, dio_14n0, dio_18iu, dio_1ibb, dio_1stv, dio_1xow`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `5`
- `gespannt`: `30`
- `kippend`: `36`
- `stabil`: `550`
- `tragend_unruhig`: `373`

Episodenzustaende:

- `field_carried`: `964`
- `field_strained`: `30`

## Artefakte

- Debug: `debug\research_chain_negative_2023_stress_test1`
- Memory: `memory\research_chain_negative_2023_stress_test1_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
