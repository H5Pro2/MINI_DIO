# MCM-Brueckenanker Landschaft

## Zweck

Diese passive Diagnose prueft, ob `0b7nep9` als Anschlussanker singulaer ist oder ob das Feld mehrere vergleichbare Anschlussanker ausbildet.
Sie nutzt vorhandene Bruecken-, Kern- und Pfadbefunde. Es wird keine neue Feldmechanik eingefuehrt.

## Gesamtbefund

- Untersuchte Bruecken-Tokens: `95`
- Klassenprofil: `schwacher_anschluss:70; brueckenkern:15; lokaler_anschlussanker:6; starker_anschlussanker:4`
- Starke Anschlussanker: `4`
- Lokale Anschlussanker: `6`

## Starke Anschlussanker

| Token | Gewicht | Welten | Dauer | Bidirektional | Pfadklasse | Bewegung | Kantenprofil |
|---|---:|---:|---:|---:|---|---|---|
| `1jwnjz4` | 59 | 4 | 94.76 | 2 | stabile_insel | stabil | bruecke_zu_aussen:2; aussen_zu_bruecke:2 |
| `0ybr5e3` | 41 | 1 | 112.37 | 3 | stabile_insel | stabil | bruecke_zu_aussen:3; aussen_zu_bruecke:3 |
| `1q3us3f` | 39 | 5 | 59.59 | 2 | rekoppelnder_pfad | reifung_oder_verdichtung | bruecke_zu_aussen:2; aussen_zu_bruecke:2 |
| `1ahj81f` | 30 | 5 | 15.07 | 2 | stabile_insel | stabil | aussen_zu_bruecke:2; bruecke_zu_aussen:2 |

## Staerkste Brueckenrollen

| Klasse | Token | Gewicht | Welten | Dauer | Rolle | Kantenprofil | Phasenprofil |
|---|---|---:|---:|---:|---|---|---|
| brueckenkern | `0e7qvj1` | 276 | 6 | 123.33 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:14; bruecke_zu_aussen:12; aussen_zu_bruecke:4 | oeffnend_belastender_austritt:19; rekoppelnder_austritt:6; gemischter_austritt:5 |
| brueckenkern | `0b7nep9` | 228 | 4 | 85.15 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:8; aussen_zu_bruecke:7; bruecke_zu_bruecke:4 | rekoppelnder_austritt:11; oeffnend_belastender_austritt:7; gemischter_austritt:1 |
| brueckenkern | `0ykar6i` | 215 | 4 | 71.02 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:4; aussen_zu_bruecke:3; bruecke_zu_aussen:3 | oeffnend_belastender_austritt:5; rekoppelnder_austritt:4; gemischter_austritt:1 |
| brueckenkern | `18l3thm` | 171 | 6 | 55.43 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:8; bruecke_zu_aussen:2; aussen_zu_bruecke:2 | oeffnend_belastender_austritt:5; gemischter_austritt:4; rekoppelnder_austritt:3 |
| brueckenkern | `1jx2k4i` | 115 | 6 | 66.35 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:4; aussen_zu_bruecke:4; bruecke_zu_aussen:4 | oeffnend_belastender_austritt:8; rekoppelnder_austritt:3; gemischter_austritt:1 |
| brueckenkern | `1joiyc3` | 101 | 6 | 146.90 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:8; bruecke_zu_aussen:7; aussen_zu_bruecke:2 | oeffnend_belastender_austritt:9; rekoppelnder_austritt:6; gemischter_austritt:2 |
| brueckenkern | `0mji3u6` | 97 | 6 | 94.06 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:6; aussen_zu_bruecke:2 | rekoppelnder_austritt:4; oeffnend_belastender_austritt:3; gemischter_austritt:1 |
| brueckenkern | `14coypf` | 57 | 3 | 100.07 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:8; bruecke_zu_aussen:7; aussen_zu_bruecke:3 | oeffnend_belastender_austritt:11; rekoppelnder_austritt:5; gemischter_austritt:2 |
| brueckenkern | `1xx3u1e` | 49 | 3 | 125.08 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:5; aussen_zu_bruecke:3; bruecke_zu_bruecke:2 | oeffnend_belastender_austritt:7; rekoppelnder_austritt:3 |
| brueckenkern | `0qzjuvj` | 33 | 6 | 2.67 | offene_variante -> zentrum_stabil | bruecke_zu_bruecke:4; bruecke_zu_aussen:2 | gemischter_austritt:3; rekoppelnder_austritt:2; oeffnend_belastender_austritt:1 |
| brueckenkern | `0jbl5pq` | 31 | 6 | 2.55 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:6; bruecke_zu_bruecke:2; bruecke_zu_aussen:2 | oeffnend_belastender_austritt:5; rekoppelnder_austritt:3; gemischter_austritt:2 |
| brueckenkern | `18n06fj` | 30 | 5 | 5.37 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:3; bruecke_zu_bruecke:2 | oeffnend_belastender_austritt:3; rekoppelnder_austritt:2 |
| brueckenkern | `0z748ck` | 26 | 5 | 9.15 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:4; aussen_zu_bruecke:1; bruecke_zu_aussen:1 | gemischter_austritt:3; rekoppelnder_austritt:2; oeffnend_belastender_austritt:1 |
| brueckenkern | `0db07p4` | 23 | 3 | 56.96 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:4; aussen_zu_bruecke:3; bruecke_zu_aussen:1 | rekoppelnder_austritt:6; oeffnend_belastender_austritt:2 |
| brueckenkern | `02ujuqf` | 9 | 3 | 139.44 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:3; bruecke_zu_bruecke:2 | oeffnend_belastender_austritt:4; rekoppelnder_austritt:1 |
| starker_anschlussanker | `1jwnjz4` | 59 | 4 | 94.76 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:2; aussen_zu_bruecke:2 | oeffnend_belastender_austritt:2; rekoppelnder_austritt:1; gemischter_austritt:1 |

## Interpretation

Das Feld bildet mehrere starke Anschlussanker.
Damit waere die Anschlussanker-Rolle keine Singularitaet, sondern eine wiederkehrende Zwischenebene der Topologie.

Wichtig: Ein Anschlussanker ist nicht gleich Brueckenkern.
Der Brueckenkern verbindet stabile zentrale Bedeutungsraeume. Ein Anschlussanker koppelt solche Raeume an offene Drift-, Rand- oder Seitenphasen.

## Wie es weitergeht

Als naechstes sollte die staerkste Anschlussanker-Landschaft gegen weitere Weltgruppen geprueft werden, um zu sehen, ob die Rolle unter anderer Weltspannung stabil bleibt oder neue Anschlussanker entstehen.