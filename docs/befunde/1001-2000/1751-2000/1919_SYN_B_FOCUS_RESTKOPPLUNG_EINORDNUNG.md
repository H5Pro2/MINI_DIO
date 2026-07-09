# 1919 - B-Fokusfenster: Restkopplung und Hartkerntrennung

## Grundfrage

Wiederholt sich Restkopplung in mehreren weichen synthetischen Fokusfenstern, oder war der vorige Befund nur ein Einzelfall?

## Methode

Geprüft wurden drei lokale Ausschnitte derselben synthetischen B-Zwischenwelt:

- `synthetic_1765_b_focus_2400_3900.csv`
- `synthetic_1765_b_focus_3000_4500.csv`
- `synthetic_1765_b_focus_3200_5200.csv`

Die Prüfung erfolgte wieder passiv unter DOGE-Hartkern-Lesung.
DOGE dient nur als bekannte Hartkern-Brille.

## Ergebnis

| Welt | Kernpaare | getragen | geöffnet | verschoben | ausgeblendet | Score | Lesung |
|---|---:|---:|---:|---:|---:|---:|---|
| `syn_b_focus_2400_3900` | 34 | 0 | 2 | 1 | 31 | -0.574 | `kern_ausgeblendet` |
| `syn_b_focus_3000_4500` | 34 | 0 | 1 | 0 | 33 | -0.626 | `kern_ausgeblendet` |
| `syn_b_focus_3200_5200` | 34 | 1 | 0 | 1 | 32 | -0.572 | `kern_ausgeblendet` |

## Lesung

Die drei Fokusfenster bleiben dominant `kern_ausgeblendet`.
Trotzdem zeigen sie verschiedene Restkopplungen:

- `2400_3900` erzeugt am stärksten Öffnung und leichte Verschiebung.
- `3000_4500` wirkt auf der breiteren Familienebene reproduzierender, trägt den harten DOGE-Kern aber kaum.
- `3200_5200` hält eine direkte Reproduktion und eine Verschiebung.

Damit wird eine wichtige Trennung sichtbar:

```text
allgemeine Feldaktivität != Hartkernkopplung
```

Eine Welt kann viele Familien berühren oder öffnen, ohne den gereiften Hartkern wirklich zu tragen.

## Bedeutung

Für MINI_DIO ist diese Trennung wichtig.
Sie verhindert, dass reine Aktivität fälschlich als Reife gelesen wird.

Organisch formuliert:

```text
Das Feld reagiert.
Aber der gereifte Kern wird nicht zwingend getragen.
```

Das stärkt die Lesung von `kern_ausgeblendet` als eigener Feldzustand mit Unterqualitäten:

- harte Ausblendung
- weiche Ausblendung mit Öffnungsrest
- weiche Ausblendung mit Reproduktionsrest
- weiche Ausblendung mit Verschiebungsrest

## Abgrenzung

Auch diese Unterqualitäten bleiben passiv.
Sie sind keine Handlung, kein Gate und keine Richtung.

## Wie es weitergeht

Als nächstes sollte die Restkopplung nicht nur gegen DOGE gelesen werden. Wir sollten dieselben B-Fokusfenster gegen einen anderen Hartkern-Träger prüfen, zum Beispiel SOL oder BTC. Dadurch sehen wir, ob die Restkopplung weltbedingt ist oder stark von der gewählten Hartkern-Brille abhängt.
