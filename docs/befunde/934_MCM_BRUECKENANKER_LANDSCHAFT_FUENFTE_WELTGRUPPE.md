# MCM-Brueckenanker Landschaft

## Zweck

Diese passive Diagnose prueft, ob `0b7nep9` als Anschlussanker singulaer ist oder ob das Feld mehrere vergleichbare Anschlussanker ausbildet.
Sie nutzt vorhandene Bruecken-, Kern- und Pfadbefunde. Es wird keine neue Feldmechanik eingefuehrt.

## Gesamtbefund

- Untersuchte Bruecken-Tokens: `90`
- Klassenprofil: `schwacher_anschluss:66; brueckenkern:18; lokaler_anschlussanker:4; starker_anschlussanker:2`
- Starke Anschlussanker: `2`
- Lokale Anschlussanker: `4`

## Starke Anschlussanker

| Token | Gewicht | Welten | Dauer | Bidirektional | Pfadklasse | Bewegung | Kantenprofil |
|---|---:|---:|---:|---:|---|---|---|
| `1jwnjz4` | 59 | 4 | 94.76 | 2 | rekoppelnder_pfad | reifung_oder_verdichtung | bruecke_zu_aussen:2; aussen_zu_bruecke:2 |
| `1q3us3f` | 44 | 5 | 71.55 | 3 | rekoppelnder_pfad | reifung_oder_verdichtung | bruecke_zu_aussen:4; aussen_zu_bruecke:3 |

## Staerkste Brueckenrollen

| Klasse | Token | Gewicht | Welten | Dauer | Rolle | Kantenprofil | Phasenprofil |
|---|---|---:|---:|---:|---|---|---|
| brueckenkern | `0e7qvj1` | 270 | 6 | 126.00 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:12; bruecke_zu_aussen:12; aussen_zu_bruecke:5 | oeffnend_belastender_austritt:19; rekoppelnder_austritt:6; gemischter_austritt:4 |
| brueckenkern | `0b7nep9` | 228 | 4 | 85.15 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:8; aussen_zu_bruecke:7; bruecke_zu_bruecke:4 | rekoppelnder_austritt:11; oeffnend_belastender_austritt:7; gemischter_austritt:1 |
| brueckenkern | `0ykar6i` | 215 | 4 | 71.02 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:4; aussen_zu_bruecke:3; bruecke_zu_aussen:3 | oeffnend_belastender_austritt:5; rekoppelnder_austritt:4; gemischter_austritt:1 |
| brueckenkern | `18l3thm` | 171 | 6 | 55.43 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:8; bruecke_zu_aussen:2; aussen_zu_bruecke:2 | oeffnend_belastender_austritt:5; gemischter_austritt:4; rekoppelnder_austritt:3 |
| brueckenkern | `0mji3u6` | 97 | 6 | 94.06 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:6; aussen_zu_bruecke:2 | rekoppelnder_austritt:4; oeffnend_belastender_austritt:3; gemischter_austritt:1 |
| brueckenkern | `14l8khu` | 71 | 3 | 63.66 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:8; bruecke_zu_aussen:1 | oeffnend_belastender_austritt:6; rekoppelnder_austritt:3 |
| brueckenkern | `14coypf` | 70 | 3 | 88.87 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:12; bruecke_zu_aussen:6; aussen_zu_bruecke:2 | oeffnend_belastender_austritt:13; rekoppelnder_austritt:5; gemischter_austritt:2 |
| brueckenkern | `0v5p8er` | 54 | 3 | 94.63 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:4; aussen_zu_bruecke:3; bruecke_zu_aussen:2 | oeffnend_belastender_austritt:6; rekoppelnder_austritt:2; gemischter_austritt:1 |
| brueckenkern | `18n06fj` | 38 | 5 | 4.79 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:4; aussen_zu_bruecke:2 | rekoppelnder_austritt:3; oeffnend_belastender_austritt:3 |
| brueckenkern | `0jbl5pq` | 32 | 6 | 2.50 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:5; bruecke_zu_bruecke:4; bruecke_zu_aussen:2 | oeffnend_belastender_austritt:5; rekoppelnder_austritt:4; gemischter_austritt:2 |
| brueckenkern | `0qzjuvj` | 29 | 6 | 2.55 | offene_variante -> zentrum_stabil | bruecke_zu_bruecke:4; bruecke_zu_aussen:2 | rekoppelnder_austritt:3; gemischter_austritt:2; oeffnend_belastender_austritt:1 |
| brueckenkern | `0hjnwsk` | 27 | 4 | 2.63 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:6; aussen_zu_bruecke:2 | rekoppelnder_austritt:8 |
| brueckenkern | `0om13wf` | 15 | 2 | 1.33 | offene_variante -> offene_variante | aussen_zu_bruecke:6; bruecke_zu_aussen:3; bruecke_zu_bruecke:2 | rekoppelnder_austritt:7; oeffnend_belastender_austritt:4 |
| brueckenkern | `0ultars` | 13 | 2 | 1.31 | offene_variante -> zentrum_stabil | bruecke_zu_bruecke:6; bruecke_zu_aussen:2 | oeffnend_belastender_austritt:5; rekoppelnder_austritt:3 |
| brueckenkern | `0l3i7ey` | 11 | 3 | 1.55 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:3; bruecke_zu_aussen:3; bruecke_zu_bruecke:2 | rekoppelnder_austritt:4; oeffnend_belastender_austritt:2; gemischter_austritt:2 |
| brueckenkern | `00yl137` | 8 | 1 | 1.38 | spannungsrand_kippnaehe -> offene_variante | bruecke_zu_bruecke:4; aussen_zu_bruecke:2; bruecke_zu_aussen:2 | oeffnend_belastender_austritt:6; rekoppelnder_austritt:2 |

## Interpretation

Das Feld bildet mehrere starke Anschlussanker.
Damit waere die Anschlussanker-Rolle keine Singularitaet, sondern eine wiederkehrende Zwischenebene der Topologie.

Wichtig: Ein Anschlussanker ist nicht gleich Brueckenkern.
Der Brueckenkern verbindet stabile zentrale Bedeutungsraeume. Ein Anschlussanker koppelt solche Raeume an offene Drift-, Rand- oder Seitenphasen.

## Wie es weitergeht

Als naechstes sollte die staerkste Anschlussanker-Landschaft gegen weitere Weltgruppen geprueft werden, um zu sehen, ob die Rolle unter anderer Weltspannung stabil bleibt oder neue Anschlussanker entstehen.