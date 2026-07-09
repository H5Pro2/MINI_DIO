# 1434 - Melodie Blockrahmung Drift Isolation

## Zweck

Diese Pruefung trennt Blockrahmung von gerichteter Weltbewegung.

Grundfrage:

Bleibt die `dio_0ein`-Verschiebung aus `1433` bestehen, wenn die Netto-Drift neutralisiert wird?

## Aufbau

`1433`:

`block -> wave_up -> regular -> wave_down -> regular -> block`

mit positiver Netto-Drift.

`1434`:

`block -> wave_up -> regular -> wave_down -> regular -> block`

mit neutralisierter Drift.

Die Formfolge bleibt gleich. Nur die gerichtete Gesamtdrift wird reduziert.

## Rohwelt

| Welt | Richtungswechsel | avg_abs_return | avg_range | Drift | Max DD | Quiet Score |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1433 | 474 | 0.000901 | 0.004358 | 0.026252 | 0.070415 | 0.367473 |
| 1434 | 474 | 0.000901 | 0.004357 | -0.000464 | 0.083680 | 0.367473 |

## Befund

Die `dio_0ein`-Verschiebung bleibt auch bei neutralisierter Drift erhalten.

`1434` reproduziert in beiden Laeufen dieselbe Symbolordnung:

- `dio_0eindxe:183`
- `dio_1fllaqz:171`
- `dio_0v65ujo:148`

Damit ist `dio_0ein` nicht nur Folge positiver Drift.

## Vergleich

| Welt | Symbole | stabil | tragend_unruhig | dominant | zweites Symbol | Carry | Rekopplung | Strain | Kopplung | Nachhall | Fokus | Beobachtung |
| --- | ---: | ---: | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1433_BLOCK_FRAME_POSITIVE_DRIFT | 52 | 1126 | 68 | `dio_0eindxe` | `dio_1fllaqz` | 0.573210 | 0.730389 | 0.129541 | 0.873480 | 0.539929 | 1022 | 172 |
| 1434_BLOCK_FRAME_NEUTRAL_DRIFT | 52 | 1115 | 79 | `dio_0eindxe` | `dio_1fllaqz` | 0.573485 | 0.730320 | 0.130022 | 0.872960 | 0.545979 | 1020 | 174 |
| 1428_STRONGLY_BROKEN | 47 | 1102 | 92 | `dio_0eindxe` | `dio_0v65ujo` | 0.572284 | 0.729330 | 0.130062 | 0.867700 | 0.518075 | 1079 | 115 |

## Lesung

Blockrahmung ist ein echter Strukturreiz fuer das Feld.

Sie verschiebt die Bedeutungsnaehe bereits ohne doppelte Irregularitaet und ohne positive Drift in Richtung `dio_0ein`.

Der volle Kipppunkt aus `1428` entsteht aber erst, wenn weitere Faktoren hinzukommen:

1. Blockrahmung,
2. doppelte Irregularitaet,
3. Ruheverlust,
4. niedrigerer Nachhall,
5. staerkere Fokusdominanz bei schwacher Beobachtung.

## Schlussfolgerung

Die Blockrahmung wirkt wie ein Rahmenanker.

Sie veraendert nicht nur die Menge unruhiger Episoden, sondern offenbar die topologische Zuordnung der Bedeutung selbst.

Das ist relevant fuer die MCM-Lesung:

Eine Weltform kann die dominante Bedeutungsinsel verschieben, ohne dass sie allein einen vollen Kollaps oder kompletten Kipppunkt erzeugt.

## Grenze

`1434` zeigt eine stabile Tendenz, aber noch keine harte Grenzbestimmung. Es bleibt offen, ob verschiedene Blockgroessen oder Blockpositionen dieselbe Verschiebung erzeugen.

## Wie es weitergeht

Als naechstes sollte die Blockgroesse variiert werden. So pruefen wir, ob `dio_0ein` auf Blockrahmung allgemein reagiert oder nur auf die konkrete block_size-Struktur dieser Welt.
