# 2116 - Zyklusuebergreifende partielle MCM-Relationen

## Zweck

Befund 2115 zeigt, dass die exakte Wiederkehr vollstaendiger Episodenformen
keine individuelle Quelltopologie traegt. Eine organische semantische
Topologie koennte jedoch aus kleineren inneren Beziehungen statt aus ganzen
Episoden entstehen.

2116 prueft deshalb, ob einzelne gerichtete Neuronenrelationswechsel ueber
aufeinanderfolgende endogene Rangzyklen tragen.

## Partielle Relation

Jede Rangzyklus-Episode besitzt bis zu 396 beobachtbare Slots:

```text
66 Neuronenpaare
x 6 gerichtete Relationswechsel
= 396 partielle Formstellen
```

Pro Episode wird nur gelesen, ob ein Slot beteiligt ist. Seine Haeufigkeit
innerhalb der Episode wird auf `0` oder `1` reduziert. Alle Slots bleiben
gleichberechtigt und unbenannt.

Eine partielle Relation traegt ueber eine Zyklusgrenze, wenn derselbe Slot in
beiden direkt benachbarten Episoden beteiligt ist:

```text
Slot in Episode n aktiv
und
derselbe Slot in Episode n+1 aktiv
-> eine Mittragsbeobachtung
```

Eine Rueckkehr nach einer Luecke gilt nicht als unmittelbares Mittragen. Es
gibt keine Mindestdauer, Aehnlichkeitsschwelle oder Gewichtung.

## Abgrenzung

Der Begriff `partielle Relation` bezeichnet in 2116 ausschliesslich die
erneute Beteiligung desselben gerichteten Rangwechsels. Er behauptet nicht,
dass eine feste Neuronenverbindung, Bedeutung oder semantische Kante besteht.

Feld und Segmentierer erhalten weiterhin keine Kontaktgrenze. Die
nachtraegliche Grenze verhindert nur, dass die in allen Zielzweigen identische
Vorweltphase mehrfach in die Profile kopiert wird.

## Zwei Lesungen

Aus denselben selbstsegmentierten Episoden entstehen:

- `episode_relation_participation`: Wie oft ist jeder Slot in einer Episode
  beteiligt?
- `consecutive_partial_relation_carry`: Wie oft ist jeder Slot auf beiden
  Seiten einer direkten Zyklusgrenze beteiligt?

Je Quelle werden die acht Zielstroeme eines Universums addiert und
staerkenormiert. Die zwei Zieluniversen bleiben disjunkt. Ein globaler
gegenseitiger Nachbarschaftsgraph wird ohne Quellen-, Asset- oder Jahreswissen
gebildet.

## Dichte des Mittragens

| Bestand | Stroeme | mit Mittragen | Beobachtungen Minimum | Median | Maximum |
|---|---:|---:|---:|---:|---:|
| 2091-Bestand | 768 | 768 | 1.287 | 1.556 | 1.721 |
| 2092-Holdout | 704 | 704 | 1.412 | 1.535 | 1.825 |

Jeder Strom besitzt eine breite zyklusuebergreifende Relationsschicht.

| Bestand | getragene Slots Minimum | Median | Maximum | Zyklusgrenzen mit Mittragen |
|---|---:|---:|---:|---:|
| 2091 | 38 | 44 | 51 | 91,1 bis 99,0 %, Median 95,1 % |
| 2092 | 36 | 44 | 57 | 90,1 bis 98,0 %, Median 94,1 % |

Die Auswertung ist damit weder durch seltene Ereignisse noch leere Profile
begrenzt. Partielle Relationsfortsetzung ist eine dominante Eigenschaft der
laufenden Rangzyklusfolge.

## Beteiligungsbasis

| Bestand | Richtung | AUC | hoechste Labelnull-AUC | p |
|---|---|---:|---:|---:|
| 2091 | A nach B | 0,518 | 0,527 | 0,00464 |
| 2091 | B nach A | 0,519 | 0,521 | 0,00146 |
| 2092 | A nach B | 0,517 | 0,543 | 0,0996 |
| 2092 | B nach A | 0,495 | 0,531 | 0,727 |

Die reine Slotbeteiligung behaelt im Entwicklungsbestand eine sehr kleine
verteilte Quellrestform. Der Holdout reproduziert sie nicht. In beiden
Bestaenden entstehen nur ein bis zwei gegenseitige Kanten und keine davon
verbindet nachtraeglich dieselbe Quelle.

Diese Basis bestaetigt die bereits bekannte Trennung zwischen schwacher
Verteilungsinformation und fehlender lokaler Topologie.

## Zyklusuebergreifendes Mittragsprofil

| Bestand | Richtung | AUC | hoechste Labelnull-AUC | p |
|---|---|---:|---:|---:|
| 2091 | A nach B | 0,502 | 0,507 | 0,225 |
| 2091 | B nach A | 0,504 | 0,510 | 0,0871 |
| 2092 | A nach B | 0,494 | 0,511 | 0,943 |
| 2092 | B nach A | 0,497 | 0,510 | 0,884 |

Keine Leserichtung liegt belastbar oberhalb ihrer formerhaltenden
Quellenlabelnull. Das unmittelbare Mittragen verdichtet die kleine
Beteiligungsrestform nicht, sondern entfernt sie weitgehend.

## Anonymer gegenseitiger Graph

| Bestand | Profil | gegenseitige Kanten | gleiche Quelle nachtraeglich | Labelnull-p |
|---|---|---:|---:|---:|
| 2091 | Beteiligung | 2 | 0 | 1,0 |
| 2091 | Mittragen | 1 | 0 | 1,0 |
| 2092 | Beteiligung | 1 | 0 | 1,0 |
| 2092 | Mittragen | 1 | 0 | 1,0 |

In keinem Fall entsteht eine lokale Verbindung derselben Quelle zwischen den
disjunkten Zieluniversen.

## Interpretation

Partielle Relationsfortsetzung ist real, breit und reproduzierbar. Sie ist
jedoch so allgemein in der Rangzyklusdynamik verteilt, dass ihre relative Form
keine individuelle Feldgeschichte bewahrt.

Damit gilt:

```text
Innere Relationsslots tragen ueber Zyklen.   getragen
Dieses Mittragen waehlt relevante Relationen. nicht getragen
```

Die Zerlegung ganzer Episoden in kleinere Relationsbestandteile loest den
Engpass aus 2114 und 2115 daher nicht. Auch eine sehr dichte partielle
Kontinuitaet ist noch keine organische semantische Topologie.

## Befund

Getragen sind:

- unmittelbares Mittragen partieller Relationsslots in allen 1.472 Stroemen,
- 36 bis 57 verschiedene getragene Slots pro Strom,
- Mittragen ueber mehr als 90 % der Zyklusgrenzen,
- eine vollstaendig binarisierte und schwellenfreie Beteiligungslesung,
- Reproduktion der dichten Tragerschicht in beiden Bestaenden,
- gefuellte Quellenprofile in beiden disjunkten Zieluniversen.

Nicht getragen sind:

- universumsuebergreifende Quelltrennung durch unmittelbares Mittragen,
- gleichquellige anonyme Nachbarschaften,
- ein Vorteil gegenueber blosser Episodenbeteiligung,
- partielle Zykluskontinuitaet als Relevanz- oder Wachstumsbedingung,
- eine neue Relations- oder Rangzyklus-Memory,
- Semantik, Rueckwirkung oder Handlung.

2116 zeigt einen weiteren realen inneren Traeger, aber keine Auswahl. Die
laufende MCM-Felddynamik bewahrt partielle Relationsbeteiligung dicht ueber
Zyklusgrenzen, ohne daraus eine individuell tragende Topologie zu bilden.

Damit ist auch unmittelbare partielle Relationsfortsetzung allein nicht als
semantisches Wachstumsrecht fundiert.

## Reproduzierbare Ausgaben

- `2116_MCM_ZYKLUSUEBERGREIFENDE_PARTIALRELATIONEN.paths.csv`
- `2116_MCM_ZYKLUSUEBERGREIFENDE_PARTIALRELATIONEN.edges.csv`
- `2116_MCM_ZYKLUSUEBERGREIFENDE_PARTIALRELATIONEN.summary.csv`

Der Runner ist `tools/run_mcm_cross_cycle_partial_relations.py`. Er erzeugt
keine Welt-, Runtime-, Memory- oder Debugdateien.
