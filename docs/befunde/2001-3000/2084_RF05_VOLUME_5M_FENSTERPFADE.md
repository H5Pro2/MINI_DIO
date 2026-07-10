# 2084 - rf_05:volume als 5m-Fensterpfad

## Zweck

Befund 2083 repliziert `rf_05:volume` im 5m-Gesamtprofil, während 2024 und BTC achsengemischt bleiben. Diese Diagnose zerlegt exakt dieselben zwölf Realfenster und 36 Volumenphasenkontrollen, um die innere Verteilung der Antwort sichtbar zu machen.

Der Lauf ist keine neue Holdout-Evidenz. Er wiederverwendet die Welten aus 2083, erzeugt keine neue Memory-Beobachtung und verändert keine Runtime.

## Fensterantworten

| Asset | Jahr | Start | Antwort | Pseudo gleich | Δ Kontinuität | Δ Ereignisanteil | Δ Abdeckung | Perzentile K/E/A |
|---|---:|---:|---|---:|---:|---:|---:|---:|
| `BTC` | 2024 | 0 | `verstaerkt` | 0/100 | 0.027 | 0.0040 | 0.042 | 1.000/1.000/1.000 |
| `BTC` | 2024 | 36000 | `gemischt` | 23/100 | -0.020 | 0.0101 | -0.042 | 0.540/1.000/0.780 |
| `BTC` | 2024 | 72000 | `gemischt` | 16/100 | -0.182 | 0.0077 | -0.125 | 0.010/1.000/0.520 |
| `SOL` | 2024 | 0 | `gemischt` | 55/100 | 0.001 | -0.0013 | 0.000 | 0.270/0.355/0.240 |
| `SOL` | 2024 | 36000 | `gemischt` | 29/100 | 0.005 | 0.0013 | 0.000 | 0.780/1.000/0.840 |
| `SOL` | 2024 | 72000 | `verstaerkt` | 7/100 | 0.178 | 0.0104 | 0.083 | 1.000/1.000/0.530 |
| `BTC` | 2025 | 0 | `verstaerkt` | 0/100 | 0.165 | 0.0121 | 0.083 | 1.000/1.000/1.000 |
| `BTC` | 2025 | 36000 | `gemischt` | 15/100 | -0.003 | 0.0074 | 0.000 | 0.930/1.000/0.930 |
| `BTC` | 2025 | 72000 | `gemischt` | 52/100 | 0.001 | 0.0111 | 0.000 | 0.930/1.000/0.900 |
| `SOL` | 2025 | 0 | `verstaerkt` | 0/100 | 0.253 | 0.0020 | 0.125 | 1.000/1.000/1.000 |
| `SOL` | 2025 | 36000 | `verstaerkt` | 46/100 | 0.030 | 0.0003 | 0.083 | 0.550/0.180/0.710 |
| `SOL` | 2025 | 72000 | `gemischt` | 66/100 | -0.261 | 0.0034 | -0.167 | 0.000/0.960/0.330 |

## Antwortpfade

| Asset/Jahr | Startfolge | Antwortfolge | Wechsel | Mindestperzentile |
|---|---|---|---:|---|
| `BTC:2024` | `0;36000;72000` | `verstaerkt;gemischt;gemischt` | 1 | `1.000;0.540;0.010` |
| `BTC:2025` | `0;36000;72000` | `verstaerkt;gemischt;gemischt` | 1 | `1.000;0.930;0.900` |
| `SOL:2024` | `0;36000;72000` | `gemischt;gemischt;verstaerkt` | 1 | `0.240;0.780;0.530` |
| `SOL:2025` | `0;36000;72000` | `verstaerkt;verstaerkt;gemischt` | 1 | `1.000;0.180;0.000` |

## Befund

Von zwölf Fenstern sind `5` verstärkt, `7` gemischt und `0` abgeschwächt. `5` Fenster tragen positive Abstände auf allen drei Achsen, `0` negative Abstände auf allen drei Achsen. Über die acht benachbarten Übergänge der vier Asset-Jahr-Pfade wechselt die Antwort `4`-mal.

Der Ereignisanteil steigt in `11/12` Fenstern. Kontinuität steigt in `8/12`; Abdeckung steigt in `5/12`, bleibt in `4/12` unverändert und sinkt in `3/12`. Die Volumenphasenverschiebung trägt damit fast durchgehend mehr Familienereignisse, wird aber je lokaler Feldlage verschieden in Kontinuität und Mitgliederbreite aufgenommen.

Alle vier Pfade wechseln genau einmal: `1`. Die beiden BTC-Jahre tragen sogar dieselbe Folge `verstaerkt;gemischt;gemischt`: `1`. Die gemischten Teilgruppen aus 2083 stammen damit nicht aus einem einzelnen Ausreißer, sondern aus wiederkehrenden feldphasenabhängigen Verschiebungen. Für SOL ist die Pfadrichtung zwischen den Jahren verschieden, also nicht als allgemeiner Kalender- oder Positionscode lesbar.

In nur `3/12` Fenstern liegt selbst das niedrigste der drei realen Maße mindestens am Perzentil `0.950` der gematchten Pseudo-Familien. Der starke Gesamtwert aus 2083 ist deshalb eine kollektive Antwort über mehrere Feldphasen, keine lokale Invariante jedes Fensters. Ein hoher Nullabstand und eine gleichgerichtete Verstärkung sind nicht dasselbe.

Die Tabelle bewahrt diese Verläufe numerisch. Verstärkt und gemischt bleiben Berichtssprache; sie werden weder als Feldklassen noch als Wenn-Dann-Regeln programmiert.

## Grenze

Die Fenster sind eine nachträgliche Zerlegung derselben 2083-Evidenz. Sie erhöhen weder Stichprobe noch Unabhängigkeit. Die passive Antwort-Memory bleibt bei 217 Beobachtungen und 32 Identitäten; `rf_05:volume` bleibt `dio_rresponse_0gpsabe` und wird weiterhin nicht von MINI_DIO gelesen.
