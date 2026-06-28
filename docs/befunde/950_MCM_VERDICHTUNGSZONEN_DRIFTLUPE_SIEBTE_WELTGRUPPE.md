# MCM-Verdichtungszonen Driftlupe

## Zweck

Diese Diagnose liest gemeinsame Tokens zweier Verdichtungszonen-Laeufe.
Sie prueft, ob ein Token seine Verdichtungszone behaelt, driftet, reift, rekoppelt oder in Randnaehe kippt.

## Basis

- Basislauf: `SECHSTE`
- Folgelauf: `SIEBTE`
- gemeinsame Tokens: `107`
- stabile Tokens: `52`
- wechselnde Tokens: `55`
- Stabilitaetsquote: `0.4860`

## Bewegungsarten

| Bewegung | Anzahl |
|---|---:|
| oeffnung_oder_drift | 19 |
| randnaehe_entsteht | 5 |
| reifung_oder_verdichtung | 21 |
| stabil | 52 |
| verjuengung_oberflaeche | 10 |

## Staerkste Wechsel nach Beobachtungsdelta

| Token | Bewegung | Basiszone | Folgezone | Beobachtungen | Welten | Rekopplung | Strain | Lautheit | Unschaerfe |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| dio_mcm_episode_1joiyc3 | reifung_oder_verdichtung | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | -207 | +0 | +0.0063 | -0.0043 | -0.0020 | -0.0117 |
| dio_mcm_episode_0lfde2c | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | +113 | +2 | +0.0172 | -0.0120 | -0.0759 | +0.0322 |
| dio_mcm_episode_18n06fj | reifung_oder_verdichtung | rekopplungszone | hoeherer_cluster_uebergang | +73 | +1 | -0.0080 | +0.0068 | -0.0196 | +0.0623 |
| dio_mcm_episode_0jbl5pq | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | +58 | +0 | +0.0115 | -0.0079 | +0.0094 | -0.0159 |
| dio_mcm_episode_0om13wf | reifung_oder_verdichtung | driftzone | hoeherer_cluster_uebergang | +17 | +2 | -0.0083 | +0.0105 | -0.0620 | +0.1038 |
| dio_mcm_episode_17i4j9o | reifung_oder_verdichtung | offene_bedeutungszone | stabile_bedeutungsinsel | +16 | +1 | -0.0101 | +0.0233 | +0.1945 | -0.0171 |
| dio_mcm_episode_1u741ze | reifung_oder_verdichtung | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | +15 | +2 | -0.0023 | -0.0009 | +0.0007 | -0.1160 |
| dio_mcm_episode_0ne8zu9 | reifung_oder_verdichtung | offene_bedeutungszone | hoeherer_cluster_uebergang | +11 | +2 | -0.0148 | +0.0029 | -0.0110 | +0.0834 |
| dio_mcm_episode_0mlk2ts | reifung_oder_verdichtung | junge_spur | stabile_bedeutungsinsel | +8 | +2 | -0.0162 | +0.0304 | +0.0242 | +0.0661 |
| dio_mcm_episode_0tf9fq3 | reifung_oder_verdichtung | junge_spur | hoeherer_cluster_uebergang | +8 | +2 | -0.0212 | +0.0005 | -0.0593 | +0.1538 |
| dio_mcm_episode_0r99tas | verjuengung_oberflaeche | rekopplungszone | junge_spur | -6 | -2 | -0.0327 | +0.0231 | +0.0613 | +0.1206 |
| dio_mcm_episode_01yulb6 | reifung_oder_verdichtung | offene_bedeutungszone | hoeherer_cluster_uebergang | +5 | +1 | +0.0567 | -0.0594 | -0.1071 | -0.1969 |
| dio_mcm_episode_0kazrmx | reifung_oder_verdichtung | junge_spur | stabile_bedeutungsinsel | +5 | +1 | -0.0070 | +0.0253 | +0.1146 | -0.0037 |
| dio_mcm_episode_0v93uai | verjuengung_oberflaeche | hoeherer_cluster_uebergang | junge_spur | -5 | -2 | +0.0383 | +0.0113 | +0.0293 | +0.0948 |
| dio_mcm_episode_1mesbjy | oeffnung_oder_drift | junge_spur | driftzone | +5 | +2 | -0.0121 | +0.0089 | -0.0323 | +0.2137 |
| dio_mcm_episode_07llqq8 | oeffnung_oder_drift | hoeherer_cluster_uebergang | driftzone | -4 | +0 | -0.0374 | +0.0303 | -0.0883 | +0.3238 |
| dio_mcm_episode_0l5wut9 | randnaehe_entsteht | junge_spur | randnahe_verdichtung | +4 | +2 | +0.0011 | -0.0006 | +0.0042 | -0.0327 |
| dio_mcm_episode_0mvjoir | reifung_oder_verdichtung | driftzone | hoeherer_cluster_uebergang | +4 | +3 | +0.0034 | +0.0067 | +0.0207 | -0.0086 |
| dio_mcm_episode_0q7skyc | reifung_oder_verdichtung | driftzone | hoeherer_cluster_uebergang | +4 | +0 | +0.0119 | -0.0155 | -0.0583 | -0.0238 |
| dio_mcm_episode_0qhs6nb | oeffnung_oder_drift | junge_spur | driftzone | +4 | +3 | -0.0148 | +0.0068 | -0.2358 | +0.0626 |

## Befund

Weniger als die Haelfte der gemeinsamen Tokens behaelt ihre Verdichtungszone. Das wuerde auf staerkere Weltfaerbung oder noch unreife Oberflaechenbindung hinweisen.
Mehr wechselnde Tokens gehen in Richtung Reifung/Verdichtung als in Oeffnung/Drift. Das deutet auf nachtraegliche Stabilisierung einzelner Feldzeichen.
Randnaehe tritt als kleine, aber gesonderte Bewegung auf. Das passt zur bisherigen Lesart: Rand ist lokal und selten, nicht die Grundform des Feldes.

## Wie es weitergeht

Als naechstes sollten die wechselnden Tokens gegen ihre Rohweltabschnitte gelesen werden. Ziel: unterscheiden, ob Zonenwechsel aus Weltphase, Sinnesaufnahme, Rekopplung oder echter MCM-Drift entsteht.
