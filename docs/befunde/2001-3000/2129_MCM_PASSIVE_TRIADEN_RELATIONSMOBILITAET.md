# 2129 - Passive MCM-Triaden-Relationsmobilitaet

## Zweck

2128 fand mit der signierten Aenderung relationaler Umbildungsbreite einen
feldlokalen, schwellenfreien und gegen Neuronen-Umbenennung invarianten
Informationstraeger. 2129 prueft, ob drei verschieden erfahrene Mikrofelder
aus diesem Trager bereits eine bewegliche gemeinsame Relation bilden.

Die drei Mikrofelder bleiben vollstaendig unverbunden. Es gibt keine
Rueckwirkung, kein Zentralfeld und keine semantische Rolle.

## Triadenbildung

Die 48 beziehungsweise 44 Quellen werden ausschliesslich nach dem SHA-256
ihrer Quellschluessel geordnet und in Dreiergruppen gelegt. Asset, Jahr,
Dateireihenfolge und Ergebnis wirken nicht auf die Gruppierung.

Es entstehen:

- 16 Triaden im Entwicklungsbestand,
- 15 Triaden im Holdout,
- 256 beziehungsweise 240 Triade-Ziel-Pfade.

Jede Triade erlebt dieselben acht Ziele in Universum A und acht disjunkte
Ziele in Universum B. Alle Felder laufen isoliert auf ihren eigenen
kontinuierlichen Zustaenden.

## Passive Relationslesung

Pro Tick werden nur die drei 2128-Deltaereignisse verglichen.

Eine Kante entsteht, wenn zwei Felder einander bei absolutem Deltaabstand
gegenseitig am naechsten sind. Exakte Gleichstaende bleiben als mehrere
Kanten sichtbar. Ein moegliches Zentrum ist der Medoid der drei Deltas;
mehrere gleich gute Medoide bleiben ebenfalls erhalten.

Die Beobachtung programmiert weder einen bevorzugten Partner noch ein
Zentralfeld. Partner- und Zentrumsmengen koennen in jedem Tick wechseln.

## Zeitnull

32 Nullfolgen verschieben die vollstaendige Deltaereignisfolge jedes Feldes
unabhaengig im Kreis. Jede lokale Ereignismenge und Eigenkadenz bleibt
erhalten; nur die Gleichzeitigkeit zwischen den drei Feldern wird geloest.

## Erste Gesamtlesung

Ohne Ausschluss von Gleichstaenden erscheint eine sehr starke gemeinsame
Ordnung:

- Partner- und Zentrumskollisionen liegen in beiden Bestaenden und beiden
  Zieluniversen ueber allen 32 Zeitnullen.
- Alle 496 Pfade besitzen positiven Kollisionsexzess.
- Partnerlagen wechseln im Mittel 9,93 beziehungsweise 10,24 Mal.
- Zentrumslagen wechseln im Mittel 10,16 beziehungsweise 10,55 Mal.
- Die A/B-Triadenidentitaet erreicht je nach Relationsprofil AUC 0,858 bis
  0,914, jeweils ueber allen 4.096 Labelnullen.

Diese Lesung allein waere jedoch irrefuehrend.

## Gleichstandsgrenze

Im Mittel besitzen etwa 54 von 64 Ticks mehrere gleichnahe Partner. Bei den
Zentren sind es etwa 62 von 64 Ticks. Der grosse Kollisionsexzess wird damit
ueberwiegend durch gemeinsam entstehende Gleichstaende und Konvergenz
getragen.

Eine strenge Ablation behaelt deshalb nur Ticks, an denen alle drei
Deltaereignisse verschieden sind. Partner und Zentrum sind dort ohne
Tie-Aufloesung eindeutig.

Solche Ticks sind selten:

| Bestand | Mittel pro Pfad | Minimum | Maximum | Pfade ohne strikten Tick |
| --- | ---: | ---: | ---: | ---: |
| 2091 Basis | 2,20 | 0 | 6 | 21 |
| 2092 Holdout | 1,95 | 0 | 7 | 13 |

## Strenge Wiederkehr

Die absolute Wiederkehr eindeutiger Partner und Zentren liegt in beiden
Bestaenden weit unter der Zeitnull. Das bleibt auch bestehen, wenn die
Kollisionen durch die Zahl der tatsaechlich vorhandenen eindeutigen
Gelegenheiten geteilt werden.

Im Holdout sind alle strengen Ratendifferenzen negativ:

| Universum | Partner-Ratendifferenz | Zentrum-Ratendifferenz | p oben |
| --- | ---: | ---: | ---: |
| A | -9,89 | -14,11 | 1,0 / 1,0 |
| B | -13,21 | -14,93 | 1,0 / 1,0 |
| gesamt | -23,10 | -29,04 | 1,0 / 1,0 |

Damit reproduziert keine zeitlich wiederkehrende eindeutige Partnerbindung.

## Verbleibende fruehe Konfiguration

Die Verteilung der wenigen eindeutigen Lagen traegt dennoch
Vorwelterfahrung zwischen A und B:

| Bestand | strenges kombiniertes Profil AUC A/B | AUC B/A | Labelnull-p A/B |
| --- | ---: | ---: | ---: |
| 2091 Basis | 0,902 | 0,921 | 0,000244 / 0,000244 |
| 2092 Holdout | 0,776 | 0,805 | 0,000732 / 0,000244 |

Der anonyme strenge Graph reproduziert im Holdout jedoch nicht: Nur 2 von 7
gegenseitigen Kanten verbinden nachtraeglich dieselbe Triade
(`p = 0,0769`).

Getragen ist deshalb eine seltene fruehe triadenspezifische Konfiguration,
nicht eine wachsende oder wiederkehrende Triadenbeziehung.

## Befund

Getragen sind:

- passive Partner- und Zentrumsbewegung ohne Feldkopplung,
- breite Gleichzeitigkeit der drei Deltaereignisse,
- wenige eindeutige fruehe Konfigurationen mit A/B-Transfer,
- Beweglichkeit statt festem Partner oder Zentralfeld.

Nicht getragen sind:

- wiederkehrende eindeutige Partnerbindung ueber der Zeitnull,
- ein reproduzierter anonymer strenger Holdout-Graph,
- organisch entstandene Triadenmitgliedschaft,
- Mehrfeldtopologie, Feldrueckwirkung, Memory, Semantik oder Handlung.

2129 verhindert damit eine vorschnelle Integration: Die starke volle
Triadenordnung ist primaer gemeinsame Konvergenz. Der kleine eindeutige Rest
bewahrt Erfahrung, besitzt aber noch keine eigene relationale Persistenz.

## Architekturentscheidung

- keine Verbindung zwischen Mikrofeldern,
- keine Integration eines Zentrums oder Partners,
- kein Triaden-Memory,
- keine Schwelle oder Kopplungsverstaerkung,
- keine Aenderung am Produktionsfeld,
- kein Handlungsdurchgriff und kein Viranzparameter.

## Reproduzierbarkeit

Ausgaben:

- `2129_MCM_PASSIVE_TRIADEN_RELATIONSMOBILITAET.paths.csv`
- `2129_MCM_PASSIVE_TRIADEN_RELATIONSMOBILITAET.temporal.csv`
- `2129_MCM_PASSIVE_TRIADEN_RELATIONSMOBILITAET.transfer.csv`
- `2129_MCM_PASSIVE_TRIADEN_RELATIONSMOBILITAET.graph.csv`

SHA-256:

- `paths`: `70994C843E2BB2B4E5A6A7B9437E3502E6BFCC3E64A8FDFA5E1B9EEC862CB005`
- `temporal`: `4B12C31F51FD63B33DD6583FCB767F56E52061AAD6B5E2646C9D190C367F467C`
- `transfer`: `DFEB7AD862AA7CD5C045E00C4A7A748A48BE6F5D71FCC54793EB4F0A10F6732F`
- `graph`: `C305466AB368AE542F001D535EF327C0444939701D2205AB6DA9D6A86509A60B`

Runner: `tools/run_mcm_passive_triad_relational_mobility.py`

Test: `tests/test_mcm_passive_triad_relational_mobility.py`
