# MCM-Zentraler Brueckenkern Zielrollen

## Zweck

Diese Diagnose liest, wohin der zentrale Brueckenkern fuehrt.
Sie unterscheidet interne Kernbewegung, Austritt aus dem Kern und Eintritt von aussen in den Kern.

- Kern: `dio_mcm_episode_0e7qvj1, dio_mcm_episode_18l3thm`

## Kantenbestand

| Richtungstyp | Kanten |
|---|---:|
| aussen_zu_kern | 7 |
| kern_intern | 4 |
| kern_zu_aussen | 14 |

## Austritte Vom Kern Nach Pfadklasse

| Typ | Gewicht |
|---|---:|
| stabile_insel | 21 |
| brueckenpfad | 12 |
| rekoppelnder_pfad | 8 |
| unbekannt | 7 |
| junge_oberflaeche | 1 |
| randpfad | 1 |

## Austritte Vom Kern Nach Zone

| Typ | Gewicht |
|---|---:|
| stabile_bedeutungsinsel | 33 |
| rekopplungszone | 8 |
| unbekannt | 7 |
| junge_spur | 1 |
| randnahe_verdichtung | 1 |

## Eintritte In Den Kern Nach Pfadklasse

| Typ | Gewicht |
|---|---:|
| stabile_insel | 27 |
| brueckenpfad | 22 |
| rekoppelnder_pfad | 8 |

## Eintritte In Den Kern Nach Zone

| Typ | Gewicht |
|---|---:|
| stabile_bedeutungsinsel | 49 |
| rekopplungszone | 8 |

## Staerkste Kernkontakte

| Richtung | Quelle | Ziel | Gewicht | Welten | Aussenklasse | Aussenzone | Phase |
|---|---|---|---:|---:|---|---|---|
| kern_intern | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_18l3thm | 23 | 5 | - | - | rekoppelnder_austritt |
| kern_intern | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_18l3thm | 23 | 5 | - | - | oeffnend_belastender_austritt |
| kern_intern | dio_mcm_episode_18l3thm | dio_mcm_episode_0e7qvj1 | 19 | 5 | - | - | gemischter_austritt |
| kern_intern | dio_mcm_episode_18l3thm | dio_mcm_episode_0e7qvj1 | 19 | 5 | - | - | oeffnend_belastender_austritt |
| kern_zu_aussen | dio_mcm_episode_18l3thm | dio_mcm_episode_1q3us3f | 15 | 3 | stabile_insel | stabile_bedeutungsinsel | rekoppelnder_austritt |
| aussen_zu_kern | dio_mcm_episode_0mji3u6 | dio_mcm_episode_0e7qvj1 | 11 | 5 | brueckenpfad | stabile_bedeutungsinsel | oeffnend_belastender_austritt |
| aussen_zu_kern | dio_mcm_episode_0mji3u6 | dio_mcm_episode_0e7qvj1 | 11 | 5 | brueckenpfad | stabile_bedeutungsinsel | rekoppelnder_austritt |
| aussen_zu_kern | dio_mcm_episode_1q3us3f | dio_mcm_episode_18l3thm | 11 | 2 | stabile_insel | stabile_bedeutungsinsel | gemischter_austritt |
| aussen_zu_kern | dio_mcm_episode_0z748ck | dio_mcm_episode_0e7qvj1 | 10 | 5 | stabile_insel | stabile_bedeutungsinsel | oeffnend_belastender_austritt |
| kern_zu_aussen | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_1jwnjz4 | 7 | 1 | rekoppelnder_pfad | rekopplungszone | oeffnend_belastender_austritt |
| aussen_zu_kern | dio_mcm_episode_1jwnjz4 | dio_mcm_episode_0e7qvj1 | 6 | 1 | rekoppelnder_pfad | rekopplungszone | oeffnend_belastender_austritt |
| aussen_zu_kern | dio_mcm_episode_1hdpu9s | dio_mcm_episode_0e7qvj1 | 6 | 2 | stabile_insel | stabile_bedeutungsinsel | oeffnend_belastender_austritt |
| kern_zu_aussen | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mji3u6 | 6 | 4 | brueckenpfad | stabile_bedeutungsinsel | oeffnend_belastender_austritt |
| kern_zu_aussen | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mji3u6 | 6 | 4 | brueckenpfad | stabile_bedeutungsinsel | rekoppelnder_austritt |
| kern_zu_aussen | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_1hdpu9s | 6 | 2 | stabile_insel | stabile_bedeutungsinsel | gemischter_austritt |
| aussen_zu_kern | dio_mcm_episode_0lfde2c | dio_mcm_episode_0e7qvj1 | 2 | 1 | rekoppelnder_pfad | rekopplungszone | oeffnend_belastender_austritt |
| kern_zu_aussen | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_1ggl8cd | 2 | 2 | unbekannt | unbekannt | rekoppelnder_austritt |
| kern_zu_aussen | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_1pmt8u2 | 1 | 1 | junge_oberflaeche | junge_spur | rekoppelnder_austritt |
| kern_zu_aussen | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mw7rev | 1 | 1 | randpfad | randnahe_verdichtung | oeffnend_belastender_austritt |
| kern_zu_aussen | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0lfde2c | 1 | 1 | rekoppelnder_pfad | rekopplungszone | oeffnend_belastender_austritt |
| kern_zu_aussen | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0jdgxa5 | 1 | 1 | unbekannt | unbekannt | oeffnend_belastender_austritt |
| kern_zu_aussen | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0n22aiv | 1 | 1 | unbekannt | unbekannt | oeffnend_belastender_austritt |
| kern_zu_aussen | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_19dxnmz | 1 | 1 | unbekannt | unbekannt | oeffnend_belastender_austritt |
| kern_zu_aussen | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_19w9kxc | 1 | 1 | unbekannt | unbekannt | oeffnend_belastender_austritt |

## Austrittsphasen Gewichtet

| Phase | Gewicht |
|---|---:|
| oeffnend_belastender_austritt | 96 |
| rekoppelnder_austritt | 59 |
| gemischter_austritt | 36 |

## Befund

Der zentrale Kern fuehrt gewichtet am staerksten zu `stabile_insel` mit Gewicht `21`.
Die staerkste Zielzone ausserhalb des Kerns ist `stabile_bedeutungsinsel` mit Gewicht `33`.
Der zentrale Kern fuehrt kaum direkt in Randpfade. Er wirkt eher als Zentrum-/Rekopplungsuebergang als als Randkanal.
Die Austritte fuehren staerker in stabile oder rekoppelnde Rollen als in offene Drift. Das stuetzt die Lesart eines stabilisierenden Uebergangskerns.

## Bedeutung

Der zentrale Brueckenkern wirkt nicht wie ein chaotischer Durchbruch nach aussen.
Er verbindet vor allem interne Brueckenbewegung mit stabilen oder rekoppelnden Anschlussrollen.

## Wie es weitergeht

Als naechstes sollte derselbe Zielrollen-Test fuer die sekundaeren Brueckenkerne laufen. Dann wird sichtbar, ob der zentrale Kern eine Sonderrolle hat oder ob alle Kerne aehnlich anschliessen.
