# 1435/1436 - Melodie Blockgroesse Kontrast

## Zweck

Diese Pruefung variiert die Blockgroesse innerhalb derselben Blockrahmung.

Grundfrage:

Reagiert `dio_0ein` auf Blockrahmung allgemein oder auf eine bestimmte Blockdichte?

## Aufbau

Alle Welten nutzen dieselbe Formfolge:

`block -> wave_up -> regular -> wave_down -> regular -> block`

Die Drift ist neutralisiert.

Variiert wird nur die Blockgroesse:

- `1435`: block_size 4
- `1434`: block_size 8
- `1436`: block_size 16

## Rohwelt

| Welt | Blockgroesse | Richtungswechsel | Drift | Quiet Score |
| --- | ---: | ---: | ---: | ---: |
| 1435 | 4 | 523 | -0.018699 | 0.302085 |
| 1434 | 8 | 474 | -0.000464 | 0.367473 |
| 1436 | 16 | 450 | -0.000476 | 0.399500 |

## Gesamtvergleich

| Welt | Symbole | stabil | tragend_unruhig | dominant | zweites Symbol | Carry | Rekopplung | Strain | Kopplung | Nachhall | Fokus | Beobachtung |
| --- | ---: | ---: | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1435_BS4 | 53 | 1072 | 122 | `dio_0eindxe` | `dio_1fllaqz` | 0.566670 | 0.726805 | 0.130942 | 0.864521 | 0.456621 | 957 | 237 |
| 1434_BS8_NEUTRAL | 52 | 1115 | 79 | `dio_0eindxe` | `dio_1fllaqz` | 0.573485 | 0.730320 | 0.130022 | 0.872960 | 0.545979 | 1020 | 174 |
| 1436_BS16 | 49 | 1142 | 52 | `dio_1fllaqz` | `dio_0eindxe` | 0.577496 | 0.732936 | 0.128885 | 0.878344 | 0.584819 | 978 | 216 |

## Befund

Die Blockgroesse veraendert die Bedeutungsordnung.

Kurze Bloecke (`1435`, block_size 4) erzeugen:

- mehr `tragend_unruhig`,
- niedrigere Rekopplung,
- niedrigeren Nachhall,
- klare `dio_0ein`-Dominanz.

Mittlere Bloecke (`1434`, block_size 8) halten `dio_0ein` knapp vorne.

Lange Bloecke (`1436`, block_size 16) lassen `dio_1fll` wieder knapp fuehrend werden.

## Lesung

Blockrahmung ist nicht nur vorhanden oder nicht vorhanden.

Die zeitliche Dichte der Blockrahmung wirkt als Feldparameter:

- kurze Blockwechsel wirken spannungsreicher und ziehen `dio_0ein` naeher nach vorne,
- lange Blockwechsel wirken ruhiger und erlauben `dio_1fll` wieder als tragendere Grundfamilie.

Das passt zur bisherigen Melodie-Lesung:

Mini-DIO liest nicht nur einzelne Frequenzen oder einzelne Formen, sondern eine geordnete zeitliche Struktur.

## Schlussfolgerung

Der Melodie-Kipppunkt entsteht nicht aus einem Einzelreiz.

Er haengt an einer Konfiguration aus:

1. Rahmenform,
2. Blockdichte,
3. Irregularitaet,
4. Ruheverlust,
5. Nachhalltiefe,
6. Fokus- und Beobachtungsverhaeltnis.

Die Blockgroesse wirkt dabei wie ein zeitlicher Verdichtungsgrad der Weltform.

## Grenze

`1435` hat zusaetzlich eine leichte negative Drift. Dadurch ist noch offen, wie stark die klare `dio_0ein`-Dominanz aus Blockdichte allein kommt.

## Wie es weitergeht

Als naechstes sollte `1435` mit exakt neutralerer Drift wiederholt werden. Dann pruefen wir, ob kurze Blockdichte allein `dio_0ein` staerkt oder ob negative Drift die Wirkung mittraegt.
