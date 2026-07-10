# 2091 - Passive Volumen-Antwort-Memory mit balancierter Evidenz

## Zweck

Befunde 2089 und 2090 gleichen die Volumenphasenevidenz aller acht Rollenfamilien über zwei 5m-Holdouts und einen 30m-Transfer an. Diese numerischen Beobachtungen werden nun provenancegetreu in die passive Antwort-Memory aufgenommen.

Bereits gespeicherte `rf_05`-Beobachtungen aus 2083 und 2086 sowie `rf_05`- und `rf_08`-Beobachtungen aus 2081 werden ausdrücklich nicht unter neuen Evidenznamen wiederholt. Die Quellsichten enthalten ausschließlich bisher fehlende Familien.

## Reifungsprofil

- Beobachtungen vorher/nachher: `222/322`
- Antwortidentitäten vorher/nachher: `32/32`
- eindeutige Beobachtungssymbole: `322`
- Evidenzquellen vorher/nachher: `5/8`
- Kontexte vorher/nachher: `16/16`
- neue Beobachtungen: `100`
- quellenreihenfolgenstabil: `1`
- doppelte Beobachtung abgewiesen: `1`
- passiv/handlungswirksam: `1/0`

## Provenienzquellen

| Quellsicht | neue Zeilen | ausgeschlossene bereits gespeicherte Familien |
|---|---:|---|
| `docs/befunde/2001-3000/2091_PASSIVE_VOLUME_ANTWORT_MEMORY_EVIDENZBALANCE.source_2083_5m.csv` | 35 | `rf_05` |
| `docs/befunde/2001-3000/2091_PASSIVE_VOLUME_ANTWORT_MEMORY_EVIDENZBALANCE.source_2086_5m.csv` | 35 | `rf_05` |
| `docs/befunde/2001-3000/2091_PASSIVE_VOLUME_ANTWORT_MEMORY_EVIDENZBALANCE.source_2081_30m.csv` | 30 | `rf_05;rf_08` |

## Volumenidentitäten vor und nach der Balance

| Familie | vorher Beobachtungen/Quellen | neu | nachher Beobachtungen/Quellen | Δ Ereignisanteil-Mittel | Ereignisanteil-Perzentil |
|---|---:|---:|---:|---:|---:|
| `rf_05` | 21/5 | 0 | 21/5 | 0.0043 | 1.000 |
| `rf_06` | 6/2 | 15 | 21/5 | -0.0014 | 0.134 |
| `rf_07` | 6/2 | 15 | 21/5 | 0.0031 | 0.943 |
| `rf_08` | 11/3 | 10 | 21/5 | 0.0005 | 0.770 |
| `rf_10` | 6/2 | 15 | 21/5 | -0.0005 | 0.221 |
| `rf_13` | 6/2 | 15 | 21/5 | -0.0002 | 0.356 |
| `rf_17` | 6/2 | 15 | 21/5 | -0.0012 | 0.058 |
| `rf_21` | 6/2 | 15 | 21/5 | -0.0015 | 0.076 |

## Organische Bedeutung

Alle acht Volumenidentitäten besitzen nun dieselbe Beobachtungs- und Quellentiefe. Positive, negative und driftende Ereignisrichtungen werden als numerische Erfahrung nebeneinander bewahrt. Die Balance erzeugt weder eine Rangordnung noch eine feste Familieneigenschaft.

Die 100 neuen Beobachtungen erweitern vorhandene Identitäten; sie erzeugen keine neue Antwortidentität. Gleiche Weltkontexte bleiben unterscheidbar über Evidenzherkunft und Beobachtungssymbol.

## Technische Grenze

Die Memory speichert keine Richtungsklasse, Replikationsmarke, Bedeutung oder Vorhersage. `read_by_mini_dio`, `influences_action`, `is_gate`, `is_motoric`, `is_entry_signal` und `is_direction_signal` bleiben `0`. Die lokale JSON-Memory bleibt ungetrackt.
