# 2089 - Alle Rollenfamilien unter balancierter Volumen-Evidenz

## Zweck

Befund 2088 zeigt, dass die meisten Antwortidentitäten deutlich flacher belegt sind als `rf_05:volume`. Dieser Lauf liest daher alle acht Rollenfamilien auf exakt denselben 2083- und 2086-Volumenwelten.

Jede Familie erhält zehn Gruppenbeobachtungen aus zwei unabhängigen Holdouts und wird in jedem Kontext gegen ihre 100 größen- und häufigkeitsgematchten Pseudo-Familien gestellt. Es entstehen keine neuen Welten, keine neue Memory-Evidenz und keine Runtime-Wirkung.

## Ereignisanteil im Gleichstand der Evidenz

| Familie | positiv/negativ/null | Mittel | Holdout-Mittelpfad | Holdout-Vorzeichen | Persistenz | mittleres Nullperzentil | Persistenzperzentil |
|---|---:|---:|---|---|---:|---:|---:|
| `rf_05` | 10/0/0 | 0.0045 | `0.005701;0.003214` | `1;1` | 1.000 | 1.000 | 0.688 |
| `rf_06` | 1/9/0 | -0.0017 | `-0.001090;-0.002319` | `-1;-1` | 0.800 | 0.234 | 0.250 |
| `rf_07` | 10/0/0 | 0.0024 | `0.002180;0.002571` | `1;1` | 1.000 | 0.929 | 0.688 |
| `rf_08` | 10/0/0 | 0.0008 | `0.000699;0.000838` | `1;1` | 1.000 | 0.871 | 0.688 |
| `rf_10` | 3/7/0 | -0.0006 | `-0.001006;-0.000168` | `-1;-1` | 0.400 | 0.280 | 0.062 |
| `rf_13` | 1/9/0 | -0.0007 | `-0.000168;-0.001174` | `-1;-1` | 0.800 | 0.219 | 0.250 |
| `rf_17` | 0/10/0 | -0.0016 | `-0.001174;-0.002040` | `-1;-1` | 1.000 | 0.034 | 0.688 |
| `rf_21` | 0/10/0 | -0.0024 | `-0.002040;-0.002850` | `-1;-1` | 1.000 | 0.026 | 0.688 |

## rf_05:volume über drei Achsen

| Achse | positiv/negativ/null | Mittel | Holdout-Vorzeichen | Persistenz | mittleres Nullperzentil |
|---|---:|---:|---|---:|---:|
| `continuity` | 3/7/0 | -0.0211 | `1;-1` | 0.400 | 0.726 |
| `event_share` | 10/0/0 | 0.0045 | `1;1` | 1.000 | 1.000 |
| `member_coverage` | 3/7/0 | -0.0226 | `1;-1` | 0.400 | 0.946 |

## Befund

Unter gleicher Evidenztiefe tragen `3/8` Familien zehn von zehn positive Ereignisanteil-Antworten; `3/8` besitzen positive Mittelwerte in beiden Holdouts.

`rf_05` erreicht `10/10` positive Ereignisanteil-Beobachtungen, Persistenz `1.000` und ein mittleres Nullperzentil von `1.000`. Sein Persistenzperzentil innerhalb der acht gleich tief vermessenen Familien beträgt `0.688`.

Die positive Richtung ist damit nicht exklusiv: `rf_07` und `rf_08` tragen ebenfalls zehn positive Antworten. `rf_05` besitzt jedoch den größten mittleren Zuwachs und den größten mittleren Abstand zur eigenen Pseudo-Verteilung; beide Maxima liegen bei `rf_05` beziehungsweise `rf_05`. Sein Nullabstandsperzentil innerhalb der acht Familien beträgt `0.938`.

Entgegengesetzt tragen `2/8` Familien zehn von zehn negative Ereignisanteil-Antworten: `rf_17;rf_21`. Dieselbe Volumenphasenlösung wirkt deshalb nicht allgemein verstärkend oder abschwächend, sondern wird von verschiedenen Familien in unterschiedliche Ereignisrichtungen aufgenommen.

Bei `rf_05` wechseln Kontinuität und Mitgliederabdeckung zwischen den Holdouts jeweils von positiv zu negativ (`1;-1` und `1;-1`). Nur der Ereignisanteil bleibt in beiden Holdouts positiv. Die wiederkehrende Achse und die kontextplastischen Achsen sind damit im gleichen Design getrennt sichtbar.

Eine gleichgerichtete Antwort ist nur dann familienbezogen auffällig, wenn neben der Vorzeichenbilanz auch der Abstand zur jeweiligen Pseudo-Verteilung trägt. Diese beiden Koordinaten bleiben getrennt und werden nicht zu einer Klasse verdichtet.

## Grenze

Die zehn Gruppenwerte je Familie stammen aus 24 Realwelten, nicht aus zehn unabhängigen Experimenten. Der Lauf balanciert Familien und Holdouts, erweitert aber weder Assets noch Zeitebene oder Phasenoperation. Alle Pseudo-Details bleiben lokal im Debugbereich.
