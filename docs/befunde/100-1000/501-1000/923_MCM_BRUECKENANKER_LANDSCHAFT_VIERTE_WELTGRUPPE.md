# MCM-Brueckenanker Landschaft

## Zweck

Diese passive Diagnose prueft, ob `0b7nep9` als Anschlussanker singulaer ist oder ob das Feld mehrere vergleichbare Anschlussanker ausbildet.
Sie nutzt vorhandene Bruecken-, Kern- und Pfadbefunde. Es wird keine neue Feldmechanik eingefuehrt.

## Gesamtbefund

- Untersuchte Bruecken-Tokens: `90`
- Klassenprofil: `schwacher_anschluss:67; brueckenkern:12; lokaler_anschlussanker:6; starker_anschlussanker:5`
- Starke Anschlussanker: `5`
- Lokale Anschlussanker: `6`

## Starke Anschlussanker

| Token | Gewicht | Welten | Dauer | Bidirektional | Pfadklasse | Bewegung | Kantenprofil |
|---|---:|---:|---:|---:|---|---|---|
| `1jwnjz4` | 59 | 4 | 94.76 | 2 | rekoppelnder_pfad | reifung_oder_verdichtung | bruecke_zu_aussen:2; aussen_zu_bruecke:2 |
| `1joiyc3` | 57 | 6 | 243.12 | 4 | brueckenpfad | stabil | bruecke_zu_aussen:9; aussen_zu_bruecke:4 |
| `0ybr5e3` | 41 | 1 | 112.37 | 3 | rekoppelnder_pfad | reifung_oder_verdichtung | bruecke_zu_aussen:3; aussen_zu_bruecke:3 |
| `1q3us3f` | 39 | 5 | 59.59 | 2 | stabile_insel | stabil | bruecke_zu_aussen:2; aussen_zu_bruecke:2 |
| `1jx2k4i` | 35 | 6 | 159.66 | 1 | stabile_insel | stabil | aussen_zu_bruecke:1; bruecke_zu_aussen:1 |

## Staerkste Brueckenrollen

| Klasse | Token | Gewicht | Welten | Dauer | Rolle | Kantenprofil | Phasenprofil |
|---|---|---:|---:|---:|---|---|---|
| brueckenkern | `0e7qvj1` | 270 | 6 | 126.00 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:12; bruecke_zu_aussen:12; aussen_zu_bruecke:5 | oeffnend_belastender_austritt:19; rekoppelnder_austritt:6; gemischter_austritt:4 |
| brueckenkern | `0b7nep9` | 228 | 4 | 85.15 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:8; aussen_zu_bruecke:7; bruecke_zu_bruecke:4 | rekoppelnder_austritt:11; oeffnend_belastender_austritt:7; gemischter_austritt:1 |
| brueckenkern | `0ykar6i` | 215 | 4 | 71.02 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:4; aussen_zu_bruecke:3; bruecke_zu_aussen:3 | oeffnend_belastender_austritt:5; rekoppelnder_austritt:4; gemischter_austritt:1 |
| brueckenkern | `18l3thm` | 171 | 6 | 55.43 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:8; bruecke_zu_aussen:2; aussen_zu_bruecke:2 | oeffnend_belastender_austritt:5; gemischter_austritt:4; rekoppelnder_austritt:3 |
| brueckenkern | `0mji3u6` | 97 | 6 | 94.06 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:6; aussen_zu_bruecke:2 | rekoppelnder_austritt:4; oeffnend_belastender_austritt:3; gemischter_austritt:1 |
| brueckenkern | `14coypf` | 57 | 3 | 100.07 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:8; bruecke_zu_aussen:7; aussen_zu_bruecke:3 | oeffnend_belastender_austritt:11; rekoppelnder_austritt:5; gemischter_austritt:2 |
| brueckenkern | `1xx3u1e` | 49 | 3 | 125.08 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:5; aussen_zu_bruecke:3; bruecke_zu_bruecke:2 | oeffnend_belastender_austritt:7; rekoppelnder_austritt:3 |
| brueckenkern | `18n06fj` | 38 | 5 | 4.79 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:4; aussen_zu_bruecke:2 | rekoppelnder_austritt:3; oeffnend_belastender_austritt:3 |
| brueckenkern | `0jbl5pq` | 31 | 6 | 2.55 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:6; bruecke_zu_bruecke:2; bruecke_zu_aussen:2 | oeffnend_belastender_austritt:5; rekoppelnder_austritt:3; gemischter_austritt:2 |
| brueckenkern | `0qzjuvj` | 29 | 6 | 2.55 | offene_variante -> zentrum_stabil | bruecke_zu_bruecke:4; bruecke_zu_aussen:2 | rekoppelnder_austritt:3; gemischter_austritt:2; oeffnend_belastender_austritt:1 |
| brueckenkern | `0hjnwsk` | 26 | 4 | 2.62 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:4; aussen_zu_bruecke:3 | rekoppelnder_austritt:7 |
| brueckenkern | `02ujuqf` | 9 | 3 | 139.44 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:3; bruecke_zu_bruecke:2 | oeffnend_belastender_austritt:4; rekoppelnder_austritt:1 |
| starker_anschlussanker | `1jwnjz4` | 59 | 4 | 94.76 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:2; aussen_zu_bruecke:2 | oeffnend_belastender_austritt:2; rekoppelnder_austritt:1; gemischter_austritt:1 |
| starker_anschlussanker | `1joiyc3` | 57 | 6 | 243.12 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:9; aussen_zu_bruecke:4 | oeffnend_belastender_austritt:7; rekoppelnder_austritt:4; gemischter_austritt:2 |
| starker_anschlussanker | `0ybr5e3` | 41 | 1 | 112.37 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:3; aussen_zu_bruecke:3 | rekoppelnder_austritt:3; oeffnend_belastender_austritt:2; gemischter_austritt:1 |
| starker_anschlussanker | `1q3us3f` | 39 | 5 | 59.59 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:2; aussen_zu_bruecke:2 | rekoppelnder_austritt:2; gemischter_austritt:1; oeffnend_belastender_austritt:1 |

## Interpretation

Das Feld bildet mehrere starke Anschlussanker.
Damit waere die Anschlussanker-Rolle keine Singularitaet, sondern eine wiederkehrende Zwischenebene der Topologie.

Wichtig: Ein Anschlussanker ist nicht gleich Brueckenkern.
Der Brueckenkern verbindet stabile zentrale Bedeutungsraeume. Ein Anschlussanker koppelt solche Raeume an offene Drift-, Rand- oder Seitenphasen.

## Wie es weitergeht

Als naechstes sollte die staerkste Anschlussanker-Landschaft gegen weitere Weltgruppen geprueft werden, um zu sehen, ob die Rolle unter anderer Weltspannung stabil bleibt oder neue Anschlussanker entstehen.