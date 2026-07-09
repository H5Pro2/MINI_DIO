# 1733 - KAS Zeitachsen-Matrix

## Frage

Nach BTC/SOL wurde KAS als deutlich anderes Assetmilieu über mehrere Zeitmaße geprüft.

```text
5m, 15m, 30m, 1h
```

Die Frage war:

```text
Bricht KAS die bekannte MCM-Topologie,
oder bleibt die Rollenordnung stabil und wird nur lokal gefärbt?
```

## Datenbasis

Gelesen wurden vier kontrollierte KAS-Welten aus 2024:

- KAS 5m,
- KAS 15m,
- KAS 30m,
- KAS 1h.

Jede Welt enthält 2000 Rohzeilen und erzeugte 1994 Episoden.

Vollberichte:

```text
reports/kas_time_axis_matrix.md
reports/kas_time_axis_topology.md
reports/kas_time_axis_randdruck.md
```

## Matrix

| Welt | Episoden | Randdruck | Offen | Rekopplung | Dämpfung | Strain | Intake | Visual Gap | Hearing Gap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| KAS_2024_5M | 1994 | 0.3927 | 0.1740 | 0.3069 | 0.1264 | 0.1663 | 0.1086 | 0.1827 | 0.1055 |
| KAS_2024_15M | 1994 | 0.3907 | 0.1700 | 0.3024 | 0.1369 | 0.1667 | 0.1104 | 0.1798 | 0.1080 |
| KAS_2024_30M | 1994 | 0.4042 | 0.1630 | 0.3014 | 0.1314 | 0.1669 | 0.1106 | 0.1827 | 0.1081 |
| KAS_2024_1H | 1994 | 0.4007 | 0.1620 | 0.3004 | 0.1369 | 0.1675 | 0.1090 | 0.1892 | 0.1057 |

## Topologie

Alle vier KAS-Welten bleiben:

```text
stark_zentriert_wenig_rand
```

Die Topologie-Lesung zeigt:

| Welt | Zentrum | Offen | Rand/Kipp | Rekopplung |
|---|---:|---:|---:|---:|
| KAS_2024_5M | 0.9895 | 0.0105 | 0.0000 | 0.6951 |
| KAS_2024_15M | 0.9915 | 0.0085 | 0.0000 | 0.6949 |
| KAS_2024_30M | 0.9895 | 0.0105 | 0.0000 | 0.6943 |
| KAS_2024_1H | 0.9855 | 0.0145 | 0.0000 | 0.6945 |

## Interpretation

KAS bricht die bisherige Feldordnung nicht. Auch dieses Assetmilieu bleibt zentrumsnah.

Gleichzeitig ist KAS nicht identisch mit BTC/SOL:

- 30m und 1h wirken minimal randdrucknäher.
- 15m und 1h wirken minimal dämpfungsnäher.
- 1h erzeugt den höchsten offenen Anteil, aber keinen Randbruch.
- Die Rekopplung bleibt über alle KAS-Zeitmaße eng beieinander.

Damit wirkt KAS als eigenes Milieu innerhalb derselben Topologie:

```text
KAS = zentrumsnah, aber mit etwas sichtbarerer Zeitmaßfärbung
```

## Bedeutung für MINI_DIO

Der Befund stärkt die bisherige Lesart:

```text
Die MCM-Topologie ist robuster als einzelne Asset- oder Zeitmaßwechsel.
Asset und Zeitmaß färben die lokale Feldwirkung,
aber sie erzwingen bisher keine neue Grundordnung.
```

Wichtig ist dabei: Das ist kein Beweis für eine universelle Topologie. Es ist ein weiterer reproduzierbarer Befund innerhalb der geprüften Welten.

## Wie es weitergeht

Als nächstes sollte PAXG gezielt in dieselbe Zeitachsenlogik gebracht werden. Dafür fehlt aktuell ein fertiges 15m-Fenster; es sollte aus vorhandenen Rohdaten erzeugt werden, damit PAXG gegen KAS, BTC und SOL sauber vergleichbar wird.
