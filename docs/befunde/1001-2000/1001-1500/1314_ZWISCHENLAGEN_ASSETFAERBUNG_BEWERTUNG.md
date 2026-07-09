# Bewertung 1314 - Zwischenlagen und Assetfaerbung

## Prueffrage

Nach `1313` war die Frage:

```text
Sind skalenabhaengige Zwischenlagen ein allgemeines Feldmuster,
oder werden sie durch einzelne Assets/Welten dominiert?
```

## Ergebnis

Die Zwischenlagen treten breit ueber reale Assetwelten auf.

| Asset | Fenster | Anteil | Dominante Sequenz | Hoeren | Sicht | Felddruck |
|---|---:|---:|---|---:|---:|---:|
| SOL | 517 | 0.536 | normale_weltspannung -> normale_weltspannung | 0.4211 | 0.6523 | 0.1066 |
| BTC | 134 | 0.139 | normale_weltspannung -> normale_weltspannung | 0.4263 | 0.6572 | 0.1080 |
| XRP | 121 | 0.125 | normale_weltspannung -> normale_weltspannung | 0.4251 | 0.6569 | 0.1073 |
| DOGE | 116 | 0.120 | normale_weltspannung -> normale_weltspannung | 0.4299 | 0.6588 | 0.1081 |
| PAXG | 70 | 0.073 | ruhig_zentrumsnah -> normale_weltspannung | 0.4196 | 0.6536 | 0.1094 |
| SYNTH | 7 | 0.007 | randlastige_sinneslage -> ueberstabil_mit_randreiz | 0.1770 | 0.8288 | 0.0513 |

## Lesart

SOL ist mengenmaessig dominant, weil mehrere SOL-Welten im Lauf enthalten sind.

Fachlich ist die Zwischenlage aber nicht SOL-exklusiv:

- BTC zeigt sehr aehnliche Werte.
- XRP zeigt sehr aehnliche Werte.
- DOGE zeigt sehr aehnliche Werte.
- PAXG bleibt beteiligt, aber mit anderer dominanter Sequenz.
- Synthetische Welten sind nur Randbeitrag.

## Wichtigster Befund

Die Zwischenlage wirkt wie eine allgemeine Feldleseform realer Weltsequenzen.

Sie ist nicht nur ein einzelnes Asset-Artefakt.

Gleichzeitig zeigt PAXG eine eigene Faerbung:

```text
BTC / XRP / DOGE / SOL:
  normale Weltspannung bleibt normale Weltspannung

PAXG:
  ruhige Zentrumsnaehe geht in normale Weltspannung
```

Damit entsteht eine sinnvolle Trennung:

- gemeinsame MCM-Feldform
- assetbezogene Faerbung
- synthetische Sonderfaelle als Randprobe

## Bedeutung fuer MINI_DIO

Mini-DIO kann Zwischenlagen nicht nur als globale Klasse lesen.

Es muss auch die Weltfaerbung erhalten:

```text
Diese Feldform kommt wieder.
Aber sie faerbt sich je nach Welt/Asset etwas anders.
```

Das ist wichtig gegen starres Auswendiglernen.

Die Bedeutung bleibt nicht rohdatengleich, sondern feldgleich mit unterschiedlicher Oberflaeche.

## Grenze

Die Weltverteilung ist nicht perfekt balanciert.

SOL ist haeufiger vertreten als die anderen Assets.

Der Befund reicht daher fuer eine starke Arbeitshypothese, aber nicht fuer einen finalen Nachweis.

Wie es weitergeht: Als naechstes sollte eine balancierte Assetpruefung erzeugt werden, bei der pro Asset gleich viele Zwischenlagenfenster gelesen werden.
