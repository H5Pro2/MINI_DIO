# Asset-Milieu-Matrix 1h

## Zweck

Diese Matrix prueft, ob die vorherige 5m-Asset-Milieu-Ordnung auch bei groesserer Zeitauflosung sichtbar bleibt.

Gelesen wurden je Asset vier 1h-Welten:

- 2024 Start,
- 2024 Folge,
- 2025 Start,
- 2025 Folge.

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung und keine Runtime-Regel.

## Asset-Mittelwerte

| Asset | Welten | Randdruck | Offen | Rekopplung | Daempfung | Strain | Intake | Visual Gap | Hearing Gap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC | 4 | 0.4044 | 0.1580 | 0.3081 | 0.1294 | 0.1676 | 0.1051 | 0.1808 | 0.1019 |
| DOGE | 4 | 0.4094 | 0.1541 | 0.3100 | 0.1265 | 0.1682 | 0.1063 | 0.1824 | 0.1035 |
| PAXG | 4 | 0.4018 | 0.1616 | 0.3129 | 0.1238 | 0.1676 | 0.1066 | 0.1782 | 0.1018 |
| XRP | 4 | 0.4112 | 0.1511 | 0.3102 | 0.1276 | 0.1678 | 0.1057 | 0.1803 | 0.1026 |

## Kurzlesung

Die 1h-Matrix bestaetigt die Topologie, verschiebt aber die lokale Gewichtung.

```text
Topologie: stabil zentriert
Zeitmass: glatter als 5m
Assetabstand: kleiner als bei 5m
```

PAXG bleibt im 1h-Vergleich rekopplungsstaerkstes und daempfungsaermstes Asset.
Der Abstand ist aber deutlich kleiner als bei der 5m-Matrix.

XRP und DOGE zeigen im 1h-Raum mehr Randdruck als PAXG.
BTC wirkt am staerksten daempfend.

## Bezug zur 5m-Matrix

Die 5m-Matrix zeigte PAXG als deutlichsten Sonderpol:

```text
hohe Rekopplung
geringe Daempfung
klare Sonderstellung
```

Die 1h-Matrix zeigt dieselbe Richtung, aber geglaettet:

```text
PAXG bleibt rekopplungsnah
die Assetunterschiede werden flacher
alle Welten bleiben stark zentriert
```

Damit wirkt Zeitauflosung nicht wie ein Topologiebruch.
Sie faerbt die lokale Milieuqualitaet und glaettet Rand-/Kippnaehe.

## Methodische Grenze

Die 1h-Folgewelten enthalten weniger als 5000 Zeilen, weil ein Kalenderjahr auf 1h keine vollen 10000 Kerzen liefert.
Start- und Folgewelten werden deshalb getrennt gelesen.

Die Werte sind Diagnoseprofile, keine MCM-Grenzen und keine Vorgaben fuer MINI_DIO.
