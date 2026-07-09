# 1723 - Asset-Randdruck und Rekopplungsnaehe 10k

## Frage

Nach der reproduzierbaren Randdruck-Lupe war die naechste Frage:

```text
Bleibt die lokale Randdruck-/Rekopplungsform nur in SOL/BTC sichtbar,
oder erscheint sie auch bei anderen Asset-Welten?
```

Geprueft wurden drei 10k-Welten:

- PAXG 2024 5m,
- XRP 2024 5m,
- DOGE 2024 5m.

## Berichte

```text
reports/relative_rand_pressure_assets_10k.md
reports/world_relative_topology_assets_10k.md
```

## Relative Randdruck-Lupe

| Welt | Episoden | Randdruck | Offen | Rekopplung | Daempfung |
|---|---:|---:|---:|---:|---:|
| PAXG 2024 5m 10k | 9994 | 0.4222 | 0.1469 | 0.3566 | 0.0743 |
| XRP 2024 5m 10k | 9994 | 0.4247 | 0.1341 | 0.3338 | 0.1075 |
| DOGE 2024 5m 10k | 9994 | 0.4242 | 0.1366 | 0.3326 | 0.1067 |

## Globale Topologie-Matrix

| Welt | Episoden | Topologiezustand | Rekopplungsnaehe |
|---|---:|---|---:|
| PAXG 2024 5m 10k | 2216 | gemischte_rollenordnung | 1.0000 |
| XRP 2024 5m 10k | 2278 | gemischte_rollenordnung | 1.0000 |
| DOGE 2024 5m 10k | 2274 | gemischte_rollenordnung | 1.0000 |

## Zeitmass-Vergleich 5m gegen 1h

Als Folgeschritt wurden dieselben Assetklassen als 1h-Welten geprueft.

Berichte:

```text
reports/relative_rand_pressure_assets_1h_10k.md
reports/world_relative_topology_assets_1h_10k.md
```

| Welt | Episoden | Randdruck | Offen | Rekopplung | Daempfung |
|---|---:|---:|---:|---:|---:|
| PAXG 2024 1h 10k | 8778 | 0.4147 | 0.1486 | 0.3268 | 0.1099 |
| XRP 2024 1h 10k | 8778 | 0.4255 | 0.1343 | 0.3370 | 0.1032 |
| DOGE 2024 1h 10k | 8778 | 0.4232 | 0.1342 | 0.3308 | 0.1118 |

Auch die 1h-Topologie-Matrix liest alle drei Welten als
`gemischte_rollenordnung` mit dominanter Rekopplungsnaehe.

Die wichtigste Verschiebung:

```text
PAXG 5m:
  Rekopplung 0.3566
  Daempfung 0.0743

PAXG 1h:
  Rekopplung 0.3268
  Daempfung 0.1099
```

PAXG bleibt also nicht einfach gleich. Bei groberer Weltzeit wird die
Rekopplung schwaecher und Daempfung deutlicher.

XRP und DOGE bleiben dagegen naeher an ihrer 5m-Form.

## Interpretation

Alle drei Asset-Welten zeigen lokalen Randdruck, aber global keine harte
Randklasse. Die Topologie-Matrix liest sie als Rekopplungsnaehe.

Der Unterschied liegt in der Qualitaet:

```text
PAXG:
  mehr Rekopplung
  weniger Daempfung
  weniger Visual-/Hearing-Gap

XRP / DOGE:
  aehnlicher Randdruck
  weniger Rekopplung als PAXG
  mehr Daempfung
  hoehere Sicht-/Hoer-Gap
```

Damit wirkt PAXG nicht einfach "ruhig" oder "schwach", sondern anders
gebunden. XRP und DOGE wirken in dieser Pruefung naeher beieinander.

Der 1h-Vergleich zeigt zusaetzlich:

```text
Weltzeit veraendert Feldqualitaet.
Sie skaliert nicht nur dieselbe Form groesser oder kleiner.
```

## Bedeutung fuer die MCM-Lesung

Die Befunde stuetzen die Trennung:

```text
lokaler Randdruck != globale Randrolle
```

Ein Feld kann lokal Druck tragen und trotzdem global als Rekopplungsnaehe
erscheinen. Das ist fuer MINI_DIO wichtig, weil dadurch nicht nur gefragt wird,
ob ein Rand existiert, sondern wie er vom Feld gehalten wird.

## Methodische Grenze

Die globale Topologie-Matrix liest diese Asset-Welten stark als
Rekopplungsnaehe. Das ist ein Befund, aber auch ein Hinweis:

```text
Die Matrix ist fuer globale Rollen gut,
die Randdruck-Lupe fuer lokale Druckqualitaet.
```

Beide Diagnosen sollten zusammen gelesen werden.
