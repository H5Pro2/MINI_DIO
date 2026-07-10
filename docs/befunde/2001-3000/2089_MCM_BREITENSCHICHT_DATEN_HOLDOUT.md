# 2089 - Daten-Holdout der MCM-Breitenschicht

## Zweck

Befund 2088 bestätigte die alterskontinuierliche Breitenschicht in einer
dritten Reihenfolge desselben 81-Welten-Bestands. Ein großer Teil des früheren
19er-Verbunds lag erneut gemeinsam, jedoch als Teil einer größeren
70er-Komponente.

Diese Prüfung verlässt erstmals den verwendeten Weltbestand. Sie fragt, ob die
alten Relationsidentitäten auch in neuen realen Erfahrungswelten gemeinsam
reifen oder ob nur die Fähigkeit des Felds zur Gruppenbildung erhalten bleibt.

## Unabhängiger Erfahrungsblock

Der Holdout verwendet vier bereits im Repository vorhandene, aber in der
Eigenzeitkette 2085 bis 2088 nicht verwendete Rohquellen:

- BTC 2024, `30m`,
- SOL 2024, `30m`,
- BTC 2025, `30m`,
- SOL 2025, `30m`.

Aus jeder Quelle werden 16 direkt aufeinanderfolgende, nicht überlappende
Fenster mit je 1.000 Beobachtungen gebildet. Alle 64 Welten sind real. Es gibt
in diesem Lauf keine Shuffle-, Random-Sign- oder andere synthetische Welt.

Die Reihenfolge wird vor dem Lauf durch SHA-256 aus festem Holdout-Schlüssel,
Quelldatei und Fensterstart bestimmt. Quelldatei und Quellhash sind für jede
Welt in der Ordnungsdatei festgehalten.

Die 2025er Quellen führen den Rohzeitstempel in einer anderen Einheit als die
2024er Quellen. MINI_DIO reicht diesen Wert nur als Ausgabemetadatum weiter;
Feldzustand, Episodendauer und Relationsereigniszeit entstehen aus der
Schrittfolge. Die Einheit ist deshalb keine Achse dieser Prüfung.

## Blinde Auswertung

Eine frische Memory durchläuft die 64 Welten einmal. Danach werden aus den
eigenen Ereignissen jeder Beziehung die persistenten Nachbarschaften bei
Relationsalter 3, 5 und 10 gebildet.

Die Komponenten aus 2087 und 2088 werden erst eingelesen, nachdem:

1. alle neuen Welten abgeschlossen sind,
2. Ereigniszahl und Endzustand jeder Beziehung geprüft sind,
3. Eigenzeittakt, Breitenzuwachs und Profilzuwachs getrennt ausgewertet sind,
4. alle neuen Komponenten feststehen.

Die alten Relationsidentitäten können die neue Komponentenbildung damit nicht
steuern.

## Ereignis- und Feldgrenze

| Merkmal | Wert |
|---|---:|
| reale Welten | 64 |
| synthetische Welten | 0 |
| Endrelationen | 2.580 |
| Relationsereignisse | 10.092 |
| Relationen mit mindestens zwei Ereignissen | 1.204 |
| Relationen ab Alter 10 | 265 |
| Ereignisintegrität exakt | ja |
| von MINI_DIO gelesen | nein |
| Feld beeinflusst | nein |
| Handlung beeinflusst | nein |

Die neue Endrelationsmenge unterscheidet sich deutlich vom alten Weltbestand.
Ihr Jaccard liegt zur früheren Vorwärtsfolge bei 0,2174, zur Rückwärtsfolge bei
0,2158 und zur 2088-Reihenfolge bei 0,2182. Der Daten-Holdout ist damit keine
weitere kleine Variation derselben Relationstopologie.

Kein einzelnes Außenmerkmal wird als Zielgröße oder Referenz gespeichert. Die
Chartwelt liefert weiterhin nur Erfahrung an das bestehende MCM-Feld.

## Blind entstandene Komponenten

| Teilraum | Komponenten | größte Komponente | Kanten der größten Komponente |
|---|---:|---:|---:|
| Eigenzeittakt | 2 | 3 | 3 |
| Breitenzuwachs | 9 | 43 | 903 |
| Profilzuwachs | 5 | 13 | 78 |

Die jeweils größte Komponente ist vollständig verbunden. Auch im neuen
Weltbestand organisiert sich ein Teil der Beziehungen somit zu einer
alterskontinuierlichen Breitenschicht. Daraus folgt allein noch keine stabile
Mitgliedschaft oder Semantik.

## Nachgelagerter Identitätsabgleich

Die Nullkontrolle zieht je Referenz 1.000 gleich große Zufallsmengen aus den
265 im neuen Feld bis Alter 10 gereiften Beziehungen. Verglichen werden nur
die alten Relationen, die dieses Alter im Holdout tatsächlich erreichen.

### Geschlossener 2087-Breitenverbund

Von den 19 Relationen erreichen 6 das Alter 10. Zwischen ihnen bleiben 3 von
15 möglichen Kanten erhalten. Gleich große Zufallsmengen besitzen im Mittel
0,407 und höchstens 6 Kanten. Der beobachtete Wert erreicht
`p = 70/1001 = 0,0699`.

Drei der sechs Relationen liegen gemeinsam in der blind entstandenen
43er-Komponente. Auch dieser Überlapp erreicht `p = 0,0699`. Die Spur liegt
über dem Nullmittel, unterschreitet die vorab verwendete 0,05-Grenze aber
nicht.

### Blinde 2088-Breitenkomponente

Von den 70 Relationen erreichen 17 das Alter 10. Zwischen ihnen bleiben 10 von
136 möglichen Kanten erhalten. Die Nullkontrolle besitzt im Mittel 3,512 und
höchstens 28 Kanten; der beobachtete Wert liegt bei `p = 116/1001 = 0,1159`.

Fünf der 17 Relationen liegen gemeinsam in der neuen 43er-Komponente. Zufällige
17er-Mengen treffen dort im Mittel 2,784 Relationen; auch der beobachtete
Überlapp bleibt mit `p = 0,1159` ungesichert.

## Befund

Getragen sind:

- erneute blinde Bildung einer alterskontinuierlichen Breitenschicht,
- eine deutliche Änderung der gesamten Relationstopologie durch neue
  Erfahrungswelten,
- eine schwache Restspur des kleinen 2087-Verbunds,
- passive und verlustfrei rekonstruierbare Relationsereigniszeit.

Nicht getragen sind:

- unabhängige Reproduktion der 19 alten Relationsidentitäten,
- unabhängige Reproduktion der 70 Relationen aus Befund 2088,
- feste Mitglieder oder ein gespeicherter semantischer Kern,
- eine Übertragung des früheren Profilverbunds,
- Feld-, Wahrnehmungs- oder Handlungsrückwirkung.

Die bisherige Breitenschicht ist damit keine feste innere Objektklasse. Das
Feld bildet unter neuer Erfahrung erneut Zusammenhang, besetzt ihn aber mit
anderen Beziehungen. Für eine organische Topologie ist deshalb die Entstehung,
Umbildung und Lebensdauer solcher Nachbarschaften bedeutsamer als das
Festschreiben ihrer bisherigen Mitglieder.

## Reproduzierbare Ausgaben

- `2089_MCM_BREITENSCHICHT_DATEN_HOLDOUT.order.csv`
- `2089_MCM_BREITENSCHICHT_DATEN_HOLDOUT.equivalence.csv`
- `2089_MCM_BREITENSCHICHT_DATEN_HOLDOUT.discovery.csv`
- `2089_MCM_BREITENSCHICHT_DATEN_HOLDOUT.reference.csv`
- `2089_MCM_BREITENSCHICHT_DATEN_HOLDOUT.summary.csv`
- `data/2089_mcm_breadth_data_holdout_events.zip`

Das ZIP enthält nur Ereignishistorien und Quellenordnung. Die 64 Fenster
werden reproduzierbar aus den bereits versionierten Rohquellen erzeugt. Ihre
extrahierten Dateien, alle Debugdaten und die Laufzeit-Memory werden nach dem
Versuch entfernt.
