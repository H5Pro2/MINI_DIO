# MCM-Shift-Triggerprofile

Diese Diagnose bindet wiederkehrende Bedeutungsfaerbungen an konkrete Rohwelt- und Sinnesprofile zurueck.

Sie bleibt passiv: keine Handlung, keine Richtung, kein Gate.

## Einzelprofile

| Quelle | Asset | Shift | Folge | Rohklasse | dHoeren | dSicht | dDruck | dRange | Holdout-Hoeren | Holdout-Sicht | Holdout-Druck | Holdout-Range |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| FIRST | BTC | `hoerbarer_schmaler_folgeschift` | `lauter_feldkontakt->lauter_feldkontakt` | `gemischte_rohwelt` | 0.0530 | 0.0255 | 0.0099 | -0.0762 | 0.4625 | 0.6736 | 0.1145 | 0.1397 |
| FIRST | DOGE | `oberflaeche_veraendert` | `normale_weltspannung->normale_weltspannung` | `gemischte_rohwelt` | -0.0165 | -0.0127 | -0.0037 | -0.1449 | 0.4207 | 0.6474 | 0.1060 | 0.2871 |
| FIRST | PAXG | `druck_entlasteter_normalisierungsshift` | `normale_weltspannung->normale_weltspannung` | `gemischte_rohwelt` | -0.0204 | 0.0087 | -0.0067 | 0.0108 | 0.3993 | 0.6623 | 0.1027 | 0.0926 |
| SECOND | BTC | `folgefaerbung_veraendert` | `normale_weltspannung->normale_weltspannung` | `gemischte_rohwelt` | -0.0000 | 0.0009 | -0.0000 | -0.0034 | 0.4095 | 0.6490 | 0.1046 | 0.2125 |
| CONTRAST | BTC | `folgefaerbung_veraendert` | `normale_weltspannung->normale_weltspannung` | `gemischte_rohwelt` | 0.0207 | 0.0173 | 0.0035 | -0.0336 | 0.4302 | 0.6653 | 0.1081 | 0.1823 |
| CONTRAST | DOGE | `folgefaerbung_veraendert` | `offen_suchend->offen_suchend` | `gemischte_rohwelt` | -0.0110 | -0.0107 | -0.0020 | -0.1335 | 0.4263 | 0.6495 | 0.1077 | 0.2985 |
| CONTRAST | PAXG | `druck_entlasteter_normalisierungsshift` | `normale_weltspannung->normale_weltspannung` | `gemischte_rohwelt` | -0.0242 | 0.0030 | -0.0072 | 0.0271 | 0.3955 | 0.6566 | 0.1022 | 0.1089 |
| CONTRAST | XRP | `oberflaeche_veraendert` | `normale_weltspannung->normale_weltspannung` | `gemischte_rohwelt` | -0.0174 | -0.0039 | -0.0031 | -0.1988 | 0.4127 | 0.6577 | 0.1049 | 0.2264 |

## Verdichtete Shift-Typen

| Shift | Vorkommen | Assets | dHoeren | dSicht | dDruck | dRange | Holdout-Hoeren | Holdout-Sicht | Holdout-Druck | Holdout-Range |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `druck_entlasteter_normalisierungsshift` | 2 | PAXG | -0.0223 | 0.0059 | -0.0070 | 0.0190 | 0.3974 | 0.6595 | 0.1024 | 0.1008 |
| `folgefaerbung_veraendert` | 3 | BTC,DOGE | 0.0032 | 0.0025 | 0.0005 | -0.0568 | 0.4220 | 0.6546 | 0.1068 | 0.2311 |
| `hoerbarer_schmaler_folgeschift` | 1 | BTC | 0.0530 | 0.0255 | 0.0099 | -0.0762 | 0.4625 | 0.6736 | 0.1145 | 0.1397 |
| `oberflaeche_veraendert` | 2 | DOGE,XRP | -0.0170 | -0.0083 | -0.0034 | -0.1719 | 0.4167 | 0.6526 | 0.1055 | 0.2567 |

## Bewertung

`druck_entlasteter_normalisierungsshift` erscheint bisher als PAXG-nahe Normalisierung: Hoeren und Felddruck sinken gegenueber der Basis, waehrend die Folge auf `normale_weltspannung->normale_weltspannung` rueckbindet.

`oberflaeche_veraendert` erscheint bisher als Oberflaechen-/Range-Verschiebung: die dominante Folge kann gleich bleiben, aber Range und teilweise Hoeren/Sicht veraendern die Faerbung.

`hoerbarer_schmaler_folgeschift` bleibt ein einzelner starker BTC-Befund aus `1325`: Hoeren, Sicht und Druck steigen, Range sinkt deutlich. Dieser Typ ist noch nicht reproduziert.

Wie es weitergeht: Als naechstes sollte gezielt eine Weltgruppe mit hoher Hoer-/Sichtzunahme und sinkender Range gebaut oder ausgewaehlt werden, um zu pruefen, ob `hoerbarer_schmaler_folgeschift` wiederholbar ist.
