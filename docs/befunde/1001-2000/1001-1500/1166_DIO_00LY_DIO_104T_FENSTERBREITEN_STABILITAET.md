# 1166 - Fensterbreiten-Stabilitaet der Achsenbeziehung

## Grundfrage

Bleibt die Beziehung zwischen `dio_00ly` und `dio_104t` sichtbar, wenn das zeitliche Naehefenster veraendert wird?

Geprueft wurden dieselben acht Weltklassen mit drei Tickfenstern:

- 6 Ticks
- 12 Ticks
- 24 Ticks

Die Pruefung bleibt passiv. Es wird keine Handlung, kein Gate und keine Strategie daraus abgeleitet.

## Ergebnis

Die Achsenbeziehung bleibt ueber alle Fenster sichtbar.

Je groesser das Fenster wird, desto haeufiger liegt `dio_104t` in der Naehe von `dio_00ly`. Das bedeutet: Die Beziehung ist nicht nur ein einzelner Tickkontakt, sondern ein laengerer Feldbereich.

Die Richtung ist aber nicht ueberall gleich stabil. Einige Welten halten dieselbe Richtung ueber alle Fenster, andere kippen mit der Fensterbreite in eine balancierte Lesung.

## Stabile Richtungsbilder

- `PAXG 2024 5m`: ueber 6, 12 und 24 Ticks balanciert.
- `BTC 2024 1h`: ueber 6, 12 und 24 Ticks balanciert.
- `KAS 2024 5m`: ueber 6, 12 und 24 Ticks `dio_00ly -> dio_104t`.
- `BTC 2024 Quiet 5m`: ueber 6, 12 und 24 Ticks `dio_104t -> dio_00ly`.
- `Negative Stress 2024`: ueber 6, 12 und 24 Ticks `dio_00ly -> dio_104t`.

Diese Welten zeigen eine robuste Feldrichtung innerhalb der Achsenbeziehung.

## Fensterabhaengige Richtungsbilder

- `Expansion 2023`: bei 12 Ticks `dio_104t -> dio_00ly`, bei 6 und 24 Ticks balanciert.
- `SOL 2026 Seitwaerts`: bei 6 Ticks `dio_104t -> dio_00ly`, bei 12 und 24 Ticks balanciert.
- `Positive Recovery 2025`: bei 6 Ticks `dio_104t -> dio_00ly`, bei 12 und 24 Ticks balanciert.

Diese Welten zeigen keine feste Kette, sondern eine feldzeitliche Ausdehnung. Kurzfenster lesen lokale Reihenfolge, groessere Fenster lesen eher die gemeinsame Zone.

## MCM-Lesung

Der Befund spricht fuer einen gemeinsamen Feldbereich zwischen `dio_00ly` und `dio_104t`.

`dio_00ly` wirkt weiter als breite Uebergangsbruecke.  
`dio_104t` wirkt weiter als rekopplungsnahe Stabilitaetsbruecke.

Die beiden Familien stehen aber nicht als starre Ursache-Folge-Kette hintereinander. Sie bilden eher eine feldzeitliche Achsennaehe, deren Richtung von der Weltspannung und vom betrachteten Zeitfenster moduliert wird.

Damit wird die bisherige Lesart verstaerkt:

- `dio_00ly` und `dio_104t` gehoeren zu einem gemeinsamen Brueckenraum.
- Die Beziehung ist ueber Weltklassen hinweg robust.
- Die konkrete Richtung ist welt- und skalenabhaengig.
- Groessere Fenster zeigen mehr Feldzone, kleinere Fenster mehr lokale Reihenfolge.

## Grenze

Diese Pruefung zeigt Ticknaehe und Fensterstabilitaet. Sie beweist noch keine segmentgenaue Ursache.

Der naechste methodische Schritt ist deshalb eine Rohwelt-Ruecklesung der stabilen Richtungsfaelle:

- Was passiert in `KAS 2024 5m` und `Negative Stress 2024`, wenn `dio_00ly -> dio_104t` stabil erscheint?
- Was passiert in `BTC 2024 Quiet 5m`, wenn `dio_104t -> dio_00ly` stabil erscheint?
- Welche Weltmerkmale erzeugen balancierte Brueckennaehe?

## Kurzfazit

Die Achsenbeziehung ist skalenrobust, aber nicht richtungsstarr.

Das ist fachlich wichtig: MINI_DIO bildet keinen einfachen Ablaufplan, sondern einen Feldbereich, dessen innere Richtung je nach Weltspannung anders gelesen wird.

