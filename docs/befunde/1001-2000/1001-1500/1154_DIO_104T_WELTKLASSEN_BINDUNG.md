# 1154 - Dio 104T Weltklassen Bindung

Diese Diagnose ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Frage

Woran sind die neuen Brueckenkandidaten gebunden: Asset, Zeitrahmen, Rezeptorhaltung, Tonband oder Feldfolge?

## Bindungsmatrix

| Familie | Lesart | Asset | TF | Events | Welten | Visual | Ton | Feld | Spannung | Rekopplung | Strain | Hoeren | Schaerfe | Intake |
|---|---|---|---|---:|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| dio_104t | kippnaehe | BTC | 5m | 2 | 1 | wechselnde_form:2 | geordnetes_hinhoeren:2 | offen:2 | 0.0653 | 0.6656 | 0.1630 | 0.8782 | 0.6298 | 0.0653 |
| dio_104t | kippnaehe | PAXG | 5m | 2 | 1 | wechselnde_form:2 | geordnetes_hinhoeren:2 | belastet_kippnah:2 | 0.1009 | 0.6796 | 0.1852 | 0.8321 | 0.5744 | 0.1009 |
| dio_104t | kippnaehe | UNBEKANNT | 5m | 2 | 1 | stabile_scharfe_form:2 | geordnetes_hinhoeren_mit_wechsel:2 | offen:2 | 0.0892 | 0.6603 | 0.1713 | 0.7910 | 0.7145 | 0.0892 |
| dio_104t | tragende_verarbeitung | UNBEKANNT | 5m | 45 | 4 | wechselnde_form:37;stabile_scharfe_form:8 | geordnetes_hinhoeren_mit_wechsel:35;geordnetes_hinhoeren:10 | rekoppelt:28;offen:17 | 0.0701 | 0.7218 | 0.1341 | 0.8433 | 0.6687 | 0.0701 |
| dio_104t | tragende_verarbeitung | BTC | 5m | 23 | 1 | wechselnde_form:17;stabile_scharfe_form:6 | geordnetes_hinhoeren_mit_wechsel:17;geordnetes_hinhoeren:6 | rekoppelt:23 | 0.0665 | 0.7305 | 0.1365 | 0.8483 | 0.6839 | 0.0665 |
| dio_104t | tragende_verarbeitung | KAS | 5m | 18 | 1 | wechselnde_form:18 | geordnetes_hinhoeren_mit_wechsel:12;geordnetes_hinhoeren:6 | rekoppelt:18 | 0.0688 | 0.7262 | 0.1358 | 0.8463 | 0.6568 | 0.0688 |
| dio_104t | tragende_verarbeitung | BTC | 1h | 9 | 1 | wechselnde_form:9 | geordnetes_hinhoeren_mit_wechsel:7;geordnetes_hinhoeren:2 | rekoppelt:9 | 0.0668 | 0.7286 | 0.1353 | 0.8556 | 0.6610 | 0.0668 |
| dio_104t | tragende_verarbeitung | PAXG | 5m | 2 | 1 | wechselnde_form:2 | geordnetes_hinhoeren_mit_wechsel:2 | rekoppelt:2 | 0.0782 | 0.7305 | 0.1332 | 0.8177 | 0.6602 | 0.0782 |

## Technische Lesart

- `dio_104t`: `103` Ereignisse, Assets `BTC, KAS, PAXG, UNBEKANNT`, Zeitrahmen `1h, 5m`, Lesarten `kippnaehe, tragende_verarbeitung`.

## Grenze

Die Matrix beschreibt Bindung, nicht Bedeutung. Eine Familie wird erst belastbarer, wenn sie in weiteren Weltgruppen aehnlich gebunden bleibt.

## Wie es weitergeht

Als naechstes sollte geprueft werden, ob die Bindung aus Asset, Zeitrahmen und Rezeptorhaltung bei frisch erzeugten Folgewelten wieder auftaucht.
