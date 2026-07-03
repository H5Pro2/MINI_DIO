# Hoerbarer schmaler Shift - assetrelativer Holdout

Diese Diagnose prueft, ob das Mikrofensterprofil des `hoerbarer_schmaler_folgeschift` auch ausserhalb der BTC-Kandidaten assetrelativ auftaucht.

Jedes Fenster wird gegen die eigene Asset-Basis gelesen. Dadurch wird nicht Preisgroesse oder Lautstaerke eines Assets gemessen, sondern relative Veraenderung der Sinneslage.

Gesucht wurde passiv nach:

- Hoeren steigt gegenueber eigener Asset-Basis deutlich
- Sicht steigt gegenueber eigener Asset-Basis
- Felddruck steigt gegenueber eigener Asset-Basis
- Range sinkt gegenueber eigener Asset-Basis

Die Diagnose erzeugt keine Handlung, keine Richtung und kein Gate.

## Verdichtung

- Kandidatenfenster: `84`

Assets:

- `SOL`: `41`
- `BTC`: `32`
- `DOGE`: `5`
- `XRP`: `4`
- `PAXG`: `2`

Sequenzen:

- `normale_weltspannung->lauter_feldkontakt`: `29`
- `normale_weltspannung->normale_weltspannung`: `19`
- `lauter_feldkontakt->lauter_feldkontakt`: `17`
- `ruhig_zentrumsnah->normale_weltspannung`: `7`
- `offen_suchend->lauter_feldkontakt`: `4`
- `randlastige_sinneslage->normale_weltspannung`: `3`
- `offen_suchend->normale_weltspannung`: `2`
- `lauter_feldkontakt->normale_weltspannung`: `1`
- `normale_weltspannung->offen_suchend`: `1`
- `ruhig_zentrumsnah->offen_suchend`: `1`

Rohklassen:

- `gemischte_rohwelt`: `59`
- `laute_oder_druckvolle_rohwelt`: `16`
- `bewegungsreiche_rohwelt`: `9`

## Staerkste Fenster pro Asset

| Asset | Welt | Skala | Block | Sequenz | Rohklasse | Score | dHoeren | dSicht | dDruck | dRange |
|---|---|---:|---:|---|---|---:|---:|---:|---:|---:|
| BTC | BTC_2024_5M | 100 | 58 | `normale_weltspannung->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.4598 | 0.1999 | 0.0458 | 0.0412 | -0.1729 |
| BTC | BTC_2024_5M | 100 | 96 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.4385 | 0.1976 | 0.0413 | 0.0421 | -0.1576 |
| BTC | BTC_2024_5M | 100 | 98 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.4363 | 0.1872 | 0.0423 | 0.0408 | -0.1661 |
| BTC | BTC_2024_5M | 200 | 48 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3990 | 0.1689 | 0.0412 | 0.0357 | -0.1532 |
| BTC | BTC_2024_5M | 400 | 24 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3866 | 0.1570 | 0.0427 | 0.0332 | -0.1537 |
| BTC | BTC_2024_5M | 200 | 49 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3742 | 0.1451 | 0.0442 | 0.0307 | -0.1542 |
| BTC | BTC_2024_5M | 100 | 97 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3595 | 0.1402 | 0.0411 | 0.0294 | -0.1487 |
| BTC | BTC_2024_5M | 200 | 29 | `normale_weltspannung->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3480 | 0.1256 | 0.0402 | 0.0257 | -0.1566 |
| DOGE | DOGE_2025_5M | 100 | 86 | `normale_weltspannung->lauter_feldkontakt` | `gemischte_rohwelt` | 0.2808 | 0.0457 | 0.0256 | 0.0101 | -0.1995 |
| DOGE | DOGE_2025_5M | 100 | 13 | `normale_weltspannung->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.2360 | 0.0641 | 0.0123 | 0.0123 | -0.1474 |
| DOGE | DOGE_2025_5M | 100 | 2 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.2047 | 0.0724 | 0.0229 | 0.0141 | -0.0954 |
| DOGE | DOGE_2025_5M | 200 | 6 | `normale_weltspannung->lauter_feldkontakt` | `gemischte_rohwelt` | 0.1928 | 0.0351 | 0.0070 | 0.0069 | -0.1438 |
| DOGE | DOGE_2025_5M | 200 | 1 | `lauter_feldkontakt->lauter_feldkontakt` | `bewegungsreiche_rohwelt` | 0.1927 | 0.0413 | 0.0244 | 0.0082 | -0.1187 |
| PAXG | PAXG_2024_5M | 200 | 49 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.2676 | 0.1669 | 0.0140 | 0.0368 | -0.0499 |
| PAXG | PAXG_2024_5M | 400 | 24 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.1939 | 0.1276 | 0.0063 | 0.0277 | -0.0323 |
| SOL | SOL_2026_STABLE | 100 | 28 | `normale_weltspannung->lauter_feldkontakt` | `gemischte_rohwelt` | 0.3558 | 0.0567 | 0.0345 | 0.0119 | -0.2526 |
| SOL | SOL_2026_STABLE | 100 | 71 | `normale_weltspannung->lauter_feldkontakt` | `gemischte_rohwelt` | 0.3546 | 0.0704 | 0.0261 | 0.0150 | -0.2431 |
| SOL | SOL_2023_NEG | 100 | 21 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3339 | 0.0944 | 0.0254 | 0.0198 | -0.1943 |
| SOL | SOL_2026_STABLE | 200 | 14 | `normale_weltspannung->normale_weltspannung` | `gemischte_rohwelt` | 0.3326 | 0.0422 | 0.0352 | 0.0074 | -0.2477 |
| SOL | SOL_2025_STRESS | 100 | 33 | `normale_weltspannung->lauter_feldkontakt` | `gemischte_rohwelt` | 0.3078 | 0.0605 | 0.0543 | 0.0112 | -0.1819 |
| SOL | SOL_2026_STABLE | 200 | 35 | `normale_weltspannung->normale_weltspannung` | `gemischte_rohwelt` | 0.3032 | 0.0324 | 0.0223 | 0.0074 | -0.2411 |
| SOL | SOL_2025_STRESS | 200 | 16 | `ruhig_zentrumsnah->normale_weltspannung` | `gemischte_rohwelt` | 0.2874 | 0.0459 | 0.0521 | 0.0080 | -0.1813 |
| SOL | SOL_2025_STRESS | 100 | 32 | `ruhig_zentrumsnah->normale_weltspannung` | `gemischte_rohwelt` | 0.2670 | 0.0313 | 0.0500 | 0.0049 | -0.1807 |
| XRP | XRP_2025_5M | 100 | 17 | `offen_suchend->lauter_feldkontakt` | `gemischte_rohwelt` | 0.3417 | 0.0589 | 0.0430 | 0.0105 | -0.2292 |
| XRP | XRP_2025_5M | 100 | 12 | `normale_weltspannung->lauter_feldkontakt` | `gemischte_rohwelt` | 0.2495 | 0.0592 | 0.0140 | 0.0125 | -0.1639 |
| XRP | XRP_2025_5M | 100 | 18 | `lauter_feldkontakt->lauter_feldkontakt` | `gemischte_rohwelt` | 0.2230 | 0.0411 | 0.0137 | 0.0087 | -0.1595 |
| XRP | XRP_2025_5M | 400 | 4 | `normale_weltspannung->lauter_feldkontakt` | `bewegungsreiche_rohwelt` | 0.1288 | 0.0397 | 0.0086 | 0.0082 | -0.0722 |

## Bewertung

Der hoerbare-schmale Shift wird hier nicht als feste Rolle gesetzt.

Wenn er assetrelativ in mehreren Assets erscheint, ist er eher eine wiederkehrende Mikrophase des Feldes. Wenn er nur bei BTC stabil bleibt, ist er eher BTC-spezifische Faerbung.

Wie es weitergeht: Als naechstes sollte die Kandidatenfamilie gegen neue, noch nicht verwendete Weltfenster gelesen werden. Erst dann ist entscheidbar, ob daraus eine reproduzierbare Mikrorolle oder nur lokale Oberflaechenvarianz entsteht.
