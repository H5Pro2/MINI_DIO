# 1437 - Melodie Blockgroesse Driftkontrolle

## Zweck

Diese Pruefung kontrolliert den offenen Punkt aus `1435/1436`.

Grundfrage:

Kam die starke `dio_0ein`-Dominanz bei kurzer Blockgroesse aus der kurzen Blockdichte selbst oder aus der negativen Drift der Rohwelt?

## Aufbau

`1435`:

`block_size = 4`, negative Drift.

`1437`:

`block_size = 4`, nahezu neutrale Drift.

Die Formfolge bleibt gleich:

`block -> wave_up -> regular -> wave_down -> regular -> block`

## Rohwelt

| Welt | Blockgroesse | Richtungswechsel | Drift | Max DD | Quiet Score |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1435 | 4 | 523 | -0.018699 | 0.084180 | 0.302085 |
| 1437 | 4 | 523 | -0.000172 | 0.074257 | 0.302085 |

## Befund

Die starke `dio_0ein`-Dominanz bleibt bei neutralisierter Drift bestehen.

`1437`:

- `dio_0eindxe:210`
- `dio_1fllaqz:168`
- `dio_0v65ujo:163`

Damit ist die kurze Blockdichte selbst ein tragender Faktor.

## Vergleich

| Welt | Blockgroesse | stabil | tragend_unruhig | dominant | zweites Symbol | Carry | Rekopplung | Nachhall |
| --- | ---: | ---: | ---: | --- | --- | ---: | ---: | ---: |
| 1435_BS4_NEGATIVE_DRIFT | 4 | 1072 | 122 | `dio_0eindxe` | `dio_1fllaqz` | 0.566670 | 0.726805 | 0.456621 |
| 1437_BS4_NEUTRAL_DRIFT | 4 | 1078 | 116 | `dio_0eindxe` | `dio_1fllaqz` | 0.566291 | 0.726725 | 0.452784 |
| 1434_BS8_NEUTRAL_DRIFT | 8 | 1115 | 79 | `dio_0eindxe` | `dio_1fllaqz` | 0.573485 | 0.730320 | 0.545979 |
| 1436_BS16_NEUTRAL_DRIFT | 16 | 1142 | 52 | `dio_1fllaqz` | `dio_0eindxe` | 0.577496 | 0.732936 | 0.584819 |

## Lesung

Die Blockdichte wirkt wie zeitliche Verdichtung.

Bei kurzer Blockgroesse entsteht:

- weniger Nachhall,
- mehr `tragend_unruhig`,
- niedrigere Rekopplung,
- staerkere Bindung an `dio_0ein`.

Bei langer Blockgroesse entsteht:

- hoeherer Nachhall,
- weniger unruhige Tragwirkung,
- bessere Rekopplung,
- Rueckkehr von `dio_1fll`.

## Schlussfolgerung

Die Dominanzverschiebung ist nicht nur Driftwirkung.

Mini-DIO liest die zeitliche Dichte einer Weltform als Feldqualitaet. Kurze Blockwechsel wirken anders als lange Blockwechsel, obwohl die gleiche grobe Formfolge erhalten bleibt.

Das staerkt die bisherige Melodie-Hypothese:

Nicht nur Form, sondern geordnete Form in Zeit erzeugt Bedeutung.

## Grenze

Die genaue Schwelle zwischen `dio_0ein` und `dio_1fll` ist noch nicht bestimmt. Zwischen block_size 8 und 16 liegt wahrscheinlich ein Uebergangsbereich.
