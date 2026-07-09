# Balancierte Zwischenlagen - Assetvergleich

Diese Diagnose liest skalenabhaengige Zwischenlagen mit gleicher Fensterzahl pro realem Asset.

Sample pro Asset: `73` Fenster.

Skalenquote:

- Block `100`: `39` Fenster pro Asset
- Block `200`: `20` Fenster pro Asset
- Block `400`: `14` Fenster pro Asset

Synthetische Welten werden hier nicht in die Balance einbezogen.

## Assetvergleich

| Asset | Fenster | Rohklasse | Sequenz | Skalen | Hoeren | Sicht | Felddruck | Range |
|---|---:|---|---|---|---:|---:|---:|---:|
| BTC | 73 | gemischte_rohwelt | normale_weltspannung->normale_weltspannung | 100:39;200:20;400:14 | 0.4095 | 0.6490 | 0.1046 | 0.2125 |
| DOGE | 73 | gemischte_rohwelt | normale_weltspannung->normale_weltspannung | 100:39;200:20;400:14 | 0.4367 | 0.6601 | 0.1096 | 0.4341 |
| PAXG | 73 | gemischte_rohwelt | ruhig_zentrumsnah->normale_weltspannung | 100:39;200:20;400:14 | 0.4262 | 0.6549 | 0.1108 | 0.0789 |
| SOL | 73 | gemischte_rohwelt | normale_weltspannung->normale_weltspannung | 100:39;200:20;400:14 | 0.4166 | 0.6475 | 0.1060 | 0.2980 |
| XRP | 73 | gemischte_rohwelt | normale_weltspannung->normale_weltspannung | 100:39;200:20;400:14 | 0.4264 | 0.6586 | 0.1074 | 0.4496 |

## Bewertung

Die balancierte Lesung nimmt SOL die Mengen-Dominanz.

Wenn die Zwischenlagen danach weiter aehnliche Rohklassen und Sinneswerte tragen, spricht das fuer eine gemeinsame MCM-Feldform mit Assetfaerbung.

Wenn einzelne Assets stark abweichen, ist die Zwischenlage eher weltgebunden.

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung und keine Steuerung.
