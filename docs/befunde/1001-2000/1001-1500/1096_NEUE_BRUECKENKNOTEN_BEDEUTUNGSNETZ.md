# 1096 - Neue Brueckenknoten im Bedeutungsnetz

Diese Notiz fasst die passive Holdout-Pruefung `1095` zusammen. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Ausgangspunkt

Die bisherige Qualitaetskarte aus `1092` beschreibt fuenf stabile Brueckenfamilien:

- `dio_1ewh`
- `dio_17ct`
- `dio_0g2r`
- `dio_155c`
- `dio_1gp2`

Die Holdout-Pruefung `1095` fragt, ob ausserhalb dieser Karte weitere Familien auftreten, die sowohl tragende Verarbeitung als auch Kippnaehe beruehren und dabei unterscheidbare Feldqualitaeten zeigen.

## Befund

In den Holdout-Welten wurden `66` Familien gefunden, die in beiden Lesarten vorkommen.

Davon sind:

- `5` bekannte Kartenfamilien,
- `2` neue starke Brueckenkandidaten,
- `10` neue lokale Brueckenkandidaten,
- `49` schwache Kontakte.

Die zwei staerksten neuen Kandidaten sind:

| Familie | Lesart | Befund |
|---|---|---|
| `dio_00ly` | starker neuer Brueckenkandidat | hohe tragende Aktivierung, kleinere kippnahe Gegenlesung, in 5m- und 1h-Welten sichtbar |
| `dio_0pq6` | starker neuer Brueckenkandidat | weniger Gesamtaktivitaet, aber klarere Balance zwischen tragender und kippnaher Lesart |

## Technische Deutung

Der Befund spricht dafuer, dass das Bedeutungsnetz nicht nur aus einer festen Symboltabelle besteht.

Stattdessen zeigen sich drei Ebenen:

1. Stabile Kartenfamilien
   - bekannte, wiederholt tragende Brueckenrollen.

2. Neue Brueckenkandidaten
   - Familien, die noch nicht zur stabilen Karte gehoeren, aber wiederholt in tragender und kippnaher Verarbeitung auftauchen.

3. Schwache Kontakte
   - Familien mit Beruehrung, aber noch ohne ausreichende Breite oder Unterscheidbarkeit.

Damit entsteht ein dynamisches Bedeutungsnetz: vorhandene Familien bleiben lesbar, waehrend neue Knoten am Rand der Karte auftreten koennen.

## Grenze

`1095` beweist noch keine neue stabile Bedeutung.

Ein neuer Kandidat gilt erst dann als belastbarer Brueckenknoten, wenn:

- er ueber mehrere Welten wiederkehrt,
- seine tragende und kippnahe Lesart unterscheidbar bleibt,
- seine Tickfenster keine reine Zufallsnaehe zeigen,
- seine Rolle nicht vollstaendig durch eine bekannte Kartenfamilie erklaert wird.

## Bedeutung fuer MINI_DIO

MINI_DIO zeigt hier eine moegliche Erweiterungsfaehigkeit des Innenfelds:

- bekannte Bedeutungen werden nicht einfach ersetzt,
- neue Kandidaten koennen neben ihnen auftreten,
- schwache Kontakte bleiben beobachtbar, ohne sofort als stabile Bedeutung gesetzt zu werden.

Das ist wichtig fuer organische MCM-Mechanik, weil Lernen nicht als starres Hinzufuegen einzelner Werte erscheint, sondern als Reifung, Drift, Rekopplung und moegliche Netzwerkerweiterung.

## Wie es weitergeht

Als naechstes sollten `dio_00ly` und `dio_0pq6` mit Tickfenstern gelesen werden. Ziel ist zu pruefen, ob sie echte neue Brueckenknoten sind oder nur lokale Oberflaechenkontakte.
