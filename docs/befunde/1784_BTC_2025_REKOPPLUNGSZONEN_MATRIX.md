# 1784 - BTC 2025: Rekopplungszonen-Matrix

## Grundfrage

Nach 1782 und 1783 war sichtbar, dass BTC 2025 mehrfach rekoppelnde Breite bilden kann, aber nicht an einem festen Zeitmaß. Die offene Frage war, welche gemeinsamen Merkmale diese rekoppelnden Treffer tragen und wodurch sie sich von offener Breite oder kompakter Nachhallbindung unterscheiden.

## Prüfung

Zusammengeführt wurden:

- 1782: erste BTC-Zeitmaßzone mit rekoppelnden Treffern in 1h und 15m
- 1783: verschobene BTC-Zeitmaßzone mit rekoppelndem Treffer in 30m

Alle Zeilen wurden nach Achsenklasse aggregiert. Zusätzlich wurden die drei `verteilt_rekoppelnd`-Treffer isoliert.

## Ergebnis

Gesamtmittel der Klassen:

| Klasse | n | Rollen | Kombinationen | Cross | Same | Rekopplung | Erfahrung | Nachhall | Stabil | Unruhig |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `kompakt_nachhallend` | 7 | 1.5714 | 0.5714 | 0.2857 | 0.2857 | 0.687946 | 0.6089 | 0.2890 | 975.4 | 18.6 |
| `mittlere_uebergangsphase` | 5 | 3.2000 | 3.6000 | 2.2000 | 1.4000 | 0.689464 | 0.5389 | 0.3073 | 980.0 | 14.0 |
| `verteilt_offen` | 7 | 5.8571 | 14.1429 | 8.0000 | 4.7143 | 0.691003 | 0.5286 | 0.3058 | 980.3 | 13.7 |
| `verteilt_rekoppelnd` | 3 | 5.3333 | 11.6667 | 4.3333 | 5.0000 | 0.695374 | 0.4344 | 0.3456 | 984.0 | 10.0 |

Die drei rekoppelnden Treffer:

| Phase | Zeitmaß | Label | Rollen | Kombinationen | Cross | Same | Rekopplung | Erfahrung | Nachhall |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1782 | 1h | `BTC_2025_1H_CORE_2000_3000` | 5 | 10 | 4 | 6 | 0.695555 | 0.4432 | 0.3512 |
| 1782 | 15m | `BTC_2025_15M_ZONE_9000_10000` | 5 | 10 | 4 | 3 | 0.695155 | 0.4249 | 0.3388 |
| 1783 | 30m | `BTC_2025_30M_SHIFT_8000_9000` | 6 | 15 | 5 | 6 | 0.695411 | 0.4352 | 0.3467 |

## Interpretation

Die Matrix trennt vier Zustände:

```text
kompakt_nachhallend
  -> viel Erfahrung, wenig Rollenraum

mittlere_uebergangsphase
  -> mittlere Öffnung, noch nicht breit getragen

verteilt_offen
  -> viele Rollen/Kombinationen, stärker offen

verteilt_rekoppelnd
  -> mittlere Breite, höchste Rekopplung, stärkster Nachhall, höchste Stabilität
```

Der wichtigste Befund ist nicht die Anzahl der Rollen. `verteilt_offen` trägt im Mittel mehr Rollen und Kombinationen als `verteilt_rekoppelnd`. Trotzdem ist `verteilt_rekoppelnd` stärker zusammengehalten.

Damit wird die bisherige Arbeitsform präziser:

```text
Breite
  -> kann offen bleiben

Breite + Rückbindung + Nachhall + Stabilität
  -> kann rekoppelnd getragen werden
```

Der niedrigere Erfahrungswert der rekoppelnden Treffer ist ebenfalls relevant: Rekopplung wirkt hier nicht wie bloßes Auswendiglernen. Sie entsteht eher als phasisch getragene Feldqualität mit genügend Breite, aber ohne maximale Streuung.

## Grenze

Das ist eine passive Diagnose aus BTC 2025. Sie beschreibt keine Handlung und keine feste Regel. Der Befund sagt nur: In den geprüften BTC-Zonen unterscheidet MINI_DIO offene Rollenbreite und rekoppelnd getragene Rollenbreite messbar.

## Artefakte

- `reports/btc_2025_rekopplungszonen_matrix.csv`
- `reports/btc_2025_rekopplungszonen_matrix.md`
- `reports/btc_2025_rekopplungszonen_treffer.csv`

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob diese BTC-Matrix auf PAXG-Rekopplungsfenster übertragbar ist. Ziel ist zu klären, ob PAXG und BTC dieselbe rekoppelnde Signatur tragen oder ob PAXG eine andere Form von Rückbindung zeigt.
