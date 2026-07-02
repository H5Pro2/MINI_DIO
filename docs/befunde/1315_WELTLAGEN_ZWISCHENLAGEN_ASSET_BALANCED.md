# Balancierte Zwischenlagen - Assetvergleich

Diese Diagnose liest skalenabhaengige Zwischenlagen mit gleicher Fensterzahl pro realem Asset.

Sample pro Asset: `70` Fenster.

Skalenquote:

- Block `100`: `32` Fenster pro Asset
- Block `200`: `23` Fenster pro Asset
- Block `400`: `15` Fenster pro Asset

Synthetische Welten werden hier nicht in die Balance einbezogen.

## Assetvergleich

| Asset | Fenster | Rohklasse | Sequenz | Skalen | Hoeren | Sicht | Felddruck | Range |
|---|---:|---|---|---|---:|---:|---:|---:|
| BTC | 70 | gemischte_rohwelt | offen_suchend->offen_suchend | 100:32;200:23;400:15 | 0.4095 | 0.6481 | 0.1046 | 0.2159 |
| DOGE | 70 | gemischte_rohwelt | normale_weltspannung->normale_weltspannung | 100:32;200:23;400:15 | 0.4372 | 0.6601 | 0.1097 | 0.4320 |
| PAXG | 70 | gemischte_rohwelt | ruhig_zentrumsnah->normale_weltspannung | 100:32;200:23;400:15 | 0.4196 | 0.6536 | 0.1094 | 0.0818 |
| SOL | 70 | gemischte_rohwelt | normale_weltspannung->normale_weltspannung | 100:32;200:23;400:15 | 0.4166 | 0.6495 | 0.1059 | 0.3686 |
| XRP | 70 | gemischte_rohwelt | normale_weltspannung->normale_weltspannung | 100:32;200:23;400:15 | 0.4301 | 0.6616 | 0.1080 | 0.4252 |

## Bewertung

Die balancierte Lesung nimmt SOL die Mengen-Dominanz.

Wenn die Zwischenlagen danach weiter aehnliche Rohklassen und Sinneswerte tragen, spricht das fuer eine gemeinsame MCM-Feldform mit Assetfaerbung.

Wenn einzelne Assets stark abweichen, ist die Zwischenlage eher weltgebunden.

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung und keine Steuerung.

Wie es weitergeht: Als naechstes sollte der balancierte Befund gegen die unbalancierte Verteilung aus `1313` bewertet werden.
