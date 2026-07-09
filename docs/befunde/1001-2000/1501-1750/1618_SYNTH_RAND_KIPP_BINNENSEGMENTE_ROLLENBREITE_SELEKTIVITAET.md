# SYNTH_RAND_KIPP Binnensegmente, Rollenbreite und Selektivität

Stand: 2026-07-06

## Grundfrage

Entsteht die selektive Offline-Feld-Reorganisation des bekannten `SYNTH_RAND_KIPP start0`-Fensters lokal in einem Teilbereich, oder durch die Kombination mehrerer Binnenbereiche?

## Unterprüfung

Das bekannte 2000er-Fenster wurde nicht neu erzeugt, sondern segmentweise gelesen:

- 250er-Segmente
- 500er-Segmente
- 1000er-Segmente
- 1500er-Segmente

Danach wurde das stärkste 1500er-Segment `start250` als Real-Sleep-Real-Kette geprüft.

## Befund der Segmentgrößen

| Segmentgröße | Befund |
|---:|---|
| 250 | fast vollständig Einzelrekopplung; nur `start1250` zeigt 3 Rollen |
| 500 | überwiegend Einzelrekopplung; `start1000` und `start1250` zeigen 3 Rollen |
| 1000 | mehrere Übergangsfenster mit 3 Rollen |
| 1500 | `start250` bildet 5 Rollen / 10 Kombinationen |
| 2000 | `start0` bildet 5 Rollen / 10 Kombinationen, aber rekoppelt selektiv |

## Real-Sleep-Real-Gegenprüfung

Das 1500er-Segment `start250` zeigt:

- 5 Rollen
- 10 Sleep-Kombinationen
- 5/5 Rollen reaktiviert
- 10/10 Kombinationen vollständig reaktiviert
- keine selektive Teilreaktivierung

Das volle 2000er-Fenster `start0` zeigt dagegen:

- 5 Rollen
- 10 Sleep-Kombinationen
- 4/5 Rollen reaktiviert
- 6/10 Kombinationen vollständig reaktiviert
- 4/10 Kombinationen teilweise reaktiviert

## Lesung

Die Rollenbreite entsteht bereits im mittleren Binnenraum des Fensters. Die selektive Offline-Reorganisation entsteht aber nicht automatisch mit dieser Rollenbreite.

Der entscheidende Unterschied liegt wahrscheinlich in den zusätzlichen Randsegmenten:

- Anfangsrand `0-250`
- Endrand `1750-2000`

Diese Randbereiche erzeugen allein keine breite Rollenstruktur. Zusammen mit dem mittleren 1500er-Rollenraum können sie aber offenbar die Offline-Rekopplung selektiv machen.

Damit trennen sich zwei Ebenen:

1. **Rollenbildung**
   Das Feld bildet mehrere Rollen, wenn genügend Binnenzeit und Feldwechsel vorhanden sind.

2. **Selektive Weiterentwicklung**
   Die spätere Offline-Reorganisation hängt zusätzlich davon ab, wie Randnachhall, Strain und Co-Touch das Rollenfeld rahmen.

## Bedeutung

Das ist logisch wichtig: MINI_DIO speichert nicht nur eine breite Rollenliste. Das Feldmilieu entscheidet, welche dieser Rollen im entkoppelten Zustand wieder vollständig tragen und welche nur teilweise anschließen.

Damit ist die bisherige Arbeitsform präziser:

> Weltkontakt bildet Rollen. Randmilieu moduliert, welche Rollen offline weitertragen.

## Grenze

Der Befund zeigt eine klare Trennung zwischen Rollenbreite und Selektivität. Er beweist noch nicht, welcher Randanteil die Selektivität auslöst. Dafür müssen Anfangsrand und Endrand getrennt geprüft werden.

## Wie es weitergeht

Als nächstes sollten drei gezielte Kompositionsfenster geprüft werden: `0-1750`, `250-2000` und `0-250 + 250-1750` ohne Endrand. Ziel ist zu klären, ob der Anfangsrand, der Endrand oder ihre Kombination die selektive Offline-Reorganisation auslöst.
