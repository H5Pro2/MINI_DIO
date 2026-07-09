# MCM-Verdichtungszonen Driftlupe

## Zweck

Diese Diagnose liest gemeinsame Tokens zweier Verdichtungszonen-Laeufe.
Sie prueft, ob ein Token seine Verdichtungszone behaelt, driftet, reift, rekoppelt oder in Randnaehe kippt.

## Basis

- Basislauf: `BASIS_854`
- Folgelauf: `FUENFTE_928`
- gemeinsame Tokens: `98`
- stabile Tokens: `32`
- wechselnde Tokens: `66`
- Stabilitaetsquote: `0.3265`

## Bewegungsarten

| Bewegung | Anzahl |
|---|---:|
| oeffnung_oder_drift | 18 |
| randnaehe_entsteht | 1 |
| reifung_oder_verdichtung | 38 |
| stabil | 32 |
| verjuengung_oberflaeche | 9 |

## Staerkste Wechsel nach Beobachtungsdelta

| Token | Bewegung | Basiszone | Folgezone | Beobachtungen | Welten | Rekopplung | Strain | Lautheit | Unschaerfe |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| dio_mcm_episode_0e7qvj1 | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | +24949 | +2 | +0.0006 | +0.0024 | -0.0025 | -0.0069 |
| dio_mcm_episode_1joiyc3 | reifung_oder_verdichtung | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | -3459 | +0 | -0.0127 | +0.0081 | -0.0054 | +0.0139 |
| dio_mcm_episode_1xx3u1e | verjuengung_oberflaeche | hoeherer_cluster_uebergang | junge_spur | -2963 | -1 | +0.0134 | -0.0111 | -0.0803 | -0.0143 |
| dio_mcm_episode_1hdpu9s | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | +2538 | +4 | -0.0028 | +0.0033 | +0.0332 | +0.0056 |
| dio_mcm_episode_1jwnjz4 | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | +2414 | +3 | +0.0022 | +0.0040 | +0.0153 | -0.0056 |
| dio_mcm_episode_0v5p8er | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -1931 | -1 | +0.0015 | -0.0024 | -0.0131 | -0.0223 |
| dio_mcm_episode_14coypf | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -1527 | +1 | +0.0028 | -0.0007 | -0.0353 | +0.0293 |
| dio_mcm_episode_0ykar6i | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -1349 | -1 | +0.0170 | -0.0353 | -0.0926 | -0.1129 |
| dio_mcm_episode_1q3us3f | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | -1020 | +0 | -0.0091 | +0.0103 | +0.0159 | +0.0811 |
| dio_mcm_episode_0lfde2c | reifung_oder_verdichtung | junge_spur | rekopplungszone | +716 | +4 | -0.0031 | +0.0005 | -0.0705 | -0.0151 |
| dio_mcm_episode_18l3thm | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -576 | -1 | +0.0035 | -0.0048 | -0.0298 | +0.0133 |
| dio_mcm_episode_1hs3jsa | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -566 | +0 | +0.0025 | -0.0048 | -0.0184 | -0.0257 |
| dio_mcm_episode_14l8khu | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -547 | +0 | +0.0098 | -0.0081 | -0.0387 | -0.0377 |
| dio_mcm_episode_0dgle71 | oeffnung_oder_drift | stabile_bedeutungsinsel | offene_bedeutungszone | -110 | +0 | -0.0092 | -0.0158 | -0.0629 | -0.0602 |
| dio_mcm_episode_0qzjuvj | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | +98 | +3 | +0.0266 | -0.0267 | -0.0468 | -0.0737 |
| dio_mcm_episode_0z748ck | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | +93 | +3 | -0.0107 | +0.0072 | -0.0251 | +0.0214 |
| dio_mcm_episode_0lne9ax | reifung_oder_verdichtung | driftzone | hoeherer_cluster_uebergang | +56 | +3 | -0.0172 | +0.0361 | +0.1077 | +0.0415 |
| dio_mcm_episode_18n06fj | reifung_oder_verdichtung | stabile_bedeutungsinsel | hoeherer_cluster_uebergang | +46 | +3 | +0.0024 | -0.0001 | -0.0119 | -0.0000 |
| dio_mcm_episode_0aztxel | reifung_oder_verdichtung | stabile_bedeutungsinsel | hoeherer_cluster_uebergang | +42 | +3 | -0.0147 | +0.0191 | -0.0027 | +0.0621 |
| dio_mcm_episode_0hjnwsk | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | +37 | +3 | +0.0119 | -0.0159 | -0.0283 | -0.0125 |

## Befund

Weniger als die Haelfte der gemeinsamen Tokens behaelt ihre Verdichtungszone. Das wuerde auf staerkere Weltfaerbung oder noch unreife Oberflaechenbindung hinweisen.
Mehr wechselnde Tokens gehen in Richtung Reifung/Verdichtung als in Oeffnung/Drift. Das deutet auf nachtraegliche Stabilisierung einzelner Feldzeichen.
Randnaehe tritt als kleine, aber gesonderte Bewegung auf. Das passt zur bisherigen Lesart: Rand ist lokal und selten, nicht die Grundform des Feldes.

## Wie es weitergeht

Als naechstes sollten die wechselnden Tokens gegen ihre Rohweltabschnitte gelesen werden. Ziel: unterscheiden, ob Zonenwechsel aus Weltphase, Sinnesaufnahme, Rekopplung oder echter MCM-Drift entsteht.
