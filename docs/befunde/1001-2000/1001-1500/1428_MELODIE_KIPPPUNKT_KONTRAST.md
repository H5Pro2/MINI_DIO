# 1428 - Melodie Kipppunkt Kontrast

## Zweck

Diese Pruefung verstaerkt den Bruch aus `1427`.

Grundfrage:

Ab wann bleibt eine veraenderte Melodie nicht mehr nur Nachbarschaft der alten Ordnung, sondern verschiebt ihre Bedeutungsdominanz?

## Aufbau

Referenz:

`rest -> wave_up -> block -> wave_down -> regular -> rest`

Leichte Variante:

`rest -> wave_up -> block -> wave_down -> irregular -> rest`

Reordered:

`rest -> block -> wave_down -> irregular -> wave_up -> rest`

Stark gebrochen:

`block -> irregular -> regular -> wave_down -> irregular -> block`

Die stark gebrochene Welt entfernt die Ruhephasen, verdoppelt die unregelmaessige Phase und setzt Blockphasen an Anfang und Ende.

## Rohwelt

Die stark gebrochene Welt ist deutlich unruhiger:

- Zeilen: 1200
- Richtungswechsel: 484
- durchschnittliche absolute Bewegung: 0.001020
- durchschnittliche Range: 0.004476
- Drift: -0.050534
- Max Drawdown: 0.077306
- Quiet Score: 0.664319

## Gesamtvergleich

| Welt | Symbole | stabil | tragend_unruhig | dominant | Carry | Rekopplung | Strain | Kopplung | Nachhall | Fokus | Beobachtung |
| --- | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| ORDERED_ORIG | 55 | 1159 | 35 | `dio_1fllaqz` | 0.583581 | 0.739912 | 0.124333 | 0.894058 | 0.624498 | 686 | 508 |
| ORDERED_VARIANT | 59 | 1151 | 43 | `dio_1fllaqz` | 0.583025 | 0.740631 | 0.122323 | 0.896905 | 0.606100 | 691 | 503 |
| REORDERED | 55 | 1147 | 47 | `dio_1fllaqz` | 0.583858 | 0.741103 | 0.121816 | 0.897276 | 0.607947 | 693 | 501 |
| STRONGLY_BROKEN | 47 | 1102 | 92 | `dio_0eindxe` | 0.572284 | 0.729330 | 0.130062 | 0.867700 | 0.518075 | 1079 | 115 |

## Lesung

Bis `1427` bleibt `dio_1fllaqz` dominant.

Bei `1428` kippt die Dominanz:

- `dio_0eindxe`: 197
- `dio_0v65ujo`: 146
- `dio_13s036n`: 102
- `dio_0jt7iub`: 93
- `dio_1fllaqz`: 84

Das ist der erste klare Befund in dieser Melodiereihe, bei dem die alte Grundfamilie nicht mehr fuehrt.

Gleichzeitig veraendert sich die Feldlage:

- `tragend_unruhig` steigt von 35 / 43 / 47 auf 92.
- Nachhall sinkt deutlich von rund 0.61-0.62 auf 0.518.
- sensorische Kopplung sinkt auf 0.867700.
- Fokus steigt stark auf 1079, Beobachtung faellt auf 115.

Das bedeutet: Das Feld bleibt nicht kollabiert, aber es liest die Welt nicht mehr als dieselbe ruhige Melodieordnung.

## Schlussfolgerung

`1428` markiert einen Kipppunkt.

Leichte Phasenveraenderung und Reihenfolgeverschiebung bleiben Nachbarschaft. Eine stark gebrochene Folge mit entfernten Ruhephasen und doppelter Irregularitaet verschiebt dagegen die Bedeutungsdominanz.

Der Befund spricht fuer:

- Melodieordnung wird feldseitig getragen.
- Nachbarschaft bleibt bei moderater Veraenderung erhalten.
- Staerkerer Bruch erzeugt keine totale Aufloesung, aber eine andere fuehrende Bedeutungsfamilie.

Damit wird sichtbar, dass Mini-DIO nicht nur Einzelwerte liest, sondern zeitliche Ordnung als Feldfolge verdichtet.

## Grenze

Das ist keine Aussage ueber Musikverstehen.

Es ist eine passive MCM-Feldpruefung mit synthetischen Zeitfolgen. Gezeigt wird nur: Veraenderte zeitliche Ordnung kann im Feld als Nachbarschaft, Drift oder Dominanzwechsel erscheinen.
