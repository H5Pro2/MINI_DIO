# 1739 - PAXG 2025 Folgefenster Drift

## Fragestellung

Nach dem PAXG-2025-Holdout wurde ein verschobenes Folgefenster gelesen.

Die Frage:

```text
Bleibt PAXG 2025 im Folgeabschnitt rekopplungsstark,
oder driftet die lokale Feldfärbung innerhalb desselben Jahres?
```

## Grundlage

Geprüft wurden:

- `PAXG_2025_5M_SHIFT1`,
- `PAXG_2025_15M_SHIFT1`,
- `PAXG_2025_1H_SHIFT1`.

Die 15m-Welt wurde wieder aus 5m-Daten aggregiert.

## Ergebnis

Alle drei SHIFT1-Welten bleiben:

```text
stark_zentriert_wenig_rand
```

Die Topologie bleibt damit stabil. Rand/Kipp wird nicht dominant.

## Veränderung Gegenüber Holdout

| Zeitachse | Rekopplung | Dämpfung | Topologie |
|---|---|---|---|
| 5m | sinkt leicht | steigt | bleibt zentrumsnah |
| 15m | sinkt sichtbar | steigt | bleibt zentrumsnah |
| 1h | sinkt leicht | steigt | bleibt zentrumsnah |

Kurz:

```text
PAXG bleibt PAXG,
aber das Folgefenster liest sich gedämpfter.
```

## Interpretation

Der Befund ist wichtig, weil er zwei Ebenen trennt:

1. Die MCM-Topologie bleibt stabil.
2. Die lokale Feldfärbung ist phasenabhängig.

PAXG 2025 wird im Folgefenster nicht zu einer anderen Topologie. Es wirkt eher so, als würde dieselbe Weltqualität mehr Abstand, Dämpfung und Schutz aufnehmen.

Das passt zur bisherigen MCM-Lesart:

```text
Stabilität ohne starre Kopie.
Drift ohne Topologiebruch.
```

## Methodische Grenze

Diese Prüfung zeigt einen Folgeabschnitt, aber noch keine vollständige Jahresbewegung. Der nächste sinnvolle Schritt ist entweder ein zweites verschobenes Fenster oder ein längerer 10k-Gesamtvergleich.

## Referenzen

- [paxg_2025_holdout_shift_compare.md](../../../../reports/paxg_2025_holdout_shift_compare.md)
- [paxg_2025_shift1_topology.md](../../../../reports/paxg_2025_shift1_topology.md)
- [paxg_2025_shift1_randdruck.md](../../../../reports/paxg_2025_shift1_randdruck.md)
