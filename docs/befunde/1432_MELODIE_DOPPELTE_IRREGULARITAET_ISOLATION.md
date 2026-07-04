# 1432 - Melodie Doppelte Irregularitaet Isolation

## Zweck

Diese Pruefung isoliert den zweiten Faktor aus dem `1428`-Kipppunkt:

doppelte Irregularitaet.

Grundfrage:

Reicht doppelte Irregularitaet bei erhaltenen Ruhephasen, damit `dio_0ein` die Dominanz von `dio_1fll` uebernimmt?

## Aufbau

`1430`:

`rest -> block -> wave_down -> irregular -> regular -> rest`

`1431`:

`block -> wave_up -> block -> wave_down -> irregular -> regular`

`1432`:

`rest -> irregular -> wave_down -> irregular -> regular -> rest`

`1428`:

`block -> irregular -> regular -> wave_down -> irregular -> block`

`1432` enthaelt zwei Irregularitaetsphasen, aber Ruhe bleibt am Anfang und Ende erhalten.

## Rohwelt

| Welt | Richtungswechsel | avg_abs_return | avg_range | Drift | Max DD | Quiet Score |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1432 | 447 | 0.000696 | 0.004152 | -0.059490 | 0.075659 | 0.693431 |

## Gesamtvergleich

| Welt | Symbole | stabil | tragend_unruhig | dominant | zweites Symbol | Carry | Rekopplung | Strain | Kopplung | Nachhall | Fokus | Beobachtung |
| --- | ---: | ---: | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1430_THRESHOLD_MID | 48 | 1139 | 55 | `dio_1fllaqz` | `dio_0eindxe` | 0.581064 | 0.736879 | 0.126924 | 0.884080 | 0.606884 | 761 | 433 |
| 1431_NO_REST_SINGLE_IRREGULAR | 53 | 1118 | 76 | `dio_1fllaqz` | `dio_0eindxe` | 0.573338 | 0.732059 | 0.126514 | 0.878326 | 0.517223 | 1013 | 181 |
| 1432_DOUBLE_IRREGULAR_WITH_REST | 49 | 1106 | 88 | `dio_1fllaqz` | `dio_0eindxe` | 0.577041 | 0.733721 | 0.130061 | 0.875480 | 0.588876 | 806 | 388 |
| 1428_STRONGLY_BROKEN | 47 | 1102 | 92 | `dio_0eindxe` | `dio_0v65ujo` | 0.572284 | 0.729330 | 0.130062 | 0.867700 | 0.518075 | 1079 | 115 |

## Befund

Doppelte Irregularitaet allein reicht noch nicht fuer den Dominanzwechsel.

`1432` erzeugt fast dieselbe Menge `tragend_unruhig` wie `1428`:

- `1432`: 88
- `1428`: 92

Trotzdem bleibt `dio_1fllaqz` fuehrend:

- `1432`: `dio_1fllaqz:313`, `dio_0eindxe:159`
- `1428`: `dio_0eindxe:197`, `dio_1fllaqz:84`

Das bedeutet:

Doppelte Irregularitaet erzeugt starke Feldspannung, aber mit erhaltener Ruhe bleibt die alte Grundfamilie noch tragfaehig.

## Lesung

Die beiden isolierten Faktoren wirken unterschiedlich:

- `1431` zeigt starken Nachhallverlust und starken Fokusanstieg.
- `1432` zeigt hohe unruhige Tragwirkung, aber Nachhall bleibt deutlich hoeher als bei `1428`.
- `1428` kombiniert beides: niedriger Nachhall, hohe unruhige Tragwirkung, niedrige Beobachtung und Dominanzwechsel.

Damit wird die Schwelle als kombinatorisch lesbar.

Nicht ein einzelner Faktor kippt das Feld, sondern die Kopplung mehrerer Strukturwirkungen:

1. Ruheverlust,
2. doppelte Irregularitaet,
3. gebrochene Blockrahmung,
4. fallender Nachhall,
5. Fokusdominanz bei schwacher Beobachtung.

## Schlussfolgerung

Mini-DIO reagiert nicht linear auf einzelne Belastungsmerkmale.

Der Melodie-Kipppunkt entsteht offenbar erst, wenn mehrere Feldbedingungen zusammenfallen. Das ist fuer die MCM-Forschung wichtig, weil die Bedeutungsdominanz nicht einfach aus einer Einzelvariable entsteht, sondern aus einer Feldkonfiguration.

## Grenze

Die konkrete Rolle der Blockrahmung ist noch nicht isoliert.

`1432` zeigt nur, dass doppelte Irregularitaet bei vorhandener Ruhe nicht ausreicht.

## Wie es weitergeht

Als naechstes sollte die Blockrahmung isoliert werden: Block am Anfang und Ende, aber ohne doppelte Irregularitaet. Dann pruefen wir, ob die Rahmung selbst die Dominanzverschiebung vorbereitet.
