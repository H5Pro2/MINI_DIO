# 1732 - BTC/SOL Zeitachsen-Matrix

## Frage

Nach der 15m-Zwischenprüfung wurde BTC/SOL über drei Zeitmaße zusammengeführt:

```text
5m, 15m, 1h
```

Geprüft wurde, ob das Zeitmaß eine neue Topologie erzwingt oder ob dieselbe MCM-Rollenordnung nur anders gefärbt wird.

## Datenbasis

Gelesen wurden 24 Welten:

- BTC 2024 Start/Folge in 5m, 15m, 1h,
- BTC 2025 Start/Folge in 5m, 15m, 1h,
- SOL 2024 Start/Folge in 5m, 15m, 1h,
- SOL 2025 Start/Folge in 5m, 15m, 1h.

Die 5m- und 15m-Fenster enthalten jeweils 5000 Zeilen. Die 1h-Folgefenster sind kürzer, weil nach Start 5000 weniger Restdaten im Jahr vorhanden sind.

Vollberichte:

```text
reports/btc_sol_time_axis_matrix.md
reports/btc_sol_time_axis_topology.md
reports/btc_sol_time_axis_randdruck.md
```

## Zeitmaß-Mittelwerte

| Zeitmaß | Welten | Randdruck | Offen | Rekopplung | Dämpfung | Strain | Intake | Visual Gap | Hearing Gap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5M | 8 | 0.4084 | 0.1561 | 0.3111 | 0.1244 | 0.1685 | 0.1079 | 0.1785 | 0.1047 |
| 15M | 8 | 0.4093 | 0.1540 | 0.3105 | 0.1263 | 0.1688 | 0.1076 | 0.1800 | 0.1046 |
| 1H | 8 | 0.4056 | 0.1554 | 0.3063 | 0.1326 | 0.1684 | 0.1060 | 0.1837 | 0.1030 |

## Asset-Mittelwerte

| Asset | Welten | Randdruck | Offen | Rekopplung | Dämpfung | Strain | Intake | Visual Gap | Hearing Gap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC | 12 | 0.4082 | 0.1553 | 0.3111 | 0.1255 | 0.1679 | 0.1063 | 0.1784 | 0.1030 |
| SOL | 12 | 0.4074 | 0.1551 | 0.3075 | 0.1301 | 0.1693 | 0.1080 | 0.1831 | 0.1052 |

## Befund

Alle 24 Welten bleiben in der Topologie-Diagnose:

```text
stark_zentriert_wenig_rand
```

Damit bestätigt die Zeitachsenmatrix den bisherigen Befund:

```text
Zeitmaß färbt die Rollenordnung.
Zeitmaß bricht die Topologie nicht.
```

## Interpretation

Die stärkste Veränderung liegt nicht im Randbruch, sondern in der lokalen Milieu-Färbung:

- 1h zeigt etwas mehr Dämpfung und Visual Gap.
- 5m und 15m liegen enger beieinander.
- BTC wirkt leicht rekopplungsnäher.
- SOL wirkt leicht offener und dämpfender.

Die Grundform bleibt trotzdem stabil:

```text
Zentrum bleibt dominant.
Offene Variante bleibt klein.
Rand/Kipp wird lokal sichtbar, aber nicht tragend dominant.
Rekopplung bleibt eine stabilisierende Übergangsqualität.
```

## Bedeutung für MINI_DIO

MINI_DIO liest die geprüften Zeitmaße nicht als getrennte Welten mit völlig anderer Innenordnung. Es entsteht eher ein gemeinsamer Rollenraum, der durch Asset und Zeitmaß lokal eingefärbt wird.

Das stützt die aktuelle MCM-Lesart:

```text
Topologie = robuste Feldordnung
Zeitmaß   = lokale Färbung dieser Ordnung
Asset     = Milieuqualität innerhalb dieser Ordnung
```

## Methodische Grenze

Dieser Befund gilt für BTC/SOL und die geprüften Fenster. Er ersetzt noch keine vollständige Zeitachsenmatrix über PAXG, XRP, DOGE, KAS oder synthetische Kontrollwelten.
