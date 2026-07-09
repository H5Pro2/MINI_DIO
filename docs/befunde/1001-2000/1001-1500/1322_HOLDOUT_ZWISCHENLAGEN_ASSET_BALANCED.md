# Balancierte Zwischenlagen - Assetvergleich

Diese Diagnose liest skalenabhaengige Zwischenlagen mit gleicher Fensterzahl pro realem Asset.

Sample pro Asset: `26` Fenster.

Skalenquote:

- Block `100`: `15` Fenster pro Asset
- Block `200`: `8` Fenster pro Asset
- Block `400`: `3` Fenster pro Asset

Synthetische Welten werden hier nicht in die Balance einbezogen.

## Assetvergleich

| Asset | Fenster | Rohklasse | Sequenz | Skalen | Hoeren | Sicht | Felddruck | Range |
|---|---:|---|---|---|---:|---:|---:|---:|
| BTC | 26 | gemischte_rohwelt | lauter_feldkontakt->lauter_feldkontakt | 100:15;200:8;400:3 | 0.4625 | 0.6736 | 0.1145 | 0.1397 |
| DOGE | 26 | gemischte_rohwelt | normale_weltspannung->normale_weltspannung | 100:15;200:8;400:3 | 0.4207 | 0.6474 | 0.1060 | 0.2871 |
| KAS | 26 | gemischte_rohwelt | normale_weltspannung->normale_weltspannung | 100:15;200:8;400:3 | 0.4258 | 0.6482 | 0.1078 | 0.5653 |
| PAXG | 26 | gemischte_rohwelt | normale_weltspannung->normale_weltspannung | 100:15;200:8;400:3 | 0.3993 | 0.6623 | 0.1027 | 0.0926 |
| SOL | 26 | gemischte_rohwelt | normale_weltspannung->normale_weltspannung | 100:15;200:8;400:3 | 0.4369 | 0.6749 | 0.1091 | 0.3674 |

## Bewertung

Die balancierte Lesung nimmt SOL die Mengen-Dominanz.

Wenn die Zwischenlagen danach weiter aehnliche Rohklassen und Sinneswerte tragen, spricht das fuer eine gemeinsame MCM-Feldform mit Assetfaerbung.

Wenn einzelne Assets stark abweichen, ist die Zwischenlage eher weltgebunden.

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung und keine Steuerung.

Wie es weitergeht: Als naechstes sollte der balancierte Befund gegen die unbalancierte Verteilung aus `1313` bewertet werden.
