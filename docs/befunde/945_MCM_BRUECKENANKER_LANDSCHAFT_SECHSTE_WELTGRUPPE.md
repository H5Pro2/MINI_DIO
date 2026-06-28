# MCM-Brueckenanker Landschaft

## Zweck

Diese passive Diagnose prueft, ob `0b7nep9` als Anschlussanker singulaer ist oder ob das Feld mehrere vergleichbare Anschlussanker ausbildet.
Sie nutzt vorhandene Bruecken-, Kern- und Pfadbefunde. Es wird keine neue Feldmechanik eingefuehrt.

## Gesamtbefund

- Untersuchte Bruecken-Tokens: `45`
- Klassenprofil: `schwacher_anschluss:36; brueckenkern:4; starker_anschlussanker:4; lokaler_anschlussanker:1`
- Starke Anschlussanker: `4`
- Lokale Anschlussanker: `1`

## Starke Anschlussanker

| Token | Gewicht | Welten | Dauer | Bidirektional | Pfadklasse | Bewegung | Kantenprofil |
|---|---:|---:|---:|---:|---|---|---|
| `0e7qvj1` | 176 | 6 | 186.55 | 6 | brueckenpfad | reifung_oder_verdichtung | bruecke_zu_aussen:15; aussen_zu_bruecke:8 |
| `18l3thm` | 55 | 6 | 110.25 | 1 | - | - | bruecke_zu_aussen:1; aussen_zu_bruecke:1 |
| `1jwnjz4` | 50 | 4 | 92.08 | 1 | - | - | bruecke_zu_aussen:1; aussen_zu_bruecke:1 |
| `0mji3u6` | 37 | 6 | 226.84 | 1 | offener_driftpfad | stabil | aussen_zu_bruecke:1; bruecke_zu_aussen:1 |

## Staerkste Brueckenrollen

| Klasse | Token | Gewicht | Welten | Dauer | Rolle | Kantenprofil | Phasenprofil |
|---|---|---:|---:|---:|---|---|---|
| brueckenkern | `0jbl5pq` | 32 | 6 | 2.50 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:5; bruecke_zu_bruecke:4; bruecke_zu_aussen:2 | oeffnend_belastender_austritt:5; rekoppelnder_austritt:4; gemischter_austritt:2 |
| brueckenkern | `0qzjuvj` | 29 | 6 | 2.55 | offene_variante -> zentrum_stabil | bruecke_zu_bruecke:4; bruecke_zu_aussen:2 | rekoppelnder_austritt:3; gemischter_austritt:2; oeffnend_belastender_austritt:1 |
| brueckenkern | `0hjnwsk` | 18 | 4 | 2.44 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:3; bruecke_zu_bruecke:2; bruecke_zu_aussen:1 | rekoppelnder_austritt:6 |
| brueckenkern | `0l3i7ey` | 11 | 3 | 1.55 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:3; bruecke_zu_aussen:3; bruecke_zu_bruecke:2 | rekoppelnder_austritt:4; oeffnend_belastender_austritt:2; gemischter_austritt:2 |
| starker_anschlussanker | `0e7qvj1` | 176 | 6 | 186.55 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:15; aussen_zu_bruecke:8 | oeffnend_belastender_austritt:15; rekoppelnder_austritt:4; gemischter_austritt:4 |
| starker_anschlussanker | `18l3thm` | 55 | 6 | 110.25 | - -> - | bruecke_zu_aussen:1; aussen_zu_bruecke:1 | rekoppelnder_austritt:1; gemischter_austritt:1 |
| starker_anschlussanker | `1jwnjz4` | 50 | 4 | 92.08 | - -> - | bruecke_zu_aussen:1; aussen_zu_bruecke:1 | rekoppelnder_austritt:1; gemischter_austritt:1 |
| starker_anschlussanker | `0mji3u6` | 37 | 6 | 226.84 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:1; bruecke_zu_aussen:1 | oeffnend_belastender_austritt:2 |
| lokaler_anschlussanker | `0z748ck` | 12 | 5 | 16.50 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:1; bruecke_zu_aussen:1 | oeffnend_belastender_austritt:1; gemischter_austritt:1 |
| schwacher_anschluss | `1hdpu9s` | 11 | 3 | 18.73 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:1; bruecke_zu_aussen:1 | oeffnend_belastender_austritt:2 |
| schwacher_anschluss | `0lne9ax` | 9 | 6 | 2.44 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:2; bruecke_zu_aussen:1 | rekoppelnder_austritt:2; oeffnend_belastender_austritt:1 |
| schwacher_anschluss | `1q3us3f` | 8 | 2 | 328.25 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:2; bruecke_zu_aussen:2 | oeffnend_belastender_austritt:3; rekoppelnder_austritt:1 |
| schwacher_anschluss | `18n06fj` | 8 | 4 | 2.62 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:1 | rekoppelnder_austritt:1 |
| schwacher_anschluss | `1hs3jsa` | 6 | 2 | 204.00 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:2; bruecke_zu_aussen:2 | oeffnend_belastender_austritt:4 |
| schwacher_anschluss | `0aztxel` | 6 | 3 | 2.67 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:2; bruecke_zu_aussen:1 | rekoppelnder_austritt:2; gemischter_austritt:1 |
| schwacher_anschluss | `0ldht3x` | 4 | 3 | 1.25 | - -> - | aussen_zu_bruecke:2 | oeffnend_belastender_austritt:2 |

## Interpretation

Das Feld bildet mehrere starke Anschlussanker.
Damit waere die Anschlussanker-Rolle keine Singularitaet, sondern eine wiederkehrende Zwischenebene der Topologie.

Wichtig: Ein Anschlussanker ist nicht gleich Brueckenkern.
Der Brueckenkern verbindet stabile zentrale Bedeutungsraeume. Ein Anschlussanker koppelt solche Raeume an offene Drift-, Rand- oder Seitenphasen.

## Wie es weitergeht

Als naechstes sollte die staerkste Anschlussanker-Landschaft gegen weitere Weltgruppen geprueft werden, um zu sehen, ob die Rolle unter anderer Weltspannung stabil bleibt oder neue Anschlussanker entstehen.