# Adaptierte Feldkopplung: Zeitaufloesungs-Topologie-Synthese

Stand: 2026-06-22

## Zweck

Diese Synthese prueft, ob die passive MCM-Topologie an einer bestimmten Kerzenfrequenz haengt.

Verglichen wurden 5m- und 1h-Welten fuer:

- BTC
- SOL
- KAS
- PAXG
- DOGE
- XRP

Die Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, keine Strategie und keine Richtungsvorgabe.

## Kernergebnis

Die Rollen-Topologie bleibt unter anderer Zeitaufloesung erhalten.

In allen geprueften Welten bleiben sichtbar:

- zentrumsnahe Stabilisierung,
- offene Variante,
- kleine Rand-/Kippnaehe,
- Rekopplungsnaehe als Uebergangsqualitaet.

Es gibt keine pauschale 1h-Verzerrung.

1h macht das Feld nicht automatisch ruhiger, offener oder randlastiger.

## 5m gegen 1h

Die wichtigsten Verschiebungen:

| Asset | Zentrum 5m | Zentrum 1h | Delta Zentrum | Offen 5m | Offen 1h | Delta Offen |
|---|---:|---:|---:|---:|---:|---:|
| BTC | 0.7934 | 0.7914 | -0.0020 | 0.1976 | 0.1961 | -0.0015 |
| SOL | 0.7543 | 0.7823 | +0.0281 | 0.2372 | 0.2101 | -0.0271 |
| KAS | 0.7783 | 0.7688 | -0.0095 | 0.2131 | 0.2202 | +0.0070 |
| PAXG | 0.8474 | 0.7919 | -0.0555 | 0.1497 | 0.2020 | +0.0523 |
| DOGE | 0.7963 | 0.7959 | -0.0004 | 0.1968 | 0.1977 | +0.0008 |
| XRP | 0.7960 | 0.8136 | +0.0176 | 0.1958 | 0.1781 | -0.0178 |

## Lesart

Die Topologie scheint nicht direkt an `5m` oder `1h` zu haengen.

Stattdessen reagiert sie auf die Weltwirkung, die nach Sinnesaufnahme und Rezeptoradaptation im Feld ankommt.

Das ist wichtig:

```text
Zeitaufloesung veraendert den Kontakt zur Welt.
Sie ersetzt aber nicht die MCM-Feldwirkung.
```

DOGE bleibt fast identisch zwischen 5m und 1h.
SOL und XRP werden in 1h zentrumsnaeher.
PAXG verliert in 1h seine besonders starke Zentrumslage und wird offener.
KAS wird leicht offener und randnaeher.

## Rezeptorbefund

Die Adaptionsratio bleibt auch im Zeitvergleich eng bei ca. `0.85`.

Gleichzeitig steigen in den Hochlastfenstern einzelner 1h-Welten Lautheit, Rohfeldaufnahme und Adaptionsreduktion leicht an.

Beispiel:

- staerkste auditive Hochlast: `BTC_1H`
- staerkste Adaptionsreduktion: `BTC_1H`
- staerkste Hochlast-Randnaehe: `KAS_1H`

Das spricht dafuer, dass 1h groessere Weltpakete liefern kann, die Rezeptorschicht diese aber weiter begrenzt.

## Fachliche Ableitung

Die bisherige Annahme wird gestuetzt:

```text
MCM-Topologie entsteht nicht aus Rohdatenfrequenz allein.
Sie entsteht aus der gekoppelten Feldwirkung nach Wahrnehmung und Rezeptoradaptation.
```

Damit bleibt die Topologie nicht nur assetstabil und zustandsstabil, sondern im aktuellen Test auch zeitaufloesungsstabil.

## Grenze

Die Pruefung ist noch kein Universalbeweis.

Sie zeigt:

- robuste Reproduktion in den geprueften Welten,
- keine einfache Abhaengigkeit von 5m/1h,
- aber assetbezogene Verschiebungen der Rollenanteile.

Fuer eine staerkere Aussage braucht es:

- laengere Zeitfenster,
- mehr als zwei Zeitaufloesungen,
- und eine gezielt synthetische Welt, in der dieselbe Struktur nur zeitlich gedehnt oder gestaucht wird.

## Wie es weitergeht

Als naechstes sollte eine synthetische Zeitdehnungswelt gebaut werden: gleiche Formfolge, einmal kompakt und einmal gedehnt. Ziel ist zu pruefen, ob MINI_DIO dieselbe MCM-Rollenordnung trotz veraenderter zeitlicher Streckung erkennt.
