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

## Wie es weitergeht

Als naechstes sollte dieselbe Pruefung auf 1h-Welten laufen.
Entscheidend ist, ob die Rekopplungsnaehe bei groberer Weltzeit erhalten
bleibt oder ob PAXG, XRP und DOGE dann staerker auseinanderlaufen.
