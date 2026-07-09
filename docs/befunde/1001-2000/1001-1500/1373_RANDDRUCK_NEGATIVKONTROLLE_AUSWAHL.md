# 1373 - Randdruck: Negativkontrolle Auswahl

## Zweck

Diese Auswahl prueft randnahen Kontaktdruck gegen zwei Gegenproben:

- gleicher fortgesetzter lauter Kontakt, aber ohne laute/druckvolle Rohweltklasse
- gleiche laute/druckvolle Rohweltklasse, aber ohne fortgesetzten lauten Kontakt

Damit wird geprueft, ob Randdruck aus der vollen Kopplung `lauter_feldkontakt->lauter_feldkontakt` plus `laute_oder_druckvolle_rohwelt` entsteht.

## Referenz

- Randdruckfenster: `11`
- Referenz Hoeren: `0.560215`
- Referenz Druck: `0.136674`
- Referenz Range: `0.069175`

## Auswahl

- Kontrollfenster: `6`
- Kontrolltypen: [('same_loud_contact_not_raw_loud', 4), ('same_raw_loud_not_loud_contact_loop', 2)]
- Lagefolgen: [('lauter_feldkontakt->lauter_feldkontakt', 4), ('normale_weltspannung->lauter_feldkontakt', 2)]
- Rohweltklassen: [('gemischte_rohwelt', 4), ('laute_oder_druckvolle_rohwelt', 2)]
