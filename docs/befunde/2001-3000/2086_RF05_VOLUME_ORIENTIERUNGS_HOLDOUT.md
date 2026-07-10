# 2086 - rf_05:volume Orientierungs-Holdout

## Zweck

Befund 2085 fand vier positive Kreuzkopplungen zwischen ungestörtem Familienzustand und Volumenphasenantwort. Dieser Lauf prüft genau diese Orientierung vorab in zwölf neuen, nicht überlappenden 5m-Fenstern.

## Vorab festgelegtes Design

- Datenjahre `2024` und `2025`
- Assets `BTC` und `SOL`
- neue Startpunkte `18000`, `54000`, `90000`
- zwölf Realwelten mit je `1000` Beobachtungen
- ausschließlich Volumenphase mit Offsets `17`, `83`, `251`
- 36 Phasenkontrollen in einem Weltarchiv
- dieselben 100 größen- und häufigkeitsgematchten Pseudo-Familien
- positive Richtung, signiertes Pseudo-Perzentil mindestens `0.950` und `4/4` Leave-one-path-Richtungsstabilität je Primärachse
- geschlossene Replikation nur bei `4/4` Primärachsen
- Weltarchiv: `data/2086_rf05_volume_orientation_holdout.zip`
- keine Memory-Erweiterung und keine Runtime-Rückwirkung

## Primäre Orientierungen

| Ausgangslage | Antwortachse | Spearman ρ | signiertes Perzentil | Pseudo gleiches Vorzeichen | LOO stabil | repliziert |
|---|---|---:|---:|---:|---:|---:|
| `baseline_continuity` | `delta_event_share` | -0.312 | 0.080 | 30/100 | 4/4 | 0 |
| `baseline_event_share` | `delta_continuity` | -0.198 | 0.330 | 65/100 | 3/4 | 0 |
| `baseline_event_share` | `delta_member_coverage` | -0.272 | 0.190 | 62/100 | 3/4 | 0 |
| `baseline_member_coverage` | `delta_event_share` | -0.358 | 0.120 | 33/100 | 4/4 | 0 |

## Vollständige Matrix

| Ausgangslage | Antwortachse | primär | Spearman ρ | Pseudo-Mittel | signiertes Perzentil | Betrag-Perzentil |
|---|---|---:|---:|---:|---:|---:|
| `baseline_continuity` | `delta_continuity` | 0 | -0.613 | -0.742 | 0.765 | 0.235 |
| `baseline_continuity` | `delta_event_share` | 1 | -0.312 | 0.193 | 0.080 | 0.550 |
| `baseline_continuity` | `delta_member_coverage` | 0 | -0.233 | -0.718 | 1.000 | 0.000 |
| `baseline_event_share` | `delta_continuity` | 1 | -0.198 | -0.093 | 0.330 | 0.590 |
| `baseline_event_share` | `delta_event_share` | 0 | -0.476 | -0.389 | 0.450 | 0.550 |
| `baseline_event_share` | `delta_member_coverage` | 1 | -0.272 | -0.077 | 0.190 | 0.780 |
| `baseline_member_coverage` | `delta_continuity` | 0 | -0.844 | -0.756 | 0.390 | 0.610 |
| `baseline_member_coverage` | `delta_event_share` | 1 | -0.358 | 0.114 | 0.120 | 0.610 |
| `baseline_member_coverage` | `delta_member_coverage` | 0 | -0.547 | -0.759 | 0.970 | 0.030 |

## Sekundäre Gesamtantwort

| Gruppe | erwartet/beobachtet | Pseudo gleich | Δ K/E/A | Perzentile K/E/A |
|---|---|---:|---:|---:|
| `overall` | `verstaerkt/gemischt` | 0/100 | -0.055/0.0032/-0.052 | 0.520/1.000/0.950 |
| `year:2024` | `verstaerkt/gemischt` | 1/100 | -0.048/0.0036/-0.035 | 0.580/1.000/0.940 |
| `year:2025` | `verstaerkt/gemischt` | 2/100 | -0.066/0.0028/-0.069 | 0.310/1.000/0.800 |
| `asset:BTC` | `verstaerkt/gemischt` | 4/100 | -0.077/0.0033/-0.042 | 0.100/1.000/0.915 |
| `asset:SOL` | `verstaerkt/gemischt` | 10/100 | -0.034/0.0031/-0.062 | 0.800/1.000/0.900 |

## Befund

Die vorab festgelegte Orientierungsordnung repliziert auf `0/4` Primärachsen; geschlossen: `0`.

Alle vier primären Rohkorrelationen sind im Holdout negativ: `1`. Die positive Kreuzorientierung aus 2085 ist damit keine unabhängige Invariante und begründet keine Kopplungsregel oder neue passive Beziehungsidentität.

Die bekannte Gesamtverstärkung erscheint in `0/5` Gruppen. Im Gesamtprofil lautet die Antwort `gemischt` bei `0/100` gleichen Pseudo-Antworten und den Perzentilen `0.520`, `1.000`, `0.950`.

Enger trägt nur der Ereignisanteil: Seine Antwort ist in allen fünf Gruppen positiv und liegt jeweils am Pseudo-Perzentil `1.000`. Gesamt steigt er um `0.0032`, während Kontinuität um `-0.055` und Mitgliederabdeckung um `-0.052` sinken. Die wiederkehrende Volumenphasensensitivität ist damit eher eine Umverteilung der Familienereignisse als eine allgemein verstärkende Familienform.

Die Orientierung und die aggregierte Verstärkung sind getrennte Ebenen. Eine Kreuzkopplung beschreibt, wie Ausgangslagen und Antwortachsen gemeinsam variieren; sie beweist weder Ursache noch feste Bedeutung und darf nicht als Schaltlogik gelesen werden.

## Grenze

Der Holdout erweitert die unabhängigen Fenster, bleibt aber bei BTC/SOL, 5m, derselben Fensterlänge und derselben Volumenphasenoperation. Die passive Antwort-Memory bleibt bei 217 Beobachtungen und 32 Identitäten, bis eine weitere organische Erweiterung getrennt begründet und geprüft ist.
