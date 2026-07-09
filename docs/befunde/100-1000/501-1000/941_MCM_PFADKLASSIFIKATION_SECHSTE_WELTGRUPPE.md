# MCM-Pfadklassifikation

## Zweck

Diese Diagnose erweitert die Verdichtungspfad-Lesart von vier Beispiel-Tokens auf alle gemeinsamen Tokens der Driftmatrix.
Sie ist passiv und klassifiziert Feldbewegungen, nicht Verhalten.

## Pfadklassen

| Pfadklasse | Anzahl |
|---|---:|
| stabile_insel | 4 |
| rekoppelnder_pfad | 11 |
| offener_driftpfad | 18 |
| randpfad | 1 |
| brueckenpfad | 10 |
| junge_oberflaeche | 11 |

## Ausgangsbewegungen

| Bewegung aus Driftlupe | Anzahl |
|---|---:|
| oeffnung_oder_drift | 11 |
| randnaehe_rekoppelt | 1 |
| reifung_oder_verdichtung | 18 |
| stabil | 19 |
| verjuengung_oberflaeche | 6 |

## Staerkste Tokens Je Pfadklasse

| Pfadklasse | Token | Bewegung | Basiszone | Folgezone | Beobachtungsdelta | Weltendelta | Grund |
|---|---|---|---|---|---:|---:|---|
| stabile_insel | dio_mcm_episode_0ko7wqc | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | -1785 | -1 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_1jx2k4i | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | -271 | 1 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_1ahj81f | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | -207 | -2 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_0db07p4 | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | 61 | 1 | Zone bleibt stabile Bedeutungsinsel. |
| rekoppelnder_pfad | dio_mcm_episode_1q3us3f | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | -865 | 0 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_1hdpu9s | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | 134 | 3 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_0z748ck | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | 35 | 2 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_0lfde2c | reifung_oder_verdichtung | junge_spur | stabile_bedeutungsinsel | 15 | 0 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_0lne9ax | reifung_oder_verdichtung | driftzone | rekopplungszone | 15 | 2 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_18n06fj | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | -13 | 1 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_0393v08 | reifung_oder_verdichtung | offene_bedeutungszone | stabile_bedeutungsinsel | 2 | 1 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_0k1pid9 | stabil | rekopplungszone | rekopplungszone | 2 | 1 | Zone bleibt Rekopplungszone. |
| offener_driftpfad | dio_mcm_episode_1joiyc3 | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | -4205 | -1 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_1t42af6 | oeffnung_oder_drift | stabile_bedeutungsinsel | driftzone | -435 | -1 | Token oeffnet oder driftet zwischen den Weltgruppen. |
| offener_driftpfad | dio_mcm_episode_0mji3u6 | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | -40 | 1 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_17i4j9o | oeffnung_oder_drift | stabile_bedeutungsinsel | offene_bedeutungszone | -28 | -1 | Token oeffnet oder driftet zwischen den Weltgruppen. |
| offener_driftpfad | dio_mcm_episode_0om13wf | oeffnung_oder_drift | hoeherer_cluster_uebergang | driftzone | -6 | 0 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_0aztxel | reifung_oder_verdichtung | stabile_bedeutungsinsel | hoeherer_cluster_uebergang | 3 | 1 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_0dsrwv5 | reifung_oder_verdichtung | junge_spur | hoeherer_cluster_uebergang | 3 | 1 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_0r1o8ja | stabil | driftzone | driftzone | 3 | 1 | Rekopplung faellt bei steigender Last oder Sinnesunschärfe. |
| randpfad | dio_mcm_episode_102i30n | randnaehe_rekoppelt | randnahe_verdichtung | driftzone | -1 | 0 | Randnaehe ist in Basis oder Folgezone direkt beteiligt. |
| brueckenpfad | dio_mcm_episode_0e7qvj1 | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -2057 | 1 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_1hs3jsa | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -593 | -1 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_0qzjuvj | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | 29 | 2 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_0jbl5pq | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 15 | 2 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_0hjnwsk | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | -8 | 2 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_0y1i8dq | reifung_oder_verdichtung | junge_spur | hoeherer_cluster_uebergang | 6 | 2 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_0ifxej6 | reifung_oder_verdichtung | junge_spur | hoeherer_cluster_uebergang | 2 | 2 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_0l3i7ey | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 2 | 2 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| junge_oberflaeche | dio_mcm_episode_0krixak | verjuengung_oberflaeche | stabile_bedeutungsinsel | junge_spur | -7 | -3 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0mvt50o | verjuengung_oberflaeche | driftzone | junge_spur | -1 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0pfredm | verjuengung_oberflaeche | driftzone | junge_spur | -1 | 0 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0qhs6nb | verjuengung_oberflaeche | driftzone | junge_spur | -1 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_1ovglru | verjuengung_oberflaeche | driftzone | junge_spur | -1 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_1yzsm16 | verjuengung_oberflaeche | offene_bedeutungszone | junge_spur | -1 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_00yl137 | stabil | junge_spur | junge_spur | 0 | 0 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0ssvqb2 | stabil | junge_spur | junge_spur | 0 | 0 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |

## Befund

Die Mehrzahl der gemeinsamen Tokens liegt in stabilen, rekoppelnden oder brueckenartigen Pfaden. Das spricht fuer geordnete Feldbewegung statt zufaelliger Symboloberflaeche.
Randpfade bleiben selten. Das passt zum bisherigen Befund: Randnaehe entsteht lokal, aber sie dominiert die Topologie nicht.

## Bedeutung Fuer MINI_DIO

Die Pfadklassifikation verschiebt die Lesart von Tokenlisten zu Feldbewegungen.
Ein `dio_mcm_episode_*`-Zeichen ist damit nicht nur ein Name, sondern kann eine Insel, ein Pfad, eine Bruecke oder eine Driftbewegung tragen.

## Wie es weitergeht

Als naechstes sollte diese Pfadklassifikation gegen eine weitere frische Weltgruppe reproduziert werden. Ziel: pruefen, ob die Verteilung der Pfadklassen stabil bleibt oder ob neue Weltspannung andere Pfadtypen erzwingt.
