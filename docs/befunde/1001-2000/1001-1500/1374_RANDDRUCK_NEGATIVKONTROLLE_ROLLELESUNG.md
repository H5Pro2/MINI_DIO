# 1374 - Randdruck: Negativkontrolle Rollenlesung

Diese Diagnose liest die Randdruck-Kontrollfenster aus `1373` gegen passive Feldrollen.

Wichtig: Die Rollen werden hier nicht als neue Mechanik gesetzt. Es ist eine Ruecklesung der Lagefolge:

```text
Welche Feldrolle wird durch diese Mikrophase nahegelegt?
```

Die Diagnose erzeugt keine Handlung, keine Richtung und kein Gate.

## Verdichtung

- gelesene Fenster: `6`
- komprimierte Sinnesphase: `3`
- Brueckennaehe: `2`
- Randnaehe: `0`
- Zentrumskontakt: `0`

Rollen:

- `lauter_kontakt_bleibt_offen`: `4`
- `brueckenuebergang_zum_lauten_kontakt`: `2`

Lagefolgen:

- `lauter_feldkontakt->lauter_feldkontakt`: `4`
- `normale_weltspannung->lauter_feldkontakt`: `2`

## Fenster

| Asset | Welt | Ticks | Lagefolge | passive Rolle | kompakt | Klasse | Hoeren | Druck | Range |
|---|---|---:|---|---|---:|---|---|---|---|
| BTC | BTC_2024_5M | 5800-5900 | `normale_weltspannung->lauter_feldkontakt` | `brueckenuebergang_zum_lauten_kontakt` | 1 | `laute_oder_druckvolle_rohwelt` | 0.453687->0.609422->0.460735 | 0.113814->0.145789->0.114815 | 0.075637->0.043024->0.075657 |
| SOL | SOL_2023_ALT_A_FOLLOW | 2200-2300 | `normale_weltspannung->lauter_feldkontakt` | `brueckenuebergang_zum_lauten_kontakt` | 1 | `laute_oder_druckvolle_rohwelt` | 0.387923->0.531606->0.467813 | 0.099374->0.129368->0.11632 | 0.261434->0.208557->0.244543 |
| DOGE | DOGE_2024_5M_CONTRAST | 5000-5100 | `lauter_feldkontakt->lauter_feldkontakt` | `lauter_kontakt_bleibt_offen` | 0 | `gemischte_rohwelt` | 0.478087->0.482805->0.481586 | 0.118493->0.119398->0.120434 | 0.125464->0.203511->0.282565 |
| DOGE | DOGE_2024_5M | 5000-5100 | `lauter_feldkontakt->lauter_feldkontakt` | `lauter_kontakt_bleibt_offen` | 0 | `gemischte_rohwelt` | 0.478087->0.482805->0.481586 | 0.118493->0.119398->0.120434 | 0.125464->0.203511->0.282565 |
| XRP | XRP_2024_5M_CONTRAST | 5500-5600 | `lauter_feldkontakt->lauter_feldkontakt` | `lauter_kontakt_bleibt_offen` | 1 | `gemischte_rohwelt` | 0.460506->0.46924->0.440065 | 0.115887->0.116231->0.111524 | 0.199552->0.152257->0.155877 |
| XRP | XRP_2024_5M_CONTRAST | 5400-5600 | `lauter_feldkontakt->lauter_feldkontakt` | `lauter_kontakt_bleibt_offen` | 0 | `gemischte_rohwelt` | 0.468302->0.464873->0.440065 | 0.116606->0.116059->0.111524 | 0.285469->0.175905->0.155877 |

## Bewertung

Die Kontrollfenster fallen nicht in Randdruck.

Sie erscheinen als Brueckenuebergang oder als offener lauter Kontakt.

Damit wirkt Randdruck an die volle Kopplung aus fortgesetztem lautem Kontakt und lauter/druckvoller Rohwelt gebunden.

Wie es weitergeht: Als naechstes wird die Nachhallspur dieser Kontrolle gelesen, um zu pruefen, ob fehlender Randdruck dennoch als andere Feldfunktion weitertraegt.
