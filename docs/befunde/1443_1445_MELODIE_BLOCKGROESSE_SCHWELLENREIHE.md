# 1443-1445 - Melodie Blockgroesse Schwellenreihe

## Zweck

Diese Pruefung verengt den Schwellenraum aus `1441/1442`.

Grundfrage:

Wo kippt die dominante Innenfeldbedeutung bei driftneutraler Melodie von `dio_0ein` zu `dio_1fll`?

## Aufbau

Die Weltfolge bleibt gleich:

`block -> wave_up -> regular -> wave_down -> regular -> block`

Verglichen werden driftkontrollierte Welten mit:

- `block_size 11`
- `block_size 12`
- `block_size 13`

Die Drift wurde praktisch neutral gesetzt. Damit soll die Lesung nicht durch gerichteten Preisdrift, sondern durch zeitliche Blockdichte entstehen.

## Rohwelt

| Welt | Blockgroesse | Richtungswechsel | Drift | Quiet Score |
| --- | ---: | ---: | ---: | ---: |
| 1443 | 11 | 464 | 0.0000000001 | 0.380424 |
| 1444 | 12 | 458 | 0.0000000000 | 0.388424 |
| 1445 | 13 | 455 | 0.0000000000 | 0.392424 |

## Ergebnis

| Welt | Blockgroesse | Symbole | stabil | tragend_unruhig | dominant | zweites Symbol | Carry | Rekopplung | Strain | Kopplung | Nachhall |
| --- | ---: | ---: | ---: | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1443_BS11_DRIFTCTRL | 11 | 52 | 1137 | 57 | `dio_0eindxe:178` | `dio_1fllaqz:176` | 0.575357 | 0.731755 | 0.129185 | 0.876276 | 0.562592 |
| 1444_BS12_DRIFTCTRL | 12 | 53 | 1133 | 61 | `dio_0eindxe:175` | `dio_1fllaqz:174` | 0.575627 | 0.731866 | 0.129285 | 0.876614 | 0.568198 |
| 1445_BS13_DRIFTCTRL | 13 | 52 | 1137 | 57 | `dio_1fllaqz:173` | `dio_0eindxe:172` | 0.575961 | 0.732131 | 0.129039 | 0.877238 | 0.569523 |

## Top-Symbole

| Welt | Top 8 |
| --- | --- |
| 1443_BS11_DRIFTCTRL | `dio_0eindxe:178`, `dio_1fllaqz:176`, `dio_0v65ujo:148`, `dio_13s036n:114`, `dio_0jt7iub:95`, `dio_13o0i6x:45`, `dio_0n0i1kn:38`, `dio_15vu68q:38` |
| 1444_BS12_DRIFTCTRL | `dio_0eindxe:175`, `dio_1fllaqz:174`, `dio_0v65ujo:145`, `dio_13s036n:118`, `dio_0jt7iub:91`, `dio_15vu68q:47`, `dio_13o0i6x:44`, `dio_0n0i1kn:39` |
| 1445_BS13_DRIFTCTRL | `dio_1fllaqz:173`, `dio_0eindxe:172`, `dio_0v65ujo:142`, `dio_13s036n:120`, `dio_0jt7iub:96`, `dio_15vu68q:53`, `dio_13o0i6x:43`, `dio_0n0i1kn:40` |

## Befund

Die enge Reihe bestaetigt einen sehr schmalen Umschlagsraum.

- `block_size 11`: `dio_0ein` bleibt knapp vor `dio_1fll`.
- `block_size 12`: fast Gleichgewicht, `dio_0ein` nur noch minimal vorn.
- `block_size 13`: Dominanz kippt zu `dio_1fll`.

Die Differenzen sind klein, aber systematisch:

- Rekopplung steigt von `0.731755` auf `0.732131`.
- Kopplung steigt von `0.876276` auf `0.877238`.
- Nachhall steigt von `0.562592` auf `0.569523`.
- `focus_tone` nimmt ab, `observation_tone` nimmt zu.

## Lesung

Die Blockgroesse wirkt hier wie ein Feldzeit-Parameter.

Bei kleinerer Blockgroesse bleibt die Welt mehr im `dio_0ein`-nahen Verdichtungsraum. Mit wachsender Blockgroesse nimmt Nachhall zu und die Welt wird `dio_1fll`-naeher.

Der Umschlag ist nicht hart im Sinne eines Schalters. Er ist ein sehr enger Bedeutungsuebergang:

`block_size 11 -> 12 -> 13`

Mini-DIO bildet damit keine starre Klasse, sondern eine feine Uebergangsordnung zwischen zwei stabilen Bedeutungsraeumen.

## Schlussfolgerung

Der Schwellenpunkt liegt in dieser Konstruktion wahrscheinlich um `block_size 12/13`.

`block_size 12` ist nahezu Gleichgewicht. `block_size 13` reicht bereits aus, um die Fuehrungsrolle zu verschieben.

Das ist wichtig fuer die MCM-Lesung:

Nicht nur Weltform und Drift wirken, sondern auch die zeitliche Dichte gleicher Formphasen. Die Innenfeldordnung reagiert auf Blockdauer, Nachhall und Rekopplung.

## Grenze

Die Werte liegen eng beieinander. Deshalb darf diese Reihe nicht als absolute Schwelle gelesen werden.

Sie zeigt einen stabilen Hinweis auf einen Uebergangsraum, nicht eine feste Regel.

## Wie es weitergeht

Als naechstes sollte die Schwellennaehe `12/13` gegen eine zweite Phasenordnung geprueft werden. Wichtig ist, ob der Umschlag an der Blockgroesse selbst haengt oder an der konkreten Reihenfolge `block -> wave_up -> regular -> wave_down -> regular -> block`.
