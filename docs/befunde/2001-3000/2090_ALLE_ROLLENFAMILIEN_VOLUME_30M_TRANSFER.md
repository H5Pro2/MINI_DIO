# 2090 - Familienabhängige Volumenrichtung im 30m-Transfer

## Zweck

Befund 2089 zeigt auf zwei 5m-Holdouts positive Ereignisanteil-Antworten für `rf_05`, `rf_07`, `rf_08` und negative für `rf_17`, `rf_21`. Dieser Lauf prüft diese fünf Richtungen vorab auf den bereits vorhandenen 30m-Welten aus Befund 2081.

## Vorab festgelegtes Design

- zwölf 30m-Realwelten aus 2024 und 2025
- BTC und SOL
- 36 vorhandene Volumenphasenkontrollen mit Offsets `17`, `83`, `251`
- fünf Gruppen: Gesamt, beide Jahre und beide Assets
- pro Familie und Gruppe 100 größen- und häufigkeitsgematchte Pseudo-Familien
- positive Erwartung für `rf_05`, `rf_07`, `rf_08`
- negative Erwartung für `rf_17`, `rf_21`
- strenge Replikation nur bei `5/5` passenden Gruppenvorzeichen und Gesamt-Nullperzentil mindestens `0.950` in erwarteter Richtung
- `rf_06`, `rf_10`, `rf_13` bleiben explorativ
- keine neuen Welten, keine Memory-Erweiterung und keine Runtime-Wirkung

## Primäre Richtungen

| Familie | erwartet | Vorzeichenpfad G/24/25/BTC/SOL | passende Gruppen | Gesamt Δ Ereignisanteil | Nullperzentil | repliziert |
|---|---:|---|---:|---:|---:|---:|
| `rf_05` | 1 | `1;1;1;1;1` | 5/5 | 0.0040 | 1.000 | 1 |
| `rf_07` | 1 | `1;1;1;1;1` | 5/5 | 0.0042 | 1.000 | 1 |
| `rf_08` | 1 | `-1;-1;1;-1;0` | 1/5 | -0.0001 | 0.515 | 0 |
| `rf_17` | -1 | `-1;-1;-1;-1;-1` | 5/5 | -0.0007 | 0.040 | 1 |
| `rf_21` | -1 | `-1;-1;1;1;-1` | 3/5 | -0.0012 | 0.000 | 0 |

## Explorative Familien

| Familie | Vorzeichenpfad | Gesamt Δ Ereignisanteil | Nullperzentil | Persistenz |
|---|---|---:|---:|---:|
| `rf_06` | `-1;-1;-1;-1;-1` | -0.0011 | 0.000 | 1.000 |
| `rf_10` | `-1;-1;-1;-1;-1` | -0.0006 | 0.030 | 1.000 |
| `rf_13` | `1;1;1;1;-1` | 0.0003 | 0.595 | 0.600 |

## Synthese über drei Holdouts

| Familie | positiv/negativ/null | Mittel | Holdout-Vorzeichen | Persistenz | mittleres Nullperzentil |
|---|---:|---:|---|---:|---:|
| `rf_05` | 15/0/0 | 0.0043 | `1;1;1` | 1.000 | 1.000 |
| `rf_06` | 1/14/0 | -0.0015 | `-1;-1;-1` | 0.867 | 0.156 |
| `rf_07` | 15/0/0 | 0.0030 | `1;1;1` | 1.000 | 0.953 |
| `rf_08` | 11/3/1 | 0.0005 | `-1;1;1` | 0.533 | 0.756 |
| `rf_10` | 3/12/0 | -0.0006 | `-1;-1;-1` | 0.600 | 0.211 |
| `rf_13` | 5/10/0 | -0.0003 | `1;-1;-1` | 0.333 | 0.328 |
| `rf_17` | 0/15/0 | -0.0013 | `-1;-1;-1` | 1.000 | 0.070 |
| `rf_21` | 2/13/0 | -0.0020 | `-1;-1;-1` | 0.733 | 0.051 |

## Befund

Von fünf vorab gerichteten Familien replizieren `3/5` streng auf 30m.

Geschlossen tragen `rf_05;rf_07;rf_17`; nicht geschlossen übertragen sich `rf_08;rf_21`. Damit besitzt die familienabhängige Ereignisrichtung einen zeitebenenübergreifenden Kern, aber keine vollständige Invarianz aller 5m-Profile.

Über alle drei Holdouts bleiben `rf_05` und `rf_07` in `15/15` Gruppen positiv, `rf_17` in `15/15` negativ. Diese drei Richtungen wiederholen sich auf 5m und 30m. `rf_08` und `rf_21` tragen dagegen Zeitebenen- beziehungsweise Gruppendrift.

Explorativ liegen `rf_06;rf_10` auf 30m in allen fünf Gruppen negativ und am unteren Rand ihrer Pseudo-Verteilungen. Da diese Richtung nicht vorab festgelegt war, bleibt sie Kandidat und keine Replikation.

Der Transfer prüft die Richtung des Familienereignisanteils, nicht eine vollständige dreiachsige Familienform. Kontinuität und Mitgliederabdeckung bleiben in der Achsendatei sichtbar, werden aber nicht nachträglich zu Primärzielen erklärt.

## Grenze

Die 30m-Welten erweitern die Zeitebene, bleiben aber bei BTC/SOL, denselben Jahren, derselben Fensterlänge und derselben zirkulären Volumenphasenoperation. Gruppenwerte überlappen in ihrer Weltbasis und sind keine fünf unabhängigen Experimente. Pseudo-Details bleiben lokal.
