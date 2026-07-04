# 1470-1472 - Melodie-Gleichlage obere Kante

## Zweck

Diese Pruefung sucht die obere Kante des Gleichlagenplateaus aus `1467-1469`.

Die konkrete Frage war:

Ab welcher kleinen Erhoehung oberhalb `0.00114` verlaesst `dio_1fll` die Gleichlage und wird wieder dominant?

## Aufbau

Geprueft wurden drei nahe Amplituden:

- `0.00115`
- `0.00116`
- `0.00117`

Alle Welten nutzen:

- `block_size 13`
- gleiche Melodiephasen,
- gleiche Richtungswechselzahl `455`,
- `world_relative`,
- frischen Speicher.

## Ergebnis

| Welt | Amp | `dio_0ein` | `dio_1fll` | Differenz | Dominanz | Symbole | stabil | unruhig | Rekopplung | Nachhall |
|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|
| 1470 | 0.00115 | 172 | 173 | -1 | `dio_1fll` | 52 | 1138 | 56 | 0.732185 | 0.570749 |
| 1471 | 0.00116 | 172 | 173 | -1 | `dio_1fll` | 52 | 1137 | 57 | 0.732065 | 0.569554 |
| 1472 | 0.00117 | 171 | 173 | -2 | `dio_1fll` | 52 | 1137 | 57 | 0.731945 | 0.567226 |

## Befund

Ab `0.00115` ist `dio_1fll` durchgehend dominant.

Die Dominanz bleibt zunaechst sehr knapp:

- `0.00115`: Abstand `1`
- `0.00116`: Abstand `1`
- `0.00117`: Abstand `2`

Gleichzeitig sinkt der Nachhall leicht und der Fokus-Ton steigt.

## Lesung

Das Plateau endet nicht abrupt mit grossem Abstand.

Stattdessen verlaesst `dio_1fll` die Gleichlage langsam:

`Gleichlage -> knappe Dominanz -> staerkere Dominanz`

Die Feldantwort bleibt nah, aber die Richtung der Bedeutungsnaehe ist ab `0.00115` stabil auf `dio_1fll` verschoben.

## Schlussfolgerung

Das Gleichlagenplateau liegt in dieser Pruefreihe etwa bei:

`0.00112` bis `0.00114`

Die obere Kante beginnt bei:

`0.00115`

Fachlich sauberer:

Die MCM-Antwort zeigt kein hartes Umschalten, sondern eine weiche Kantenbildung.

## Grenze

Die Werte sind Pruefwerte, keine Regeln.

Der Befund gilt fuer diese synthetische Melodiefamilie und `block_size 13`.

## Wie es weitergeht

Als naechstes sollte die untere Plateau-Kante genauer geprueft werden: `0.00108`, `0.00109`, `0.00110`, `0.00111`. Ziel ist zu sehen, wo `dio_0ein` die Gleichlage verlaesst und wie breit das Balancefenster wirklich ist.
