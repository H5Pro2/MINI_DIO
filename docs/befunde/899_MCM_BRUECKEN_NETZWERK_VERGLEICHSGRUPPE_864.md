# MCM-Bruecken Netzwerk

## Zweck

Diese Diagnose liest die stabilen Bruecken nicht mehr als Einzelzeichen, sondern als Netzwerk aus Eintritts- und Austrittskanten.
Knoten sind MCM-Episodentokens. Kanten sind beobachtete Eintritte in eine Bruecke oder Austritte aus einer Bruecke.

## Netzwerkbestand

- Brueckenknoten: `18`
- Kanten gesamt: `162`
- Interne Bruecke-zu-Bruecke-Kanten: `38`
- Bruecke-zu-Aussen-Kanten: `65`
- Aussen-zu-Bruecke-Kanten: `59`

## Austrittsphasen Der Kanten

| Austrittsphase | Kanten |
|---|---:|
| gemischter_austritt | 18 |
| oeffnend_belastender_austritt | 79 |
| rekoppelnder_austritt | 65 |

## Brueckenknoten

| Token | Segmente | Welten | Dauer | Dominanter Eintritt | intern | Dominanter Austritt | intern | Austrittsphase |
|---|---:|---:|---:|---|---:|---|---:|---|
| dio_mcm_episode_0e7qvj1 | 90 | 8 | 193.10 | dio_mcm_episode_0mji3u6 | 1 | dio_mcm_episode_18l3thm | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0b7nep9 | 70 | 5 | 107.81 | dio_mcm_episode_0ykar6i | 1 | dio_mcm_episode_0ykar6i | 1 | rekoppelnder_austritt |
| dio_mcm_episode_0ykar6i | 64 | 4 | 55.56 | dio_mcm_episode_0b7nep9 | 1 | dio_mcm_episode_0b7nep9 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_18l3thm | 52 | 6 | 14.60 | dio_mcm_episode_0e7qvj1 | 1 | dio_mcm_episode_0e7qvj1 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_1jx2k4i | 40 | 6 | 25.52 | dio_mcm_episode_1joiyc3 | 1 | dio_mcm_episode_1joiyc3 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_1joiyc3 | 29 | 8 | 266.62 | dio_mcm_episode_1jx2k4i | 1 | dio_mcm_episode_1jx2k4i | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0mji3u6 | 25 | 6 | 14.08 | dio_mcm_episode_0e7qvj1 | 1 | dio_mcm_episode_0e7qvj1 | 1 | rekoppelnder_austritt |
| dio_mcm_episode_1xx3u1e | 23 | 4 | 133.04 | dio_mcm_episode_0ybr5e3 | 0 | dio_mcm_episode_0ybr5e3 | 0 | oeffnend_belastender_austritt |
| dio_mcm_episode_14coypf | 22 | 3 | 128.09 | dio_mcm_episode_18l3thm | 1 | dio_mcm_episode_14l8khu | 0 | oeffnend_belastender_austritt |
| dio_mcm_episode_0jbl5pq | 11 | 6 | 2.55 | dio_mcm_episode_0lne9ax | 0 | dio_mcm_episode_0qzjuvj | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_18n06fj | 10 | 5 | 2.70 | dio_mcm_episode_0hjnwsk | 0 | dio_mcm_episode_0mji3u6 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0qzjuvj | 9 | 6 | 2.56 | dio_mcm_episode_0jbl5pq | 1 | dio_mcm_episode_0z748ck | 1 | gemischter_austritt |
| dio_mcm_episode_0db07p4 | 7 | 3 | 10.57 | dio_mcm_episode_1joiyc3 | 1 | dio_mcm_episode_1joiyc3 | 1 | rekoppelnder_austritt |
| dio_mcm_episode_0wjn8vm | 7 | 2 | 310.29 | dio_mcm_episode_1engxbn | 0 | dio_mcm_episode_1engxbn | 0 | oeffnend_belastender_austritt |
| dio_mcm_episode_0z748ck | 7 | 5 | 2.86 | dio_mcm_episode_0qzjuvj | 1 | dio_mcm_episode_0e7qvj1 | 1 | gemischter_austritt |
| dio_mcm_episode_1al8fjz | 7 | 5 | 1.57 | dio_mcm_episode_1k0rrn2 | 0 | dio_mcm_episode_1y2gc2i | 0 | rekoppelnder_austritt |
| dio_mcm_episode_05lquqm | 5 | 5 | 1.20 | dio_mcm_episode_0ag2osp | 0 | dio_mcm_episode_079228h | 0 | rekoppelnder_austritt |
| dio_mcm_episode_02ujuqf | 3 | 3 | 3.00 | dio_mcm_episode_0jwgafx | 0 | dio_mcm_episode_1xx3u1e | 1 | oeffnend_belastender_austritt |

## Staerkste Interne Brueckenkanten

| Quelle | Ziel | Relation | Anzahl | Welten | Austrittsphase |
|---|---|---|---:|---:|---|
| dio_mcm_episode_0b7nep9 | dio_mcm_episode_0ykar6i | austritt | 44 | 3 | rekoppelnder_austritt |
| dio_mcm_episode_0b7nep9 | dio_mcm_episode_0ykar6i | eintritt | 44 | 3 | oeffnend_belastender_austritt |
| dio_mcm_episode_0ykar6i | dio_mcm_episode_0b7nep9 | eintritt | 44 | 4 | rekoppelnder_austritt |
| dio_mcm_episode_0ykar6i | dio_mcm_episode_0b7nep9 | austritt | 44 | 4 | oeffnend_belastender_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_18l3thm | austritt | 30 | 6 | rekoppelnder_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_18l3thm | eintritt | 30 | 6 | oeffnend_belastender_austritt |
| dio_mcm_episode_0mji3u6 | dio_mcm_episode_0e7qvj1 | eintritt | 25 | 6 | oeffnend_belastender_austritt |
| dio_mcm_episode_0mji3u6 | dio_mcm_episode_0e7qvj1 | austritt | 25 | 6 | rekoppelnder_austritt |
| dio_mcm_episode_18l3thm | dio_mcm_episode_0e7qvj1 | eintritt | 25 | 5 | gemischter_austritt |
| dio_mcm_episode_18l3thm | dio_mcm_episode_0e7qvj1 | austritt | 25 | 5 | oeffnend_belastender_austritt |
| dio_mcm_episode_1jx2k4i | dio_mcm_episode_1joiyc3 | eintritt | 19 | 6 | gemischter_austritt |
| dio_mcm_episode_1jx2k4i | dio_mcm_episode_1joiyc3 | austritt | 19 | 6 | oeffnend_belastender_austritt |
| dio_mcm_episode_1joiyc3 | dio_mcm_episode_1jx2k4i | austritt | 16 | 6 | rekoppelnder_austritt |
| dio_mcm_episode_1joiyc3 | dio_mcm_episode_1jx2k4i | eintritt | 16 | 6 | oeffnend_belastender_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mji3u6 | austritt | 12 | 5 | oeffnend_belastender_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mji3u6 | eintritt | 12 | 5 | rekoppelnder_austritt |
| dio_mcm_episode_18n06fj | dio_mcm_episode_0mji3u6 | eintritt | 10 | 5 | rekoppelnder_austritt |
| dio_mcm_episode_18n06fj | dio_mcm_episode_0mji3u6 | austritt | 10 | 5 | oeffnend_belastender_austritt |
| dio_mcm_episode_0jbl5pq | dio_mcm_episode_0qzjuvj | austritt | 9 | 6 | oeffnend_belastender_austritt |
| dio_mcm_episode_0jbl5pq | dio_mcm_episode_0qzjuvj | eintritt | 9 | 6 | gemischter_austritt |

## Staerkste Externe Austritte

| Quelle | Ziel | Anzahl | Welten | Austrittsphase |
|---|---|---:|---:|---|
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_1jwnjz4 | 27 | 4 | rekoppelnder_austritt |
| dio_mcm_episode_18l3thm | dio_mcm_episode_1q3us3f | 19 | 5 | rekoppelnder_austritt |
| dio_mcm_episode_1jx2k4i | dio_mcm_episode_1ahj81f | 12 | 4 | oeffnend_belastender_austritt |
| dio_mcm_episode_1xx3u1e | dio_mcm_episode_0ybr5e3 | 11 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0b7nep9 | dio_mcm_episode_1eju9g0 | 10 | 1 | rekoppelnder_austritt |
| dio_mcm_episode_0ykar6i | dio_mcm_episode_0geqqo3 | 9 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0ykar6i | dio_mcm_episode_0ybr5e3 | 9 | 1 | rekoppelnder_austritt |
| dio_mcm_episode_0b7nep9 | dio_mcm_episode_0w4x7xs | 8 | 2 | rekoppelnder_austritt |
| dio_mcm_episode_14coypf | dio_mcm_episode_14l8khu | 7 | 2 | rekoppelnder_austritt |
| dio_mcm_episode_1xx3u1e | dio_mcm_episode_077r0df | 7 | 2 | rekoppelnder_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_1hdpu9s | 5 | 2 | oeffnend_belastender_austritt |
| dio_mcm_episode_0wjn8vm | dio_mcm_episode_1engxbn | 5 | 2 | oeffnend_belastender_austritt |
| dio_mcm_episode_1jx2k4i | dio_mcm_episode_0dgle71 | 5 | 1 | rekoppelnder_austritt |
| dio_mcm_episode_1al8fjz | dio_mcm_episode_1y2gc2i | 4 | 4 | rekoppelnder_austritt |
| dio_mcm_episode_0b7nep9 | dio_mcm_episode_0mw7rev | 3 | 2 | oeffnend_belastender_austritt |
| dio_mcm_episode_14coypf | dio_mcm_episode_1jwnjz4 | 3 | 3 | oeffnend_belastender_austritt |
| dio_mcm_episode_1jx2k4i | dio_mcm_episode_1i1sl4l | 3 | 2 | oeffnend_belastender_austritt |
| dio_mcm_episode_1xx3u1e | dio_mcm_episode_0geqqo3 | 3 | 2 | oeffnend_belastender_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mm85pw | 2 | 2 | oeffnend_belastender_austritt |
| dio_mcm_episode_0qzjuvj | dio_mcm_episode_0hjnwsk | 2 | 2 | rekoppelnder_austritt |

## Gegenseitige Brueckenpaare

| Bruecke A | Bruecke B | Kantengewicht |
|---|---|---:|
| dio_mcm_episode_0b7nep9 | dio_mcm_episode_0ykar6i | 176 |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_18l3thm | 110 |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mji3u6 | 74 |
| dio_mcm_episode_1joiyc3 | dio_mcm_episode_1jx2k4i | 70 |
| dio_mcm_episode_14coypf | dio_mcm_episode_18l3thm | 24 |
| dio_mcm_episode_0mji3u6 | dio_mcm_episode_18n06fj | 20 |
| dio_mcm_episode_0db07p4 | dio_mcm_episode_1joiyc3 | 18 |
| dio_mcm_episode_0jbl5pq | dio_mcm_episode_0qzjuvj | 18 |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0z748ck | 12 |
| dio_mcm_episode_0qzjuvj | dio_mcm_episode_0z748ck | 12 |
| dio_mcm_episode_02ujuqf | dio_mcm_episode_1xx3u1e | 6 |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_14coypf | 4 |

## Befund

Das staerkste interne Brueckenpaar ist `dio_mcm_episode_0b7nep9` <-> `dio_mcm_episode_0ykar6i` mit Kantengewicht `176`. Das spricht fuer eine echte Rueckbezugsstruktur im Brueckennetz.
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
