# 2108 - Kontextstabilitaet der quellgebundenen MCM-Form

## Zweck

Befund 2107 findet eine quellgebundene relative Form in den gerichteten
neuronalen Rangwechseln. Die Wiedererkennung war zwischen den beiden dort
verwendeten Zielgruppen unterschiedlich stark. 2108 prueft deshalb, ob der
Befund von einer guenstigen Aufteilung der Zielwelten abhing.

Die Frage lautet:

```text
Bleibt die konkrete Vorwelt unterscheidbar,
wenn dieselben acht Zielwelten
auf jede moegliche ausgeglichene Weise
in zwei unabhaengige Vierergruppen geteilt werden?
```

Es gibt keine Ergebniswahl, keine Feldrueckwirkung und keine neue
Identitaetsdefinition.

## Erschoepfende Zielaufteilung

2108 verwendet exakt die acht datenblind per SHA-256 bestimmten Zielwelten und
die davon getrennten 56 beziehungsweise 52 Vorweltidentitaeten aus 2107.

Acht Zielwelten besitzen 70 moegliche Vierergruppen. Da jede Gruppe und ihr
Komplement dieselbe Aufteilung mit vertauschten Seiten bilden, bleiben 35
einzigartige komplementaere Aufteilungen:

```text
C(8, 4) / 2 = 35
```

Alle 35 werden geprueft. Die erste Zielwelt bleibt nur zur Vermeidung der
komplementaeren Doppelzaehlung immer auf Seite A. Beide Leserichtungen A nach B
und B nach A werden getrennt erhalten.

Damit entstehen je Datenbestand 70 gerichtete Aufteilungspruefungen und
insgesamt 140.

## Strengste Lesung aus 2107

Die Auswertung behaelt nur die bereits strengste 2107-Bedingung:

- staerkenormierte relative Rangwechselform,
- ungewichtete Manhattan-Distanz,
- Konkurrenz nur zwischen Fenstern desselben Assets und Jahres,
- exakte Distanzgleichstaende ohne erzwungenen Sieger,
- Herkunftslabel ausschliesslich nach dem Feldlauf.

Rohe Nachhallstaerke und globale Asset-/Jahresunterschiede koennen den Befund
damit nicht tragen.

## Alle Aufteilungen tragen dieselbe Richtung

| Bestand | Richtung | minimale AUC | Median AUC | mittlere AUC | maximale AUC | AUC ueber 0,5 |
|---|---|---:|---:|---:|---:|---:|
| 2091 | A nach B | 0,600 | 0,793 | 0,790 | 0,903 | 35/35 |
| 2091 | B nach A | 0,691 | 0,818 | 0,812 | 0,893 | 35/35 |
| 2092 | A nach B | 0,625 | 0,835 | 0,825 | 0,912 | 35/35 |
| 2092 | B nach A | 0,660 | 0,815 | 0,816 | 0,923 | 35/35 |

Keine einzige ausgeglichene Zielaufteilung faellt auf oder unter die
ungebundene AUC von 0,5. Auch die jeweils schwaechste Zusammensetzung bewahrt
eine gleichgerichtete Quelltrennung.

Die einzelne schwaechere Richtung aus 2107 war damit kein ausgewaehlter
Sonderfall. Sie lag am unteren Rand einer breiteren, durchgehend getragenen
Verteilung.

## Eindeutige Nachbarn pro Aufteilung

Die Zahl der Vorwelten, deren eigenes Profil der eindeutig naechste
Formnachbar ist, bleibt kontextabhaengig:

| Bestand | Richtung | Minimum | Median | Maximum |
|---|---|---:|---:|---:|
| 2091 | A nach B | 7 | 17 | 25 |
| 2091 | B nach A | 10 | 16 | 25 |
| 2092 | A nach B | 10 | 23 | 29 |
| 2092 | B nach A | 11 | 22 | 32 |

Die Population traegt in jeder Aufteilung Quellform, aber die konkrete Menge
eindeutig gelesener Vorwelten wechselt mit der Zusammensetzung der Zielreize.
Quellform ist daher relational und kontextuell, nicht ein festes Etikett am
Vorzustand.

## Breite ueber einzelne Vorwelten

Fuer jede Vorwelt wird ihre mittlere AUC ueber alle 35 Aufteilungen gelesen:

| Bestand | Richtung | Quellen mit mittlerer AUC ueber 0,5 | Quellen in allen Aufteilungen ueber 0,5 | niedrigste Quellenmittel-AUC |
|---|---|---:|---:|---:|
| 2091 | A nach B | 56/56 | 18/56 | 0,508 |
| 2091 | B nach A | 56/56 | 15/56 | 0,628 |
| 2092 | A nach B | 52/52 | 12/52 | 0,598 |
| 2092 | B nach A | 51/52 | 13/52 | 0,469 |

Die Quelltrennung wird damit breit von den Vorwelten getragen. Sie ist jedoch
nicht fuer jede einzelne Identitaet in jedem Zielkontext stabil. Im
Holdout-Rueckweg liegt eine von 52 Vorwelten im Mittel unter 0,5; in jeder
Richtung verlieren viele Quellen in mindestens einer Aufteilung ihre
individuelle Trennung.

## Gemeinsame Gruppenlabelnull

Die Herkunftslabels werden 4.096-mal innerhalb desselben Assets und Jahres
vertauscht. Eine Nullwiederholung verwendet fuer jede Vorwelt ueber alle 35
Aufteilungen dasselbe vertauschte Label. Die Null kann sich dadurch nicht an
jede Zielzusammensetzung neu anpassen.

| Bestand | Richtung | beobachtete Gesamt-AUC | mittlere Null-AUC | hoechste Null-AUC | empirisches p |
|---|---|---:|---:|---:|---:|
| 2091 | A nach B | 0,790 | 0,500 | 0,591 | 0,000244 |
| 2091 | B nach A | 0,812 | 0,500 | 0,617 | 0,000244 |
| 2092 | A nach B | 0,825 | 0,499 | 0,635 | 0,000244 |
| 2092 | B nach A | 0,816 | 0,500 | 0,621 | 0,000244 |

Alle vier Gesamtwerte liegen oberhalb jeder zugehoerigen gemeinsamen
Labelnull. Auch die ueber Aufteilungen summierten eindeutigen Naechsttreffer
liegen in allen vier Pruefungen ueber jeder Null.

## Mechanische Grenze

2108 erzeugt keine neuen Feldpfade gegenueber 2107. Dieselben 448 und 416
Quell-Ziel-Kontakte werden nur in allen moeglichen Zielgruppierungen gelesen.
447 von 448 beziehungsweise 416 von 416 Pfaden enthalten mindestens einen
Rangwechsel. Alle 864 Pfade konvergieren bitgenau zum Resetfeld.

Die Stabilitaet ist daher weder dauerhaft abweichender Feldzustand noch
zusatzliche Speicherung.

## Befund

Getragen sind:

- Quelltrennung in allen 140 gerichteten Zielaufteilungspruefungen,
- dieselbe Form nach Entfernung der gesamten Nachhallstaerke,
- Erhalt innerhalb gleicher Assets und Jahre,
- hohe mittlere Trennung in Entwicklungsbestand und Holdout,
- breite Beteiligung fast aller Vorweltidentitaeten im Mittel,
- vollstaendige spaetere Konvergenz aller Feldpfade.

Nicht getragen sind:

- identische Staerke fuer jede Zielzusammensetzung,
- eindeutige Wiedererkennung jeder Vorwelt,
- individuelle Stabilitaet jeder Quelle in jeder Aufteilung,
- Stabilitaet ueber andere, neu gewaehlte Zieluniversen,
- ein vom Feld selbst gelesenes Identitaetssymbol,
- Memory, Semantik, autonome Aktivitaet oder Handlung.

2108 zeigt, dass die quellgebundene Mikrotopologie kein Produkt einer einzigen
guenstigen Zielaufteilung ist. Sie bleibt als Populationseigenschaft unter
jeder moeglichen ausgeglichenen Zusammensetzung des vorhandenen Zieluniversums
sichtbar.

Die Form ist zugleich organisch kontextabhaengig: Welche einzelne Vorwelt klar
erkennbar wird, entsteht aus ihrem Vorzustand im Zusammenspiel mit den
nachfolgenden Reizen. Das ist tragfaehiger als ein festes Identitaetsetikett,
aber noch keine realisierte Innenidentitaet.

## Reproduzierbare Ausgaben

- `2108_MCM_KONTINUITAET_KONTEXTSTABILITAET.partitions.csv`
- `2108_MCM_KONTINUITAET_KONTEXTSTABILITAET.summary.csv`

Der Runner ist `tools/run_mcm_continuity_context_stability.py`. Er erzeugt
keine Welt-, Runtime-, Memory- oder Debugdateien.
