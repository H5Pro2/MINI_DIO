# MCM-Bruecken Netzwerk

## Zweck

Diese Diagnose liest die stabilen Bruecken nicht mehr als Einzelzeichen, sondern als Netzwerk aus Eintritts- und Austrittskanten.
Knoten sind MCM-Episodentokens. Kanten sind beobachtete Eintritte in eine Bruecke oder Austritte aus einer Bruecke.

## Netzwerkbestand

- Brueckenknoten: `10`
- Kanten gesamt: `60`
- Interne Bruecke-zu-Bruecke-Kanten: `6`
- Bruecke-zu-Aussen-Kanten: `29`
- Aussen-zu-Bruecke-Kanten: `25`

## Austrittsphasen Der Kanten

| Austrittsphase | Kanten |
|---|---:|
| gemischter_austritt | 8 |
| oeffnend_belastender_austritt | 30 |
| rekoppelnder_austritt | 22 |

## Brueckenknoten

| Token | Segmente | Welten | Dauer | Dominanter Eintritt | intern | Dominanter Austritt | intern | Austrittsphase |
|---|---:|---:|---:|---|---:|---|---:|---|
| dio_mcm_episode_0e7qvj1 | 90 | 8 | 193.10 | dio_mcm_episode_0mji3u6 | 0 | dio_mcm_episode_18l3thm | 0 | oeffnend_belastender_austritt |
| dio_mcm_episode_0jbl5pq | 11 | 6 | 2.55 | dio_mcm_episode_0lne9ax | 0 | dio_mcm_episode_0qzjuvj | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0qzjuvj | 9 | 6 | 2.56 | dio_mcm_episode_0jbl5pq | 1 | dio_mcm_episode_0z748ck | 0 | gemischter_austritt |
| dio_mcm_episode_0hjnwsk | 8 | 4 | 2.62 | dio_mcm_episode_0aztxel | 0 | dio_mcm_episode_18n06fj | 0 | rekoppelnder_austritt |
| dio_mcm_episode_0l3i7ey | 5 | 3 | 1.40 | dio_mcm_episode_0ldht3x | 0 | dio_mcm_episode_0lne9ax | 0 | rekoppelnder_austritt |
| dio_mcm_episode_1hs3jsa | 3 | 2 | 204.00 | dio_mcm_episode_1q3us3f | 0 | dio_mcm_episode_1q3us3f | 0 | oeffnend_belastender_austritt |
| dio_mcm_episode_0ifxej6 | 1 | 1 | 1.00 | dio_mcm_episode_0mm85pw | 0 | dio_mcm_episode_0r1o8ja | 0 | oeffnend_belastender_austritt |
| dio_mcm_episode_0q7j4gf | 1 | 1 | 1.00 | dio_mcm_episode_0qhiq5e | 0 | dio_mcm_episode_0ldenly | 0 | rekoppelnder_austritt |
| dio_mcm_episode_0y1i8dq | 1 | 1 | 1.00 | dio_mcm_episode_0om13wf | 0 | dio_mcm_episode_0om13wf | 0 | oeffnend_belastender_austritt |
| dio_mcm_episode_1i31hl0 | 1 | 1 | 2.00 | dio_mcm_episode_1mesbjy | 0 | dio_mcm_episode_0om13wf | 0 | rekoppelnder_austritt |

## Staerkste Interne Brueckenkanten

| Quelle | Ziel | Relation | Anzahl | Welten | Austrittsphase |
|---|---|---|---:|---:|---|
| dio_mcm_episode_0jbl5pq | dio_mcm_episode_0qzjuvj | austritt | 9 | 6 | oeffnend_belastender_austritt |
| dio_mcm_episode_0jbl5pq | dio_mcm_episode_0qzjuvj | eintritt | 9 | 6 | gemischter_austritt |
| dio_mcm_episode_0qzjuvj | dio_mcm_episode_0hjnwsk | eintritt | 2 | 2 | rekoppelnder_austritt |
| dio_mcm_episode_0qzjuvj | dio_mcm_episode_0hjnwsk | austritt | 2 | 2 | rekoppelnder_austritt |
| dio_mcm_episode_0l3i7ey | dio_mcm_episode_0jbl5pq | eintritt | 1 | 1 | gemischter_austritt |
| dio_mcm_episode_0l3i7ey | dio_mcm_episode_0jbl5pq | austritt | 1 | 1 | rekoppelnder_austritt |

## Staerkste Externe Austritte

| Quelle | Ziel | Anzahl | Welten | Austrittsphase |
|---|---|---:|---:|---|
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_18l3thm | 30 | 6 | rekoppelnder_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_1jwnjz4 | 27 | 4 | rekoppelnder_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mji3u6 | 12 | 5 | oeffnend_belastender_austritt |
| dio_mcm_episode_0hjnwsk | dio_mcm_episode_18n06fj | 8 | 4 | rekoppelnder_austritt |
| dio_mcm_episode_0qzjuvj | dio_mcm_episode_0z748ck | 6 | 5 | gemischter_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_1hdpu9s | 5 | 2 | oeffnend_belastender_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mm85pw | 2 | 2 | oeffnend_belastender_austritt |
| dio_mcm_episode_0l3i7ey | dio_mcm_episode_0lne9ax | 2 | 2 | rekoppelnder_austritt |
| dio_mcm_episode_1hs3jsa | dio_mcm_episode_1q3us3f | 2 | 2 | oeffnend_belastender_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0jzhgzp | 1 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0lfde2c | 1 | 1 | gemischter_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mw7rev | 1 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0t7i6fh | 1 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0tph7s0 | 1 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_13cw75j | 1 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_14coypf | 1 | 1 | rekoppelnder_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_19dxnmz | 1 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_1jansx7 | 1 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_1q3us3f | 1 | 1 | rekoppelnder_austritt |
| dio_mcm_episode_0ifxej6 | dio_mcm_episode_0r1o8ja | 1 | 1 | oeffnend_belastender_austritt |

## Gegenseitige Brueckenpaare

| Bruecke A | Bruecke B | Kantengewicht |
|---|---|---:|
| dio_mcm_episode_0jbl5pq | dio_mcm_episode_0qzjuvj | 18 |
| dio_mcm_episode_0hjnwsk | dio_mcm_episode_0qzjuvj | 4 |
| dio_mcm_episode_0jbl5pq | dio_mcm_episode_0l3i7ey | 2 |

## Befund

Das staerkste interne Brueckenpaar ist `dio_mcm_episode_0jbl5pq` <-> `dio_mcm_episode_0qzjuvj` mit Kantengewicht `18`. Das spricht fuer eine echte Rueckbezugsstruktur im Brueckennetz.
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
