# 1361 - Brueckenfunktion: Negativkontrolle Auswahl

## Zweck

Diese Auswahl sucht Fenster mit aehnlicher Hoer-/Druckstaerke wie die Brueckenfenster aus `1358`, aber ohne Lagefolge `->lauter_feldkontakt`.
Damit wird geprueft, ob die Bruecken-Nachhallfunktion aus der Lagefolge entsteht oder nur aus starker Sinnesaktivierung.

## Referenz

- Brueckenfenster: `10`
- Referenz Hoeren: `0.492219`
- Referenz Druck: `0.121039`
- Referenz Range: `0.155565`

## Auswahl

- Kontrollfenster: `20`
- Assets: [('BTC', 5), ('SOL', 14), ('XRP', 1)]
- Lagefolgen: [('lauter_feldkontakt->normale_weltspannung', 2), ('normale_weltspannung->normale_weltspannung', 7), ('normale_weltspannung->offen_suchend', 2), ('offen_suchend->normale_weltspannung', 3), ('offen_suchend->offen_suchend', 1), ('randlastige_sinneslage->normale_weltspannung', 3), ('ruhig_zentrumsnah->normale_weltspannung', 2)]

## Wie es weitergeht

Als naechstes wird diese Auswahl durch dieselbe Rohwelt-, Rollen- und Nachhallpipeline gelesen wie die Brueckenfenster.
