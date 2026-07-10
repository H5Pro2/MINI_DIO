# 015 - Passiver MCM-Relationsnachbarschafts-Lebenslauf

## Aufgabe

Diese Ebene bewahrt, wie Beziehungen der passiven MCM-Nachbarschafts-Memory im
Verlauf ihrer eigenen Ereigniszeit Nachbarn bilden und wechseln. Sie übernimmt
keine Forschungsgruppe und kennt keine vorgegebenen Relationsmitglieder.

## Bildung

Nach Abschluss einer Welt werden zuerst die bestehenden
Nachbarschaftsrelationen und ihre Eigenzeitereignisse aktualisiert. Erst danach
arbeitet der Lebenslauf:

1. Er betrachtet nur vollständig beobachtete Relationen mit einem neuen
   Ereignis.
2. Er gruppiert sie mit allen anderen Relationen gleichen aktuellen Alters.
3. Er bildet ihre bisherige Bewegung aus dem Zuwachs von Weltpaarbreite und
   Weltbreite.
4. Er rankt jede Bewegungsposition innerhalb der gleichaltrigen Kohorte.
5. Er schreibt gegenseitige nächste Nachbarschaften als passive Beobachtung.

Zwei Ereignisse sind die strukturelle Mindestbedingung für eine Bewegung. Es
existieren keine weiteren festen Alters-, Distanz- oder Persistenzschwellen.

## Speicherung

```text
passive_mcm_relation_lifecycle_memory
  format = compressed_relation_neighbor_observation_chunks_v1
  symbols
  observation_chunks
    finalization_delta
    observation_count
    payload = zlib/base64(relation_age, left_index, right_index)
```

Jede Relation steht nur einmal in der Symboltabelle. Pro Finalisierung wird
höchstens ein append-only Block ergänzt. Das Format ist verlustfrei; die
diagnostische Lesung rekonstruiert daraus Kanten, Wiederkehr, spätere Alter und
Partnerbreite.

Nicht beobachtete Kanten werden weder gelöscht noch als gescheitert markiert.
Unvollständige Legacy-Eigenzeiten werden nicht rückwirkend erfunden und deshalb
nicht in Bewegungsvergleiche aufgenommen.

## Grenze

Die Ebene ist ausschließlich ein passiver Schreiber. MINI_DIO liest sie nicht
in Wahrnehmung, Feldmechanik, Aktionsbereitschaft oder Motorik zurück. Sie
speichert keine Komponenten, Klassen, Richtungen oder früheren
Forschungsmitglieder.

Der 64-Welten-Replay aus Befund 2090 bestätigt bytegleiche Relationsereignisse
und eine exakte Offline-Rekonstruktion aller 212.466 gespeicherten
Kantenbeobachtungen. Die zusätzliche Runtime-Struktur benötigt 903.742 Bytes.

## Eigenstabilitätsstand 2091

Eine rein nachgelagerte Prüfung vergleicht fortsetzungsfähige Kanten gleichen
Alters. Bereits beim vorherigen Alter getragene Kanten bestehen beim nächsten
Alter zu 37,12 Prozent fort, neue Kontakte zu 34,09 Prozent. Der relative
Vorsprung von 8,87 Prozent bleibt sowohl unter altersstratifizierter
Kantenlabel-Null als auch bei relationsweiser Permutation des vollständigen
Zukunftsgraphen überzufällig.

Diese Eigenstabilität wird nicht in die Mechanik zurückgelesen. Der Lebenslauf
bewahrt weiterhin Beobachtungen ohne Gewichtung, Auswahl oder Verstärkung.

## Holdoutstand 2092

In 60 unabhängigen realen `5m`-Welten aus DOGE, PAXG und XRP erscheint die
Richtung erneut, aber schwächer. Getragene Kanten setzen sich zu 36,72 Prozent,
neue Kontakte zu 35,04 Prozent fort. Die Relationsidentität bleibt gegenüber
einer graphstrukturerhaltenden Null überzufällig; die primäre
altersstratifizierte Labelkontrolle erreicht mit `p = 0,064` die festgelegte
Grenze von 0,05 nicht.

Der Stand ist deshalb eine Teilreplikation. Es wird weder ein Stabilitätswert
gespeichert noch ein Reifealter, eine Gewichtung oder eine Rückwirkung ergänzt.

## Methodische Korrektur 2093

Die Fortsetzungsvergleiche 2091 und 2092 setzten das spätere Erreichen des
nächsten Alters mit einer gemeinsamen Gelegenheit gleich. Die exakte
Ereigniszeit zeigt jedoch, dass eine Relation dieses Alter häufig bereits
wieder verlassen hatte, bevor die zweite dort eintraf. Nach Entfernung dieser
Schein-Gelegenheiten bleibt im Entwicklungsbestand kein
herkunftsstratifiziert belastbarer Vorteil; im unabhängigen Holdout ist die
Richtung leicht negativ.

Damit ist keine übertragbare Eigenstabilität getragen. Unverändert gültig
bleibt nur der passive, exakt rekonstruierbare Lebenslauf. Die Mechanik erhält
keinen Stabilitätswert und keine Rückwirkung.

## Synchronisationsstand 2094

Aus denselben Ereignisfinalisierungen lässt sich ohne zusätzliche Speicherung
rekonstruieren, wann zwei Relationen dasselbe Eigenalter gleichzeitig
besitzen. Diese Synchronisationspaare behalten in Entwicklungsbestand und
unabhängigem Holdout ihre konkrete Identität deutlich häufiger, als die
jeweilige Graphform allein erwarten lässt. Gleichzeitig wechseln pro
Altersübergang ungefähr 45 bis 48 Prozent der Partner.

Damit trägt die Ereigniszeit einen wiederkehrenden, aber beweglichen
Synchronisationsrahmen. Er wird nicht als Gruppe, Gewicht oder neue
Memory-Ebene festgeschrieben und bleibt ohne Rückwirkung.

## Kopplungsgrenze 2095

Bewegungsnachbarschaften liegen im Rohvergleich etwas häufiger auf später
erhaltenen Synchronisationspaaren. Wird jedoch die vollständige Graphform des
nächsten Synchronisationsalters bewahrt und nur ihre Relationsidentität
permutiert, liegt der beobachtete Abstand mitten in der Null. Eine besondere
Identitätskopplung zwischen Synchronisation und Bewegung ist damit nicht
getragen.

Die beiden Ebenen werden weder zusammengeführt noch gewichtet. Insbesondere
entsteht keine Multiplexklasse und keine neue Rücklesung.
