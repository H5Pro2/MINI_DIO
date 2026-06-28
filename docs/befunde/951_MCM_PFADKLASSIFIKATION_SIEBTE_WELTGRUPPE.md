# MCM-Pfadklassifikation

## Zweck

Diese Diagnose erweitert die Verdichtungspfad-Lesart von vier Beispiel-Tokens auf alle gemeinsamen Tokens der Driftmatrix.
Sie ist passiv und klassifiziert Feldbewegungen, nicht Verhalten.

## Pfadklassen

| Pfadklasse | Anzahl |
|---|---:|
| stabile_insel | 5 |
| rekoppelnder_pfad | 26 |
| offener_driftpfad | 26 |
| randpfad | 12 |
| brueckenpfad | 17 |
| junge_oberflaeche | 21 |

## Ausgangsbewegungen

| Bewegung aus Driftlupe | Anzahl |
|---|---:|
| oeffnung_oder_drift | 19 |
| randnaehe_entsteht | 5 |
| reifung_oder_verdichtung | 21 |
| stabil | 52 |
| verjuengung_oberflaeche | 10 |

## Staerkste Tokens Je Pfadklasse

| Pfadklasse | Token | Bewegung | Basiszone | Folgezone | Beobachtungsdelta | Weltendelta | Grund |
|---|---|---|---|---|---:|---:|---|
| stabile_insel | dio_mcm_episode_1ahj81f | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | -118 | 1 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_1jx2k4i | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | 46 | -1 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_0db07p4 | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | -34 | -1 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_1rylps5 | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | 27 | 2 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_0ko7wqc | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | 14 | 0 | Zone bleibt stabile Bedeutungsinsel. |
| rekoppelnder_pfad | dio_mcm_episode_0e7qvj1 | stabil | rekopplungszone | rekopplungszone | 15572 | 0 | Zone bleibt Rekopplungszone. |
| rekoppelnder_pfad | dio_mcm_episode_1hdpu9s | stabil | rekopplungszone | rekopplungszone | 3821 | 0 | Zone bleibt Rekopplungszone. |
| rekoppelnder_pfad | dio_mcm_episode_1rxdw4p | stabil | rekopplungszone | rekopplungszone | 2451 | 1 | Zone bleibt Rekopplungszone. |
| rekoppelnder_pfad | dio_mcm_episode_1q3us3f | stabil | rekopplungszone | rekopplungszone | 613 | 1 | Zone bleibt Rekopplungszone. |
| rekoppelnder_pfad | dio_mcm_episode_1hs3jsa | stabil | rekopplungszone | rekopplungszone | 257 | 3 | Zone bleibt Rekopplungszone. |
| rekoppelnder_pfad | dio_mcm_episode_0lfde2c | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | 113 | 2 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_0qzjuvj | stabil | rekopplungszone | rekopplungszone | 54 | 0 | Zone bleibt Rekopplungszone. |
| rekoppelnder_pfad | dio_mcm_episode_0z748ck | stabil | rekopplungszone | rekopplungszone | 49 | 0 | Zone bleibt Rekopplungszone. |
| offener_driftpfad | dio_mcm_episode_0hjnwsk | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 68 | 0 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_0om13wf | reifung_oder_verdichtung | driftzone | hoeherer_cluster_uebergang | 17 | 2 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_0y1i8dq | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 12 | 1 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_0ne8zu9 | reifung_oder_verdichtung | offene_bedeutungszone | hoeherer_cluster_uebergang | 11 | 2 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_0tf9fq3 | reifung_oder_verdichtung | junge_spur | hoeherer_cluster_uebergang | 8 | 2 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_1mesbjy | oeffnung_oder_drift | junge_spur | driftzone | 5 | 2 | Token oeffnet oder driftet zwischen den Weltgruppen. |
| offener_driftpfad | dio_mcm_episode_07llqq8 | oeffnung_oder_drift | hoeherer_cluster_uebergang | driftzone | -4 | 0 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_0qhs6nb | oeffnung_oder_drift | junge_spur | driftzone | 4 | 3 | Token oeffnet oder driftet zwischen den Weltgruppen. |
| randpfad | dio_mcm_episode_0dbqs19 | stabil | randnahe_verdichtung | randnahe_verdichtung | 14 | 2 | Randnaehe ist in Basis oder Folgezone direkt beteiligt. |
| randpfad | dio_mcm_episode_19a388p | stabil | randnahe_verdichtung | randnahe_verdichtung | 12 | 2 | Randnaehe ist in Basis oder Folgezone direkt beteiligt. |
| randpfad | dio_mcm_episode_0kvu3mb | stabil | randnahe_verdichtung | randnahe_verdichtung | 11 | 1 | Randnaehe ist in Basis oder Folgezone direkt beteiligt. |
| randpfad | dio_mcm_episode_0tre8bg | stabil | randnahe_verdichtung | randnahe_verdichtung | 5 | 2 | Randnaehe ist in Basis oder Folgezone direkt beteiligt. |
| randpfad | dio_mcm_episode_0l5wut9 | randnaehe_entsteht | junge_spur | randnahe_verdichtung | 4 | 2 | Randnaehe ist in Basis oder Folgezone direkt beteiligt. |
| randpfad | dio_mcm_episode_1ve60mw | stabil | randnahe_verdichtung | randnahe_verdichtung | 4 | 0 | Randnaehe ist in Basis oder Folgezone direkt beteiligt. |
| randpfad | dio_mcm_episode_1vfs1bz | randnaehe_entsteht | junge_spur | randnahe_verdichtung | 3 | 1 | Randnaehe ist in Basis oder Folgezone direkt beteiligt. |
| randpfad | dio_mcm_episode_0f1kb3e | randnaehe_entsteht | junge_spur | randnahe_verdichtung | 2 | 2 | Randnaehe ist in Basis oder Folgezone direkt beteiligt. |
| brueckenpfad | dio_mcm_episode_0mji3u6 | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 1547 | 1 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_1joiyc3 | reifung_oder_verdichtung | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | -207 | 0 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_18n06fj | reifung_oder_verdichtung | rekopplungszone | hoeherer_cluster_uebergang | 73 | 1 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_0jbl5pq | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | 58 | 0 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_0aztxel | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 53 | 1 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_0l3i7ey | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 40 | 0 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_1u741ze | reifung_oder_verdichtung | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | 15 | 2 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_0n5sqpn | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 7 | 1 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| junge_oberflaeche | dio_mcm_episode_0r99tas | verjuengung_oberflaeche | rekopplungszone | junge_spur | -6 | -2 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0v93uai | verjuengung_oberflaeche | hoeherer_cluster_uebergang | junge_spur | -5 | -2 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_080f74u | verjuengung_oberflaeche | rekopplungszone | junge_spur | -2 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0ppr02l | verjuengung_oberflaeche | hoeherer_cluster_uebergang | junge_spur | -2 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_180stw7 | verjuengung_oberflaeche | driftzone | junge_spur | -2 | -2 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_19g1diz | verjuengung_oberflaeche | driftzone | junge_spur | -2 | -2 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_1y26981 | verjuengung_oberflaeche | offene_bedeutungszone | junge_spur | -2 | 0 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0q7j4gf | verjuengung_oberflaeche | hoeherer_cluster_uebergang | junge_spur | -1 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |

## Befund

Die Mehrzahl der gemeinsamen Tokens liegt in stabilen, rekoppelnden oder brueckenartigen Pfaden. Das spricht fuer geordnete Feldbewegung statt zufaelliger Symboloberflaeche.

## Bedeutung Fuer MINI_DIO

Die Pfadklassifikation verschiebt die Lesart von Tokenlisten zu Feldbewegungen.
Ein `dio_mcm_episode_*`-Zeichen ist damit nicht nur ein Name, sondern kann eine Insel, ein Pfad, eine Bruecke oder eine Driftbewegung tragen.

## Wie es weitergeht

Als naechstes sollte diese Pfadklassifikation gegen eine weitere frische Weltgruppe reproduziert werden. Ziel: pruefen, ob die Verteilung der Pfadklassen stabil bleibt oder ob neue Weltspannung andere Pfadtypen erzwingt.
