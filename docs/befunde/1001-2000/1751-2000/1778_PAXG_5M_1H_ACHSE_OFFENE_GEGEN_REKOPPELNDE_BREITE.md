# PAXG 5m/1h: Achse zwischen offener und rekoppelnder Breite

Stand: 2026-07-08

## Grundfrage

Nach 1777 war sichtbar:

```text
PAXG 1h bildet Rollenbreite,
aber bisher keine rekoppelnde Rollenbreite.
```

Die nächste Unterprüfung war:

```text
Was unterscheidet PAXG 5m `verteilt_rekoppelnd`
von PAXG 1h `verteilt_offen`?
```

## Prüfung

Verglichen wurden Gruppenwerte aus:

```text
PAXG 2024 5m
PAXG 2025 5m
PAXG 2024/2025 1h
```

Der kompakte Vergleich liegt in:

```text
reports/paxg_5m_1h_rekopplung_achsenvergleich.csv
reports/paxg_5m_1h_rekopplung_achsenvergleich.md
```

## Ergebnis

PAXG 2025 5m `verteilt_rekoppelnd`:

```text
Rollen: 8.0
Kombinationen: 20.0
Rekopplung: 0.704207
Nachhall: 0.3753
Folge-Richtungswechsel: 0.3046
```

PAXG 1h `verteilt_offen`:

```text
Rollen: 7.125
Kombinationen: 19.0
Rekopplung: 0.691141
Nachhall: 0.3014
Folge-Richtungswechsel: 0.4815
```

## Befund

PAXG 1h hat fast die gleiche Rollen- und Kombinationsbreite wie PAXG 5m rekoppelnd.

Der Unterschied liegt nicht primär in:

```text
Rollenanzahl
```

sondern in:

```text
Rekopplung
Nachhall
ruhigerer Anschlussrichtung
```

## Deutung

Offene Breite entsteht, wenn mehrere Rollen sichtbar werden, aber die Rückbindung nicht stark genug geschlossen wird.

Rekoppelnde Breite entsteht, wenn Rollenbreite zusätzlich durch Nachhall und gerichtete Anschlussqualität gehalten wird.

Arbeitsformel:

```text
Rollenbreite allein -> verteilt_offen
Rollenbreite + Nachhall + Rekopplung + ruhigere Folgebewegung -> verteilt_rekoppelnd
```

## Bedeutung für MINI_DIO

Das ist ein wichtiger methodischer Schritt:

```text
MINI_DIO unterscheidet Breite von Bindung.
```

Damit kann das Feld nicht nur zählen, wie viele Rollen aktiv sind.

Es kann passiv gelesen werden, ob diese Rollen:

- offen nebeneinander stehen,
- rekoppelnd getragen werden,
- oder später wieder kompakt nachhallen.

## Grenze

Die Werte sind Gruppenmittel der bisher geprüften Fenster.

Sie sind keine festen MCM-Grenzen und keine Regel.

Sie beschreiben eine bisher sichtbare Achse zwischen offener und rekoppelnder Rollenbreite.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob diese Achse auch in anderen Assets sichtbar ist: DOGE/BTC/XRP offen gegen PAXG rekoppelnd, oder ob PAXG hier eine besondere Anschlussqualität trägt.
