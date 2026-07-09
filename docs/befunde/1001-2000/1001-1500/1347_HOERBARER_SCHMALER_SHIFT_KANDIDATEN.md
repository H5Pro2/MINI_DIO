# Hoerbarer schmaler Folgeschift - Kandidatenfenster

Diese Diagnose sucht Fenster, die das Rohprofil des bisher einzelnen `hoerbarer_schmaler_folgeschift` tragen.

Gesucht wurde passiv nach:

- Hoeren steigt gegenueber BTC-Basis deutlich
- Sicht steigt gegenueber BTC-Basis
- Felddruck steigt gegenueber BTC-Basis
- Range sinkt gegenueber BTC-Basis

Die Diagnose erzeugt keine Handlung, keine Richtung und kein Gate.

## BTC-Basis

- Hoeren: `0.409494`
- Sicht: `0.648058`
- Felddruck: `0.104631`
- Range: `0.215895`

## Verdichtung

- Kandidatenfenster: `95`

Sequenzen:

- `lauter_feldkontakt->lauter_feldkontakt`: `26`
- `normale_weltspannung->normale_weltspannung`: `26`
- `randlastige_sinneslage->lauter_feldkontakt`: `9`
- `lauter_feldkontakt->normale_weltspannung`: `8`
- `ruhig_zentrumsnah->normale_weltspannung`: `7`
- `offen_suchend->normale_weltspannung`: `6`
- `randlastige_sinneslage->normale_weltspannung`: `6`
- `ruhig_zentrumsnah->lauter_feldkontakt`: `4`
- `leise_duenn->normale_weltspannung`: `1`
- `offen_suchend->offen_suchend`: `1`
- `randlastige_sinneslage->offen_suchend`: `1`

Welten:

- `BTC_2025_5M_FULL`: `28`
- `BTC_2024_5M_FULL`: `24`
- `BTC_2024_5M_STRESS`: `10`
- `BTC_2024_5M_QUIET`: `8`
- `BTC_2025_5M_QUIET`: `8`
- `BTC_2025_5M_STRESS`: `6`
- `BTC_2025_5M_TEST`: `6`
- `BTC_2025_BREAK`: `3`
- `BTC_2024_5M_TEST`: `2`

Rohklassen:

- `gemischte_rohwelt`: `72`
- `laute_oder_druckvolle_rohwelt`: `21`
- `bewegungsreiche_rohwelt`: `2`

## Staerkste Fenster

| Welt | Skala | Block | Sequenz | Rohklasse | Score | dHoeren | dSicht | dDruck | dRange |
|---|---:|---:|---|---|---:|---:|---:|---:|---:|
| BTC_2025_5M_QUIET | 200 | 5 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.4717 | 0.1779 | 0.0681 | 0.0367 | -0.1890 |
| BTC_2024_5M_FULL | 100 | 96 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.4385 | 0.1976 | 0.0413 | 0.0421 | -0.1576 |
| BTC_2024_5M_FULL | 100 | 98 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.4363 | 0.1872 | 0.0423 | 0.0408 | -0.1661 |
| BTC_2025_5M_QUIET | 100 | 31 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.4193 | 0.1382 | 0.0654 | 0.0286 | -0.1871 |
| BTC_2025_5M_QUIET | 100 | 11 | `randlastige_sinneslage->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.4113 | 0.1292 | 0.0655 | 0.0252 | -0.1914 |
| BTC_2024_5M_FULL | 200 | 48 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3990 | 0.1689 | 0.0412 | 0.0357 | -0.1532 |
| BTC_2024_5M_FULL | 400 | 24 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3866 | 0.1570 | 0.0427 | 0.0332 | -0.1537 |
| BTC_2024_5M_FULL | 200 | 49 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3742 | 0.1451 | 0.0442 | 0.0307 | -0.1542 |
| BTC_2025_5M_FULL | 100 | 12 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3602 | 0.1329 | 0.0469 | 0.0267 | -0.1536 |
| BTC_2024_5M_FULL | 100 | 97 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3595 | 0.1402 | 0.0411 | 0.0294 | -0.1487 |
| BTC_2025_5M_FULL | 100 | 11 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3499 | 0.1175 | 0.0600 | 0.0245 | -0.1478 |
| BTC_2024_5M_QUIET | 100 | 33 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3267 | 0.0915 | 0.0485 | 0.0191 | -0.1676 |
| BTC_2024_5M_QUIET | 200 | 16 | `randlastige_sinneslage->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3195 | 0.0938 | 0.0394 | 0.0193 | -0.1669 |
| BTC_2025_5M_FULL | 200 | 5 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3194 | 0.1028 | 0.0558 | 0.0207 | -0.1400 |
| BTC_2024_5M_QUIET | 100 | 32 | `randlastige_sinneslage->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3123 | 0.0962 | 0.0304 | 0.0195 | -0.1663 |
| BTC_2024_5M_FULL | 100 | 99 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.3121 | 0.1031 | 0.0461 | 0.0206 | -0.1423 |
| BTC_2025_5M_QUIET | 100 | 30 | `lauter_feldkontakt->lauter_feldkontakt` | `gemischte_rohwelt` | 0.2987 | 0.0602 | 0.0472 | 0.0118 | -0.1794 |
| BTC_2025_5M_TEST | 100 | 12 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.2954 | 0.0914 | 0.0329 | 0.0176 | -0.1536 |
| BTC_2025_5M_FULL | 100 | 10 | `lauter_feldkontakt->lauter_feldkontakt` | `gemischte_rohwelt` | 0.2889 | 0.0881 | 0.0516 | 0.0169 | -0.1322 |
| BTC_2024_5M_STRESS | 100 | 3 | `lauter_feldkontakt->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.2843 | 0.1115 | 0.0448 | 0.0229 | -0.1050 |
| BTC_2024_5M_FULL | 100 | 77 | `ruhig_zentrumsnah->lauter_feldkontakt` | `gemischte_rohwelt` | 0.2656 | 0.0824 | 0.0362 | 0.0174 | -0.1296 |
| BTC_2024_5M_QUIET | 100 | 13 | `randlastige_sinneslage->lauter_feldkontakt` | `gemischte_rohwelt` | 0.2636 | 0.0569 | 0.0512 | 0.0100 | -0.1456 |
| BTC_2025_5M_QUIET | 400 | 3 | `lauter_feldkontakt->lauter_feldkontakt` | `gemischte_rohwelt` | 0.2575 | 0.0612 | 0.0306 | 0.0134 | -0.1523 |
| BTC_2024_5M_STRESS | 200 | 1 | `randlastige_sinneslage->lauter_feldkontakt` | `laute_oder_druckvolle_rohwelt` | 0.2562 | 0.0929 | 0.0430 | 0.0187 | -0.1016 |
| BTC_2025_5M_FULL | 100 | 71 | `lauter_feldkontakt->lauter_feldkontakt` | `gemischte_rohwelt` | 0.2539 | 0.0759 | 0.0418 | 0.0144 | -0.1218 |

## Bewertung

Der starke hoerbare-schmale Shift ist als Mikrofenster mehrfach vorhanden.

Er wird aber in breiten Weltgruppen nicht automatisch zur dominanten Assetfaerbung. Das spricht dafuer, dass diese Sonderrolle lokal und phasenabhaengig ist.

Wichtig ist die Trennung:

- als Mikrofenster: klar vorhanden
- als ganze Weltfaerbung: bisher nicht stabil reproduziert
