# MCM-Bruecken Netzwerk

## Zweck

Diese Diagnose liest die stabilen Bruecken nicht mehr als Einzelzeichen, sondern als Netzwerk aus Eintritts- und Austrittskanten.
Knoten sind MCM-Episodentokens. Kanten sind beobachtete Eintritte in eine Bruecke oder Austritte aus einer Bruecke.

## Netzwerkbestand

- Brueckenknoten: `22`
- Kanten gesamt: `161`
- Interne Bruecke-zu-Bruecke-Kanten: `48`
- Bruecke-zu-Aussen-Kanten: `57`
- Aussen-zu-Bruecke-Kanten: `56`

## Austrittsphasen Der Kanten

| Austrittsphase | Kanten |
|---|---:|
| gemischter_austritt | 17 |
| oeffnend_belastender_austritt | 81 |
| rekoppelnder_austritt | 63 |

## Brueckenknoten

| Token | Segmente | Welten | Dauer | Dominanter Eintritt | intern | Dominanter Austritt | intern | Austrittsphase |
|---|---:|---:|---:|---|---:|---|---:|---|
| dio_mcm_episode_0e7qvj1 | 90 | 8 | 193.10 | dio_mcm_episode_0mji3u6 | 1 | dio_mcm_episode_18l3thm | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0b7nep9 | 70 | 5 | 107.81 | dio_mcm_episode_0ykar6i | 1 | dio_mcm_episode_0ykar6i | 1 | rekoppelnder_austritt |
| dio_mcm_episode_0ykar6i | 64 | 4 | 55.56 | dio_mcm_episode_0b7nep9 | 1 | dio_mcm_episode_0b7nep9 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_18l3thm | 52 | 6 | 14.60 | dio_mcm_episode_0e7qvj1 | 1 | dio_mcm_episode_0e7qvj1 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0mji3u6 | 25 | 6 | 14.08 | dio_mcm_episode_0e7qvj1 | 1 | dio_mcm_episode_0e7qvj1 | 1 | rekoppelnder_austritt |
| dio_mcm_episode_14coypf | 22 | 3 | 128.09 | dio_mcm_episode_18l3thm | 1 | dio_mcm_episode_14l8khu | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_14l8khu | 18 | 3 | 50.33 | dio_mcm_episode_0v5p8er | 1 | dio_mcm_episode_0v5p8er | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0v5p8er | 16 | 4 | 125.81 | dio_mcm_episode_14l8khu | 1 | dio_mcm_episode_14l8khu | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0jbl5pq | 11 | 6 | 2.55 | dio_mcm_episode_0lne9ax | 0 | dio_mcm_episode_0qzjuvj | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_18n06fj | 10 | 5 | 2.70 | dio_mcm_episode_0hjnwsk | 1 | dio_mcm_episode_0mji3u6 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0qzjuvj | 9 | 6 | 2.56 | dio_mcm_episode_0jbl5pq | 1 | dio_mcm_episode_0z748ck | 0 | gemischter_austritt |
| dio_mcm_episode_0hjnwsk | 8 | 4 | 2.62 | dio_mcm_episode_0aztxel | 0 | dio_mcm_episode_18n06fj | 1 | rekoppelnder_austritt |
| dio_mcm_episode_1al8fjz | 7 | 5 | 1.57 | dio_mcm_episode_1k0rrn2 | 0 | dio_mcm_episode_1y2gc2i | 0 | rekoppelnder_austritt |
| dio_mcm_episode_0om13wf | 6 | 2 | 1.33 | dio_mcm_episode_0r1o8ja | 0 | dio_mcm_episode_0ultars | 1 | rekoppelnder_austritt |
| dio_mcm_episode_0l3i7ey | 5 | 3 | 1.40 | dio_mcm_episode_0ldht3x | 0 | dio_mcm_episode_0lne9ax | 0 | rekoppelnder_austritt |
| dio_mcm_episode_0ultars | 4 | 3 | 1.25 | dio_mcm_episode_0om13wf | 1 | dio_mcm_episode_0aztxel | 0 | oeffnend_belastender_austritt |
| dio_mcm_episode_00yl137 | 3 | 3 | 1.33 | dio_mcm_episode_00er6t0 | 0 | dio_mcm_episode_0ultars | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0mvjoir | 3 | 3 | 1.00 | dio_mcm_episode_0mw7rev | 0 | dio_mcm_episode_0n5sqpn | 0 | oeffnend_belastender_austritt |
| dio_mcm_episode_1hs3jsa | 3 | 2 | 204.00 | dio_mcm_episode_1q3us3f | 0 | dio_mcm_episode_1q3us3f | 0 | oeffnend_belastender_austritt |
| dio_mcm_episode_0i7gfxw | 1 | 1 | 3.00 | dio_mcm_episode_0tf9fq3 | 1 | dio_mcm_episode_0hjnwsk | 1 | rekoppelnder_austritt |
| dio_mcm_episode_0ifxej6 | 1 | 1 | 1.00 | dio_mcm_episode_0mm85pw | 0 | dio_mcm_episode_0r1o8ja | 0 | oeffnend_belastender_austritt |
| dio_mcm_episode_0tf9fq3 | 1 | 1 | 1.00 | dio_mcm_episode_0oc1i7g | 0 | dio_mcm_episode_0i7gfxw | 1 | gemischter_austritt |

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
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mji3u6 | austritt | 12 | 5 | oeffnend_belastender_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mji3u6 | eintritt | 12 | 5 | rekoppelnder_austritt |
| dio_mcm_episode_0v5p8er | dio_mcm_episode_14l8khu | austritt | 11 | 3 | oeffnend_belastender_austritt |
| dio_mcm_episode_0v5p8er | dio_mcm_episode_14l8khu | eintritt | 11 | 3 | oeffnend_belastender_austritt |
| dio_mcm_episode_14l8khu | dio_mcm_episode_0v5p8er | eintritt | 11 | 2 | rekoppelnder_austritt |
| dio_mcm_episode_14l8khu | dio_mcm_episode_0v5p8er | austritt | 11 | 2 | oeffnend_belastender_austritt |
| dio_mcm_episode_18n06fj | dio_mcm_episode_0mji3u6 | eintritt | 10 | 5 | rekoppelnder_austritt |
| dio_mcm_episode_18n06fj | dio_mcm_episode_0mji3u6 | austritt | 10 | 5 | oeffnend_belastender_austritt |
| dio_mcm_episode_0jbl5pq | dio_mcm_episode_0qzjuvj | austritt | 9 | 6 | oeffnend_belastender_austritt |
| dio_mcm_episode_0jbl5pq | dio_mcm_episode_0qzjuvj | eintritt | 9 | 6 | gemischter_austritt |

## Staerkste Externe Austritte

| Quelle | Ziel | Anzahl | Welten | Austrittsphase |
|---|---|---:|---:|---|
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_1jwnjz4 | 27 | 4 | rekoppelnder_austritt |
| dio_mcm_episode_18l3thm | dio_mcm_episode_1q3us3f | 19 | 5 | rekoppelnder_austritt |
| dio_mcm_episode_0b7nep9 | dio_mcm_episode_1eju9g0 | 10 | 1 | rekoppelnder_austritt |
| dio_mcm_episode_0ykar6i | dio_mcm_episode_0geqqo3 | 9 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_0ykar6i | dio_mcm_episode_0ybr5e3 | 9 | 1 | rekoppelnder_austritt |
| dio_mcm_episode_0b7nep9 | dio_mcm_episode_0w4x7xs | 8 | 2 | rekoppelnder_austritt |
| dio_mcm_episode_0qzjuvj | dio_mcm_episode_0z748ck | 6 | 5 | gemischter_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_1hdpu9s | 5 | 2 | oeffnend_belastender_austritt |
| dio_mcm_episode_0v5p8er | dio_mcm_episode_1ds636q | 4 | 2 | gemischter_austritt |
| dio_mcm_episode_1al8fjz | dio_mcm_episode_1y2gc2i | 4 | 4 | rekoppelnder_austritt |
| dio_mcm_episode_0b7nep9 | dio_mcm_episode_0mw7rev | 3 | 2 | oeffnend_belastender_austritt |
| dio_mcm_episode_14coypf | dio_mcm_episode_1jwnjz4 | 3 | 3 | oeffnend_belastender_austritt |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mm85pw | 2 | 2 | oeffnend_belastender_austritt |
| dio_mcm_episode_0l3i7ey | dio_mcm_episode_0lne9ax | 2 | 2 | rekoppelnder_austritt |
| dio_mcm_episode_0ultars | dio_mcm_episode_0aztxel | 2 | 1 | rekoppelnder_austritt |
| dio_mcm_episode_1al8fjz | dio_mcm_episode_1k0rrn2 | 2 | 2 | oeffnend_belastender_austritt |
| dio_mcm_episode_1hs3jsa | dio_mcm_episode_1q3us3f | 2 | 2 | oeffnend_belastender_austritt |
| dio_mcm_episode_00yl137 | dio_mcm_episode_00dz86x | 1 | 1 | oeffnend_belastender_austritt |
| dio_mcm_episode_00yl137 | dio_mcm_episode_0tv1tha | 1 | 1 | rekoppelnder_austritt |
| dio_mcm_episode_0b7nep9 | dio_mcm_episode_01s42m6 | 1 | 1 | rekoppelnder_austritt |

## Gegenseitige Brueckenpaare

| Bruecke A | Bruecke B | Kantengewicht |
|---|---|---:|
| dio_mcm_episode_0b7nep9 | dio_mcm_episode_0ykar6i | 176 |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_18l3thm | 110 |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mji3u6 | 74 |
| dio_mcm_episode_0v5p8er | dio_mcm_episode_14l8khu | 44 |
| dio_mcm_episode_14coypf | dio_mcm_episode_14l8khu | 26 |
| dio_mcm_episode_14coypf | dio_mcm_episode_18l3thm | 24 |
| dio_mcm_episode_0mji3u6 | dio_mcm_episode_18n06fj | 20 |
| dio_mcm_episode_0jbl5pq | dio_mcm_episode_0qzjuvj | 18 |
| dio_mcm_episode_0hjnwsk | dio_mcm_episode_18n06fj | 16 |
| dio_mcm_episode_0om13wf | dio_mcm_episode_0ultars | 6 |
| dio_mcm_episode_00yl137 | dio_mcm_episode_0ultars | 4 |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_14coypf | 4 |
| dio_mcm_episode_0hjnwsk | dio_mcm_episode_0qzjuvj | 4 |
| dio_mcm_episode_0hjnwsk | dio_mcm_episode_0i7gfxw | 2 |
| dio_mcm_episode_0i7gfxw | dio_mcm_episode_0tf9fq3 | 2 |
| dio_mcm_episode_0jbl5pq | dio_mcm_episode_0l3i7ey | 2 |

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
