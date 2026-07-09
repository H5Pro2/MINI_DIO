# 1736 - Holdout 2025 BTC/SOL Zeitachsen

## Frage

Nach der Asset-Zeitachsen-Synthese wurde eine erste Holdout-Gegenprobe gefahren:

```text
gleiches Assetmilieu,
anderes Jahr,
gleiche Zeitachsenlogik.
```

Geprüft wurde, ob die bisherige Topologie- und Milieulesung auch in unabhängigen 2025-Fenstern von BTC und SOL erhalten bleibt.

## Datenbasis

Gelesen wurden acht 2025-Welten:

- BTC 5m, 15m, 30m, 1h,
- SOL 5m, 15m, 30m, 1h.

Jede Welt enthält 2000 Rohzeilen und erzeugte 1994 Episoden.

Vollberichte:

```text
reports/holdout_2025_btc_sol_matrix.md
reports/holdout_2025_btc_sol_topology.md
reports/holdout_2025_btc_sol_randdruck.md
```

## Matrix

| Welt | Episoden | Randdruck | Offen | Rekopplung | Dämpfung | Strain | Intake | Visual Gap | Hearing Gap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC_2025_5M_HOLDOUT | 1994 | 0.3922 | 0.1805 | 0.2954 | 0.1319 | 0.1658 | 0.1095 | 0.1776 | 0.1061 |
| BTC_2025_15M_HOLDOUT | 1994 | 0.3992 | 0.1605 | 0.3159 | 0.1244 | 0.1650 | 0.1069 | 0.1762 | 0.1040 |
| BTC_2025_30M_HOLDOUT | 1994 | 0.4027 | 0.1605 | 0.3044 | 0.1324 | 0.1649 | 0.1051 | 0.1820 | 0.1015 |
| BTC_2025_1H_HOLDOUT | 1994 | 0.3977 | 0.1620 | 0.3004 | 0.1399 | 0.1638 | 0.1029 | 0.1790 | 0.0993 |
| SOL_2025_5M_HOLDOUT | 1994 | 0.4077 | 0.1605 | 0.2959 | 0.1359 | 0.1673 | 0.1099 | 0.1876 | 0.1073 |
| SOL_2025_15M_HOLDOUT | 1994 | 0.4042 | 0.1575 | 0.3124 | 0.1259 | 0.1646 | 0.1081 | 0.1676 | 0.1058 |
| SOL_2025_30M_HOLDOUT | 1994 | 0.3957 | 0.1610 | 0.3134 | 0.1299 | 0.1659 | 0.1101 | 0.1752 | 0.1079 |
| SOL_2025_1H_HOLDOUT | 1994 | 0.3942 | 0.1665 | 0.3104 | 0.1289 | 0.1663 | 0.1082 | 0.1808 | 0.1061 |

## Topologie

Alle acht Holdout-Welten bleiben:

```text
stark_zentriert_wenig_rand
```

Die Topologie-Lesung zeigt weiter keine Randdominanz:

```text
Rand/Kipp = 0.0000 in allen acht Welten
```

Die offene Variante bleibt klein, wird aber lokal sichtbarer:

- BTC 15m: 0.0165,
- BTC 30m: 0.0181,
- SOL 1h: 0.0165.

## Interpretation

Die Holdout-Gegenprobe bestätigt den bisherigen Kern:

```text
Die Topologie bleibt stabil.
Das Jahr/Fenster färbt lokal.
Es entsteht keine neue Grundordnung.
```

Gleichzeitig verschiebt sich das Milieu gegenüber der vorherigen BTC/SOL-Matrix:

- BTC 2025 5m zeigt mehr Offenheit in der Randdruck-Lupe.
- BTC 15m/30m zeigen mehr offene Variante in der Topologie-Lesung.
- SOL bleibt zentrumsnah, zeigt aber je nach Zeitmaß andere Rekopplungsprofile.

Damit ist die Holdout-Lesung nicht einfach eine Kopie der alten Matrix. Sie bestätigt die Rollenordnung, aber nicht jede lokale Gewichtung.

## Bedeutung für MINI_DIO

Der Befund ist wichtig, weil er zwei Dinge trennt:

```text
Reproduzierbar bleibt die Rollenordnung.
Variabel bleibt die lokale Feldfärbung.
```

Das spricht gegen reine Projektion eines festen Bildes. Wenn alles gleich wäre, wäre es nur Kopie. Wenn alles bräche, wäre es instabil. Der aktuelle Befund liegt dazwischen: stabile Topologie mit variabler lokaler Milieudynamik.
