# 2080 - rf_08:sign im gematchten Crossyear-Kontrast

## Zweck

Befund 2079 ließ `rf_08:sign` nur im 15m-Kontext deutlich außerhalb größen- und häufigkeitsgematchter Pseudo-Familien zurück. Dieser Lauf wendet dieselbe Nullkontrolle auf die vorhandenen 2024-Welten an und prüft, ob die 15m-Bindung über das Jahr hinweg wiederkehrt.

## Vorab Festgelegtes Design

- keine neuen Weltläufe und keine neuen Kontrollwelten
- wiederverwendetes 2024-Phasenarchiv: `data/2076_rf05_component_phase_controls.zip`
- exakt dieselben 800 Pseudo-Familien wie in 2079: `docs/befunde/2001-3000/2079_ROLLENFAMILIEN_GEMATCHE_PSEUDOFAMILIEN.definitions.csv`
- Primärachse: `rf_08:sign`
- vorab erwarteter Kontrast: größerer Abstand zur Pseudo-Verteilung auf 15m als auf 1h
- Gesamtprofil, 1h und 15m werden getrennt ausgewiesen
- `rf_05:volume` bleibt explorativ und zählt nicht zur Primärprüfung
- keine neue Klasse, keine Handlung, kein Gate und keine Richtung

## Primärachse Über Beide Jahre

| Jahr | Ebene | reales Profil | Pseudo gleich | Δ Kontinuität Perzentil | Δ Ereignisanteil Perzentil | Δ Abdeckung Perzentil |
|---|---|---|---:|---:|---:|---:|
| 2024 | `overall` | `verstaerkt` | 11/100 | 0.980 | 0.990 | 1.000 |
| 2024 | `timeframe:1h` | `verstaerkt` | 16/100 | 0.970 | 0.840 | 0.970 |
| 2024 | `timeframe:15m` | `verstaerkt` | 12/100 | 0.900 | 0.970 | 0.910 |
| 2025 | `overall` | `verstaerkt` | 13/100 | 0.900 | 0.920 | 0.930 |
| 2025 | `timeframe:1h` | `verstaerkt` | 24/100 | 0.670 | 0.740 | 0.705 |
| 2025 | `timeframe:15m` | `verstaerkt` | 9/100 | 0.990 | 0.990 | 0.985 |

## Explorative rf_05-Volumenachse

| Jahr | Ebene | reales Profil | Pseudo gleich | Δ Kontinuität Perzentil | Δ Ereignisanteil Perzentil | Δ Abdeckung Perzentil |
|---|---|---|---:|---:|---:|---:|
| 2024 | `overall` | `verstaerkt` | 0/100 | 1.000 | 1.000 | 1.000 |
| 2024 | `timeframe:1h` | `verstaerkt` | 3/100 | 1.000 | 1.000 | 0.975 |
| 2024 | `timeframe:15m` | `verstaerkt` | 0/100 | 1.000 | 1.000 | 1.000 |
| 2025 | `overall` | `verstaerkt` | 0/100 | 0.980 | 1.000 | 1.000 |
| 2025 | `timeframe:1h` | `verstaerkt` | 16/100 | 1.000 | 1.000 | 0.935 |
| 2025 | `timeframe:15m` | `gemischt` | 88/100 | 0.750 | 1.000 | 0.980 |

## Alle 2024-Familienachsen

| Familie | Komponente | reales Profil | Pseudo gleich | Kontinuitätsperzentil |
|---|---|---|---:|---:|
| `rf_05` | `sign` | `abgeschwaecht` | 72/100 | 0.090 |
| `rf_05` | `magnitude` | `verstaerkt` | 8/100 | 1.000 |
| `rf_05` | `wick` | `verstaerkt` | 0/100 | 1.000 |
| `rf_05` | `volume` | `verstaerkt` | 0/100 | 1.000 |
| `rf_06` | `sign` | `abgeschwaecht` | 97/100 | 0.120 |
| `rf_06` | `magnitude` | `gemischt` | 58/100 | 0.710 |
| `rf_06` | `wick` | `gemischt` | 21/100 | 0.000 |
| `rf_06` | `volume` | `abgeschwaecht` | 23/100 | 0.000 |
| `rf_07` | `sign` | `gemischt` | 20/100 | 0.630 |
| `rf_07` | `magnitude` | `gemischt` | 24/100 | 0.560 |
| `rf_07` | `wick` | `gemischt` | 52/100 | 0.670 |
| `rf_07` | `volume` | `gemischt` | 48/100 | 0.590 |
| `rf_08` | `sign` | `verstaerkt` | 11/100 | 0.980 |
| `rf_08` | `magnitude` | `verstaerkt` | 35/100 | 0.980 |
| `rf_08` | `wick` | `verstaerkt` | 16/100 | 0.900 |
| `rf_08` | `volume` | `verstaerkt` | 16/100 | 0.940 |
| `rf_10` | `sign` | `abgeschwaecht` | 44/100 | 0.300 |
| `rf_10` | `magnitude` | `abgeschwaecht` | 26/100 | 0.020 |
| `rf_10` | `wick` | `abgeschwaecht` | 24/100 | 0.000 |
| `rf_10` | `volume` | `abgeschwaecht` | 29/100 | 0.030 |
| `rf_13` | `sign` | `gemischt` | 26/100 | 0.820 |
| `rf_13` | `magnitude` | `abgeschwaecht` | 24/100 | 0.080 |
| `rf_13` | `wick` | `gemischt` | 51/100 | 0.530 |
| `rf_13` | `volume` | `abgeschwaecht` | 46/100 | 0.470 |
| `rf_17` | `sign` | `abgeschwaecht` | 46/100 | 0.000 |
| `rf_17` | `magnitude` | `abgeschwaecht` | 28/100 | 0.190 |
| `rf_17` | `wick` | `abgeschwaecht` | 34/100 | 0.350 |
| `rf_17` | `volume` | `abgeschwaecht` | 45/100 | 0.010 |
| `rf_21` | `sign` | `abgeschwaecht` | 43/100 | 0.040 |
| `rf_21` | `magnitude` | `gemischt` | 30/100 | 0.520 |
| `rf_21` | `wick` | `abgeschwaecht` | 14/100 | 0.210 |
| `rf_21` | `volume` | `abgeschwaecht` | 2/100 | 0.320 |

## Befund

Der vorab erwartete stärkere 15m-Abstand repliziert 2024 nicht. Auf 1h tragen `16/100`, auf 15m `12/100` Pseudo-Familien dieselbe `rf_08:sign`-Antwort. Die 1h-Perzentile liegen zwischen `0.840` und `0.970`, die 15m-Perzentile zwischen `0.900` und `0.970`. `rf_08:sign` ist 2024 somit auf beiden Zeitebenen auffällig.

Der breitere Familienabstand wiederholt sich dagegen. Im 2024-Gesamtprofil tragen `11/100` dieselbe Verstärkung bei Perzentilen `0.980`, `0.990`, `1.000`; 2025 sind es `13/100` bei `0.900`, `0.920`, `0.930`. Das stützt eine wiederkehrende familienbezogene Vorzeichen-Phasenantwort gegenüber identischen alternativen Mitgliedschaften. Ihre genaue Verteilung auf Zeitebenen ist jedoch jahresabhängig.

Explorativ ist `rf_05:volume` noch deutlicher: In beiden Gesamtjahren tragen `0/100` beziehungsweise `0/100` Pseudo-Familien dieselbe Verstärkung. 2024 liegen alle drei Perzentile bei `1.000`; 2025 bei `0.980`, `1.000`, `1.000`. Da diese Achse erst nach 2079 ausgewählt wurde und 2025 auf 15m gemischt bleibt, ist sie ein vorab zu prüfender Kandidat und keine Bestätigung.

Der Crossyear-Befund trägt damit eine mögliche Familien-Komponenten-Kopplung, aber keine feste Zeitebenenbindung. Auch der wiederkehrende Abstand bleibt passive Evidenz und wird nicht als Familienbedeutung, Handlung oder neue Feldregel gespeichert. Eine organische Erweiterung ist noch nicht begründet.

## Grenze

Beide Jahre verwenden BTC/SOL, dieselben Fensterlängen, dieselben Phasenoperationen und denselben Symbolpool. Der Lauf prüft Jahreswiederkehr innerhalb dieser Messgeometrie, nicht Modalitätsunabhängigkeit, Kausalität oder allgemeine Feldintelligenz.
