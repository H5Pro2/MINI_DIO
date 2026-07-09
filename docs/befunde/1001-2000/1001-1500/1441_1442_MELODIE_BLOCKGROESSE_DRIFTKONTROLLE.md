# 1441/1442 - Melodie Blockgroesse Driftkontrolle

## Zweck

Diese Pruefung schliesst die Grenze aus `1438-1440`.

Grundfrage:

Bleibt die Blockgroessen-Lesung erhalten, wenn `block_size 10` und `block_size 14` driftkorrigiert werden?

## Aufbau

Die Formfolge bleibt unveraendert:

`block -> wave_up -> regular -> wave_down -> regular -> block`

Verglichen werden:

- `1438`: block_size 10, urspruengliche Drift
- `1441`: block_size 10, driftkorrigiert
- `1440`: block_size 14, urspruengliche Drift
- `1442`: block_size 14, driftkorrigiert

## Rohwelt

| Welt | Blockgroesse | Richtungswechsel | Drift | Max DD | Quiet Score |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1438 | 10 | 463 | -0.018699 | 0.084180 | 0.382152 |
| 1441 | 10 | 463 | -0.000016 | 0.074686 | 0.381758 |
| 1440 | 14 | 454 | -0.009630 | 0.083787 | 0.394162 |
| 1442 | 14 | 456 | -0.000057 | 0.079460 | 0.391091 |

## Ergebnis

| Welt | Blockgroesse | Symbole | stabil | tragend_unruhig | dominant | zweites Symbol | Carry | Rekopplung | Strain | Kopplung | Nachhall |
| --- | ---: | ---: | ---: | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1438_BS10_ORIGINAL | 10 | 53 | 1127 | 67 | `dio_0eindxe:178` | `dio_1fllaqz:171` | 0.574855 | 0.731283 | 0.129639 | 0.875252 | 0.562161 |
| 1441_BS10_DRIFTCTRL | 10 | 53 | 1135 | 59 | `dio_0eindxe:179` | `dio_1fllaqz:174` | 0.574543 | 0.731305 | 0.129184 | 0.875611 | 0.553188 |
| 1440_BS14_ORIGINAL | 14 | 53 | 1139 | 55 | `dio_0eindxe:173` | `dio_1fllaqz:173` | 0.576394 | 0.732420 | 0.128969 | 0.877734 | 0.574251 |
| 1442_BS14_DRIFTCTRL | 14 | 52 | 1141 | 53 | `dio_1fllaqz:176` | `dio_0eindxe:173` | 0.576781 | 0.732613 | 0.128915 | 0.877878 | 0.576467 |

## Befund

Die Driftkontrolle bestaetigt die Blockgroessen-Lesung.

`block_size 10` bleibt trotz Driftkorrektur `dio_0ein`-nah:

- original: `dio_0ein:178` vor `dio_1fll:171`
- driftkorrigiert: `dio_0ein:179` vor `dio_1fll:174`

`block_size 14` kippt bei driftkorrigierter Welt klarer zu `dio_1fll`:

- original: Gleichstand `173 / 173`
- driftkorrigiert: `dio_1fll:176` vor `dio_0ein:173`

Gleichzeitig steigen Stabilitaet und Rekopplung leicht, waehrend `tragend_unruhig` faellt.

## Lesung

Die Dominanzverschiebung kommt nicht primaer aus negativer Drift.

Sie folgt der zeitlichen Blockdichte:

- `block_size 10` bleibt noch im `dio_0ein`-nahen Uebergangsbereich.
- `block_size 14` liegt bereits nahe an der Rueckkehr von `dio_1fll`.
- `block_size 16` hatte diese Rueckkehr schon gezeigt.

Damit wird der Uebergangsbereich enger:

`block_size 10` bis `14` ist nicht mehr nur ein breiter Verdacht, sondern ein realer Schwellenraum.

## Schlussfolgerung

Mini-DIO bildet bei geordneter Melodie nicht nur eine Feldklasse, sondern eine feinere zeitliche Bedeutungsordnung.

Die Blockgroesse wirkt als Feldzeit-Parameter:

- kurze Blockdichte: mehr aktive Verdichtung, `dio_0ein`-naeher,
- laengere Blockdichte: mehr Nachhall, bessere Rekopplung, `dio_1fll`-naeher.

## Grenze

Die exakte Schwelle ist noch nicht punktgenau bestimmt.

`block_size 12` war fast gleich, `block_size 14` driftkorrigiert kippt zu `dio_1fll`.
