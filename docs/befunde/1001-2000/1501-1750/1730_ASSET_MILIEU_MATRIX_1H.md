# 1730 - Asset-Milieu-Matrix 1h

## Frage

Nach der 5m-Asset-Milieu-Matrix wurde geprueft, ob dieselbe Rollenordnung auch bei 1h-Zeitauflosung sichtbar bleibt.

```text
Bleibt die MCM-Topologie stabil,
wenn dieselben Assettypen mit groesserem Zeitmass gelesen werden?
```

## Datenbasis

Je Asset wurden vier 1h-Welten gelesen:

- 2024 Start,
- 2024 Folge,
- 2025 Start,
- 2025 Folge.

Vollberichte:

```text
reports/asset_milieu_1h_matrix.md
reports/asset_milieu_1h_randdruck_recheck.md
reports/asset_milieu_1h_topology_recheck.md
```

## Asset-Mittelwerte

| Asset | Randdruck | Offen | Rekopplung | Daempfung | Lesart |
|---|---:|---:|---:|---:|---|
| BTC | 0.4044 | 0.1580 | 0.3081 | 0.1294 | staerkste Daempfung |
| DOGE | 0.4094 | 0.1541 | 0.3100 | 0.1265 | mehr Randdruck als PAXG |
| PAXG | 0.4018 | 0.1616 | 0.3129 | 0.1238 | rekopplungsstaerkster 1h-Pol |
| XRP | 0.4112 | 0.1511 | 0.3102 | 0.1276 | hoechster Randdruck im 1h-Vergleich |

## Befund

Die 1h-Topologiematrix liest alle 16 Welten als:

```text
stark_zentriert_wenig_rand
```

Damit bleibt die globale Topologie erhalten.
Der Unterschied zur 5m-Matrix liegt nicht in einem Bruch der Grundform, sondern in der Glaettung der Asset-Milieus.

## Interpretation

PAXG bleibt rekopplungsnah, aber nicht mehr so stark abgesetzt wie bei 5m.
BTC, DOGE und XRP liegen naeher beieinander.
XRP und DOGE zeigen bei 1h relativ mehr Randdruck, BTC mehr Daempfung.

Das spricht fuer:

```text
Topologie = stabile Rollenordnung
Zeitmass = lokale Faerbung / Glaettung
Asset = Milieuqualitaet innerhalb derselben Grundform
```

## Bedeutung fuer MINI_DIO

MINI_DIO liest bei 1h nicht einfach eine neue Topologie.
Es liest dieselbe Rollenordnung mit anderer Milieugewichtung.

Das ist wichtig, weil es gegen eine starre Symboltabelle spricht:

```text
gleiche Grundform
andere Gewichtung
andere lokale Rand-/Rekopplungsnaehe
```

## Methodische Grenze

Die Folgewelten enthalten weniger als 5000 Zeilen, weil die 1h-Jahresdaten nach dem Startfenster keine vollen weiteren 5000 Zeilen tragen.
Der Befund ist deshalb als Start/Folge-Vergleich zu lesen, nicht als exakt gleich langer 5k/5k-Split.
