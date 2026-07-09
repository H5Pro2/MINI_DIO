# 1429 - Melodie Kipppunkt Reproduktion

## Zweck

Diese Pruefung wiederholt `1428` mit frischem Memory.

Grundfrage:

Ist der Dominanzwechsel zu `dio_0eindxe` reproduzierbar, oder war er ein einzelner Laufzustand?

## Aufbau

Welt:

`block -> irregular -> regular -> wave_down -> irregular -> block`

Die Datei ist identisch zu `1428`:

`data/synthetic_1428_melody_strongly_broken_1200_5m.csv`

Memory und Debug wurden neu angelegt:

- `memory/1429_repro_melody_strongly_broken_memory.json`
- `debug/1429_repro_melody_strongly_broken/`

## Vergleich

| Lauf | Symbole | stabil | tragend_unruhig | dominant | Carry | Rekopplung | Strain | Kopplung | Nachhall | Fokus | Beobachtung |
| --- | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1428_ORIG | 47 | 1102 | 92 | `dio_0eindxe` | 0.572284 | 0.729330 | 0.130062 | 0.867700 | 0.518075 | 1079 | 115 |
| 1429_REPRO | 47 | 1102 | 92 | `dio_0eindxe` | 0.572284 | 0.729330 | 0.130062 | 0.867700 | 0.518075 | 1079 | 115 |

Top-Symbole:

| Lauf | Top-Symbole |
| --- | --- |
| 1428_ORIG | `dio_0eindxe:197`, `dio_0v65ujo:146`, `dio_13s036n:102`, `dio_0jt7iub:93`, `dio_1fllaqz:84` |
| 1429_REPRO | `dio_0eindxe:197`, `dio_0v65ujo:146`, `dio_13s036n:102`, `dio_0jt7iub:93`, `dio_1fllaqz:84` |

## Befund

Die Reproduktion ist in den Kernwerten identisch.

Damit ist der in `1428` beobachtete Wechsel von `dio_1fllaqz` zu `dio_0eindxe` kein zufaelliger Einzelzustand des Speichers. Unter gleicher Welt und frischem Memory bildet Mini-DIO dieselbe dominante Bedeutungsordnung.

## Schlussfolgerung

Der Melodie-Kipppunkt ist reproduzierbar.

Die stark gebrochene Folge erzeugt stabil eine andere fuehrende Bedeutungsfamilie als die geordnete und moderat veraenderte Melodiefolge.

Das ist fuer die MCM-Forschung relevant, weil hier nicht nur eine Feldspannung steigt. Die innere Symbolordnung selbst verschiebt sich reproduzierbar.

## Grenze

Die Reproduktion gilt fuer dieselbe synthetische Welt.

Sie beweist keine allgemeine Regel fuer alle Melodien oder alle Welten. Sie zeigt aber, dass Mini-DIO bei identischem Weltkontakt dieselbe Bedeutungsdominanz erneut ausbildet.
