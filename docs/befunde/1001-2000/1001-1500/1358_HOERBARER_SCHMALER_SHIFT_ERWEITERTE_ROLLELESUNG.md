# Hoerbarer schmaler Shift - passive Rollenlesung

Diese Diagnose liest die komprimierte Sinnesphase aus `1350` gegen passive Feldrollen.

Wichtig: Die Rollen werden hier nicht als neue Mechanik gesetzt. Es ist eine Ruecklesung der Lagefolge:

```text
Welche Feldrolle wird durch diese Mikrophase nahegelegt?
```

Die Diagnose erzeugt keine Handlung, keine Richtung und kein Gate.

## Verdichtung

- gelesene Fenster: `41`
- komprimierte Sinnesphase: `27`
- Brueckennaehe: `10`
- Randnaehe: `11`
- Zentrumskontakt: `9`

Rollen:

- `randnaher_kontaktdruck`: `11`
- `brueckenuebergang_zum_lauten_kontakt`: `10`
- `zentrumskontakt_mit_hoeranstieg`: `7`
- `rueckbindung_in_normale_weltspannung`: `5`
- `lauter_kontakt_bleibt_offen`: `4`
- `zentrumskontakt_wird_aktiviert`: `2`
- `offener_uebergang_zum_lauten_kontakt`: `2`

Lagefolgen:

- `lauter_feldkontakt->lauter_feldkontakt`: `15`
- `normale_weltspannung->lauter_feldkontakt`: `9`
- `ruhig_zentrumsnah->lauter_feldkontakt`: `9`
- `offen_suchend->lauter_feldkontakt`: `2`
- `offen_suchend->normale_weltspannung`: `2`
- `ruhig_zentrumsnah->normale_weltspannung`: `1`
- `normale_weltspannung->normale_weltspannung`: `1`
- `lauter_feldkontakt->normale_weltspannung`: `1`
- `randlastige_sinneslage->lauter_feldkontakt`: `1`

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
| DOGE | DOGE_2024_5M_CONTRAST | 4900-5000 | `normale_weltspannung->lauter_feldkontakt` | `brueckenuebergang_zum_lauten_kontakt` | 1 | `gemischte_rohwelt` | 0.417213->0.478087->0.482805 | 0.104354->0.118493->0.119398 | 0.183874->0.125464->0.203511 |
| DOGE | DOGE_2024_5M | 4900-5000 | `normale_weltspannung->lauter_feldkontakt` | `brueckenuebergang_zum_lauten_kontakt` | 1 | `gemischte_rohwelt` | 0.417213->0.478087->0.482805 | 0.104354->0.118493->0.119398 | 0.183874->0.125464->0.203511 |
| BTC | BTC_2024_5M | 9600-10000 | `lauter_feldkontakt->lauter_feldkontakt` | `randnaher_kontaktdruck` | 1 | `laute_oder_druckvolle_rohwelt` | 0.521503->0.566509->0.0 | 0.126459->0.137849->0.0 | 0.063027->0.062225->0.0 |
| BTC | BTC_2024_5M | 9800-10000 | `lauter_feldkontakt->lauter_feldkontakt` | `randnaher_kontaktdruck` | 1 | `laute_oder_druckvolle_rohwelt` | 0.549736->0.554616->0.0 | 0.134037->0.135337->0.0 | 0.067147->0.061705->0.0 |
| BTC | BTC_2025_5M_CONTRAST | 1200-1300 | `lauter_feldkontakt->lauter_feldkontakt` | `randnaher_kontaktdruck` | 1 | `laute_oder_druckvolle_rohwelt` | 0.527->0.542439->0.49564 | 0.129141->0.131329->0.121586 | 0.068105->0.062296->0.106265 |
| BTC | BTC_2025_5M | 1200-1300 | `lauter_feldkontakt->lauter_feldkontakt` | `randnaher_kontaktdruck` | 1 | `laute_oder_druckvolle_rohwelt` | 0.527->0.542439->0.49564 | 0.129141->0.131329->0.121586 | 0.068105->0.062296->0.106265 |
| BTC | BTC_2024_5M | 9700-9800 | `lauter_feldkontakt->lauter_feldkontakt` | `randnaher_kontaktdruck` | 0 | `laute_oder_druckvolle_rohwelt` | 0.60707->0.549736->0.596644 | 0.146683->0.134037->0.1454 | 0.058343->0.067147->0.049782 |
| BTC | BTC_2025_5M_CONTRAST | 1100-1200 | `lauter_feldkontakt->lauter_feldkontakt` | `randnaher_kontaktdruck` | 1 | `laute_oder_druckvolle_rohwelt` | 0.497594->0.527->0.542439 | 0.121577->0.129141->0.131329 | 0.083727->0.068105->0.062296 |
| XRP | XRP_2024_5M_CONTRAST | 5500-5600 | `lauter_feldkontakt->lauter_feldkontakt` | `lauter_kontakt_bleibt_offen` | 1 | `gemischte_rohwelt` | 0.460506->0.46924->0.440065 | 0.115887->0.116231->0.111524 | 0.199552->0.152257->0.155877 |
| XRP | XRP_2024_5M_CONTRAST | 9200-9300 | `offen_suchend->lauter_feldkontakt` | `brueckenuebergang_zum_lauten_kontakt` | 1 | `gemischte_rohwelt` | 0.430852->0.472458->0.448609 | 0.109616->0.115368->0.112911 | 0.210707->0.137057->0.193039 |
| XRP | XRP_2024_5M_CONTRAST | 5700-5800 | `normale_weltspannung->lauter_feldkontakt` | `brueckenuebergang_zum_lauten_kontakt` | 1 | `gemischte_rohwelt` | 0.440065->0.470208->0.421527 | 0.111524->0.116888->0.104664 | 0.155877->0.14427->0.096048 |
| SOL | SOL_2023_POS_EXP | 2700-2800 | `ruhig_zentrumsnah->lauter_feldkontakt` | `zentrumskontakt_wird_aktiviert` | 1 | `gemischte_rohwelt` | 0.412725->0.474465->0.445046 | 0.103869->0.119139->0.111379 | 0.156128->0.142896->0.192159 |
| DOGE | DOGE_2024_5M_CONTRAST | 7700-7800 | `ruhig_zentrumsnah->lauter_feldkontakt` | `zentrumskontakt_mit_hoeranstieg` | 0 | `gemischte_rohwelt` | 0.380721->0.476478->0.43287 | 0.095969->0.118026->0.109327 | 0.117354->0.162303->0.170145 |
| DOGE | DOGE_2024_5M | 7700-7800 | `ruhig_zentrumsnah->lauter_feldkontakt` | `zentrumskontakt_mit_hoeranstieg` | 0 | `gemischte_rohwelt` | 0.380721->0.476478->0.43287 | 0.095969->0.118026->0.109327 | 0.117354->0.162303->0.170145 |
| SOL | SOL_2023_NEG_STRESS | 2100-2200 | `lauter_feldkontakt->lauter_feldkontakt` | `randnaher_kontaktdruck` | 1 | `laute_oder_druckvolle_rohwelt` | 0.470049->0.510955->0.440786 | 0.116286->0.125712->0.111145 | 0.247424->0.174351->0.330714 |
| XRP | XRP_2024_5M_CONTRAST | 5000-5100 | `normale_weltspannung->lauter_feldkontakt` | `offener_uebergang_zum_lauten_kontakt` | 0 | `gemischte_rohwelt` | 0.451107->0.462556->0.427474 | 0.110881->0.115868->0.108313 | 0.118253->0.159591->0.235493 |
| SOL | SOL_2023_ALT_A_FOLLOW | 2200-2300 | `normale_weltspannung->lauter_feldkontakt` | `brueckenuebergang_zum_lauten_kontakt` | 1 | `laute_oder_druckvolle_rohwelt` | 0.387923->0.531606->0.467813 | 0.099374->0.129368->0.11632 | 0.261434->0.208557->0.244543 |
| DOGE | DOGE_2024_5M_CONTRAST | 5000-5100 | `lauter_feldkontakt->lauter_feldkontakt` | `lauter_kontakt_bleibt_offen` | 0 | `gemischte_rohwelt` | 0.478087->0.482805->0.481586 | 0.118493->0.119398->0.120434 | 0.125464->0.203511->0.282565 |
| DOGE | DOGE_2024_5M | 5000-5100 | `lauter_feldkontakt->lauter_feldkontakt` | `lauter_kontakt_bleibt_offen` | 0 | `gemischte_rohwelt` | 0.478087->0.482805->0.481586 | 0.118493->0.119398->0.120434 | 0.125464->0.203511->0.282565 |
| SOL | SOL_2025_REC | 1300-1400 | `ruhig_zentrumsnah->lauter_feldkontakt` | `zentrumskontakt_wird_aktiviert` | 1 | `bewegungsreiche_rohwelt` | 0.402707->0.477867->0.487822 | 0.100827->0.116913->0.120965 | 0.218376->0.179161->0.244797 |
| SOL | SOL_2025_ALT_A_FOLLOW | 3200-3300 | `ruhig_zentrumsnah->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 1 | `gemischte_rohwelt` | 0.387999->0.45799->0.409289 | 0.09695->0.111747->0.1028 | 0.15689->0.144339->0.186825 |
| SOL | SOL_2025_STRESS | 3300-3400 | `normale_weltspannung->lauter_feldkontakt` | `brueckenuebergang_zum_lauten_kontakt` | 1 | `gemischte_rohwelt` | 0.447904->0.477061->0.4792 | 0.110772->0.117016->0.119275 | 0.187897->0.186763->0.259269 |
| SOL | SOL_2025_REC | 4200-4300 | `normale_weltspannung->lauter_feldkontakt` | `brueckenuebergang_zum_lauten_kontakt` | 1 | `gemischte_rohwelt` | 0.430077->0.479236->0.397609 | 0.106879->0.118109->0.101147 | 0.214075->0.16294->0.236782 |
| XRP | XRP_2024_5M_CONTRAST | 5400-5600 | `lauter_feldkontakt->lauter_feldkontakt` | `lauter_kontakt_bleibt_offen` | 0 | `gemischte_rohwelt` | 0.468302->0.464873->0.440065 | 0.116606->0.116059->0.111524 | 0.285469->0.175905->0.155877 |
| SOL | SOL_2025_REC | 3400-3500 | `normale_weltspannung->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 1 | `gemischte_rohwelt` | 0.446872->0.45214->0.4078 | 0.111358->0.111922->0.100037 | 0.150636->0.150307->0.120477 |
| SOL | SOL_2025_REC | 3200-3600 | `offen_suchend->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 1 | `gemischte_rohwelt` | 0.395253->0.449009->0.46586 | 0.100708->0.111085->0.114041 | 0.266431->0.151857->0.117548 |
| SOL | SOL_2025_REC | 3300-3400 | `lauter_feldkontakt->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 0 | `gemischte_rohwelt` | 0.489222->0.446872->0.45214 | 0.121022->0.111358->0.111922 | 0.186008->0.150636->0.150307 |
| XRP | XRP_2024_5M_CONTRAST | 9700-9800 | `offen_suchend->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 1 | `gemischte_rohwelt` | 0.440753->0.461316->0.424248 | 0.112189->0.114867->0.107331 | 0.292849->0.175028->0.140524 |
| XRP | XRP_2024_5M_CONTRAST | 5200-5600 | `randlastige_sinneslage->lauter_feldkontakt` | `brueckenuebergang_zum_lauten_kontakt` | 1 | `gemischte_rohwelt` | 0.427474->0.463631->0.440065 | 0.108313->0.11564->0.111524 | 0.235493->0.199337->0.155877 |
| PAXG | PAXG_2024_5M | 9800-10000 | `lauter_feldkontakt->lauter_feldkontakt` | `randnaher_kontaktdruck` | 1 | `laute_oder_druckvolle_rohwelt` | 0.497304->0.586549->0.0 | 0.126509->0.146238->0.0 | 0.061332->0.031926->0.0 |
| XRP | XRP_2025_5M | 1200-1300 | `normale_weltspannung->lauter_feldkontakt` | `offener_uebergang_zum_lauten_kontakt` | 0 | `gemischte_rohwelt` | 0.452906->0.489282->0.429383 | 0.111705->0.120445->0.107013 | 0.228454->0.26135->0.272862 |
| XRP | XRP_2024_5M_CONTRAST | 5200-5400 | `offen_suchend->lauter_feldkontakt` | `brueckenuebergang_zum_lauten_kontakt` | 1 | `gemischte_rohwelt` | 0.427474->0.462389->0.460506 | 0.108313->0.115221->0.115887 | 0.235493->0.22277->0.199552 |

## Bewertung

Die komprimierte Sinnesphase faellt nicht in eine einzige Rolle.

Sie erscheint vor allem als Uebergang in lauteren Kontakt, als randnaher Kontaktdruck und als Aktivierung aus zentrumsnaher Ruhe.

Damit wirkt sie eher wie eine lokale Feldfunktion: Sie kann Bruecke, Randnaehe oder aktivierten Zentrumskontakt tragen, je nachdem aus welcher Lagefolge sie entsteht.

Wie es weitergeht: Als naechstes sollte diese Rollenlesung gegen das bestehende Bedeutungsnetz gelesen werden: Welche `dio_*`-Familien liegen in Fenstern mit `brueckenuebergang_zum_lauten_kontakt`, und bleiben sie in Folgefenstern stabil oder driften sie?
