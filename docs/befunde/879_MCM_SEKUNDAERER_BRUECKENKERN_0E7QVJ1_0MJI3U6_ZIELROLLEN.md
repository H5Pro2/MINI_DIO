# MCM-Zentraler Brueckenkern Zielrollen

## Zweck

Diese Diagnose liest, wohin der zentrale Brueckenkern fuehrt.
Sie unterscheidet interne Kernbewegung, Austritt aus dem Kern und Eintritt von aussen in den Kern.

- Kern: `dio_mcm_episode_0e7qvj1, dio_mcm_episode_0mji3u6`

## Kantenbestand

| Richtungstyp | Kanten |
|---|---:|
| aussen_zu_kern | 9 |
| kern_intern | 4 |
| kern_zu_aussen | 13 |

## Austritte Vom Kern Nach Pfadklasse

| Typ | Gewicht |
|---|---:|
| brueckenpfad | 46 |
| rekoppelnder_pfad | 8 |
| unbekannt | 7 |
| stabile_insel | 6 |
| junge_oberflaeche | 1 |
| randpfad | 1 |

## Austritte Vom Kern Nach Zone

| Typ | Gewicht |
|---|---:|
| stabile_bedeutungsinsel | 52 |
| rekopplungszone | 8 |
| unbekannt | 7 |
| junge_spur | 1 |
| randnahe_verdichtung | 1 |

## Eintritte In Den Kern Nach Pfadklasse

| Typ | Gewicht |
|---|---:|
| brueckenpfad | 46 |
| stabile_insel | 16 |
| rekoppelnder_pfad | 8 |
| unbekannt | 1 |

## Eintritte In Den Kern Nach Zone

| Typ | Gewicht |
|---|---:|
| stabile_bedeutungsinsel | 54 |
| rekopplungszone | 8 |
| hoeherer_cluster_uebergang | 8 |
| unbekannt | 1 |

## Staerkste Kernkontakte

| Richtung | Quelle | Ziel | Gewicht | Welten | Aussenklasse | Aussenzone | Phase |
|---|---|---|---:|---:|---|---|---|
| kern_zu_aussen | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_18l3thm | 23 | 5 | brueckenpfad | stabile_bedeutungsinsel | rekoppelnder_austritt |
| kern_zu_aussen | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_18l3thm | 23 | 5 | brueckenpfad | stabile_bedeutungsinsel | oeffnend_belastender_austritt |
| aussen_zu_kern | dio_mcm_episode_18l3thm | dio_mcm_episode_0e7qvj1 | 19 | 5 | brueckenpfad | stabile_bedeutungsinsel | gemischter_austritt |
| aussen_zu_kern | dio_mcm_episode_18l3thm | dio_mcm_episode_0e7qvj1 | 19 | 5 | brueckenpfad | stabile_bedeutungsinsel | oeffnend_belastender_austritt |
| kern_intern | dio_mcm_episode_0mji3u6 | dio_mcm_episode_0e7qvj1 | 11 | 5 | - | - | oeffnend_belastender_austritt |
| kern_intern | dio_mcm_episode_0mji3u6 | dio_mcm_episode_0e7qvj1 | 11 | 5 | - | - | rekoppelnder_austritt |
| aussen_zu_kern | dio_mcm_episode_0z748ck | dio_mcm_episode_0e7qvj1 | 10 | 5 | stabile_insel | stabile_bedeutungsinsel | oeffnend_belastender_austritt |
| kern_zu_aussen | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_1jwnjz4 | 7 | 1 | rekoppelnder_pfad | rekopplungszone | oeffnend_belastender_austritt |
| aussen_zu_kern | dio_mcm_episode_1jwnjz4 | dio_mcm_episode_0e7qvj1 | 6 | 1 | rekoppelnder_pfad | rekopplungszone | oeffnend_belastender_austritt |
| aussen_zu_kern | dio_mcm_episode_1hdpu9s | dio_mcm_episode_0e7qvj1 | 6 | 2 | stabile_insel | stabile_bedeutungsinsel | oeffnend_belastender_austritt |
| kern_intern | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mji3u6 | 6 | 4 | - | - | oeffnend_belastender_austritt |
| kern_intern | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mji3u6 | 6 | 4 | - | - | rekoppelnder_austritt |
| kern_zu_aussen | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_1hdpu9s | 6 | 2 | stabile_insel | stabile_bedeutungsinsel | gemischter_austritt |
| aussen_zu_kern | dio_mcm_episode_18n06fj | dio_mcm_episode_0mji3u6 | 4 | 3 | brueckenpfad | hoeherer_cluster_uebergang | oeffnend_belastender_austritt |
| aussen_zu_kern | dio_mcm_episode_18n06fj | dio_mcm_episode_0mji3u6 | 4 | 3 | brueckenpfad | hoeherer_cluster_uebergang | oeffnend_belastender_austritt |
| aussen_zu_kern | dio_mcm_episode_0lfde2c | dio_mcm_episode_0e7qvj1 | 2 | 1 | rekoppelnder_pfad | rekopplungszone | oeffnend_belastender_austritt |
| kern_zu_aussen | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_1ggl8cd | 2 | 2 | unbekannt | unbekannt | rekoppelnder_austritt |
| aussen_zu_kern | dio_mcm_episode_10b8y4e | dio_mcm_episode_0mji3u6 | 1 | 1 | unbekannt | unbekannt | rekoppelnder_austritt |
| kern_zu_aussen | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_1pmt8u2 | 1 | 1 | junge_oberflaeche | junge_spur | rekoppelnder_austritt |
| kern_zu_aussen | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mw7rev | 1 | 1 | randpfad | randnahe_verdichtung | oeffnend_belastender_austritt |
| kern_zu_aussen | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0lfde2c | 1 | 1 | rekoppelnder_pfad | rekopplungszone | oeffnend_belastender_austritt |
| kern_zu_aussen | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0jdgxa5 | 1 | 1 | unbekannt | unbekannt | oeffnend_belastender_austritt |
| kern_zu_aussen | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0n22aiv | 1 | 1 | unbekannt | unbekannt | oeffnend_belastender_austritt |
| kern_zu_aussen | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_19dxnmz | 1 | 1 | unbekannt | unbekannt | oeffnend_belastender_austritt |

## Austrittsphasen Gewichtet

| Phase | Gewicht |
|---|---:|
| oeffnend_belastender_austritt | 104 |
| rekoppelnder_austritt | 45 |
| gemischter_austritt | 25 |

## Befund

Der zentrale Kern fuehrt gewichtet am staerksten zu `brueckenpfad` mit Gewicht `46`.
Die staerkste Zielzone ausserhalb des Kerns ist `stabile_bedeutungsinsel` mit Gewicht `52`.
Der zentrale Kern fuehrt kaum direkt in Randpfade. Er wirkt eher als Zentrum-/Rekopplungsuebergang als als Randkanal.
Die Austritte fuehren staerker in stabile oder rekoppelnde Rollen als in offene Drift. Das stuetzt die Lesart eines stabilisierenden Uebergangskerns.

## Bedeutung

Der zentrale Brueckenkern wirkt nicht wie ein chaotischer Durchbruch nach aussen.
Er verbindet vor allem interne Brueckenbewegung mit stabilen oder rekoppelnden Anschlussrollen.

## Wie es weitergeht

Als naechstes sollte derselbe Zielrollen-Test fuer die sekundaeren Brueckenkerne laufen. Dann wird sichtbar, ob der zentrale Kern eine Sonderrolle hat oder ob alle Kerne aehnlich anschliessen.
