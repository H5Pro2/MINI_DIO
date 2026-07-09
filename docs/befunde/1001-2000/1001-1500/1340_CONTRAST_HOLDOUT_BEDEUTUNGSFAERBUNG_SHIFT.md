# Bedeutungsfaerbung - Basis gegen Holdout

Diese Diagnose untersucht, warum einzelne Assetfaerbungen ihre dominante Folge veraendern.

Verglichen werden Basis `1315_WELTLAGEN_ZWISCHENLAGEN_ASSET_BALANCED.csv` und Holdout `1337_CONTRAST_HOLDOUT_ZWISCHENLAGEN_ASSET_BALANCED.csv`.

## Verschiebungen

| Asset | Shift | Basis-Folge | Holdout-Folge | dHoeren | dSicht | dDruck | dRange |
|---|---|---|---|---:|---:|---:|---:|
| BTC | `folgefaerbung_veraendert` | `offen_suchend->offen_suchend` | `normale_weltspannung->normale_weltspannung` | 0.0207 | 0.0173 | 0.0035 | -0.0336 |
| DOGE | `folgefaerbung_veraendert` | `normale_weltspannung->normale_weltspannung` | `offen_suchend->offen_suchend` | -0.0110 | -0.0107 | -0.0020 | -0.1335 |
| PAXG | `druck_entlasteter_normalisierungsshift` | `ruhig_zentrumsnah->normale_weltspannung` | `normale_weltspannung->normale_weltspannung` | -0.0242 | 0.0030 | -0.0072 | 0.0271 |
| SOL | `stabil` | `normale_weltspannung->normale_weltspannung` | `normale_weltspannung->normale_weltspannung` | 0.0001 | 0.0005 | -0.0000 | -0.0032 |
| XRP | `oberflaeche_veraendert` | `normale_weltspannung->normale_weltspannung` | `normale_weltspannung->normale_weltspannung` | -0.0174 | -0.0039 | -0.0031 | -0.1988 |

## Bewertung

Die Feldform bleibt gleich, aber die Faerbung verschiebt sich je nach Rohweltprofil.

Die konkrete Faerbung wird ueber Folge, Hoeren, Sicht, Felddruck und Range beschrieben.

Wichtig ist nicht ein einzelnes Asset, sondern ob ein Shift-Typ in weiteren Welten wiederkehrt oder ausklingt.

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung und kein Gate.

Wie es weitergeht: Als naechstes sollte geprueft werden, ob diese Shift-Typen bei weiteren Holdout-Fenstern erneut auftreten oder ob sie lokale Oberflaechenvarianten bleiben.
