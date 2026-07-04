# 1433 - Melodie Blockrahmung Isolation

## Zweck

Diese Pruefung isoliert den dritten Faktor aus dem `1428`-Kipppunkt:

Blockrahmung.

Grundfrage:

Reicht Blockrahmung am Anfang und Ende, ohne doppelte Irregularitaet, um die Dominanz von `dio_1fll` zu `dio_0ein` zu verschieben?

## Aufbau

`1431`:

`block -> wave_up -> block -> wave_down -> irregular -> regular`

`1432`:

`rest -> irregular -> wave_down -> irregular -> regular -> rest`

`1433`:

`block -> wave_up -> regular -> wave_down -> regular -> block`

`1428`:

`block -> irregular -> regular -> wave_down -> irregular -> block`

`1433` behaelt die Blockrahmung, entfernt aber die doppelte Irregularitaet.

## Rohwelt

| Welt | Richtungswechsel | avg_abs_return | avg_range | Drift | Max DD | Quiet Score |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1433 | 474 | 0.000901 | 0.004358 | 0.026252 | 0.070415 | 0.367473 |

## Gesamtvergleich

| Welt | Symbole | stabil | tragend_unruhig | dominant | zweites Symbol | Carry | Rekopplung | Strain | Kopplung | Nachhall | Fokus | Beobachtung |
| --- | ---: | ---: | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1431_NO_REST_SINGLE_IRREGULAR | 53 | 1118 | 76 | `dio_1fllaqz` | `dio_0eindxe` | 0.573338 | 0.732059 | 0.126514 | 0.878326 | 0.517223 | 1013 | 181 |
| 1432_DOUBLE_IRREGULAR_WITH_REST | 49 | 1106 | 88 | `dio_1fllaqz` | `dio_0eindxe` | 0.577041 | 0.733721 | 0.130061 | 0.875480 | 0.588876 | 806 | 388 |
| 1433_BLOCK_FRAME_NO_DOUBLE_IRREGULAR | 52 | 1126 | 68 | `dio_0eindxe` | `dio_1fllaqz` | 0.573210 | 0.730389 | 0.129541 | 0.873480 | 0.539929 | 1022 | 172 |
| 1428_STRONGLY_BROKEN | 47 | 1102 | 92 | `dio_0eindxe` | `dio_0v65ujo` | 0.572284 | 0.729330 | 0.130062 | 0.867700 | 0.518075 | 1079 | 115 |

## Befund

Blockrahmung ohne doppelte Irregularitaet verschiebt die Oberflaechen-Dominanz knapp zu `dio_0ein`.

Die beiden Laeufe von `1433` reproduzieren exakt dieselbe Symbolreihenfolge:

- `dio_0eindxe:182`
- `dio_1fllaqz:170`
- `dio_0v65ujo:152`

Damit ist `1433` kein voller `1428`-Kipppunkt, aber klar naeher an `1428` als `1432`.

## Lesung

Die Blockrahmung scheint eine starke Ordnungswirkung zu besitzen.

Sie erzeugt nicht automatisch mehr `tragend_unruhig` als `1432`, aber sie verschiebt die Bedeutungsnaehe:

- `1432`: alte Familie `dio_1fll` bleibt klar fuehrend.
- `1433`: `dio_0ein` wird knapp fuehrend.
- `1428`: `dio_0ein` wird deutlich fuehrend und `dio_1fll` faellt stark zurueck.

Das spricht dafuer, dass die Rahmung nicht nur Belastung erzeugt, sondern den Bedeutungsraum anders bindet.

## Schlussfolgerung

Der `1428`-Kipppunkt ist wahrscheinlich eine Kopplung aus:

1. Blockrahmung,
2. doppelter Irregularitaet,
3. Ruheverlust,
4. sinkendem Nachhall,
5. steigender Fokusdominanz bei schwacher Beobachtung.

`1433` zeigt, dass Blockrahmung allein bereits die Richtung der Dominanzverschiebung vorbereitet.

Sie reicht aber nicht aus, um die volle `1428`-Struktur zu erzeugen.

## Grenze

Die Blockrahmung wurde hier mit positiver Drift erzeugt. Dadurch ist noch offen, ob die Verschiebung durch die Rahmung selbst, durch Drift oder durch deren Kopplung entsteht.

## Wie es weitergeht

Als naechstes sollte die Drift isoliert werden: gleiche Blockrahmung wie `1433`, aber neutralere Drift oder Gegenrichtung. Dann pruefen wir, ob `dio_0ein` aus der Rahmung selbst entsteht oder aus Rahmung plus gerichteter Weltbewegung.
