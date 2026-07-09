# 1729 - Asset-Milieu-Matrix

## Frage

Nach den Einzelpruefungen fuer PAXG, XRP, DOGE und BTC sollte die
Rollenlandschaft kompakt nebeneinander gelesen werden:

```text
Welche Asset-Milieus tragen dieselbe Topologie,
aber mit unterschiedlicher lokaler Gewichtung?
```

## Datenbasis

Je Asset wurden vier 5k-Welten gelesen:

- 2024 Start,
- 2024 Folge,
- 2025 Start,
- 2025 Folge.

Vollbericht:

```text
reports/asset_milieu_matrix.md
```

## Asset-Mittelwerte

| Asset | Randdruck avg | Offen avg | Rekopplung avg | Daempfung avg | Rek-Spannweite | Daempf-Spannweite | Lesart |
|---|---:|---:|---:|---:|---:|---:|---|
| BTC | 0.4098 | 0.1548 | 0.3138 | 0.1216 | 0.0042 | 0.0077 | mehr Daempfung, engere Rekopplung |
| DOGE | 0.4120 | 0.1535 | 0.3090 | 0.1255 | 0.0152 | 0.0141 | mehr Daempfung, engere Rekopplung |
| PAXG | 0.4160 | 0.1484 | 0.3438 | 0.0918 | 0.0196 | 0.0154 | stark rekoppelnd, wenig daempfend |
| XRP | 0.4112 | 0.1528 | 0.3150 | 0.1211 | 0.0142 | 0.0173 | mehr Daempfung, engere Rekopplung |

## Interpretation

Die globale Topologie bleibt ueber die geprueften Assets vergleichbar:

```text
gemischte Rollenordnung
dominante Rekopplungsnaehe
lokaler Randdruck
```

Die lokale Qualitaet unterscheidet sich aber deutlich.

PAXG:

```text
hoechste Rekopplung
niedrigste Daempfung
staerkste Sonderstellung
```

BTC, XRP, DOGE:

```text
dichter beieinander
mehr Daempfung / Schutzabstand
engere Rekopplung
```

## Bedeutung fuer die Topologie

Die Matrix stuetzt die aktuelle MCM-Skizze:

```text
gleiche Grundform
verschiedene Milieuqualitaeten
```

Damit ist die Topologie weder reine Geometrie noch reine Symboltabelle.
Sie wirkt wie ein Rollenraum, in dem verschiedene Weltspuren unterschiedliche
Gewichtungen erzeugen.

## Methodische Grenze

Die Werte sind relative Diagnoseprofile innerhalb der geprueften Welten.
Sie sind keine universellen MCM-Grenzen und keine Runtime-Regeln.
