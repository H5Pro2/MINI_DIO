# 1473-1476 - Melodie-Gleichlage untere Kante

## Zweck

Diese Pruefung sucht die untere Kante des Gleichlagenplateaus.

Die konkrete Frage war:

Bis wohin bleibt `dio_0ein` unterhalb der Gleichlage dominant, und ab wann beginnt die Balance mit `dio_1fll`?

## Aufbau

Geprueft wurden vier nahe Amplituden:

- `0.00108`
- `0.00109`
- `0.00110`
- `0.00111`

Alle Welten nutzen:

- `block_size 13`
- gleiche Melodiephasen,
- gleiche Richtungswechselzahl `455`,
- `world_relative`,
- frischen Speicher.

## Ergebnis

| Welt | Amp | `dio_0ein` | `dio_1fll` | Differenz | Dominanz | Symbole | stabil | unruhig | Rekopplung | Nachhall |
|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|
| 1473 | 0.00108 | 175 | 174 | 1 | `dio_0ein` | 49 | 1142 | 52 | 0.732864 | 0.572406 |
| 1474 | 0.00109 | 175 | 174 | 1 | `dio_0ein` | 50 | 1142 | 52 | 0.732743 | 0.572144 |
| 1475 | 0.00110 | 175 | 173 | 2 | `dio_0ein` | 51 | 1140 | 54 | 0.732630 | 0.571927 |
| 1476 | 0.00111 | 174 | 173 | 1 | `dio_0ein` | 51 | 1140 | 54 | 0.732548 | 0.571462 |

## Befund

Unterhalb `0.00112` bleibt `dio_0ein` knapp dominant.

Die Dominanz ist jedoch sehr schwach:

- Abstand `1` bei `0.00108`,
- Abstand `1` bei `0.00109`,
- Abstand `2` bei `0.00110`,
- Abstand `1` bei `0.00111`.

Bei `0.00112` beginnt die zuvor reproduzierte Gleichlage.

## Lesung

Die untere Kante wirkt nicht hart.

MINI_DIO naehrt sich der Gleichlage schrittweise:

`dio_0ein` bleibt zwar vorne, aber nur mit minimalem Abstand.

Das Feld ist in diesem Bereich bereits in direkter Bedeutungsnaehe zu `dio_1fll`.

## Schlussfolgerung

Das Balancefenster beginnt in dieser Pruefreihe bei etwa:

`0.00112`

Vorher liegt eine sehr schmale `dio_0ein`-nahe Randzone.

Zusammen mit `1470-1472` ergibt sich:

- untere Kante: `0.00112`
- Gleichlagenplateau: `0.00112` bis `0.00114`
- obere Kante: ab `0.00115` kippt es zu `dio_1fll`

## Grenze

Die Werte sind Pruefwerte, keine festen Regeln.

Der Befund gilt fuer diese synthetische Melodiefamilie und `block_size 13`.
