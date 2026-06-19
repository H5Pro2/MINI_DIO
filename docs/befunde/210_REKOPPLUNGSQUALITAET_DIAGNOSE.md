# Rekopplungsqualitaet - Diagnose

Stand: 2026-06-19 04:47:02

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
| BTC_2024_15m | nachhall_rekoppelnd | 0.631196 | 0.0088 | 0.0416 | 0.0527 | 0.3555 | 0.1718 | 0.6214 | 0.1587 | 0.0551 | 0.0520 | 0.5459 | 0.0516 |
| BTC_2024_1h | nachhall_rekoppelnd | 0.610376 | 0.0296 | 0.1389 | 0.1650 | 0.3742 | 0.1959 | 0.5351 | 0.3592 | 0.1160 | 0.1379 | 0.4685 | 0.1053 |
| BTC_2024_30m | nachhall_rekoppelnd | 0.626156 | 0.0138 | 0.0647 | 0.0898 | 0.3526 | 0.1770 | 0.5975 | 0.2121 | 0.0692 | 0.0778 | 0.5275 | 0.0650 |
| BTC_2024_5m | reiz_aktiv_rekoppelnd | 0.636577 | 0.0034 | 0.0211 | 0.0316 | 0.4110 | 0.1980 | 0.6679 | 0.1256 | 0.0473 | 0.0373 | 0.5588 | 0.0410 |
| BTC_2025_15m | nachhall_rekoppelnd | 0.631429 | 0.0086 | 0.0396 | 0.0627 | 0.3776 | 0.1785 | 0.6319 | 0.1645 | 0.0551 | 0.0573 | 0.5433 | 0.0521 |
| BTC_2025_1h | nachhall_rekoppelnd | 0.611240 | 0.0288 | 0.1414 | 0.1740 | 0.3666 | 0.1900 | 0.5342 | 0.3623 | 0.1150 | 0.1421 | 0.4726 | 0.1052 |
| BTC_2025_30m | nachhall_rekoppelnd | 0.623087 | 0.0169 | 0.0662 | 0.0838 | 0.3502 | 0.1695 | 0.5857 | 0.2161 | 0.0712 | 0.0758 | 0.5179 | 0.0691 |
| BTC_2025_5m | reiz_aktiv_rekoppelnd | 0.638380 | 0.0016 | 0.0221 | 0.0436 | 0.4473 | 0.2149 | 0.6891 | 0.1347 | 0.0492 | 0.0442 | 0.5630 | 0.0413 |
| SOL_2024_15m | nachhall_rekoppelnd | 0.606542 | 0.0335 | 0.1334 | 0.1550 | 0.3502 | 0.1570 | 0.5133 | 0.3477 | 0.1091 | 0.1305 | 0.4484 | 0.1081 |
| SOL_2024_1h | last_memory_bindend | 0.587027 | 0.0530 | 0.3159 | 0.3225 | 0.3538 | 0.1614 | 0.4047 | 0.6315 | 0.1995 | 0.2566 | 0.3646 | 0.1754 |
| SOL_2024_30m | uebergang_bindend | 0.600205 | 0.0398 | 0.1830 | 0.2212 | 0.3520 | 0.1565 | 0.4806 | 0.4398 | 0.1337 | 0.1759 | 0.4183 | 0.1302 |
| SOL_2024_5m | reiz_aktiv_rekoppelnd | 0.622776 | 0.0172 | 0.0527 | 0.0747 | 0.3743 | 0.1706 | 0.5980 | 0.1997 | 0.0651 | 0.0692 | 0.5071 | 0.0654 |
| SOL_2025_15m | nachhall_rekoppelnd | 0.615512 | 0.0245 | 0.1093 | 0.1239 | 0.3512 | 0.1563 | 0.5500 | 0.2867 | 0.0920 | 0.1062 | 0.4805 | 0.0886 |
| SOL_2025_1h | last_memory_bindend | 0.589067 | 0.0509 | 0.2944 | 0.2964 | 0.3532 | 0.1707 | 0.4165 | 0.5965 | 0.1905 | 0.2393 | 0.3815 | 0.1666 |
| SOL_2025_30m | uebergang_bindend | 0.600912 | 0.0391 | 0.2016 | 0.2177 | 0.3449 | 0.1573 | 0.4756 | 0.4475 | 0.1408 | 0.1768 | 0.4238 | 0.1300 |
| SOL_2025_5m | reiz_aktiv_rekoppelnd | 0.636504 | 0.0035 | 0.0140 | 0.0276 | 0.3821 | 0.1712 | 0.6572 | 0.1107 | 0.0398 | 0.0320 | 0.5531 | 0.0390 |

## Schwaechste Rekopplung

- `SOL_2024_1h`: Rekopplungsverlust `0.0530`, Feldlast `0.3159`, Memorylast `0.3225`, Rolle `last_memory_bindend`
- `SOL_2025_1h`: Rekopplungsverlust `0.0509`, Feldlast `0.2944`, Memorylast `0.2964`, Rolle `last_memory_bindend`
- `SOL_2024_30m`: Rekopplungsverlust `0.0398`, Feldlast `0.1830`, Memorylast `0.2212`, Rolle `uebergang_bindend`
- `SOL_2025_30m`: Rekopplungsverlust `0.0391`, Feldlast `0.2016`, Memorylast `0.2177`, Rolle `uebergang_bindend`
- `SOL_2024_15m`: Rekopplungsverlust `0.0335`, Feldlast `0.1334`, Memorylast `0.1550`, Rolle `nachhall_rekoppelnd`

## Reizaktiv aber rekoppelnd

- `BTC_2025_5m`: aktiv-rekoppelnd `0.6891`, Aufmerksamkeit `0.4473`, Rekopplung `0.638380`
- `BTC_2024_5m`: aktiv-rekoppelnd `0.6679`, Aufmerksamkeit `0.4110`, Rekopplung `0.636577`
- `SOL_2025_5m`: aktiv-rekoppelnd `0.6572`, Aufmerksamkeit `0.3821`, Rekopplung `0.636504`
- `BTC_2025_15m`: aktiv-rekoppelnd `0.6319`, Aufmerksamkeit `0.3776`, Rekopplung `0.631429`
- `BTC_2024_15m`: aktiv-rekoppelnd `0.6214`, Aufmerksamkeit `0.3555`, Rekopplung `0.631196`

## Last- und memorybindend

- `SOL_2024_1h`: lastbindend `0.1995`, memorybindend `0.2566`, feld-entrueckt `0.1754`
- `SOL_2025_1h`: lastbindend `0.1905`, memorybindend `0.2393`, feld-entrueckt `0.1666`
- `SOL_2025_30m`: lastbindend `0.1408`, memorybindend `0.1768`, feld-entrueckt `0.1300`
- `SOL_2024_30m`: lastbindend `0.1337`, memorybindend `0.1759`, feld-entrueckt `0.1302`
- `BTC_2025_1h`: lastbindend `0.1150`, memorybindend `0.1421`, feld-entrueckt `0.1052`

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
