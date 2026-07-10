# 2085 - rf_05:volume zwischen Feldzustand und Antwort

## Zweck

Befund 2084 zeigt eine kollektive Volumenphasenantwort über zwölf 5m-Fenster. Dieser Lauf prüft explorativ, ob die kontinuierliche Antwort mit dem jeweils ungestörten Familienzustand gekoppelt ist.

Verglichen werden drei Ausgangsachsen - Kontinuität, Familienereignisanteil und Mitgliederabdeckung - mit drei Antwortdifferenzen nach gelöster Volumenphase. Jede Rangkopplung von `rf_05` wird gegen dieselbe Kopplung in 100 größen- und häufigkeitsgematchten Pseudo-Familien gestellt.

## Kopplungsmatrix

| Ausgangslage | Antwortachse | Spearman ρ | Pseudo-Mittel | signiertes Perzentil | Betrag-Perzentil | Pseudo gleiches Vorzeichen | LOO-Pfade gleiches Vorzeichen |
|---|---|---:|---:|---:|---:|---:|---:|
| `baseline_continuity` | `delta_continuity` | -0.490 | -0.470 | 0.495 | 0.505 | 97/100 | 4/4 |
| `baseline_continuity` | `delta_event_share` | 0.538 | -0.250 | 1.000 | 0.845 | 17/100 | 4/4 |
| `baseline_continuity` | `delta_member_coverage` | -0.430 | -0.484 | 0.620 | 0.380 | 98/100 | 4/4 |
| `baseline_event_share` | `delta_continuity` | 0.616 | -0.358 | 1.000 | 0.900 | 7/100 | 4/4 |
| `baseline_event_share` | `delta_event_share` | -0.039 | -0.332 | 0.930 | 0.030 | 96/100 | 2/4 |
| `baseline_event_share` | `delta_member_coverage` | 0.575 | -0.384 | 1.000 | 0.780 | 8/100 | 4/4 |
| `baseline_member_coverage` | `delta_continuity` | -0.574 | -0.478 | 0.350 | 0.650 | 98/100 | 4/4 |
| `baseline_member_coverage` | `delta_event_share` | 0.481 | -0.249 | 1.000 | 0.800 | 16/100 | 4/4 |
| `baseline_member_coverage` | `delta_member_coverage` | -0.535 | -0.514 | 0.550 | 0.450 | 99/100 | 4/4 |

## Befund

Die gegenüber den gematchten Familien ungewöhnlichste Kopplung verläuft von `baseline_event_share` zu `delta_continuity`. Sie trägt `ρ = 0.616` bei einem Betrag-Perzentil von `0.900` und behält ihr Vorzeichen in `4/4` Leave-one-path-Prüfungen.

Insgesamt erreichen `0/9` Kopplungen explorativ mindestens das Betrag-Perzentil `0.950`; davon bleiben `0` beim Weglassen jedes einzelnen Asset-Jahr-Pfads vorzeichenstabil. Diese Zahlen sind eine Beschreibung des vorhandenen Feldes, keine Schwellenwerte für MINI_DIO.

Gleichzeitig liegen `4/9` Kopplungen am äußersten Rand der signierten Pseudo-Verteilung und bleiben in allen vier Leave-one-path-Prüfungen gleichgerichtet. Es sind kreuzweise positive Verbindungen: Ausgangskontinuität zu Ereignisanteil-Antwort, Ausgangsereignisanteil zu Kontinuitäts- und Abdeckungsantwort sowie Ausgangsabdeckung zu Ereignisanteil-Antwort. Ihre Pseudo-Mittel sind jeweils negativ. `rf_05` trägt hier keine stärkere Kopplung als die Alternativfamilien, sondern eine andere Orientierung zwischen den Achsen.

Die drei gleichnamigen Eigenachsen bleiben negativ und gegenüber den Pseudo-Familien gewöhnlich. Das passt zur rechnerischen Selbstkopplung von Ausgangswert und Differenz; die mögliche Besonderheit liegt nicht dort, sondern in der kreuzweisen Antwortordnung.

Eine negative Kopplung zwischen Ausgangswert und Differenz kann bereits rechnerisch entstehen, weil die Antwort als `Kontrolle minus Realzustand` gebildet wird. Der Pseudo-Familien-Vergleich begrenzt diese Selbstkopplung: Nur ein ungewöhnlicher Abstand zu deren Korrelationsverteilung spricht für eine familienbezogene Form, nicht für Kausalität oder Bedeutung.

## Organische Grenze

Der Lauf fügt keine Klasse, Gewichtung, Schwelle oder Wenn-Dann-Regel hinzu. Er erzeugt keine neue unabhängige Evidenz und vergrößert die passive Memory nicht. Die Kopplungen bleiben kontinuierliche Forschungswerte aus denselben zwölf Fenstern von 2083.
