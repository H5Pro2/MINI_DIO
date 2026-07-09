# 1735 - Asset-Zeitachsen-Synthese

## Frage

Nach den Einzelprüfungen von BTC/SOL, KAS und PAXG wurde die gemeinsame Frage verdichtet:

```text
Was ist robuste MCM-Topologie?
Was ist Assetmilieu?
Was ist Zeitmaß-Färbung?
```

## Datenbasis

Zusammengeführt wurden verfügbare Zeitachsen aus:

- BTC,
- SOL,
- KAS,
- PAXG.

Die Matrix kombiniert 5m, 15m, 30m und 1h, wobei nicht jedes Asset in jeder Zeitachse gleich breit vorliegt.

Vollbericht:

```text
reports/asset_time_axis_synthesis.md
```

## Asset-Mittelwerte

| Asset | Welten | Randdruck | Offen | Rekopplung | Dämpfung | Strain | Intake | Visual Gap | Hearing Gap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC | 12 | 0.4082 | 0.1553 | 0.3111 | 0.1255 | 0.1679 | 0.1063 | 0.1784 | 0.1030 |
| SOL | 12 | 0.4074 | 0.1551 | 0.3076 | 0.1301 | 0.1693 | 0.1080 | 0.1830 | 0.1053 |
| KAS | 4 | 0.3971 | 0.1673 | 0.3028 | 0.1329 | 0.1668 | 0.1096 | 0.1836 | 0.1068 |
| PAXG | 3 | 0.3995 | 0.1667 | 0.3198 | 0.1140 | 0.1641 | 0.1047 | 0.1771 | 0.0978 |

## Zeitmaß-Mittelwerte

| Zeitmaß | Welten | Randdruck | Offen | Rekopplung | Dämpfung | Strain | Intake | Visual Gap | Hearing Gap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5M | 10 | 0.4066 | 0.1590 | 0.3125 | 0.1220 | 0.1677 | 0.1072 | 0.1781 | 0.1036 |
| 15M | 10 | 0.4057 | 0.1573 | 0.3100 | 0.1271 | 0.1681 | 0.1077 | 0.1799 | 0.1044 |
| 30M | 1 | 0.4042 | 0.1630 | 0.3014 | 0.1314 | 0.1669 | 0.1106 | 0.1827 | 0.1081 |
| 1H | 10 | 0.4046 | 0.1568 | 0.3068 | 0.1318 | 0.1680 | 0.1064 | 0.1840 | 0.1031 |

## Befund

Alle zugrunde liegenden Topologieberichte lesen die geprüften Welten als:

```text
stark_zentriert_wenig_rand
```

Damit trennt sich der Befund in drei Ebenen:

```text
Topologie      = stabil zentrumsnah
Assetmilieu    = unterschiedliche lokale Rekopplung, Dämpfung, Offenheit
Zeitmaß        = graduelle Färbung, bisher kein Bruch
```

## Interpretation

PAXG bleibt rekopplungsstärker und dämpfungsärmer als die anderen geprüften Assets.
KAS ist offener und dämpfungsnäher.
BTC und SOL liegen enger beieinander, wobei BTC minimal rekopplungsnäher und SOL minimal offener/visuell weiter wirkt.

Die Zeitachsen zeigen eine schwache, aber konsistente Richtung:

- 5m trägt im Mittel etwas mehr Rekopplung und weniger Dämpfung.
- 15m liegt dazwischen.
- 1h ist gedämpfter, visuell weiter und weniger rekopplungsstark.

Das spricht gegen eine einfache Aussage wie:

```text
1h ist besser oder schlechter.
```

Sauberer ist:

```text
1h färbt das Feld anders.
```

## Bedeutung für MINI_DIO

Die bisherige Forschungsrichtung wird dadurch präziser:

```text
MINI_DIO bildet keinen starren Symbolraum,
sondern eine robuste Rollenordnung mit lokaler Milieu-Färbung.
```

Das ist für die weitere MCM-Forschung wichtig, weil eine stabile Topologie nicht bedeutet, dass alles gleich gelesen wird. Die gleiche Grundform kann verschiedene Weltqualitäten tragen.

## Methodische Grenze

Die Assetbreite ist noch ungleich:

- BTC/SOL liegen breiter vor,
- KAS enthält zusätzlich 30m,
- PAXG-15m wurde aus 5m aggregiert.

Der Befund ist deshalb eine Synthese der aktuellen Datenlage, keine abschließende Assettheorie.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob die gleichen Assetmilieus auch in längeren oder verschobenen Fenstern stabil bleiben. Besonders sinnvoll ist eine Holdout-Gegenprobe: anderes Jahr, gleicher Assettyp, gleiche Zeitmaßlogik.
