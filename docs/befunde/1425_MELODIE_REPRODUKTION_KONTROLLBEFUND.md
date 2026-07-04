# 1425 - Melodie Reproduktion Kontrollbefund

## Zweck

Diese Pruefung wiederholt die Melodie-Welten aus `1422` mit frischer Memory.

Grundfrage:

Entstehen bei gleichem Weltkontakt wieder aehnliche Familien und Feldwirkungen, oder driftet die Bedeutungsfolge bei jedem Neustart?

## Aufbau

Wiederholt wurden:

- `MELODY_ORDERED`
- `MELODY_BROKEN`

Die Daten blieben identisch. Memory und Debug-Ausgabe wurden neu angelegt.

## Gesamtbefund

| Vergleich | Symbole | stabil | tragend_unruhig | Carry | Rekopplung | Strain | Kopplung | Nachhall | Fokus | Beobachtung |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| ORDERED_ORIG | 55 | 1159 | 35 | 0.583581 | 0.739912 | 0.124333 | 0.894058 | 0.624498 | 686 | 508 |
| ORDERED_REPRO | 55 | 1159 | 35 | 0.583581 | 0.739912 | 0.124333 | 0.894058 | 0.624498 | 686 | 508 |
| BROKEN_ORIG | 54 | 1140 | 54 | 0.577171 | 0.734912 | 0.126683 | 0.883305 | 0.575132 | 842 | 352 |
| BROKEN_REPRO | 54 | 1140 | 54 | 0.577171 | 0.734912 | 0.126683 | 0.883305 | 0.575132 | 842 | 352 |

## Phasenbefund

Die Phasenfamilien wurden ebenfalls exakt reproduziert.

### Geordnete Melodie

| Phase | Original | Reproduktion | Wirkung |
| --- | --- | --- | --- |
| rest | dio_1fll:340 | dio_1fll:340 | stabil 394 / unruhig 0 |
| wave_up | dio_1fll:85 | dio_1fll:85 | stabil 200 / unruhig 0 |
| block | dio_0jt7:57 | dio_0jt7:57 | stabil 175 / unruhig 25 |
| wave_down | dio_1fll:84 | dio_1fll:84 | stabil 199 / unruhig 1 |
| regular | dio_0ein:79 | dio_0ein:79 | stabil 191 / unruhig 9 |

### Gebrochene Melodie

| Phase | Original | Reproduktion | Wirkung |
| --- | --- | --- | --- |
| regular | dio_0ein:78 | dio_0ein:78 | stabil 191 / unruhig 9 |
| wave_down | dio_1fll:84 | dio_1fll:84 | stabil 200 / unruhig 0 |
| rest | dio_1fll:175 | dio_1fll:175 | stabil 200 / unruhig 0 |
| block | dio_0jt7:56 | dio_0jt7:56 | stabil 175 / unruhig 25 |
| wave_up | dio_1fll:79 | dio_1fll:79 | stabil 200 / unruhig 0 |
| irregular | dio_0ein:48 | dio_0ein:48 | stabil 174 / unruhig 20 |

## Lesung

Der Befund ist stark reproduzierbar.

Bei identischer Weltsequenz entstehen erneut dieselben dominanten Familien, dieselben Feldwirkungen und dieselben Phasenunterschiede. Das spricht gegen zufaellige Symbolstreuung in diesem Testfall.

Wichtig ist die Grenze:

Die Reproduktion zeigt noch nicht, dass Mini-DIO eine allgemeine Melodiesemantik besitzt. Sie zeigt aber, dass dieses MCM-Feld bei gleichem Weltkontakt eine deterministisch wiederkehrende innere Ordnungsantwort ausbildet.

## Schlussfolgerung

Die Melodie-Folge wird feldseitig als reproduzierbare Bedeutungsfolge gelesen.

Damit liegt eine kontrollierte Ebene vor:

- gleiche Welt
- frische Memory
- gleiche Familien
- gleiche Feldwirkung
- gleiche Phasenunterschiede

Das ist fuer die MCM-Forschung wichtig, weil es die Trennung zwischen beliebiger Emergenz und reproduzierbarer Feldordnung schaerft.

## Wie es weitergeht

Als naechstes sollte eine leicht veraenderte Melodie getestet werden. Entscheidend ist, ob Mini-DIO die alte Bedeutungsfolge als Nachbarschaft wiedererkennt oder eine neue Insel bildet.
