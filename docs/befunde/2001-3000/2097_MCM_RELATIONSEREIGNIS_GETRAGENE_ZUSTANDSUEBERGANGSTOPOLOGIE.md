# 2097 - Relationsereignis-getragene MCM-Zustandsübergangstopologie

## Zweck

Befund 2096 zeigte, dass jeder Weltpräfix einen individuellen relationalen
Ereigniszustand besitzt und dass keine zusätzliche Zustands-Memory nötig ist.
Exakte Gesamtzustände wiederholen sich nicht. Eine organische Verbindung darf
deshalb nicht über vorgegebene Zustandsklassen oder Vektordistanzen erzwungen
werden.

2097 bildet Verbindungen ausschließlich aus tatsächlich fortgesetzter
Relationserfahrung: Wenn dieselbe Relation bei zwei späteren Weltpräfixen
aufeinanderfolgende Eigenzeitereignisse besitzt, verbindet sie diese beiden
Präfixänderungen gerichtet miteinander.

Die Weltpräfixe dienen nur als innere Ereignispositionen. Chartwerte,
Außenbewegungen und Handlungsergebnisse werden nicht gelesen.

## Organische Bildung

Für jede Relation mit den Ereignisfinalisierungen

```text
t1, t2, t3, ...
```

entstehen ohne weitere Bedingung:

- gerichtete Übergänge `t1 -> t2`, `t2 -> t3`, ...,
- Zweischrittpfade `t1 -> t2 -> t3`, ... .

Teilen mehrere Relationen denselben Übergang oder Pfad, erhöht sich dessen
Rohunterstützung. Es gibt keine Mindeststärke. Die primäre Bündelungsgröße ist
die Zahl aller Relationspaare, die dieselbe Struktur teilen:

```text
Kollisionen = Summe über alle Strukturen von support * (support - 1) / 2
```

Damit tragen auch Zweierunterstützungen bei; keine Schwelle trennt wichtige
von unwichtigen Pfaden.

## Beobachtete Topologie

| Merkmal | 2091-Bestand | 2092-Holdout |
|---|---:|---:|
| Relationen | 2.580 | 1.932 |
| Relationsereignisse | 10.092 | 7.807 |
| Ereignisgetragene Übergänge | 7.512 | 5.875 |
| beteiligte Präfixknoten | 63 | 59 |
| unterschiedliche Übergangskanten | 975 | 804 |
| mehrfach getragene Übergangskanten | 649 | 555 |
| Kollisionen gemeinsamer Übergänge | 99.541 | 68.374 |
| Zweischrittpfad-Instanzen | 6.308 | 4.828 |
| unterschiedliche Zweischrittpfade | 2.380 | 1.986 |
| mehrfach getragene Zweischrittpfade | 906 | 757 |
| Kollisionen gemeinsamer Zweischrittpfade | 27.262 | 16.855 |

Die Topologie konzentriert viele Relationsfortsetzungen auf dieselben
Übergänge und Pfade. Ob diese Bündelung nur aus individuellem Rhythmus oder
der Ereignisaktivität einzelner Welten entsteht, wird durch zwei Kontrollen
getrennt.

## Relationseigene Gap-Reihenfolgen-Null

Pro Relation bleiben erhalten:

- erstes und letztes Ereignis,
- Ereigniszahl,
- die vollständige Multimenge ihrer Ereignisabstände.

Nur die Reihenfolge der Abstände wird 500-mal permutiert.

| Größe | 2091 beobachtet | 2091 Nullmittel | 2092 beobachtet | 2092 Nullmittel |
|---|---:|---:|---:|---:|
| unterschiedliche Übergänge | 975 | 1.021,83 | 804 | 902,71 |
| Übergangskollisionen | 99.541 | 88.520,86 | 68.374 | 51.923,87 |
| unterschiedliche Zweischrittpfade | 2.380 | 2.743,32 | 1.986 | 2.392,31 |
| Zweischrittkollisionen | 27.262 | 21.387,54 | 16.855 | 10.681,05 |

Alle vier gerichteten Vergleiche liegen in beiden Beständen außerhalb aller
500 Nullziehungen; jeweils `p = 1/501 = 0,001996`.

## Aktivitätserhaltende Ereignisnull

Die strengere Kontrolle vertauscht nur Zwischenereignisse zwischen
Relationen. Erhalten bleiben exakt:

- Ereigniszahl jeder Relation,
- erstes und letztes Ereignis jeder Relation,
- Ereigniszahl jeder einzelnen Weltfinalisierung,
- höchstens ein Ereignis derselben Relation pro Finalisierung.

Jede von 200 Kontrollen beginnt am wirklichen Bestand. Pro veränderbarem
Zwischenereignis werden 20 Tauschversuche ausgeführt. Im Mittel werden
32.887,54 beziehungsweise 24.531,82 gültige Tausche angenommen.

| Größe | 2091 beobachtet | 2091 Nullmittel | 2092 beobachtet | 2092 Nullmittel |
|---|---:|---:|---:|---:|
| unterschiedliche Übergänge | 975 | 1.035,40 | 804 | 861,51 |
| Übergangskollisionen | 99.541 | 91.929,31 | 68.374 | 63.240,25 |
| unterschiedliche Zweischrittpfade | 2.380 | 2.729,87 | 1.986 | 2.207,44 |
| Zweischrittkollisionen | 27.262 | 22.318,44 | 16.855 | 13.846,90 |

Auch hier erreicht keine Kontrolle die beobachtete Konzentration. Für alle
vier Vergleiche gilt in beiden Beständen `p = 1/201 = 0,004975`.

## Form der Bündelung

Die Zahl unterschiedlicher mehrfach getragener Strukturen ist nicht größer
als in den Kontrollen. Der Befund besteht stattdessen aus **weniger
unterschiedlichen Wegen bei höherer gemeinsamer Belegung**. Relationsfortsetzungen
verteilen sich also nicht auf zusätzliche Pfadklassen, sondern bündeln sich
auf einen kleineren Teil der möglichen zeitlichen Übergänge.

Einzelne Maximalstärken tragen nicht in jeder strengen Kontrolle. Besonders
die maximale Übergangskanten- und Pfadunterstützung des unabhängigen Holdouts
liegt innerhalb der aktivitätserhaltenden Null. Deshalb werden weder stärkste
Kanten noch Spitzenpfade als besondere Objekte gelesen.

## Befund

Getragen sind:

- eine gerichtete Übergangstopologie allein aus aufeinanderfolgenden
  Relationsereignissen,
- überzufällige Bündelung gemeinsamer Übergänge in beiden Beständen,
- überzufällige Bündelung echter Zweischrittpfade in beiden Beständen,
- Erhalt des Befunds gegenüber relationseigenem Rhythmus und vollständiger
  Weltaktivität,
- dieselbe qualitative Form im Entwicklungsbestand und unabhängigen Holdout.

Nicht getragen sind:

- Zustandsklassen, Zustandsvektoren oder Distanzschwellen,
- eine besondere Bedeutung einzelner Weltpräfixe, Kanten oder Maximalpfade,
- bereits nachgewiesene Vorhersagekraft für spätere Relationsereignisse,
- eine neue Zustands- oder Übergangs-Memory,
- eine Rücklesung in Feld, Wahrnehmung oder Handlung.

2097 zeigt erstmals eine bestandübergreifend getragene innere
Zustandsübergangstopologie: Individuelle relationale Erfahrungen bündeln sich
auf gemeinsame zeitliche Wege, obwohl vollständige Ereigniszustände nie exakt
wiederkehren. Die Struktur bleibt aus der vorhandenen Ereigniszeit
rekonstruierbar und wird deshalb nicht zusätzlich gespeichert. Sie ist ein
Kandidat für organische Zustandsnachbarschaft, aber noch keine Feldintelligenz.

## Reproduzierbare Ausgaben

- `2097_MCM_RELATIONSEREIGNIS_GETRAGENE_ZUSTANDSUEBERGANGSTOPOLOGIE.metrics.csv`
- `2097_MCM_RELATIONSEREIGNIS_GETRAGENE_ZUSTANDSUEBERGANGSTOPOLOGIE.support.csv`
- `2097_MCM_RELATIONSEREIGNIS_GETRAGENE_ZUSTANDSUEBERGANGSTOPOLOGIE.null.csv`
- `2097_MCM_RELATIONSEREIGNIS_GETRAGENE_ZUSTANDSUEBERGANGSTOPOLOGIE.summary.csv`

Die Auswertung liest ausschließlich die kompakten Archive aus 2089 und 2092.
Sie erzeugt keine Welt-, Debug-, Memory- oder Runtime-Dateien.
