# 2086 - MCM-Eigenzeit-Bewegungsnachbarschaften

## Zweck

Befund 2085 gibt jeder gewachsenen MCM-Nachbarschaft eine eigene Folge
tatsächlicher Bestätigungsereignisse. Diese Prüfung untersucht, ob ähnlich
geformte Bewegungen bei gleichem Relationsalter reihenfolgenstabile
Nachbarschaften bilden.

Die Auswertung arbeitet ausschließlich auf dem kompakten Ereignisarchiv aus
2085. Es werden keine Welten erneut ausgeführt und keine Chart-, Außenwelt-
oder Handlungsmerkmale gelesen.

## Altersgleiche Prüfanordnung

Getrennt betrachtet werden die ersten 2, 3, 5 und 10 eigenen Ereignisse einer
Relation. Fehlende Ereignisse werden nicht interpoliert. Die jeweils
verfügbaren Grundlagen sind:

| Relationsalter | vorwärts | rückwärts | gemeinsame Identitäten |
|---:|---:|---:|---:|
| 2 | 1.215 | 1.155 | 991 |
| 3 | 873 | 831 | 677 |
| 5 | 601 | 574 | 451 |
| 10 | 331 | 334 | 258 |

Aus den exakten Zuwächsen zwischen aufeinanderfolgenden Eigenereignissen
entstehen vier getrennte Profilräume:

1. Eigenzeittakt aus den Abständen der Weltabschlussindizes,
2. Breitenzuwachs aus Weltpaar- und Weltlauftragung,
3. Profilzuwachs aus den drei bestehenden inneren Profilräumen,
4. gemeinsame Bewegung aller sechs Achsen.

Jede Komponente wird innerhalb derselben Altersstufe rangiert; Gleichstände
bleiben vollständig erhalten. Nur gegenseitig nächste Verläufe bilden eine
Kante. Es gibt kein `k`, keine Distanzschwelle und keine vorgegebene Familie.

Als achsenübergreifend robust gelten diagnostisch nur Paare, die gleichzeitig
im Eigenzeittakt, Breitenzuwachs und Profilzuwachs gegenseitige Nachbarn sind.

## Auflösung Der Groben Gleichstände

| Alter | exakte Rohprefixe vorwärts/rückwärts | größte Klasse vorwärts/rückwärts | exakte Identitätsmatches |
|---:|---:|---:|---:|
| 2 | 453 / 443 | 48 / 38 | 39 |
| 3 | 804 / 781 | 7 / 7 | 0 |
| 5 | 599 / 572 | 2 / 2 | 0 |
| 10 | 331 / 334 | 1 / 1 | 0 |

Bereits bei Alter 3 sind ungefähr 95 Prozent der Rohverläufe einzigartig. Ab
Alter 10 besitzt jede geprüfte Relation einen eigenen exakten Bewegungspräfix.
Die große Gleichstandswolke aus den globalen Checkpoints in Befund 2084 ist
damit aufgelöst.

## Achsenübergreifende Nachbarschaft

| Alter | robuste Kanten vorwärts/rückwärts | gemeinsame robuste Kanten | Jaccard | Nullmittel | Faktor zur Null |
|---:|---:|---:|---:|---:|---:|
| 2 | 5.401 / 4.515 | 87 | 0,0089 | 25,005 | 3,48 |
| 3 | 123 / 85 | 0 | 0,0000 | 0,025 | 0,00 |
| 5 | 4 / 3 | 0 | 0,0000 | 0,000 | 0,00 |
| 10 | 0 / 0 | 0 | 0,0000 | 0,000 | 0,00 |

Die 87 gemeinsamen Kanten bei Alter 2 sind vollständig Teil exakter
Rohgleichstände. Sobald die Bewegungen individueller werden, bleibt kein Paar
gleichzeitig über alle drei unabhängigen Achsen Nachbar.

Eine einheitliche Eigenzeit-Reifungsfamilie ist damit nicht getragen.

## Getrennte Teilräume

Die einzelnen Bewegungsräume zeigen dennoch reihenfolgenübergreifende Reste:

| Alter | Raum | gemeinsame Kanten | Jaccard | Nullmittel | Faktor zur Null | empirisches p |
|---:|---|---:|---:|---:|---:|---:|
| 3 | Eigenzeittakt | 61 | 0,0133 | 12,345 | 4,94 | 0,004975 |
| 3 | Breitenzuwachs | 29.284 | 0,1331 | 19.980,345 | 1,47 | 0,004975 |
| 3 | Profilzuwachs | 2.748 | 0,0724 | 563,705 | 4,87 | 0,004975 |
| 5 | Eigenzeittakt | 8 | 0,0149 | 0,255 | 31,37 | 0,004975 |
| 5 | Breitenzuwachs | 3.332 | 0,0737 | 1.044,905 | 3,19 | 0,004975 |
| 5 | Profilzuwachs | 109 | 0,0236 | 9,615 | 11,34 | 0,004975 |
| 10 | Eigenzeittakt | 1 | 0,0058 | 0,085 | 11,76 | 0,089552 |
| 10 | Breitenzuwachs | 171 | 0,0491 | 13,795 | 12,40 | 0,004975 |
| 10 | Profilzuwachs | 6 | 0,0166 | 0,055 | 109,09 | 0,004975 |

Die Nullkontrolle vertauscht Relationsidentitäten 200-mal nur innerhalb
derselben rückwärtigen Altersstufe. Graphdichte, Altersabdeckung und
Gleichstandsstruktur bleiben erhalten.

Breiten- und Profilzuwachs tragen auch bei Alter 10 überzufällige gemeinsame
Kanten. Die absoluten Jaccardwerte bleiben jedoch niedrig, und es sind nicht
dieselben Paare über alle Teilräume. Der Eigenzeittakt ist bei Alter 10 mit nur
einer gemeinsamen Kante nicht belastbar von der Null getrennt.

## Befund

Getragen sind:

- eine fein aufgelöste individuelle Bewegungsbiografie ohne globale
  Checkpointsättigung,
- reihenfolgenübergreifende Teilstruktur in Breiten- und Profilzuwachs,
- einzelne überzufällige Eigenzeittakt-Nachbarschaften bis Alter 5,
- die Trennung verschiedener Beziehungsaspekte statt erzwungener Einheitsform.

Nicht getragen sind:

- eine einheitliche achsenübergreifende Reifungsfamilie,
- stabile robuste Paare ab Relationsalter 3,
- Gleichsetzung einzelner Teilraumkanten mit Bedeutung,
- eine Runtime-Topologie aus Eigenzeitbewegungen,
- Feld- oder Handlungsrückwirkung.

Die feinere Eigenzeit zeigt damit keine gemeinsame Familie, sondern mögliche
unterschiedliche Beziehungsschichten: Eine Relation kann im Breitenzuwachs
ähnlich zu einer anderen sein, ohne denselben Eigenzeittakt oder dieselbe
Profilbewegung zu besitzen. Diese Multiplex-Lesung bleibt ein passiver
Forschungskandidat und wird nicht in die Memory integriert.

## Reproduzierbare Ausgaben

- `2086_MCM_EIGENZEIT_BEWEGUNGSNACHBARSCHAFTEN.coverage.csv`
- `2086_MCM_EIGENZEIT_BEWEGUNGSNACHBARSCHAFTEN.identity.csv`
- `2086_MCM_EIGENZEIT_BEWEGUNGSNACHBARSCHAFTEN.graphs.csv`
- `2086_MCM_EIGENZEIT_BEWEGUNGSNACHBARSCHAFTEN.order.csv`
- `2086_MCM_EIGENZEIT_BEWEGUNGSNACHBARSCHAFTEN.null.csv`
- `2086_MCM_EIGENZEIT_BEWEGUNGSNACHBARSCHAFTEN.summary.csv`

Die Auswertung liest nur
`data/2085_mcm_neighborhood_event_histories.zip`. Sie erzeugt keine Welt-,
Debug- oder Runtime-Memory-Dateien.
