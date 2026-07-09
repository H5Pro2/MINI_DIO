# 1396 - Holdout Rohwelt-Ruecklesung

## Zweck

Diese Diagnose liest die starken Holdout-Nachbarschaften aus `1395` in die konkrete Rohwelt zurueck.

## Befund

- starke Holdout-Fenster: `18`
- Rollen: `weite_weltspannungsnaehe:9, offene_nachbarschaftsrolle:5, gerichtete_spannungsrolle:3, ruhige_feldnaehe:1`
- Weltspannungen: `enge_unruhige_spannung:7, ruhige_bis_mittlere_spannung:6, weite_unruhige_spannung:3, weite_gerichtete_spannung:2`
- Richtungen: `fallend:9, steigend:8, seitwaerts:1`

## Fenster

- `HOLDOUT_2024_BRIDGE_TEST1:401-500` -> `gerichtete_spannungsrolle`, Spannung `weite_unruhige_spannung`, Richtung `fallend`, Range `8.060738`, Tonshift `0.009385`, Wirkung `stabil:66|tragend_unruhig:34`
- `HOLDOUT_2024_BRIDGE_TEST2:501-600` -> `weite_weltspannungsnaehe`, Spannung `weite_unruhige_spannung`, Richtung `fallend`, Range `6.164595`, Tonshift `-0.000443`, Wirkung `stabil:75|tragend_unruhig:24|kippend:1`
- `HOLDOUT_2024_BRIDGE_TEST2:601-700` -> `weite_weltspannungsnaehe`, Spannung `weite_unruhige_spannung`, Richtung `seitwaerts`, Range `4.265504`, Tonshift `0.000986`, Wirkung `stabil:77|tragend_unruhig:23`
- `HOLDOUT_2024_BRIDGE_TEST2:901-994` -> `weite_weltspannungsnaehe`, Spannung `weite_gerichtete_spannung`, Richtung `fallend`, Range `4.664723`, Tonshift `-0.000732`, Wirkung `stabil:73|tragend_unruhig:20|kippend:1`
- `HOLDOUT_QUIET_SOL2025:101-200` -> `weite_weltspannungsnaehe`, Spannung `enge_unruhige_spannung`, Richtung `steigend`, Range `2.462585`, Tonshift `-0.000783`, Wirkung `stabil:71|tragend_unruhig:27|kippend:2`
- `HOLDOUT_QUIET_SOL2025:601-700` -> `weite_weltspannungsnaehe`, Spannung `enge_unruhige_spannung`, Richtung `fallend`, Range `3.495824`, Tonshift `-0.000734`, Wirkung `stabil:67|tragend_unruhig:32|gespannt:1`
- `HOLDOUT_QUIET_SOL2025:701-800` -> `gerichtete_spannungsrolle`, Spannung `enge_unruhige_spannung`, Richtung `fallend`, Range `1.547744`, Tonshift `0.007006`, Wirkung `stabil:79|tragend_unruhig:20|kippend:1`
- `HOLDOUT_QUIET_SOL2025:901-1000` -> `weite_weltspannungsnaehe`, Spannung `enge_unruhige_spannung`, Richtung `fallend`, Range `3.655543`, Tonshift `0.000906`, Wirkung `stabil:69|tragend_unruhig:31`
- `HOLDOUT_QUIET_SOL2025:1301-1400` -> `weite_weltspannungsnaehe`, Spannung `enge_unruhige_spannung`, Richtung `steigend`, Range `1.011061`, Tonshift `-0.000912`, Wirkung `stabil:90|tragend_unruhig:10`
- `HOLDOUT_QUIET_SOL2025:1401-1500` -> `weite_weltspannungsnaehe`, Spannung `enge_unruhige_spannung`, Richtung `steigend`, Range `3.586142`, Tonshift `-0.000743`, Wirkung `stabil:78|tragend_unruhig:20|kippend:2`
- `HOLDOUT_SMOOTH_CONTROL:301-400` -> `offene_nachbarschaftsrolle`, Spannung `ruhige_bis_mittlere_spannung`, Richtung `steigend`, Range `2.399862`, Tonshift `-0.000909`, Wirkung `stabil:100`
- `HOLDOUT_POSITIVE_EXPANSION:501-600` -> `weite_weltspannungsnaehe`, Spannung `ruhige_bis_mittlere_spannung`, Richtung `fallend`, Range `2.134016`, Tonshift `0.000292`, Wirkung `stabil:80|tragend_unruhig:20`
- `HOLDOUT_POSITIVE_EXPANSION:701-800` -> `gerichtete_spannungsrolle`, Spannung `enge_unruhige_spannung`, Richtung `fallend`, Range `2.005119`, Tonshift `0.007565`, Wirkung `stabil:72|tragend_unruhig:28`
- `HOLDOUT_MEDIUM_QUIET_DRIFT:301-400` -> `offene_nachbarschaftsrolle`, Spannung `ruhige_bis_mittlere_spannung`, Richtung `steigend`, Range `3.248066`, Tonshift `-0.000801`, Wirkung `stabil:100`
- `HOLDOUT_COMBINED_STRESS:201-300` -> `ruhige_feldnaehe`, Spannung `weite_gerichtete_spannung`, Richtung `steigend`, Range `20.969168`, Tonshift `-0.000380`, Wirkung `stabil:100`
- `HOLDOUT_RHYTHM_BLOCK:1-100` -> `offene_nachbarschaftsrolle`, Spannung `ruhige_bis_mittlere_spannung`, Richtung `steigend`, Range `1.632727`, Tonshift `-0.000812`, Wirkung `stabil:89|tragend_unruhig:11`
- `HOLDOUT_RHYTHM_BLOCK:501-600` -> `offene_nachbarschaftsrolle`, Spannung `ruhige_bis_mittlere_spannung`, Richtung `steigend`, Range `1.641213`, Tonshift `-0.000911`, Wirkung `stabil:89|tragend_unruhig:11`
- `HOLDOUT_RHYTHM_WAVE:901-994` -> `offene_nachbarschaftsrolle`, Spannung `ruhige_bis_mittlere_spannung`, Richtung `fallend`, Range `1.786820`, Tonshift `-0.000477`, Wirkung `stabil:94`

## Lesung

Die Holdout-Beruehrungen liegen nicht in chaotischer Kippung, sondern in stabiler Innenwirkung.
Die beruehrten Rollen treten dort auf, wo die Rohwelt als Spannungs- oder Unruhebereich gelesen wird.
Der ruhige SOL-Holdout ist nicht spannungslos: er zeigt kleinere Range, aber hohe Richtungswechsel. Dadurch entsteht `enge_unruhige_spannung` statt reiner Ruhe.
Der synthetisch glatte Kontrolllauf bleibt dagegen bei ruhiger bis mittlerer Spannung und beruehrt `offene_nachbarschaftsrolle`.
Die positive Expansion beruehrt sowohl Spannungsnaehe als auch gerichtete Spannungsrolle, erzwingt aber noch keine neue Mischklasse.
Damit wird `weite_weltspannungsnaehe` als Name fraglich: die Rolle scheint eher unruhige Spannungsnaehe zu tragen, nicht zwingend nur grosse Range.

## Wie es weitergeht

Als naechstes sollte eine kombinierte Stresswelt geprueft werden: nicht nur Rauschen, sondern zugleich groessere Range, dichtere Wechsel und staerkere Ton-/Rezeptorverdichtung. Damit laesst sich pruefen, wann stabile Oberflaechenvarianz in Spannungsnaehe kippt.
