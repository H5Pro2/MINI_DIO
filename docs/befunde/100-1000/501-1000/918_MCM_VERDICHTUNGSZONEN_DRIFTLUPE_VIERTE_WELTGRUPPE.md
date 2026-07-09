# MCM-Verdichtungszonen Driftlupe

## Zweck

Diese Diagnose liest gemeinsame Tokens zweier Verdichtungszonen-Laeufe.
Sie prueft, ob ein Token seine Verdichtungszone behaelt, driftet, reift, rekoppelt oder in Randnaehe kippt.

## Basis

- Basislauf: `BASIS_854`
- Folgelauf: `VIERTE_917`
- gemeinsame Tokens: `99`
- stabile Tokens: `37`
- wechselnde Tokens: `62`
- Stabilitaetsquote: `0.3737`

## Bewegungsarten

| Bewegung | Anzahl |
|---|---:|
| oeffnung_oder_drift | 18 |
| randnaehe_rekoppelt | 1 |
| reifung_oder_verdichtung | 33 |
| stabil | 37 |
| verjuengung_oberflaeche | 10 |

## Staerkste Wechsel nach Beobachtungsdelta

| Token | Bewegung | Basiszone | Folgezone | Beobachtungen | Welten | Rekopplung | Strain | Lautheit | Unschaerfe |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| dio_mcm_episode_0ykar6i | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | +2479 | +1 | +0.0026 | -0.0012 | +0.0044 | -0.0181 |
| dio_mcm_episode_0ybr5e3 | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | +2331 | +0 | +0.0005 | +0.0007 | +0.0032 | +0.0171 |
| dio_mcm_episode_0b7nep9 | reifung_oder_verdichtung | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | +1523 | +0 | -0.0022 | +0.0012 | +0.0122 | -0.0029 |
| dio_mcm_episode_1xx3u1e | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -1110 | +1 | -0.0003 | +0.0024 | +0.0202 | +0.0054 |
| dio_mcm_episode_18l3thm | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -415 | +1 | +0.0039 | -0.0046 | -0.0200 | -0.0075 |
| dio_mcm_episode_14coypf | reifung_oder_verdichtung | hoeherer_cluster_uebergang | rekopplungszone | -350 | -1 | +0.0042 | -0.0022 | +0.0153 | -0.0328 |
| dio_mcm_episode_1eju9g0 | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | -237 | +0 | +0.0058 | +0.0063 | +0.0512 | -0.0108 |
| dio_mcm_episode_1jwnjz4 | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | +43 | +0 | +0.0080 | -0.0028 | +0.0060 | -0.0172 |
| dio_mcm_episode_03hr8bf | oeffnung_oder_drift | junge_spur | driftzone | +27 | +0 | +0.0489 | -0.0527 | -0.0457 | -0.1721 |
| dio_mcm_episode_17c7qwp | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | +18 | +0 | +0.0051 | +0.0047 | +0.0307 | +0.0543 |
| dio_mcm_episode_0hjnwsk | reifung_oder_verdichtung | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | -11 | +0 | +0.0068 | -0.0031 | +0.0442 | -0.0101 |
| dio_mcm_episode_0w4721p | oeffnung_oder_drift | rekopplungszone | offene_bedeutungszone | -10 | -4 | -0.0099 | -0.0010 | -0.0223 | +0.0061 |
| dio_mcm_episode_17rahh6 | reifung_oder_verdichtung | stabile_bedeutungsinsel | rekopplungszone | +10 | +0 | +0.0096 | +0.0010 | +0.0356 | -0.0352 |
| dio_mcm_episode_0w96mqy | verjuengung_oberflaeche | rekopplungszone | junge_spur | -9 | -2 | -0.0089 | -0.0028 | +0.0374 | +0.0210 |
| dio_mcm_episode_18n06fj | reifung_oder_verdichtung | stabile_bedeutungsinsel | hoeherer_cluster_uebergang | -9 | +1 | -0.0099 | +0.0050 | +0.0432 | -0.0217 |
| dio_mcm_episode_0krixak | verjuengung_oberflaeche | stabile_bedeutungsinsel | junge_spur | -7 | -3 | -0.0176 | +0.0168 | +0.0026 | +0.0186 |
| dio_mcm_episode_0om13wf | verjuengung_oberflaeche | hoeherer_cluster_uebergang | junge_spur | -7 | -1 | +0.0341 | -0.0233 | +0.0697 | -0.0974 |
| dio_mcm_episode_0jatqr8 | reifung_oder_verdichtung | rekopplungszone | stabile_bedeutungsinsel | -6 | -1 | -0.0174 | +0.0095 | +0.0978 | -0.0101 |
| dio_mcm_episode_1n2f96o | reifung_oder_verdichtung | junge_spur | rekopplungszone | +6 | +1 | -0.0029 | -0.0077 | +0.0045 | +0.0077 |
| dio_mcm_episode_0l3i7ey | verjuengung_oberflaeche | hoeherer_cluster_uebergang | junge_spur | -5 | -1 | +0.0388 | -0.0499 | -0.0967 | -0.2201 |

## Befund

Weniger als die Haelfte der gemeinsamen Tokens behaelt ihre Verdichtungszone. Das wuerde auf staerkere Weltfaerbung oder noch unreife Oberflaechenbindung hinweisen.
Mehr wechselnde Tokens gehen in Richtung Reifung/Verdichtung als in Oeffnung/Drift. Das deutet auf nachtraegliche Stabilisierung einzelner Feldzeichen.
Randnaehe tritt als kleine, aber gesonderte Bewegung auf. Das passt zur bisherigen Lesart: Rand ist lokal und selten, nicht die Grundform des Feldes.

## Wie es weitergeht

Als naechstes sollten die wechselnden Tokens gegen ihre Rohweltabschnitte gelesen werden. Ziel: unterscheiden, ob Zonenwechsel aus Weltphase, Sinnesaufnahme, Rekopplung oder echter MCM-Drift entsteht.
