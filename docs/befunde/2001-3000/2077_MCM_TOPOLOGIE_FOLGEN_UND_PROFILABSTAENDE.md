# 2077 - MCM-Topologie: Folgen und Profilabstände

## Zweck

Befund 2076 zeigte einen nahezu reihenfolgenstabilen globalen Graphen, aber keine belastbare Bindung zwischen zwei direkt folgenden Realwelten. Diese Prüfung untersucht deshalb ausschließlich die innere zeitliche Struktur der abgeschlossenen MCM-Feldepisoden:

- gerichtete Motive aus zwei, drei und vier Episoden,
- kontinuierliche Abstände zwischen den inneren Feldprofilen,
- Vergleich einer reihenfolgefreien Profilnähe mit einer reihenfolgensensitiven Verlaufsnähe.

Die vollständigen Welten dienen nur als Reiz- und Herkunftskontext. Es werden keine Chartbestandteile, Volumenmerkmale oder Marktmuster als Identitäten untersucht.

## Prüfbasis

Wie in Befund 2076 werden vier vollständige Welten mit jeweils frischem Memory gelesen:

- Realanker `5000_6000`,
- direktes Realfolgefenster `6000_7000`,
- Shuffle-Nullwelt des Folgefensters,
- Random-Sign-Nullwelt des Folgefensters.

Die Läufe erzeugen 29, 23, 25 und 21 abgeschlossene innere Episoden. Entpackte Welten, Laufmemory und Debugdaten werden nach der Auswertung automatisch entfernt.

## Längere gerichtete Motive

Ein Motiv ist eine überlappende Folge tatsächlich abgeschlossener Episoden. Die Knotenidentität enthält den inneren Episodenzustand, seine Nachbarschaft, Dauerklasse und quantisierte Feldqualitäten.

| Vergleich | Paar-Jaccard | Dreier-Jaccard | Vierer-Jaccard |
|---|---:|---:|---:|
| Realanker - Realfolge | 0,068 | 0,021 | 0,000 |
| Realanker - Null-Shuffle | 0,186 | 0,000 | 0,000 |
| Realanker - Null-Random | 0,154 | 0,070 | 0,000 |
| Realfolge - Null-Shuffle | 0,073 | 0,000 | 0,000 |
| Realfolge - Null-Random | 0,152 | 0,026 | 0,000 |
| Null-Shuffle - Null-Random | 0,167 | 0,000 | 0,000 |

Mit vier Episoden ist kein exaktes Motiv zwischen zwei Welten gemeinsam. Eine bloße Verlängerung der aktuellen Symbolfolge schafft daher keine verbindende Semantik. Sie macht die Identität hauptsächlich seltener.

Die gröbere Zustandsfolge löst das Problem ebenfalls nicht. In allen vier Welten treten nur zwei Episodenzustände und für jede Länge dieselben zwei alternierenden Zustandsmotive auf. Der Mengen-Jaccard beträgt deshalb für alle Zustandsvergleiche 1,000. Diese Ebene ist bereits vollständig gesättigt und kann die Welten nicht unterscheiden.

## Kontinuierliche Feldprofilabstände

Jede Episode wird nur durch ihre inneren Qualitäten gelesen. Drei Profilräume kontrollieren, ob das Ergebnis von einer einzelnen Skalierung abhängt:

1. vier rohe Kernqualitäten: Tragen, Spannung, Rekopplung und adaptive Rekopplung,
2. sieben rohe Feldqualitäten einschließlich Sinneskopplung und beider Feldabstände,
3. dieselben sieben Qualitäten plus logarithmierte Episodendauer, gemeinsam standardisiert.

Der **Profilwolken-Abstand** mittelt beidseitig den Abstand zum jeweils nächsten Profil und ignoriert die Reihenfolge. Der **DTW-Abstand** erhält die Episodenfolge und erlaubt nur eine zeitlich geordnete Streckung des Verlaufs. Kleinere Werte bedeuten größere innere Nähe.

| Profilraum | Vergleich | Profilwolke | geordneter DTW-Abstand |
|---|---|---:|---:|
| vier Kernqualitäten roh | Realanker - Realfolge | 0,005586 | 0,023175 |
|  | Realanker - Null-Shuffle | **0,005404** | **0,016720** |
|  | Realanker - Null-Random | 0,008610 | 0,027295 |
| sieben Feldqualitäten roh | Realanker - Realfolge | **0,014657** | 0,046080 |
|  | Realanker - Null-Shuffle | 0,014789 | **0,041540** |
|  | Realanker - Null-Random | 0,017778 | 0,055865 |
| Feldqualitäten und Dauer standardisiert | Realanker - Realfolge | 0,158585 | 0,483074 |
|  | Realanker - Null-Shuffle | **0,144609** | **0,415622** |
|  | Realanker - Null-Random | 0,187406 | 0,529543 |

Der reihenfolgensensitive DTW-Abstand ordnet in allen drei Profilräumen die Shuffle-Nullwelt näher an den Realanker als das direkt folgende Realfenster. Bei der reihenfolgefreien Profilwolke gilt das in zwei Profilräumen. Im vollständigen rohen Profilraum liegt die Realfolge nur um 0,000132 näher; diese kleine Umkehr trägt keine robuste Realbindung.

## Befund

Die aktuelle Topologie besitzt eine Auflösungslücke:

- Die reine Episodenzustandsfolge ist zu grob und zwischen den Welten gesättigt.
- Die exakte Episodenidentität ist für längere Motive zu fein; Viererfolgen kehren nirgends weltübergreifend wieder.
- Die kontinuierliche Profilgeometrie bleibt lesbar, hebt den direkten Realfolge-Anschluss aber nicht stabil von der Shuffle-Nullwelt ab.

Damit bestätigt Befund 2077 die Grenze aus 2076. Längere Folgen oder kontinuierliche Nähe dürfen noch nicht als semantische Bindung, Resonanz oder Bedeutung in das Feld zurückgeschrieben werden.

## Forschungsgrenze

Der aktuelle Vierweltzweig ist an dieser Stelle ausgeschöpft. Weitere Motivverlängerung mit derselben Identität würde vor allem zusätzliche Einmaligkeit erzeugen; eine Feldrückwirkung wäre nicht fundiert. Der Lauf verändert deshalb weder Topologie-Memory noch Feld, Handlung, Gate oder Motorik.

Reproduzierbare Ausgaben:

- `2077_MCM_TOPOLOGIE_FOLGEN_UND_PROFILABSTAENDE.worlds.csv`
- `2077_MCM_TOPOLOGIE_FOLGEN_UND_PROFILABSTAENDE.motifs.csv`
- `2077_MCM_TOPOLOGIE_FOLGEN_UND_PROFILABSTAENDE.distances.csv`
