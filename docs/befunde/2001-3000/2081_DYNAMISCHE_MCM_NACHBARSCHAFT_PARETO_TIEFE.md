# 2081 - Dynamische MCM-Nachbarschafts-Pareto-Tiefe

## Zweck

Befund 2080 zeigte eine starke, aber überlappende Reifungsschichtung der passiven Nachbarschafts-Memory. Diese Prüfung untersucht, ob sich daraus ohne Gewichtung und ohne Schwelle dynamische Reifungstiefen bilden.

Die Pareto-Tiefe verwendet ausschließlich die drei in Befund 2080 robusten Achsen:

- bestätigende Weltpaare,
- Zahl getragener Weltläufe,
- Weltabschlüsse mit erneuter Bestätigung.

Eine Relation liegt in Schicht 1, wenn keine andere Relation auf allen drei Achsen mindestens gleich und auf einer Achse stärker ist. Nach Entfernung dieser Spitze entsteht Schicht 2, danach Schicht 3 und so weiter. Keine Achse erhält ein Gewicht.

## Passive Prüfanordnung

Dieselben 81 Welten wachsen erneut in zwei getrennten fortlaufenden Memories vorwärts und rückwärts. Nach 10, 20, 40, 60 und 81 Welten wird der aktuelle Graph diagnostisch geschichtet.

Die Pareto-Tiefe wird nicht in die Memory geschrieben. Sie beeinflusst weder weiteres Wachstum noch Feld, Handlung, Gate oder Motorik. Die 26 strengen Relationen aus Befund 2078 werden erst nach der Schichtbildung markiert.

## Entstehende Schichten

| Welten | Relationen vorwärts/rückwärts | maximale Tiefe | Schicht 1 | Kernmedian | Peripheriemedian | AUC Kern flacher |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 240 / 190 | 20 / 23 | 1 / 1 | 8,5 / 11,5 | 20 / 22 | 0,852 / 0,871 |
| 20 | 482 / 421 | 36 / 34 | 2 / 1 | 10,5 / 8 | 34 / 32 | 0,893 / 0,895 |
| 40 | 952 / 928 | 53 / 55 | 2 / 2 | 9 / 9,5 | 51 / 52 | 0,940 / 0,952 |
| 60 | 1.591 / 1.541 | 66 / 66 | 2 / 2 | 8 / 8 | 64 / 64 | 0,965 / 0,965 |
| 81 | 2.046 / 2.085 | 77 / 75 | 2 / 2 | 9,5 / 9 | 74 / 73 | 0,972 / 0,972 |

Mit wachsender Erfahrung wandert der bekannte Kern relativ zur Gesamtstruktur deutlich nach vorn. Am Endpunkt liegt sein Median normiert bei 0,112 beziehungsweise 0,108, während die Peripherie bei 0,961 beziehungsweise 0,973 liegt. Null entspricht der Spitze, eins der tiefsten Schicht.

Die Schichtung bleibt trotzdem kontinuierlich. Am Endpunkt reicht der Kern von Schicht 1 bis 35, die Peripherie bereits von Schicht 2 an. Es existiert kein Tiefenwert, der beide Gruppen vollständig trennt.

## Migration im Wachstum

| Übergang | Tiefen-Spearman vorwärts | mittlere normierte Änderung | Tiefen-Spearman rückwärts | mittlere normierte Änderung |
|---|---:|---:|---:|---:|
| 10 -> 20 | 0,821 | 0,127 | 0,811 | 0,156 |
| 20 -> 40 | 0,825 | 0,139 | 0,829 | 0,146 |
| 40 -> 60 | 0,907 | 0,072 | 0,932 | 0,077 |
| 60 -> 81 | 0,942 | 0,045 | 0,931 | 0,046 |

Frühe Beziehungen können ihre relative Schicht noch deutlich verändern. Mit wachsender Erfahrung stabilisiert sich die Rangtiefe, und die mittlere normierte Bewegung sinkt in beiden Wegen auf ungefähr 0,045.

Das ist keine Erstarrung: Nur 64 von 1.591 beziehungsweise 87 von 1.541 bereits vorhandenen Relationen behalten zwischen Welt 60 und 81 exakt dieselbe absolute Schichtnummer. Stabil wird vor allem die relative Ordnung innerhalb eines gleichzeitig weiter wachsenden Netzes.

## Stabilität zwischen Erfahrungswegen

| Welten | Relations-Jaccard | Tiefen-Spearman gemeinsamer Relationen | Schicht-1-Jaccard |
|---:|---:|---:|---:|
| 10 | 0,201 | 0,524 | 0,000 |
| 20 | 0,254 | 0,575 | 0,500 |
| 40 | 0,243 | 0,648 | 1,000 |
| 60 | 0,554 | 0,884 | 1,000 |
| 81 | 0,881 | 0,969 | 1,000 |

Die frühen Teilwelten beider Wege unterscheiden sich absichtlich stark. Trotzdem wird Schicht 1 ab Welt 40 identisch. Am Ende besitzen die 1.935 gemeinsamen Relationen nahezu dieselbe Tiefenrangfolge.

Die zwei globalen Spitzenrelationen sind in beiden Endgraphen identisch:

- `dio_mcm_episode_1qlxgj7` zu `dio_mcm_episode_1x557o1`,
- `dio_mcm_episode_1tvdhgs` zu `dio_mcm_episode_1x557o1`.

Diese Relationen wurden weder vorgegeben noch während des Wachstums als Ziel verwendet.

## Befund

Die drei robusten Tragungsachsen erzeugen ohne Gewichtung eine dynamische und zunehmend stabile Reifungstiefe. Getragen sind:

- frühe Beweglichkeit statt sofortiger Festlegung,
- zunehmende Stabilisierung der relativen Ordnung,
- starke Kern-/Peripherieschichtung,
- identische globale Spitze unter gegensätzlicher Erfahrung,
- nahezu gleiche finale Tiefenrangfolge.

Nicht getragen sind:

- eine binäre Reifeklasse,
- ein fester Tiefengrenzwert,
- automatisches Löschen oder Dämpfen tiefer Schichten,
- Feldrückwirkung aus Pareto-Tiefe.

Pareto-Tiefe ist damit als passive Reifungsbeschreibung fundiert. Sie ist noch keine aktive Ressourcenzuteilung und keine organische Vergessensentscheidung.

## Technische Grenze

Die diagnostische Schichtung vergleicht Relationen paarweise und besitzt quadratischen Aufwand. Sie wird deshalb in diesem Befund nur an fünf Checkpoints berechnet und nicht nach jedem Weltabschluss in die Runtime integriert. Die beiden vollständigen Runtime-Memories und alle Debugdaten bleiben lokal.

Reproduzierbare Ausgaben:

- `2081_DYNAMISCHE_MCM_NACHBARSCHAFT_PARETO_TIEFE.snapshots.csv`
- `2081_DYNAMISCHE_MCM_NACHBARSCHAFT_PARETO_TIEFE.layers.csv`
- `2081_DYNAMISCHE_MCM_NACHBARSCHAFT_PARETO_TIEFE.migration.csv`
- `2081_DYNAMISCHE_MCM_NACHBARSCHAFT_PARETO_TIEFE.order.csv`
- `2081_DYNAMISCHE_MCM_NACHBARSCHAFT_PARETO_TIEFE.core.csv`
- `2081_DYNAMISCHE_MCM_NACHBARSCHAFT_PARETO_TIEFE.summary.csv`
