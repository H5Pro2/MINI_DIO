# 1734 - PAXG Zeitachsen-Matrix

## Frage

Nach BTC/SOL und KAS wurde PAXG als kontrastreiches Assetmilieu geprüft.

```text
5m, 15m, 1h
```

Die Frage war:

```text
Bleibt PAXG als rekopplungsnahes Milieu auch über Zeitmaße stabil,
oder erzwingt die Aggregation eine andere Rollenordnung?
```

## Datenbasis

Gelesen wurden drei kontrollierte PAXG-Welten aus 2024:

- PAXG 5m,
- PAXG 15m,
- PAXG 1h.

Das 15m-Fenster wurde aus vorhandenen 5m-Rohdaten aggregiert. Jede Welt enthält 2000 Rohzeilen und erzeugte 1994 Episoden.

Vollberichte:

```text
reports/paxg_time_axis_matrix.md
reports/paxg_time_axis_topology.md
reports/paxg_time_axis_randdruck.md
```

## Matrix

| Welt | Episoden | Randdruck | Offen | Rekopplung | Dämpfung | Strain | Intake | Visual Gap | Hearing Gap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| PAXG_2024_5M | 1994 | 0.4057 | 0.1670 | 0.3290 | 0.0983 | 0.1623 | 0.1011 | 0.1708 | 0.0933 |
| PAXG_2024_15M | 1994 | 0.3922 | 0.1705 | 0.3134 | 0.1239 | 0.1643 | 0.1060 | 0.1795 | 0.0990 |
| PAXG_2024_1H | 1994 | 0.4007 | 0.1625 | 0.3170 | 0.1199 | 0.1656 | 0.1071 | 0.1811 | 0.1010 |

## Topologie

Alle drei PAXG-Welten bleiben:

```text
stark_zentriert_wenig_rand
```

Die Topologie-Lesung zeigt:

| Welt | Zentrum | Offen | Rand/Kipp | Rekopplung |
|---|---:|---:|---:|---:|
| PAXG_2024_5M | 0.9930 | 0.0070 | 0.0000 | 0.7048 |
| PAXG_2024_15M | 0.9925 | 0.0075 | 0.0000 | 0.6977 |
| PAXG_2024_1H | 0.9895 | 0.0105 | 0.0000 | 0.6972 |

## Interpretation

PAXG bleibt das bisher rekopplungsstärkste und dämpfungsärmste Milieu in dieser Vergleichslogik.

Die Zeitachsenfärbung ist trotzdem sichtbar:

- 5m trägt die stärkste Rekopplung und die geringste Dämpfung.
- 15m glättet die Aufnahme, erhöht Dämpfung und senkt Rekopplung leicht.
- 1h bleibt zentriert, aber wird etwas offener und visuell weiter.

Damit bestätigt PAXG die bisherige MCM-Lesart:

```text
Topologie bleibt stabil.
Zeitmaß färbt lokale Aufnahme und Rekopplung.
Assetmilieu bestimmt, wie stark diese Färbung ausfällt.
```

## Vergleich zu KAS

KAS blieb ebenfalls zentrumsnah, wirkte aber weniger rekopplungsstark.
PAXG trägt dagegen stärkere Rekopplung und weniger Dämpfung, besonders in 5m.

Das spricht nicht für eine starre Assetklasse, sondern für unterschiedliche Milieuqualitäten innerhalb derselben passiven Rollenordnung.

## Methodische Grenze

Das PAXG-15m-Fenster wurde aggregiert. Es ist fachlich brauchbar für diese Gegenprobe, sollte aber später gegen echte 15m-Rohdaten geprüft werden, falls diese verfügbar sind.

## Wie es weitergeht

Als nächstes sollte eine gemeinsame Asset-Zeitachsen-Synthese aus BTC, SOL, KAS und PAXG erstellt werden. Ziel ist eine kompakte Matrix, die zeigt, welche Unterschiede Topologie, Assetmilieu oder Zeitmaß betreffen.
