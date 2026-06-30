# 1129 - Brueckenkandidaten Btc Quiet Bindung

Diese Diagnose ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Frage

Woran sind die neuen Brueckenkandidaten gebunden: Asset, Zeitrahmen, Rezeptorhaltung, Tonband oder Feldfolge?

## Bindungsmatrix

| Familie | Lesart | Asset | TF | Events | Welten | Visual | Ton | Feld | Spannung | Rekopplung | Strain | Hoeren | Schaerfe | Intake |
|---|---|---|---|---:|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| dio_00ly | tragende_verarbeitung | BTC | 5m | 20 | 1 | wechselnde_form:16;stabile_scharfe_form:4 | geordnetes_hinhoeren_mit_wechsel:16;geordnetes_hinhoeren:4 | rekoppelt:18;offen:2 | 0.0728 | 0.7255 | 0.1320 | 0.8277 | 0.6681 | 0.0728 |
| dio_0pq6 | tragende_verarbeitung | BTC | 5m | 2 | 1 | stabile_scharfe_form:2 | geordnetes_hinhoeren_mit_wechsel:2 | offen:2 | 0.0648 | 0.7190 | 0.1309 | 0.8486 | 0.7438 | 0.0648 |

## Technische Lesart

- `dio_00ly`: `20` Ereignisse, Assets `BTC`, Zeitrahmen `5m`, Lesarten `tragende_verarbeitung`.
- `dio_0pq6`: `2` Ereignisse, Assets `BTC`, Zeitrahmen `5m`, Lesarten `tragende_verarbeitung`.

## Grenze

Die Matrix beschreibt Bindung, nicht Bedeutung. Eine Familie wird erst belastbarer, wenn sie in weiteren Weltgruppen aehnlich gebunden bleibt.

## Wie es weitergeht

Als naechstes sollte geprueft werden, ob die Bindung aus Asset, Zeitrahmen und Rezeptorhaltung bei frisch erzeugten Folgewelten wieder auftaucht.
