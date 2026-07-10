# 2084 - MCM-Reifungsbahn-Nachbarschaften

## Zweck

Befund 2083 bewahrt die Reifungsbahn jeder passiven MCM-Nachbarschaft als
exakte Deltafolge. Diese Prüfung untersucht, ob Beziehungen mit ähnlicher
Reifungsbewegung selbst wiederkehrende Nachbarschaften bilden.

Untersucht wird ausschließlich die innere Entwicklung aus Pareto-Tiefe,
Weltpaartragung, Weltbreite und erneuter Bestätigung. Es werden keine
Chartmerkmale, Außenweltklassen oder Handlungswerte gelesen.

## Schwellenfreie Prüfanordnung

Eine Bewegung benötigt strukturell mindestens zwei beobachtete Checkpoints.
Dadurch besitzen 1.591 vorwärts und 1.541 rückwärts gewachsene Beziehungen eine
prüfbare Bahn; 1.117 Relationsidentitäten kommen in beiden Mengen vor.

Bahnen werden nur innerhalb derselben exakten Checkpointfolge verglichen. Es
gibt keine Interpolation fehlender Erfahrung. Drei innere Profilräume bleiben
getrennt:

1. Bewegung der relativen Pareto-Tiefe,
2. Bewegung der drei relativen Tragungsachsen,
3. gemeinsame Bewegung aller vier Achsen.

Ränge werden pro Checkpoint unter Erhaltung aller Gleichstände gebildet. Eine
Beziehung wird nur dann Nachbar einer anderen, wenn beide Verläufe gegenseitig
nächste Profile sind. Es gibt kein festes `k`, keine Distanzschwelle und keine
vorgegebene Familie. Als robust gelten diagnostisch nur Kanten, die in allen
drei Profilräumen auftreten.

## Sättigung Durch Exakte Gleichstände

| Punkte | vorwärts: Relationen / Fingerabdrücke / größte Klasse | rückwärts: Relationen / Fingerabdrücke / größte Klasse |
|---:|---:|---:|
| 2 | 639 / 92 / 344 | 613 / 99 / 350 |
| 3 | 470 / 197 / 145 | 507 / 206 / 194 |
| 4 | 242 / 190 / 26 | 231 / 186 / 24 |
| 5 | 240 / 214 / 11 | 190 / 177 / 7 |

Kurze Bahnen sind stark quantisiert. Bei zwei Punkten liegen 53,8
beziehungsweise 57,1 Prozent aller Beziehungen in jeweils einer einzigen
exakten Deltaklasse. Mit längerer Beobachtung werden die Verläufe deutlich
individueller.

Diese Gleichstände wirken direkt auf den schwellenfreien Nachbarschaftsgraphen:

| Folge | robuste Kanten | davon Distanz null | Anteil Distanz null |
|---|---:|---:|---:|
| vorwärts | 45.491 | 45.441 | 99,89 % |
| rückwärts | 48.442 | 48.399 | 99,91 % |

Der Graph ist damit fast vollständig eine Darstellung exakter Gleichstände,
nicht eine fein aufgelöste Geometrie verschiedener Reifungsbahnen.

## Reihenfolgenvergleich Und Nullkontrolle

| Raum | gemeinsame Kanten | Jaccard | Nullmittel | Faktor zur Null |
|---|---:|---:|---:|---:|
| exakte Rohdeltas | 10.283 | 0,069 | 5.259,4 | 1,96 |
| Tiefenbewegung | 7.712 | 0,089 | 1.554,2 | 4,96 |
| Tragungsbewegung | 7.708 | 0,089 | 1.547,2 | 4,98 |
| volle Bewegung | 7.709 | 0,089 | 1.546,2 | 4,99 |
| robust in allen Räumen | 7.707 | 0,089 | 1.540,3 | 5,00 |

Die Nullkontrolle vertauscht Relationsidentitäten 200-mal nur innerhalb
derselben rückwärtigen Checkpointsignatur. Bahnlänge, Klassengröße und
Graphdichte bleiben erhalten. In keiner Permutation erreicht die Null den
beobachteten Überlapp; das empirische `p` beträgt in allen fünf Lesarten
`1/201 = 0,004975`.

Es existiert somit ein überzufälliger gemeinsamer Strukturrest. Sein absoluter
Jaccard bleibt mit 0,089 jedoch niedrig.

## Längenabhängige Grenze

| Punkte in beiden Folgen | vergleichbare Relationen | gemeinsame robuste Kanten | Jaccard | Faktor zur Null |
|---:|---:|---:|---:|---:|
| 2 | 204 | 5.418 | 0,823 | 4,88 |
| 3 | 70 | 0 | 0,000 | 0,00 |
| 4 | 32 | 0 | 0,000 | 0,00 |
| 5 | 72 | 0 | 0,000 | 0,00 |

Der gesamte tragende Effekt konzentriert sich auf die groben
Ein-Intervall-Bahnen. Sobald mindestens zwei Bewegungsintervalle vorliegen,
bleibt kein gemeinsames robustes Nachbarschaftspaar erhalten.

Auch relationsbezogen entsteht keine stabile Bewegungsidentität: 378
Beziehungen besitzen in beiden Folgen dieselbe Checkpointsignatur, darunter 72
vollständige Fünfpunktbahnen. Keine dieser 378 Beziehungen trägt in beiden
Erfahrungsrichtungen denselben exakten Rohdeltafingerabdruck.

## Befund

Getragen sind:

- überzufällige gemeinsame Kurzzeitbewegung innerhalb grober Zweipunktbahnen,
- zunehmende Individualisierung mit längerer Erfahrung,
- schwellenfreie Sichtbarkeit exakter Gleichstände,
- eine klare Trennung zwischen statistischem Überschuss und tragfähiger
  Langzeitidentität.

Nicht getragen sind:

- reihenfolgenstabile Reifungsfamilien,
- stabile Nachbarschaften vollständiger Fünfpunktbahnen,
- ein belastbarer Bewegungsgraph für die Runtime-Memory,
- Feldrückwirkung, Bedeutung oder Handlung aus Reifungsähnlichkeit.

Die Reifungsbahn ist als individuelle zeitliche Memory weiterhin fundiert.
Ihre derzeit fünf groben Checkpoints tragen jedoch keine organische zweite
Topologie aus Reifungsfamilien. Eine Integration würde die große
Zweipunkt-Gleichstandswolke festschreiben und damit mehr Struktur programmieren,
als die längere Erfahrung bestätigt.

## Reproduzierbare Ausgaben

- `2084_MCM_REIFUNGSBAHN_NACHBARSCHAFTEN.coverage.csv`
- `2084_MCM_REIFUNGSBAHN_NACHBARSCHAFTEN.identity.csv`
- `2084_MCM_REIFUNGSBAHN_NACHBARSCHAFTEN.graphs.csv`
- `2084_MCM_REIFUNGSBAHN_NACHBARSCHAFTEN.order.csv`
- `2084_MCM_REIFUNGSBAHN_NACHBARSCHAFTEN.null.csv`
- `2084_MCM_REIFUNGSBAHN_NACHBARSCHAFTEN.longevity.csv`
- `2084_MCM_REIFUNGSBAHN_NACHBARSCHAFTEN.summary.csv`

Die Auswertung arbeitet offline auf der bereits vorhandenen 2082-Historie.
Sie erzeugt keine neuen Welt-, Debug- oder Runtime-Memory-Dateien und wird von
MINI_DIO nicht gelesen.
