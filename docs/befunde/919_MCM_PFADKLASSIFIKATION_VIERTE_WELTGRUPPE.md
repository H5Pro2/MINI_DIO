# MCM-Pfadklassifikation

## Zweck

Diese Diagnose erweitert die Verdichtungspfad-Lesart von vier Beispiel-Tokens auf alle gemeinsamen Tokens der Driftmatrix.
Sie ist passiv und klassifiziert Feldbewegungen, nicht Verhalten.

## Pfadklassen

| Pfadklasse | Anzahl |
|---|---:|
| stabile_insel | 11 |
| rekoppelnder_pfad | 23 |
| offener_driftpfad | 25 |
| randpfad | 3 |
| brueckenpfad | 16 |
| junge_oberflaeche | 19 |
| gemischter_pfad | 2 |

## Ausgangsbewegungen

| Bewegung aus Driftlupe | Anzahl |
|---|---:|
| oeffnung_oder_drift | 18 |
| randnaehe_rekoppelt | 1 |
| reifung_oder_verdichtung | 33 |
| stabil | 37 |
| verjuengung_oberflaeche | 10 |

## Staerkste Tokens Je Pfadklasse

| Pfadklasse | Token | Bewegung | Basiszone | Folgezone | Beobachtungsdelta | Weltendelta | Grund |
|---|---|---|---|---|---:|---:|---|
| stabile_insel | dio_mcm_episode_0ko7wqc | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | -1692 | -1 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_0dgle71 | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | 1221 | 0 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_1q3us3f | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | -1000 | 0 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_1jx2k4i | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | 694 | 3 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_1t42af6 | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | -396 | 0 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_1ahj81f | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | 363 | 2 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_0w4x7xs | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | 355 | 0 | Zone bleibt stabile Bedeutungsinsel. |
| stabile_insel | dio_mcm_episode_1hdpu9s | stabil | stabile_bedeutungsinsel | stabile_bedeutungsinsel | -311 | 1 | Zone bleibt stabile Bedeutungsinsel. |
| rekoppelnder_pfad | dio_mcm_episode_0ybr5e3 | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | 2331 | 0 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_077r0df | stabil | rekopplungszone | rekopplungszone | 484 | 1 | Zone bleibt Rekopplungszone. |
| rekoppelnder_pfad | dio_mcm_episode_1eju9g0 | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | -237 | 0 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_1jwnjz4 | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | 43 | 0 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_17c7qwp | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | 18 | 0 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_17rahh6 | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | 10 | 0 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_0jatqr8 | reifung_oder_verdichtung | rekopplungszone | stabile_bedeutungsinsel | -6 | -1 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| rekoppelnder_pfad | dio_mcm_episode_1n2f96o | reifung_oder_verdichtung | junge_spur | rekopplungszone | 6 | 1 | Token verschiebt sich in stabilere oder rekoppelnde Zone. |
| offener_driftpfad | dio_mcm_episode_03hr8bf | oeffnung_oder_drift | junge_spur | driftzone | 27 | 0 | Token oeffnet oder driftet zwischen den Weltgruppen. |
| offener_driftpfad | dio_mcm_episode_0w4721p | oeffnung_oder_drift | rekopplungszone | offene_bedeutungszone | -10 | -4 | Token oeffnet oder driftet zwischen den Weltgruppen. |
| offener_driftpfad | dio_mcm_episode_0lne9ax | reifung_oder_verdichtung | driftzone | hoeherer_cluster_uebergang | 4 | 0 | Clusterbindung oeffnet sich mit sinkender Rekopplung oder steigender Unschaerfe. |
| offener_driftpfad | dio_mcm_episode_0dsrwv5 | oeffnung_oder_drift | junge_spur | driftzone | 3 | 2 | Token oeffnet oder driftet zwischen den Weltgruppen. |
| offener_driftpfad | dio_mcm_episode_0o36jeo | stabil | offene_bedeutungszone | offene_bedeutungszone | 3 | 0 | Rekopplung faellt bei steigender Last oder Sinnesunschärfe. |
| offener_driftpfad | dio_mcm_episode_1ig1vs0 | oeffnung_oder_drift | junge_spur | driftzone | 3 | 2 | Token oeffnet oder driftet zwischen den Weltgruppen. |
| offener_driftpfad | dio_mcm_episode_00yl137 | oeffnung_oder_drift | junge_spur | driftzone | 2 | 1 | Token oeffnet oder driftet zwischen den Weltgruppen. |
| offener_driftpfad | dio_mcm_episode_0mb95f2 | oeffnung_oder_drift | junge_spur | driftzone | 2 | 0 | Token oeffnet oder driftet zwischen den Weltgruppen. |
| randpfad | dio_mcm_episode_0mm85pw | stabil | randnahe_verdichtung | randnahe_verdichtung | 2 | 1 | Randnaehe ist in Basis oder Folgezone direkt beteiligt. |
| randpfad | dio_mcm_episode_102i30n | randnaehe_rekoppelt | randnahe_verdichtung | hoeherer_cluster_uebergang | 2 | 1 | Randnaehe ist in Basis oder Folgezone direkt beteiligt. |
| randpfad | dio_mcm_episode_0mw7rev | stabil | randnahe_verdichtung | randnahe_verdichtung | 1 | 1 | Randnaehe ist in Basis oder Folgezone direkt beteiligt. |
| brueckenpfad | dio_mcm_episode_0e7qvj1 | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 4153 | 2 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_0ykar6i | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | 2479 | 1 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_0b7nep9 | reifung_oder_verdichtung | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | 1523 | 0 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_1xx3u1e | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -1110 | 1 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_1joiyc3 | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | -645 | 3 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_18l3thm | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -415 | 1 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_14coypf | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -350 | -1 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| brueckenpfad | dio_mcm_episode_0mji3u6 | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 133 | 3 | Hoeherer Clusteruebergang ist beteiligt; Token wirkt als Bruecke oder Uebergang. |
| junge_oberflaeche | dio_mcm_episode_0w96mqy | verjuengung_oberflaeche | rekopplungszone | junge_spur | -9 | -2 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0krixak | verjuengung_oberflaeche | stabile_bedeutungsinsel | junge_spur | -7 | -3 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0om13wf | verjuengung_oberflaeche | hoeherer_cluster_uebergang | junge_spur | -7 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0l3i7ey | verjuengung_oberflaeche | hoeherer_cluster_uebergang | junge_spur | -5 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0ldht3x | verjuengung_oberflaeche | hoeherer_cluster_uebergang | junge_spur | -3 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0i8oyce | verjuengung_oberflaeche | driftzone | junge_spur | -2 | 0 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_0k1pid9 | verjuengung_oberflaeche | rekopplungszone | junge_spur | -2 | -1 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| junge_oberflaeche | dio_mcm_episode_1f4jh6c | verjuengung_oberflaeche | driftzone | junge_spur | -2 | 0 | Token verliert Reife oder faellt in junge Oberflaeche zurueck. |
| gemischter_pfad | dio_mcm_episode_1yzsm16 | stabil | offene_bedeutungszone | offene_bedeutungszone | 2 | 1 | Zone bleibt formal stabil, aber im offenen Bedeutungsraum. |
| gemischter_pfad | dio_mcm_episode_1jc5z5p | stabil | driftzone | driftzone | 0 | 0 | Zone bleibt formal stabil, aber im offenen Bedeutungsraum. |

## Befund

Die Mehrzahl der gemeinsamen Tokens liegt in stabilen, rekoppelnden oder brueckenartigen Pfaden. Das spricht fuer geordnete Feldbewegung statt zufaelliger Symboloberflaeche.
Randpfade bleiben selten. Das passt zum bisherigen Befund: Randnaehe entsteht lokal, aber sie dominiert die Topologie nicht.

## Bedeutung Fuer MINI_DIO

Die Pfadklassifikation verschiebt die Lesart von Tokenlisten zu Feldbewegungen.
Ein `dio_mcm_episode_*`-Zeichen ist damit nicht nur ein Name, sondern kann eine Insel, ein Pfad, eine Bruecke oder eine Driftbewegung tragen.

## Wie es weitergeht

Als naechstes sollte diese Pfadklassifikation gegen eine weitere frische Weltgruppe reproduziert werden. Ziel: pruefen, ob die Verteilung der Pfadklassen stabil bleibt oder ob neue Weltspannung andere Pfadtypen erzwingt.
