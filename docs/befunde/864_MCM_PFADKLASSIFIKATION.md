# MCM-Pfadklassifikation

## Zweck

Diese Diagnose erweitert die Verdichtungspfad-Lesart von vier Beispiel-Tokens auf alle gemeinsamen Tokens der Driftmatrix.
Sie ist passiv und klassifiziert Feldbewegungen, nicht Verhalten.

## Pfadklassen

| Pfadklasse | Anzahl |
|---|---:|
| stabile_insel | 14 |
| rekoppelnder_pfad | 41 |
| offener_driftpfad | 27 |
| randpfad | 3 |
| brueckenpfad | 18 |
| junge_oberflaeche | 30 |
| gemischter_pfad | 9 |

## Ausgangsbewegungen

| Bewegung aus Driftlupe | Anzahl |
|---|---:|
| oeffnung_oder_drift | 24 |
| reifung_oder_verdichtung | 26 |
| stabil | 84 |
| verjuengung_oberflaeche | 8 |

## Staerkste Tokens Je Pfadklasse

| Pfadklasse | Token | Bewegung | Basiszone | Folgezone | Beobachtungsdelta | Weltendelta | Grund |
|---|---|---|---|---|---:|---:|---|
| stabile_insel | dio_mcm_episode_0ybr5e3 | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | 2331 | 0 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_0ko7wqc | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | -1692 | -1 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_0dgle71 | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | 1221 | 0 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_1t42af6 | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | -396 | 0 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_0w4x7xs | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | 355 | 0 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_1ahj81f | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | 285 | 1 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_1eju9g0 | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | -237 | 0 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_1jwnjz4 | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | 43 | 0 | Zone bleibt stabile Bedeutungsinsel. |
| rekoppelnder_pfad | dio_mcm_episode_1q3us3f | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | -629 | 0 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_077r0df | reifung_oder_verdichtung | rekopplungszone | stabile_bedeutungsinsel | 543 | 2 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_08lp0ua | stabil | rekopplungszone | rekopplungszone | -6 | 0 | Zone bleibt Rekopplungszone. |
| rekoppelnder_pfad | dio_mcm_episode_0qvodoj | stabil | rekopplungszone | rekopplungszone | 6 | 0 | Zone bleibt Rekopplungszone. |
| rekoppelnder_pfad | dio_mcm_episode_1engxbn | stabil | rekopplungszone | rekopplungszone | 6 | 0 | Zone bleibt Rekopplungszone. |
| rekoppelnder_pfad | dio_mcm_episode_1n2f96o | reifung_oder_verdichtung | junge_spur | rekopplungszone | 6 | 1 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_1y2gc2i | reifung_oder_verdichtung | driftzone | stabile_bedeutungsinsel | 6 | 2 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_0393v08 | reifung_oder_verdichtung | offene_bedeutungszone | stabile_bedeutungsinsel | 5 | 2 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| offener_driftpfad | dio_mcm_episode_0v5p8er | oeffnung_oder_drift | hoeherer_cluster_uebergang | driftzone | -1878 | -2 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_14l8khu | oeffnung_oder_drift | hoeherer_cluster_uebergang | driftzone | -695 | -2 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_01s42m6 | oeffnung_oder_drift | stabile_bedeutungsinsel | driftzone | -88 | 0 | Token oeffnet oder driftet zwischen den Weltgruppen. |
| offener_driftpfad | dio_mcm_episode_0hjnwsk | oeffnung_oder_drift | hoeherer_cluster_uebergang | driftzone | -11 | 0 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_0lne9ax | reifung_oder_verdichtung | driftzone | hoeherer_cluster_uebergang | 5 | 1 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_028a6an | oeffnung_oder_drift | junge_spur | driftzone | 4 | 0 | Token oeffnet oder driftet zwischen den Weltgruppen. |
| offener_driftpfad | dio_mcm_episode_00i7zy5 | oeffnung_oder_drift | junge_spur | driftzone | 3 | 3 | Token oeffnet oder driftet zwischen den Weltgruppen. |
| offener_driftpfad | dio_mcm_episode_06ccuqv | oeffnung_oder_drift | junge_spur | offene_bedeutungszone | 3 | 1 | Token oeffnet oder driftet zwischen den Weltgruppen. |
| randpfad | dio_mcm_episode_0mm85pw | stabil | randnahe_verdichtung | randnahe_verdichtung | 2 | 1 | Randnaehe ist in Basis oder Folgezone direkt beteiligt. |
| randpfad | dio_mcm_episode_0mw7rev | stabil | randnahe_verdichtung | randnahe_verdichtung | -2 | 0 | Randnaehe ist in Basis oder Folgezone direkt beteiligt. |
| randpfad | dio_mcm_episode_102i30n | stabil | randnahe_verdichtung | randnahe_verdichtung | 0 | 0 | Randnaehe ist in Basis oder Folgezone direkt beteiligt. |
| brueckenpfad | dio_mcm_episode_0ykar6i | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 2479 | 1 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_0e7qvj1 | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 2287 | 2 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_0b7nep9 | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 1523 | 0 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_1xx3u1e | reifung_oder_verdichtung | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | -1110 | 1 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_1jx2k4i | reifung_oder_verdichtung | stabile_bedeutungsinsel | hoeherer_cluster_uebergang | 505 | 3 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_18l3thm | reifung_oder_verdichtung | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | -445 | 1 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_14coypf | reifung_oder_verdichtung | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | -350 | -1 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_0db07p4 | reifung_oder_verdichtung | stabile_bedeutungsinsel | hoeherer_cluster_uebergang | 37 | 2 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| junge_oberflaeche | dio_mcm_episode_0aztxel | verjuengung_oberflaeche | stabile_bedeutungsinsel | junge_spur | -7 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0l3i7ey | verjuengung_oberflaeche | hoeherer_cluster_uebergang | junge_spur | -5 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0ldht3x | verjuengung_oberflaeche | hoeherer_cluster_uebergang | junge_spur | -3 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0ultars | verjuengung_oberflaeche | hoeherer_cluster_uebergang | junge_spur | -3 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0i8oyce | verjuengung_oberflaeche | driftzone | junge_spur | -2 | 0 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_1f4jh6c | verjuengung_oberflaeche | driftzone | junge_spur | -2 | 0 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0tph7s0 | verjuengung_oberflaeche | driftzone | junge_spur | -1 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_1ovglru | verjuengung_oberflaeche | driftzone | junge_spur | -1 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| gemischter_pfad | dio_mcm_episode_1yzsm16 | stabil | offene_bedeutungszone | offene_bedeutungszone | 2 | 1 | Zone bleibt formal stabil, aber im offenen Bedeutungsraum. |
| gemischter_pfad | dio_mcm_episode_1v9dvrl | stabil | offene_bedeutungszone | offene_bedeutungszone | -1 | 0 | Zone bleibt formal stabil, aber im offenen Bedeutungsraum. |
| gemischter_pfad | dio_mcm_episode_0e6va2r | stabil | driftzone | driftzone | 0 | 0 | Zone bleibt formal stabil, aber im offenen Bedeutungsraum. |
| gemischter_pfad | dio_mcm_episode_0igfdmt | stabil | driftzone | driftzone | 0 | 0 | Zone bleibt formal stabil, aber im offenen Bedeutungsraum. |
| gemischter_pfad | dio_mcm_episode_0nj1l40 | stabil | driftzone | driftzone | 0 | 0 | Zone bleibt formal stabil, aber im offenen Bedeutungsraum. |
| gemischter_pfad | dio_mcm_episode_0t1ymth | stabil | offene_bedeutungszone | offene_bedeutungszone | 0 | 0 | Zone bleibt formal stabil, aber im offenen Bedeutungsraum. |
| gemischter_pfad | dio_mcm_episode_1jc5z5p | stabil | driftzone | driftzone | 0 | 0 | Zone bleibt formal stabil, aber im offenen Bedeutungsraum. |
| gemischter_pfad | dio_mcm_episode_1pwdejt | stabil | offene_bedeutungszone | offene_bedeutungszone | 0 | 0 | Zone bleibt formal stabil, aber im offenen Bedeutungsraum. |

## Befund

Die Mehrzahl der gemeinsamen Tokens liegt in stabilen, rekoppelnden oder brueckenartigen Pfaden. Das spricht fuer geordnete Feldbewegung statt zufaelliger Symboloberflaeche.
Randpfade bleiben selten. Das passt zum bisherigen Befund: Randnaehe entsteht lokal, aber sie dominiert die Topologie nicht.

## Bedeutung Fuer MINI_DIO

Die Pfadklassifikation verschiebt die Lesart von Tokenlisten zu Feldbewegungen.
Ein `dio_mcm_episode_*`-Zeichen ist damit nicht nur ein Name, sondern kann eine Insel, ein Pfad, eine Bruecke oder eine Driftbewegung tragen.

## Wie es weitergeht

Als naechstes sollte diese Pfadklassifikation gegen eine weitere frische Weltgruppe reproduziert werden. Ziel: pruefen, ob die Verteilung der Pfadklassen stabil bleibt oder ob neue Weltspannung andere Pfadtypen erzwingt.
