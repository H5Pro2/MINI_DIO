# 2052 - Passive Reifespur nachgereifter Syntaxinseln

## Zweck

Diese Auswertung markiert lokale Syntaxinseln, die in Folgewelten zu robuster Feldsyntax nachgereift sind. Sie werden bewusst getrennt von den ursprünglichen robusten Familien geführt.

Die Trennung ist wichtig: Eine Familie kann primär weltübergreifend stabil sein oder erst über weitere Weltzufuhr nachreifen. Beides ist Feldsyntax, aber nicht derselbe Reifeweg.

## Übersicht

- nachgereifte Familien: `72`
- Klassenverteilung: `{'nachgereift_multi_zu_folgewelt': 6, 'nachgereift_offen': 5, 'nachgereift_schwach': 44, 'nachgereift_spannungsnah': 13, 'nachgereift_tragend': 4}`

## Reifeklassen

| matured_trace_class | families | origin_present_in | follow_fields | max_follow_events |
| --- | --- | --- | --- | --- |
| nachgereift_multi_zu_folgewelt | 6 | multi_only:6 | tragende_rekopplung:4;offene_rekopplung:2 | 6 |
| nachgereift_offen | 5 | xrp_only:5 | offene_rekopplung:5 | 34 |
| nachgereift_schwach | 44 | xrp_only:44 | tragende_rekopplung:33;offene_rekopplung:11 | 18 |
| nachgereift_spannungsnah | 13 | xrp_only:13 | spannungsnahe_oeffnung:13 | 18 |
| nachgereift_tragend | 4 | xrp_only:4 | tragende_rekopplung:4 | 32 |

## Stärkste nachgereifte Familien

| symbol_family | matured_trace_class | origin_present_in | origin_field | follow_events | follow_labels | follow_field | follow_mcm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| dio_0v6z | nachgereift_multi_zu_folgewelt | multi_only | tragende_rekopplung | 6 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | 0.444/0.175/0.665 |
| dio_1h95 | nachgereift_multi_zu_folgewelt | multi_only | tragende_rekopplung | 6 | xrp2025_1h:1;xrp2024_1h:1 | tragende_rekopplung | 0.439/0.195/0.652 |
| dio_0p3i | nachgereift_multi_zu_folgewelt | multi_only | offene_rekopplung | 4 | xrp2024_1h:1;xrp2025_1h:1 | offene_rekopplung | 0.370/0.279/0.587 |
| dio_1ozo | nachgereift_multi_zu_folgewelt | multi_only | tragende_rekopplung | 4 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | 0.407/0.227/0.631 |
| dio_1p7l | nachgereift_multi_zu_folgewelt | multi_only | tragende_rekopplung | 4 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | 0.463/0.135/0.689 |
| dio_1qpu | nachgereift_multi_zu_folgewelt | multi_only | offene_rekopplung | 4 | sol2024:1;xrp2025_1h:1 | offene_rekopplung | 0.405/0.245/0.619 |
| dio_18i0 | nachgereift_offen | xrp_only | offene_rekopplung | 34 | xrp2025_1h:2;xrp2024_1h:2 | offene_rekopplung | 0.389/0.281/0.596 |
| dio_02n9 | nachgereift_offen | xrp_only | offene_rekopplung | 32 | xrp2025_1h:1;xrp2024_1h:1 | offene_rekopplung | 0.430/0.254/0.622 |
| dio_08zr | nachgereift_offen | xrp_only | offene_rekopplung | 24 | xrp2025_1h:2;xrp2024_1h:1 | offene_rekopplung | 0.416/0.252/0.619 |
| dio_02a1 | nachgereift_offen | xrp_only | offene_rekopplung | 20 | xrp2024_1h:2;xrp2025_1h:2 | offene_rekopplung | 0.385/0.277/0.600 |
| dio_0lil | nachgereift_offen | xrp_only | offene_rekopplung | 20 | xrp2025_1h:2;xrp2024_1h:1 | offene_rekopplung | 0.401/0.267/0.607 |
| dio_1grk | nachgereift_schwach | xrp_only | tragende_rekopplung | 18 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | 0.463/0.181/0.671 |
| dio_0e70 | nachgereift_schwach | xrp_only | offene_rekopplung | 16 | xrp2025_1h:3;xrp2024_1h:1 | offene_rekopplung | 0.379/0.272/0.605 |
| dio_10yy | nachgereift_schwach | xrp_only | tragende_rekopplung | 14 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | 0.498/0.123/0.708 |
| dio_00ta | nachgereift_schwach | xrp_only | tragende_rekopplung | 12 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | 0.436/0.198/0.654 |
| dio_02ez | nachgereift_schwach | xrp_only | tragende_rekopplung | 12 | xrp2025_1h:1;xrp2024_1h:1 | tragende_rekopplung | 0.449/0.205/0.650 |
| dio_0aw0 | nachgereift_schwach | xrp_only | tragende_rekopplung | 12 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | 0.448/0.195/0.655 |
| dio_17j2 | nachgereift_schwach | xrp_only | tragende_rekopplung | 12 | xrp2025_1h:1;xrp2024_1h:1 | tragende_rekopplung | 0.488/0.134/0.701 |
| dio_1feg | nachgereift_schwach | xrp_only | tragende_rekopplung | 12 | xrp2025_1h:1;xrp2024_1h:1 | tragende_rekopplung | 0.499/0.117/0.710 |
| dio_0naq | nachgereift_schwach | xrp_only | tragende_rekopplung | 10 | xrp2025_1h:1;xrp2024_1h:1 | tragende_rekopplung | 0.432/0.204/0.644 |
| dio_0qzh | nachgereift_schwach | xrp_only | tragende_rekopplung | 10 | xrp2025_1h:1;xrp2024_1h:1 | tragende_rekopplung | 0.436/0.187/0.659 |
| dio_11q8 | nachgereift_schwach | xrp_only | tragende_rekopplung | 10 | xrp2025_1h:2;xrp2024_1h:1 | tragende_rekopplung | 0.421/0.228/0.627 |
| dio_1w0r | nachgereift_schwach | xrp_only | offene_rekopplung | 10 | xrp2024_1h:2;xrp2025_1h:1 | offene_rekopplung | 0.396/0.270/0.593 |
| dio_08nu | nachgereift_schwach | xrp_only | tragende_rekopplung | 8 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | 0.431/0.202/0.635 |
| dio_0m81 | nachgereift_schwach | xrp_only | tragende_rekopplung | 8 | xrp2025_1h:1;xrp2024_1h:1 | tragende_rekopplung | 0.431/0.204/0.644 |
| dio_0qe7 | nachgereift_schwach | xrp_only | tragende_rekopplung | 8 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | 0.449/0.179/0.665 |
| dio_18d9 | nachgereift_schwach | xrp_only | tragende_rekopplung | 8 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | 0.455/0.184/0.665 |
| dio_1h2q | nachgereift_schwach | xrp_only | tragende_rekopplung | 8 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | 0.461/0.156/0.673 |
| dio_0ifh | nachgereift_schwach | xrp_only | tragende_rekopplung | 6 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | 0.435/0.185/0.650 |
| dio_0ko2 | nachgereift_schwach | xrp_only | tragende_rekopplung | 6 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | 0.446/0.167/0.663 |

## Lesung

Nachgereifte Familien sind keine neuen Regeln. Sie zeigen, dass eine zuerst lokale Insel unter weiterer Weltzufuhr wieder anschließen und stabiler werden kann.

Diese Spur ist für MINI_DIO wichtig, weil Entwicklung dadurch nicht binär gelesen wird. Eine Insel muss nicht sofort robust sein. Sie kann jung erscheinen, später wieder auftauchen und erst dann Reife bekommen.

## Grenze

Keine Handlung, keine Richtung, kein Gate. Diese Reifespur beschreibt nur Entwicklungsqualität im Feldgedächtnis.

## Wie es weitergeht

Als nächstes sollten diese nachgereiften Familien unter Stress geprüft werden. Entscheidend ist, ob sie belastbar bleiben oder wieder in junge, lokale Inseln zurückfallen.
