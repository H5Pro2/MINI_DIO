# Hoerbarer schmaler Shift - passive Rollenlesung

Diese Diagnose liest die komprimierte Sinnesphase aus `1350` gegen passive Feldrollen.

Wichtig: Die Rollen werden hier nicht als neue Mechanik gesetzt. Es ist eine Ruecklesung der Lagefolge:

```text
Welche Feldrolle wird durch diese Mikrophase nahegelegt?
```

Die Diagnose erzeugt keine Handlung, keine Richtung und kein Gate.

## Verdichtung

- gelesene Fenster: `20`
- komprimierte Sinnesphase: `12`
- Brueckennaehe: `0`
- Randnaehe: `0`
- Zentrumskontakt: `0`

Rollen:

- `rueckbindung_in_normale_weltspannung`: `17`
- `unklare_mikrophase`: `3`

Lagefolgen:

- `normale_weltspannung->normale_weltspannung`: `7`
- `offen_suchend->normale_weltspannung`: `3`
- `randlastige_sinneslage->normale_weltspannung`: `3`
- `lauter_feldkontakt->normale_weltspannung`: `2`
- `ruhig_zentrumsnah->normale_weltspannung`: `2`
- `normale_weltspannung->offen_suchend`: `2`
- `offen_suchend->offen_suchend`: `1`

## Fenster

| Asset | Welt | Ticks | Lagefolge | passive Rolle | kompakt | Klasse | Hoeren | Druck | Range |
|---|---|---:|---|---|---:|---|---|---|---|
| SOL | SOL_2025_REC | 3400-3500 | `normale_weltspannung->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 1 | `gemischte_rohwelt` | 0.446872->0.45214->0.4078 | 0.111358->0.111922->0.100037 | 0.150636->0.150307->0.120477 |
| SOL | SOL_2025_REC | 3200-3600 | `offen_suchend->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 1 | `gemischte_rohwelt` | 0.395253->0.449009->0.46586 | 0.100708->0.111085->0.114041 | 0.266431->0.151857->0.117548 |
| SOL | SOL_2025_REC | 3300-3400 | `lauter_feldkontakt->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 0 | `gemischte_rohwelt` | 0.489222->0.446872->0.45214 | 0.121022->0.111358->0.111922 | 0.186008->0.150636->0.150307 |
| XRP | XRP_2024_5M_CONTRAST | 9700-9800 | `offen_suchend->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 1 | `gemischte_rohwelt` | 0.440753->0.461316->0.424248 | 0.112189->0.114867->0.107331 | 0.292849->0.175028->0.140524 |
| SOL | SOL_2025_STRESS | 3200-3400 | `ruhig_zentrumsnah->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 1 | `gemischte_rohwelt` | 0.384591->0.462482->0.4792 | 0.096079->0.113894->0.119275 | 0.216043->0.18733->0.259269 |
| SOL | SOL_2025_REC | 3600-4000 | `normale_weltspannung->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 0 | `bewegungsreiche_rohwelt` | 0.4078->0.463605->0.466796 | 0.100037->0.114223->0.11643 | 0.120477->0.183341->0.313557 |
| SOL | SOL_2025_REC | 9600-9700 | `normale_weltspannung->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 1 | `gemischte_rohwelt` | 0.434409->0.453295->0.387702 | 0.107512->0.111657->0.09845 | 0.187423->0.174268->0.211978 |
| SOL | SOL_2023_ALT_A_FOLLOW | 8900-9000 | `normale_weltspannung->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 1 | `gemischte_rohwelt` | 0.430945->0.452312->0.452814 | 0.107377->0.114272->0.113333 | 0.222135->0.173978->0.226789 |
| SOL | SOL_2025_REC | 4700-4800 | `randlastige_sinneslage->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 0 | `gemischte_rohwelt` | 0.456492->0.453623->0.514753 | 0.114065->0.111827->0.124781 | 0.306435->0.190931->0.211063 |
| BTC | BTC_2024_5M | 5900-6000 | `lauter_feldkontakt->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 0 | `gemischte_rohwelt` | 0.609422->0.460735->0.530051 | 0.145789->0.114815->0.129712 | 0.043024->0.075657->0.130719 |
| SOL | SOL_2025_REC | 9400-9500 | `normale_weltspannung->offen_suchend` | `unklare_mikrophase` | 0 | `gemischte_rohwelt` | 0.42807->0.457587->0.434409 | 0.105635->0.113078->0.107512 | 0.185714->0.190491->0.187423 |
| SOL | SOL_2025_REC | 5500-5600 | `normale_weltspannung->offen_suchend` | `unklare_mikrophase` | 1 | `gemischte_rohwelt` | 0.401011->0.452836->0.410309 | 0.101055->0.113067->0.103516 | 0.251406->0.194902->0.162124 |
| BTC | BTC_2024_5M | 8400-8500 | `randlastige_sinneslage->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 1 | `gemischte_rohwelt` | 0.435792->0.458284->0.403165 | 0.108113->0.111907->0.101877 | 0.147678->0.095215->0.205361 |
| SOL | SOL_2023_ALT_A_FOLLOW | 4200-4400 | `randlastige_sinneslage->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 0 | `gemischte_rohwelt` | 0.480361->0.462058->0.463868 | 0.118492->0.115058->0.115536 | 0.307484->0.224433->0.334886 |
| SOL | SOL_2025_REC | 7300-7400 | `offen_suchend->offen_suchend` | `unklare_mikrophase` | 1 | `gemischte_rohwelt` | 0.445751->0.455231->0.389647 | 0.11265->0.11401->0.098891 | 0.389463->0.228694->0.235475 |
| SOL | SOL_2025_REC | 400-500 | `offen_suchend->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 1 | `gemischte_rohwelt` | 0.421669->0.462917->0.430991 | 0.106534->0.113517->0.108142 | 0.301681->0.238564->0.325231 |
| BTC | BTC_2024_5M | 7600-8000 | `normale_weltspannung->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 0 | `gemischte_rohwelt` | 0.427251->0.452677->0.439427 | 0.107258->0.113415->0.109681 | 0.090346->0.109074->0.149473 |
| SOL | SOL_2023_ALT_A_FOLLOW | 9000-9200 | `normale_weltspannung->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 0 | `gemischte_rohwelt` | 0.452312->0.456588->0.41413 | 0.114272->0.114642->0.104857 | 0.173978->0.232785->0.22298 |
| BTC | BTC_2024_5M | 9200-9400 | `normale_weltspannung->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 1 | `gemischte_rohwelt` | 0.366893->0.462263->0.431889 | 0.094526->0.114184->0.109062 | 0.216127->0.122975->0.136954 |
| BTC | BTC_2024_5M | 1600-1700 | `ruhig_zentrumsnah->normale_weltspannung` | `rueckbindung_in_normale_weltspannung` | 1 | `gemischte_rohwelt` | 0.387205->0.453618->0.482094 | 0.097488->0.113302->0.118461 | 0.129267->0.120266->0.122476 |

## Bewertung

Die komprimierte Sinnesphase faellt nicht in eine einzige Rolle.

Sie erscheint vor allem als Uebergang in lauteren Kontakt, als randnaher Kontaktdruck und als Aktivierung aus zentrumsnaher Ruhe.

Damit wirkt sie eher wie eine lokale Feldfunktion: Sie kann Bruecke, Randnaehe oder aktivierten Zentrumskontakt tragen, je nachdem aus welcher Lagefolge sie entsteht.
