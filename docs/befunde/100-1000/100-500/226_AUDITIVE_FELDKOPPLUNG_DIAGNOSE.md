# Auditive Feldkopplung - Diagnose

Stand: 2026-06-19 05:42:36

## Zweck

Diese Diagnose legt auditive Hoerzustande gegen MCM-Feldlast, Memorylast und Rekopplung.
Sie prueft, ob Hoeren nur Oberflaechenlabel ist oder eine lesbare Feldkopplung besitzt.

Wichtig: Das ist keine Handlung, kein Gate und kein Entry-Signal.

Hierarchie der Pruefung:

1. Grundfrage: Koppeln Hoerzustande messbar an MCM-Feldwirkung?
2. Unterpruefung: aktive Hoeranteile, Filter-/Abklinganteile, Feldbindung und Rekopplung vergleichen.
3. Folgeschritt: Bestimmen, ob Rauschenfiltern und Reizabklingen wirklich entlasten oder ob das Feld trotzdem bindet.

## Einzelwerte

| Welt | Gruppe | Rolle | auditive Kopplung | aktiv hoeren | Filter/Abklingen | Hoerlast | Hoerentlastung | Feldbindung | Kopplungsluecke | Fit | Rekopplung |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| SOL_2024_5M | referenz | reiz_aktiv_rekoppelnd | offene_hoerkopplung | 0.3762 | 0.5673 | 0.2374 | 0.1574 | 0.0517 | 0.0000 | 0.8143 | 0.622776 |
| SOL_2025_5M | referenz | reiz_aktiv_rekoppelnd | offene_hoerkopplung | 0.3792 | 0.5638 | 0.2370 | 0.1580 | 0.0161 | 0.0000 | 0.7791 | 0.636504 |
| STRESS_2023_TEST4 | stress | last_memory_bindend | offene_hoerkopplung | 0.1616 | 0.7980 | 0.1267 | 0.1840 | 0.2052 | 0.0212 | 0.9214 | 0.596927 |
| STRESS_2024_REAL | stress | uebergang_bindend | offene_hoerkopplung | 0.3737 | 0.6061 | 0.2508 | 0.1527 | 0.1907 | 0.0380 | 0.9399 | 0.601652 |
| STRESS_2025_STRESS | stress | last_memory_bindend | hoerlast_feldnah | 0.2424 | 0.7374 | 0.1929 | 0.1863 | 0.2076 | 0.0213 | 0.9854 | 0.594327 |
| SOL_2024_1H | vergleich | last_memory_bindend | hoerlast_feldnah | 0.3602 | 0.5788 | 0.2257 | 0.1553 | 0.2551 | 0.0997 | 0.9707 | 0.587027 |
| SOL_2024_30M | vergleich | uebergang_bindend | offene_hoerkopplung | 0.3477 | 0.5893 | 0.2264 | 0.1577 | 0.1616 | 0.0040 | 0.9352 | 0.600205 |
| SOL_2025_1H | vergleich | last_memory_bindend | hoerlast_feldnah | 0.3562 | 0.5988 | 0.2268 | 0.1535 | 0.2366 | 0.0831 | 0.9901 | 0.589067 |
| SOL_2025_30M | vergleich | uebergang_bindend | offene_hoerkopplung | 0.3492 | 0.5903 | 0.2211 | 0.1599 | 0.1681 | 0.0081 | 0.9470 | 0.600912 |

## Rollenzaehlung

- `hoerlast_feldnah`: `3`
- `offene_hoerkopplung`: `6`

## Lesart

- `hoerfilter_entlastend`: Filter-/Abklinganteile sind hoch und Feldbindung bleibt niedrig.
- `filtert_aber_feld_bindet`: Hoerfilter ist vorhanden, aber Feld/Memory binden trotzdem.
- `hoerlast_feldnah`: auditive Last und Feldbindung liegen nah beieinander.
- `aktiv_rekoppelnd`: aktives Hoeren bleibt mit guter Rekopplung verbunden.
- `offene_hoerkopplung`: Hoerzustand ist noch nicht eindeutig interpretierbar.

## Vorlaeufiger Befund

Diese Diagnose trennt Hoeren von Feldwirkung.
Rauschenfiltern oder Reizabklingen ist nur dann entlastend, wenn die Feldbindung niedrig bleibt.
Wenn Feldlast und Memorylast hoch bleiben, ist auditive Filterung allein nicht ausreichend.

## Wie es weitergeht

Als naechstes wird der Befund geschrieben.
Dort wird bewertet, ob SOL 5m eine entlastende Hoerkopplung zeigt und warum Stress/1h trotz Filterung binden kann.
