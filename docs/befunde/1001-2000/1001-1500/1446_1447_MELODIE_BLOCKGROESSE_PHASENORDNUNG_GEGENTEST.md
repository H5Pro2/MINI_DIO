# 1446/1447 - Melodie Blockgroesse Phasenordnung Gegentest

## Zweck

Diese Pruefung kontrolliert den Befund aus `1443-1445`.

Grundfrage:

Haengt der Umschlag von `dio_0ein` zu `dio_1fll` an der Blockgroesse selbst oder an der konkreten Phasenfolge?

## Aufbau

Die vorherige Reihe nutzte:

`block -> wave_up -> regular -> wave_down -> regular -> block`

Der Gegentest spiegelt die Bewegungsphasen:

`block -> wave_down -> regular -> wave_up -> regular -> block`

Geprueft werden wieder die engen Schwellenpunkte:

- `block_size 12`
- `block_size 13`

Beide Welten wurden driftneutral gebaut.

## Rohwelt

| Welt | Blockgroesse | Richtungswechsel | Drift | Quiet Score |
| --- | ---: | ---: | ---: | ---: |
| 1446 | 12 | 456 | 0.0000000001 | 0.378335 |
| 1447 | 13 | 455 | 0.0000000000 | 0.378110 |

## Ergebnis

| Welt | Blockgroesse | Symbole | stabil | tragend_unruhig | dominant | zweites Symbol | Carry | Rekopplung | Strain | Kopplung | Nachhall |
| --- | ---: | ---: | ---: | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1446_BS12_MIRROR_DRIFTCTRL | 12 | 53 | 1133 | 61 | `dio_0eindxe:176` | `dio_1fllaqz:174` | 0.576107 | 0.732058 | 0.129207 | 0.876645 | 0.571860 |
| 1447_BS13_MIRROR_DRIFTCTRL | 13 | 49 | 1137 | 57 | `dio_1fllaqz:174` | `dio_0eindxe:173` | 0.576746 | 0.732471 | 0.128897 | 0.877371 | 0.575547 |

## Top-Symbole

| Welt | Top 8 |
| --- | --- |
| 1446_BS12_MIRROR_DRIFTCTRL | `dio_0eindxe:176`, `dio_1fllaqz:174`, `dio_0v65ujo:146`, `dio_13s036n:115`, `dio_0jt7iub:90`, `dio_15vu68q:48`, `dio_0n0i1kn:46`, `dio_13o0i6x:46` |
| 1447_BS13_MIRROR_DRIFTCTRL | `dio_1fllaqz:174`, `dio_0eindxe:173`, `dio_0v65ujo:143`, `dio_13s036n:119`, `dio_0jt7iub:96`, `dio_15vu68q:52`, `dio_0n0i1kn:48`, `dio_13o0i6x:43` |

## Befund

Der Umschlag bleibt auch bei gespiegelter Phasenfolge erhalten.

- `block_size 12`: `dio_0ein` bleibt knapp dominant.
- `block_size 13`: `dio_1fll` wird knapp dominant.

Damit wird die vorherige Lesung gestuetzt:

Der Effekt haengt nicht nur an der Reihenfolge `wave_up` vor `wave_down`.

## Vergleich zu 1443-1445

Die Richtung des Umschlags bleibt gleich:

| Blockgroesse | Originalfolge | Spiegelfolge |
| ---: | --- | --- |
| 12 | `dio_0ein:175` vor `dio_1fll:174` | `dio_0ein:176` vor `dio_1fll:174` |
| 13 | `dio_1fll:173` vor `dio_0ein:172` | `dio_1fll:174` vor `dio_0ein:173` |

Die Differenzen bleiben klein, aber sie reproduzieren sich.

## Lesung

Die Blockgroesse wirkt weiterhin wie ein Feldzeit-Parameter.

Die Phasenordnung veraendert Oberflaechenwerte, aber sie zerstoert den Schwellenraum nicht. Das spricht dafuer, dass Mini-DIO die zeitliche Dichte der Blockphase als Innenfeldnaehe liest.

Gleichzeitig bleibt die Grenze wichtig:

Der Abstand zwischen `dio_0ein` und `dio_1fll` ist nur knapp. Es geht hier nicht um eine harte Klassifikation, sondern um eine feine Verschiebung der Bedeutungsnaehe.

## Schlussfolgerung

Die Schwellennaehe `12/13` ist robuster als die konkrete Reihenfolge der Bewegungsphasen.

Der Befund spricht fuer:

- Feldzeitwirkung durch Blockdauer,
- Nachhallverschiebung,
- enge Bedeutungsnaehe zwischen `dio_0ein` und `dio_1fll`,
- keine reine Drift- oder Phasenfolgen-Artefaktbildung.
