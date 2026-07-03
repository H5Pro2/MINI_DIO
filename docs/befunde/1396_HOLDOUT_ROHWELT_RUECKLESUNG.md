# 1396 - Holdout Rohwelt-Ruecklesung

## Zweck

Diese Diagnose liest die starken Holdout-Nachbarschaften aus `1395` in die konkrete Rohwelt zurueck.

## Befund

- starke Holdout-Fenster: `14`
- Rollen: `weite_weltspannungsnaehe:9, gerichtete_spannungsrolle:3, offene_nachbarschaftsrolle:2`
- Weltspannungen: `enge_unruhige_spannung:7, weite_unruhige_spannung:3, ruhige_bis_mittlere_spannung:3, weite_gerichtete_spannung:1`
- Richtungen: `fallend:8, steigend:5, seitwaerts:1`

## Fenster

- `HOLDOUT_2024_BRIDGE_TEST1:401-500` -> `gerichtete_spannungsrolle`, Spannung `weite_unruhige_spannung`, Richtung `fallend`, Range `8.060738`, Tonshift `0.009385`
- `HOLDOUT_2024_BRIDGE_TEST2:501-600` -> `weite_weltspannungsnaehe`, Spannung `weite_unruhige_spannung`, Richtung `fallend`, Range `6.164595`, Tonshift `-0.000443`
- `HOLDOUT_2024_BRIDGE_TEST2:601-700` -> `weite_weltspannungsnaehe`, Spannung `weite_unruhige_spannung`, Richtung `seitwaerts`, Range `4.265504`, Tonshift `0.000986`
- `HOLDOUT_2024_BRIDGE_TEST2:901-994` -> `weite_weltspannungsnaehe`, Spannung `weite_gerichtete_spannung`, Richtung `fallend`, Range `4.664723`, Tonshift `-0.000732`
- `HOLDOUT_QUIET_SOL2025:101-200` -> `weite_weltspannungsnaehe`, Spannung `enge_unruhige_spannung`, Richtung `steigend`, Range `2.462585`, Tonshift `-0.000783`
- `HOLDOUT_QUIET_SOL2025:601-700` -> `weite_weltspannungsnaehe`, Spannung `enge_unruhige_spannung`, Richtung `fallend`, Range `3.495824`, Tonshift `-0.000734`
- `HOLDOUT_QUIET_SOL2025:701-800` -> `gerichtete_spannungsrolle`, Spannung `enge_unruhige_spannung`, Richtung `fallend`, Range `1.547744`, Tonshift `0.007006`
- `HOLDOUT_QUIET_SOL2025:901-1000` -> `weite_weltspannungsnaehe`, Spannung `enge_unruhige_spannung`, Richtung `fallend`, Range `3.655543`, Tonshift `0.000906`
- `HOLDOUT_QUIET_SOL2025:1301-1400` -> `weite_weltspannungsnaehe`, Spannung `enge_unruhige_spannung`, Richtung `steigend`, Range `1.011061`, Tonshift `-0.000912`
- `HOLDOUT_QUIET_SOL2025:1401-1500` -> `weite_weltspannungsnaehe`, Spannung `enge_unruhige_spannung`, Richtung `steigend`, Range `3.586142`, Tonshift `-0.000743`
- `HOLDOUT_SMOOTH_CONTROL:301-400` -> `offene_nachbarschaftsrolle`, Spannung `ruhige_bis_mittlere_spannung`, Richtung `steigend`, Range `2.399862`, Tonshift `-0.000909`
- `HOLDOUT_POSITIVE_EXPANSION:501-600` -> `weite_weltspannungsnaehe`, Spannung `ruhige_bis_mittlere_spannung`, Richtung `fallend`, Range `2.134016`, Tonshift `0.000292`
- `HOLDOUT_POSITIVE_EXPANSION:701-800` -> `gerichtete_spannungsrolle`, Spannung `enge_unruhige_spannung`, Richtung `fallend`, Range `2.005119`, Tonshift `0.007565`
- `HOLDOUT_MEDIUM_QUIET_DRIFT:301-400` -> `offene_nachbarschaftsrolle`, Spannung `ruhige_bis_mittlere_spannung`, Richtung `steigend`, Range `3.248066`, Tonshift `-0.000801`

## Lesung

Die Holdout-Beruehrungen liegen nicht in chaotischer Kippung, sondern in stabiler Innenwirkung.
Die beruehrten Rollen treten dort auf, wo die Rohwelt als Spannungs- oder Unruhebereich gelesen wird.
Der ruhige SOL-Holdout ist nicht spannungslos: er zeigt kleinere Range, aber hohe Richtungswechsel. Dadurch entsteht `enge_unruhige_spannung` statt reiner Ruhe.
Der synthetisch glatte Kontrolllauf bleibt dagegen bei ruhiger bis mittlerer Spannung und beruehrt `offene_nachbarschaftsrolle`.
Die positive Expansion beruehrt sowohl Spannungsnaehe als auch gerichtete Spannungsrolle, erzwingt aber noch keine neue Mischklasse.
Damit wird `weite_weltspannungsnaehe` als Name fraglich: die Rolle scheint eher unruhige Spannungsnaehe zu tragen, nicht zwingend nur grosse Range.

## Wie es weitergeht

Als naechstes sollte eine kombinierte Stresswelt geprueft werden: nicht nur Rauschen, sondern zugleich groessere Range, dichtere Wechsel und staerkere Ton-/Rezeptorverdichtung. Damit laesst sich pruefen, wann stabile Oberflaechenvarianz in Spannungsnaehe kippt.
