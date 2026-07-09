# 1493-1497 - Stabilitaet von `dio_1wdik71` im Randbruchraum

## Fragestellung

Im Befund 1491-1492 trat `dio_1wdik71` beim Randbruch als dominante Familie auf. Die offene Frage war:

Ist `dio_1wdik71` ein stabiler Randbruch-/Uebergangsanker oder nur ein spezifischer Anker der konkreten 1492-Welt?

## Pruefaufbau

Es wurden zwei Pruefebenen getrennt:

1. Enge Stoerung derselben 1492-Welt
   - `1496`: gleiche Preisstruktur, nur Volumen leicht veraendert
   - `1497`: minimale Preis-/Wick-Stoerung

2. Anders konstruierte Randbruchwelten
   - `1493`: Bruch am Anfang
   - `1494`: Bruch am Ende
   - `1495`: beidseitiger Randbruch mit leichter Intensitaetsverschiebung

Alle Laeufe waren passiv, mit frischem Memory und `world_relative`-Sinnesaufnahme.

## Ergebnis

| Welt | Pruefung | Top-Symbol | Top-Count | `dio_1wdik71` | Nachhall | Fokus | Beobachtung |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1492 | Referenz | `dio_1wdik71` | 220 | 220 | 0.551470 | 734 | 460 |
| 1496 | Volumenstoerung | `dio_1wdik71` | 217 | 217 | 0.550461 | 748 | 446 |
| 1497 | minimale Preisstoerung | `dio_1wdik71` | 220 | 220 | 0.551289 | 742 | 452 |
| 1493 | Start-Randbruch | `dio_0l7pvdk` | 179 | 0 | 0.355713 | 1069 | 125 |
| 1494 | End-Randbruch | `dio_0l7pvdk` | 180 | 0 | 0.350116 | 1085 | 109 |
| 1495 | beidseitig verschoben | `dio_14wjmk5` | 144 | 0 | 0.385335 | 1064 | 130 |

## Deutung

`dio_1wdik71` ist kein allgemeines Wort fuer Randbruch.

Es ist aber innerhalb desselben Randbruch-Phaenotyps sehr stabil:

- Volumenstoerung erhaelt den Anker fast unveraendert.
- Minimale Preis-/Wick-Stoerung erhaelt den Anker voll.
- Nachhall und Fokus-/Beobachtungsverhaeltnis bleiben sehr nah an der Referenz.

Bei anders konstruierten Randbruechen verschwindet `dio_1wdik71` vollstaendig. Dort entstehen neue Familien (`dio_0l7pvdk`, `dio_14wjmk5`) mit deutlich weniger Nachhall und viel staerkerem Fokus.

## Schlussfolgerung

MINI_DIO bildet hier keine starre Symboltabelle wie:

`Randbruch = dio_1wdik71`

Stattdessen wirkt die Familie wie ein phänotypischer Anker:

`dio_1wdik71` steht fuer eine bestimmte Randbruch-Gestalt mit hoher Nachhall-/Beobachtungsnaehe.

Das ist fachlich wichtiger als ein allgemeiner Name. Es zeigt, dass die eigene Syntax an konkrete Feldqualitaet gebunden bleibt und nicht einfach Kategorieetiketten ausgibt.
