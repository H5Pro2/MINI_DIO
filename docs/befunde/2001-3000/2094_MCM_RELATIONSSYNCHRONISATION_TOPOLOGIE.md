# 2094 - Topologie der MCM-Relationssynchronisation

## Zweck

Befund 2093 zeigte, dass eine mögliche Kantenfortsetzung nur dann fair geprüft
werden kann, wenn beide Relationen das nächste Eigenalter gleichzeitig
besitzen. Die bisher behauptete Eigenstabilität der Lebenslaufkanten trug unter
dieser Korrektur nicht über unabhängige Bestände.

2094 untersucht deshalb nicht erneut `getragen` gegen `neu`. Geprüft wird die
darunterliegende innere Zeitordnung selbst: Bilden Relationen, die dasselbe
Eigenalter gleichzeitig besitzen, eine wiederkehrende Synchronisationstopologie
oder entsteht deren Zusammenhang allein aus Paarzahl, Graphform und beliebiger
Reihenfolge ihrer eigenen Ereignisabstände?

Außenwerte, Chartmuster, Quellenentwicklung und Handlungsergebnisse sind keine
Zielgrößen.

## Exakte Synchronisationskante

Relation `r` besitzt Eigenalter `a` ab der Finalisierung ihres Ereignisses `a`
bis unmittelbar vor ihrem Ereignis `a + 1`. Zwei Relationen bilden bei Alter
`a` eine Synchronisationskante, wenn sich diese beiden Intervalle mindestens
bei einer Finalisierung überschneiden.

Berühren sich das Ende des einen und der Beginn des anderen Intervalls nur an
derselben Grenze, besteht keine Gleichzeitigkeit: Nach der Finalisierung hat
die erste Relation ihr altes Alter bereits verlassen.

Diese Definition benötigt keine Distanz-, Dauer-, Alters- oder
Persistenzschwelle.

## Bestände und Rekonstruktion

| Merkmal | 2091-Bestand | 2092-Holdout |
|---|---:|---:|
| reale Welten | 64 | 60 |
| Relationen mit Ereigniszeit | 2.580 | 1.932 |
| beobachtete Altersschichten | 61 | 50 |
| Synchronisationspaar-Alter | 414.706 | 332.387 |
| Lebenslaufpaar-Alter | 212.466 | 159.199 |
| Lebenslaufanteil an Synchronisation | 51,23 % | 47,90 % |

Alle 371.665 gespeicherten Lebenslaufbeobachtungen beider Bestände liegen
innerhalb einer exakten Synchronisationskante. Es existiert keine
Lebenslaufkante ohne gleichzeitiges Relationsalter.

Der Synchronisationsgraph wird nicht zusätzlich gespeichert. Er lässt sich
vollständig aus den bereits passiv bewahrten Relationsereignissen und ihren
Finalisierungsindizes rekonstruieren.

## Null der relationseigenen Abstandsreihenfolge

Für jede Relation bleiben erhalten:

- ihre erste und letzte Ereignisfinalisierung,
- ihre Ereigniszahl,
- die vollständige Multimenge ihrer Abstände zwischen Ereignissen.

Nur die Reihenfolge dieser eigenen Abstände wird 500-mal permutiert. Die Null
verändert damit weder Geburtszeit, Lebensspanne noch individuelle
Ereignisabstände, löst aber deren Zuordnung zu den aufeinanderfolgenden
Eigenaltern.

| Bestand | beobachtet | Nullmittel | Null-Standardabweichung | Nullmaximum | empirisches `p` |
|---|---:|---:|---:|---:|---:|
| 2091 | 414.706 | 409.781,74 | 2.442,00 | 416.577 | 0,01597 |
| 2092 | 332.387 | 327.699,79 | 2.375,11 | 334.495 | 0,02395 |

Die wirkliche Abstandsreihenfolge erzeugt in beiden Beständen etwas mehr
gleichzeitige Paar-Alter als die relationseigene Rhythmusnull. Der Abstand ist
klein und einzelne Nullziehungen liegen höher; getragen ist eine schwache
Ordnungswirkung, keine starre Taktung.

## Graphformerhaltende Identitätsnull

Für jeden Übergang von Alter `a` zu `a + 1` werden nur Relationen betrachtet,
die in beiden Schichten vorkommen. Aktueller und nächster
Synchronisationsgraph behalten:

- dieselben Relationsmengen,
- ihre vollständige Kantenzahl,
- ihre jeweilige Gradstruktur.

Nur die Relationsidentitäten des nächsten Graphen werden innerhalb derselben
überlebenden Relationsmenge permutiert. 200 Permutationen prüfen, ob konkrete
Paare häufiger wiederkehren, als die Graphformen allein erwarten lassen.

| Merkmal | 2091-Bestand | 2092-Holdout |
|---|---:|---:|
| auswertbare Altersübergänge | 50 | 48 |
| aktuelle Synchronisationspaare | 182.781 | 149.018 |
| identisch erhaltene Paare | 96.023 | 81.318 |
| Identitätserhaltungsrate | 52,53 % | 54,57 % |
| analytische Nullerwartung | 33.047,03 | 31.227,44 |
| beobachtet / erwartet | 2,9056 | 2,6041 |
| höchster Permutationswert | 34.944 | 33.071 |
| empirisches `p` | 1/201 = 0,004975 | 1/201 = 0,004975 |

In beiden Beständen bleibt konkrete Synchronisationsidentität deutlich über
der bloßen Graphform erhalten. Anders als der in 2093 verworfene
Fortsetzungsvorteil betrifft dieser Befund nicht die Auswahl einer
Lebenslaufkante, sondern die gemeinsame Eigenzeitanwesenheit selbst.

## Erhalt und Partnerwechsel

Trotz des überzufälligen Identitätserhalts wechseln beim nächsten
Relationsalter:

- im 2091-Bestand `47,47 %` der aktuellen Synchronisationspaare,
- im 2092-Holdout `45,43 %` der aktuellen Synchronisationspaare.

Der Rahmen ist damit weder zufällig neu noch dauerhaft fest. Etwa die Hälfte
der Paaridentitäten bleibt erhalten, während die andere Hälfte organisch
umbaut. Es entstehen keine vorgegebenen Gruppen oder unveränderlichen
Mitglieder.

## Befund

Getragen sind:

- eine vollständig aus Relationsereignissen rekonstruierbare
  Synchronisationstopologie,
- eine kleine Ordnungswirkung der wirklichen relationseigenen
  Ereignisabstandsfolge in beiden Beständen,
- ein starker, graphformübergreifender Erhalt konkreter
  Synchronisationsidentitäten,
- gleichzeitig ein Partnerwechsel von ungefähr 45 bis 48 Prozent pro
  Altersübergang,
- dieselbe qualitative Form im Entwicklungsbestand und unabhängigen Holdout.

Nicht getragen sind:

- eine feste Gruppe, Komponente oder Mitgliedsliste,
- eine globale Taktvorgabe oder feste Synchronisationsdauer,
- die in 2093 verworfene Eigenstabilität ausgewählter Lebenslaufkanten,
- eine semantische Bedeutung der synchronisierten Paare,
- eine Rücklesung in Feld, Wahrnehmung oder Handlung.

2094 zeigt einen stabilen, aber beweglichen Eigenzeitrahmen: Relationen finden
über ihre individuellen Ereignisfolgen wiederholt gleichzeitig in dasselbe
Alter, ohne ihre Partner vollständig festzuschreiben. Dieser Rahmen ist eine
innere topologische Eigenschaft des Feldverlaufs, aber noch keine Regel und
keine Feldintelligenz. An Runtime und Memory wird nichts geändert.

## Reproduzierbare Ausgaben

- `2094_MCM_RELATIONSSYNCHRONISATION_TOPOLOGIE.ages.csv`
- `2094_MCM_RELATIONSSYNCHRONISATION_TOPOLOGIE.transitions.csv`
- `2094_MCM_RELATIONSSYNCHRONISATION_TOPOLOGIE.null.csv`
- `2094_MCM_RELATIONSSYNCHRONISATION_TOPOLOGIE.summary.csv`

Die Auswertung liest ausschließlich die kompakten Archive aus 2089, 2090 und
2092. Sie erzeugt keine Welt-, Debug-, Memory- oder Runtime-Dateien und wird
von MINI_DIO nicht zurückgelesen.
