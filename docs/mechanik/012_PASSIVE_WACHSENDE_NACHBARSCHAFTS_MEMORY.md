# 012 - Passive wachsende Nachbarschafts-Memory

## Aufgabe

Die Nachbarschafts-Memory bildet eine mittlere relationale Ebene zwischen zwei bereits vorhandenen Auflösungen:

- Ein grober Feldzustand fasst viele Episoden zusammen und kann dadurch früh sättigen.
- Eine exakte Episodenidentität bewahrt feine Unterschiede, kann aber über längere Folgen zu stark vereinzeln.
- Eine Nachbarschaft verbindet verschiedene exakte Identitäten nur über wiederholt beobachtete kontinuierliche Feldnähe.

Sie ersetzt weder die Episodenidentität noch die gerichtete Topologie. Sie ergänzt beide um erfahrungsgetragene Nähe.

## Datenstruktur

Die Ebene liegt unter `passive_mcm_neighborhood_memory` im Semantic-Memory-Dokument:

```text
passive_mcm_neighborhood_memory
  world_profiles
    dio_mcm_world_*
      world_label
      run_index
      episode_observations
      nodes
        dio_mcm_episode_*
          seen_count
          avg_duration
          innere Feldqualitäten

  neighborhoods
    dio_mcm_neighbor_*
      left_node
      right_node
      current_scope_support
      current_world_pair_count
      current_world_count
      support_world_mask
      current_avg_distance
      first_run
      last_run
      growth_seen_count
```

Weltlabel und Laufnummer erzeugen eine Herkunftsidentität für ein Weltprofil. Die Nachbarschaftsidentität selbst entsteht ausschließlich aus den beiden sortierten inneren Episodenidentitäten.

## Wachstumsbedingung

Nach Abschluss eines Weltlaufs wird sein Profil mit jedem früher abgeschlossenen Weltprofil verglichen. Eine Beziehung erhält Evidenz, wenn zwei verschiedene Episodenidentitäten gegenseitig nächste Profile sind.

Die Prüfung erfolgt getrennt in drei Räumen:

1. Tragen, Spannung, Rekopplung und adaptive Rekopplung,
2. diese Kernqualitäten plus Sinneskopplung und beide Feldabstände,
3. vollständiges Profil plus Episodendauer, pro Weltpaar standardisiert.

Es existieren weder eine feste Distanzschwelle noch ein vorgegebenes `k`. Auch die später häufigsten Links werden nicht als Konstanten geführt.

## Akkumulation Statt Festschreibung

Jedes Weltpaar wird genau einmal verarbeitet. Bestehende Relationen sammeln zusätzliche Tragung, Kontextbreite und Abstandserfahrung. Neue Relationen können jederzeit hinzukommen.

Die aktuelle Version löscht alte Evidenz noch nicht. Relative Tragung kann sich durch neue Beobachtungen verschieben, aber eine eigenständige Alterung, Konkurrenz oder Vergessensdynamik ist noch nicht Bestandteil dieser Ebene.

Die Kontextbreite wird verlustfrei als Ganzzahl-Bitmaske der bestätigenden Laufnummern gespeichert. Dadurch muss eine Relation nicht für jeden getragenen Lauf einen langen Hash wiederholen. Die Bitmaske ist reine Kompaktierung; sie verändert weder Nachbarschaft noch Tragungszahl.

## Harte Grenze

Alle Weltprofile, Knoten und Nachbarschaften tragen dieselben passiven Sperren:

```text
read_by_mini_dio = 0
influences_field = 0
influences_action = 0
is_gate = 0
is_motoric = 0
is_entry_signal = 0
is_direction_signal = 0
```

Runtime und Reports dürfen die Memory schreiben und diagnostisch ausgeben. Wahrnehmung, MCM-Feldwirkung, Aktionswahl und Motorik konsumieren sie nicht.

## Skalierungsgrenze

Weltprofile und Evidenz wachsen derzeit ohne organische Kompression. Der inkrementelle Vergleich vermeidet wiederholte Vollaufbauten, aber die persistierte Erfahrung bleibt unbeschränkt. Dieser Stand ist für kontrollierte Forschung tragfähig, nicht für unbegrenzten Dauerbetrieb.

## Reifungsstand 2080

Weltpaartragung, Zahl getragener Welten und bestätigende Weltabschlüsse bilden gemeinsam eine robuste kontinuierliche Reifungsordnung. Ihre Rangfolgen korrelieren zwischen umgekehrten Erfahrungswegen mit 0,804 bis 0,975. Ein schwellenfreier Pareto-Vergleich findet drei identische undominierte Kernrelationen in beiden Wegen.

Diese Ordnung ist nicht binär. Kern und periphere Ausreißer überlappen; Aktualität und Bestätigungsalter sind deutlich pfadabhängiger. Deshalb existiert weiterhin keine Lösch-, Dämpfungs- oder Feldrückleselogik.
