# 1484-1486 - `dio_0v65` Bruchanker Lautstaerkereihe

## Zweck

Diese Pruefung isoliert `dio_0v65` als moeglichen Bruchanker.

Die konkrete Unterfrage war:

Bleibt `dio_0v65` bei gleicher Bruchstruktur ueber mehrere Lautstaerken hinweg Hauptanker?

## Aufbau

Verwendet wurde dieselbe Bruchstruktur wie in `1481-1483`:

`block -> irregular -> regular -> wave_down -> irregular -> block`

Gepruefte Amplituden:

- `0.00095`
- `0.00120`
- `0.00135`

Konstant:

- `block_size 13`,
- `world_relative`,
- frischer Speicher,
- driftkontrollierte Konstruktion.

## Ergebnis

| Welt | Amp | Hauptanker | `dio_0v65` | `dio_0ein` | `dio_1fll` | Symbole | stabil | unruhig | Rekopplung | Nachhall |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1484 | 0.00095 | `dio_1fll` 132 | 127 | 126 | 132 | 52 | 1121 | 73 | 0.732478 | 0.539627 |
| 1485 | 0.00120 | `dio_0v65` 146 | 146 | 140 | 134 | 58 | 1113 | 81 | 0.729790 | 0.517597 |
| 1486 | 0.00135 | `dio_0v65` 147 | 147 | 142 | 133 | 61 | 1107 | 87 | 0.728812 | 0.509364 |

## Befund

`dio_0v65` ist nicht bei jeder Bruchwelt automatisch Hauptanker.

Bei niedriger Bruchlautstaerke `0.00095` bleibt `dio_1fll` knapp vorne.

Ab `0.00120` uebernimmt `dio_0v65` klar die Hauptrolle.

Bei `0.00135` bleibt `dio_0v65` Hauptanker und die Feldlast steigt weiter:

- mehr Symbole,
- weniger stabile Wirkung,
- mehr tragende Unruhe,
- sinkender Nachhall,
- steigender Fokus-Ton.

## Lesung

`dio_0v65` wirkt wie ein Bruchanker, aber erst wenn die Bruchstruktur genug Lautstaerke/Feldwirkung erreicht.

Fachlich:

`dio_0v65` steht nicht einfach fuer Bruch allein.

Es scheint fuer eine Kombination aus:

- gebrochener Struktur,
- ausreichender Weltlautstaerke,
- hoeherem Fokus-Ton,
- sinkendem Nachhall,
- steigender tragender Unruhe

zu stehen.

## Schlussfolgerung

Die Rolle `dio_0v65 = gebrochene Feldnaehe` ist plausibel, aber bedingt.

Praeziser:

`dio_0v65` ist ein Hauptanker fuer lautere gebrochene Feldnaehe.

Bei leiser Bruchwelt bleibt die alte `dio_1fll`-Naehe noch tragend.

## Grenze

Diese Pruefung nutzt nur eine Bruchform.

Offen bleibt, ob `dio_0v65` auch bei anderer Irregularitaetsform oder anderer Bruchlage Hauptanker bleibt.

## Wie es weitergeht

Als naechstes sollte eine andere Irregularitaetsform getestet werden. Ziel ist zu pruefen, ob `dio_0v65` an Bruch allgemein gekoppelt ist oder nur an diese konkrete Bruchsignatur.
