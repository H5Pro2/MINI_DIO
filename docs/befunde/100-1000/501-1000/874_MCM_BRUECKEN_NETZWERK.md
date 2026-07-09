# MCM-Bruecken Netzwerk

## Zweck

Diese Diagnose liest die stabilen Bruecken nicht mehr als Einzelzeichen, sondern als Netzwerk aus Eintritts- und Austrittskanten.
Knoten sind MCM-Episodentokens. Kanten sind beobachtete Eintritte in eine Bruecke oder Austritte aus einer Bruecke.

## Netzwerkbestand

- Brueckenknoten: `12`
- Kanten gesamt: `94`
- Interne Bruecke-zu-Bruecke-Kanten: `18`
- Bruecke-zu-Aussen-Kanten: `40`
- Aussen-zu-Bruecke-Kanten: `36`

## Austrittsphasen Der Kanten

| Austrittsphase | Kanten |
|---|---:|
| gemischter_austritt | 13 |
| oeffnend_belastender_austritt | 49 |
| rekoppelnder_austritt | 32 |

## Brueckenknoten

| Token | Segmente | Welten | Dauer | Dominanter Eintritt | intern | Dominanter Austritt | intern | Austrittsphase |
|---|---:|---:|---:|---|---:|---|---:|---|
| dio_mcm_episode_0e7qvj1 | 54 | 6 | 259.30 | dio_mcm_episode_18l3thm | 1 | dio_mcm_episode_18l3thm | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_18l3thm | 34 | 5 | 45.26 | dio_mcm_episode_0e7qvj1 | 1 | dio_mcm_episode_0e7qvj1 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_1joiyc3 | 29 | 7 | 200.90 | dio_mcm_episode_1jx2k4i | 0 | dio_mcm_episode_1jx2k4i | 0 | oeffnend_belastender_austritt |
| dio_mcm_episode_0b7nep9 | 18 | 3 | 472.39 | dio_mcm_episode_00nzcuc | 0 | dio_mcm_episode_00nzcuc | 0 | oeffnend_belastender_austritt |
| dio_mcm_episode_0db07p4 | 15 | 5 | 17.60 | dio_mcm_episode_1joiyc3 | 1 | dio_mcm_episode_1joiyc3 | 1 | rekoppelnder_austritt |
| dio_mcm_episode_0mji3u6 | 11 | 5 | 8.91 | dio_mcm_episode_0e7qvj1 | 1 | dio_mcm_episode_0e7qvj1 | 1 | rekoppelnder_austritt |
| dio_mcm_episode_0jbl5pq | 10 | 5 | 2.00 | dio_mcm_episode_0lne9ax | 0 | dio_mcm_episode_0qzjuvj | 1 | gemischter_austritt |
| dio_mcm_episode_0qzjuvj | 10 | 5 | 2.70 | dio_mcm_episode_0jbl5pq | 1 | dio_mcm_episode_0z748ck | 0 | oeffnend_belastender_austritt |
| dio_mcm_episode_18n06fj | 6 | 4 | 2.33 | dio_mcm_episode_0hjnwsk | 0 | dio_mcm_episode_0mji3u6 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_1xx3u1e | 6 | 2 | 15.00 | dio_mcm_episode_0geqqo3 | 0 | dio_mcm_episode_0geqqo3 | 0 | oeffnend_belastender_austritt |
| dio_mcm_episode_1al8fjz | 3 | 2 | 1.67 | dio_mcm_episode_0dsrwv5 | 0 | dio_mcm_episode_1y2gc2i | 0 | oeffnend_belastender_austritt |
| dio_mcm_episode_05lquqm | 2 | 1 | 2.00 | dio_mcm_episode_08ubq99 | 0 | dio_mcm_episode_0ej0lhx | 0 | oeffnend_belastender_austritt |

## Staerkste Interne Brueckenkanten

| Quelle | Ziel | Relation | Anzahl | Welten | Austrittsphase |
|---|---|---|---:|---:|---|
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_18l3thm | austritt | 23 | 5 | rekoppelnder_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_18l3thm | eintritt | 23 | 5 | oeffnend_belastender_austritt |
| dio_mcm_episode_18l3thm | dio_mcm_episode_0e7qvj1 | eintritt | 19 | 5 | gemischter_austritt |
| dio_mcm_episode_18l3thm | dio_mcm_episode_0e7qvj1 | austritt | 19 | 5 | oeffnend_belastender_austritt |
| dio_mcm_episode_0db07p4 | dio_mcm_episode_1joiyc3 | austritt | 11 | 5 | rekoppelnder_austritt |
| dio_mcm_episode_0db07p4 | dio_mcm_episode_1joiyc3 | eintritt | 11 | 5 | oeffnend_belastender_austritt |
| dio_mcm_episode_0mji3u6 | dio_mcm_episode_0e7qvj1 | eintritt | 11 | 5 | oeffnend_belastender_austritt |
| dio_mcm_episode_0mji3u6 | dio_mcm_episode_0e7qvj1 | austritt | 11 | 5 | rekoppelnder_austritt |
| dio_mcm_episode_0jbl5pq | dio_mcm_episode_0qzjuvj | austritt | 7 | 5 | rekoppelnder_austritt |
| dio_mcm_episode_0jbl5pq | dio_mcm_episode_0qzjuvj | eintritt | 7 | 5 | oeffnend_belastender_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mji3u6 | austritt | 6 | 4 | oeffnend_belastender_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mji3u6 | eintritt | 6 | 4 | rekoppelnder_austritt |
| dio_mcm_episode_1joiyc3 | dio_mcm_episode_0db07p4 | eintritt | 6 | 4 | rekoppelnder_austritt |
| dio_mcm_episode_1joiyc3 | dio_mcm_episode_0db07p4 | austritt | 6 | 4 | oeffnend_belastender_austritt |
| dio_mcm_episode_18n06fj | dio_mcm_episode_0mji3u6 | eintritt | 4 | 3 | oeffnend_belastender_austritt |
| dio_mcm_episode_18n06fj | dio_mcm_episode_0mji3u6 | austritt | 4 | 3 | oeffnend_belastender_austritt |
| dio_mcm_episode_0qzjuvj | dio_mcm_episode_18n06fj | austritt | 1 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0qzjuvj | dio_mcm_episode_18n06fj | eintritt | 1 | 1 | gemischter_austritt |

## Staerkste Externe Austritte

| Quelle | Ziel | Anzahl | Welten | Austrittsphase |
|---|---|---:|---:|---|
| dio_mcm_episode_1joiyc3 | dio_mcm_episode_1jx2k4i | 16 | 5 | rekoppelnder_austritt |
| dio_mcm_episode_18l3thm | dio_mcm_episode_1q3us3f | 15 | 3 | rekoppelnder_austritt |
| dio_mcm_episode_0qzjuvj | dio_mcm_episode_0z748ck | 9 | 5 | oeffnend_belastender_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_1jwnjz4 | 7 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0b7nep9 | dio_mcm_episode_00nzcuc | 6 | 2 | gemischter_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_1hdpu9s | 6 | 2 | gemischter_austritt |
| dio_mcm_episode_0b7nep9 | dio_mcm_episode_0w4x7xs | 5 | 1 | rekoppelnder_austritt |
| dio_mcm_episode_1xx3u1e | dio_mcm_episode_0geqqo3 | 5 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0db07p4 | dio_mcm_episode_1i1sl4l | 2 | 2 | rekoppelnder_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_1ggl8cd | 2 | 2 | rekoppelnder_austritt |
| dio_mcm_episode_0jbl5pq | dio_mcm_episode_0aztxel | 2 | 1 | gemischter_austritt |
| dio_mcm_episode_18n06fj | dio_mcm_episode_0z748ck | 2 | 2 | rekoppelnder_austritt |
| dio_mcm_episode_1al8fjz | dio_mcm_episode_1y2gc2i | 2 | 2 | rekoppelnder_austritt |
| dio_mcm_episode_05lquqm | dio_mcm_episode_0ej0lhx | 1 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_05lquqm | dio_mcm_episode_0jatqr8 | 1 | 1 | rekoppelnder_austritt |
| dio_mcm_episode_0b7nep9 | dio_mcm_episode_0fljihc | 1 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0b7nep9 | dio_mcm_episode_0mm85pw | 1 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0b7nep9 | dio_mcm_episode_0mw7rev | 1 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0b7nep9 | dio_mcm_episode_0rz7ra9 | 1 | 1 | gemischter_austritt |
| dio_mcm_episode_0b7nep9 | dio_mcm_episode_0tosxof | 1 | 1 | rekoppelnder_austritt |

## Gegenseitige Brueckenpaare

| Bruecke A | Bruecke B | Kantengewicht |
|---|---|---:|
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_18l3thm | 84 |
| dio_mcm_episode_0db07p4 | dio_mcm_episode_1joiyc3 | 34 |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mji3u6 | 34 |
| dio_mcm_episode_0jbl5pq | dio_mcm_episode_0qzjuvj | 14 |
| dio_mcm_episode_0mji3u6 | dio_mcm_episode_18n06fj | 8 |
| dio_mcm_episode_0qzjuvj | dio_mcm_episode_18n06fj | 2 |

## Befund

Das staerkste interne Brueckenpaar ist `dio_mcm_episode_0e7qvj1` <-> `dio_mcm_episode_18l3thm` mit Kantengewicht `84`. Das spricht fuer eine echte Rueckbezugsstruktur im Brueckennetz.
Es gibt interne Bruecke-zu-Bruecke-Kanten. Bruecken sind damit nicht nur Ausgaenge aus dem Feld, sondern koennen andere Bruecken aktivieren oder rahmen.
Die meisten Austritte fuehren dennoch in Aussen- oder Nicht-Bruecken-Tokens. Das passt zur Uebergangslesart: Bruecken halten eine Innenphase und fuehren danach in andere Feldlagen.

## Bedeutung

Die Netzwerklesung verschiebt die Brueckenhypothese weiter:

```text
Bruecke = gehaltene Innenphase + gerichtete Kanten + Rueckbezuege
```

Damit wird Bedeutung nicht nur als Insel oder Punkt lesbar, sondern als topologische Verbindung zwischen Feldzustaenden.

## Wie es weitergeht

Als naechstes sollte das staerkste Brueckenpaar gezielt gelesen werden: Welche Weltphasen erzeugen `0e7qvj1` und `18l3thm`, und warum halten sie sich gegenseitig so stabil?
