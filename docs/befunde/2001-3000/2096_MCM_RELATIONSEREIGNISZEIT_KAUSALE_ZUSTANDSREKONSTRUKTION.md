# 2096 - Kausale Zustandsrekonstruktion aus MCM-Relationsereigniszeit

## Zweck

Nach Abschluss des Lebenslaufzweigs stellt sich die Frage, ob für weitere
Feldentwicklung eine neue Zustands-Memory benötigt wird. Eine solche Ebene
darf nicht vorab programmiert werden, wenn der vorhandene passive Speicher
dieselbe Information bereits trägt.

2096 prüft deshalb ausschließlich die relationale Ebene: Reicht der bis zu
jeder Welt tatsächlich beobachtete Präfix der Relationsereigniszeit aus, um

- die Bewegungsnachbarschaften des Relationslebenslaufs und
- die gleichzeitige Eigenalter-Synchronisation

kausal und exakt zu rekonstruieren?

Der Rekonstruktor kennt keine zukünftigen Ereignisse, keine Außenwerte und
keine vorgegebenen Zustandsklassen.

## Kausaler Vorwärtslauf

Für jede Weltfinalisierung werden nur die dort neu eingetroffenen
Relationsereignisse an den bisherigen Präfix angehängt. Daraus entstehen:

1. das aktuelle Eigenalter jeder bisher erschienenen Relation,
2. die Kohorten gleichzeitig gleichen Eigenalters,
3. deren vollständige Synchronisationspaare,
4. für tatsächlich veränderte Alterskohorten die gegenseitigen nächsten
   Breitenbewegungsnachbarschaften,
5. der kumulierte passive Relationslebenslauf.

Nach jeder Welt wird die Rekonstruktion mit genau den bei dieser
Finalisierung archivierten Lebenslaufbeobachtungen verglichen. Spätere
Ereignisse werden weder zum Vervollständigen noch zum Bewerten verwendet.

Der Zustandsfingerabdruck ist keine neue Signaturklasse. Er ist nur ein
kanonischer SHA-256-Prüfwert über den bis dahin tatsächlich beobachteten
Ereignispräfix einschließlich Relationsidentität, Ereignisindex und aller
gespeicherten Ereignisfelder.

## Präfixintegrität

| Merkmal | 2091-Bestand | 2092-Holdout |
|---|---:|---:|
| reale Weltpräfixe | 64 | 60 |
| Relationsereignisse | 10.092 | 7.807 |
| Relationen | 2.580 | 1.932 |
| exakt rekonstruierte Lebenslaufpräfixe | 64/64 | 60/60 |
| kausale Lebenslaufbeobachtungen | 212.466 | 159.199 |
| archivierte Lebenslaufbeobachtungen | 212.466 | 159.199 |
| kausale Synchronisationspaar-Alter | 414.706 | 332.387 |
| offline rekonstruierte Synchronisationspaar-Alter | 414.706 | 332.387 |
| Zukunftszugriffe | 0 | 0 |

Die Ereignisindizes jeder Relation sind lückenlos. Bei jeder einzelnen
Finalisierung stimmen neue und kumulierte Lebenslaufbeobachtungen exakt mit
dem Archiv überein. Auch die ausschließlich vorwärts gebildete Vereinigung
aller Synchronisationspaar-Alter ist mengenidentisch zur nachgelagerten
Intervallrekonstruktion aus 2094.

## Zustandsindividualität

| Merkmal | 2091-Bestand | 2092-Holdout |
|---|---:|---:|
| unterschiedliche Ereignispräfix-Fingerabdrücke | 64 | 60 |
| Welten ohne Präfixänderung gegenüber der Vorwelt | 0 | 0 |

Jede Welt hinterlässt damit einen eigenen relationalen Ereigniszustand. Es
gibt in diesen Beständen keine exakt wiederholte vollständige Präfixidentität.
Eine feste Benennung oder Klassifizierung solcher Gesamtzustände würde daher
Ähnlichkeit von außen festlegen, statt sie aus dem Feld entstehen zu lassen.

## Minimalitätsbefund

Getragen sind:

- kausale Rekonstruktion aller 124 Weltpräfixe ohne Zukunftszugriff,
- exakte Ableitung des passiven Lebenslaufs aus der vorhandenen
  Relationsereigniszeit,
- exakte Ableitung der Synchronisationstopologie aus derselben Quelle,
- ein individueller relationaler Ereigniszustand nach jeder Welt,
- die Relationsereigniszeit als hinreichende Quelle für diese beiden
  nachgelagerten passiven Ebenen.

Nicht getragen sind:

- die Notwendigkeit einer zusätzlichen Feldzustands-Memory für Lebenslauf und
  Synchronisation,
- wiederkehrende exakte Gesamtzustandsklassen,
- eine bereits gefundene organische Nachbarschaft zwischen Weltzuständen,
- eine vollständige Beschreibung des gesamten MCM-Feldes,
- eine Rücklesung in Wahrnehmung, Feld oder Handlung.

2096 verhindert eine redundante Programmierung. Der relationale
Ereignispräfix ist innerhalb des geprüften Umfangs der bereits vorhandene,
kausal hinreichende Quellzustand; Lebenslauf und Synchronisation sind daraus
ableitbare Ansichten, keine eigenständigen lernenden Zustände. An Runtime und
Memory wird nichts geändert.

## Reproduzierbare Ausgaben

- `2096_MCM_RELATIONSEREIGNISZEIT_KAUSALE_ZUSTANDSREKONSTRUKTION.snapshots.csv`
- `2096_MCM_RELATIONSEREIGNISZEIT_KAUSALE_ZUSTANDSREKONSTRUKTION.integrity.csv`
- `2096_MCM_RELATIONSEREIGNISZEIT_KAUSALE_ZUSTANDSREKONSTRUKTION.summary.csv`

Die Auswertung liest ausschließlich die kompakten Archive aus 2089, 2090 und
2092. Sie erzeugt keine Welt-, Debug-, Memory- oder Runtime-Dateien.
