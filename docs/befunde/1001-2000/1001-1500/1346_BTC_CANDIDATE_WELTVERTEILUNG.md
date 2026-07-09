# Mehrskalige Zwischenlagen - Asset- und Weltverteilung

Diese Diagnose prueft, ob skalenabhaengige Lagefolgen von einzelnen Assets/Welten dominiert werden.

## Asset-Verteilung

| Asset | Fenster | Anteil | Rohklasse | Sequenz | Skalen | Hoeren | Sicht | Felddruck |
|---|---:|---:|---|---|---|---:|---:|---:|
| BTC | 487 | 1.000 | gemischte_rohwelt | normale_weltspannung->normale_weltspannung | 100:257;200:151;400:79 | 0.4194 | 0.6587 | 0.1063 |

## Welt-Verteilung

| Welt | Fenster | Anteil | Rohklasse | Sequenz | Skalen | Hoeren | Sicht | Felddruck |
|---|---:|---:|---|---|---|---:|---:|---:|
| BTC_2024_5M_FULL | 126 | 0.259 | gemischte_rohwelt | normale_weltspannung->normale_weltspannung | 100:66;200:39;400:21 | 0.4193 | 0.6559 | 0.1066 |
| BTC_2025_5M_FULL | 118 | 0.242 | gemischte_rohwelt | normale_weltspannung->normale_weltspannung | 100:59;200:40;400:19 | 0.4217 | 0.6618 | 0.1065 |
| BTC_2024_5M_STRESS | 51 | 0.105 | gemischte_rohwelt | normale_weltspannung->normale_weltspannung | 100:27;200:15;400:9 | 0.4289 | 0.6641 | 0.1080 |
| BTC_2025_5M_STRESS | 44 | 0.090 | gemischte_rohwelt | normale_weltspannung->normale_weltspannung | 100:23;200:14;400:7 | 0.4193 | 0.6601 | 0.1059 |
| BTC_2024_5M_QUIET | 43 | 0.088 | gemischte_rohwelt | offen_suchend->normale_weltspannung | 100:23;200:13;400:7 | 0.4183 | 0.6534 | 0.1062 |
| BTC_2025_5M_QUIET | 33 | 0.068 | gemischte_rohwelt | leise_duenn->normale_weltspannung | 100:18;200:10;400:5 | 0.4060 | 0.6634 | 0.1043 |
| BTC_2025_5M_TEST | 25 | 0.051 | gemischte_rohwelt | normale_weltspannung->offen_suchend | 100:14;200:7;400:4 | 0.4194 | 0.6463 | 0.1067 |
| BTC_2025_BREAK | 24 | 0.049 | gemischte_rohwelt | normale_weltspannung->normale_weltspannung | 100:15;200:6;400:3 | 0.4163 | 0.6649 | 0.1052 |
| BTC_2024_5M_TEST | 23 | 0.047 | gemischte_rohwelt | normale_weltspannung->normale_weltspannung | 100:12;200:7;400:4 | 0.4115 | 0.6545 | 0.1046 |

## Bewertung

Die skalenabhaengigen Zwischenlagen werden nicht von einer einzelnen Welt erzeugt.

Sie treten breit ueber reale Assetwelten auf. Synthetische Welten sind nur schwach beteiligt.

Damit ist die Zwischenlage eher eine wiederkehrende Feldleseform als ein einzelnes Asset-Artefakt.

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung und keine Steuerung.
