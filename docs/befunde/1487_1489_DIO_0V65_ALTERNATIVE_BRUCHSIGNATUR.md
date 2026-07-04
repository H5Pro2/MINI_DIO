# 1487-1489 - `dio_0v65` alternative Bruchsignatur

## Zweck

Diese Pruefung testet, ob `dio_0v65` allgemein an Bruch gekoppelt ist.

Die konkrete Unterfrage war:

Bleibt `dio_0v65` auch bei einer anderen Irregularitaetsform Hauptanker?

## Aufbau

Statt der vorherigen `irregular`-Bruchform wurde eine andere Bruchsignatur gebaut:

`block -> pulse_break -> regular -> wave_down -> stutter_break -> block`

Gepruefte Amplituden:

- `0.00120`
- `0.00135`
- `0.00150`

Konstant:

- `block_size 13`,
- `world_relative`,
- frischer Speicher,
- driftkontrollierte Konstruktion.

## Ergebnis

| Welt | Amp | Hauptanker | `dio_0v65` | `dio_0ein` | `dio_1fll` | `dio_0jt7` | Symbole | stabil | unruhig | Rekopplung | Nachhall |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1487 | 0.00120 | `dio_1fll` 170 | 104 | 161 | 170 | 112 | 56 | 1141 | 53 | 0.732514 | 0.540666 |
| 1488 | 0.00135 | `dio_1fll` 174 | 109 | 155 | 174 | 108 | 65 | 1129 | 65 | 0.731083 | 0.533827 |
| 1489 | 0.00150 | `dio_1fll` 174 | 109 | 147 | 174 | 106 | 73 | 1125 | 69 | 0.729769 | 0.521901 |

## Befund

`dio_0v65` ist nicht allgemein der Bruchanker fuer jede Irregularitaetsform.

Bei dieser alternativen Pulse/Stutter-Bruchsignatur bleibt `dio_1fll` klar Hauptanker.

`dio_0v65` bleibt sichtbar, aber nicht zentral.

## Vergleich Zur Vorherigen Bruchform

Vorherige Bruchform:

`block -> irregular -> regular -> wave_down -> irregular -> block`

Dort wurde `dio_0v65` ab mittlerer Lautstaerke Hauptanker.

Neue Bruchform:

`block -> pulse_break -> regular -> wave_down -> stutter_break -> block`

Hier bleibt `dio_1fll` Hauptanker, trotz steigender Feldlast.

## Lesung

Der Befund differenziert die Rolle von `dio_0v65`.

`dio_0v65` steht nicht fuer Bruch allgemein.

Es scheint an eine bestimmte Art gebrochener Feldnaehe gekoppelt zu sein:

- eher richtungsumkehrende, mittig gebrochene Irregularitaet,
- nicht einfach jede Pulse/Stutter-Stoerung.

Die alternative Bruchsignatur wird von MINI_DIO naeher an `dio_1fll` gelesen.

## Schlussfolgerung

Die MCM-Syntax arbeitet differenzierter als eine grobe Klasse `Bruch`.

MINI_DIO trennt offenbar Bruchqualitaeten:

- bestimmte Irregularitaet -> `dio_0v65`
- Pulse/Stutter-Bruch -> `dio_1fll`

Das stuetzt die Lesung, dass Bedeutungsrollen nicht nur aus Lautstaerke entstehen, sondern aus der konkreten Feldform.

## Grenze

Diese Pruefung zeigt eine klare Differenzierung, aber noch keine vollstaendige Bruchtypologie.

Weitere Bruchformen sind noetig, bevor `dio_0v65` sauber benannt werden kann.

## Wie es weitergeht

Als naechstes sollte eine Bruchtypologie aufgebaut werden: mehrere Bruchformen nebeneinander, mit Hauptanker, Nachhall, Rekopplung und Unruhe. Ziel ist zu klaeren, welche Feldform welche Bedeutung aktiviert.
