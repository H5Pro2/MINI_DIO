# 2112 - Kontinuierliche Rangzyklus-Selbstsegmentierung

## Zweck

Befund 2111 schliesst intrinsische Formprofile durch die erste exakte
Wiederkehr einer neuronalen Rangordnung. Der Segmentierer begann dort jedoch
erst an der von aussen bereitgestellten Kontaktgrenze.

2112 prueft deshalb, ob derselbe Rangzyklus ohne Reset durch eine vollstaendige
Vorwelt und eine direkt anschliessende Zielwelt laufen, geschlossene Episoden
selbst wieder oeffnen und dabei weiterhin quellgebundene Form tragen kann.

## Durchgehender Feldstrom

Jeder Versuch besteht aus:

```text
vollstaendige Vorwelt -> vollstaendige Zielwelt
```

Feld und Segmentierer laufen ueber diesen Uebergang unveraendert weiter. Der
Segmentierer erhaelt weder den Grenztick noch Welt-, Asset-, Jahres- oder
Herkunftsinformation. Fuer jede der 48 beziehungsweise 44 Vorwelten werden die
acht Ziele beider disjunkten Universen aus 2109 angeschlossen. Insgesamt
entstehen 1.472 kontinuierliche Vorwelt-Zielwelt-Stroeme.

Es gibt am verdeckten Uebergang:

- keinen Feldreset,
- keinen Segmentiererreset,
- kein erzwungenes Schliessen oder Oeffnen,
- keine feste Episodendauer,
- kein Reset- oder Nullfeld,
- kein Lernen, Memory oder Handlung.

## Fortlaufende Selbstsegmentierung

Nach jeder exakten Rangwiederkehr wird die Abschlussordnung zum neuen
Ruheanker. Eine spaetere neue Rangordnung oeffnet die naechste Episode. Deren
erste exakte Wiederkehr schliesst sie wieder. Derselbe kleine Zustandsprozess
laeuft beliebig oft weiter:

```text
Ruheanker -> neue Rangordnung -> offene Episode
offene Episode -> erste exakte Wiederkehr -> Abschluss und neuer Ruheanker
```

Damit wird weder ein Kontakttick noch eine Episodenzahl als Feldregel gesetzt.

## Strenge Nachgrenzen-Auswertung

Die versteckte Vorwelt-Zielwelt-Grenze wird erst nach dem Lauf fuer eine
methodische Gegenprobe gelesen. Eine Episode gelangt nur dann in das Profil,
wenn sie vollstaendig nach dieser Grenze selbst geoeffnet und geschlossen
wurde.

640 von 768 Basisstroemen und 592 von 704 Holdoutstroemen tragen beim
verdeckten Uebergang noch eine bereits in der Vorwelt geoeffnete Episode. Alle
diese grenzuebergreifenden Episoden werden verworfen. Dadurch kann keine vor
dem Zielkontakt beobachtete Rangbewegung in das Quellprofil durchsickern.

Die Grenze steuert weder Segmentierung noch Graphbildung. Sie dient nur dem
nachtraeglichen Ausschluss dieses direkten Informationslecks.

## Reiche endogene Episodenbildung

| Bestand | Stroeme | strikte Episoden Minimum | Median | Maximum |
|---|---:|---:|---:|---:|
| 2091-Bestand | 768 | 172 | 183 | 205 |
| 2092-Holdout | 704 | 176 | 186 | 205 |

Jeder Strom bildet deutlich mehr als 64 vollstaendig nachgrenzige Episoden.
Der Mechanismus kann sich somit ohne Reset wiederholt schliessen und erneut
oeffnen. Es fehlt nicht an endogener Zyklusaktivitaet.

## Erste strikte Episode

| Bestand | Oeffnung Minimum | Oeffnung Median | Oeffnung Maximum | Schliessung Minimum | Schliessung Median | Schliessung Maximum |
|---|---:|---:|---:|---:|---:|---:|
| 2091 | 1 | 3 | 13 | 2 | 7 | 27 |
| 2092 | 1 | 3 | 10 | 2 | 8 | 20 |

Die erste nicht kontaminierte Episode beginnt in beiden Bestaenden median drei
Ticks nach dem verdeckten Kontaktwechsel. Sie ist jedoch erst bei Tick 7
beziehungsweise 8 geschlossen. Der gemeinsame starke Quellformbereich aus
2110 lag bei 1 bis 4 Ticks.

## Endogene Episodenskala

Die Profile werden nach den ersten 1, 2, 4, 8, 16, 32 und 64 vollstaendig
selbstsegmentierten Episoden sowie ueber alle Episoden gelesen. Diese Skala ist
nur ein Forschungsinstrument. Keine dieser Zahlen wird als organische
Laufzeit, Auswahlregel oder Memory-Grenze in DIO integriert.

Wie in 2110 und 2111 werden nur gerichtete Wechsel der 66 paarweisen
Neuronenrelationen gezaehlt, ueber acht Zielwelten je Universum addiert und
staerkenormiert.

## Verteilungsweite Quelltrennung

| Bestand | Episoden | A nach B | B nach A |
|---|---:|---:|---:|
| 2091 | 1 | 0,615 | 0,615 |
| 2091 | 2 | 0,629 | 0,612 |
| 2091 | 4 | 0,570 | 0,538 |
| 2091 | 8 | 0,508 | 0,503 |
| 2091 | 16 | 0,510 | 0,525 |
| 2091 | 32 | 0,513 | 0,510 |
| 2091 | 64 | 0,516 | 0,507 |
| 2091 | alle | 0,544 | 0,552 |
| 2092 | 1 | 0,642 | 0,547 |
| 2092 | 2 | 0,586 | 0,545 |
| 2092 | 4 | 0,534 | 0,541 |
| 2092 | 8 | 0,518 | 0,511 |
| 2092 | 16 | 0,524 | 0,558 |
| 2092 | 32 | 0,498 | 0,530 |
| 2092 | 64 | 0,506 | 0,511 |
| 2092 | alle | 0,503 | 0,498 |

In den ersten ein bis zwei Episoden bleibt eine schwache verteilte
Quellinformation. Sie ist deutlich kleiner als in 2111 und zerfaellt unter
weiterer selbstsegmentierter Erfahrung weitgehend in die Naehe von 0,5. Eine
verteilte Restinformation reicht zudem nicht fuer eine organische lokale
Topologie.

## Anonymer gegenseitiger Graph

| Bestand | Episoden | gegenseitige Kanten | gleiche Quelle nachtraeglich | Labelnull-p |
|---|---:|---:|---:|---:|
| 2091 | 1 | 6 | 3 | 0,000244 |
| 2091 | 2 | 2 | 1 | 0,0388 |
| 2091 | 4 | 1 | 0 | 1,0 |
| 2091 | 8 | 1 | 0 | 1,0 |
| 2091 | 16 | 1 | 0 | 1,0 |
| 2091 | 32 | 2 | 0 | 1,0 |
| 2091 | 64 | 1 | 0 | 1,0 |
| 2091 | alle | 2 | 0 | 1,0 |
| 2092 | 1 | 6 | 0 | 1,0 |
| 2092 | 2 | 2 | 0 | 1,0 |
| 2092 | 4 | 2 | 0 | 1,0 |
| 2092 | 8 | 2 | 0 | 1,0 |
| 2092 | 16 | 1 | 0 | 1,0 |
| 2092 | 32 | 1 | 0 | 1,0 |
| 2092 | 64 | 2 | 0 | 1,0 |
| 2092 | alle | 1 | 0 | 1,0 |

Der einzelne Fruehtreffer im Entwicklungsbestand reproduziert nicht. Der
Holdout bildet bereits bei der ersten strikten Episode keine gleichquellige
Kante. Ab vier Episoden tragen beide Bestaende keine lokale Quellnachbarschaft
mehr.

Der Graph entsteht weiterhin ohne Herkunfts-, Asset-, Jahres-, Grenz- oder
Weltwissen. Die Quellen werden erst nach abgeschlossener Kantenbildung gelesen.

## Befund

Getragen sind:

- ein Rangzyklus-Segmentierer, der ohne Reset fortlaufend schliesst und wieder
  oeffnet,
- 172 bis 205 strikte endogene Episoden pro Zielkontakt,
- ein medianer selbst bestimmter Wiederbeginn drei Ticks nach dem verdeckten
  Kontaktwechsel,
- eine schwache verteilte Quellrestform in den ersten Ereignissen,
- der vollstaendige Ausschluss vorgrenziger Rangbewegung aus den Profilen,
- Reproduktion der Segmentierungsfaehigkeit in beiden Bestaenden.

Nicht getragen sind:

- eine reproduzierbare lokale Quelltopologie der selbst gestarteten Episoden,
- die gleichzeitige Bewahrung des starken 1- bis 4-Tick-Formtraegers aus 2110,
- eine feldinterne Auswahl, welche der vielen Rangzyklen kontaktrelevant ist,
- ein autonom erkannter Kontaktwechsel,
- eine speicherreife Formepisode,
- Semantik, Memory, Rueckwirkung oder Handlung.

2112 zeigt eine wichtige Trennung: Das Feld kann seine Rangzyklen fortlaufend
und ohne Grenzsignal selbst segmentieren. Diese reine Schliessungs- und
Wiederoeffnungsmechanik waehlt jedoch noch nicht die Episode aus, in der die
quellgebundene Form robust liegt. Die erste strikte Episode schliesst dafuer im
Median zu spaet, und der lokale Quellgraph reproduziert nicht im Holdout.

Damit ist die Selbstsegmentierung mechanisch real, aber noch kein tragfaehiger
organischer Formtraeger fuer Memory oder weitere Feldwirkung.

## Reproduzierbare Ausgaben

- `2112_MCM_KONTINUIERLICHE_RANGZYKLUS_SEGMENTIERUNG.paths.csv`
- `2112_MCM_KONTINUIERLICHE_RANGZYKLUS_SEGMENTIERUNG.edges.csv`
- `2112_MCM_KONTINUIERLICHE_RANGZYKLUS_SEGMENTIERUNG.summary.csv`

Der Runner ist `tools/run_mcm_continuous_rank_self_segmentation.py`. Er
erzeugt keine Welt-, Runtime-, Memory- oder Debugdateien.
