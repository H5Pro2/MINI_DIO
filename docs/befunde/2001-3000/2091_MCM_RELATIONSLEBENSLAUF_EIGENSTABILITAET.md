# 2091 - Eigenstabilität des MCM-Relationslebenslaufs

## Zweck

Befund 2090 integrierte einen passiven Lebenslauf gleichaltriger
Relationsnachbarschaften. Von 184.300 unterschiedlichen Kanten erschienen
22.801 bei einem späteren Eigenalter erneut. Diese Wiederkehr allein zeigt
noch nicht, ob eine bereits getragene Kante beim nächsten Alter tatsächlich
stabiler ist als ein neuer Kontakt.

2091 prüft deshalb ausschließlich die innere Fortsetzungsordnung des
Lebenslaufs. Außenwerte, Chartabschnitte und Handlungsergebnisse sind keine
Vergleichsgrößen.

## Vergleichslogik

Für jeden Übergang von Relationsalter `a` zu `a + 1` werden nur Kanten bei
Alter `a` betrachtet, deren beide Relationen das nächste Alter tatsächlich
erreichen. Jede Kante besitzt damit dieselbe grundsätzliche
Fortsetzungsmöglichkeit.

Innerhalb dieser Menge werden zwei Gruppen gebildet:

- **getragen:** Die Kante bestand bereits bei Alter `a - 1`.
- **neu:** Die Kante bestand beim unmittelbar vorherigen Alter nicht. Eine
  weiter zurückliegende Beobachtung bleibt möglich.

Fortsetzung bedeutet, dass dieselbe Relationskante auch bei Alter `a + 1`
beobachtet wird. Die Gruppen sind nur Auswertungskategorien und werden weder in
der Runtime gespeichert noch zurückgelesen.

49 Altersübergänge sind auswertbar. Bei 41 Übergängen existieren gleichzeitig
getragene und neue Kanten; nur diese informativen Schichten gehen in den
Primärvergleich ein.

## Nullkontrollen

### Altersstratifizierte Kantenlabel

Pro Alter bleiben exakt erhalten:

- alle aktuellen fortsetzungsfähigen Kanten,
- die Zahl der getragenen Kanten,
- die Zahl der Kanten, die beim nächsten Alter fortbestehen.

Nur die Zuordnung `getragen` oder `neu` wird innerhalb derselben Altersstufe
zufällig verteilt. 2.000 Ziehungen prüfen, ob die wirklichen getragenen Kanten
überzufällig oft unter den später fortgesetzten liegen.

### Relationsidentität des Zukunftsgraphen

Diese strengere Kontrolle erhält pro Alter den vollständigen Zukunftsgraphen
mit Kantenzahl und Gradstruktur. Seine Relationsidentitäten werden über alle
fortsetzungsfähigen Relationen permutiert. 1.000 Permutationen prüfen damit,
ob der beobachtete Vorsprung nur aus Größe oder Form des Zukunftsgraphen
entsteht.

## Primärer Gesamtbefund

| Merkmal | getragen | neu |
|---|---:|---:|
| fortsetzungsfähige Kanten | 10.854 | 10.242 |
| beim nächsten Alter fortgesetzt | 4.029 | 3.492 |
| Fortsetzungsrate | 0,3712 | 0,3409 |

Der absolute Abstand beträgt `0,0303` oder 3,03 Prozentpunkte. Bereits
getragene Kanten setzen sich relativ `1,0887`-mal so häufig fort. Der über die
41 Altersschichten gemeinsame Mantel-Haenszel-Odds-Faktor beträgt `1,1499`.

Die stratifizierte Null erwartet 3.861,91 fortgesetzte getragene Kanten bei
einer Standardabweichung von 34,56; beobachtet werden 4.029. Daraus folgt
`z = 4,8350` und ein einseitiger analytischer Wert von
`p = 6,66 * 10^-7`. Keine der 2.000 Kantenlabel-Ziehungen erreicht den
beobachteten Wert; mit Korrektur ergibt sich `p = 1/2001 = 0,000500`.

## Graphstrukturerhaltende Gegenprobe

| Merkmal | Wert |
|---|---:|
| beobachteter Ratendifferenz | 0,03025 |
| Nullmittel | 0,00231 |
| Null-Standardabweichung | 0,00402 |
| höchster Nullwert | 0,01448 |
| empirisches `p` | 1/1001 = 0,000999 |

Der Vorsprung bleibt damit auch dann erhalten, wenn jeder Zukunftsgraph seine
vollständige Gradstruktur und Kantenzahl behält. Die konkrete relationale
Fortsetzung trägt mehr Information als die bloße Graphform.

## Altersrobustheit

Die frühen, zahlenmäßig dominierenden Kontakte erklären den Gesamtbefund nicht
allein.

| Altersbereich | getragen | neu | relatives Verhältnis | gemeinsamer Odds-Faktor | einseitiges `p` |
|---|---:|---:|---:|---:|---:|
| 3 bis 4 | 0,3572 | 0,3421 | 1,0441 | 1,0730 | 0,0172 |
| 5 bis 9 | 0,4065 | 0,3353 | 1,2121 | 1,3470 | 2,82 * 10^-6 |
| 10 bis 20 | 0,4592 | 0,3292 | 1,3949 | 1,7332 | 0,000153 |
| 21 bis 40 | 0,5667 | 0,3889 | 1,4571 | 1,9456 | 0,00273 |

Ab Alter 10 setzen sich getragene Kanten in `49,56 %`, neue Kanten in
`34,72 %` der Fälle fort. Die spätere Verstärkung beruht jedoch auf deutlich
kleineren Kantenmengen und darf nicht als feste Reifeschwelle gelesen werden.

## Zusammenhängende Altersläufe

Von den 22.801 mehrfach beobachteten Kanten besitzen:

- 21.329 oder `93,54 %` mindestens einen direkt aufeinanderfolgenden
  Altersübergang,
- 1.472 oder `6,46 %` ausschließlich Wiederkehr mit Alterslücken.

Die längste direkt zusammenhängende Folge umfasst 13 Relationsalter. 18.404
Kanten erreichen eine Zweierfolge, 2.178 eine Dreierfolge und 536 eine
Viererfolge. Längere Bahnen werden schnell selten.

## Befund

Getragen sind:

- ein kleiner, aber überzufälliger Fortsetzungsvorteil bereits getragener
  Relationsnachbarschaften,
- Stabilität dieses Vorteils über frühe und spätere Altersschichten,
- Identitätsinformation über die reine Größe und Gradstruktur des Graphen
  hinaus,
- überwiegend direkt aufeinanderfolgende statt nur lückenhafte Wiederkehr.

Nicht getragen sind:

- eine starke oder deterministische Selbststabilisierung,
- eine feste Reifeschwelle,
- dauerhafte Mitglieder oder ein semantischer Kern,
- Selbstverstärkung durch die Memory, da sie weiterhin nicht zurückgelesen
  wird,
- Feld-, Wahrnehmungs- oder Handlungswirkung.

2091 zeigt erstmals, dass der passive Relationslebenslauf nicht nur Kontakt
archiviert. Seine eigene Vorgeschichte enthält eine schwache Information über
die nächste topologische Fortsetzung. Das ist ein inneres Eigenstabilitätsmaß,
aber noch keine Regel und keine Feldintelligenz.

## Grenzen

Die Prüfung verwendet denselben 64-Welten-Lebenslauf wie 2090. Sie ist daher
eine innere Gegenprobe, kein unabhängiger Welt-Holdout. Kanten teilen
Relationen und sind nicht vollständig unabhängig; die
graphstrukturerhaltende Relationspermutation begrenzt dieses Problem, beseitigt
aber nicht jede mögliche Abhängigkeit. In hohen Altern werden die Mengen klein.

## Reproduzierbare Ausgaben

- `2091_MCM_RELATIONSLEBENSLAUF_EIGENSTABILITAET.transitions.csv`
- `2091_MCM_RELATIONSLEBENSLAUF_EIGENSTABILITAET.sensitivity.csv`
- `2091_MCM_RELATIONSLEBENSLAUF_EIGENSTABILITAET.null.csv`
- `2091_MCM_RELATIONSLEBENSLAUF_EIGENSTABILITAET.runs.csv`
- `2091_MCM_RELATIONSLEBENSLAUF_EIGENSTABILITAET.summary.csv`

Es werden keine neuen Welt-, Debug-, Memory- oder Runtime-Dateien erzeugt.
