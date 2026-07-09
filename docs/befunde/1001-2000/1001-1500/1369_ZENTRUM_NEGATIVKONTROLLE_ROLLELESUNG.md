# Hoerbarer schmaler Shift - passive Rollenlesung

Diese Diagnose liest die komprimierte Sinnesphase aus `1350` gegen passive Feldrollen.

Wichtig: Die Rollen werden hier nicht als neue Mechanik gesetzt. Es ist eine Ruecklesung der Lagefolge:

```text
Welche Feldrolle wird durch diese Mikrophase nahegelegt?
```

Die Diagnose erzeugt keine Handlung, keine Richtung und kein Gate.

## Verdichtung

- gelesene Fenster: `19`
- komprimierte Sinnesphase: `13`
- Brueckennaehe: `7`
- Randnaehe: `0`
- Zentrumskontakt: `0`

Rollen:

- `brueckenuebergang_zum_lauten_kontakt`: `7`
- `rueckbindung_in_normale_weltspannung`: `7`
- `offener_uebergang_zum_lauten_kontakt`: `4`
- `lauter_kontakt_bleibt_offen`: `1`

Lagefolgen:

- `normale_weltspannung->lauter_feldkontakt`: `9`
- `ruhig_zentrumsnah->normale_weltspannung`: `7`
- `offen_suchend->lauter_feldkontakt`: `1`
- `randlastige_sinneslage->lauter_feldkontakt`: `1`
- `lauter_feldkontakt->lauter_feldkontakt`: `1`

## Fenster

| Asset | Welt | Ticks | Lagefolge | passive Rolle | kompakt | Klasse | Hoeren | Druck | Range |
|---|---|---:|---|---|---:|---|---|---|---|
| DOGE | DOGE_2024_5M_CONTRAST | 4900-5000 | `normale_weltspannung->lauter_feldkontakt` | `brueckenuebergang_zum_lauten_kontakt` | 1 | `gemischte_rohwelt` | 0.417213->0.478087->0.482805 | 0.104354->0.118493->0.119398 | 0.183874->0.125464->0.203511 |
| DOGE | DOGE_2024_5M | 4900-5000 | `normale_weltspannung->lauter_feldkontakt` | `brueckenuebergang_zum_lauten_kontakt` | 1 | `gemischte_rohwelt` | 0.417213->0.478087->0.482805 | 0.104354->0.118493->0.119398 | 0.183874->0.125464->0.203511 |
| XRP | XRP_2024_5M_CONTRAST | 9200-9300 | `offen_suchend->lauter_feldkontakt` | `brueckenuebergang_zum_lauten_kontakt` | 1 | `gemischte_rohwelt` | 0.430852->0.472458->0.448609 | 0.109616->0.115368->0.112911 | 0.210707->0.137057->0.193039 |
| XRP | XRP_2024_5M_CONTRAST | 5700-5800 | `normale_weltspannung->lauter_feldkontakt` | `brueckenuebergang_zum_lauten_kontakt` | 1 | `gemischte_rohwelt` | 0.440065->0.470208->0.421527 | 0.111524->0.116888->0.104664 | 0.155877->0.14427->0.096048 |
| SOL | SOL_2025_REC | 4200-4300 | `normale_weltspannung->lauter_feldkontakt` | `brueckenuebergang_zum_lauten_kontakt` | 1 | `gemischte_rohwelt` | 0.430077->0.479236->0.397609 | 0.106879->0.118109->0.101147 | 0.214075->0.16294->0.236782 |
| SOL | SOL_2025_STRESS | 3200-3400 | `ruhig_zentrumsnah->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 1 | `gemischte_rohwelt` | 0.384591->0.462482->0.4792 | 0.096079->0.113894->0.119275 | 0.216043->0.18733->0.259269 |
| SOL | SOL_2025_STRESS | 3200-3300 | `ruhig_zentrumsnah->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 1 | `gemischte_rohwelt` | 0.384591->0.447904->0.477061 | 0.096079->0.110772->0.117016 | 0.216043->0.187897->0.186763 |
| BTC | BTC_2024_5M | 9400-9600 | `normale_weltspannung->lauter_feldkontakt` | `offener_uebergang_zum_lauten_kontakt` | 0 | `gemischte_rohwelt` | 0.481308->0.476696->0.60707 | 0.11782->0.11776->0.146683 | 0.13886->0.09999->0.058343 |
| SOL | SOL_2025_STRESS | 5400-5500 | `ruhig_zentrumsnah->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 0 | `gemischte_rohwelt` | 0.416127->0.450354->0.44095 | 0.102986->0.110436->0.108383 | 0.170228->0.223508->0.315627 |
| BTC | BTC_2024_5M | 9200-9600 | `normale_weltspannung->lauter_feldkontakt` | `brueckenuebergang_zum_lauten_kontakt` | 1 | `gemischte_rohwelt` | 0.366893->0.469479->0.60707 | 0.094526->0.115972->0.146683 | 0.216127->0.111483->0.058343 |
| BTC | BTC_2024_5M | 1700-1800 | `normale_weltspannung->lauter_feldkontakt` | `offener_uebergang_zum_lauten_kontakt` | 0 | `gemischte_rohwelt` | 0.453618->0.482094->0.405593 | 0.113302->0.118461->0.102651 | 0.120266->0.122476->0.117228 |
| BTC | BTC_2024_5M | 5600-5700 | `ruhig_zentrumsnah->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 1 | `gemischte_rohwelt` | 0.390585->0.447385->0.453687 | 0.099552->0.111075->0.113814 | 0.08584->0.085103->0.075637 |
| BTC | BTC_2024_5M | 1600-1800 | `normale_weltspannung->lauter_feldkontakt` | `brueckenuebergang_zum_lauten_kontakt` | 1 | `gemischte_rohwelt` | 0.387205->0.467856->0.405593 | 0.097488->0.115881->0.102651 | 0.129267->0.121371->0.117228 |
| BTC | BTC_2024_5M | 3800-3900 | `ruhig_zentrumsnah->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 1 | `gemischte_rohwelt` | 0.343799->0.45021->0.429976 | 0.089628->0.110781->0.109572 | 0.127626->0.116414->0.159991 |
| BTC | BTC_2024_5M | 9300-9400 | `normale_weltspannung->lauter_feldkontakt` | `offener_uebergang_zum_lauten_kontakt` | 0 | `gemischte_rohwelt` | 0.443218->0.481308->0.431889 | 0.110549->0.11782->0.109062 | 0.10709->0.13886->0.136954 |
| BTC | BTC_2024_5M | 1600-1700 | `ruhig_zentrumsnah->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 1 | `gemischte_rohwelt` | 0.387205->0.453618->0.482094 | 0.097488->0.113302->0.118461 | 0.129267->0.120266->0.122476 |
| SOL | SOL_2025_STRESS | 1200-1400 | `ruhig_zentrumsnah->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 1 | `gemischte_rohwelt` | 0.412866->0.456937->0.461789 | 0.102288->0.113869->0.113166 | 0.310723->0.281616->0.377101 |
| BTC | BTC_2024_5M | 7900-8000 | `randlastige_sinneslage->lauter_feldkontakt` | `offener_uebergang_zum_lauten_kontakt` | 0 | `gemischte_rohwelt` | 0.453293->0.474375->0.439427 | 0.114453->0.118873->0.109681 | 0.130734->0.141957->0.149473 |
| BTC | BTC_2024_5M | 6000-6200 | `lauter_feldkontakt->lauter_feldkontakt` | `lauter_kontakt_bleibt_offen` | 0 | `gemischte_rohwelt` | 0.460735->0.473162->0.422336 | 0.114815->0.117973->0.1098 | 0.075657->0.177329->0.352349 |

## Bewertung

Die komprimierte Sinnesphase faellt nicht in eine einzige Rolle.

Sie erscheint vor allem als Uebergang in lauteren Kontakt, als randnaher Kontaktdruck und als Aktivierung aus zentrumsnaher Ruhe.

Damit wirkt sie eher wie eine lokale Feldfunktion: Sie kann Bruecke, Randnaehe oder aktivierten Zentrumskontakt tragen, je nachdem aus welcher Lagefolge sie entsteht.

Wie es weitergeht: Als naechstes sollte diese Rollenlesung gegen das bestehende Bedeutungsnetz gelesen werden: Welche `dio_*`-Familien liegen in Fenstern mit `brueckenuebergang_zum_lauten_kontakt`, und bleiben sie in Folgefenstern stabil oder driften sie?
