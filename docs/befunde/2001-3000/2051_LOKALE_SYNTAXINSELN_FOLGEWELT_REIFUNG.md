# 2051 - Reifung lokaler Syntaxinseln in Folgewelten

## Zweck

Diese Auswertung nimmt die lokalen jungen Syntaxinseln aus 2049 und prüft sie gegen weitere Weltzufuhr aus 2050. Ziel ist die Unterscheidung: reift eine lokale Insel, bleibt sie lokal, oder verschwindet sie?

Die Prüfung bleibt passiv. Es geht um Reife und Wiederfindung, nicht um Handlung.

## Übersicht

- geprüfte lokale Inseln: `578`
- Statusverteilung: `{'gereift_zu_robuster_feldsyntax': 72, 'nicht_wiedergefunden': 282, 'wiedergefunden_jung': 224}`

## Statusklassen

| follow_status | families | origin_present_in | follow_fields | max_follow_events |
| --- | --- | --- | --- | --- |
| gereift_zu_robuster_feldsyntax | 72 | xrp_only:66;multi_only:6 | tragende_rekopplung:41;offene_rekopplung:18;spannungsnahe_oeffnung:13 | 34 |
| nicht_wiedergefunden | 282 | xrp_only:189;multi_only:93 | -:282 | 0 |
| wiedergefunden_jung | 224 | xrp_only:203;multi_only:21 | tragende_rekopplung:98;offene_rekopplung:79;spannungsnahe_oeffnung:40;offener_feldkontakt:7 | 82 |

## Stärkste gereifte oder wiedergefundene Inseln

| symbol_family | follow_status | origin_present_in | follow_events | follow_labels | follow_field | follow_reifung | follow_mcm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| dio_18i0 | gereift_zu_robuster_feldsyntax | xrp_only | 34 | xrp2025_1h:2;xrp2024_1h:2 | offene_rekopplung | weltuebergreifend_feldstabil | 0.389/0.281/0.596 |
| dio_02n9 | gereift_zu_robuster_feldsyntax | xrp_only | 32 | xrp2025_1h:1;xrp2024_1h:1 | offene_rekopplung | weltuebergreifend_feldstabil | 0.430/0.254/0.622 |
| dio_1yhs | gereift_zu_robuster_feldsyntax | xrp_only | 32 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | weltuebergreifend_feldstabil | 0.485/0.170/0.683 |
| dio_0ixk | gereift_zu_robuster_feldsyntax | xrp_only | 30 | xrp2025_1h:2;xrp2024_1h:2 | tragende_rekopplung | weltuebergreifend_feldstabil | 0.419/0.228/0.636 |
| dio_0l2q | gereift_zu_robuster_feldsyntax | xrp_only | 30 | xrp2024_1h:2;xrp2025_1h:2 | tragende_rekopplung | weltuebergreifend_feldstabil | 0.430/0.224/0.632 |
| dio_158y | gereift_zu_robuster_feldsyntax | xrp_only | 26 | xrp2024_1h:2;xrp2025_1h:1 | tragende_rekopplung | weltuebergreifend_feldstabil | 0.409/0.229/0.633 |
| dio_08zr | gereift_zu_robuster_feldsyntax | xrp_only | 24 | xrp2025_1h:2;xrp2024_1h:1 | offene_rekopplung | weltuebergreifend_feldstabil | 0.416/0.252/0.619 |
| dio_02a1 | gereift_zu_robuster_feldsyntax | xrp_only | 20 | xrp2024_1h:2;xrp2025_1h:2 | offene_rekopplung | weltuebergreifend_feldstabil | 0.385/0.277/0.600 |
| dio_0lil | gereift_zu_robuster_feldsyntax | xrp_only | 20 | xrp2025_1h:2;xrp2024_1h:1 | offene_rekopplung | weltuebergreifend_feldstabil | 0.401/0.267/0.607 |
| dio_0n8c | gereift_zu_robuster_feldsyntax | xrp_only | 18 | xrp2025_1h:1;xrp2024_1h:1 | spannungsnahe_oeffnung | weltuebergreifend_feldstabil | 0.357/0.339/0.558 |
| dio_18f1 | gereift_zu_robuster_feldsyntax | xrp_only | 18 | xrp2024_1h:1;xrp2025_1h:1 | spannungsnahe_oeffnung | weltuebergreifend_feldstabil | 0.358/0.330/0.565 |
| dio_1grk | gereift_zu_robuster_feldsyntax | xrp_only | 18 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | weltuebergreifend_feldstabil | 0.463/0.181/0.671 |
| dio_0e70 | gereift_zu_robuster_feldsyntax | xrp_only | 16 | xrp2025_1h:3;xrp2024_1h:1 | offene_rekopplung | weltuebergreifend_feldstabil | 0.379/0.272/0.605 |
| dio_1an1 | gereift_zu_robuster_feldsyntax | xrp_only | 16 | xrp2024_1h:2;xrp2025_1h:1 | spannungsnahe_oeffnung | weltuebergreifend_feldstabil | 0.369/0.308/0.580 |
| dio_10yy | gereift_zu_robuster_feldsyntax | xrp_only | 14 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | weltuebergreifend_feldstabil | 0.498/0.123/0.708 |
| dio_00ta | gereift_zu_robuster_feldsyntax | xrp_only | 12 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | weltuebergreifend_feldstabil | 0.436/0.198/0.654 |
| dio_02ez | gereift_zu_robuster_feldsyntax | xrp_only | 12 | xrp2025_1h:1;xrp2024_1h:1 | tragende_rekopplung | weltuebergreifend_feldstabil | 0.449/0.205/0.650 |
| dio_0aw0 | gereift_zu_robuster_feldsyntax | xrp_only | 12 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | weltuebergreifend_feldstabil | 0.448/0.195/0.655 |
| dio_17j2 | gereift_zu_robuster_feldsyntax | xrp_only | 12 | xrp2025_1h:1;xrp2024_1h:1 | tragende_rekopplung | weltuebergreifend_feldstabil | 0.488/0.134/0.701 |
| dio_1feg | gereift_zu_robuster_feldsyntax | xrp_only | 12 | xrp2025_1h:1;xrp2024_1h:1 | tragende_rekopplung | weltuebergreifend_feldstabil | 0.499/0.117/0.710 |
| dio_0a0e | gereift_zu_robuster_feldsyntax | xrp_only | 10 | xrp2024_1h:2;xrp2025_1h:2 | spannungsnahe_oeffnung | weltuebergreifend_feldstabil | 0.378/0.315/0.580 |
| dio_0naq | gereift_zu_robuster_feldsyntax | xrp_only | 10 | xrp2025_1h:1;xrp2024_1h:1 | tragende_rekopplung | weltuebergreifend_feldstabil | 0.432/0.204/0.644 |
| dio_0qzh | gereift_zu_robuster_feldsyntax | xrp_only | 10 | xrp2025_1h:1;xrp2024_1h:1 | tragende_rekopplung | weltuebergreifend_feldstabil | 0.436/0.187/0.659 |
| dio_11q8 | gereift_zu_robuster_feldsyntax | xrp_only | 10 | xrp2025_1h:2;xrp2024_1h:1 | tragende_rekopplung | weltuebergreifend_feldstabil | 0.421/0.228/0.627 |
| dio_1w0r | gereift_zu_robuster_feldsyntax | xrp_only | 10 | xrp2024_1h:2;xrp2025_1h:1 | offene_rekopplung | weltuebergreifend_feldstabil | 0.396/0.270/0.593 |
| dio_08nu | gereift_zu_robuster_feldsyntax | xrp_only | 8 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | weltuebergreifend_feldstabil | 0.431/0.202/0.635 |
| dio_0m81 | gereift_zu_robuster_feldsyntax | xrp_only | 8 | xrp2025_1h:1;xrp2024_1h:1 | tragende_rekopplung | weltuebergreifend_feldstabil | 0.431/0.204/0.644 |
| dio_0qe7 | gereift_zu_robuster_feldsyntax | xrp_only | 8 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | weltuebergreifend_feldstabil | 0.449/0.179/0.665 |
| dio_18d9 | gereift_zu_robuster_feldsyntax | xrp_only | 8 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | weltuebergreifend_feldstabil | 0.455/0.184/0.665 |
| dio_1h2q | gereift_zu_robuster_feldsyntax | xrp_only | 8 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | weltuebergreifend_feldstabil | 0.461/0.156/0.673 |

## Lesung

Wenn lokale junge Inseln in Folgewelten wieder auftauchen, sind sie nicht mehr nur lokale Reste. Sie werden zu Reifekandidaten. Wenn sie nicht wiedergefunden werden, bleiben sie vorerst weltgebundene oder zu schwache Inseln.

Wichtig: Auch `nicht_wiedergefunden` ist kein Fehler. Es zeigt, dass ein Teil der Syntaxbildung wirklich situativ bleibt.

## Grenze

Keine Handlung, keine Richtung, kein Gate. Diese Karte beschreibt nur, welche lokalen Inseln bei weiterer Weltzufuhr wieder anschließen.
