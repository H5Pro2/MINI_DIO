# Bewertung 1316 - Balancierte Zwischenlagen

## Prueffrage

Nach `1313-1314` war offen, ob SOL die Zwischenlagen nur wegen groesserer Datenmenge dominiert.

Deshalb wurde eine balancierte Pruefung erzeugt:

```text
pro reales Asset:
  32 Fenster aus Block 100
  23 Fenster aus Block 200
  15 Fenster aus Block 400
  = 70 Fenster pro Asset
```

Synthetische Welten wurden nicht in die Balance einbezogen.

## Ergebnis

Alle realen Assets bleiben in derselben dominanten Rohklasse:

```text
gemischte_rohwelt
```

Die Sinneswerte bleiben nah beieinander:

| Asset | Hoeren | Sicht | Felddruck | Range | Dominante Sequenz |
|---|---:|---:|---:|---:|---|
| BTC | 0.4095 | 0.6481 | 0.1046 | 0.2159 | offen_suchend -> offen_suchend |
| DOGE | 0.4372 | 0.6601 | 0.1097 | 0.4320 | normale_weltspannung -> normale_weltspannung |
| PAXG | 0.4196 | 0.6536 | 0.1094 | 0.0818 | ruhig_zentrumsnah -> normale_weltspannung |
| SOL | 0.4166 | 0.6495 | 0.1059 | 0.3686 | normale_weltspannung -> normale_weltspannung |
| XRP | 0.4301 | 0.6616 | 0.1080 | 0.4252 | normale_weltspannung -> normale_weltspannung |

## Lesart

Der Kern bleibt assetuebergreifend:

```text
Zwischenlage = gemischte Rohwelt bei mittlerem Hoeren,
mittlerer Sicht und moderatem Felddruck.
```

Die Oberflaeche faerbt sich je Asset:

- SOL, XRP und DOGE liegen nah bei `normale_weltspannung -> normale_weltspannung`.
- BTC kippt in der balancierten Lesung eher zu `offen_suchend -> offen_suchend`.
- PAXG bleibt bei `ruhig_zentrumsnah -> normale_weltspannung`.

## Wichtigster Befund

Die Zwischenlage bleibt nach Mengen- und Skalenbalance erhalten.

Damit ist sie nicht nur ein SOL-Mengeneffekt.

Gleichzeitig ist sie nicht komplett gleichfoermig:

```text
gemeinsame Feldform:
  gemischte Rohwelt
  aehnliche Sinneswerte
  aehnlicher Felddruck

assetbezogene Faerbung:
  unterschiedliche dominante Lagefolge
  unterschiedliche Range-Oberflaeche
```

Das passt zur bisherigen MCM-Lesung:

Eine Bedeutung kann feldgleich sein, ohne rohdatengleich zu sein.

## Grenze

Die Auswahl ist deterministisch, aber noch kein statistischer Endnachweis.

Fuer eine haertere Pruefung waeren mehrere balancierte Ziehungen oder verschiedene Weltfenster pro Asset sinnvoll.

## Bedeutung fuer MINI_DIO

Mini-DIO sollte Zwischenlagen als wiederkehrende Feldform lesen koennen, ohne die Assetfaerbung zu loeschen.

Das ist wichtig fuer ein spaeteres organisches Wahrnehmungssystem:

```text
Ich erkenne eine aehnliche Feldlage.
Aber die Welt, aus der sie kommt, faerbt diese Lage anders.
```

Die Memory sollte daher nicht nur "gleich" oder "anders" speichern, sondern:

- feldgleiche Bedeutung
- unterschiedliche Weltoberflaeche
- unterschiedliche Folgefaerbung
