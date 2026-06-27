# MCM-Verdichtungszonen Driftlupe

## Zweck

Diese Diagnose liest gemeinsame Tokens zweier Verdichtungszonen-Laeufe.
Sie prueft, ob ein Token seine Verdichtungszone behaelt, driftet, reift, rekoppelt oder in Randnaehe kippt.

## Basis

- Basislauf: `854_Ausgangsgruppe`
- Folgelauf: `855_Frische_Weltgruppe`
- gemeinsame Tokens: `142`
- stabile Tokens: `84`
- wechselnde Tokens: `58`
- Stabilitaetsquote: `0.5915`

## Bewegungsarten

| Bewegung | Anzahl |
|---|---:|
| oeffnung_oder_drift | 24 |
| reifung_oder_verdichtung | 26 |
| stabil | 84 |
| verjuengung_oberflaeche | 8 |

## Staerkste Wechsel nach Beobachtungsdelta

| Token | Bewegung | Basiszone | Folgezone | Beobachtungen | Welten | Rekopplung | Strain | Lautheit | Unschaerfe |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| dio_mcm_episode_0v5p8er | oeffnung_oder_drift | hoeherer_cluster_uebergang | driftzone | -1878 | -2 | -0.0274 | +0.0187 | +0.0369 | +0.1194 |
| dio_mcm_episode_1xx3u1e | reifung_oder_verdichtung | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | -1110 | +1 | -0.0003 | +0.0024 | +0.0202 | +0.0054 |
| dio_mcm_episode_14l8khu | oeffnung_oder_drift | hoeherer_cluster_uebergang | driftzone | -695 | -2 | -0.0319 | +0.0250 | +0.0480 | +0.1134 |
| dio_mcm_episode_1q3us3f | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | -629 | +0 | +0.0064 | -0.0067 | -0.0298 | -0.0612 |
| dio_mcm_episode_077r0df | reifung_oder_verdichtung | rekopplungszone | stabile_bedeutungsinsel | +543 | +2 | -0.0106 | +0.0164 | +0.0796 | +0.0984 |
| dio_mcm_episode_1jx2k4i | reifung_oder_verdichtung | stabile_bedeutungsinsel | hoeherer_cluster_uebergang | +505 | +3 | +0.0047 | -0.0008 | -0.0203 | +0.0222 |
| dio_mcm_episode_18l3thm | reifung_oder_verdichtung | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | -445 | +1 | +0.0050 | -0.0045 | -0.0234 | -0.0058 |
| dio_mcm_episode_14coypf | reifung_oder_verdichtung | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | -350 | -1 | +0.0042 | -0.0022 | +0.0153 | -0.0328 |
| dio_mcm_episode_01s42m6 | oeffnung_oder_drift | stabile_bedeutungsinsel | driftzone | -88 | +0 | +0.0106 | -0.0121 | -0.0472 | -0.0118 |
| dio_mcm_episode_0db07p4 | reifung_oder_verdichtung | stabile_bedeutungsinsel | hoeherer_cluster_uebergang | +37 | +2 | -0.0010 | +0.0007 | -0.0119 | +0.0123 |
| dio_mcm_episode_0mji3u6 | reifung_oder_verdichtung | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | +26 | +2 | -0.0022 | +0.0008 | -0.0027 | +0.0152 |
| dio_mcm_episode_0hjnwsk | oeffnung_oder_drift | hoeherer_cluster_uebergang | driftzone | -11 | +0 | -0.0113 | +0.0122 | +0.0472 | +0.1079 |
| dio_mcm_episode_18n06fj | reifung_oder_verdichtung | stabile_bedeutungsinsel | hoeherer_cluster_uebergang | -9 | +1 | +0.0133 | -0.0133 | -0.0312 | -0.0715 |
| dio_mcm_episode_0aztxel | verjuengung_oberflaeche | stabile_bedeutungsinsel | junge_spur | -7 | -1 | -0.0044 | -0.0291 | -0.1428 | -0.0300 |
| dio_mcm_episode_1n2f96o | reifung_oder_verdichtung | junge_spur | rekopplungszone | +6 | +1 | -0.0029 | -0.0077 | +0.0045 | +0.0077 |
| dio_mcm_episode_1y2gc2i | reifung_oder_verdichtung | driftzone | stabile_bedeutungsinsel | +6 | +2 | +0.0005 | -0.0017 | -0.0775 | +0.0419 |
| dio_mcm_episode_0393v08 | reifung_oder_verdichtung | offene_bedeutungszone | stabile_bedeutungsinsel | +5 | +2 | -0.0002 | +0.0040 | +0.0657 | -0.0590 |
| dio_mcm_episode_0l3i7ey | verjuengung_oberflaeche | hoeherer_cluster_uebergang | junge_spur | -5 | -1 | +0.0388 | -0.0499 | -0.0967 | -0.2201 |
| dio_mcm_episode_0lne9ax | reifung_oder_verdichtung | driftzone | hoeherer_cluster_uebergang | +5 | +1 | -0.0192 | +0.0276 | +0.0419 | +0.0650 |
| dio_mcm_episode_028a6an | oeffnung_oder_drift | junge_spur | driftzone | +4 | +0 | -0.0049 | -0.0028 | +0.0481 | -0.1366 |

## Befund

Die Mehrheit der gemeinsamen Tokens behaelt ihre Verdichtungszone. Das spricht fuer stabile Rollenordnung mit variabler Oberflaeche.
Mehr wechselnde Tokens gehen in Richtung Reifung/Verdichtung als in Oeffnung/Drift. Das deutet auf nachtraegliche Stabilisierung einzelner Feldzeichen.

## Wie es weitergeht

Als naechstes sollten die wechselnden Tokens gegen ihre Rohweltabschnitte gelesen werden. Ziel: unterscheiden, ob Zonenwechsel aus Weltphase, Sinnesaufnahme, Rekopplung oder echter MCM-Drift entsteht.
