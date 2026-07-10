# 2087 - MCM-Eigenzeit-Kantenpersistenz

## Zweck

Befund 2086 fand getrennte, überzufällige Bewegungsnachbarschaften in
Eigenzeittakt, Breitenzuwachs und Profilzuwachs. Die Paare waren jedoch nicht
gleichzeitig über alle Achsen Nachbarn.

Diese Prüfung untersucht deshalb nicht erneut die Kantenmenge einer einzelnen
Altersstufe. Sie fragt, ob dieselben achsenspezifischen Relationspaare vom
Eigenalter 3 über Alter 5 bis Alter 10 erhalten bleiben.

Die Auswertung liest ausschließlich das Ereignisarchiv aus Befund 2085. Sie
verändert weder Memory noch Feld.

## Persistenzprüfung

Für jede Erfahrungsrichtung und jeden der drei Teilräume werden die
schwellenfreien gegenseitigen Nachbarschaften aus Befund 2086 erneut gebildet.
Bei einem Altersübergang werden nur Relationen betrachtet, die das spätere
Alter tatsächlich erreicht haben.

Die Nullkontrolle permutiert die Relationsidentitäten 200-mal innerhalb dieser
späteren Altersmenge. Kantenmenge, Graphdichte und Altersabdeckung bleiben
erhalten. Es werden keine fehlenden Ereignisse ergänzt.

## Übergänge Innerhalb Einer Erfahrungsfolge

Alle drei Teilräume besitzen deutlich mehr persistente Kanten als ihre
altersmengenerhaltende Nullkontrolle.

### Vorwärts

| Raum | Übergang | persistente Kanten | Anteil älterer Kanten | Nullmittel | Faktor zur Null |
|---|---:|---:|---:|---:|---:|
| Eigenzeittakt | 3 -> 5 | 175 | 0,0825 | 3,050 | 57,38 |
| Eigenzeittakt | 5 -> 10 | 11 | 0,0643 | 0,320 | 34,38 |
| Breitenzuwachs | 3 -> 5 | 25.230 | 0,4857 | 7.261,790 | 3,47 |
| Breitenzuwachs | 5 -> 10 | 1.850 | 0,2886 | 216,820 | 8,53 |
| Profilzuwachs | 3 -> 5 | 2.897 | 0,3194 | 148,260 | 19,54 |
| Profilzuwachs | 5 -> 10 | 219 | 0,2281 | 4,260 | 51,41 |

### Rückwärts

| Raum | Übergang | persistente Kanten | Anteil älterer Kanten | Nullmittel | Faktor zur Null |
|---|---:|---:|---:|---:|---:|
| Eigenzeittakt | 3 -> 5 | 128 | 0,0801 | 2,430 | 52,67 |
| Eigenzeittakt | 5 -> 10 | 10 | 0,0637 | 0,210 | 47,62 |
| Breitenzuwachs | 3 -> 5 | 23.272 | 0,4386 | 7.516,945 | 3,10 |
| Breitenzuwachs | 5 -> 10 | 1.730 | 0,3227 | 176,600 | 9,80 |
| Profilzuwachs | 3 -> 5 | 1.730 | 0,2470 | 76,330 | 22,66 |
| Profilzuwachs | 5 -> 10 | 89 | 0,1902 | 1,015 | 87,68 |

Jeder Einzelübergang liegt in keiner der 200 Permutationen auf oder über dem
beobachteten Wert; das empirische `p` beträgt jeweils `1/201 = 0,004975`.

## Durchgehende Persistenz Von Alter 3 Bis 10

| Folge | Raum | Kanten in allen drei Altern | beteiligte Relationen | Nullmittel | Faktor zur Null |
|---|---|---:|---:|---:|---:|
| vorwärts | Eigenzeittakt | 9 | 18 | 0,010 | 900,00 |
| vorwärts | Breitenzuwachs | 1.848 | 94 | 52,340 | 35,31 |
| vorwärts | Profilzuwachs | 217 | 35 | 0,165 | 1.315,15 |
| rückwärts | Eigenzeittakt | 9 | 10 | 0,015 | 600,00 |
| rückwärts | Breitenzuwachs | 1.728 | 93 | 45,655 | 37,85 |
| rückwärts | Profilzuwachs | 86 | 26 | 0,035 | 2.457,14 |

Innerhalb jeder Erfahrungsfolge existiert damit eine klare alterskontinuierliche
Teilstruktur. Sie ist nicht nur ein momentaner Graph einer einzelnen
Relationsreife.

## Reihenfolgenübergreifender Persistenzkern

Die entscheidende strengere Prüfung verlangt, dass eine Kante:

1. vorwärts bei Alter 3, 5 und 10 besteht,
2. rückwärts bei Alter 3, 5 und 10 besteht,
3. in beiden Erfahrungsrichtungen dieselben Relationsidentitäten verbindet.

| Raum | vorwärts persistent | rückwärts persistent | gemeinsam persistent | Relationen | Jaccard | Nullmittel | Faktor | empirisches p |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Eigenzeittakt | 9 | 9 | 1 | 2 | 0,0588 | 0,195 | 5,13 | 0,1990 |
| Breitenzuwachs | 1.848 | 1.728 | 171 | 19 | 0,0502 | 108,570 | 1,58 | 0,0398 |
| Profilzuwachs | 217 | 86 | 6 | 4 | 0,0202 | 1,610 | 3,73 | 0,0498 |

Der Eigenzeittakt trägt reihenfolgenübergreifend nicht belastbar. Breiten- und
Profilzuwachs liegen nur schwach über ihrer strengeren Identitätsnull.

Die 171 Breitenkanten bilden einen vollständigen Verbund aus 19 Relationen. Die
6 Profilkanten bilden einen vollständigen Viererverbund. Alle vier
Profilrelationen sind Teil des 19er-Breitenverbunds. Der Taktverbund aus zwei
Relationen ist davon vollständig getrennt.

Keine Relation dieser drei Komponenten gehört zu den 26 strengen
Nachbarschaftsrelationen aus Befund 2078. Diese Markierung erfolgte erst nach
der Komponentenbildung und war kein Auswahlkriterium.

## Befund

Getragen sind:

- starke Alterskontinuität achsenspezifischer Kanten innerhalb beider
  Erfahrungsfolgen,
- ein kleiner reihenfolgenübergreifender Breitenverbund,
- ein darin liegender reihenfolgenübergreifender Profilverbund,
- eine mehrschichtige Ordnung, in der Profilähnlichkeit in einem breiteren
  Tragungszusammenhang liegen kann.

Nicht getragen sind:

- ein reihenfolgenstabiler Eigenzeittaktverbund,
- eine Verbindung des neuen Persistenzkerns mit dem strengen 2078-Kern,
- eine bereits breit abgesicherte Multiplex-Topologie,
- bevorzugte Runtime-Knoten oder fest codierte Komponenten,
- Feld- oder Handlungsrückwirkung.

2087 zeigt erstmals einen kleinen, über Relationsalter und Erfahrungsrichtung
erhaltenen Multiplex-Kandidaten. Seine reihenfolgenübergreifende Absicherung ist
mit 19 beziehungsweise 4 Relationen und empirischen Werten nahe 0,05 noch zu
schmal für eine Integration. Die Komponenten bleiben nachgelagerter
Forschungsbefund und werden nicht als Konstanten in MINI_DIO geschrieben.

## Reproduzierbare Ausgaben

- `2087_MCM_EIGENZEIT_KANTENPERSISTENZ.transitions.csv`
- `2087_MCM_EIGENZEIT_KANTENPERSISTENZ.persistence.csv`
- `2087_MCM_EIGENZEIT_KANTENPERSISTENZ.order.csv`
- `2087_MCM_EIGENZEIT_KANTENPERSISTENZ.components.csv`
- `2087_MCM_EIGENZEIT_KANTENPERSISTENZ.overlap.csv`
- `2087_MCM_EIGENZEIT_KANTENPERSISTENZ.summary.csv`

Es werden keine Welt-, Debug-, Kantenlisten- oder Runtime-Memory-Dateien
erzeugt.
