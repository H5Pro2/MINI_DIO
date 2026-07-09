# 1147 - Dio 104T Drei Weltklassen Bindung

Diese Diagnose ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Frage

Woran sind die neuen Brueckenkandidaten gebunden: Asset, Zeitrahmen, Rezeptorhaltung, Tonband oder Feldfolge?

## Bindungsmatrix

| Familie | Lesart | Asset | TF | Events | Welten | Visual | Ton | Feld | Spannung | Rekopplung | Strain | Hoeren | Schaerfe | Intake |
|---|---|---|---|---:|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| dio_104t | kippnaehe | BTC | 5m | 2 | 1 | wechselnde_form:2 | geordnetes_hinhoeren:2 | offen:2 | 0.0653 | 0.6656 | 0.1630 | 0.8782 | 0.6298 | 0.0653 |
| dio_104t | kippnaehe | UNBEKANNT | 5m | 2 | 1 | stabile_scharfe_form:2 | geordnetes_hinhoeren_mit_wechsel:2 | offen:2 | 0.0892 | 0.6603 | 0.1713 | 0.7910 | 0.7145 | 0.0892 |
| dio_104t | tragende_verarbeitung | BTC | 5m | 23 | 1 | wechselnde_form:17;stabile_scharfe_form:6 | geordnetes_hinhoeren_mit_wechsel:17;geordnetes_hinhoeren:6 | rekoppelt:23 | 0.0665 | 0.7305 | 0.1365 | 0.8483 | 0.6839 | 0.0665 |
| dio_104t | tragende_verarbeitung | UNBEKANNT | 5m | 19 | 2 | wechselnde_form:15;stabile_scharfe_form:4 | geordnetes_hinhoeren_mit_wechsel:17;geordnetes_hinhoeren:2 | rekoppelt:10;offen:9 | 0.0714 | 0.7196 | 0.1343 | 0.8368 | 0.6664 | 0.0714 |

## Technische Lesart

- `dio_104t`: `46` Ereignisse, Assets `BTC, UNBEKANNT`, Zeitrahmen `5m`, Lesarten `kippnaehe, tragende_verarbeitung`.

## Grenze

Die Matrix beschreibt Bindung, nicht Bedeutung. Eine Familie wird erst belastbarer, wenn sie in weiteren Weltgruppen aehnlich gebunden bleibt.

## Wie es weitergeht

Als naechstes sollte geprueft werden, ob die Bindung aus Asset, Zeitrahmen und Rezeptorhaltung bei frisch erzeugten Folgewelten wieder auftaucht.
