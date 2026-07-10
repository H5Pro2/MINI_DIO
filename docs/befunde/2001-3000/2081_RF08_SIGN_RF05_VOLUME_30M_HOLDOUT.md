# 2081 - rf_08:sign und rf_05:volume im unabhängigen 30m-Holdout

## Zweck

Befund 2080 ließ zwei mögliche Familien-Komponenten-Kopplungen zurück. Dieser Lauf prüft beide vorab auf einer bisher ungenutzten 30m-Zeitebene und gegen dieselben größen- und häufigkeitsgematchten Pseudo-Familien.

## Vorab Festgelegtes Design

- Datenjahre `2024` und `2025`
- Assets `BTC` und `SOL`
- ausschließlich die bisher ungenutzte Zeitebene `30m`
- Startpunkte `0`, `6000`, `12000` je Asset und Jahr
- zwölf Realwelten mit je `1000` Beobachtungen
- Komponenten ausschließlich `sign` und `volume`
- feste Offsets `17`, `83`, `251`
- `72` gezielte Phasenkontrollen statt eines vollständigen Vier-Komponenten-Satzes
- exakt dieselben gematchten Pseudo-Familien wie 2079 und 2080
- Weltarchiv: `data/2081_role_family_30m_phase_holdout.zip`
- vorab erwartete Antworten: `rf_08:sign = verstaerkt`, `rf_05:volume = verstaerkt`
- keine neue Klasse, keine Handlung, kein Gate und keine Richtung

## Primärvergleich

| Gruppe | Achse | erwartet/beobachtet | Pseudo gleich | Δ Kontinuität Perzentil | Δ Ereignisanteil Perzentil | Δ Abdeckung Perzentil |
|---|---|---|---:|---:|---:|---:|
| `overall` | `rf_05:volume` | `verstaerkt/verstaerkt` | 3/100 | 1.000 | 1.000 | 1.000 |
| `year:2024` | `rf_05:volume` | `verstaerkt/verstaerkt` | 0/100 | 1.000 | 1.000 | 1.000 |
| `year:2025` | `rf_05:volume` | `verstaerkt/verstaerkt` | 41/100 | 1.000 | 1.000 | 0.825 |
| `asset:BTC` | `rf_05:volume` | `verstaerkt/verstaerkt` | 16/100 | 1.000 | 1.000 | 1.000 |
| `asset:SOL` | `rf_05:volume` | `verstaerkt/verstaerkt` | 0/100 | 1.000 | 1.000 | 1.000 |
| `overall` | `rf_08:sign` | `verstaerkt/verstaerkt` | 11/100 | 0.840 | 0.840 | 0.865 |
| `year:2024` | `rf_08:sign` | `verstaerkt/gemischt` | 25/100 | 0.610 | 0.870 | 0.600 |
| `year:2025` | `rf_08:sign` | `verstaerkt/verstaerkt` | 19/100 | 0.870 | 0.840 | 0.910 |
| `asset:BTC` | `rf_08:sign` | `verstaerkt/verstaerkt` | 25/100 | 0.720 | 0.835 | 0.740 |
| `asset:SOL` | `rf_08:sign` | `verstaerkt/gemischt` | 21/100 | 0.820 | 0.830 | 0.785 |

## Gekreuzte Sekundärachsen

| Gruppe | Achse | beobachtet | Pseudo gleich | Kontinuitätsperzentil |
|---|---|---|---:|---:|
| `overall` | `rf_05:sign` | `gemischt` | 31/100 | 0.900 |
| `year:2024` | `rf_05:sign` | `gemischt` | 68/100 | 1.000 |
| `year:2025` | `rf_05:sign` | `gemischt` | 91/100 | 0.070 |
| `asset:BTC` | `rf_05:sign` | `gemischt` | 76/100 | 0.780 |
| `asset:SOL` | `rf_05:sign` | `gemischt` | 23/100 | 0.810 |
| `overall` | `rf_08:volume` | `abgeschwaecht` | 57/100 | 0.490 |
| `year:2024` | `rf_08:volume` | `abgeschwaecht` | 50/100 | 0.200 |
| `year:2025` | `rf_08:volume` | `verstaerkt` | 19/100 | 0.830 |
| `asset:BTC` | `rf_08:volume` | `abgeschwaecht` | 55/100 | 0.370 |
| `asset:SOL` | `rf_08:volume` | `gemischt` | 26/100 | 0.580 |

## Befund

`rf_05:volume` repliziert die vorab erwartete Verstärkung auf 30m. Im Gesamtprofil tragen nur `3/100` Pseudo-Familien dieselbe Antwort; Kontinuität, Ereignisanteil und Abdeckung liegen jeweils am Perzentil `1.000`. 2024 sind es `0/100` bei drei Perzentilen `1.000`; 2025 `41/100` bei `1.000`, `1.000`, `0.825`.

Der Effekt ist nicht auf ein Asset begrenzt. BTC trägt `16/100` gleiche Antworten, SOL `0/100`; auf beiden Assetgruppen liegen alle drei realen Maße am Perzentil `1.000`. Zusammen mit 2079 und 2080 ist dies eine vorab festgelegte Replikation auf einer neuen Zeitebene gegenüber größen- und häufigkeitsgematchten Alternativmitgliedschaften.

`rf_08:sign` repliziert auf 30m nicht gleichwertig. Das Gesamtprofil ist zwar verstärkt, aber nur bei Perzentilen `0.840`, `0.840`, `0.865`. 2024 und SOL wechseln mit `gemischt` beziehungsweise `gemischt` aus der erwarteten gemeinsamen Verstärkung. Seine bisherige Evidenz bleibt damit zeitebenenabhängig.

Der robuste `rf_05`-Befund bedeutet nicht, dass reale Volumenkopplung die Familie trägt. Die zirkuläre Volumenverschiebung löst die relative Phase und verstärkt anschließend die Familienlesung. Belegt ist daher eine wiederkehrende, familienbezogene Volumen-Phasensensitivität beziehungsweise Plastizität, keine feste Volumenbedeutung und keine bevorzugte Handlungsrichtung.

Dieser Befund reicht erstmals aus, eine kleine organische Erweiterung der passiven Memory fachlich zu begründen: kontinuierliche Familien-Komponenten-Antwortvektoren samt Weltkontext und Nullabstand können als Erfahrung gespeichert werden. Er rechtfertigt weiterhin keine automatische Runtime-Regel, Handlung oder fest codierte Sonderbehandlung von `rf_05`.

## Grenze

Der Lauf erweitert die Zeitebene, bleibt aber bei BTC/SOL, Marktzeitreihen, derselben Fensterlänge, denselben Phasenoperationen und demselben Symbolpool. Er prüft Übertragbarkeit auf 30m, nicht andere Sinnesmodalitäten, Kausalität oder allgemeine Feldintelligenz.
