# 014 - Passive relationsinterne Ereigniszeit

## Aufgabe

Die Ereigniszeit bewahrt den eigenen Wachstumsrhythmus jeder passiven
MCM-Nachbarschaft. Sie ersetzt einen global vorgegebenen Messtakt durch bereits
vorhandene Relationsereignisse.

Ein Ereignis wird ausschließlich dann geschrieben, wenn eine Beziehung beim
Abschluss eines Weltlaufs neue gegenseitige Nachbarschaftsevidenz erhält. An
derselben Stelle steigt bereits `growth_seen_count`. Die Ereignis-Memory
erzeugt keinen zusätzlichen Trigger.

## Datenstruktur

```text
passive_mcm_neighborhood_event_memory
  format = compact_relation_event_delta_v1
  relations
    dio_mcm_neighbor_*
      left_node
      right_node
      event_deltas
        finalization_index_delta
        world_pair_count_delta
        world_count_delta
        growth_seen_count_delta
        field_core_raw_delta
        field_full_raw_delta
        field_full_plus_duration_standardized_delta
```

Der erste Vektor einer Relation ist relativ zu null und enthält ihren
vollständigen ersten Ereignisstand. Jeder weitere Vektor ist die exakte
ganzzahlige Differenz zum vorherigen eigenen Ereignis. Beim diagnostischen
Lesen werden absolute Stände rekonstruiert, ohne sie expandiert zurück in die
Memory zu schreiben.

Beginnt die Ebene in einer bereits gewachsenen Alt-Memory, werden frühere
Bestätigungen nicht mit erfundenen Zeitpunkten nachgebildet. Die Relation
bewahrt deren Anzahl ausdrücklich als `unobserved_prior_events`; erst folgende
Ereignisse besitzen eine beobachtete Eigenzeit. In frischen Memories ist dieser
Legacy-Anteil null.

Weltlabel und Außenwerte sind nicht Bestandteil des Ereignisses. Der
`finalization_index` bewahrt nur die Lage des Relationsereignisses innerhalb
der bereits durchlaufenen inneren Erfahrung.

## Harte Grenze

```text
passive_only = 1
relation_event_time_only = 1
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

Der Schreibaufruf liegt im passiven Nachbarschaftswachstum. Es existiert kein
Lesepfad von der Ereigniszeit zurück in Wahrnehmung, Feldmechanik,
Aktionsbereitschaft oder Motorik.

## Integritätsprinzip

Für jede Relation müssen drei Identitäten gelten:

1. Zahl der Ereignisse ist gleich `growth_seen_count`.
2. Der letzte Ereigniszeitpunkt ist gleich `last_finalization`.
3. Der letzte Ereignisstand ist gleich den aktuellen Trägerwerten der
   Nachbarschaft.

Befund 2085 bestätigt alle drei Identitäten für 4.131 Endrelationen in zwei
gegengesetzten 81-Welten-Folgen ohne eine Abweichung. Auch Relationsmenge,
Trägerachsen und Pareto-Tiefe bleiben exakt zur Referenz 2081.

## Forschungsstand 2085

Die beiden Folgen erzeugen zusammen 23.492 eigene Relationsereignisse. Die
Ereigniszahl gemeinsamer Beziehungen korreliert mit 0,804, während exakte
Langzeitverläufe ab fünf Ereignissen nicht mehr identisch bleiben.

Die Ebene trägt daher individuelle relationale Erfahrung, aber keine feste
Reifungsfamilie. Sie bleibt passive Zeitstruktur und erzeugt weder Selektion
noch Feldrückwirkung.

## Bewegungsstand 2086

Bei gleichem Relationsalter lösen sich exakte Gleichstände ab drei Ereignissen
nahezu vollständig auf. Breiten- und Profilzuwachs bilden getrennt noch bis
Alter 10 überzufällige gemeinsame Nachbarschaften. Dieselben Paare tragen aber
ab Alter 3 nicht gleichzeitig über Eigenzeittakt, Breite und Profilraum.

Die Ereignis-Memory bleibt deshalb eine individuelle Zeitbasis. Sie erhält
keine einheitliche Reifungsfamilie und keine Multiplex-Rückleselogik. Die
getrennten Teilräume bleiben diagnostische Forschungskandidaten.

## Persistenzstand 2087

Achsenspezifische Kanten bleiben innerhalb beider Erfahrungsrichtungen von
Relationsalter 3 über 5 bis 10 deutlich überzufällig erhalten.
Reihenfolgenübergreifend verbleiben ein vollständiger Breitenverbund aus 19
Relationen und ein darin liegender vollständiger Profilverbund aus 4
Relationen. Die strengere Identitätsnull wird nur schwach unterschritten; der
Taktverbund trägt nicht.

Die Komponenten werden weder gespeichert noch bevorzugt. Insbesondere stehen
keine Relationsidentitäten als Konstanten im Runtime-Code. Die Ereignis-Memory
bleibt eine passive Grundlage ohne Multiplex- oder Feldrückleselogik.

## Holdoutstand 2088

Eine dritte, vorab per Hash festgelegte Reihenfolge desselben 81-Welten-Bestands
bildet die Komponenten blind, bevor die 2087-Relationen eingelesen werden. Eine
große alterskontinuierliche Breitenschicht enthält 12 der früheren 19
Relationen deutlich über Zufall. Der geschlossene 19er-Verbund erscheint nicht
erneut; vom vollständigen Vierer-Profilverbund bleibt nur eine überzufällige
Teilkante.

Damit trägt die Ereigniszeit eine reihenfolgenrobuste Bewegungsschicht, aber
noch keinen ausreichend bestimmten Multiplexkern. Die Ereignis-Memory bleibt
passiv und wird nicht zur Auswahl, Feldänderung oder Handlung zurückgelesen.

## Daten-Holdoutstand 2089

In 64 neuen realen `30m`-Welten bildet sich blind erneut eine große
alterskontinuierliche Breitenschicht. Ihre Relationsidentitäten stimmen jedoch
weder mit dem kleinen 2087-Verbund noch mit der großen 2088-Komponente
statistisch belastbar überein.

Die Ereigniszeit trägt damit die erneute Entstehung von Zusammenhang, nicht
die dauerhafte Identität seiner Mitglieder. Es wird weiterhin keine Komponente
gespeichert oder zurückgelesen. Insbesondere erzeugt der Befund keine feste
Klasse, kein Gate und keine Feld- oder Handlungswirkung.

## Lebenslaufanschluss 2090

Die Eigenzeit dient nun als einzige Quelle einer nachgelagerten passiven
Relationsnachbarschaft. Nur vollständig beobachtete Relationen gleichen Alters
werden anhand ihrer Breitenbewegung verglichen. Ihre gegenseitigen nächsten
Nachbarschaften werden kompakt gespeichert, aber nicht in die Ereigniszeit
zurückgelesen.

Der 64-Welten-Replay erhält alle 10.092 bisherigen Relationsereignisse
bytegleich. Die Ereignis-Memory bleibt damit Quelle des Lebenslaufs, nicht sein
Produkt und nicht sein Steuerobjekt.

## Kausaler Zustandsstand 2096

Ein reiner Vorwärtsrekonstruktor liest bei jeder Welt nur den bis dahin
vorhandenen Ereignispräfix. In Entwicklungsbestand und unabhängigem Holdout
rekonstruiert er alle 124 Lebenslaufpräfixe sowie sämtliche
Synchronisationspaar-Alter exakt und ohne Zukunftszugriff.

Damit ist die Relationsereigniszeit innerhalb dieser passiven relationalen
Ebene der hinreichende Quellzustand. Lebenslauf und Synchronisation sind
ableitbare Ansichten; eine zusätzliche Zustands-Memory würde dieselbe
Erfahrung duplizieren. Es entsteht weder eine Zustandsklasse noch eine
Rücklesung.

## Übergangstopologiestand 2097

Aufeinanderfolgende Ereignisse derselben Relation verbinden ihre
Weltpräfixänderungen gerichtet. Viele Relationen teilen in Entwicklungsbestand
und unabhängigem Holdout dieselben Übergänge und Zweischrittpfade deutlich
häufiger als unter relationseigener Gap-Neuordnung und einer pro Welt
aktivitätserhaltenden Ereignisnull.

Diese Zustandsübergangstopologie benötigt keine Zustandsklasse und keine neue
Speicherung. Sie bleibt aus der Ereignis-Memory rekonstruierbar. Einzelne
stärkste Pfade werden nicht bevorzugt und es entsteht noch keine Rücklesung.

## Erwartungsgrenze 2098

Ein strikt kausaler Vorwärtstest verwendet nach jedem Relationsereignis nur
den gerade bekannten Gap und die bis dahin abgeschlossenen Gap-Übergänge. In
beiden Beständen ordnet diese konditionierte Erfahrung den nächsten Gap
schlechter ein als die globale bisherige Gap-Häufigkeit. Ihr Vorteil gegenüber
der dünnen Einzelhistorie wird durch die Kontrollen erklärt.

Die Übergangstopologie bleibt damit retrospektive Ordnung, nicht Erwartung.
Die Ereignis-Memory erhält keinen Prognosewert, kein Gate und keine
Rücklesung.

## Kollektiver Kadenztransfer 2099

Die globale Gap-Häufigkeit eines unabhängigen Bestands ordnet die Gaps des
anderen Bestands in beiden Richtungen besser ein als dessen erst wachsende
Eigenhäufigkeit. Der Vorteil liegt in allen zehn Asset-Jahr-Herkünften vor und
fast vollständig in der frühen Zielerfahrung. Nach weiterer Erfahrung erreicht
das Ziel praktisch dieselbe kollektive Kadenz.

Damit trägt die Ereigniszeit übertragbare Kaltstarterfahrung, ohne eine feste
Reifeschwelle oder Mischungsregel zu benötigen. Eine kumulative Nutzung in der
Runtime ist noch nicht geprüft; es entsteht keine Rücklesung.

## Kumulative Grenze 2100

Die ungewichtete Addition jedes neuen Zielgaps zur eingefrorenen Fremderfahrung
verbessert deren Score nur um rund 0,013 bis 0,014 Prozentpunkte. Der Effekt
trägt nicht in beiden Vorzeichentests, ist nicht in allen Herkunftsgruppen
positiv und liegt vollständig innerhalb einer Ziel-Gap-Labelkontrolle.

Eine aktive Kadenznutzung würde damit zusätzliche Mischungs-, Vergessens- oder
Umschaltlogik benötigen. Diese ist nicht organisch aus der Erfahrung getragen.
Die Ereignis-Memory erhält keine Erwartungsrücklesung; der Zweig endet ohne
neue Mechanik.

## Synthesegrenze 2101

Die korrigierte Kette 2091 bis 2100 trägt die Relationsereigniszeit als
kausalen Quellzustand einer beweglichen relationalen Eigenordnung. Lebenslauf,
Synchronisation, Übergangstopologie und kollektive Gap-Kadenz sind daraus
ableitbare Ansichten. Keine dieser Ansichten trägt eine robuste stabile
Semantik, eine wachsende Erwartung oder eine direkte Feld- und
Handlungswirkung.

Deshalb bleibt die Ereignis-Memory unverändert. Es entstehen weder ein
paralleler Zustandsspeicher noch feste Identitäten, Schwellen, Gewichte,
Mischungsregeln oder eine Rücklesung. Der Eigenzeit-Erwartungszweig ist damit
methodisch abgeschlossen.

## Selbstabweichungsgrenze 2102

Die drei ungewichteten Stützachsen jeder Relation bilden nach jeder
Weltfinalisierung neue Pareto-Schichten. Mehr als drei Viertel der vorhandenen
Relationspositionen wechseln dabei ihre Schicht. Diese starke Plastizität
liegt in Entwicklungsbestand und unabhängigem Holdout jedoch vollständig in
einer Null, die Weltaktivität, Ereignisalter und jede individuelle
Stütztrajektorie exakt erhält.

Die konkrete Zuordnung zwischen Relation und Ereigniszeit trägt daher keinen
robusten Zusatz zur globalen Pareto-Umbildung. Die Ereignis-Memory erhält
weder einen Selbstabweichungs- oder Neuheitswert noch eine Rücklesung.
