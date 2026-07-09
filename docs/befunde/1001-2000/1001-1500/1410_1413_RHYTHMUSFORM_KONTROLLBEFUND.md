# 1410-1413 - Rhythmusform Kontrollbefund

## Zweck

Diese Pruefung trennt reine Wechselanzahl von Rhythmusform.

Die Grundfrage lautet:

Wirkt Mini-DIO nur auf die Menge der Richtungswechsel, oder liest das MCM-Feld auch die Form des Rhythmus?

## Welten

| Welt | Rhythmusform | Richtungswechsel | Quiet Score |
| --- | --- | ---: | ---: |
| RHYTHM_REGULAR | regelmaessiger Tickwechsel | 998 | 0.716998 |
| RHYTHM_BLOCK | Blockwechsel | 124 | 0.293447 |
| RHYTHM_IRREGULAR | unregelmaessiger Wechsel | 550 | 0.524601 |
| RHYTHM_WAVE | Wellenbewegung | 60 | 0.228581 |

## MINI_DIO Befund

| Welt | Symbole | stabil | tragend_unruhig | Carry | Rekopplung | Strain | Kopplung | Nachhall |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| RHYTHM_REGULAR | 24 | 712 | 282 | 0.555928 | 0.713970 | 0.150471 | 0.826495 | 0.425093 |
| RHYTHM_BLOCK | 27 | 874 | 120 | 0.579223 | 0.734859 | 0.122595 | 0.883722 | 0.482436 |
| RHYTHM_IRREGULAR | 46 | 783 | 211 | 0.554452 | 0.717053 | 0.139958 | 0.841537 | 0.392353 |
| RHYTHM_WAVE | 37 | 994 | 0 | 0.575977 | 0.737141 | 0.119177 | 0.901279 | 0.460114 |

## Lesung

Die Feldreaktion ist nicht linear an die Wechselanzahl gekoppelt.

Der regelmaessige Tickwechsel erzeugt trotz weniger Symbolvarianz deutlich mehr `tragend_unruhig` als die Wellenwelt. Die Wellenwelt bleibt vollstaendig stabil, obwohl sie nicht statisch ist. Der Blockrhythmus wird stabiler getragen als der regelmaessige Tickwechsel.

Damit zeigt sich:

- Rhythmusform wirkt als eigene Weltqualitaet.
- Wechselanzahl allein erklaert die Innenfeldwirkung nicht.
- Sanfte Rhythmusbewegung kann stabiler sein als harte Taktumkehr.
- Die Kopplung steigt bei block- und wellenfoermiger Bewegung.
- `tragend_unruhig` entsteht vor allem dort, wo die Welt einen schnellen oder unregelmaessigen Richtungszug erzeugt.

## Forschungsgrenze

Das ist kein Beweis fuer eine vollstaendige Rhythmussemantik.

Der Befund zeigt aber, dass Mini-DIO nicht nur Rohwerte liest. Das Feld reagiert differenziert auf zeitliche Formqualitaet: regelmaessig, blockhaft, unregelmaessig oder wellenfoermig.
