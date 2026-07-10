# 2078 - Wiederkehrende MCM-Episodennachbarschaften

## Zweck

Befund 2077 zeigte eine Auflösungslücke zwischen gesättigten groben Zuständen und zu spezifischen exakten Episodenfolgen. Diese Prüfung untersucht deshalb, ob zwischen verschiedenen exakten Episodenidentitäten eine wiederkehrende kontinuierliche Nachbarschaft sichtbar wird.

Gesucht wird noch keine Gruppe und keine feste Bedeutung. Gemessen wird nur, welche zwei verschiedenen inneren Episodenprofile sich über unabhängige Feldläufe wiederholt gegenseitig am nächsten liegen.

## Schwellenfreie Lesung

Die Prüfung verwendet weder eine Distanzschwelle noch eine vorgegebene Nachbarzahl. Für jedes Paar vollständiger Welten gilt:

1. Jede exakte Episodenidentität sucht im anderen Feldlauf ihr nächstes verschiedenes Profil.
2. Eine Relation wird nur gezählt, wenn die Nähe wechselseitig ist.
3. Die Zählung erfolgt getrennt in drei inneren Profilräumen.
4. Welt, Jahr und Kontrollart bleiben ausschließlich Herkunft und Prüfbasis.

Die drei Profilräume entsprechen Befund 2077:

- vier rohe Kernqualitäten,
- sieben rohe Feldqualitäten,
- sieben Feldqualitäten plus Episodendauer, gemeinsam standardisiert.

## Breite Prüfbasis

81 vollständige Welten werden mit jeweils frischem Memory gelesen:

- 27 Realwelten,
- 54 Shuffle- und Random-Sign-Nullwelten,
- 2025er Feldläufe sowie unabhängige 2024er Holdouts,
- zwei Zeitebenen und mehrere vollständige Weltkontexte.

Die Außenwelten werden nicht in Chartmerkmale zerlegt. Entpackte Welten, Debugdaten und Laufmemories werden nach der Auswertung automatisch entfernt.

Realwelten bilden im Mittel 17,26 verschiedene Episodenidentitäten, Nullwelten 14,80. Deshalb werden absolute Linkzahlen zusätzlich durch die jeweils kleinere Topologie normiert.

## Nachbarschaftsdichte

| Profilraum | Weltpaartyp | mittlere Links | Anteil an kleinerer Topologie |
|---|---|---:|---:|
| vier Kernqualitäten | Real - Real | 8,365 | 0,553 |
|  | Real - Null | 7,960 | 0,575 |
|  | Null - Null | 7,415 | 0,571 |
| sieben Feldqualitäten | Real - Real | 8,202 | 0,542 |
|  | Real - Null | 7,772 | 0,561 |
|  | Null - Null | 7,392 | 0,570 |
| Feldqualitäten und Dauer | Real - Real | 8,311 | 0,551 |
|  | Real - Null | 7,818 | 0,564 |
|  | Null - Null | 7,393 | 0,568 |

Real-Real-Paare besitzen absolut etwas mehr gegenseitige Nachbarn. Nach Berücksichtigung ihrer größeren Topologien kehrt sich dieser Abstand jedoch in allen drei Profilräumen um. Eine allgemeine realweltspezifische Nachbarschaftsdichte ist damit nicht belegt.

## Wiederkehrende Relationen

Insgesamt entstehen 2.116 verschiedene Nachbarschaftskandidaten:

| getragene Profilräume | Relationen |
|---:|---:|
| 1 von 3 | 1.021 |
| 2 von 3 | 501 |
| 3 von 3 | 594 |

Die Profilräume lesen also keinen identischen Graphen. Ihre Linkmengen überlappen mit Jaccard-Werten von 0,361 bis 0,543. Gleichzeitig ist die Verteilung stark ungleich: Wenige Relationen kehren in sehr vielen Weltpaaren wieder, während viele nur in einem Profilraum oder wenigen Kontexten auftreten.

Auch die Weltpaartypen tragen unterschiedliche, aber überlappende Linkmengen:

| Vergleich | Link-Jaccard |
|---|---:|
| Real-Real zu Real-Null | 0,347 |
| Real-Real zu Null-Null | 0,213 |
| Real-Null zu Null-Null | 0,464 |

Die häufigste Relation tritt in 2.227 Weltpaaren auf. Ihre normierte Tragungsrate ist jedoch in Real-Real-Paaren mit 0,644 niedriger als in Real-Null-Paaren mit 0,741 und Null-Null-Paaren mit 0,789. Hohe Wiederkehr allein ist daher noch keine reale Bedeutung.

## Jahres- und Profilkern

Von den 2.116 Relationen besitzen:

- 490 gegenseitige Nachbarschaft über die Jahresgrenze,
- 112 Unterstützung innerhalb 2025, über die Jahresgrenze und innerhalb 2024,
- 26 in allen drei Realweltkohorten mindestens eine Weltpaarbeobachtung, die zugleich von allen drei Profilräumen getragen wird.

Diese 26 bilden einen strengen diagnostischen Kern, keine Runtime-Auswahl. Innerhalb dieses Kerns haben 18 Relationen eine höhere Real-Real-Tragungsrate als beide Kontrollarten; acht werden von mindestens einer Kontrollart stärker getragen.

Über alle 940 in Real-Real-Paaren überhaupt prüfbaren Relationen ist das Bild schwächer:

- 295 besitzen einen positiven Realratenabstand,
- 65 liegen gleich,
- 580 werden von mindestens einer Kontrollart stärker getragen.

Der kleine Kern ist somit nicht realexklusiv. Er zeigt eine wiederkehrende innere Geometrie, die teilweise in Realwelten stärker, teilweise aber allgemein oder kontrollgetragen entsteht.

## Befund

Zwischen exakten Episodenidentitäten existiert eine reproduzierbare kontinuierliche Nachbarschaftsebene. Sie ist weder so grob gesättigt wie die reine Zustandsfolge noch so vollständig vereinzelt wie längere exakte Motive.

Getragen ist:

- verschiedene exakte Episoden können wiederholt gegenseitige nächste Nachbarn sein,
- ein kleiner Teil dieser Relationen bleibt profil- und jahresübergreifend sichtbar,
- die Nachbarschaft kann ohne feste Distanzschwelle gelesen werden.

Nicht getragen ist:

- eine allgemeine Überlegenheit der Real-Real-Nachbarschaften,
- eine realexklusive semantische Bindung,
- eine Berechtigung, Nähe bereits als Bedeutung oder Resonanz auf das Feld zurückwirken zu lassen.

## Technische Grenze

Der Lauf verändert weder Topologie-Memory noch Feld, Handlung, Gate oder Motorik. Die 26 Kernrelationen werden nicht als festes Verzeichnis in MINI_DIO geschrieben. Sie bleiben reproduzierbare Forschungsevidenz dafür, dass eine passive, erfahrungsakkumulierende Nachbarschaftsebene möglich ist, ohne ihre konkreten Beziehungen vorzuprogrammieren.

Reproduzierbare Ausgaben:

- `2078_WIEDERKEHRENDE_MCM_EPISODENNACHBARSCHAFTEN.worlds.csv`
- `2078_WIEDERKEHRENDE_MCM_EPISODENNACHBARSCHAFTEN.summary.csv`
- `2078_WIEDERKEHRENDE_MCM_EPISODENNACHBARSCHAFTEN.links.csv`
- `2078_WIEDERKEHRENDE_MCM_EPISODENNACHBARSCHAFTEN.overlap.csv`
