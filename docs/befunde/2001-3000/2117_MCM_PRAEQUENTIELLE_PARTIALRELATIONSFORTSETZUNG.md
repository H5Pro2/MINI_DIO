# 2117 - Praequentielle Fortsetzung partieller MCM-Relationen

## Zweck

Befund 2116 findet eine dichte partielle Relationsfortsetzung ueber
Rangzyklusgrenzen, aber keine quellgebundene Topologie. Quellidentitaet ist
jedoch nur ein rueckblickendes Kriterium. Eine innere Relation koennte fuer das
Feld relevant sein, wenn ihr aktueller Verlauf Information ueber die eigene
naechste Entwicklung traegt.

2117 prueft deshalb rein praequentiell:

```text
Setzt sich ein bereits mitgetragener Relationsslot
im naechsten Rangzyklus eher fort
als ein gleich erfahrener, aktuell neuer Slot?
```

## Kandidaten im aktuellen Zyklus

Pro Entscheidungspunkt werden nur gerichtete Relationsslots betrachtet, die
im aktuellen Rangzyklus aktiv sind.

Zwei Gruppen entstehen ausschliesslich aus Vergangenheit und Gegenwart:

- `mitgetragen`: derselbe Slot war auch im direkt vorherigen Zyklus aktiv,
- `neu aktiv`: der Slot ist aktuell aktiv, war im direkt vorherigen Zyklus
  jedoch nicht aktiv.

Erst danach wird gelesen, ob der jeweilige Slot im naechsten Zyklus wieder
aktiv ist. Die Zukunft beeinflusst weder Gruppenzuordnung noch Matching.

## Exaktes Erfahrungsmatching

Ein haeufiger Slot koennte allein wegen seiner allgemeinen Aktivitaet leichter
fortbestehen. Deshalb werden mitgetragene und neue Slots nur verglichen, wenn
sie bis einschliesslich des aktuellen Zyklus exakt gleich oft aufgetreten
sind.

Zwei Kontrollen werden getrennt:

1. `frequency`: gleiche bisherige Auftretenszahl im gesamten Feld,
2. `neuron_pair_and_frequency`: gleiche Auftretenszahl und dasselbe
   Neuronenpaar; nur die gerichtete Wechselart darf verschieden sein.

Die zweite Lesung ist die strenge Hauptkontrolle. Sie entfernt zusaetzlich
unterschiedliche Dynamik einzelner Neuronenpaare.

## Paarweiser Zukunftsvergleich

Innerhalb jedes exakten Matchingblocks werden alle mitgetragenen mit allen
neuen Slots verglichen:

- Mitgetragener Slot bleibt, neuer nicht: Sieg fuer Mittragen.
- Neuer Slot bleibt, mitgetragener nicht: Niederlage fuer Mittragen.
- Beide bleiben oder beide enden: Gleichstand.

Die praequentielle AUC zaehlt Siege mit `1`, Gleichstaende mit `0,5` und
Niederlagen mit `0`. Eine AUC ueber `0,5` waere Fortsetzungsvorteil; eine AUC
unter `0,5` bedeutet bevorzugte Abloesung des bereits mitgetragenen Slots.

Es gibt keinen Entscheidungsschwellwert, kein Lernen und keine Rueckwirkung.

## Vollstaendige Abdeckung

| Bestand | Stroeme | mit strengen Matches | Paare Minimum | Median | Maximum | Gesamtpaare |
|---|---:|---:|---:|---:|---:|---:|
| 2091-Bestand | 768 | 768 | 2 | 17 | 30 | 12.648 |
| 2092-Holdout | 704 | 704 | 3 | 16 | 35 | 12.212 |

Jeder kontinuierliche Strom traegt mindestens zwei streng frequenz- und
neuronenpaargematchte Zukunftsvergleiche. Der Befund ist nicht auf wenige
Sonderfaelle begrenzt.

## Breite Frequenzkontrolle

| Bestand | Universum | Vergleichspaare | AUC | Quellen ueber / unter 0,5 |
|---|---|---:|---:|---:|
| 2091 | alle | 157.273 | 0,491 | 4 / 44 |
| 2091 | A | 71.167 | 0,482 | 1 / 47 |
| 2091 | B | 86.106 | 0,499 | 15 / 33 |
| 2092 | alle | 145.922 | 0,492 | 5 / 39 |
| 2092 | A | 79.264 | 0,478 | 1 / 43 |
| 2092 | B | 66.658 | 0,509 | 43 / 1 |

Ohne Neuronenpaar-Matching ist die Richtung klein und im Holdout-Universum B
sogar umgekehrt. Gleiche Haeufigkeit allein kontrolliert die unterschiedliche
Paargeometrie somit nicht ausreichend.

## Strenge Neuronenpaar- und Frequenzkontrolle

| Bestand | Universum | Vergleichspaare | AUC | Quellen ueber / unter 0,5 | untere Sign-p |
|---|---|---:|---:|---:|---:|
| 2091 | alle | 12.648 | 0,451 | 0 / 48 | 3,55e-15 |
| 2091 | A | 6.717 | 0,463 | 0 / 48 | 3,55e-15 |
| 2091 | B | 5.931 | 0,437 | 0 / 48 | 3,55e-15 |
| 2092 | alle | 12.212 | 0,453 | 0 / 44 | 5,68e-14 |
| 2092 | A | 6.578 | 0,444 | 0 / 44 | 5,68e-14 |
| 2092 | B | 5.634 | 0,464 | 0 / 44 | 5,68e-14 |

Die Gegenrichtung ist vollstaendig:

- jede der 48 Quellen des Entwicklungsbestands liegt unter `0,5`,
- jede der 44 Holdoutquellen liegt unter `0,5`,
- dieselbe Richtung gilt in beiden disjunkten Zieluniversen,
- die quellenweise exakte Signkontrolle liegt weit unter jeder ueblichen
  Zufallsgrenze.

Mitgetragene gerichtete Wechsel setzen sich damit nicht bevorzugt fort. Sie
werden im naechsten Rangzyklus haeufiger von gleich erfahrenen, aktuell neuen
Wechseln desselben Neuronenpaares abgeloest.

## Sieg-, Gleichstands- und Verluststruktur

| Bestand | Siege Mittragen | Gleichstaende | Niederlagen Mittragen |
|---|---:|---:|---:|
| 2091 | 736 | 9.938 | 1.974 |
| 2092 | 424 | 10.221 | 1.567 |

Die meisten gematchten Paare enden gleich. Unter den richtungsentscheidenden
Vergleichen sind Niederlagen des mitgetragenen Slots jedoch in beiden
Bestaenden deutlich haeufiger als Siege.

## Interpretation

2116 zeigte dichte zyklusuebergreifende Kontinuitaet. 2117 zeigt nun, dass
diese Kontinuitaet keine einfache Traegheit bildet. Unter gleicher bisheriger
Erfahrung und demselben Neuronenpaar besitzt ein bereits wiederholter
gerichteter Wechsel eine geringere naechste Anschlusswahrscheinlichkeit als
ein aktuell neu aufgetretener Wechsel.

Das Feld traegt damit eine reproduzierbare innere Abloesungsordnung:

```text
Mittragen erzeugt keine unbegrenzte Selbstverstaerkung.
Fortgesetzte Relationsformen geben haeufiger Raum fuer neue Richtungsformen.
```

Diese Ordnung ist eine Form selbstbegrenzender Plastizitaet. Sie benoetigt
keine Quellenidentitaet, Marktgruppe oder externe Ergebnisbedeutung.

## Keine fertige Vorhersage oder Handlung

Die AUC wird nur nachtraeglich ueber viele gematchte Beobachtungen berechnet.
MINI_DIO berechnet im Feld keinen Score, waehlt keinen Slot aus und handelt
nicht danach.

Getragen ist eine populationsweit reproduzierbare praequentielle Beziehung
zwischen aktuellem Mittragsstatus und naechster Feldbeteiligung. Nicht
getragen ist ein individuelles Zukunftsversprechen fuer jeden Slot.

## Befund

Getragen sind:

- ein kausaler Vergleich ohne Zugriff auf den naechsten Zyklus,
- exaktes Matching bisheriger Slothaeufigkeit,
- eine strenge Kontrolle innerhalb desselben Neuronenpaares,
- vollstaendige Pfadabdeckung in beiden Bestaenden,
- AUC 0,437 bis 0,464 in beiden disjunkten Zieluniversen,
- dieselbe Abloserichtung in allen 92 Quellen,
- eine reproduzierbare selbstbegrenzende Relationsplastizitaet.

Nicht getragen sind:

- bevorzugte Fortsetzung bereits mitgetragener Relationsslots,
- unbegrenzte relationale Selbstverstaerkung,
- ein fertiger Online-Praediktor,
- ein bereits ausgewaehlter Relevanz- oder Bedeutungsknoten,
- Memory-Ruecklesung, Feldwirkung durch Lernen oder Handlung.

2117 findet erstmals auf der neuen Partialrelationsebene ein robustes rein
internes Zukunftssignal. Dieses Signal lautet nicht Persistenz, sondern
Abloesung: Wiederholt mitgetragene gerichtete Relationsformen haben unter
gleicher Erfahrung geringere naechste Anschlussfaehigkeit.

Damit entsteht ein mechanischer Kandidat fuer organische Selbstbegrenzung,
noch keine Semantik oder Entscheidungsregel.

## Reproduzierbare Ausgaben

- `2117_MCM_PRAEQUENTIELLE_PARTIALRELATIONSFORTSETZUNG.paths.csv`
- `2117_MCM_PRAEQUENTIELLE_PARTIALRELATIONSFORTSETZUNG.sources.csv`
- `2117_MCM_PRAEQUENTIELLE_PARTIALRELATIONSFORTSETZUNG.summary.csv`

Der Runner ist
`tools/run_mcm_prequential_partial_relation_continuation.py`. Er erzeugt keine
Welt-, Runtime-, Memory- oder Debugdateien.
