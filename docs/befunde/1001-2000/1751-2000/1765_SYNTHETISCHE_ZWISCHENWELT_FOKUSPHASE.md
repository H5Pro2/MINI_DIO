# Synthetische Zwischenwelt: Fokusphase gegen Rekopplungsbreite

Stand: 2026-07-08

## Grundfrage

Die vorherige Zwischenwelt zeigte eine einzelne lokale `mittlere_uebergangsphase`.

Die neue Frage war:

```text
Ist diese Phase stabil reproduzierbar,
wenn man genau den Bereich um gegenpol -> rekopplung vergrößert?
```

## Unterprüfung

Aus `synthetic_1764_rekopplungsbreite_zwischenwelt_b_9000_5m.csv` wurden Fokusfenster um die auffällige Übergangszone erzeugt:

- 1500er-Fenster
- 2000er-Fenster
- ein längeres 2500er-Fenster

Diese Fenster wurden wieder mit der Real-Sleep-Real-Achsenprüfung gelesen.

## Ergebnis

Die mittlere Übergangsphase wurde reproduziert.

Sie erschien in:

```text
SYN1765_3000_4500_TO_3200_4700
SYN1765_3000_5000_TO_3200_5200
```

Beide Fälle zeigten:

```text
3 Rollen
3 Kombinationen
2 Cross-State-Kombinationen
adaptive Rekopplung deutlich erhöht
Nachhall hoch
keinen Randkollaps
```

Es entstand weiterhin kein:

```text
verteilt_rekoppelnd
```

## Rohwelt-Rücklesung

Die Rücklesung der Fokusfenster unterscheidet sich von der vorherigen globaleren Rücklesung.

Für die mittlere Übergangsphase gilt hier:

```text
Basisenergie: moderat
Folgeenergie: steigt leicht
Basisdrift: moderat
Folgedrift: steigt leicht
Range: steigt leicht
Nachhall: bleibt hoch
adaptive Rekopplung: steigt deutlich
```

Damit wirkt diese Phase nicht nur wie Beruhigung nach Drift.

Sie wirkt eher wie:

```text
lokale Öffnung,
die vom Feld rekoppelnd angehoben wird,
aber noch nicht breit genug wird.
```

## Deutung

Die Fokusprüfung zeigt:

- Die Übergangsphase war kein Einzelfehler.
- Sie bleibt bei 1500er- und 2000er-Fenstern sichtbar.
- Mehr Fensterbreite zerstört sie nicht.
- Die adaptive Rekopplung reagiert klar auf diese Zone.

Aber:

```text
Die Rollenbreite bleibt mittel.
```

MINI_DIO öffnet hier lokale Rollen, hält sie aber noch nicht als verteilte rekoppelnde Breite.

## Bedeutung für MINI_DIO

Diese Prüfung ist ein methodischer Fortschritt:

```text
Die synthetische Suche findet jetzt eine reproduzierbare Vorform rekoppelnder Breite.
```

Sie liegt zwischen:

- kompakter Nachhallbindung,
- offener Drift,
- harter Randlast,
- echter verteilter Rekopplung.

Damit wird die gesuchte Feldqualität eingrenzbarer.

## Grenze

Die Phase ist bisher eine Vorform.

Sie darf nicht als `verteilt_rekoppelnd` umbenannt werden.

Der Befund lautet vorsichtig:

```text
stabile mittlere Rollenöffnung mit adaptiver Rekopplung
```

## Wie es weitergeht

Als nächstes sollte diese Fokusphase nicht breiter, sondern variabler gemacht werden: kleine wechselnde Öffnungsimpulse innerhalb derselben Rekopplungszone. Ziel ist zu prüfen, ob mehr Binnenvarianz aus 3 Rollen eine verteilte Rollenbreite macht, ohne Nachhall und Rückbindung zu verlieren.
