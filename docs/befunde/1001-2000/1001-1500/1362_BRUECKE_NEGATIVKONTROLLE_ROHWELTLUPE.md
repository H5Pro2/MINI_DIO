# Hoerbarer schmaler Shift - Rohweltlupe

Diese Diagnose liest starke Mikrofenster gegen konkrete Rohweltabschnitte zurueck.

Gelesen wird passiv:

- Vorfenster
- Trefferfenster
- Folgefenster

Die Diagnose erzeugt keine Handlung, keine Richtung und kein Gate.

## Verdichtung

- gelesene Fenster: `20`
- Trefferfenster enger als Vorfenster: `15`
- Hoeren steigt gegen Vorfenster: `16`
- Felddruck steigt gegen Vorfenster: `16`

## Fenster

| Asset | Welt | Ticks | Sequenz | Klasse vor -> waehrend -> nach | Range | Hoeren | Druck |
|---|---|---:|---|---|---|---|---|
| SOL | SOL_2025_REC | 3400-3500 | `normale_weltspannung->normale_weltspannung` | `gemischte_rohwelt` -> `gemischte_rohwelt` -> `gemischte_rohwelt` | 0.1506->0.1503->0.1205 | 0.4469->0.4521->0.4078 | 0.1114->0.1119->0.1000 |
| SOL | SOL_2025_REC | 3200-3600 | `offen_suchend->normale_weltspannung` | `gemischte_rohwelt` -> `gemischte_rohwelt` -> `gemischte_rohwelt` | 0.2664->0.1519->0.1175 | 0.3953->0.4490->0.4659 | 0.1007->0.1111->0.1140 |
| SOL | SOL_2025_REC | 3300-3400 | `lauter_feldkontakt->normale_weltspannung` | `gemischte_rohwelt` -> `gemischte_rohwelt` -> `gemischte_rohwelt` | 0.1860->0.1506->0.1503 | 0.4892->0.4469->0.4521 | 0.1210->0.1114->0.1119 |
| XRP | XRP_2024_5M_CONTRAST | 9700-9800 | `offen_suchend->normale_weltspannung` | `gemischte_rohwelt` -> `gemischte_rohwelt` -> `gemischte_rohwelt` | 0.2928->0.1750->0.1405 | 0.4408->0.4613->0.4242 | 0.1122->0.1149->0.1073 |
| SOL | SOL_2025_STRESS | 3200-3400 | `ruhig_zentrumsnah->normale_weltspannung` | `gemischte_rohwelt` -> `gemischte_rohwelt` -> `gemischte_rohwelt` | 0.2160->0.1873->0.2593 | 0.3846->0.4625->0.4792 | 0.0961->0.1139->0.1193 |
| SOL | SOL_2025_REC | 3600-4000 | `normale_weltspannung->normale_weltspannung` | `gemischte_rohwelt` -> `bewegungsreiche_rohwelt` -> `bewegungsreiche_rohwelt` | 0.1205->0.1833->0.3136 | 0.4078->0.4636->0.4668 | 0.1000->0.1142->0.1164 |
| SOL | SOL_2025_REC | 9600-9700 | `normale_weltspannung->normale_weltspannung` | `gemischte_rohwelt` -> `gemischte_rohwelt` -> `gemischte_rohwelt` | 0.1874->0.1743->0.2120 | 0.4344->0.4533->0.3877 | 0.1075->0.1117->0.0984 |
| SOL | SOL_2023_ALT_A_FOLLOW | 8900-9000 | `normale_weltspannung->normale_weltspannung` | `gemischte_rohwelt` -> `gemischte_rohwelt` -> `gemischte_rohwelt` | 0.2221->0.1740->0.2268 | 0.4309->0.4523->0.4528 | 0.1074->0.1143->0.1133 |
| SOL | SOL_2025_REC | 4700-4800 | `randlastige_sinneslage->normale_weltspannung` | `gemischte_rohwelt` -> `gemischte_rohwelt` -> `laute_oder_druckvolle_rohwelt` | 0.3064->0.1909->0.2111 | 0.4565->0.4536->0.5148 | 0.1141->0.1118->0.1248 |
| BTC | BTC_2024_5M | 5900-6000 | `lauter_feldkontakt->normale_weltspannung` | `laute_oder_druckvolle_rohwelt` -> `gemischte_rohwelt` -> `laute_oder_druckvolle_rohwelt` | 0.0430->0.0757->0.1307 | 0.6094->0.4607->0.5301 | 0.1458->0.1148->0.1297 |
| SOL | SOL_2025_REC | 9400-9500 | `normale_weltspannung->offen_suchend` | `gemischte_rohwelt` -> `gemischte_rohwelt` -> `gemischte_rohwelt` | 0.1857->0.1905->0.1874 | 0.4281->0.4576->0.4344 | 0.1056->0.1131->0.1075 |
| SOL | SOL_2025_REC | 5500-5600 | `normale_weltspannung->offen_suchend` | `gemischte_rohwelt` -> `gemischte_rohwelt` -> `gemischte_rohwelt` | 0.2514->0.1949->0.1621 | 0.4010->0.4528->0.4103 | 0.1011->0.1131->0.1035 |
| BTC | BTC_2024_5M | 8400-8500 | `randlastige_sinneslage->normale_weltspannung` | `gemischte_rohwelt` -> `gemischte_rohwelt` -> `gemischte_rohwelt` | 0.1477->0.0952->0.2054 | 0.4358->0.4583->0.4032 | 0.1081->0.1119->0.1019 |
| SOL | SOL_2023_ALT_A_FOLLOW | 4200-4400 | `randlastige_sinneslage->normale_weltspannung` | `gemischte_rohwelt` -> `gemischte_rohwelt` -> `gemischte_rohwelt` | 0.3075->0.2244->0.3349 | 0.4804->0.4621->0.4639 | 0.1185->0.1151->0.1155 |
| SOL | SOL_2025_REC | 7300-7400 | `offen_suchend->offen_suchend` | `gemischte_rohwelt` -> `gemischte_rohwelt` -> `gemischte_rohwelt` | 0.3895->0.2287->0.2355 | 0.4458->0.4552->0.3896 | 0.1127->0.1140->0.0989 |
| SOL | SOL_2025_REC | 400-500 | `offen_suchend->normale_weltspannung` | `gemischte_rohwelt` -> `gemischte_rohwelt` -> `gemischte_rohwelt` | 0.3017->0.2386->0.3252 | 0.4217->0.4629->0.4310 | 0.1065->0.1135->0.1081 |
| BTC | BTC_2024_5M | 7600-8000 | `normale_weltspannung->normale_weltspannung` | `gemischte_rohwelt` -> `gemischte_rohwelt` -> `gemischte_rohwelt` | 0.0903->0.1091->0.1495 | 0.4273->0.4527->0.4394 | 0.1073->0.1134->0.1097 |
| SOL | SOL_2023_ALT_A_FOLLOW | 9000-9200 | `normale_weltspannung->normale_weltspannung` | `gemischte_rohwelt` -> `gemischte_rohwelt` -> `gemischte_rohwelt` | 0.1740->0.2328->0.2230 | 0.4523->0.4566->0.4141 | 0.1143->0.1146->0.1049 |
| BTC | BTC_2024_5M | 9200-9400 | `normale_weltspannung->normale_weltspannung` | `gemischte_rohwelt` -> `gemischte_rohwelt` -> `gemischte_rohwelt` | 0.2161->0.1230->0.1370 | 0.3669->0.4623->0.4319 | 0.0945->0.1142->0.1091 |
| BTC | BTC_2024_5M | 1600-1700 | `ruhig_zentrumsnah->normale_weltspannung` | `gemischte_rohwelt` -> `gemischte_rohwelt` -> `gemischte_rohwelt` | 0.1293->0.1203->0.1225 | 0.3872->0.4536->0.4821 | 0.0975->0.1133->0.1185 |

## Bewertung

Die Mikrophase wird hier als konkrete Weltphase gelesen, nicht als abstrakte Symbolrolle.

Wenn Range enger wird und Hoeren/Felddruck steigen, liegt eine plausible komprimierte Sinnesphase vor: weniger aeussere Ausdehnung, aber mehr innere Ton-/Druckwirkung.
