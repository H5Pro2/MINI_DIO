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
      first_checkpoint
      last_checkpoint
      observed_checkpoint_count
      latest_pareto_depth
      latest_normalized_depth
      history
        checkpoint_symbol
        pareto_depth
        max_pareto_depth
        normalized_depth
        world_pair_count
        world_count
        growth_seen_count
```

Ein Checkpoint besitzt eine deterministische Identität aus Bezeichnung und
Laufindex. Derselbe Checkpoint kann dadurch nicht versehentlich zweimal in die
Historie geschrieben werden.

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

Der gesamte Zweig und jeder Relationsstand tragen folgende Sperren:

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

Die wachsende Historie ist damit zunächst verlustfrei. Befund 2082 zeigt
zugleich ihre technische Grenze: Fünf Checkpoints erhöhen die vollständige
Memory-Größe bei 81 Welten um rund 32 bis 33 Prozent. Diese Ebene ist eine
kontrollierte Forschungsstruktur, noch keine organische Kompression.
