# Rekopplungsqualitaet - Diagnose

Stand: 2026-06-19 04:50:03

## Zweck

Diese Diagnose prueft passiv, warum manche Welten trotz Aufmerksamkeit gut rekoppeln und andere in Feld-/Memorylast binden.
Sie ist keine Handlung, kein Gate und keine Strategie.

Hierarchie der Pruefung:

1. Grundfrage: Warum rekoppeln manche Welten besser als andere?
2. Unterpruefung: Reizaktivitaet, Feldlast, Memorylast, Nachhall und Entrueckung getrennt lesen.
3. Folgeschritt: Entscheiden, ob `last_bindend` und `reiz_aktiv_rekoppelnd` stabile passive Rollen sind.

## Rollenkarte

| Welt | Rolle | Rekopplung | Rek-Verlust | Feldlast | Memorylast | Aufmerksamkeit | Nachhall | aktiv-rekoppelnd | Bindungssumme | lastbindend | memorybindend | nachhall-rekoppelnd | feld-entrueckt |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| AUTO_STRESS_EXTREME_EXPANSION | nachhall_rekoppelnd | 0.618465 | 0.0215 | 0.0785 | 0.1036 | 0.3661 | 0.1660 | 0.5737 | 0.2489 | 0.0795 | 0.0901 | 0.4926 | 0.0794 |
| EXPANSION_2023_EXTREME | reiz_aktiv_rekoppelnd | 0.623022 | 0.0170 | 0.0604 | 0.0875 | 0.3811 | 0.1715 | 0.5998 | 0.2167 | 0.0698 | 0.0770 | 0.5060 | 0.0699 |
| EXPANSION_2023_POSITIVE_10k | reiz_aktiv_rekoppelnd | 0.632556 | 0.0074 | 0.0366 | 0.0571 | 0.4063 | 0.1834 | 0.6485 | 0.1556 | 0.0530 | 0.0538 | 0.5387 | 0.0488 |
| EXPANSION_2025_RECOVERY | reiz_aktiv_rekoppelnd | 0.630474 | 0.0095 | 0.0332 | 0.0573 | 0.4175 | 0.1857 | 0.6470 | 0.1628 | 0.0553 | 0.0546 | 0.5299 | 0.0530 |
| LATE_NEGATIVE_2025_2k | reiz_aktiv_rekoppelnd | 0.630192 | 0.0098 | 0.0341 | 0.0587 | 0.3875 | 0.1711 | 0.6332 | 0.1583 | 0.0521 | 0.0544 | 0.5292 | 0.0518 |
| NEGATIVE_2023_MODERATE_2k | reiz_aktiv_rekoppelnd | 0.629660 | 0.0103 | 0.0336 | 0.0527 | 0.4225 | 0.1979 | 0.6462 | 0.1642 | 0.0578 | 0.0536 | 0.5335 | 0.0529 |
| NEGATIVE_2023_STRESS | reiz_aktiv_rekoppelnd | 0.630398 | 0.0096 | 0.0302 | 0.0594 | 0.4244 | 0.1992 | 0.6503 | 0.1677 | 0.0572 | 0.0562 | 0.5340 | 0.0543 |
| POSITIVE_STRESS_2024_2k | reiz_aktiv_rekoppelnd | 0.631225 | 0.0088 | 0.0241 | 0.0396 | 0.3729 | 0.1598 | 0.6330 | 0.1346 | 0.0455 | 0.0414 | 0.5353 | 0.0476 |
| SIDEWAYS_2026_2k | nachhall_rekoppelnd | 0.622030 | 0.0180 | 0.0602 | 0.0878 | 0.3723 | 0.1640 | 0.5928 | 0.2154 | 0.0682 | 0.0770 | 0.5052 | 0.0702 |
| STRESS_SEGMENT_2023 | last_memory_bindend | 0.596927 | 0.0431 | 0.2660 | 0.2447 | 0.1409 | 0.0443 | 0.3609 | 0.4903 | 0.1510 | 0.1940 | 0.4325 | 0.1453 |

## Schwaechste Rekopplung

- `STRESS_SEGMENT_2023`: Rekopplungsverlust `0.0431`, Feldlast `0.2660`, Memorylast `0.2447`, Rolle `last_memory_bindend`
- `AUTO_STRESS_EXTREME_EXPANSION`: Rekopplungsverlust `0.0215`, Feldlast `0.0785`, Memorylast `0.1036`, Rolle `nachhall_rekoppelnd`
- `SIDEWAYS_2026_2k`: Rekopplungsverlust `0.0180`, Feldlast `0.0602`, Memorylast `0.0878`, Rolle `nachhall_rekoppelnd`
- `EXPANSION_2023_EXTREME`: Rekopplungsverlust `0.0170`, Feldlast `0.0604`, Memorylast `0.0875`, Rolle `reiz_aktiv_rekoppelnd`
- `NEGATIVE_2023_MODERATE_2k`: Rekopplungsverlust `0.0103`, Feldlast `0.0336`, Memorylast `0.0527`, Rolle `reiz_aktiv_rekoppelnd`

## Reizaktiv aber rekoppelnd

- `NEGATIVE_2023_STRESS`: aktiv-rekoppelnd `0.6503`, Aufmerksamkeit `0.4244`, Rekopplung `0.630398`
- `EXPANSION_2023_POSITIVE_10k`: aktiv-rekoppelnd `0.6485`, Aufmerksamkeit `0.4063`, Rekopplung `0.632556`
- `EXPANSION_2025_RECOVERY`: aktiv-rekoppelnd `0.6470`, Aufmerksamkeit `0.4175`, Rekopplung `0.630474`
- `NEGATIVE_2023_MODERATE_2k`: aktiv-rekoppelnd `0.6462`, Aufmerksamkeit `0.4225`, Rekopplung `0.629660`
- `LATE_NEGATIVE_2025_2k`: aktiv-rekoppelnd `0.6332`, Aufmerksamkeit `0.3875`, Rekopplung `0.630192`

## Last- und memorybindend

- `STRESS_SEGMENT_2023`: lastbindend `0.1510`, memorybindend `0.1940`, feld-entrueckt `0.1453`
- `AUTO_STRESS_EXTREME_EXPANSION`: lastbindend `0.0795`, memorybindend `0.0901`, feld-entrueckt `0.0794`
- `EXPANSION_2023_EXTREME`: lastbindend `0.0698`, memorybindend `0.0770`, feld-entrueckt `0.0699`
- `SIDEWAYS_2026_2k`: lastbindend `0.0682`, memorybindend `0.0770`, feld-entrueckt `0.0702`
- `NEGATIVE_2023_STRESS`: lastbindend `0.0572`, memorybindend `0.0562`, feld-entrueckt `0.0543`

## Lesart

- `reiz_aktiv_rekoppelnd`: Welt ist aufmerksamkeitsnah, aber das Feld kommt gut zurueck.
- `last_bindend`: Feldlast und Rekopplungsverlust binden die Weltwirkung.
- `memory_bindend`: Episodenspuren halten die Weltwirkung staerker im Feld.
- `nachhall_rekoppelnd`: Nachhall ist da, bleibt aber mit Rekopplung verbunden.
- `feld_entrueckt`: Rekopplung und Tragqualitaet sinken zusammen.

## Befund

Die Rollen sind passive Auswertungsnamen.
Sie beschreiben keine festen Mechaniken im Kern.

Wenn die Rollen ueber weitere Welten stabil bleiben, entsteht daraus eine Rekopplungslandkarte:
Welche Welt wirkt aktiv und bleibt loesbar, welche bindet das Feld, welche schreibt Memorylast?

## Wie es weitergeht

Als naechstes wird ein Befund geschrieben.
Dabei steht die Unterscheidung zwischen `reiz_aktiv_rekoppelnd` und `last_bindend` im Mittelpunkt.
