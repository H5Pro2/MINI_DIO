# MCM-Brueckenanker Landschaft

## Zweck

Diese passive Diagnose prueft, ob `0b7nep9` als Anschlussanker singulaer ist oder ob das Feld mehrere vergleichbare Anschlussanker ausbildet.
Sie nutzt vorhandene Bruecken-, Kern- und Pfadbefunde. Es wird keine neue Feldmechanik eingefuehrt.

## Gesamtbefund

- Untersuchte Bruecken-Tokens: `104`
- Klassenprofil: `schwacher_anschluss:79; brueckenkern:12; lokaler_anschlussanker:7; starker_anschlussanker:6`
- Starke Anschlussanker: `6`
- Lokale Anschlussanker: `7`

## Starke Anschlussanker

| Token | Gewicht | Welten | Dauer | Bidirektional | Pfadklasse | Bewegung | Kantenprofil |
|---|---:|---:|---:|---:|---|---|---|
| `0ykar6i` | 88 | 4 | 98.95 | 1 | offener_driftpfad | oeffnung_oder_drift | aussen_zu_bruecke:1; bruecke_zu_aussen:1 |
| `1jwnjz4` | 50 | 4 | 92.08 | 1 | rekoppelnder_pfad | reifung_oder_verdichtung | bruecke_zu_aussen:1; aussen_zu_bruecke:1 |
| `1xx3u1e` | 46 | 3 | 133.04 | 3 | brueckenpfad | reifung_oder_verdichtung | bruecke_zu_aussen:5; aussen_zu_bruecke:4 |
| `1q3us3f` | 43 | 5 | 68.30 | 3 | stabile_insel | stabil | bruecke_zu_aussen:3; aussen_zu_bruecke:3 |
| `1jx2k4i` | 35 | 6 | 159.66 | 1 | stabile_insel | stabil | aussen_zu_bruecke:1; bruecke_zu_aussen:1 |
| `0v5p8er` | 32 | 3 | 125.81 | 3 | brueckenpfad | reifung_oder_verdichtung | aussen_zu_bruecke:4; bruecke_zu_aussen:3 |

## Staerkste Brueckenrollen

| Klasse | Token | Gewicht | Welten | Dauer | Rolle | Kantenprofil | Phasenprofil |
|---|---|---:|---:|---:|---|---|---|
| brueckenkern | `0e7qvj1` | 268 | 6 | 126.93 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:13; bruecke_zu_bruecke:8; aussen_zu_bruecke:6 | oeffnend_belastender_austritt:17; rekoppelnder_austritt:6; gemischter_austritt:4 |
| brueckenkern | `18l3thm` | 159 | 6 | 47.69 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:4; bruecke_zu_aussen:3; aussen_zu_bruecke:3 | gemischter_austritt:4; rekoppelnder_austritt:3; oeffnend_belastender_austritt:3 |
| brueckenkern | `0b7nep9` | 141 | 4 | 107.06 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:9; aussen_zu_bruecke:7; bruecke_zu_bruecke:2 | rekoppelnder_austritt:12; oeffnend_belastender_austritt:5; gemischter_austritt:1 |
| brueckenkern | `0mji3u6` | 97 | 6 | 94.06 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:6; aussen_zu_bruecke:2 | rekoppelnder_austritt:4; oeffnend_belastender_austritt:3; gemischter_austritt:1 |
| brueckenkern | `1joiyc3` | 66 | 6 | 211.06 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:8; bruecke_zu_bruecke:4; aussen_zu_bruecke:3 | oeffnend_belastender_austritt:7; rekoppelnder_austritt:6; gemischter_austritt:2 |
| brueckenkern | `18n06fj` | 38 | 5 | 4.79 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:4; aussen_zu_bruecke:2 | rekoppelnder_austritt:3; oeffnend_belastender_austritt:3 |
| brueckenkern | `0jbl5pq` | 32 | 6 | 2.50 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:5; bruecke_zu_bruecke:4; bruecke_zu_aussen:2 | oeffnend_belastender_austritt:5; rekoppelnder_austritt:4; gemischter_austritt:2 |
| brueckenkern | `0qzjuvj` | 29 | 6 | 2.55 | offene_variante -> zentrum_stabil | bruecke_zu_bruecke:4; bruecke_zu_aussen:2 | rekoppelnder_austritt:3; gemischter_austritt:2; oeffnend_belastender_austritt:1 |
| brueckenkern | `0hjnwsk` | 26 | 4 | 2.62 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:4; aussen_zu_bruecke:3 | rekoppelnder_austritt:7 |
| brueckenkern | `0db07p4` | 23 | 3 | 56.96 | zentrum_stabil -> zentrum_stabil | bruecke_zu_bruecke:4; aussen_zu_bruecke:3; bruecke_zu_aussen:1 | rekoppelnder_austritt:6; oeffnend_belastender_austritt:2 |
| brueckenkern | `0l3i7ey` | 11 | 3 | 1.55 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:3; bruecke_zu_aussen:3; bruecke_zu_bruecke:2 | rekoppelnder_austritt:4; oeffnend_belastender_austritt:2; gemischter_austritt:2 |
| brueckenkern | `17c7qwp` | 9 | 1 | 48.78 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:3; bruecke_zu_aussen:2; bruecke_zu_bruecke:2 | rekoppelnder_austritt:4; oeffnend_belastender_austritt:2; gemischter_austritt:1 |
| starker_anschlussanker | `0ykar6i` | 88 | 4 | 98.95 | zentrum_stabil -> zentrum_stabil | aussen_zu_bruecke:1; bruecke_zu_aussen:1 | rekoppelnder_austritt:2 |
| starker_anschlussanker | `1jwnjz4` | 50 | 4 | 92.08 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:1; aussen_zu_bruecke:1 | rekoppelnder_austritt:1; gemischter_austritt:1 |
| starker_anschlussanker | `1xx3u1e` | 46 | 3 | 133.04 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:5; aussen_zu_bruecke:4 | oeffnend_belastender_austritt:6; rekoppelnder_austritt:3 |
| starker_anschlussanker | `1q3us3f` | 43 | 5 | 68.30 | zentrum_stabil -> zentrum_stabil | bruecke_zu_aussen:3; aussen_zu_bruecke:3 | oeffnend_belastender_austritt:3; rekoppelnder_austritt:2; gemischter_austritt:1 |

## Interpretation

Das Feld bildet mehrere starke Anschlussanker.
Damit waere die Anschlussanker-Rolle keine Singularitaet, sondern eine wiederkehrende Zwischenebene der Topologie.

Wichtig: Ein Anschlussanker ist nicht gleich Brueckenkern.
Der Brueckenkern verbindet stabile zentrale Bedeutungsraeume. Ein Anschlussanker koppelt solche Raeume an offene Drift-, Rand- oder Seitenphasen.

## Wie es weitergeht

Als naechstes sollte die staerkste Anschlussanker-Landschaft gegen weitere Weltgruppen geprueft werden, um zu sehen, ob die Rolle unter anderer Weltspannung stabil bleibt oder neue Anschlussanker entstehen.