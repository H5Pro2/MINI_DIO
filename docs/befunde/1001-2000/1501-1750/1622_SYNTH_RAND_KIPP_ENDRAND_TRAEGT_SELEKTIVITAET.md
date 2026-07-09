# SYNTH_RAND_KIPP Endrand und selektive Offline-Reorganisation

Stand: 2026-07-06

## Grundfrage

Welcher Randanteil des selektiven `SYNTH_RAND_KIPP start0`-Fensters trägt die selektive Offline-Reorganisation?

## Unterprüfung

Aus dem bekannten 2000er-Fenster wurden zwei 1750er-Kompositionsfenster erzeugt:

- `OHNE_ENDRAND`: Bereich `0-1750`
- `OHNE_ANFANGSRAND`: Bereich `250-2000`

Beide Fenster bilden 5 Rollen und 10 Sleep-Kombinationen. Dadurch kann geprüft werden, ob die selektive Reorganisation vom Anfangsrand oder vom Endrand abhängt.

## Befund

| Fenster | Rollen | Kombinationen | Rollen reaktiviert | Kombinationen voll | Kombinationen teilweise | Ergebnis |
|---|---:|---:|---:|---:|---:|---|
| `OHNE_ENDRAND` | 5 | 10 | 5/5 | 10/10 | 0/10 | voll fokussiert |
| `OHNE_ANFANGSRAND` | 5 | 10 | 4/5 | 6/10 | 4/10 | selektiv |
| volles `start0` | 5 | 10 | 4/5 | 6/10 | 4/10 | selektiv |

## Lesung

Die Rollenbreite allein reicht erneut nicht aus. Beide 1750er-Fenster tragen dieselbe Breite: 5 Rollen und 10 Kombinationen.

Der Unterschied liegt in der Randkomposition:

- Wenn der Endrand fehlt, rekoppelt das Feld vollständig.
- Wenn der Anfangsrand fehlt, bleibt die selektive Struktur erhalten.

Damit ist der Endrand beziehungsweise die späte Rand-/Nachhallphase der wahrscheinlichere Träger der selektiven Offline-Reorganisation.

## Bedeutung

Das Feld bildet Rollen im Binnenraum, aber der spätere Rand bestimmt, ob diese Rollen offline vollständig zusammenfinden oder selektiv bleiben.

Kurzform:

> Binnenraum bildet Rollen. Endrand moduliert Selektivität.

Das ist eine präzisere Form der bisherigen Feldmilieu-Hypothese.

## Grenze

Der Befund lokalisiert die Wirkung auf den Endbereich, beweist aber noch nicht, welche Eigenschaft dort entscheidend ist. Möglich sind:

- späte Strain-Rolle
- Nachhallform
- Co-Touch-Verteilung
- Übergang von Rekopplung in Randspannung
- Verhältnis von stabilen und gespannten Rollen am Ende
