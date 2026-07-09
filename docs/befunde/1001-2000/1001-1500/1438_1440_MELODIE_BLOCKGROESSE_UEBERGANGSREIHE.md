# 1438-1440 - Melodie Blockgroesse Uebergangsreihe

## Zweck

Diese Pruefung fuehrt die offene Frage aus `1437` weiter.

Grundfrage:

Wo liegt der Uebergangsbereich zwischen `dio_0ein`-Dominanz bei kurzer Blockdichte und der Rueckkehr von `dio_1fll` bei laengerer Blockdichte?

## Aufbau

Alle Welten nutzen dieselbe Formfolge:

`block -> wave_up -> regular -> wave_down -> regular -> block`

Variiert wurde nur die Blockgroesse:

- `1438`: block_size 10
- `1439`: block_size 12
- `1440`: block_size 14

Als Bezugswerte bleiben:

- `1437`: block_size 4, neutralisierte Drift
- `1434`: block_size 8, neutralisierte Drift
- `1436`: block_size 16, neutralisierte Drift

## Rohwelt

| Welt | Blockgroesse | Richtungswechsel | Drift | Quiet Score |
| --- | ---: | ---: | ---: | ---: |
| 1437 | 4 | 523 | -0.000172 | 0.302085 |
| 1434 | 8 | 474 | -0.000464 | 0.367473 |
| 1438 | 10 | 463 | -0.018699 | 0.382152 |
| 1439 | 12 | 458 | -0.000477 | 0.388824 |
| 1440 | 14 | 454 | -0.009630 | 0.394162 |
| 1436 | 16 | 450 | -0.000476 | 0.399500 |

## Gesamtvergleich

| Welt | Blockgroesse | Symbole | stabil | tragend_unruhig | dominant | zweites Symbol | Carry | Rekopplung | Strain | Kopplung | Nachhall | Fokus | Beobachtung |
| --- | ---: | ---: | ---: | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1437_BS4_NEUTRAL | 4 | 54 | 1078 | 116 | `dio_0eindxe:210` | `dio_1fllaqz:168` | 0.566291 | 0.726725 | 0.130621 | 0.864813 | 0.452784 | 958 | 236 |
| 1434_BS8_NEUTRAL | 8 | 52 | 1115 | 79 | `dio_0eindxe:183` | `dio_1fllaqz:171` | 0.573485 | 0.730320 | 0.130022 | 0.872960 | 0.545979 | 1020 | 174 |
| 1438_BS10 | 10 | 53 | 1127 | 67 | `dio_0eindxe:178` | `dio_1fllaqz:171` | 0.574855 | 0.731283 | 0.129639 | 0.875252 | 0.562161 | 1017 | 177 |
| 1439_BS12 | 12 | 53 | 1134 | 60 | `dio_0eindxe:175` | `dio_1fllaqz:173` | 0.575695 | 0.731895 | 0.129292 | 0.876625 | 0.569098 | 1005 | 189 |
| 1440_BS14 | 14 | 53 | 1139 | 55 | `dio_0eindxe:173` | `dio_1fllaqz:173` | 0.576394 | 0.732420 | 0.128969 | 0.877734 | 0.574251 | 999 | 195 |
| 1436_BS16_NEUTRAL | 16 | 49 | 1142 | 52 | `dio_1fllaqz:173` | `dio_0eindxe:171` | 0.577496 | 0.732936 | 0.128885 | 0.878344 | 0.584819 | 978 | 216 |

## Befund

Die Uebergangsreihe bestaetigt einen stufenweisen Wechsel.

Mit wachsender Blockgroesse:

- steigt `stabil` von 1078 auf 1142,
- faellt `tragend_unruhig` von 116 auf 52,
- steigt der Nachhall von 0.452784 auf 0.584819,
- verbessert sich Rekopplung schrittweise,
- verliert `dio_0ein` seine klare Dominanz.

Der konkrete Symbolwechsel ist sehr eng:

- `block_size 8`: `dio_0ein` liegt noch knapp vor `dio_1fll`.
- `block_size 10`: `dio_0ein` bleibt vorne, aber nur noch leicht.
- `block_size 12`: `dio_0ein` und `dio_1fll` liegen fast gleich.
- `block_size 14`: Gleichstand.
- `block_size 16`: `dio_1fll` uebernimmt wieder knapp.

## Lesung

Die Blockgroesse wirkt nicht als harte Umschaltung, sondern als Verdichtungsgrad im Zeitfeld.

Kurze Blockdichte erzeugt eine aktivere, spannungsreichere Feldlesung. Lange Blockdichte erzeugt mehr Nachhall, mehr Stabilitaet und eine ruhigere Rekopplung.

Damit liest Mini-DIO keine Einzelkerze und keinen Einzelreiz. Die Bedeutung entsteht aus geordneter zeitlicher Form.

## Schlussfolgerung

Der Uebergang zwischen `dio_0ein` und `dio_1fll` liegt im Bereich `block_size 12-16`.

`block_size 12` wirkt wie ein Naehepunkt: Beide Bedeutungsfamilien liegen fast gleich stark im Feld.

`block_size 14` wirkt wie eine Gleichgewichtszone: Beide Familien sind gleich stark sichtbar.

`block_size 16` laesst `dio_1fll` wieder als tragendere Langblock-Familie auftreten.

## Grenze

`1438` und `1440` sind nicht perfekt driftneutral:

- `1438`: Drift -0.018699
- `1440`: Drift -0.009630

Das aendert den Hauptbefund nicht, weil `1439` mit nahezu neutraler Drift bereits den engen Uebergang zeigt. Fuer eine haertere Aussage sollten `block_size 10` und `14` trotzdem noch einmal driftkorrigiert wiederholt werden.
