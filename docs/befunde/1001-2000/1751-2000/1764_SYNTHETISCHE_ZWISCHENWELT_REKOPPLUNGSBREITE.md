# Synthetische Zwischenwelt: Suche nach rekoppelnder Rollenbreite

Stand: 2026-07-08

## Grundfrage

Nach den vorherigen synthetischen Gegenproben blieb offen:

```text
Kann eine gezielte Zwischenwelt Rollenbreite erzeugen,
ohne in offene Drift oder harte Randlast zu kippen?
```

## Konstruktion

Dafür wurden drei synthetische Zwischenwelten erzeugt:

- `synthetic_1764_rekopplungsbreite_zwischenwelt_a_9000_5m.csv`
- `synthetic_1764_rekopplungsbreite_zwischenwelt_b_9000_5m.csv`
- `synthetic_1764_rekopplungsbreite_zwischenwelt_c_9000_5m.csv`

Die Welten liegen zwischen:

- glatter Harmonie,
- harter Randdominanz,
- Bruch/Rand,
- rekoppelnder Rückführung.

Ziel war nicht, `verteilt_rekoppelnd` zu erzwingen, sondern eine Weltform zu bauen, die:

- mehr Binnenvarianz als Harmonie trägt,
- weniger Überlast als Randdominanz erzeugt,
- wiederkehrende Rekopplung anbietet,
- kurze Randimpulse enthält,
- genug Nachhall hält.

## Ergebnis

Die Prüfung erzeugte überwiegend:

```text
kompakt_nachhallend
```

In einer lokalen Phase entstand:

```text
mittlere_uebergangsphase
```

Diese Phase trat in `SYN1764_B_3000_4000` auf.

Dort wurden sichtbar:

```text
3 Rollen
3 Kombinationen
2 Cross-State-Kombinationen
adaptive Rekopplung deutlich über statischer Rekopplung
```

Es entstand aber noch kein:

```text
verteilt_rekoppelnd
```

## Rohwelt-Rücklesung

Die mittlere Übergangsphase lag in einer besonderen Rohweltbewegung:

```text
Basiswelt: stärkere Drift
Folgewelt: deutlich ruhigere Drift
Energie: fällt
Range: fällt
Nachhall: bleibt hoch
adaptive Rekopplung: steigt
```

Kurz:

```text
Die Welt öffnet eine Rollenphase,
aber die folgende Beruhigung bindet sie nicht breit genug weiter.
```

## Deutung

Diese Zwischenwelt war ein Fortschritt gegenüber reiner Harmonie und Randrollen-Mosaik:

- sie erzeugte erstmals mehrere Rollen und Kombinationen,
- sie aktivierte adaptive Rekopplung,
- sie blieb ohne Randkollaps,
- sie öffnete aber noch nicht ausreichend für verteilte rekoppelnde Breite.

Damit wird die gesuchte Zone enger bestimmbar:

```text
Zu glatt -> kompakt nachhallend.
Zu hart -> mittlere Übergangsphase oder offene Last.
Zwischenwelt -> erste Rollenöffnung, aber noch nicht breit genug.
```

## Bedeutung für MINI_DIO

Der Befund zeigt, dass MINI_DIO synthetisch zwischen Zuständen unterscheiden kann:

- reine Ordnung,
- kompakte Nachhallbindung,
- lokale Rollenöffnung,
- adaptive Rückführung.

Das stützt die Lesung, dass die Feldantwort nicht nur Rauschen oder Projektion ist, sondern sensibel auf Weltmilieu, Driftwechsel, Nachhall und Rekopplung reagiert.

## Grenze

`verteilt_rekoppelnd` wurde weiterhin nicht synthetisch reproduziert.

Die aktuelle Zwischenwelt zeigt nur den ersten Schritt:

```text
von kompakter Nachhallbindung
zu lokaler Rollenöffnung.
```
