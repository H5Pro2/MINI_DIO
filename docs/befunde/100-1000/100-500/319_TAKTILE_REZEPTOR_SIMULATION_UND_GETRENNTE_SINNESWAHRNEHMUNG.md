# 319 - Taktile Rezeptor-Simulation und getrennte Sinneswahrnehmung

## Grundfrage

Wie kann MINI_DIO spaeter eine taktile Wahrnehmung bekommen, ohne Sehen und Hoeren faelschlich als Fuehlen zu behandeln?

Die wichtige Korrektur lautet:

```text
Sehen + Hoeren ist nicht Fuehlen.
```

Sehen, Hoeren und Tasten muessen getrennte Sinnesachsen bleiben.

## Problem

Wenn visuelle und auditive Daten direkt zu `Fuehlen` verrechnet werden, entsteht ein Wahrnehmungsbrei.

Das waere fachlich falsch:

```text
visuelle Rezeptorwirkung
+ auditive Rezeptorwirkung
= nicht automatisch taktiles Fuehlen
```

Ein Organismus unterscheidet Sinnesarten:

- Ich sehe etwas.
- Ich hoere etwas.
- Ich beruehre etwas.
- Ich spuere, wie diese Wahrnehmung in mir wirkt.

Diese Ebenen duerfen nicht vermischt werden.

## Saubere Sinnesarchitektur

MINI_DIO sollte langfristig so gelesen werden:

```text
Sehen
  -> visuelle Rezeptoren
  -> visuelle Feldwirkung

Hoeren
  -> auditive Rezeptoren
  -> auditive Feldwirkung

Tasten
  -> taktile Rezeptoren
  -> taktile Feldwirkung

Innenwahrnehmung
  -> reflektive Lesung der eigenen Feldwirkung
```

Damit entsteht kein Gefuehlsbrei, sondern getrennte Wahrnehmung mit anschliessender Innenfeld-Deutung.

## Taktile Simulation

Da MINI_DIO aktuell keinen realen Hautkontakt besitzt, kann eine Mousepad- oder Flaechen-Simulation als kontrollierte taktile Welt dienen.

Moegliche Achsen:

- `contact_x`: Position der Beruehrung auf der Flaeche.
- `contact_y`: Position der Beruehrung auf der Flaeche.
- `contact_active`: ob ueberhaupt Beruehrung besteht.
- `contact_pressure`: simulierter Druck, zum Beispiel aus Klick, Hold-Dauer oder Eingabestaerke.
- `contact_motion`: Bewegung ueber die Flaeche.
- `contact_friction`: Widerstand/Reibung aus Geschwindigkeit, Richtungswechsel und Kontaktstabilitaet.
- `contact_stability`: bleibt die Beruehrung ruhig oder bricht sie?
- `contact_afterimage`: Nachhall der Beruehrung nach Kontaktende.

Die Kette waere:

```text
Mousepad / Kontaktflaeche
  -> taktile Rezeptoren
  -> taktile Kontaktqualitaet
  -> MCM-Feldwirkung
```

Wichtig:

```text
Das Mousepad ist kein Steuergeraet fuer Handlung.
Es ist zuerst ein passives Tastfeld.
```

## Reflektive Innenwahrnehmung

Eine getrennte Sinnesachse reicht nicht aus.

MINI_DIO muss auch unterscheiden koennen:

```text
Wie fuehlt sich diese Wahrnehmung an?
Was macht diese Wahrnehmung mit mir?
```

Das sind zwei verschiedene Ebenen.

### Reflektive Lesung

Reflektive Innenwahrnehmung fragt:

```text
Wie nehme ich diese Wahrnehmung in mir wahr?
```

Beispiele:

- Diese visuelle Form wirkt ruhig.
- Dieser Ton wirkt gespannt.
- Diese Beruehrung wirkt stabil.
- Diese Kombination wirkt offen.

Das ist eine innere Beobachtung der Sinneswirkung.

### Metaphysische Feldwirkung

Metaphysische MCM-Feldwirkung fragt:

```text
Was macht diese Wahrnehmung mit meinem Feld?
```

Beispiele:

- Sie zieht mich zum Zentrum.
- Sie drueckt mich an den Rand.
- Sie oeffnet eine Bruecke.
- Sie erzeugt Nachhall.
- Sie erzeugt Spannung, Entlastung oder Rekopplung.

Das ist nicht mehr nur Sinnesbeschreibung, sondern Feldwirkung.

## Zentrale Trennung

Die saubere Trennung lautet:

```text
Sinneswahrnehmung:
Was kommt ueber einen Sinneskanal an?

Reflektive Innenwahrnehmung:
Wie wirkt diese Wahrnehmung in mir?

MCM-Feldwirkung:
Was veraendert diese Wahrnehmung in meiner inneren Feldordnung?
```

Damit kann MINI_DIO mehrere Sinnesachsen halten, ohne sie zu vermischen.

## Bedeutung fuer die MCM-Schicht

Die MCM-Schicht bekommt keine Rohdaten und keinen Sinnesbrei.

Sie bekommt getrennte, rezeptorisch uebersetzte Feldwirkungen:

```text
visuelle Feldwirkung
auditive Feldwirkung
taktile Feldwirkung
```

Erst danach kann das Feld passiv ordnen:

- Zentrum,
- Rand,
- Bruecke,
- Drift,
- Nachhall,
- Rekopplung.

## Grenze

Diese Mechanik ist aktuell ein Bauplanpunkt.

Sie ist noch keine aktive taktile Implementierung.

Sie darf nicht als Handlung, Gate oder Steuerung gelesen werden.

## Wie es weitergeht

Als naechstes sollte die aktuelle Dokumentation sprachlich schaerfer trennen: `Fuehlen` in MINI_DIO meint derzeit MCM-Feldwirkung durch Rezeptorkontakt, nicht Hautkontakt. Erst eine spaetere taktile Simulation wuerde eine eigene Tastachse ergaenzen.
