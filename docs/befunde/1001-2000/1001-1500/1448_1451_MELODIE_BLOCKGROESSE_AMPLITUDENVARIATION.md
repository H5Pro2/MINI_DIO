# 1448-1451 - Melodie Blockgroesse Amplitudenvariation

## Zweck

Diese Pruefung kontrolliert die Schwellennaehe `12/13` gegen Weltlautstaerke.

Grundfrage:

Bleibt der Umschlag zwischen `dio_0ein` und `dio_1fll` bestehen, wenn die gleiche Weltform leiser oder lauter wird?

## Aufbau

Die Phasenfolge bleibt:

`block -> wave_up -> regular -> wave_down -> regular -> block`

Geprueft werden:

- leise Amplitude: `0.00080`
- laute Amplitude: `0.00150`
- jeweils `block_size 12` und `block_size 13`

Alle Welten wurden driftneutral gebaut.

## Rohwelt

| Welt | Blockgroesse | Amplitude | Richtungswechsel | Drift | Quiet Score |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1448 | 12 | 0.00080 | 458 | 0.0000000001 | 0.296614 |
| 1449 | 13 | 0.00080 | 455 | 0.0000000000 | 0.296440 |
| 1450 | 12 | 0.00150 | 458 | 0.0000000001 | 0.459329 |
| 1451 | 13 | 0.00150 | 455 | 0.0000000001 | 0.459004 |

## Ergebnis

| Welt | Blockgroesse | Amplitude | Symbole | stabil | tragend_unruhig | dominant | zweites Symbol | Carry | Rekopplung | Strain | Kopplung | Nachhall |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1448_BS12_QUIET | 12 | 0.00080 | 41 | 1156 | 38 | `dio_1fllaqz:181` | `dio_0eindxe:176` | 0.580839 | 0.735770 | 0.126568 | 0.881924 | 0.589791 |
| 1449_BS13_QUIET | 13 | 0.00080 | 43 | 1160 | 34 | `dio_1fllaqz:181` | `dio_0eindxe:177` | 0.581014 | 0.736003 | 0.126536 | 0.882539 | 0.593631 |
| 1450_BS12_LOUD | 12 | 0.00150 | 64 | 1109 | 85 | `dio_1fllaqz:168` | `dio_0eindxe:154` / `dio_0v65ujo:154` | 0.571396 | 0.728932 | 0.131286 | 0.872804 | 0.546321 |
| 1451_BS13_LOUD | 13 | 0.00150 | 66 | 1112 | 82 | `dio_1fllaqz:167` | `dio_0eindxe:155` | 0.571696 | 0.729203 | 0.131128 | 0.873486 | 0.548478 |

## Befund

Die Amplitude verschiebt den Schwellenraum deutlich.

Bei der leisen Welt:

- `dio_1fll` dominiert bereits bei `block_size 12`.
- Symbolstreuung sinkt deutlich.
- Stabilitaet, Carry, Rekopplung, Kopplung und Nachhall steigen.
- `tragend_unruhig` sinkt stark.
- `observation_tone` steigt, `focus_tone` sinkt.

Bei der lauten Welt:

- `dio_1fll` bleibt dominant.
- Symbolstreuung steigt deutlich.
- Rekopplung und Kopplung sinken.
- Strain und `tragend_unruhig` steigen.
- `focus_tone` steigt, `observation_tone` sinkt.

## Vergleich zur Normalamplitude

Normalamplitude `0.00115` zeigte:

- `block_size 12`: fast Gleichgewicht, meist noch knapp `dio_0ein`.
- `block_size 13`: knapp `dio_1fll`.

Die Amplitudenvariation zeigt:

- leiser: Schwelle verschiebt sich nach unten, `dio_1fll` schon bei 12.
- lauter: `dio_1fll` bleibt, aber das Feld wird fragmentierter und angespannter.

## Lesung

Die Blockgroesse ist nicht allein fuehrend.

Mini-DIO liest offenbar eine Kopplung aus:

- zeitlicher Blockdauer,
- Amplitude/Weltlautstaerke,
- Nachhall,
- Rekopplungsqualitaet,
- Symbolstreuung.

Leisere Weltspannung macht die Bedeutung glatter und stabiler. Lautere Weltspannung erzeugt mehr Randstreuung, ohne die `dio_1fll`-Dominanz zu brechen.

## Schlussfolgerung

Der vorherige Schwellenbefund bleibt relevant, muss aber als zweidimensionaler Schwellenraum gelesen werden:

`Blockdauer x Weltlautstaerke`

`block_size 12/13` ist kein isolierter Punkt, sondern ein Feldzeit-Lautstaerke-Uebergang.

## Grenze

Die Amplitudenwerte sind Pruefwerte, keine festen Regeln.

Der Befund sagt nicht: `dio_1fll` gehoert immer zu leiser Welt. Er sagt: In dieser Melodiekonstruktion verschiebt geringere Amplitude die Bedeutungsnaehe frueher zu `dio_1fll`.
