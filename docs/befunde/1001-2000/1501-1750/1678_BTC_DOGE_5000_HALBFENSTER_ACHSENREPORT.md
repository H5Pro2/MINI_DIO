# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-07 11:47:52

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `docs\befunde\1678_BTC_DOGE_5000_HALBFENSTER_ACHSENREPORT.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| axis_btc_2024_5000_halves | btc_2024_5m_5000_halves | rand_kippnah | verteilt | 5 | 10 | 4 | 6 | 0.6979 | 0.1468 | 3721 | 1223 | 43 | 7 |
| axis_doge_2024_5000_halves | doge_2024_5m_5000_halves | rand_kippnah | mittel | 4 | 6 | 3 | 3 | 0.6973 | 0.1382 | 3587 | 1362 | 44 | 1 |

## Klassenverteilung

- `rand_kippnah`: `2`

## Befund

Der Report macht sichtbar, ob eine Weltphase kompakt gebunden, verteilt offen, verteilt rekoppelnd, nachhallend kompakt oder rand-/kippnah wirkt.

Diese Pruefung nutzt echte Halbfenster:

```text
0-5000 -> 5000-10000
```

Damit ist sie methodisch sauberer als die 10k-Selbstgegenprobe aus dem vorherigen Report.

Der Befund bestaetigt die laengere Rand-/Kippnaehe:

- BTC 2024 5m bleibt bei 5000er Halbfenstern `rand_kippnah`.
- DOGE 2024 5m bleibt ebenfalls `rand_kippnah`.
- BTC traegt dabei eine verteilte Rollenbreite: 5 Rollen, 10 Kombinationen, 4 Cross-State- und 6 Same-State-Anschluesse.
- DOGE bleibt mittlerer: 4 Rollen, 6 Kombinationen, 3 Cross-State- und 3 Same-State-Anschluesse.

Damit war die Rand-/Kippnaehe aus Report 1677 nicht nur ein Effekt der Selbstgegenprobe. Sie tritt auch auf, wenn die erste Welthaelfte gegen die zweite Welthaelfte rekoppelt.

Vorlaeufige methodische Folgerung:

```text
2000er-Fenster zeigen lokale Rollenform.
4000er/5000er-Fenster zeigen eher Feldmilieu.
```

BTC kann lokal verteilt-rekoppelnd wirken, bleibt im laengeren Feldmilieu aber rand-/kippnah. DOGE kann lokal verteilt-offen wirken, wird im laengeren Feldmilieu ebenfalls rand-/kippnah. Das spricht fuer eine mehrschichtige Feldlesung: lokale Ordnung und uebergeordnete Weltspannung sind nicht identisch.

Wichtig ist die gemeinsame Lesung:

```text
Rollenbreite allein reicht nicht.
Nachhall allein reicht nicht.
Topologie allein reicht nicht.
Erst die gemeinsame Achsenlage beschreibt das Feldmilieu.
```

## Grenze

Die Klassifikation ist eine passive Diagnose. Sie beschreibt Feldmilieu und Anschlussfaehigkeit, aber keine Richtung, keine Handlung und keine Strategie.

## Wie es weitergeht

Als naechstes sollte die gleiche Halbfensterlogik auf XRP und PAXG laufen. Ziel ist zu klaeren, ob auch die zuvor mittleren Uebergangsphasen bei laengerer Lesetiefe rand-/kippnah werden oder ob sie als mittleres Feldmilieu stabil bleiben.
