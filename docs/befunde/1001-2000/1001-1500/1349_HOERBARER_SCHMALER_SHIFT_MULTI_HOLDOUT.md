# Hoerbarer schmaler Shift - Multi-Holdout

Diese Diagnose prueft den hoerbaren-schmale Mikrofenster-Shift gegen mehrere unabhaengige Rohweltfenster-Gruppen.

Jede Gruppe wird assetrelativ gelesen. Dadurch bleibt die Pruefung passiv und vergleicht keine absoluten Preisgroessen.

## Gruppen

- `CONTRAST`: `125` Kandidatenfenster
- `HOLDOUT1`: `72` Kandidatenfenster
- `HOLDOUT2`: `102` Kandidatenfenster

## Gesamtverdichtung

- Kandidatenfenster gesamt: `299`

Assets:

- `SOL`: `157`
- `BTC`: `105`
- `DOGE`: `19`
- `XRP`: `13`
- `PAXG`: `5`

Sequenzen:

- `normale_weltspannung->lauter_feldkontakt`: `78`
- `lauter_feldkontakt->lauter_feldkontakt`: `51`
- `normale_weltspannung->normale_weltspannung`: `50`
- `ruhig_zentrumsnah->lauter_feldkontakt`: `25`
- `lauter_feldkontakt->normale_weltspannung`: `19`
- `ruhig_zentrumsnah->normale_weltspannung`: `18`
- `offen_suchend->normale_weltspannung`: `13`
- `normale_weltspannung->offen_suchend`: `10`
- `randlastige_sinneslage->normale_weltspannung`: `10`
- `randlastige_sinneslage->lauter_feldkontakt`: `9`
- `offen_suchend->lauter_feldkontakt`: `6`
- `offen_suchend->offen_suchend`: `5`

Rohklassen:

- `gemischte_rohwelt`: `241`
- `bewegungsreiche_rohwelt`: `30`
- `laute_oder_druckvolle_rohwelt`: `28`

## Staerkste Fenster

| Gruppe | Asset | Welt | Skala | Block | Sequenz | Rohklasse | Score | dHoeren | dSicht | dDruck | dRange |
|---|---|---|---:|---:|---|---|---:|---:|---:|---:|---:|
| HOLDOUT2 | BTC | BTC_2024_5M | 100 | 58 | `normale_weltspannung->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.4598 | 0.1999 | 0.0458 | 0.0412 | -0.1729 |
| CONTRAST | DOGE | DOGE_2024_5M_CONTRAST | 100 | 96 | `ruhig_zentrumsnah->lauter_feldkontakt` | `gemischte_rohwelt` | 0.4462 | 0.0457 | 0.0525 | 0.0096 | -0.3383 |
| HOLDOUT1 | DOGE | DOGE_2024_5M | 100 | 96 | `ruhig_zentrumsnah->lauter_feldkontakt` | `gemischte_rohwelt` | 0.4462 | 0.0457 | 0.0525 | 0.0096 | -0.3383 |
| HOLDOUT2 | BTC | BTC_2024_5M | 100 | 96 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.4385 | 0.1976 | 0.0413 | 0.0421 | -0.1576 |
| HOLDOUT2 | BTC | BTC_2024_5M | 100 | 98 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.4363 | 0.1872 | 0.0423 | 0.0408 | -0.1661 |
| CONTRAST | DOGE | DOGE_2024_5M_CONTRAST | 200 | 48 | `ruhig_zentrumsnah->lauter_feldkontakt` | `gemischte_rohwelt` | 0.4263 | 0.0372 | 0.0448 | 0.0079 | -0.3364 |
| HOLDOUT1 | DOGE | DOGE_2024_5M | 200 | 48 | `ruhig_zentrumsnah->lauter_feldkontakt` | `gemischte_rohwelt` | 0.4263 | 0.0372 | 0.0448 | 0.0079 | -0.3364 |
| CONTRAST | XRP | XRP_2024_5M_CONTRAST | 100 | 78 | `ruhig_zentrumsnah->lauter_feldkontakt` | `gemischte_rohwelt` | 0.4092 | 0.0435 | 0.0311 | 0.0103 | -0.3243 |
| HOLDOUT2 | BTC | BTC_2024_5M | 200 | 48 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3990 | 0.1689 | 0.0412 | 0.0357 | -0.1532 |
| CONTRAST | DOGE | DOGE_2024_5M_CONTRAST | 100 | 49 | `normale_weltspannung->lauter_feldkontakt` | `gemischte_rohwelt` | 0.3886 | 0.0409 | 0.0324 | 0.0088 | -0.3065 |
| HOLDOUT1 | DOGE | DOGE_2024_5M | 100 | 49 | `normale_weltspannung->lauter_feldkontakt` | `gemischte_rohwelt` | 0.3886 | 0.0409 | 0.0324 | 0.0088 | -0.3065 |
| HOLDOUT2 | BTC | BTC_2024_5M | 400 | 24 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3866 | 0.1570 | 0.0427 | 0.0332 | -0.1537 |
| HOLDOUT2 | BTC | BTC_2024_5M | 200 | 49 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3742 | 0.1451 | 0.0442 | 0.0307 | -0.1542 |
| CONTRAST | BTC | BTC_2025_5M_CONTRAST | 100 | 12 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3602 | 0.1329 | 0.0469 | 0.0267 | -0.1536 |
| HOLDOUT1 | BTC | BTC_2025_5M | 100 | 12 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3602 | 0.1329 | 0.0469 | 0.0267 | -0.1536 |
| HOLDOUT2 | BTC | BTC_2024_5M | 100 | 97 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3595 | 0.1402 | 0.0411 | 0.0294 | -0.1487 |
| CONTRAST | BTC | BTC_2025_5M_CONTRAST | 100 | 11 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3499 | 0.1175 | 0.0600 | 0.0245 | -0.1478 |
| HOLDOUT1 | BTC | BTC_2025_5M | 100 | 11 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3499 | 0.1175 | 0.0600 | 0.0245 | -0.1478 |
| HOLDOUT2 | BTC | BTC_2024_5M | 200 | 29 | `normale_weltspannung->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3480 | 0.1256 | 0.0402 | 0.0257 | -0.1566 |
| CONTRAST | XRP | XRP_2024_5M_CONTRAST | 100 | 55 | `lauter_feldkontakt->lauter_feldkontakt` | `gemischte_rohwelt` | 0.3459 | 0.0391 | 0.0255 | 0.0082 | -0.2730 |
| CONTRAST | XRP | XRP_2024_5M_CONTRAST | 100 | 92 | `offen_suchend->lauter_feldkontakt` | `gemischte_rohwelt` | 0.3395 | 0.0424 | 0.0016 | 0.0074 | -0.2882 |
| CONTRAST | XRP | XRP_2024_5M_CONTRAST | 100 | 57 | `normale_weltspannung->lauter_feldkontakt` | `gemischte_rohwelt` | 0.3378 | 0.0401 | 0.0078 | 0.0089 | -0.2810 |
| CONTRAST | SOL | SOL_2023_POS_EXP | 100 | 27 | `ruhig_zentrumsnah->lauter_feldkontakt` | `gemischte_rohwelt` | 0.3361 | 0.0579 | 0.0392 | 0.0133 | -0.2257 |
| CONTRAST | DOGE | DOGE_2024_5M_CONTRAST | 100 | 77 | `ruhig_zentrumsnah->lauter_feldkontakt` | `gemischte_rohwelt` | 0.3352 | 0.0392 | 0.0179 | 0.0083 | -0.2697 |
| HOLDOUT1 | DOGE | DOGE_2024_5M | 100 | 77 | `ruhig_zentrumsnah->lauter_feldkontakt` | `gemischte_rohwelt` | 0.3352 | 0.0392 | 0.0179 | 0.0083 | -0.2697 |
| CONTRAST | SOL | SOL_2023_NEG_STRESS | 100 | 21 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3339 | 0.0944 | 0.0254 | 0.0198 | -0.1943 |
| CONTRAST | XRP | XRP_2024_5M_CONTRAST | 100 | 50 | `normale_weltspannung->lauter_feldkontakt` | `gemischte_rohwelt` | 0.3328 | 0.0325 | 0.0268 | 0.0079 | -0.2656 |
| HOLDOUT2 | BTC | BTC_2024_5M | 100 | 95 | `normale_weltspannung->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3258 | 0.1120 | 0.0391 | 0.0218 | -0.1529 |
| HOLDOUT2 | SOL | SOL_2023_ALT_A_FOLLOW | 100 | 22 | `normale_weltspannung->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3255 | 0.1151 | 0.0269 | 0.0235 | -0.1601 |
| CONTRAST | BTC | BTC_2025_5M_CONTRAST | 200 | 5 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3194 | 0.1028 | 0.0558 | 0.0207 | -0.1400 |

## Bewertung

Der hoerbare-schmale Shift erscheint in mehreren Kontrollgruppen erneut.

Damit ist er nicht nur ein einzelner BTC-Fund aus `1342`, sondern eine wiederkehrende lokale Mikrophase. Gleichzeitig bleibt er lokal: Die breite Weltfaerbung wird dadurch nicht automatisch ersetzt.

Fachliche Grenze:

- bestaetigt als wiederkehrendes Mikrofensterprofil
- noch nicht bestaetigt als eigenstaendige stabile Topologierolle
