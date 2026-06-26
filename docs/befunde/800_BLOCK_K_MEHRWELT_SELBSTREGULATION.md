# 800 - Block-K-Mehrwelt-Selbstregulation

## Fragestellung

Bleibt die Block-K-Folge in einem frischen Mehrweltlauf sichtbar, wenn jede Welt einzeln mit frischer Memory gelesen wird?

Gepruefte Folge:

```text
Wahrnehmung -> Benennung -> Feldwirkung -> passive Regulation -> Integration -> Stabilisierung
```

## Methode

Jede Welt wurde mit eigener frischer Memory einmal passiv gelesen. Dieser Report nutzt nur `mini_report.json` aus dem Lauf.

Keine Handlung, kein Gate, keine Strategie, keine aktive Regulation.

Welten:

- `data\kontrolliert_sol_2025_5m_test1_2000_SOLUSDT.csv`
- `data\kontrolliert_btc_2025_1h_test1_2000_BTCUSDT.csv`
- `data\kontrolliert_kas_2024_5m_test1_2000_KASUSDT.csv`
- `data\kontrolliert_2026_sideways_test1_2000_5m_SOLUSDT.csv`

## Mehrwelt-Matrix

| Welt | Wahrnehmung | Benennung | Feldklasse | Rekopplung | Carry | Strain | passive Regulation | Integration | Stabilisierung |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|
| kontrolliert_sol_2025_5m_test1_2000_SOLUSDT.csv | 0.8381 | 351 | stabil | 0.6927 | 0.5081 | 0.1572 | 0.6646 | 0.0015 | 0.5626 |
| kontrolliert_btc_2025_1h_test1_2000_BTCUSDT.csv | 0.8447 | 340 | stabil | 0.6979 | 0.5149 | 0.1540 | 0.6738 | 0.0025 | 0.5680 |
| kontrolliert_kas_2024_5m_test1_2000_KASUSDT.csv | 0.8404 | 350 | stabil | 0.6940 | 0.5099 | 0.1562 | 0.6663 | 0.0005 | 0.5634 |
| kontrolliert_2026_sideways_test1_2000_5m_SOLUSDT.csv | 0.8431 | 356 | stabil | 0.6949 | 0.5100 | 0.1553 | 0.6662 | 0.0015 | 0.5634 |

## Wiederkehrende Rollen

Dominante MCM-Klassen:

- `stabil`: `4` Welten

Dominante MCM-Feldepisoden:

- `dio_mcm_episode_0e7qvj1`: `2` Welten
- `dio_mcm_episode_1wra2fc`: `1` Welten
- `dio_mcm_episode_1joiyc3`: `1` Welten

## Befund

- Durchschnittliche Stabilisierung ueber die geprueften Welten: `0.5644`.
- Die Kette ist in jeder geprueften Welt vollstaendig messbar: Wahrnehmung, Benennung, Feldwirkung, passive Regulation, Integration und Stabilisierung liefern Werte.
- Die konkrete Syntax bleibt weltabhaengig, waehrend Rollen wie `stabil`, Episodenbildung und Feldtragungswerte vergleichbar bleiben.
- Das stuetzt den Block-K-Anschluss staerker als Befund 799, weil hier nicht nur vorhandene Summaries zusammengelegt wurden.

## Grenze

Die Werte sind Diagnosewerte. Sie sind keine Regeln und keine Beweiszahlen. Besonders `stabilization_score` ist eine kompakte Lesegroesse, damit Welten vergleichbar werden, nicht ein Zielwert fuer das System.

## Wie es weitergeht

Als naechstes sollte diese Mehrwelt-Kette gegen eine bewusst stressigere Weltgruppe laufen. Dann wird sichtbar, ob Stabilisierung sinkt, ob mehr Drift entsteht oder ob das Feld trotzdem seine Rollenordnung haelt.
