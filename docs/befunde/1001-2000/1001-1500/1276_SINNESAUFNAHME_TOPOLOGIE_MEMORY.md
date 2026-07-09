# Sinnesaufnahme Topologie Memory

Passive Verdichtung von Sinnes-Signaturen zu Feldrollen.

Diese Memory ist keine Handlungsschicht. Sie speichert, welche Aufnahmeform mit welcher Feldrolle und welcher Tragqualitaet zusammen auftritt.

## Signaturen

| Signatur | Rolle | Segmente | Dauer | Rekopplung | Strain | Rohfeld | Tragqualitaet | Hoeren | Sehen | Fuehlen |
|---|---|---:|---:|---:|---:|---:|---:|---|---|---|
| leise_scharf_feldduenn_getragen | zentrum_stabil | 6886 | 44707 | 0.7441 | 0.1278 | 0.0505 | 0.7851 | hold | hold | hold |
| laut_unscharf_feldmittel_offen | offene_variante | 5656 | 11052 | 0.6708 | 0.1743 | 0.1697 | 0.7204 | down | up | hold |
| mittelton_mittelsicht_feldmittel_getragen | rekopplungsnaehe | 4226 | 5074 | 0.7056 | 0.1440 | 0.1077 | 0.7537 | hold | hold | hold |
| laut_mittelsicht_feldstark_offen | offene_variante | 693 | 1385 | 0.6724 | 0.1832 | 0.1947 | 0.7187 | down | hold | soften |
| laut_unscharf_feldstark_angespannt | spannungsrand_kippnaehe | 571 | 615 | 0.5869 | 0.2781 | 0.3895 | 0.6301 | down | up | down |
| laut_scharf_feldstark_angespannt | spannungsrand_kippnaehe | 391 | 395 | 0.6179 | 0.2828 | 0.4860 | 0.6497 | down | soften | down |

## Rollenindex

- `offene_variante`: `laut_mittelsicht_feldstark_offen`, `laut_unscharf_feldmittel_offen`
- `rekopplungsnaehe`: `mittelton_mittelsicht_feldmittel_getragen`
- `spannungsrand_kippnaehe`: `laut_scharf_feldstark_angespannt`, `laut_unscharf_feldstark_angespannt`
- `zentrum_stabil`: `leise_scharf_feldduenn_getragen`

## Befund

- Staerkste Tragqualitaet: `leise_scharf_feldduenn_getragen` -> `zentrum_stabil` mit `0.7851`.
- Schwaechste Tragqualitaet: `laut_unscharf_feldstark_angespannt` -> `spannungsrand_kippnaehe` mit `0.6301`.

## Bewertung

Mini-DIO kann Sinnesaufnahme jetzt als passive Bedeutungsnaehe speichern: nicht als Rohdatenstrom, sondern als wiederkehrende Aufnahmeform mit Feldrolle.

Zusaetzlich erzeugt die Memory jetzt eine achsenabhaengige Rezeptor-Praeferenz. Sie ist keine Handlung und kein Gate. Sie beschreibt nur, ob Mini-DIO bei aehnlicher Aufnahme eher Hoeren, Sehen oder Fuehlen hochregeln, herunterregeln oder halten sollte.

Das ist die Grundlage fuer eine spaetere lernende Rezeptorschicht. Sie kann im naechsten Schritt nicht entscheiden, aber lesen: Diese Aufnahmeart fuehrt haeufig zu Zentrum, Bruecke, Offenheit oder Rand und legt eine bestimmte Sinneshaltung nahe.
