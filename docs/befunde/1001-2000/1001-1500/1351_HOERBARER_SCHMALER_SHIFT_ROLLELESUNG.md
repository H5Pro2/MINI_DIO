# Hoerbarer schmaler Shift - passive Rollenlesung

Diese Diagnose liest die komprimierte Sinnesphase aus `1350` gegen passive Feldrollen.

Wichtig: Die Rollen werden hier nicht als neue Mechanik gesetzt. Es ist eine Ruecklesung der Lagefolge:

```text
Welche Feldrolle wird durch diese Mikrophase nahegelegt?
```

Die Diagnose erzeugt keine Handlung, keine Richtung und kein Gate.

## Verdichtung

- gelesene Fenster: `17`
- komprimierte Sinnesphase: `12`
- Brueckennaehe: `4`
- Randnaehe: `5`
- Zentrumskontakt: `7`

Rollen:

- `zentrumskontakt_mit_hoeranstieg`: `5`
- `randnaher_kontaktdruck`: `5`
- `brueckenuebergang_zum_lauten_kontakt`: `4`
- `zentrumskontakt_wird_aktiviert`: `2`
- `lauter_kontakt_bleibt_offen`: `1`

Lagefolgen:

- `ruhig_zentrumsnah->lauter_feldkontakt`: `7`
- `lauter_feldkontakt->lauter_feldkontakt`: `6`
- `normale_weltspannung->lauter_feldkontakt`: `3`
- `offen_suchend->lauter_feldkontakt`: `1`

## Fenster

| Asset | Welt | Ticks | Lagefolge | passive Rolle | kompakt | Klasse | Hoeren | Druck | Range |
|---|---|---:|---|---|---:|---|---|---|---|
| BTC | BTC_2024_5M | 5800-5900 | `normale_weltspannung->lauter_feldkontakt` | `brueckenuebergang_zum_lauten_kontakt` | 1 | `laute_oder_druckvolle_rohwelt` | 0.453687->0.609422->0.460735 | 0.113814->0.145789->0.114815 | 0.075637->0.043024->0.075657 |
| DOGE | DOGE_2024_5M_CONTRAST | 9600-9700 | `ruhig_zentrumsnah->lauter_feldkontakt` | `zentrumskontakt_mit_hoeranstieg` | 0 | `gemischte_rohwelt` | 0.438809->0.482978->0.465979 | 0.108772->0.119291->0.115878 | 0.089584->0.093699->0.097535 |
| DOGE | DOGE_2024_5M | 9600-9700 | `ruhig_zentrumsnah->lauter_feldkontakt` | `zentrumskontakt_mit_hoeranstieg` | 0 | `gemischte_rohwelt` | 0.438809->0.482978->0.465979 | 0.108772->0.119291->0.115878 | 0.089584->0.093699->0.097535 |
| BTC | BTC_2024_5M | 9600-9700 | `lauter_feldkontakt->lauter_feldkontakt` | `randnaher_kontaktdruck` | 1 | `laute_oder_druckvolle_rohwelt` | 0.521503->0.60707->0.549736 | 0.126459->0.146683->0.134037 | 0.063027->0.058343->0.067147 |
| BTC | BTC_2024_5M | 9800-9900 | `lauter_feldkontakt->lauter_feldkontakt` | `randnaher_kontaktdruck` | 1 | `laute_oder_druckvolle_rohwelt` | 0.549736->0.596644->0.512588 | 0.134037->0.1454->0.125275 | 0.067147->0.049782->0.073628 |
| DOGE | DOGE_2024_5M_CONTRAST | 9600-9800 | `ruhig_zentrumsnah->lauter_feldkontakt` | `zentrumskontakt_mit_hoeranstieg` | 0 | `gemischte_rohwelt` | 0.438809->0.474478->0.45086 | 0.108772->0.117584->0.113875 | 0.089584->0.095617->0.097525 |
| DOGE | DOGE_2024_5M | 9600-9800 | `ruhig_zentrumsnah->lauter_feldkontakt` | `zentrumskontakt_mit_hoeranstieg` | 0 | `gemischte_rohwelt` | 0.438809->0.474478->0.45086 | 0.108772->0.117584->0.113875 | 0.089584->0.095617->0.097525 |
| XRP | XRP_2024_5M_CONTRAST | 7800-7900 | `ruhig_zentrumsnah->lauter_feldkontakt` | `zentrumskontakt_mit_hoeranstieg` | 0 | `gemischte_rohwelt` | 0.372604->0.47363->0.418974 | 0.095372->0.118298->0.106775 | 0.091274->0.100905->0.127401 |
| BTC | BTC_2024_5M | 9600-9800 | `lauter_feldkontakt->lauter_feldkontakt` | `randnaher_kontaktdruck` | 1 | `laute_oder_druckvolle_rohwelt` | 0.521503->0.578403->0.596644 | 0.126459->0.14036->0.1454 | 0.063027->0.062745->0.049782 |
| XRP | XRP_2024_5M_CONTRAST | 5500-5600 | `lauter_feldkontakt->lauter_feldkontakt` | `lauter_kontakt_bleibt_offen` | 1 | `gemischte_rohwelt` | 0.460506->0.46924->0.440065 | 0.115887->0.116231->0.111524 | 0.199552->0.152257->0.155877 |
| XRP | XRP_2024_5M_CONTRAST | 9200-9300 | `offen_suchend->lauter_feldkontakt` | `brueckenuebergang_zum_lauten_kontakt` | 1 | `gemischte_rohwelt` | 0.430852->0.472458->0.448609 | 0.109616->0.115368->0.112911 | 0.210707->0.137057->0.193039 |
| XRP | XRP_2024_5M_CONTRAST | 5700-5800 | `normale_weltspannung->lauter_feldkontakt` | `brueckenuebergang_zum_lauten_kontakt` | 1 | `gemischte_rohwelt` | 0.440065->0.470208->0.421527 | 0.111524->0.116888->0.104664 | 0.155877->0.14427->0.096048 |
| SOL | SOL_2023_POS_EXP | 2700-2800 | `ruhig_zentrumsnah->lauter_feldkontakt` | `zentrumskontakt_wird_aktiviert` | 1 | `gemischte_rohwelt` | 0.412725->0.474465->0.445046 | 0.103869->0.119139->0.111379 | 0.156128->0.142896->0.192159 |
| SOL | SOL_2023_NEG_STRESS | 2100-2200 | `lauter_feldkontakt->lauter_feldkontakt` | `randnaher_kontaktdruck` | 1 | `laute_oder_druckvolle_rohwelt` | 0.470049->0.510955->0.440786 | 0.116286->0.125712->0.111145 | 0.247424->0.174351->0.330714 |
| SOL | SOL_2023_ALT_A_FOLLOW | 2200-2300 | `normale_weltspannung->lauter_feldkontakt` | `brueckenuebergang_zum_lauten_kontakt` | 1 | `laute_oder_druckvolle_rohwelt` | 0.387923->0.531606->0.467813 | 0.099374->0.129368->0.11632 | 0.261434->0.208557->0.244543 |
| SOL | SOL_2025_REC | 1300-1400 | `ruhig_zentrumsnah->lauter_feldkontakt` | `zentrumskontakt_wird_aktiviert` | 1 | `bewegungsreiche_rohwelt` | 0.402707->0.477867->0.487822 | 0.100827->0.116913->0.120965 | 0.218376->0.179161->0.244797 |
| PAXG | PAXG_2024_5M | 9800-10000 | `lauter_feldkontakt->lauter_feldkontakt` | `randnaher_kontaktdruck` | 1 | `laute_oder_druckvolle_rohwelt` | 0.497304->0.586549->0.0 | 0.126509->0.146238->0.0 | 0.061332->0.031926->0.0 |

## Bewertung

Die komprimierte Sinnesphase faellt nicht in eine einzige Rolle.

Sie erscheint vor allem als Uebergang in lauteren Kontakt, als randnaher Kontaktdruck und als Aktivierung aus zentrumsnaher Ruhe.

Damit wirkt sie eher wie eine lokale Feldfunktion: Sie kann Bruecke, Randnaehe oder aktivierten Zentrumskontakt tragen, je nachdem aus welcher Lagefolge sie entsteht.
