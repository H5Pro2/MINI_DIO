# 2079 - Rollenfamilien gegen größen- und häufigkeitsgematchte Pseudo-Familien

## Zweck

Befund 2078 ließ drei gerichtete Phasenachsen über Gesamtprofil, 1h und 15m gleichgerichtet zurück. Dieser Lauf prüft, ob diese Achsen über die konkrete relationale Familienzugehörigkeit hinausgehen oder bereits durch Mitgliederzahl und Quellhäufigkeit entstehen können.

## Vorab Festgelegtes Design

- keine neuen Weltläufe und keine neuen Kontrollwelten
- wiederverwendetes 2025-Holdoutarchiv: `data/2078_role_family_phase_profile_holdout.zip`
- für jede der acht Familien `100` Pseudo-Familien
- exakt gleiche Mitgliederzahl
- vollständig disjunkt von den Mitgliedern der jeweiligen realen Familie
- deterministische Auswahl der 100 nächstliegenden Quellhäufigkeitsprofile
- Matching über sortierte logarithmische Mitgliedshäufigkeiten und Gesamthäufigkeit
- dieselben zwölf Realwelten und `144` Phasenkontrollen wie in 2078
- Primärachsen aus 2078: `rf_08:sign`, `rf_10:sign`, `rf_10:magnitude`
- keine neue Klasse, keine Handlung, kein Gate und keine Richtung

Die Nullverteilung wird nicht durch einen festen Grenzwert in bestätigt oder verworfen geteilt. Ausgegeben werden die Lage des realen Effekts innerhalb der 100 gematchten Pseudo-Familien und die Häufigkeit derselben kategorialen Antwort.

## Matching-Qualität

| Familie | Mitglieder | mittlere Distanz | Median Häufigkeitsverhältnis |
|---|---:|---:|---:|
| `rf_05` | 8 | 0.2312 | 0.983 |
| `rf_06` | 8 | 0.5210 | 1.345 |
| `rf_07` | 2 | 2.3540 | 0.318 |
| `rf_08` | 2 | 0.5013 | 1.026 |
| `rf_10` | 2 | 0.5239 | 0.902 |
| `rf_13` | 3 | 0.1446 | 1.003 |
| `rf_17` | 2 | 0.4520 | 1.047 |
| `rf_21` | 2 | 1.1486 | 0.679 |

## Primärachsen

Perzentile geben die Lage des realen Differenzwerts innerhalb der gematchten Pseudo-Familien an.

| Ebene | Achse | reales Profil | Pseudo gleich | Δ Kontinuität Perzentil | Δ Ereignisanteil Perzentil | Δ Abdeckung Perzentil |
|---|---|---|---:|---:|---:|---:|
| `overall` | `rf_08:sign` | `verstaerkt` | 13/100 | 0.900 | 0.920 | 0.930 |
| `overall` | `rf_10:sign` | `abgeschwaecht` | 54/100 | 0.450 | 0.370 | 0.370 |
| `overall` | `rf_10:magnitude` | `abgeschwaecht` | 45/100 | 0.360 | 0.360 | 0.290 |
| `timeframe:1h` | `rf_08:sign` | `verstaerkt` | 24/100 | 0.670 | 0.740 | 0.705 |
| `timeframe:1h` | `rf_10:sign` | `abgeschwaecht` | 52/100 | 0.590 | 0.170 | 0.450 |
| `timeframe:1h` | `rf_10:magnitude` | `abgeschwaecht` | 33/100 | 0.220 | 0.110 | 0.170 |
| `timeframe:15m` | `rf_08:sign` | `verstaerkt` | 9/100 | 0.990 | 0.990 | 0.985 |
| `timeframe:15m` | `rf_10:sign` | `abgeschwaecht` | 39/100 | 0.390 | 0.530 | 0.330 |
| `timeframe:15m` | `rf_10:magnitude` | `abgeschwaecht` | 45/100 | 0.550 | 0.490 | 0.430 |

## Alle Familienachsen

| Familie | Komponente | reales Profil | Pseudo gleich | Kontinuitätsperzentil |
|---|---|---|---:|---:|
| `rf_05` | `sign` | `abgeschwaecht` | 88/100 | 0.120 |
| `rf_05` | `magnitude` | `gemischt` | 1/100 | 0.980 |
| `rf_05` | `wick` | `gemischt` | 15/100 | 0.390 |
| `rf_05` | `volume` | `verstaerkt` | 0/100 | 0.980 |
| `rf_06` | `sign` | `abgeschwaecht` | 95/100 | 0.970 |
| `rf_06` | `magnitude` | `verstaerkt` | 3/100 | 0.990 |
| `rf_06` | `wick` | `abgeschwaecht` | 72/100 | 0.710 |
| `rf_06` | `volume` | `abgeschwaecht` | 50/100 | 0.000 |
| `rf_07` | `sign` | `gemischt` | 48/100 | 0.610 |
| `rf_07` | `magnitude` | `gemischt` | 36/100 | 0.510 |
| `rf_07` | `wick` | `gemischt` | 59/100 | 0.580 |
| `rf_07` | `volume` | `gemischt` | 54/100 | 0.610 |
| `rf_08` | `sign` | `verstaerkt` | 13/100 | 0.900 |
| `rf_08` | `magnitude` | `verstaerkt` | 26/100 | 0.920 |
| `rf_08` | `wick` | `verstaerkt` | 20/100 | 0.730 |
| `rf_08` | `volume` | `verstaerkt` | 29/100 | 0.940 |
| `rf_10` | `sign` | `abgeschwaecht` | 54/100 | 0.450 |
| `rf_10` | `magnitude` | `abgeschwaecht` | 45/100 | 0.360 |
| `rf_10` | `wick` | `abgeschwaecht` | 50/100 | 0.560 |
| `rf_10` | `volume` | `gemischt` | 23/100 | 0.540 |
| `rf_13` | `sign` | `verstaerkt` | 18/100 | 0.810 |
| `rf_13` | `magnitude` | `abgeschwaecht` | 44/100 | 0.000 |
| `rf_13` | `wick` | `abgeschwaecht` | 45/100 | 0.260 |
| `rf_13` | `volume` | `gemischt` | 31/100 | 0.530 |
| `rf_17` | `sign` | `abgeschwaecht` | 50/100 | 0.000 |
| `rf_17` | `magnitude` | `abgeschwaecht` | 32/100 | 0.130 |
| `rf_17` | `wick` | `abgeschwaecht` | 45/100 | 0.220 |
| `rf_17` | `volume` | `abgeschwaecht` | 31/100 | 0.020 |
| `rf_21` | `sign` | `gemischt` | 44/100 | 0.550 |
| `rf_21` | `magnitude` | `gemischt` | 42/100 | 0.670 |
| `rf_21` | `wick` | `gemischt` | 56/100 | 0.500 |
| `rf_21` | `volume` | `gemischt` | 60/100 | 0.240 |

## Befund

Von den drei vorab festgelegten Achsen bleibt nur `rf_08:sign` im Gesamtprofil gegenüber den gematchten Pseudo-Familien auffällig: dieselbe Verstärkung tragen `13/100`, die drei Primärmaße liegen auf den Perzentilen `0.900`, `0.920` und `0.930`.

Dieser Abstand ist zeitebenengebunden. Auf `1h` tragen `24/100` Pseudo-Familien dieselbe Antwort und die Perzentile liegen nur zwischen `0.670` und `0.740`. Auf `15m` tragen nur `9/100` dieselbe Verstärkung; alle drei Perzentile liegen zwischen `0.985` und `0.990`. Damit bleibt kein allgemeiner Familienmarker, sondern ein möglicher `rf_08`-Vorzeichen-Kopplungseffekt im 15m-Kontext.

Die beiden `rf_10`-Achsen werden durch die Pseudo-Kontrolle nicht als familienspezifisch getragen. Bei Vorzeichen zeigen `54/100`, bei Körpergröße `45/100` dieselbe Abschwächung; ihre Gesamtperzentile liegen überwiegend im mittleren Bereich. Mitgliederzahl und Quellhäufigkeitsnähe reichen damit aus, um diese Antwort häufig hervorzubringen.

Explorativ fällt `rf_05:volume` auf. Diese Achse gehörte wegen fehlender Zeitebenenstabilität nicht zum Primärvergleich, liegt insgesamt aber bei `0/100` gleichen Pseudo-Antworten und Perzentilen `0.980`, `1.000`, `1.000`. Auf `1h` liegen alle drei Maße zwischen `0.935` und `1.000`. Das ist ein nachgelagerter, kontextgebundener Kandidat und keine Bestätigung.

Der tragfähige Befund ist damit enger als 2078: Phasenantworten können aus Größe und Häufigkeitsprofil entstehen; nur einzelne Familien-Komponenten-Kontexte bleiben darüber hinaus auffällig. Diese Kontextbindung ist passive Evidenz für mögliche relationale Kopplung, aber noch keine stabile Familienindividualität, feste Bedeutung oder organische Runtime-Erweiterung.

## Grenze

Das Matching nähert Quellhäufigkeiten an, kann sie bei extremen Familienprofilen aber nicht identisch ersetzen. Pseudo-Familien verwenden denselben 29-Symbol-Pool und dieselben Marktwelten. Der Lauf trennt Familienzugehörigkeit von Größe und Häufigkeitsnähe, nicht von allen möglichen Eigenschaften der Symbolgeometrie oder Messpipeline.
