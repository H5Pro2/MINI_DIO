# 1426 - Melodie Variante Nachbarschaft

## Zweck

Diese Pruefung veraendert die geordnete Melodie aus `1422` nur leicht.

Grundfrage:

Erkennt Mini-DIO die veraenderte Melodie als Nachbarschaft der alten Bedeutungsfolge, oder entsteht eine neue Insel?

## Aufbau

Original:

`rest -> wave_up -> block -> wave_down -> regular -> rest`

Variante:

`rest -> wave_up -> block -> wave_down -> irregular -> rest`

Nur die fuenfte aktive Phase wurde ersetzt.

## Gesamtbefund

| Welt | Symbole | stabil | tragend_unruhig | Carry | Rekopplung | Strain | Kopplung | Nachhall | Fokus | Beobachtung |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| ORDERED_ORIG | 55 | 1159 | 35 | 0.583581 | 0.739912 | 0.124333 | 0.894058 | 0.624498 | 686 | 508 |
| ORDERED_VARIANT | 59 | 1151 | 43 | 0.583025 | 0.740631 | 0.122323 | 0.896905 | 0.606100 | 691 | 503 |

## Phasenvergleich

| Phase | Original | Variante | Lesung |
| --- | --- | --- | --- |
| rest | dio_1fll:340 | dio_1fll:340 | nahezu identisch |
| wave_up | dio_1fll:85 | dio_1fll:85 | identisch |
| block | dio_0jt7:57 | dio_0jt7:57 | identisch |
| wave_down | dio_1fll:84 | dio_1fll:84 | identisch |
| regular / irregular | dio_0ein:79 | dio_0ein:53 | gleiche Nachbarschaft, andere Lastform |

## Lesung

Die Variante bildet keine komplett neue Insel.

Die ersten vier Phasen bleiben praktisch deckungsgleich. Die dominante Grundfamilie `dio_1fll` bleibt mit exakt gleicher Top-Symbolzahl erhalten. Auch `block` bleibt bei `dio_0jt7`.

Die ersetzte Phase bleibt in der Nachbarschaft von `dio_0ein`, verschiebt aber die Wirkung:

- `regular`: stabil 191 / unruhig 9 / Strain 0.148017
- `irregular`: stabil 183 / unruhig 17 / Strain 0.135946

Das spricht fuer eine Nachbarschaftslesung:

Die Melodie wird als gleiche Grundordnung getragen, aber die veraenderte Phase erzeugt eine andere Innenfeldnuance.

## Schlussfolgerung

Mini-DIO behandelt die veraenderte Melodie nicht als voellig fremde Welt.

Das Feld erkennt die gemeinsame Struktur wieder und lokalisiert die Abweichung in der betroffenen Phase. Damit entsteht keine neue Gesamtinsel, sondern eine variantische Bedeutungsnaehe innerhalb der bestehenden Melodieordnung.

## Grenze

Das ist eine kontrollierte synthetische Pruefung.

Sie zeigt nicht, dass Mini-DIO beliebige Melodien versteht. Sie zeigt aber, dass eine leicht veraenderte Folge feldseitig als nahe Ordnung mit lokaler Abweichung gelesen werden kann.

## Wie es weitergeht

Als naechstes sollte die Abweichung staerker gemacht werden: zwei Phasen ersetzen oder die Reihenfolge verschieben. Dann pruefen wir, ab wann Nachbarschaft in neue Inselbildung kippt.
