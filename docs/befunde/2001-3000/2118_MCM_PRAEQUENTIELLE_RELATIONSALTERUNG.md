# 2118 - Praequentielle Alterung getragener MCM-Relationen

## Zweck

Befund 2117 zeigt eine robuste innere Abloesungsordnung: Ein bereits aus dem
vorherigen Rangzyklus mitgetragener Relationsslot setzt sich seltener fort als
ein gleich erfahrener, aktuell neuer Slot desselben Neuronenpaares.

Offen blieb, ob dies nur den ersten Uebergang von neu zu mitgetragen betrifft
oder ob jede weitere ununterbrochene Tragedauer die naechste
Anschlusswahrscheinlichkeit weiter vermindert.

2118 prueft deshalb rein praequentiell:

```text
Besitzt eine aktuell aktive Relationsform eine kontinuierliche Lebenskurve,
bei der groesseres ununterbrochenes Alter ihre naechste Fortsetzung mindert?
```

## Exaktes Relationsalter

Das Alter eines gerichteten Relationsslots ist die Anzahl unmittelbar
aufeinanderfolgender Rangepisoden, in denen er bis einschliesslich der
aktuellen Episode aktiv ist.

- Eine neu aktive Form hat Alter `1`.
- Eine einmal mitgetragene Form hat Alter `2`.
- Jede weitere unmittelbar anschliessende Beteiligung erhoeht das Alter um
  genau eins.
- Eine inaktive Episode beendet die laufende Tragedauer. Eine spaetere
  Wiederkehr beginnt wieder bei Alter `1`.

Die beobachteten Alter werden nicht in Klassen eingeteilt. Im
Entwicklungsbestand reichen sie bis `26`, im Holdout bis `19`.

## Praequentielles Matching

In jeder aktuellen Episode werden nur aktive Slots verglichen, die

1. zum selben Neuronenpaar gehoeren,
2. bis einschliesslich der aktuellen Episode exakt gleich oft aktiv waren,
3. eine unterschiedliche ununterbrochene Tragedauer besitzen.

Damit bleibt die gesamte Erfahrung gleich. Nur ihre zeitliche Form ist
verschieden: Ein Slot traegt seine Erfahrung laenger zusammenhaengend, der
andere hat einen juengeren aktuellen Lauf mit frueheren Unterbrechungen.

Erst nach der Gruppierung wird die Folgeepisode gelesen. Bleibt nur der
aeltere Slot aktiv, ist dies ein Sieg fuer Alter; bleibt nur der juengere
aktiv, ist es eine Niederlage. Gleiche Ergebnisse bilden einen Gleichstand.

Die AUC zaehlt Siege mit `1`, Gleichstaende mit `0,5` und Niederlagen mit `0`.
Eine AUC unter `0,5` bedeutet geringere Fortsetzung des aelteren Slots.

## Vollstaendige Abdeckung

| Bestand | Stroeme | mit Vergleich | Paare Minimum | Median | Maximum | Gesamtpaare |
|---|---:|---:|---:|---:|---:|---:|
| 2091-Bestand | 768 | 768 | 2 | 38 | 82 | 30.105 |
| 2092-Holdout | 704 | 704 | 6 | 46 | 98 | 32.308 |

Jeder Strom traegt exakte gleich erfahrene Altersvergleiche. Der Test ist
nicht auf einzelne Quellen oder Sonderwelten begrenzt.

## Primaerer kontinuierlicher Altersrang

| Bestand | Universum | Paare | AUC aelter | Quellen ueber / unter 0,5 |
|---|---|---:|---:|---:|
| 2091 | alle | 30.105 | 0,482 | 0 / 48 |
| 2091 | A | 15.793 | 0,483 | 0 / 48 |
| 2091 | B | 14.312 | 0,480 | 0 / 48 |
| 2092 | alle | 32.308 | 0,474 | 0 / 44 |
| 2092 | A | 16.804 | 0,467 | 0 / 44 |
| 2092 | B | 15.504 | 0,481 | 0 / 44 |

Ueber alle ungleichen Alter erscheint zunaechst dieselbe Gegenrichtung wie in
2117. Jede Quelle beider Bestaende liegt unter `0,5`.

Dieser Gesamtwert beweist jedoch noch keine kontinuierliche Alterung. Er
enthaelt den bereits aus 2117 bekannten ersten Unterschied zwischen Alter `1`
und allen mitgetragenen Formen.

## Natuerliche Grenze nach dem ersten Mittragen

Die entscheidende Gegenprobe betrachtet nur Vergleiche, in denen auch der
juengere Slot bereits mitgetragen wurde. Beide Formen haben damit Alter
mindestens `2`; ihre exakten Alter bleiben weiterhin ungeklammert.

| Bestand | Universum | Paare | AUC aelter | Quellen ueber / unter / gleich 0,5 |
|---|---|---:|---:|---:|
| 2091 | alle | 17.457 | 0,504 | 36 / 3 / 9 |
| 2091 | A | 9.076 | 0,498 | 15 / 25 / 8 |
| 2091 | B | 8.381 | 0,510 | 43 / 3 / 2 |
| 2092 | alle | 20.096 | 0,486 | 0 / 44 / 0 |
| 2092 | A | 10.226 | 0,481 | 1 / 43 / 0 |
| 2092 | B | 9.870 | 0,491 | 0 / 43 / 1 |

Die Richtung uebertraegt nicht:

- Im Entwicklungsbestand verschwindet der Gesamteffekt.
- Zwischen dessen Universen A und B wechselt die Quellenrichtung deutlich.
- Im Holdout bleibt eine Gegenrichtung, ist aber nicht mit dem
  Entwicklungsbestand vereinbar.
- Die exakten spaeteren Alterspaare wechseln mehrfach zwischen unter, nahe
  und ueber `0,5`.

Damit liegt keine gemeinsame kontinuierliche Alterungs- oder Ermuedungskurve
vor.

## Der reproduzierte erste Erneuerungsuebergang

Der direkte Vergleich Alter `1` gegen Alter `2` reproduziert dagegen fast
identisch:

| Bestand | Exakte Alter | Paare | AUC aelter |
|---|---:|---:|---:|
| 2091 | 1 gegen 2 | 6.145 | 0,446 |
| 2092 | 1 gegen 2 | 6.026 | 0,447 |

Dies lokalisiert die robuste Ordnung aus 2117 enger. Die allgemein getragene
Mechanik ist kein fortlaufender Zerfall mit jedem weiteren Zyklus. Sie sitzt
am ersten Erneuerungsuebergang zwischen einer neu aktivierten und einer
unmittelbar erneut beteiligten Relationsform.

## Interpretation

2118 begrenzt 2117, ohne dessen Befund zu verwerfen:

```text
Das erste Mittragen veraendert die naechste Anschlussordnung robust.
Weiteres Alter erzeugt daraus keine universelle Lebenskurve.
```

Das Feld behandelt Neuaktivierung und unmittelbare Erneuerung verschieden.
Danach bleibt die Fortsetzung kontextabhaengig und kann nicht auf ein fixes
Relationsalter reduziert werden.

Die tragfaehige organische Lesung ist deshalb eine Erneuerungsgrenze, kein
Zaehler fuer Verfall und keine programmierte Lebensdauer. Ein System, das
Relationen allein wegen steigenden Alters abschwaecht oder loescht, waere
durch diese Befunde nicht fundiert.

## Keine Memory- oder Wirkungsregel

Der Altersrang wird nur fuer die nachgelagerte Forschungslesung berechnet.
MINI_DIO speichert keinen Alterswert im Feld, vergibt keine Lebensdauer,
veraendert keine Relation und waehlt keine Handlung danach aus.

Quellenbezeichnungen, Asset und Jahr werden nur nachtraeglich zur
Reproduktionskontrolle verwendet. Es gibt keinen Zukunftszugriff, keine feste
Altersklasse und keinen Entscheidungsschwellwert.

## Reproduzierbare Ausgaben

- `2118_MCM_PRAEQUENTIELLE_RELATIONSALTERUNG.paths.csv`
- `2118_MCM_PRAEQUENTIELLE_RELATIONSALTERUNG.sources.csv`
- `2118_MCM_PRAEQUENTIELLE_RELATIONSALTERUNG.summary.csv`
- `2118_MCM_PRAEQUENTIELLE_RELATIONSALTERUNG.exact_ages.csv`

Der Runner ist
`tools/run_mcm_prequential_relation_age_continuation.py`. Er erzeugt keine
Welt-, Runtime-, Memory- oder Debugdateien.
