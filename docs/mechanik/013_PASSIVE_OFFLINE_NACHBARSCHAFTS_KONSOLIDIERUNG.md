# 013 - Passive Offline-Nachbarschafts-Konsolidierung

## Aufgabe

Diese Ebene bewahrt beobachtete Reifungsstände der passiven
MCM-Nachbarschafts-Memory. Sie erzeugt keine neue Beziehung und verändert keine
Nachbarschaftsevidenz. Ihre einzige Quelle sind bereits aktive, organisch
gewachsene Beziehungen.

Die Konsolidierung wird ausdrücklich außerhalb eines Weltlaufs aufgerufen.
`mini_dio.run_mini` kennt und liest ihre Ergebnisse nicht.

## Datenstruktur

Die Ebene liegt unter `passive_mcm_neighborhood_consolidation`:

```text
passive_mcm_neighborhood_consolidation
  checkpoints
    dio_mcm_consolidation_*
      checkpoint_index
      checkpoint_label
      run_index
      relation_count
      max_pareto_depth
      layer_counts

  relations
    dio_mcm_neighbor_*
      left_node
      right_node
      history_deltas
        checkpoint_index_delta
        pareto_depth_delta
        world_pair_count_delta
        world_count_delta
        growth_seen_count_delta
```

Ein Checkpoint besitzt eine deterministische Identität aus Bezeichnung und
Laufindex. Derselbe Checkpoint kann dadurch nicht versehentlich zweimal in die
Historie geschrieben werden.

Der erste Vektor einer Relation ist relativ zu null und enthält damit ihren
vollständigen Ausgangsstand. Folgende Vektoren sind exakte ganzzahlige
Differenzen zum vorherigen beobachteten Stand. Bezeichnung, Laufindex, maximale
Tiefe und Schichtverteilung liegen einmal im gemeinsamen Checkpoint.

Beim diagnostischen Lesen werden daraus wieder vollständige Datensätze mit
absoluten Werten und normierter Tiefe erzeugt. Diese Expansion wird nicht in
das Memory-Dokument zurückgeschrieben.

## Schichtbildung

Verglichen werden nur drei gewachsene Tragungsachsen:

1. Weltpaartragung,
2. Zahl getragener Welten,
3. Zahl bestätigender Weltabschlüsse.

Eine Relation liegt in Schicht 1, wenn keine andere auf allen drei Achsen
mindestens gleich und auf einer Achse stärker ist. Danach werden weitere
nichtdominierte Schichten gebildet. Es gibt weder Gewichte noch feste
Grenzwerte.

## Harte Grenze

Der gesamte Zweig trägt folgende Sperren, die beim diagnostischen Lesen auf
jeden Relationsstand projiziert werden:

```text
passive_only = 1
offline_only = 1
read_by_mini_dio = 0
influences_field = 0
influences_action = 0
deletes_memory = 0
dampens_memory = 0
is_gate = 0
is_motoric = 0
is_entry_signal = 0
is_direction_signal = 0
```

Die öffentliche `SemanticMemory`-Methode darf einen Checkpoint anlegen und
diagnostisch lesen. Es existiert kein Aufruf aus Wahrnehmung, Feldmechanik,
Aktionswahl oder Motorik.

## Erhaltungsprinzip

Jeder neue Checkpoint hängt den aktuellen Stand an die jeweilige
Relationshistorie an. Frühere Einträge werden nicht neu berechnet, ersetzt,
gedämpft oder gelöscht. Relationen, die an einem späteren Checkpoint nicht
aktiv sind, behalten ihre bisherige Bahn unverändert.

Die wachsende Historie bleibt verlustfrei. Befund 2082 zeigte die technische
Grenze der wiederholten Vollstände: Fünf Checkpoints erhöhten die vollständige
Memory-Größe bei 81 Welten um rund 32 bis 33 Prozent.

Seit Befund 2083 speichert `compact_delta_v1` dieselben Reifungsbahnen als
Änderungsvektoren. Alle 10.476 Einträge werden exakt rekonstruiert, während
rund 72,7 Prozent des vorherigen Konsolidierungsmehrbedarfs entfallen. Es wird
keine Relation entfernt, gerundet oder nach Bedeutung ausgewählt.

## Bewegungsgrenze 2084

Eine schwellenfreie Offline-Prüfung verbindet gegenseitig nächste
Reifungsbewegungen in drei getrennten Profilräumen. Der überzufällige
Kantenüberschuss entsteht fast vollständig aus groben Zweipunktbahnen mit sehr
großen exakten Gleichstandsklassen. Bei drei, vier und fünf beobachteten
Punkten bleibt kein gemeinsames robustes Nachbarschaftspaar zwischen den
Erfahrungsrichtungen erhalten.

Die Delta-Historie wird deshalb nicht als Reifungsfamilien- oder
Feldrücklesestruktur erweitert. Sie bewahrt individuelle Entwicklung, ohne aus
der derzeit unzureichenden Bewegungsstabilität zusätzliche Runtime-Ordnung zu
erzeugen.
