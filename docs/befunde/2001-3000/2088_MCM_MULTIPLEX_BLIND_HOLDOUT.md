# 2088 - Blinder Holdout des MCM-Multiplexkandidaten

## Zweck

Befund 2087 fand in zwei entgegengesetzten Erfahrungsfolgen einen über das
Relationsalter 3, 5 und 10 erhaltenen Breitenverbund aus 19 Relationen. Darin
lag ein Profilverbund aus 4 Relationen. Die statistische Absicherung beider
Komponenten war jedoch noch schmal.

Diese Prüfung fragt deshalb, ob die Struktur in einer dritten, vor der
Auswertung festgelegten Reihenfolge wieder erscheint. Sie ist ein
Reihenfolgen-Holdout desselben 81-Welten-Bestands, kein unabhängiger
Daten-Holdout.

## Blinde Reihenfolge und Auswertung

Die 81 Welten werden nach dem SHA-256-Wert aus festem Holdout-Schlüssel,
Archivname und internem Dateinamen sortiert. So steht die vollständige Folge
vor dem ersten Weltlauf fest und hängt von keinem Feldergebnis ab.

Eine frische Memory durchläuft diese Folge einmal. Danach werden für
Eigenzeittakt, Breitenzuwachs und Profilzuwachs getrennt die
Nachbarschaftskanten bei Relationsalter 3, 5 und 10 gebildet. Nur Kanten, die
in allen drei Altern bestehen, gehen in die Komponentenbildung ein.

Die Relationsidentitäten aus Befund 2087 werden erst gelesen, nachdem:

1. alle 81 Welten abgeschlossen sind,
2. die Ereignisintegrität geprüft ist,
3. alle drei persistenten Graphen gebildet sind,
4. deren Zusammenhangskomponenten feststehen.

Die bekannten Relationen können die Entdeckung damit nicht steuern.

## Ereignis- und Feldgrenze

Die Folge erzeugt 2.088 Beziehungen mit 12.089 eigenen Ereignissen. 1.207
Beziehungen besitzen mindestens zwei Ereignisse und 343 erreichen Alter 10.
Ereigniszahl und jeweiliger Endstand stimmen für jede Beziehung exakt mit der
passiven Nachbarschafts-Memory überein.

| Merkmal | Wert |
|---|---:|
| Welten | 81 |
| Endrelationen | 2.088 |
| Relationsereignisse | 12.089 |
| Relationen ab Alter 10 | 343 |
| Ereignisintegrität exakt | ja |
| von MINI_DIO gelesen | nein |
| Feld beeinflusst | nein |
| Handlung beeinflusst | nein |

Die Endrelationsmenge bleibt der früheren Felderfahrung sehr ähnlich. Mit der
Vorwärtsfolge aus Befund 2081 teilt sie 1.993 Relationen bei einem Jaccard von
0,9309, mit der Rückwärtsfolge 1.983 Relationen bei einem Jaccard von 0,9055.

## Blind entdeckte Komponenten

| Teilraum | Komponenten | größte Komponente | Kanten der größten Komponente |
|---|---:|---:|---:|
| Eigenzeittakt | 10 | 4 | 6 |
| Breitenzuwachs | 17 | 70 | 2.415 |
| Profilzuwachs | 12 | 20 | 190 |

Die jeweils größte Komponente ist vollständig verbunden. Diese Größen wurden
bestimmt, bevor die Komponenten aus Befund 2087 eingelesen wurden.

## Nachgelagerter Abgleich mit Befund 2087

Die Nullkontrolle zieht 1.000 gleich große zufällige Relationsmengen aus den
343 bei Alter 10 vorhandenen Beziehungen. Sie verändert weder den entdeckten
Graphen noch dessen Komponenten.

### Breitenzuwachs

Von den 19 früheren Relationen sind 16 im Holdout bei Alter 10 vorhanden. 66
der 171 möglichen alten Kanten bleiben über alle drei Altersstufen erhalten.
Zufällige 16er-Mengen besitzen im Mittel 5,0 solcher Kanten, höchstens 45. Der
beobachtete Wert liegt mit `p = 1/1001` klar darüber.

Die blinde 70er-Komponente enthält 12 der 19 früheren Relationen. Zufällige
19er-Mengen treffen im Mittel 3,915, höchstens 10 Relationen derselben
Komponente; auch dieser Überlapp liegt bei `p = 1/1001`.

Damit reproduziert sich kein geschlossener 19er-Kern. Getragen ist vielmehr
eine breitere persistente Bewegungsschicht, in der ein großer Teil des
früheren Verbunds erneut gemeinsam liegt.

### Profilzuwachs

Alle vier früheren Profilrelationen erreichen Alter 10, aber nur eine der sechs
alten Kanten bleibt erhalten. Zufällige Vierermengen besitzen im Mittel 0,014
solcher Kanten; der Teilrest liegt bei `p = 15/1001` darüber.

Die persistente Kante liegt in der blinden 20er-Komponente, die zwei der vier
früheren Relationen enthält. Der größte Relationsüberlapp liegt gegenüber
zufälligen Vierermengen bei `p = 21/1001`. Der vollständige Viererverbund und
seine Einbettung als geschlossene Unterkomponente erscheinen jedoch nicht
erneut. Ein nur nach Jaccard ausgewählter Kleinstverbund ist mit
`p = 236/1001` nicht auffällig.

## Befund

Getragen sind:

- eine reihenfolgenrobuste, alterskontinuierliche Breitenschicht,
- eine starke, blind entstandene Überlappung dieser Schicht mit dem
  2087-Breitenverbund,
- ein kleiner überzufälliger Profilrest,
- individuelle Relationsereigniszeit als passive Grundlage der Prüfung.

Nicht getragen sind:

- der 19er-Breitenverbund als geschlossene und feste Komponente,
- der vollständige verschachtelte 4er-Profilverbund,
- ein belastbarer Eigenzeittaktkern,
- fest codierte Relationsidentitäten oder bevorzugte Runtime-Knoten,
- Feld-, Wahrnehmungs- oder Handlungsrückwirkung.

2088 verschiebt den Befund nicht zum Außenchart. Untersucht wird weiterhin,
wie sich innere Beziehungen des MCM-Felds unter anderer Erfahrungsreihenfolge
organisieren. Die Evidenz trägt eine organisch entstehende Breitenschicht,
aber noch keine ausreichend bestimmte Multiplexstruktur für eine Integration.

## Reproduzierbare Ausgaben

- `2088_MCM_MULTIPLEX_BLIND_HOLDOUT.order.csv`
- `2088_MCM_MULTIPLEX_BLIND_HOLDOUT.equivalence.csv`
- `2088_MCM_MULTIPLEX_BLIND_HOLDOUT.discovery.csv`
- `2088_MCM_MULTIPLEX_BLIND_HOLDOUT.reference.csv`
- `2088_MCM_MULTIPLEX_BLIND_HOLDOUT.summary.csv`
- `data/2088_mcm_multiplex_holdout_events.zip`

Das ZIP enthält nur die kompakte Ereignistabelle und die Holdout-Reihenfolge.
Extrahierte Welten, Debug-Ausgaben und die Laufzeit-Memory bleiben lokal und
werden nach dem Lauf entfernt.
