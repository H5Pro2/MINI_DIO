# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-07 11:42:36

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `docs\befunde\1677_BTC_DOGE_LANGFENSTER_ACHSENREPORT.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| axis_btc_2024_4000_a | btc_2024_5m_4000 | rand_kippnah | verteilt | 5 | 10 | 4 | 6 | 0.6950 | 0.1370 | 2904 | 1042 | 41 | 7 |
| axis_doge_2024_4000_a | doge_2024_5m_4000 | rand_kippnah | mittel | 3 | 3 | 2 | 1 | 0.6940 | 0.1265 | 2782 | 1171 | 40 | 1 |
| axis_btc_2024_10k_self | btc_2024_5m_10k_self | rand_kippnah | mittel | 4 | 6 | 0 | 6 | 0.7032 | 0.1651 | 7756 | 2166 | 64 | 8 |
| axis_doge_2024_10k_self | doge_2024_5m_10k_self | rand_kippnah | mittel | 4 | 6 | 0 | 6 | 0.7027 | 0.1540 | 7445 | 2483 | 63 | 3 |

## Klassenverteilung

- `rand_kippnah`: `4`

## Befund

Der Report macht sichtbar, ob eine Weltphase kompakt gebunden, verteilt offen, verteilt rekoppelnd, nachhallend kompakt oder rand-/kippnah wirkt.

Dieser Lauf wurde mit `--ticks 1000` ausgefuehrt. Dadurch wird die aktive Pruefung tiefer als bei den vorherigen 300-Tick-Achsenreports.

Der Befund ist deutlich:

- BTC 2024 5m im 4000er-Fenster wird `rand_kippnah`, obwohl die 2000er-Shift-Fenster zuvor `kompakt_gebunden` und `verteilt_rekoppelnd` zeigten.
- DOGE 2024 5m im 4000er-Fenster wird ebenfalls `rand_kippnah`, obwohl das verschobene 2000er-Fenster zuvor einmal `verteilt_offen` zeigte.
- Die 10k-Selbstgegenproben fuer BTC und DOGE liegen ebenfalls `rand_kippnah`.

Damit verdichtet sich der Eindruck: Bei laengerer Tiefenlesung wird nicht einfach eine ruhige groessere Stabilitaet sichtbar. Stattdessen kommt eine Rand-/Kippnaehe zum Vorschein, die in kuerzeren Fenstern teilweise als kompakte Bindung, verteilte Rekopplung oder offene Verteilung erschien.

Die 10k-Selbstgegenproben sind methodisch getrennt zu lesen: Sie pruefen keine echte Folgewelt, sondern Selbstrekopplung innerhalb derselben Weltspur. Dass beide trotzdem rand-/kippnah werden, spricht dafuer, dass die lange Weltlage eine eigene Spannungsschicht traegt.

Vorlaeufige Lesung:

```text
Kurze Fenster zeigen lokale Rollenform.
Laengere Fenster zeigen eher Feldmilieu.
```

Damit wird die Achsenanalyse tiefer: Ein lokales Fenster kann verteilt-rekoppelnd oder offen wirken, waehrend die laengere Weltphase insgesamt rand-/kippnah bleibt.

Wichtig ist die gemeinsame Lesung:

```text
Rollenbreite allein reicht nicht.
Nachhall allein reicht nicht.
Topologie allein reicht nicht.
Erst die gemeinsame Achsenlage beschreibt das Feldmilieu.
```

## Grenze

Die Klassifikation ist eine passive Diagnose. Sie beschreibt Feldmilieu und Anschlussfaehigkeit, aber keine Richtung, keine Handlung und keine Strategie.
