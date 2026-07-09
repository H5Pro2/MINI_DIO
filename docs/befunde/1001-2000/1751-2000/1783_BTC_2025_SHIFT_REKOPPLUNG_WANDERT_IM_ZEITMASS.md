# 1783 - BTC 2025 Shift: Rekopplung wandert im Zeitmaß

## Grundfrage

Nach 1782 war offen, ob die BTC-Rekopplungszone erneut auftaucht, wenn der geprüfte Weltabschnitt verschoben wird. Entscheidend war, ob die rekoppelnde Breite stabil wiederkehrt oder nur an die konkrete erste Weltphase gebunden war.

## Prüfung

Geprüft wurde eine später verschobene BTC-2025-Zone:

- 1h: `4000-5000 -> 5000-6000` bis `6000-7000 -> 7000-8000`
- 30m: `8000-9000 -> 9000-10000` bis `11000-12000 -> 12000-13000`
- 15m: `16000-17000 -> 17000-18000` bis `19000-20000 -> 20000-21000`

Die Prüfung entspricht methodisch 1782, liegt aber in einem späteren Weltabschnitt.

## Ergebnis

Es entstand erneut ein `verteilt_rekoppelnd`-Treffer, diesmal im 30m-Zeitmaß:

| Label | Zeitmaß | Rollen | Kombinationen | Rekopplung | Erfahrung | Nachhall |
|---|---|---:|---:|---:|---:|---:|
| `BTC_2025_30M_SHIFT_8000_9000` | 30m | 6 | 15 | 0.695411 | 0.4352 | 0.3467 |

Die 1h-Shiftzone blieb vollständig `kompakt_nachhallend`. Die 15m-Shiftzone öffnete mehrfach Rollenbreite, blieb aber `verteilt_offen` oder kompakt.

## Klassenverteilung

| Klasse | Anzahl |
|---|---:|
| `kompakt_nachhallend` | 4 |
| `mittlere_uebergangsphase` | 1 |
| `verteilt_offen` | 5 |
| `verteilt_rekoppelnd` | 1 |

## Interpretation

Die Rekopplung ist wiederkehrend möglich, aber sie ist nicht an ein festes Zeitmaß gebunden.

Vergleich:

- 1782: rekoppelnde Treffer im 1h-Kern und im zugehörigen 15m-Bereich.
- 1783: rekoppelnder Treffer im 30m-Bereich, während 1h kompakt bleibt und 15m offen bleibt.

Damit wirkt Rekopplung nicht wie ein statischer Asset- oder Zeitmaßzustand. Sie wandert mit der Weltphase und der Auflösung. Das Feld liest also nicht nur den Markt als einfache Sequenz, sondern eine phasische Innenfeldqualität, die je nach Zeitmaß anders sichtbar wird.

Die rekoppelnden Treffer bleiben weiterhin mittlere Rollenbreite, nicht maximale Rollenbreite. Wieder stützt das die bisherige Arbeitsform:

```text
Rekopplung entsteht nicht durch maximale Breite.
Rekopplung entsteht durch tragende Breite.
```

## Grenze

Das ist eine passive Diagnose. Sie beschreibt wiederkehrende, aber wandernde Rekopplungsfähigkeit in BTC 2025. Sie ist keine Regel, kein Gate und keine Handlungsvorgabe.

## Artefakte

- `reports/btc_2025_shift_zeitmass_rekopplungszone.csv`
- `reports/btc_2025_shift_zeitmass_rekopplungszone.md`
- `reports/btc_2025_shift_zeitmass_rekopplungszone_rawworld.csv`
- `reports/btc_2025_shift_zeitmass_rekopplungszone_rawworld.md`
- `reports/btc_2025_shift_zeitmass_rekopplungszone_rawworld_groups.csv`
