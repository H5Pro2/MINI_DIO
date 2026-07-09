# 1738 - PAXG 2024/2025 Direktvergleich

## Fragestellung

Nach der PAXG-2025-Holdout-Prüfung wurde die PAXG-Zeitachsenmatrix direkt gegen PAXG 2024 gelegt.

Die Frage:

```text
Ist PAXG nur in einem einzelnen Fenster rekopplungsstark,
oder bleibt diese Feldfärbung jahresübergreifend wiedererkennbar?
```

## Grundlage

Verglichen wurden:

- PAXG 2024: 5m, 15m, 1h,
- PAXG 2025: 5m, 15m, 1h.

Jede Welt enthält 1994 Episoden. Die 15m-Fenster wurden aus 5m-Daten aggregiert.

## Kernergebnis

Alle sechs PAXG-Zeitachsen bleiben:

```text
stark_zentriert_wenig_rand
```

Rand/Kipp bleibt in der Topologie-Lesung bei 0.0000. Die Topologie bricht damit weder im Jahreswechsel noch im Zeitmaßwechsel.

## Direkte Lesung

| Zeitachse | Hauptänderung 2025 gegenüber 2024 |
|---|---|
| 5m | mehr Rekopplung, weniger Dämpfung, geringere Sinneslücken |
| 15m | fast gleiche Feldfärbung, leicht mehr Rekopplung |
| 1h | leicht weniger Rekopplung, etwas mehr Dämpfung und Sinneslücke |

Die 5m-Achse ist der deutlichste Unterschied. Dort wirkt PAXG 2025 stärker rekoppelnd und weniger gedämpft als PAXG 2024.

## Interpretation

PAXG wirkt nicht wie eine starre Kopie zwischen 2024 und 2025. Es bleibt aber als Milieu wiedererkennbar:

```text
zentrumsnah
rekopplungsstark
vergleichsweise dämpfungsarm
ohne Rand-/Kippdominanz
```

Das ist für die MCM-Lesung wichtig, weil es zwei Ebenen trennt:

- Die globale Rollenordnung bleibt stabil.
- Die lokale Feldfärbung verändert sich mit Jahr und Zeitachse.

Damit wird die bisherige Topologie nicht mechanisch wiederholt, sondern innerhalb eines stabilen Rollenraums unterschiedlich gefärbt.

## Bedeutung Für MINI_DIO

Der Befund stärkt die Annahme, dass MINI_DIO nicht nur einzelne Fenster auswendig wiedergibt. Das Feld liest eine wiederkehrende Weltqualität, bleibt aber empfindlich für lokale Unterschiede.

Für die weitere Forschung heißt das:

```text
Stabilität ohne starre Kopie.
Varianz ohne Topologiebruch.
```

## Grenze

Der Vergleich verwendet je Jahr ein kontrolliertes Fenster. Für eine stärkere Aussage muss PAXG 2025 zusätzlich in verschobenen Folgefenstern geprüft werden.

## Referenz

- [paxg_2024_2025_direct_compare.md](../../../../reports/paxg_2024_2025_direct_compare.md)
- [paxg_time_axis_matrix.md](../../../../reports/paxg_time_axis_matrix.md)
- [holdout_2025_paxg_matrix.md](../../../../reports/holdout_2025_paxg_matrix.md)

## Wie es weitergeht

Als nächstes sollte ein verschobenes PAXG-2025-Fenster geprüft werden. Ziel ist zu klären, ob die rekopplungsstarke PAXG-Färbung stabil wiederkehrt oder innerhalb des Jahres phasenabhängig driftet.
