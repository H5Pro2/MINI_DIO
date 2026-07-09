# MCM-Verdichtungszonen Driftlupe

## Zweck

Diese Diagnose liest gemeinsame Tokens zweier Verdichtungszonen-Laeufe.
Sie prueft, ob ein Token seine Verdichtungszone behaelt, driftet, reift, rekoppelt oder in Randnaehe kippt.

## Basis

- Basislauf: `BASIS_854`
- Folgelauf: `WEITERE_865`
- gemeinsame Tokens: `103`
- stabile Tokens: `45`
- wechselnde Tokens: `58`
- Stabilitaetsquote: `0.4369`

## Bewegungsarten

| Bewegung | Anzahl |
|---|---:|
| oeffnung_oder_drift | 10 |
| randnaehe_rekoppelt | 1 |
| reifung_oder_verdichtung | 33 |
| stabil | 45 |
| verjuengung_oberflaeche | 14 |

## Staerkste Wechsel nach Beobachtungsdelta

| Token | Bewegung | Basiszone | Folgezone | Beobachtungen | Welten | Rekopplung | Strain | Lautheit | Unschaerfe |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| dio_mcm_episode_1xx3u1e | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -2874 | +0 | +0.0006 | -0.0036 | +0.0014 | -0.0090 |
| dio_mcm_episode_0v5p8er | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -1939 | -3 | +0.0075 | -0.0080 | -0.0300 | -0.0254 |
| dio_mcm_episode_0ykar6i | oeffnung_oder_drift | hoeherer_cluster_uebergang | driftzone | -1347 | +0 | -0.0114 | +0.0077 | +0.0518 | -0.0095 |
| dio_mcm_episode_18l3thm | reifung_oder_verdichtung | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | +941 | +3 | -0.0014 | -0.0019 | -0.0042 | +0.0000 |
| dio_mcm_episode_0lfde2c | reifung_oder_verdichtung | junge_spur | rekopplungszone | +755 | +0 | +0.0029 | -0.0098 | -0.1136 | -0.0045 |
| dio_mcm_episode_1eju9g0 | verjuengung_oberflaeche | stabile_bedeutungsinsel | junge_spur | -326 | +0 | +0.0209 | -0.0188 | -0.1467 | +0.0043 |
| dio_mcm_episode_0db07p4 | reifung_oder_verdichtung | stabile_bedeutungsinsel | hoeherer_cluster_uebergang | +227 | +4 | -0.0050 | +0.0050 | -0.0212 | +0.0616 |
| dio_mcm_episode_17c7qwp | reifung_oder_verdichtung | stabile_bedeutungsinsel | hoeherer_cluster_uebergang | +91 | +1 | -0.0000 | -0.0059 | -0.0235 | +0.0253 |
| dio_mcm_episode_1hs3jsa | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -80 | -1 | -0.0008 | +0.0018 | +0.0146 | -0.0097 |
| dio_mcm_episode_0mji3u6 | reifung_oder_verdichtung | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | -65 | +3 | -0.0024 | +0.0029 | -0.0040 | +0.0121 |
| dio_mcm_episode_1jwnjz4 | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | +36 | -1 | +0.0028 | +0.0010 | +0.0172 | -0.0028 |
| dio_mcm_episode_0w4x7xs | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | -20 | +1 | +0.0018 | -0.0004 | -0.0150 | +0.0058 |
| dio_mcm_episode_0ldenly | reifung_oder_verdichtung | junge_spur | hoeherer_cluster_uebergang | +7 | +3 | -0.0090 | +0.0151 | +0.0664 | +0.1245 |
| dio_mcm_episode_0aztxel | reifung_oder_verdichtung | stabile_bedeutungsinsel | hoeherer_cluster_uebergang | +6 | +2 | -0.0314 | +0.0273 | +0.0019 | +0.0775 |
| dio_mcm_episode_102i30n | randnaehe_rekoppelt | randnahe_verdichtung | hoeherer_cluster_uebergang | +6 | +2 | +0.0253 | -0.0340 | -0.0951 | -0.0892 |
| dio_mcm_episode_02ujuqf | verjuengung_oberflaeche | hoeherer_cluster_uebergang | junge_spur | -5 | -1 | +0.0092 | -0.0175 | -0.0269 | -0.1284 |
| dio_mcm_episode_0393v08 | reifung_oder_verdichtung | offene_bedeutungszone | stabile_bedeutungsinsel | +5 | +2 | -0.0002 | +0.0041 | +0.0657 | -0.0590 |
| dio_mcm_episode_0dsrwv5 | reifung_oder_verdichtung | junge_spur | stabile_bedeutungsinsel | +5 | +3 | -0.0083 | +0.0114 | +0.0065 | +0.0488 |
| dio_mcm_episode_0krixak | oeffnung_oder_drift | stabile_bedeutungsinsel | driftzone | -5 | -1 | -0.0185 | +0.0168 | -0.0056 | +0.0568 |
| dio_mcm_episode_028a6an | reifung_oder_verdichtung | junge_spur | stabile_bedeutungsinsel | +4 | +0 | -0.0030 | +0.0026 | +0.0239 | -0.1176 |

## Befund

Weniger als die Haelfte der gemeinsamen Tokens behaelt ihre Verdichtungszone. Das wuerde auf staerkere Weltfaerbung oder noch unreife Oberflaechenbindung hinweisen.
Mehr wechselnde Tokens gehen in Richtung Reifung/Verdichtung als in Oeffnung/Drift. Das deutet auf nachtraegliche Stabilisierung einzelner Feldzeichen.
Randnaehe tritt als kleine, aber gesonderte Bewegung auf. Das passt zur bisherigen Lesart: Rand ist lokal und selten, nicht die Grundform des Feldes.

## Wie es weitergeht

Als naechstes sollten die wechselnden Tokens gegen ihre Rohweltabschnitte gelesen werden. Ziel: unterscheiden, ob Zonenwechsel aus Weltphase, Sinnesaufnahme, Rekopplung oder echter MCM-Drift entsteht.
