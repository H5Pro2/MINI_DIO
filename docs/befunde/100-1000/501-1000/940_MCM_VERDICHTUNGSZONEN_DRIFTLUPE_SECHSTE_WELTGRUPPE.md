# MCM-Verdichtungszonen Driftlupe

## Zweck

Diese Diagnose liest gemeinsame Tokens zweier Verdichtungszonen-Laeufe.
Sie prueft, ob ein Token seine Verdichtungszone behaelt, driftet, reift, rekoppelt oder in Randnaehe kippt.

## Basis

- Basislauf: `BASIS_854`
- Folgelauf: `SECHSTE_939`
- gemeinsame Tokens: `55`
- stabile Tokens: `19`
- wechselnde Tokens: `36`
- Stabilitaetsquote: `0.3455`

## Bewegungsarten

| Bewegung | Anzahl |
|---|---:|
| oeffnung_oder_drift | 11 |
| randnaehe_rekoppelt | 1 |
| reifung_oder_verdichtung | 18 |
| stabil | 19 |
| verjuengung_oberflaeche | 6 |

## Staerkste Wechsel nach Beobachtungsdelta

| Token | Bewegung | Basiszone | Folgezone | Beobachtungen | Welten | Rekopplung | Strain | Lautheit | Unschaerfe |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| dio_mcm_episode_0e7qvj1 | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -2057 | +1 | -0.0083 | +0.0047 | -0.0016 | -0.0054 |
| dio_mcm_episode_1q3us3f | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | -865 | +0 | -0.0053 | +0.0062 | +0.0088 | +0.0424 |
| dio_mcm_episode_1hs3jsa | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -593 | -1 | -0.0042 | +0.0012 | +0.0065 | +0.0003 |
| dio_mcm_episode_1t42af6 | oeffnung_oder_drift | stabile_bedeutungsinsel | driftzone | -435 | -1 | -0.0383 | +0.0380 | +0.1972 | +0.0270 |
| dio_mcm_episode_1hdpu9s | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | +134 | +3 | -0.0073 | +0.0036 | +0.0219 | +0.0075 |
| dio_mcm_episode_0z748ck | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | +35 | +2 | -0.0137 | +0.0046 | -0.0438 | +0.0173 |
| dio_mcm_episode_0qzjuvj | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | +29 | +2 | +0.0209 | -0.0235 | -0.0332 | -0.0760 |
| dio_mcm_episode_17i4j9o | oeffnung_oder_drift | stabile_bedeutungsinsel | offene_bedeutungszone | -28 | -1 | +0.0103 | -0.0190 | -0.1957 | -0.0279 |
| dio_mcm_episode_0lfde2c | reifung_oder_verdichtung | junge_spur | stabile_bedeutungsinsel | +15 | +0 | -0.0193 | +0.0142 | -0.0088 | -0.0408 |
| dio_mcm_episode_0lne9ax | reifung_oder_verdichtung | driftzone | rekopplungszone | +15 | +2 | -0.0256 | +0.0264 | +0.0527 | +0.0586 |
| dio_mcm_episode_18n06fj | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | -13 | +1 | +0.0085 | -0.0064 | +0.0032 | -0.1067 |
| dio_mcm_episode_0krixak | verjuengung_oberflaeche | stabile_bedeutungsinsel | junge_spur | -7 | -3 | -0.0204 | +0.0255 | +0.0615 | +0.0677 |
| dio_mcm_episode_0om13wf | oeffnung_oder_drift | hoeherer_cluster_uebergang | driftzone | -6 | +0 | +0.0330 | -0.0331 | +0.0518 | -0.1697 |
| dio_mcm_episode_0y1i8dq | reifung_oder_verdichtung | junge_spur | hoeherer_cluster_uebergang | +6 | +2 | -0.0314 | -0.0109 | -0.0662 | -0.0053 |
| dio_mcm_episode_0aztxel | reifung_oder_verdichtung | stabile_bedeutungsinsel | hoeherer_cluster_uebergang | +3 | +1 | -0.0255 | +0.0302 | +0.0730 | +0.0138 |
| dio_mcm_episode_0dsrwv5 | reifung_oder_verdichtung | junge_spur | hoeherer_cluster_uebergang | +3 | +1 | -0.0110 | +0.0167 | +0.0197 | +0.0739 |
| dio_mcm_episode_0393v08 | reifung_oder_verdichtung | offene_bedeutungszone | stabile_bedeutungsinsel | +2 | +1 | -0.0059 | +0.0142 | +0.1004 | -0.0428 |
| dio_mcm_episode_0ifxej6 | reifung_oder_verdichtung | junge_spur | hoeherer_cluster_uebergang | +2 | +2 | -0.0044 | +0.0076 | -0.0263 | +0.1024 |
| dio_mcm_episode_1i31hl0 | reifung_oder_verdichtung | offene_bedeutungszone | hoeherer_cluster_uebergang | +2 | +1 | +0.0091 | +0.0040 | -0.0179 | -0.0075 |
| dio_mcm_episode_00i7zy5 | oeffnung_oder_drift | junge_spur | driftzone | +1 | +1 | -0.0091 | +0.0065 | -0.0693 | +0.2423 |

## Befund

Weniger als die Haelfte der gemeinsamen Tokens behaelt ihre Verdichtungszone. Das wuerde auf staerkere Weltfaerbung oder noch unreife Oberflaechenbindung hinweisen.
Mehr wechselnde Tokens gehen in Richtung Reifung/Verdichtung als in Oeffnung/Drift. Das deutet auf nachtraegliche Stabilisierung einzelner Feldzeichen.
Randnaehe tritt als kleine, aber gesonderte Bewegung auf. Das passt zur bisherigen Lesart: Rand ist lokal und selten, nicht die Grundform des Feldes.

## Wie es weitergeht

Als naechstes sollten die wechselnden Tokens gegen ihre Rohweltabschnitte gelesen werden. Ziel: unterscheiden, ob Zonenwechsel aus Weltphase, Sinnesaufnahme, Rekopplung oder echter MCM-Drift entsteht.
