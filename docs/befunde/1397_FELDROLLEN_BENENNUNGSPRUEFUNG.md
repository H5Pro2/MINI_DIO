# 1397 - Feldrollen Benennungspruefung

## Zweck

Diese Diagnose prueft, ob die bisherige Rollenbezeichnung aus `1394` fachlich zur Rohwelt-Ruecklesung aus `1396` passt.

## Befund

- `gerichtete_spannungsrolle`: Fenster `3`, avg_range `3.871200`, avg_wechsel `47.666667`, Spannungen `enge_unruhige_spannung:2 | weite_unruhige_spannung:1`, Bewertung `name_derzeit_plausibel`
- `offene_nachbarschaftsrolle`: Fenster `5`, avg_range `2.141738`, avg_wechsel `6.000000`, Spannungen `ruhige_bis_mittlere_spannung:5`, Bewertung `nicht_genug_daten`
- `ruhige_feldnaehe`: Fenster `1`, avg_range `20.969168`, avg_wechsel `0.000000`, Spannungen `weite_gerichtete_spannung:1`, Bewertung `nicht_genug_daten`
- `weite_weltspannungsnaehe`: Fenster `9`, avg_range `3.493333`, avg_wechsel `47.333333`, Spannungen `enge_unruhige_spannung:5 | weite_unruhige_spannung:2 | weite_gerichtete_spannung:1 | ruhige_bis_mittlere_spannung:1`, Bewertung `name_zu_eng_unruhe_statt_weite`

## Lesung

`weite_weltspannungsnaehe` ist als Name wahrscheinlich zu eng.
Die Rolle wird im Kontrast-Holdout auch durch enge, aber stark wechselnde Weltspannung beruehrt.
Der synthetisch glatte Kontrolllauf beruehrt diese Rolle nicht stark, sondern landet bei `offene_nachbarschaftsrolle`.
Die ruhige Driftwelt bleibt ebenfalls nur schwach bei `offene_nachbarschaftsrolle` und bildet keine starke Spannungsnaehe.
Die High-Noisy-Drift beruehrt Spannungsnaehe nur schwach. Mehr Rauschen allein reicht also nicht aus, um eine starke Spannungsnaehe zu erzeugen.
Fachlich genauer waere vorerst `unruhige_spannungsnaehe`: eine Feldrolle, die nicht nur grosse Range, sondern allgemein unruhige Spannungsdichte traegt.

## Grenze

Das ist eine Benennungspruefung, keine Umbenennung im Code.
Die bestehende Datenkette bleibt reproduzierbar.

## Wie es weitergeht

Als naechstes sollte eine kombinierte Stresswelt geprueft werden: groessere Range, dichtere Wechsel und staerkere Ton-/Rezeptorverdichtung gemeinsam. Entscheidend ist, ob erst die Kopplung mehrerer Belastungsqualitaeten Spannungsnaehe aktiviert.
