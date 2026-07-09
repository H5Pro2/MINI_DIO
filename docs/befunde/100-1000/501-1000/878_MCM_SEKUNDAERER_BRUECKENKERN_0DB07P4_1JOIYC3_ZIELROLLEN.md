# MCM-Zentraler Brueckenkern Zielrollen

## Zweck

Diese Diagnose liest, wohin der zentrale Brueckenkern fuehrt.
Sie unterscheidet interne Kernbewegung, Austritt aus dem Kern und Eintritt von aussen in den Kern.

- Kern: `dio_mcm_episode_0db07p4, dio_mcm_episode_1joiyc3`

## Kantenbestand

| Richtungstyp | Kanten |
|---|---:|
| aussen_zu_kern | 8 |
| kern_intern | 4 |
| kern_zu_aussen | 10 |

## Austritte Vom Kern Nach Pfadklasse

| Typ | Gewicht |
|---|---:|
| stabile_insel | 17 |
| unbekannt | 7 |
| junge_oberflaeche | 1 |
| randpfad | 1 |

## Austritte Vom Kern Nach Zone

| Typ | Gewicht |
|---|---:|
| stabile_bedeutungsinsel | 17 |
| unbekannt | 7 |
| junge_spur | 1 |
| randnahe_verdichtung | 1 |

## Eintritte In Den Kern Nach Pfadklasse

| Typ | Gewicht |
|---|---:|
| stabile_insel | 17 |
| unbekannt | 9 |
| rekoppelnder_pfad | 1 |

## Eintritte In Den Kern Nach Zone

| Typ | Gewicht |
|---|---:|
| stabile_bedeutungsinsel | 18 |
| unbekannt | 9 |

## Staerkste Kernkontakte

| Richtung | Quelle | Ziel | Gewicht | Welten | Aussenklasse | Aussenzone | Phase |
|---|---|---|---:|---:|---|---|---|
| aussen_zu_kern | dio_mcm_episode_1jx2k4i | dio_mcm_episode_1joiyc3 | 17 | 5 | stabile_insel | stabile_bedeutungsinsel | gemischter_austritt |
| kern_zu_aussen | dio_mcm_episode_1joiyc3 | dio_mcm_episode_1jx2k4i | 16 | 5 | stabile_insel | stabile_bedeutungsinsel | rekoppelnder_austritt |
| kern_intern | dio_mcm_episode_0db07p4 | dio_mcm_episode_1joiyc3 | 11 | 5 | - | - | rekoppelnder_austritt |
| kern_intern | dio_mcm_episode_0db07p4 | dio_mcm_episode_1joiyc3 | 11 | 5 | - | - | oeffnend_belastender_austritt |
| kern_intern | dio_mcm_episode_1joiyc3 | dio_mcm_episode_0db07p4 | 6 | 4 | - | - | rekoppelnder_austritt |
| kern_intern | dio_mcm_episode_1joiyc3 | dio_mcm_episode_0db07p4 | 6 | 4 | - | - | oeffnend_belastender_austritt |
| aussen_zu_kern | dio_mcm_episode_1i1sl4l | dio_mcm_episode_0db07p4 | 4 | 2 | unbekannt | unbekannt | rekoppelnder_austritt |
| kern_zu_aussen | dio_mcm_episode_0db07p4 | dio_mcm_episode_1i1sl4l | 2 | 2 | unbekannt | unbekannt | rekoppelnder_austritt |
| aussen_zu_kern | dio_mcm_episode_0t1ymth | dio_mcm_episode_0db07p4 | 1 | 1 | rekoppelnder_pfad | stabile_bedeutungsinsel | rekoppelnder_austritt |
| aussen_zu_kern | dio_mcm_episode_04s5k7g | dio_mcm_episode_0db07p4 | 1 | 1 | unbekannt | unbekannt | oeffnend_belastender_austritt |
| aussen_zu_kern | dio_mcm_episode_0mqw5s3 | dio_mcm_episode_0db07p4 | 1 | 1 | unbekannt | unbekannt | rekoppelnder_austritt |
| aussen_zu_kern | dio_mcm_episode_0nuo9k1 | dio_mcm_episode_0db07p4 | 1 | 1 | unbekannt | unbekannt | rekoppelnder_austritt |
| aussen_zu_kern | dio_mcm_episode_1q3u8v6 | dio_mcm_episode_0db07p4 | 1 | 1 | unbekannt | unbekannt | oeffnend_belastender_austritt |
| aussen_zu_kern | dio_mcm_episode_1rzvd1k | dio_mcm_episode_1joiyc3 | 1 | 1 | unbekannt | unbekannt | oeffnend_belastender_austritt |
| kern_zu_aussen | dio_mcm_episode_1joiyc3 | dio_mcm_episode_0sxikqi | 1 | 1 | junge_oberflaeche | junge_spur | oeffnend_belastender_austritt |
| kern_zu_aussen | dio_mcm_episode_1joiyc3 | dio_mcm_episode_0mm85pw | 1 | 1 | randpfad | randnahe_verdichtung | oeffnend_belastender_austritt |
| kern_zu_aussen | dio_mcm_episode_1joiyc3 | dio_mcm_episode_1ahj81f | 1 | 1 | stabile_insel | stabile_bedeutungsinsel | rekoppelnder_austritt |
| kern_zu_aussen | dio_mcm_episode_0db07p4 | dio_mcm_episode_04s5k7g | 1 | 1 | unbekannt | unbekannt | oeffnend_belastender_austritt |
| kern_zu_aussen | dio_mcm_episode_1joiyc3 | dio_mcm_episode_0h9ka55 | 1 | 1 | unbekannt | unbekannt | oeffnend_belastender_austritt |
| kern_zu_aussen | dio_mcm_episode_0db07p4 | dio_mcm_episode_0mqw5s3 | 1 | 1 | unbekannt | unbekannt | oeffnend_belastender_austritt |
| kern_zu_aussen | dio_mcm_episode_1joiyc3 | dio_mcm_episode_19w9kxc | 1 | 1 | unbekannt | unbekannt | oeffnend_belastender_austritt |
| kern_zu_aussen | dio_mcm_episode_1joiyc3 | dio_mcm_episode_1rzvd1k | 1 | 1 | unbekannt | unbekannt | oeffnend_belastender_austritt |

## Austrittsphasen Gewichtet

| Phase | Gewicht |
|---|---:|
| rekoppelnder_austritt | 43 |
| oeffnend_belastender_austritt | 27 |
| gemischter_austritt | 17 |

## Befund

Der zentrale Kern fuehrt gewichtet am staerksten zu `stabile_insel` mit Gewicht `17`.
Die staerkste Zielzone ausserhalb des Kerns ist `stabile_bedeutungsinsel` mit Gewicht `17`.
Der zentrale Kern fuehrt kaum direkt in Randpfade. Er wirkt eher als Zentrum-/Rekopplungsuebergang als als Randkanal.
Die Austritte fuehren staerker in stabile oder rekoppelnde Rollen als in offene Drift. Das stuetzt die Lesart eines stabilisierenden Uebergangskerns.

## Bedeutung

Der zentrale Brueckenkern wirkt nicht wie ein chaotischer Durchbruch nach aussen.
Er verbindet vor allem interne Brueckenbewegung mit stabilen oder rekoppelnden Anschlussrollen.

## Wie es weitergeht

Als naechstes sollte derselbe Zielrollen-Test fuer die sekundaeren Brueckenkerne laufen. Dann wird sichtbar, ob der zentrale Kern eine Sonderrolle hat oder ob alle Kerne aehnlich anschliessen.
