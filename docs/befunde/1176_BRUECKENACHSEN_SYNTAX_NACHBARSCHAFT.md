# 1176 - Syntax-Nachbarschaft der Brueckenachsen

## Grundfrage

Tauchen die lokalen Ton-/Brueckenunterschiede aus 1169-1172 in MINI_DIOs eigener Syntax wieder auf?

Geprueft wurde nicht, ob unsere Diagnoseklassen passen, sondern ob um die Brueckenereignisse wiederkehrende `symbol_family`-Nachbarschaften entstehen.

Damit ist die Prueffrage:

Bildet MINI_DIO eigene Bedeutungsinseln fuer fallende und steigende Brueckenrichtung, oder sehen wir bisher nur externe Auswertungsmerkmale?

## Methode

Aus den lokalen Segmentfenstern aus 1170 wurden die Familien im Umfeld der Achsenpaare gelesen:

- `dio_00ly -> dio_104t`
- `dio_104t -> dio_00ly`

Die Achsenfamilien selbst wurden fuer die Nachbarschaftszaehlung ausgeklammert.

Geprueft wurden:

- Familienanzahl je Richtung,
- wiederkehrende Nachbarfamilien,
- Ueberlappung der Familienraeume,
- Cosinusnaehe der Familienzaehlungen,
- phasenbezogene Nachbarschaften vor, zwischen und nach dem Paar.

## Ergebnis

Die beiden Richtungen bilden keine hart getrennten Symbolraeume.

| Vergleich | Wert |
|---|---:|
| Familien `dio_00ly -> dio_104t` | 139 |
| Familien `dio_104t -> dio_00ly` | 172 |
| Familien mit mindestens 3 Treffern, Richtung A | 73 |
| Familien mit mindestens 3 Treffern, Richtung B | 88 |
| Ueberlappung ab 3 Treffern | 52 |
| Jaccard ab 3 Treffern | 0.4771 |
| Cosinusnaehe aller Zaehlungen | 0.8766 |

Das ist ein hoher Zusammenhang.

Die Brueckenrichtungen liegen also in einem gemeinsamen Bedeutungsnetz. Sie sind nicht zwei getrennte Inseln.

## Gewichtungsverschiebung

Trotz hoher Ueberlappung gibt es Richtungsbias:

Bei `dio_00ly -> dio_104t` fallen unter anderem staerker auf:

- `dio_00ja`
- `dio_1uof`
- `dio_1lsu`
- `dio_06s7`

Bei `dio_104t -> dio_00ly` fallen unter anderem staerker auf:

- `dio_0tay`
- `dio_1kpz`
- `dio_1r55`
- `dio_17ct`
- `dio_0oc3`

Diese Familien sind keine bewiesenen Bedeutungen. Sie sind Kandidaten fuer lokale Gewichtung innerhalb desselben Brueckenraums.

## MCM-Lesung

Der aktuelle Stand spricht nicht fuer zwei getrennte Bedeutungsinseln.

Er spricht fuer:

- einen gemeinsamen Brueckenraum,
- hohe innere Nachbarschaft,
- lokale Gewichtungsverschiebung je Tonrichtung,
- noch keine vollstaendig eigenstaendige semantische Trennung.

Das ist fachlich plausibel:

Ein MCM-Feld muss nicht fuer jede Richtung sofort eine eigene Insel bilden. Es kann zuerst einen gemeinsamen Raum tragen und darin lokale Rollen verschieben.

## Antwort auf die Prueffrage

Die Ton-/Brueckenunterschiede tauchen in MINI_DIOs eigener Syntax teilweise wieder auf, aber noch nicht als klare getrennte Bedeutungsinseln.

Besser formuliert:

MINI_DIO zeigt ein gemeinsames Brueckennetz mit richtungsabhaengiger Nachbarschaftsgewichtung.

Das ist mehr als reine externe Messung, aber noch weniger als eine ausgereifte eigene Bedeutungsfamilie fuer jede Richtung.

## Grenze

Die Nachbarschaftszaehlung sagt noch nicht, dass MINI_DIO diese Rollen bewusst oder stabil unterscheidet.

Dafuer waere ein Folgetest noetig:

- dieselben Richtungsfenster in weiteren Welten suchen,
- pruefen, ob `dio_00ja`, `dio_0tay`, `dio_1kpz`, `dio_1uof` wieder richtungsnah auftauchen,
- pruefen, ob daraus eine neue stabile Familienrolle entsteht oder ob es Oberflaechenvarianz bleibt.

## Kurzfazit

Die Brueckenachsen sind kein isoliertes Paar.

Sie liegen in einem groesseren Bedeutungsnetz. Die Richtung zeigt sich bisher nicht als harte Symboltrennung, sondern als Verschiebung der Nachbarschaftsgewichte innerhalb dieses Netzes.

Das ist ein wichtiger Zwischenstand: MINI_DIO verdichtet nicht blind einzelne Werte, sondern baut einen gemeinsamen semantischen Raum, in dem lokale Richtungsqualitaeten unterschiedlich gewichtet werden.

