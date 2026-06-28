# MCM-Brueckenanker Landschaft

## Zweck

Diese passive Diagnose prueft, ob `0b7nep9` als Anschlussanker singulaer ist oder ob das Feld mehrere vergleichbare Anschlussanker ausbildet.
Sie nutzt vorhandene Bruecken-, Kern- und Pfadbefunde. Es wird keine neue Feldmechanik eingefuehrt.

## Gesamtbefund

- Untersuchte Bruecken-Tokens: `65`
- Klassenprofil: `schwacher_anschluss:50; brueckenkern:8; lokaler_anschlussanker:5; starker_anschlussanker:2`
- Starke Anschlussanker: `2`
- Lokale Anschlussanker: `5`

## Starke Anschlussanker

| Token | Gewicht | Welten | Dauer | Bidirektional | Pfadklasse | Bewegung | Kantenprofil |
|---|---:|---:|---:|---:|---|---|---|
| `0b7nep9` | 35 | 2 | 470.94 | 3 | brueckenpfad | stabil | bruecke_zu_aussen:8; aussen_zu_bruecke:6 |
| `1jx2k4i` | 33 | 5 | 133.18 | 1 | stabile_insel | stabil | aussen_zu_bruecke:1; bruecke_zu_aussen:1 |

## Staerkste Brueckenrollen

| Klasse | Token | Gewicht | Welten | Dauer | Rolle | Kantenprofil | Phasenprofil |
|---|---|---:|---:|---:|---|---|---|
| brueckenkern | `0e7qvj1` | 165 | 5 | 174.21 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:11; bruecke_zu_bruecke:8; aussen_zu_bruecke:4 | oeffnend_belastender_austritt:15; rekoppelnder_austritt:6; gemischter_austritt:2 |
| brueckenkern | `18l3thm` | 110 | 5 | 77.90 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:4; bruecke_zu_aussen:1; aussen_zu_bruecke:1 | rekoppelnder_austritt:2; oeffnend_belastender_austritt:2; gemischter_austritt:2 |
| brueckenkern | `1joiyc3` | 74 | 5 | 138.82 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:7; bruecke_zu_bruecke:4; aussen_zu_bruecke:2 | oeffnend_belastender_austritt:8; rekoppelnder_austritt:4; gemischter_austritt:1 |
| brueckenkern | `0db07p4` | 47 | 5 | 56.43 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:6; bruecke_zu_bruecke:4; bruecke_zu_aussen:3 | rekoppelnder_austritt:7; oeffnend_belastender_austritt:6 |
| brueckenkern | `0mji3u6` | 43 | 5 | 180.37 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:6; aussen_zu_bruecke:1 | oeffnend_belastender_austritt:4; rekoppelnder_austritt:3 |
| brueckenkern | `0qzjuvj` | 28 | 5 | 2.57 | offene_variante -> zentrum_stabil | bruecke_zu_bruecke:4; aussen_zu_bruecke:2; bruecke_zu_aussen:1 | oeffnend_belastender_austritt:5; rekoppelnder_austritt:1; gemischter_austritt:1 |
| brueckenkern | `0jbl5pq` | 27 | 5 | 2.26 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:6; bruecke_zu_bruecke:2; bruecke_zu_aussen:2 | rekoppelnder_austritt:4; oeffnend_belastender_austritt:3; gemischter_austritt:3 |
| brueckenkern | `18n06fj` | 17 | 3 | 4.06 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:4; aussen_zu_bruecke:2; bruecke_zu_aussen:1 | oeffnend_belastender_austritt:4; rekoppelnder_austritt:2; gemischter_austritt:1 |
| starker_anschlussanker | `0b7nep9` | 35 | 2 | 470.94 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:8; aussen_zu_bruecke:6 | oeffnend_belastender_austritt:5; rekoppelnder_austritt:5; gemischter_austritt:4 |
| starker_anschlussanker | `1jx2k4i` | 33 | 5 | 133.18 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:1; bruecke_zu_aussen:1 | gemischter_austritt:1; rekoppelnder_austritt:1 |
| lokaler_anschlussanker | `1q3us3f` | 26 | 3 | 57.27 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:1; aussen_zu_bruecke:1 | rekoppelnder_austritt:1; gemischter_austritt:1 |
| lokaler_anschlussanker | `0z748ck` | 22 | 5 | 59.45 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:2; bruecke_zu_aussen:2 | oeffnend_belastender_austritt:2; rekoppelnder_austritt:2 |
| lokaler_anschlussanker | `00nzcuc` | 14 | 2 | 134.07 | - -> - | aussen_zu_bruecke:1; bruecke_zu_aussen:1 | oeffnend_belastender_austritt:1; gemischter_austritt:1 |
| lokaler_anschlussanker | `1hdpu9s` | 12 | 2 | 20.42 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:1; bruecke_zu_aussen:1 | oeffnend_belastender_austritt:1; gemischter_austritt:1 |
| lokaler_anschlussanker | `1xx3u1e` | 12 | 2 | 15.00 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:2; aussen_zu_bruecke:1 | oeffnend_belastender_austritt:2; gemischter_austritt:1 |
| schwacher_anschluss | `1jwnjz4` | 13 | 1 | 20.23 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:1; aussen_zu_bruecke:1 | oeffnend_belastender_austritt:2 |

## Interpretation

Das Feld bildet mehrere starke Anschlussanker.
Damit waere die Anschlussanker-Rolle keine Singularitaet, sondern eine wiederkehrende Zwischenebene der Topologie.
`0b7nep9` bleibt dabei ein starker Anschlussanker, ist aber nicht die einzige Auspraegung dieser Rolle.

Wichtig: Ein Anschlussanker ist nicht gleich Brueckenkern.
Der Brueckenkern verbindet stabile zentrale Bedeutungsraeume. Ein Anschlussanker koppelt solche Raeume an offene Drift-, Rand- oder Seitenphasen.

## Wie es weitergeht

Als naechstes sollte die staerkste Anschlussanker-Landschaft gegen weitere Weltgruppen geprueft werden, um zu sehen, ob die Rolle unter anderer Weltspannung stabil bleibt oder neue Anschlussanker entstehen.