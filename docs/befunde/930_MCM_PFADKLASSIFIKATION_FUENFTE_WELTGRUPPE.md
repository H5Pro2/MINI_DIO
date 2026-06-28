# MCM-Pfadklassifikation

## Zweck

Diese Diagnose erweitert die Verdichtungspfad-Lesart von vier Beispiel-Tokens auf alle gemeinsamen Tokens der Driftmatrix.
Sie ist passiv und klassifiziert Feldbewegungen, nicht Verhalten.

## Pfadklassen

| Pfadklasse | Anzahl |
|---|---:|
| stabile_insel | 6 |
| rekoppelnder_pfad | 26 |
| offener_driftpfad | 26 |
| randpfad | 1 |
| brueckenpfad | 22 |
| junge_oberflaeche | 16 |
| gemischter_pfad | 1 |

## Ausgangsbewegungen

| Bewegung aus Driftlupe | Anzahl |
|---|---:|
| oeffnung_oder_drift | 18 |
| randnaehe_entsteht | 1 |
| reifung_oder_verdichtung | 38 |
| stabil | 32 |
| verjuengung_oberflaeche | 9 |

## Staerkste Tokens Je Pfadklasse

| Pfadklasse | Token | Bewegung | Basiszone | Folgezone | Beobachtungsdelta | Weltendelta | Grund |
|---|---|---|---|---|---:|---:|---|
| stabile_insel | dio_mcm_episode_1t42af6 | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | -421 | 1 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_1ahj81f | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | -303 | 1 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_1jx2k4i | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | -157 | 2 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_0db07p4 | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | -19 | 0 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_17i4j9o | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | -13 | 0 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_0d40zcv | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | 7 | 2 | Zone bleibt stabile Bedeutungsinsel. |
| rekoppelnder_pfad | dio_mcm_episode_1hdpu9s | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | 2538 | 4 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_1jwnjz4 | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | 2414 | 3 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_1q3us3f | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | -1020 | 0 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_0lfde2c | reifung_oder_verdichtung | junge_spur | rekopplungszone | 716 | 4 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_0z748ck | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | 93 | 3 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_0w4x7xs | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | 29 | 0 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_17c7qwp | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | -26 | 0 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_03hr8bf | reifung_oder_verdichtung | junge_spur | stabile_bedeutungsinsel | 17 | 2 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| offener_driftpfad | dio_mcm_episode_1joiyc3 | reifung_oder_verdichtung | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | -3459 | 0 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_0dgle71 | oeffnung_oder_drift | stabile_bedeutungsinsel | offene_bedeutungszone | -110 | 0 | Token oeffnet oder driftet zwischen den Weltgruppen. |
| offener_driftpfad | dio_mcm_episode_0lne9ax | reifung_oder_verdichtung | driftzone | hoeherer_cluster_uebergang | 56 | 3 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_0aztxel | reifung_oder_verdichtung | stabile_bedeutungsinsel | hoeherer_cluster_uebergang | 42 | 3 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_0q7j4gf | oeffnung_oder_drift | junge_spur | driftzone | 9 | 3 | Token oeffnet oder driftet zwischen den Weltgruppen. |
| offener_driftpfad | dio_mcm_episode_0y1i8dq | reifung_oder_verdichtung | junge_spur | hoeherer_cluster_uebergang | 9 | 2 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_0krixak | oeffnung_oder_drift | stabile_bedeutungsinsel | offene_bedeutungszone | -6 | -2 | Token oeffnet oder driftet zwischen den Weltgruppen. |
| offener_driftpfad | dio_mcm_episode_0ldenly | reifung_oder_verdichtung | junge_spur | hoeherer_cluster_uebergang | 6 | 1 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| randpfad | dio_mcm_episode_06ciaj1 | randnaehe_entsteht | offene_bedeutungszone | randnahe_verdichtung | 3 | 2 | Randnaehe ist in Basis oder Folgezone direkt beteiligt. |
| brueckenpfad | dio_mcm_episode_0e7qvj1 | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | 24949 | 2 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_0v5p8er | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -1931 | -1 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_0b7nep9 | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | -1888 | 0 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_14coypf | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -1527 | 1 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_0ykar6i | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -1349 | -1 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_0mji3u6 | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 721 | 3 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_18l3thm | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -576 | -1 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_1hs3jsa | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -566 | 0 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| junge_oberflaeche | dio_mcm_episode_1xx3u1e | verjuengung_oberflaeche | hoeherer_cluster_uebergang | junge_spur | -2963 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_1b3r4if | verjuengung_oberflaeche | rekopplungszone | junge_spur | -5 | -2 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0ag2osp | verjuengung_oberflaeche | driftzone | junge_spur | -3 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0ldht3x | verjuengung_oberflaeche | hoeherer_cluster_uebergang | junge_spur | -3 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0vff3w6 | verjuengung_oberflaeche | rekopplungszone | junge_spur | -3 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0mvt50o | verjuengung_oberflaeche | driftzone | junge_spur | -1 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0u69u6w | verjuengung_oberflaeche | driftzone | junge_spur | -1 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0ybhu2p | verjuengung_oberflaeche | driftzone | junge_spur | -1 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| gemischter_pfad | dio_mcm_episode_09rbps0 | stabil | driftzone | driftzone | -9 | 1 | Zone bleibt formal stabil, aber im offenen Bedeutungsraum. |

## Befund

Die Mehrzahl der gemeinsamen Tokens liegt in stabilen, rekoppelnden oder brueckenartigen Pfaden. Das spricht fuer geordnete Feldbewegung statt zufaelliger Symboloberflaeche.
Randpfade bleiben selten. Das passt zum bisherigen Befund: Randnaehe entsteht lokal, aber sie dominiert die Topologie nicht.

## Bedeutung Fuer MINI_DIO

Die Pfadklassifikation verschiebt die Lesart von Tokenlisten zu Feldbewegungen.
Ein `dio_mcm_episode_*`-Zeichen ist damit nicht nur ein Name, sondern kann eine Insel, ein Pfad, eine Bruecke oder eine Driftbewegung tragen.

## Wie es weitergeht

Als naechstes sollte diese Pfadklassifikation gegen eine weitere frische Weltgruppe reproduziert werden. Ziel: pruefen, ob die Verteilung der Pfadklassen stabil bleibt oder ob neue Weltspannung andere Pfadtypen erzwingt.
