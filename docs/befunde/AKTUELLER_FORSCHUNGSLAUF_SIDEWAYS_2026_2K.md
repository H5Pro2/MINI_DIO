# Aktueller Forschungslauf

Stand: 2026-06-18 22:02:17

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2026_sideways_test1_2000_5m_SOLUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `1890` -> `1890`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `177` -> `175`
- MCM-Rekopplung: `0.622353` -> `0.62203`
- MCM-Tragqualitaet: `0.355125` -> `0.355412`
- Sinnes-MCM-Kopplung: `0.826852` -> `0.826561`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_07y1h7q, dio_0f10dj6, dio_0feua68, dio_0n481ri, dio_0u9308n, dio_1ar10hz, dio_1g35sz0, dio_1sme4ov`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_03t5, dio_07y1, dio_0f10, dio_0n48, dio_0scj, dio_0u93, dio_1ar1, dio_1sme`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `44`
- `gespannt`: `116`
- `kippend`: `155`
- `rekoppelnd`: `4`
- `stabil`: `821`
- `tragend_unruhig`: `854`

Episodenzustaende:

- `field_carried`: `1874`
- `field_strained`: `120`

## Artefakte

- Debug: `debug\research_chain_sideways_2026_2k`
- Memory: `memory\research_chain_sideways_2026_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
