# Visuelle Feldkopplung - Diagnose

Stand: 2026-06-19 06:36:43

## Zweck

Diese Diagnose legt visuelle Sehzustande gegen MCM-Feldlast, Memorylast und Rekopplung.
Sie prueft, ob Sehen nur Oberflaechenform bleibt oder messbar mit dem Innenfeld gekoppelt ist.

Wichtig: Das ist keine Handlung, kein Gate und kein Entry-Signal.

Hierarchie der Pruefung:

1. Grundfrage: Koppeln visuelle Formzustaende messbar an MCM-Feldwirkung?
2. Unterpruefung: aktive Sehanteile, visuelle Filter-/Hintergrundanteile, Feldbindung und Rekopplung vergleichen.
3. Folgeschritt: Bestimmen, wann sichtbare Form entlastet, bindet oder als offene Sehkopplung stehen bleibt.

## Einzelwerte

| Welt | Gruppe | Rolle | visuelle Kopplung | aktiv sehen | Filter/Hintergrund | Sehlast | Sehentlastung | Feldbindung | Kopplungsluecke | Fit | Rekopplung |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| SOL_2024_5M | referenz | reiz_aktiv_rekoppelnd | offene_sehkopplung | 0.0261 | 0.9739 | 0.1607 | 0.2471 | 0.0517 | 0.0000 | 0.8910 | 0.622776 |
| SOL_2025_5M | referenz | reiz_aktiv_rekoppelnd | offene_sehkopplung | 0.0015 | 0.9985 | 0.1120 | 0.2417 | 0.0161 | 0.0000 | 0.9041 | 0.636504 |
| STRESS_2023_TEST4 | stress | last_memory_bindend | sehlast_feldnah | 0.2553 | 0.7447 | 0.2675 | 0.1962 | 0.2052 | 0.0091 | 0.9377 | 0.596927 |
| STRESS_2024_REAL | stress | uebergang_bindend | offene_sehkopplung | 0.1915 | 0.8085 | 0.2575 | 0.2083 | 0.1907 | 0.0000 | 0.9332 | 0.601652 |
| STRESS_2025_STRESS | stress | last_memory_bindend | sehlast_feldnah | 0.2660 | 0.7340 | 0.2619 | 0.1915 | 0.2076 | 0.0161 | 0.9456 | 0.594327 |
| SOL_2024_1H | vergleich | last_memory_bindend | sehlast_feldnah | 0.3164 | 0.6836 | 0.2988 | 0.1820 | 0.2551 | 0.0730 | 0.9562 | 0.587027 |
| SOL_2024_30M | vergleich | uebergang_bindend | offene_sehkopplung | 0.1780 | 0.8220 | 0.2435 | 0.2156 | 0.1616 | 0.0000 | 0.9182 | 0.600205 |
| SOL_2025_1H | vergleich | last_memory_bindend | sehlast_feldnah | 0.2934 | 0.7066 | 0.2905 | 0.1880 | 0.2366 | 0.0487 | 0.9461 | 0.589067 |
| SOL_2025_30M | vergleich | uebergang_bindend | offene_sehkopplung | 0.1770 | 0.8230 | 0.2414 | 0.2142 | 0.1681 | 0.0000 | 0.9266 | 0.600912 |

## Rollenzaehlung

- `offene_sehkopplung`: `5`
- `sehlast_feldnah`: `4`

## Lesart

- `visuell_entlastend`: Form bleibt sichtbar, aber Feldbindung bleibt niedrig.
- `filtert_aber_feld_bindet`: visuelle Filterung ist vorhanden, Feld/Memory binden trotzdem.
- `sehlast_feldnah`: visuelle Last und Feldbindung liegen nah beieinander.
- `aktive_form_rekoppelnd`: aktive Formwahrnehmung bleibt mit guter Rekopplung verbunden.
- `offene_sehkopplung`: Sehzustand ist noch nicht eindeutig interpretierbar.

## Vorlaeufiger Befund

Diese Diagnose trennt Sehen von Feldwirkung.
Eine Form kann sichtbar, stabil oder unruhig sein, ohne automatisch als Feldlast zu gelten.
Feldlast entsteht erst, wenn sichtbare Form, Memorylast und Rekopplung gemeinsam binden.

## Wie es weitergeht

Als naechstes wird der Befund geschrieben.
Danach koennen Hoeren, Sehen und Fuehlen als multisensorische Kopplung verglichen werden.
