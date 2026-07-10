# 2090 - Passiver MCM-Relationsnachbarschafts-Lebenslauf

## Zweck

Befund 2089 zeigte in neuen realen Welten erneut eine große
alterskontinuierliche Breitenschicht, aber keine stabile Übernahme ihrer alten
Relationsmitglieder. Das Feld bewahrt damit eher die Fähigkeit zur Bildung von
Zusammenhang als eine feste innere Objektklasse.

2090 integriert diese Grenze. MINI_DIO erhält keine frühere Komponente und
keine ausgewählte Relation. Stattdessen bewahrt eine neue passive Ebene, welche
Beziehungen bei gleichem selbst erreichtem Relationsalter gegenseitige
Nachbarn ihrer Breitenbewegung waren.

## Organisches Bildungsprinzip

Eine Beziehung kommt nur dann in Betracht, wenn ihre bestehende
Nachbarschafts-Memory tatsächlich ein neues Eigenzeitereignis erhalten hat.
Verglichen werden ausschließlich Beziehungen mit:

- vollständig beobachteter Eigenzeit ohne erfundene Rückfüllung,
- gleichem aktuellem Relationsalter,
- mindestens zwei eigenen Ereignissen und damit mindestens einer Bewegung.

Aus den Änderungen von `world_pair_count` und `world_count` entsteht für jede
Beziehung ihre bisherige Breitenbewegung. Jede Bewegungsposition wird innerhalb
der gleichaltrigen Kohorte gerankt. Eine Kante entsteht nur, wenn zwei
Beziehungen gegenseitig nächste Nachbarn sind. Exakte Gleichstände bleiben
sichtbar.

Es gibt dabei:

- keine feste Distanzschwelle,
- keine vorgegebenen Mitglieder,
- keine Altersliste wie 3, 5 oder 10,
- keine gespeicherte Komponente oder Klasse,
- keine Negativmarkierung für eine nicht erneut beobachtete Kante.

Gespeichert wird nur ein positives Kantenereignis, an dem mindestens eine in
dieser Finalisierung gewachsene Beziehung beteiligt ist. Wiederkehr und
Umbildung ergeben sich später aus der eigenen Beobachtungsfolge.

## Kompakte Datenstruktur

Eine erste Objektstruktur pro Kante erwies sich angesichts der großen Zahl
früher Kontakte als zu breit und wurde nicht übernommen. Die endgültige Memory
verwendet eine append-only Symboltabelle und einen komprimierten Block je
Finalisierung:

```text
passive_mcm_relation_lifecycle_memory
  format = compressed_relation_neighbor_observation_chunks_v1
  symbols
    [relation_symbol, ...]
  observation_chunks
    finalization_delta
    observation_count
    payload
      relation_age
      left_relation_index
      right_relation_index
```

Der Payload besteht aus festen ganzzahligen Tripeln, wird verlustfrei mit zlib
komprimiert und als Base64 im JSON-Dokument gespeichert. Die Relationstexte
stehen nur einmal in der Symboltabelle. Alle Kanten, Alter und
Finalisierungszeitpunkte sind exakt rekonstruierbar.

## Harte passive Grenze

```text
passive_only = 1
relation_event_derived_only = 1
read_by_mini_dio = 0
influences_field = 0
influences_action = 0
deletes_memory = 0
dampens_memory = 0
stores_components = 0
uses_fixed_members = 0
uses_distance_threshold = 0
is_gate = 0
is_motoric = 0
is_entry_signal = 0
is_direction_signal = 0
```

Der Schreibpfad liegt nach dem bestehenden Relationsereignis. Es gibt keinen
Lesepfad zurück in Wahrnehmung, MCM-Feldwirkung oder Handlung.

## Exakter 64-Welten-Replay

Die 64 realen `30m`-Welten aus Befund 2089 werden in exakt derselben
Hash-Reihenfolge erneut durchlaufen.

| Integritätsprüfung | Ergebnis |
|---|---:|
| Reihenfolge bytegleich | ja |
| bestehende Ereignisintegrität | exakt |
| 10.092 Relationsereignisse bytegleich zu 2089 | ja |
| gespeicherte Lebenslaufbeobachtungen | 212.466 |
| offline erwartete Beobachtungen | 212.466 |
| fehlende Beobachtungen | 0 |
| unerwartete Beobachtungen | 0 |

Die neue Ebene verändert damit weder Relationsmenge noch Eigenzeitverlauf. Eine
unabhängige Offline-Rekonstruktion aus den Relationsereignissen erzeugt exakt
dieselben Lebenslaufkanten.

## Gewachsene Lebenslaufstruktur

| Merkmal | Wert |
|---|---:|
| beteiligte Relationen | 1.203 |
| unterschiedliche Kanten | 184.300 |
| Kantenbeobachtungen | 212.466 |
| wiederkehrende Kanten | 22.801 |
| nur einmal beobachtete Kanten | 161.499 |
| Relationen mit mehreren Partnern | 1.188 |
| höchstes beobachtetes Relationsalter | 52 |

`87,63 %` der Kanten bleiben einmalige Kontakte, `12,37 %` kehren bei einem
späteren Relationsalter wieder. Von den beteiligten Relationen besitzen
`98,75 %` im Verlauf mehr als einen Partner. Die Topologie ist daher stark
beweglich und nicht kernzentriert.

Auch zeitlich liegt der Schwerpunkt früh:

- Alter 2: 164.239 Beobachtungen oder `77,30 %`,
- Alter 3: 32.465 Beobachtungen oder `15,28 %`,
- Alter 2 und 3 gemeinsam: `92,58 %`,
- ab Alter 10: 1.355 Beobachtungen oder `0,64 %`.

Frühe Kontaktbreite ist häufig, lang getragene Nachbarschaft dagegen selten.
Die Memory schreibt beide gleichwertig und legt keine Reifeschwelle fest.

## Speichergrenze

| Dokument | Bytes |
|---|---:|
| 2089-Memory ohne Lebenslauf | 14.343.282 |
| 2090-Memory mit Lebenslauf | 15.251.405 |
| Lebenslaufebene allein | 903.742 |

Die zusätzliche Ebene erhöht das Gesamtdokument um rund `6,33 %`. Das
veröffentlichte Diagnosearchiv ist 3.648.944 Bytes groß; die Runtime-Memory
speichert nicht die ausführliche CSV, sondern nur die komprimierten Blöcke.

## Befund

Getragen sind:

- vorgabenfreie Kantenbildung aus eigenen Relationsereignissen,
- verlustfreie Beobachtung von Entstehung, Wiederkehr und Partnerwechsel,
- eine stark bewegliche frühe Topologie mit kleinem wiederkehrendem Anteil,
- exakte Rückwirkungsfreiheit gegenüber der bestehenden Feld- und Eigenzeit,
- eine kompakte append-only Speicherung ohne Kantenobjektflut.

Nicht getragen sind:

- feste semantische Mitglieder oder Komponenten,
- eine Deutung einmaliger Kontakte als Fehler oder Tod,
- eine bevorzugte Altersstufe,
- Auswahl, Dämpfung oder Löschung von Erinnerung,
- Feld-, Wahrnehmungs- oder Handlungswirkung.

2090 überführt damit erstmals die in 2089 beobachtete Umbildungsfähigkeit in
eine wachsende Runtime-Struktur. Sie ist noch keine Feldintelligenz, bewahrt
aber eine notwendige Grundlage: Beziehungen können ihre eigenen
Nachbarschaftsverläufe bilden, wiederholen und verändern, ohne dass ihre Rollen
vorprogrammiert werden.

## Reproduzierbare Ausgaben

- `2090_PASSIVE_MCM_RELATIONSNACHBARSCHAFT_LEBENSLAUF.integrity.csv`
- `2090_PASSIVE_MCM_RELATIONSNACHBARSCHAFT_LEBENSLAUF.ages.csv`
- `2090_PASSIVE_MCM_RELATIONSNACHBARSCHAFT_LEBENSLAUF.recurrence.csv`
- `2090_PASSIVE_MCM_RELATIONSNACHBARSCHAFT_LEBENSLAUF.partners.csv`
- `2090_PASSIVE_MCM_RELATIONSNACHBARSCHAFT_LEBENSLAUF.summary.csv`
- `data/2090_mcm_relation_lifecycle_events.zip`

Das ZIP enthält nur die ausführlichen Kantenbeobachtungen und die
Weltreihenfolge. Extrahierte Welten, Debugdaten und Laufzeit-Memory bleiben
lokal und werden nach dem Lauf entfernt.
