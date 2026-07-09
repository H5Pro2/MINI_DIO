# 1367 - Zentrumskontakt: Negativkontrolle Auswahl

## Zweck

Diese Auswahl prueft den Zentrumskontakt gegen zwei Gegenproben:

- gleicher Zielkontakt `->lauter_feldkontakt`, aber ohne zentrumsnahen Ausgang
- gleicher zentrumsnaher Ausgang, aber ohne Zielkontakt `->lauter_feldkontakt`

Damit wird geprueft, ob der Zentrumskontakt aus der vollen Lagefolge `ruhig_zentrumsnah->lauter_feldkontakt` entsteht.

## Referenz

- Zentrumfenster: `9`
- Referenz Hoeren: `0.477092`
- Referenz Druck: `0.118239`
- Referenz Range: `0.125133`

## Auswahl

- Kontrollfenster: `19`
- Kontrolltypen: [('same_origin_not_loud_contact', 7), ('same_target_not_center_origin', 12)]
- Lagefolgen: [('lauter_feldkontakt->lauter_feldkontakt', 1), ('normale_weltspannung->lauter_feldkontakt', 9), ('offen_suchend->lauter_feldkontakt', 1), ('randlastige_sinneslage->lauter_feldkontakt', 1), ('ruhig_zentrumsnah->normale_weltspannung', 7)]
