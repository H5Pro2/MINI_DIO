# 1737 - PAXG 2025 Holdout Der Zeitachsenmatrix

## Fragestellung

Die vorherigen Prüfungen zeigten PAXG als rekopplungsstarkes und dämpfungsarmes Assetmilieu. Diese Datei prüft, ob dieser Befund in einem PAXG-2025-Holdout weiter sichtbar bleibt.

Die zentrale Frage:

```text
Bleibt PAXG auch in 2025 zentrumsnah und rekopplungsstark,
oder bricht die bisherige PAXG-Färbung unter neuer Weltphase auf?
```

## Datengrundlage

Geprüft wurden drei PAXG-2025-Welten:

| Welt | Datei | Episoden |
|---|---|---:|
| PAXG_2025_5M_HOLDOUT | `data/kontrolliert_paxg_2025_5m_test1_2000_PAXGUSDT.csv` | 1994 |
| PAXG_2025_15M_HOLDOUT | `data/kontrolliert_paxg_2025_15m_test1_2000_PAXGUSDT.csv` | 1994 |
| PAXG_2025_1H_HOLDOUT | `data/kontrolliert_paxg_2025_1h_test1_2000_PAXGUSDT.csv` | 1994 |

Die 15m-Welt wurde aus 5m-Daten aggregiert.

## Kurzbefund

Alle drei PAXG-2025-Welten bleiben topologisch:

```text
stark_zentriert_wenig_rand
```

Es entsteht keine Rand-/Kippdominanz. Die offene Variante bleibt klein:

| Welt | Zentrum | Offen | Rand/Kipp | Rekopplung | Dämpfung |
|---|---:|---:|---:|---:|---:|
| 5m | 0.9950 | 0.0050 | 0.0000 | 0.3561 | 0.0777 |
| 15m | 0.9900 | 0.0100 | 0.0000 | 0.3250 | 0.1118 |
| 1h | 0.9935 | 0.0065 | 0.0000 | 0.3104 | 0.1264 |

## Interpretation

PAXG 2025 bestätigt die bisherige Grundlinie:

- Die Topologie bleibt zentrumsnah.
- Rand/Kipp wird nicht dominant.
- Rekopplung bleibt deutlich sichtbar.
- Die Dämpfung steigt mit gröberer Zeitachse.

Der wichtigste Unterschied liegt nicht in der Topologie, sondern in der lokalen Färbung:

```text
5m  = stärker rekoppelnd, weniger gedämpft
15m = glatter, etwas offener und stärker gedämpft
1h  = weiter geglättet, mit höherer Dämpfung und Sinneslücke
```

Damit stützt der Holdout die bisherige Lesart: PAXG wirkt als eigene Weltqualität innerhalb derselben MCM-Topologie. Die Topologie bleibt stabil, während die Zeitachse die Aufnahmequalität färbt.

## Vergleich Zu 2024

Der Befund passt zur PAXG-2024-Zeitachsenmatrix. PAXG bleibt auch 2025 kein Randbruch, sondern eine zentrumsnahe Welt mit starker Rekopplungsneigung.

Der genaue Jahresvergleich ist noch offen. Dafür braucht es eine direkte 2024/2025-Gegenüberstellung der PAXG-Matrixwerte.

## Methodische Grenze

Diese Prüfung zeigt Stabilität in den gewählten PAXG-2025-Fenstern. Sie beweist nicht, dass jede PAXG-Welt gleich wirkt. Wichtig ist deshalb die nächste Gegenprobe mit verschobenen PAXG-Fenstern.

## Referenzen

- [holdout_2025_paxg_matrix.md](../../../../reports/holdout_2025_paxg_matrix.md)
- [holdout_2025_paxg_topology.md](../../../../reports/holdout_2025_paxg_topology.md)
- [holdout_2025_paxg_randdruck.md](../../../../reports/holdout_2025_paxg_randdruck.md)
