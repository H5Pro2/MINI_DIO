# 2083 - Exakte Delta-Konsolidierung der MCM-Nachbarschaft

## Zweck

Befund 2082 bewahrte fünf Reifungsstände der passiven
MCM-Nachbarschafts-Memory verlustfrei, erhöhte die gesamte Memory-Größe aber um
rund 32 bis 33 Prozent. Diese Prüfung untersucht, ob dieselbe Reifungsbahn ohne
inhaltliche Auswahl kompakter gespeichert werden kann.

Die Kompaktierung darf keine Relation löschen, dämpfen, zusammenlegen oder
bevorzugen. Sie verändert nur die technische Darstellung bereits beobachteter
Werte.

## Schwellenfreies Deltaformat

Checkpoint-Metadaten werden einmal zentral gespeichert. Jede Relation enthält
nur noch:

- ihre beiden inneren Episodenknoten,
- ihre Nachbarschaftsidentität,
- eine Folge ganzzahliger Änderungsvektoren.

Der erste Vektor enthält den vollständigen Ausgangsstand aus Checkpointindex,
Pareto-Tiefe, Weltpaartragung, Weltbreite und Bestätigungszahl. Jeder weitere
Vektor enthält nur die exakte Differenz zum vorherigen Stand. Maximale Tiefe,
Bezeichnung und Laufindex stammen aus dem gemeinsamen Checkpoint. Die
normierte Tiefe wird daraus deterministisch rekonstruiert.

Es gibt keine Rundung, Mindeständerung, Häufigkeitsgrenze oder Prioritätsregel.

## Prüfanordnung

Dieselben 81 archivierten Welten wachsen erneut in zwei getrennten Memories
vorwärts und rückwärts. Nach 10, 20, 40, 60 und 81 Welten wird die kompakte
Reifungshistorie außerhalb des Feldlaufs fortgeschrieben.

An jedem der zehn Checkpoints werden geprüft:

- Relationsmenge gegen Befund 2081,
- alle drei Tragungsachsen gegen Befund 2081,
- Pareto-Tiefe gegen Befund 2081,
- unveränderte Nachbarschaftsquelldaten,
- unveränderte Präfixe früherer Reifungsstände.

Nach dem Lauf wird die vollständig rekonstruierte Historie zusätzlich gegen
alle 10.476 unkomprimierten Einträge aus Befund 2082 verglichen.

## Äquivalenz

| Folge | Checkpoints | Relationsabweichungen | Achsenabweichungen | Tiefenabweichungen | Quellen unverändert |
|---|---:|---:|---:|---:|---:|
| vorwärts | 5 | 0 | 0 | 0 | ja |
| rückwärts | 5 | 0 | 0 | 0 | ja |

Beide rekonstruierten Historien sind zeilenweise identisch zu Befund 2082:

| Folge | Einträge | SHA-256 | exakt |
|---|---:|---|---:|
| vorwärts | 5.311 | `91379512053a83f096469c870b9dcb7e00189bf4ccf538d7c2ab1bc8c81b892d` | ja |
| rückwärts | 5.165 | `9c19d7224e76edfa7f504615f794a6fe7c0bf70dc5ca859fc947cfffd0e531fe` | ja |

Alle früheren Historien bleiben bei jedem Übergang als unveränderter Präfix
erhalten. Die kompakte Darstellung trägt damit denselben beobachteten
Reifungsverlauf wie die Vollhistorie.

## Speicherwirkung

| Folge | Basis 2081 | Vollhistorie 2082 | Deltaformat 2083 | Ersparnis zu 2082 |
|---|---:|---:|---:|---:|
| vorwärts | 12.057.026 Byte | 16.009.722 Byte | 13.133.069 Byte | 2.876.653 Byte / 17,97 % |
| rückwärts | 12.119.957 Byte | 16.040.293 Byte | 13.189.448 Byte | 2.850.845 Byte / 17,77 % |

Gegenüber der konsolidierungsfreien Basis verbleiben 8,92 beziehungsweise
8,82 Prozent Mehrbedarf. Vom in 2082 beobachteten Konsolidierungsmehrbedarf
werden 72,78 beziehungsweise 72,72 Prozent entfernt.

Der reine kompakte Konsolidierungszweig umfasst am Endpunkt 921.539 Byte
vorwärts und 917.210 Byte rückwärts.

## Befund

Getragen sind:

- vollständige Reifungshistorie ohne Vollstandwiederholung,
- exakte Rekonstruktion jedes gespeicherten Wertes,
- verlustfreie Migration der 2082-Vollhistorie,
- unveränderte spätere Feld- und Nachbarschaftsentwicklung,
- deutliche Speicherentlastung ohne inhaltliche Schwelle.

Nicht getragen sind:

- semantische Verdichtung verschiedener Beziehungen,
- organisches Vergessen oder Dämpfen,
- Rückwirkung der Reifungsbahn auf das MCM-Feld,
- aktive Ressourcenverteilung,
- Bedeutung oder Handlungsentscheidung.

Das Deltaformat ist damit eine tragfähigere Gedächtnisform, aber noch keine
Feldintelligenz. Es bewahrt Erfahrung wirtschaftlicher, ohne aus ihr bereits
eine Wirkung zu programmieren.

## Reproduzierbare Ausgaben

- `2083_EXAKTE_DELTA_KONSOLIDIERUNG_MCM_NACHBARSCHAFT.checkpoints.csv`
- `2083_EXAKTE_DELTA_KONSOLIDIERUNG_MCM_NACHBARSCHAFT.equivalence.csv`
- `2083_EXAKTE_DELTA_KONSOLIDIERUNG_MCM_NACHBARSCHAFT.continuity.csv`
- `2083_EXAKTE_DELTA_KONSOLIDIERUNG_MCM_NACHBARSCHAFT.order.csv`
- `2083_EXAKTE_DELTA_KONSOLIDIERUNG_MCM_NACHBARSCHAFT.reconstruction.csv`
- `2083_EXAKTE_DELTA_KONSOLIDIERUNG_MCM_NACHBARSCHAFT.summary.csv`

Die bereits vorhandene 2082-Historientabelle dient als vollständige
Rekonstruktionsreferenz und wird nicht dupliziert. Extrahierte Welten,
Debugdaten und vollständige Runtime-Memories bleiben lokal und werden nach der
Prüfung entfernt.
