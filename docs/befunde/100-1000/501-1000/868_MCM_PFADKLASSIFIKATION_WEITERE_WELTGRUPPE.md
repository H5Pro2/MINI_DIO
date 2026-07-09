# MCM-Pfadklassifikation

## Zweck

Diese Diagnose erweitert die Verdichtungspfad-Lesart von vier Beispiel-Tokens auf alle gemeinsamen Tokens der Driftmatrix.
Sie ist passiv und klassifiziert Feldbewegungen, nicht Verhalten.

## Pfadklassen

| Pfadklasse | Anzahl |
|---|---:|
| stabile_insel | 11 |
| rekoppelnder_pfad | 24 |
| offener_driftpfad | 16 |
| randpfad | 3 |
| brueckenpfad | 19 |
| junge_oberflaeche | 29 |
| gemischter_pfad | 1 |

## Ausgangsbewegungen

| Bewegung aus Driftlupe | Anzahl |
|---|---:|
| oeffnung_oder_drift | 10 |
| randnaehe_rekoppelt | 1 |
| reifung_oder_verdichtung | 33 |
| stabil | 45 |
| verjuengung_oberflaeche | 14 |

## Staerkste Tokens Je Pfadklasse

| Pfadklasse | Token | Bewegung | Basiszone | Folgezone | Beobachtungsdelta | Weltendelta | Grund |
|---|---|---|---|---|---:|---:|---|
| stabile_insel | dio_mcm_episode_0ko7wqc | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | -1764 | 0 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_0ybr5e3 | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | -1519 | 0 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_1jx2k4i | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | 875 | 3 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_1q3us3f | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | 534 | 0 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_1t42af6 | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | -430 | -1 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_17rahh6 | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | 275 | 0 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_1ahj81f | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | -201 | 0 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_1hdpu9s | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | -166 | 1 | Zone bleibt stabile Bedeutungsinsel. |
| rekoppelnder_pfad | dio_mcm_episode_0lfde2c | reifung_oder_verdichtung | junge_spur | rekopplungszone | 755 | 0 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_077r0df | stabil | rekopplungszone | rekopplungszone | 100 | 0 | Zone bleibt Rekopplungszone. |
| rekoppelnder_pfad | dio_mcm_episode_1jwnjz4 | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | 36 | -1 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_0w4x7xs | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | -20 | 1 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_0w4721p | stabil | rekopplungszone | rekopplungszone | -10 | -4 | Zone bleibt Rekopplungszone. |
| rekoppelnder_pfad | dio_mcm_episode_0jatqr8 | stabil | rekopplungszone | rekopplungszone | -7 | -2 | Zone bleibt Rekopplungszone. |
| rekoppelnder_pfad | dio_mcm_episode_0393v08 | reifung_oder_verdichtung | offene_bedeutungszone | stabile_bedeutungsinsel | 5 | 2 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_0dsrwv5 | reifung_oder_verdichtung | junge_spur | stabile_bedeutungsinsel | 5 | 3 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| offener_driftpfad | dio_mcm_episode_0ykar6i | oeffnung_oder_drift | hoeherer_cluster_uebergang | driftzone | -1347 | 0 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_0ldenly | reifung_oder_verdichtung | junge_spur | hoeherer_cluster_uebergang | 7 | 3 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_0aztxel | reifung_oder_verdichtung | stabile_bedeutungsinsel | hoeherer_cluster_uebergang | 6 | 2 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_0krixak | oeffnung_oder_drift | stabile_bedeutungsinsel | driftzone | -5 | -1 | Token oeffnet oder driftet zwischen den Weltgruppen. |
| offener_driftpfad | dio_mcm_episode_1ovglru | reifung_oder_verdichtung | driftzone | hoeherer_cluster_uebergang | 4 | 1 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_0lne9ax | reifung_oder_verdichtung | driftzone | hoeherer_cluster_uebergang | 3 | 2 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_0qhiq5e | oeffnung_oder_drift | junge_spur | driftzone | 3 | 3 | Token oeffnet oder driftet zwischen den Weltgruppen. |
| offener_driftpfad | dio_mcm_episode_00i7zy5 | oeffnung_oder_drift | junge_spur | driftzone | 2 | 2 | Token oeffnet oder driftet zwischen den Weltgruppen. |
| randpfad | dio_mcm_episode_102i30n | randnaehe_rekoppelt | randnahe_verdichtung | hoeherer_cluster_uebergang | 6 | 2 | Randnaehe ist in Basis oder Folgezone direkt beteiligt. |
| randpfad | dio_mcm_episode_0mm85pw | stabil | randnahe_verdichtung | randnahe_verdichtung | 1 | 0 | Randnaehe ist in Basis oder Folgezone direkt beteiligt. |
| randpfad | dio_mcm_episode_0mw7rev | stabil | randnahe_verdichtung | randnahe_verdichtung | 0 | 0 | Randnaehe ist in Basis oder Folgezone direkt beteiligt. |
| brueckenpfad | dio_mcm_episode_0e7qvj1 | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 6483 | 3 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_0b7nep9 | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 5453 | 0 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_1xx3u1e | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -2874 | 0 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_0v5p8er | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -1939 | -3 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_1joiyc3 | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 1197 | 4 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_18l3thm | reifung_oder_verdichtung | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | 941 | 3 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_0db07p4 | reifung_oder_verdichtung | stabile_bedeutungsinsel | hoeherer_cluster_uebergang | 227 | 4 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_17c7qwp | reifung_oder_verdichtung | stabile_bedeutungsinsel | hoeherer_cluster_uebergang | 91 | 1 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| junge_oberflaeche | dio_mcm_episode_1eju9g0 | verjuengung_oberflaeche | stabile_bedeutungsinsel | junge_spur | -326 | 0 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_02ujuqf | verjuengung_oberflaeche | hoeherer_cluster_uebergang | junge_spur | -5 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0ag2osp | verjuengung_oberflaeche | driftzone | junge_spur | -3 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0ultars | verjuengung_oberflaeche | hoeherer_cluster_uebergang | junge_spur | -3 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_1pmt8u2 | verjuengung_oberflaeche | rekopplungszone | junge_spur | -3 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_1v9dvrl | verjuengung_oberflaeche | offene_bedeutungszone | junge_spur | -2 | 0 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_1xp8xyu | verjuengung_oberflaeche | driftzone | junge_spur | -2 | 0 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0ml8r41 | verjuengung_oberflaeche | driftzone | junge_spur | -1 | 0 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| gemischter_pfad | dio_mcm_episode_1jc5z5p | stabil | driftzone | driftzone | 0 | 0 | Zone bleibt formal stabil, aber im offenen Bedeutungsraum. |

## Befund

Die Mehrzahl der gemeinsamen Tokens liegt in stabilen, rekoppelnden oder brueckenartigen Pfaden. Das spricht fuer geordnete Feldbewegung statt zufaelliger Symboloberflaeche.
Randpfade bleiben selten. Das passt zum bisherigen Befund: Randnaehe entsteht lokal, aber sie dominiert die Topologie nicht.

## Bedeutung Fuer MINI_DIO

Die Pfadklassifikation verschiebt die Lesart von Tokenlisten zu Feldbewegungen.
Ein `dio_mcm_episode_*`-Zeichen ist damit nicht nur ein Name, sondern kann eine Insel, ein Pfad, eine Bruecke oder eine Driftbewegung tragen.

## Wie es weitergeht

Als naechstes sollte diese Pfadklassifikation gegen eine weitere frische Weltgruppe reproduziert werden. Ziel: pruefen, ob die Verteilung der Pfadklassen stabil bleibt oder ob neue Weltspannung andere Pfadtypen erzwingt.
