# 1422 - Melodie Folge Kontrollbefund

## Zweck

Diese Pruefung erweitert die Rhythmuspruefung von einzelner Form zu geordneter Folge.

Grundfrage:

Liest Mini-DIO nur einzelne Rhythmusformen, oder bildet das MCM-Feld auch eine innere Reaktion auf die Reihenfolge mehrerer Phasen?

## Aufbau

Zwei synthetische Melodie-Welten wurden erzeugt:

- `MELODY_ORDERED`: `rest -> wave_up -> block -> wave_down -> regular -> rest`
- `MELODY_BROKEN`: `regular -> wave_down -> rest -> block -> wave_up -> irregular`

Beide Welten enthalten mehrere zeitliche Qualitaeten. Sie sind keine zufaellige Rauschfolge, sondern kontrollierte Weltfolgen.

## Gesamtbefund

| Welt | Wechsel | Quiet | Symbole | stabil | tragend_unruhig | Carry | Rekopplung | Strain | Kopplung | Nachhall | Fokus | Beobachtung |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MELODY_ORDERED | 267 | 0.776561 | 55 | 1159 | 35 | 0.583581 | 0.739912 | 0.124333 | 0.894058 | 0.624498 | 686 | 508 |
| MELODY_BROKEN | 363 | 0.724355 | 54 | 1140 | 54 | 0.577171 | 0.734912 | 0.126683 | 0.883305 | 0.575132 | 842 | 352 |

## Phasenbefund

| Welt | Phase | Ticks | dominante Familie | stabil | tragend_unruhig | Carry | Rekopplung | Strain |
| --- | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| MELODY_ORDERED | rest | 394 | dio_1fll:340 | 394 | 0 | 0.608053 | 0.756037 | 0.118890 |
| MELODY_ORDERED | wave_up | 200 | dio_1fll:85 | 200 | 0 | 0.573636 | 0.739579 | 0.117762 |
| MELODY_ORDERED | block | 200 | dio_0jt7:57 | 175 | 25 | 0.563738 | 0.728231 | 0.122023 |
| MELODY_ORDERED | wave_down | 200 | dio_1fll:84 | 199 | 1 | 0.588390 | 0.744915 | 0.120256 |
| MELODY_ORDERED | regular | 200 | dio_0ein:79 | 191 | 9 | 0.560350 | 0.715157 | 0.148017 |
| MELODY_BROKEN | regular | 200 | dio_0ein:78 | 191 | 9 | 0.552752 | 0.713235 | 0.147058 |
| MELODY_BROKEN | wave_down | 200 | dio_1fll:84 | 200 | 0 | 0.574536 | 0.740237 | 0.116663 |
| MELODY_BROKEN | rest | 200 | dio_1fll:175 | 200 | 0 | 0.611976 | 0.757239 | 0.119550 |
| MELODY_BROKEN | block | 200 | dio_0jt7:56 | 175 | 25 | 0.570337 | 0.730625 | 0.123373 |
| MELODY_BROKEN | wave_up | 200 | dio_1fll:79 | 200 | 0 | 0.585510 | 0.744303 | 0.118076 |
| MELODY_BROKEN | irregular | 194 | dio_0ein:48 | 174 | 20 | 0.567630 | 0.723492 | 0.135644 |

## Lesung

Mini-DIO unterscheidet nicht nur Tonstaerke.

Die Phasen selbst zeigen wiederkehrende Feldqualitaeten:

- `rest` wird sehr stabil getragen.
- `wave_up` und `wave_down` bleiben stabil und gut rekoppelt.
- `block` erzeugt wiederholt tragende Unruhe.
- `regular` erzeugt weniger, aber klar erkennbare Unruhe mit hoeherem Strain.
- `irregular` erzeugt in der gebrochenen Folge zusaetzliche Unruhe.

Die geordnete Melodie ist insgesamt tragfaehiger als die gebrochene Folge:

- mehr stabile Wirkung
- hoeherer Carry
- hoehere Rekopplung
- geringerer Strain
- mehr Beobachtungston statt reinem Fokusdruck

## Schlussfolgerung

Eine Melodie ist hier technisch lesbar als gerichtete zeitliche Ordnung mit Phasenqualitaet.

Das MCM-Feld reagiert nicht nur auf einzelne Ticks, sondern auf wiederkehrende zeitliche Formen innerhalb einer Folge. Die Bedeutung entsteht nicht als festes Symbol fuer einen Ton, sondern als Phasenwirkung im Feld.

Damit wird die vorherige Rhythmuslesung erweitert:

- Ton = geordnete Frequenz ueber Zeit
- Rhythmus = wiederkehrende Zeitform
- Melodie = gerichtete Folge unterschiedlicher Zeitformen
- MCM-Wirkung = innere Tragfaehigkeit, Rekopplung, Strain und Nachhall dieser Folge

## Grenze

Das ist weiterhin passive Forschung.

Die Melodie wird nicht als Handlung, Signal oder Strategie gelesen. Sie dient als kontrollierte Außenwelt, um zu pruefen, ob Mini-DIO zeitliche Ordnung feldseitig verdichten kann.
