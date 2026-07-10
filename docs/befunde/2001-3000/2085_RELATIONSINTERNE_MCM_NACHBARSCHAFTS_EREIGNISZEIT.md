# 2085 - Relationsinterne MCM-Nachbarschafts-Ereigniszeit

## Zweck

Befund 2084 zeigte, dass fünf globale Checkpoints für belastbare
Reifungsbewegungen zu grob sind. Diese Prüfung ersetzt den vorgegebenen
Messtakt nicht durch ein dichteres festes Raster. Stattdessen erhält jede
gewachsene MCM-Nachbarschaft ihre eigene Ereigniszeit.

Ein Ereignis entsteht genau dann, wenn die Relation beim Abschluss einer Welt
erneut gegenseitige Nachbarschaftsevidenz erhält. Dieser Vorgang existiert
bereits im Wachstumsmechanismus und erhöht `growth_seen_count`. Es wird kein
zusätzlicher Auslöser programmiert.

## Passive Integration

Jedes Ereignis bewahrt sieben innere Ganzzahlen:

1. Index des abgeschlossenen inneren Weltlaufs,
2. Weltpaartragung der Relation,
3. Zahl getragener Weltläufe,
4. bisherige Zahl eigener Bestätigungsereignisse,
5. Tragung im Feldkernprofil,
6. Tragung im vollständigen Feldprofil,
7. Tragung im standardisierten Profil mit Episodendauer.

Der erste Vektor ist absolut, alle folgenden Vektoren enthalten nur exakte
Differenzen zum vorherigen Relationsereignis. Weltlabel, Chartwerte,
Außenweltklassen und Handlungsgrößen werden nicht gespeichert.

Die Ebene liegt getrennt unter
`passive_mcm_neighborhood_event_memory`. Sie wird beim vorhandenen
Nachbarschaftswachstum nur beschrieben und von Feld, Wahrnehmung, Gate,
Aktionswahl und Motorik nicht gelesen.

## Feldäquivalenz

Dieselben 81 archivierten Welten wachsen erneut vorwärts und rückwärts. Die
Endgraphen werden relationsweise gegen Befund 2081 geprüft.

| Folge | Relationen | Relationsabweichungen | Trägerabweichungen | Tiefenabweichungen |
|---|---:|---:|---:|---:|
| vorwärts | 2.046 | 0 | 0 | 0 |
| rückwärts | 2.085 | 0 | 0 | 0 |

Zusätzlich gilt für jede einzelne Relation:

- Ereigniszahl entspricht exakt `growth_seen_count`,
- letzter Ereigniszeitpunkt entspricht exakt `last_finalization`,
- letzter Stand aller sechs Tragungswerte entspricht exakt dem aktuellen
  Relationsstand.

In beiden Folgen gibt es dabei null Abweichungen. Die Eigenzeit verändert das
weitere Feld- und Nachbarschaftswachstum nicht.

## Entstehende Eigenzeit

| Folge | Relationen | Ereignisse | Relationen mit mindestens zwei Ereignissen | Maximum |
|---|---:|---:|---:|---:|
| vorwärts | 2.046 | 11.780 | 1.215 | 79 |
| rückwärts | 2.085 | 11.712 | 1.155 | 78 |

Der Median liegt in beiden Folgen bei zwei Ereignissen. Gleichzeitig tragen
331 vorwärts und 334 rückwärts gewachsene Beziehungen mindestens zehn eigene
Bestätigungen. Die Memory bildet damit nicht nur fünf globale Beobachtungen ab,
sondern 23.492 tatsächlich von den Relationen selbst ausgelöste Zeitpunkte.

## Stabilität Und Individualisierung

Die 1.935 gemeinsamen Relationsidentitäten zeigen eine deutliche Stabilität
der Ereignisbreite:

- Ereigniszahl-Spearman: `0,804264`,
- mindestens zwei Ereignisse in beiden Folgen: 991 Relationen,
- exakt gleiche Ereigniszahl: 842 Relationen.

Die genaue Bahn wird mit wachsender Erfahrung individueller:

| Mindestereignisse bei gleicher Ereigniszahl | vergleichbare Relationen | exakt gleicher altersbezogener Verlauf | Anteil |
|---:|---:|---:|---:|
| 1 | 842 | 654 | 77,67 % |
| 2 | 226 | 71 | 31,42 % |
| 3 | 105 | 10 | 9,52 % |
| 5 | 54 | 0 | 0,00 % |
| 10 | 27 | 0 | 0,00 % |
| 20 | 13 | 0 | 0,00 % |

Die Eigenzeit reproduziert also die Breite der Reifung deutlich besser als den
exakten Detailpfad. Das ist kein Grund für eine feste Familie: Längere
Relationsbiografien bleiben erfahrungsabhängig.

## Speicherwirkung

| Folge | Basis 2081 | Memory 2085 | Mehrbedarf | Ereigniszweig |
|---|---:|---:|---:|---:|
| vorwärts | 12.057.026 Byte | 14.186.286 Byte | 2.129.260 Byte / 17,66 % | 1.768.301 Byte |
| rückwärts | 12.119.957 Byte | 14.249.293 Byte | 2.129.336 Byte / 17,57 % | 1.769.379 Byte |

Die vollständigen 23.492 expandierten Forschungsereignisse umfassen als CSV
2.404.092 Byte. Im deterministischen ZIP-Archiv benötigen sie zusammen mit
dem Manifest 274.993 Byte. Es werden daher keine losen Ereignisdateien und
keine Runtime-Memories in das Repository übernommen.

## Befund

Getragen sind:

- eine schwellenfreie Eigenzeit jeder bestätigten Beziehung,
- vollständige und kompakte Ereigniserhaltung,
- exakte Feldäquivalenz zur ereignislosen Referenz,
- deutliche reihenfolgenübergreifende Stabilität der Ereignisbreite,
- zunehmende Individualisierung längerer Relationsbiografien.

Nicht getragen sind:

- feste Reifungsfamilien aus identischen Langzeitverläufen,
- eine vorgegebene optimale Ereigniszahl,
- Löschen, Dämpfen oder Bevorzugen einzelner Erfahrungen,
- Rücklesen der Eigenzeit in das MCM-Feld,
- Bedeutung oder Handlung aus der Ereignisbahn.

Die relationsinterne Ereigniszeit ist damit eine organischere passive
Gedächtnisgrundlage als globale Festintervalle. Sie beschreibt, wann eine
Beziehung aus eigener Evidenz weitergewachsen ist, ohne daraus bereits eine
Wirkung zu machen.

## Reproduzierbare Ausgaben

- `2085_RELATIONSINTERNE_MCM_NACHBARSCHAFTS_EREIGNISZEIT.equivalence.csv`
- `2085_RELATIONSINTERNE_MCM_NACHBARSCHAFTS_EREIGNISZEIT.coverage.csv`
- `2085_RELATIONSINTERNE_MCM_NACHBARSCHAFTS_EREIGNISZEIT.order.csv`
- `2085_RELATIONSINTERNE_MCM_NACHBARSCHAFTS_EREIGNISZEIT.length.csv`
- `2085_RELATIONSINTERNE_MCM_NACHBARSCHAFTS_EREIGNISZEIT.summary.csv`
- `data/2085_mcm_neighborhood_event_histories.zip`

Extrahierte Welten, Debugdaten und vollständige Runtime-Memories bleiben lokal
und werden nach der Prüfung entfernt.
