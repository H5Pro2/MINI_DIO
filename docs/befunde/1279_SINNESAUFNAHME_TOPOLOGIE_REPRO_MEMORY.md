# Sinnesaufnahme Topologie Memory

Passive Verdichtung von Sinnes-Signaturen zu Feldrollen.

Diese Memory ist keine Handlungsschicht. Sie speichert, welche Aufnahmeform mit welcher Feldrolle und welcher Tragqualitaet zusammen auftritt.

## Signaturen

| Signatur | Rolle | Segmente | Dauer | Rekopplung | Strain | Rohfeld | Tragqualitaet | Hoeren | Sehen | Fuehlen |
|---|---|---:|---:|---:|---:|---:|---:|---|---|---|
| leise_scharf_feldduenn_getragen | zentrum_stabil | 23893 | 167128 | 0.7434 | 0.1273 | 0.0498 | 0.7848 | hold | hold | hold |
| mittelton_mittelsicht_feldmittel_getragen | rekopplungsnaehe | 11670 | 13812 | 0.7052 | 0.1478 | 0.1171 | 0.7523 | hold | hold | hold |
| laut_unscharf_feldstark_offen | offene_variante | 10906 | 19297 | 0.6711 | 0.1768 | 0.1821 | 0.7197 | down | up | soften |
| laut_unscharf_feldmittel_offen | offene_variante | 5656 | 11052 | 0.6708 | 0.1743 | 0.1697 | 0.7204 | down | up | hold |
| mittelton_unscharf_feldmittel_offen | offene_variante | 2382 | 5607 | 0.6747 | 0.1686 | 0.1364 | 0.7249 | hold | up | hold |
| laut_unscharf_feldstark_angespannt | spannungsrand_kippnaehe | 1750 | 1908 | 0.5887 | 0.2777 | 0.3917 | 0.6315 | down | up | down |
| leise_unscharf_feldduenn_offen | offene_variante | 906 | 14858 | 0.6506 | 0.1825 | 0.0000 | 0.7040 | up | up | up |
| leise_unscharf_feldduenn_angespannt | spannungsrand_kippnaehe | 821 | 1015 | 0.5937 | 0.2868 | 0.0000 | 0.6320 | hold | up | hold |
| laut_mittelsicht_feldstark_offen | offene_variante | 693 | 1385 | 0.6724 | 0.1832 | 0.1947 | 0.7187 | down | hold | soften |
| laut_scharf_feldstark_angespannt | spannungsrand_kippnaehe | 391 | 395 | 0.6179 | 0.2828 | 0.4860 | 0.6497 | down | soften | down |
| leise_unscharf_feldduenn_getragen | rekopplungsnaehe | 95 | 103 | 0.7073 | 0.1243 | 0.0000 | 0.7612 | hold | hold | hold |

## Rollenindex

- `offene_variante`: `laut_mittelsicht_feldstark_offen`, `laut_unscharf_feldmittel_offen`, `laut_unscharf_feldstark_offen`, `leise_unscharf_feldduenn_offen`, `mittelton_unscharf_feldmittel_offen`
- `rekopplungsnaehe`: `leise_unscharf_feldduenn_getragen`, `mittelton_mittelsicht_feldmittel_getragen`
- `spannungsrand_kippnaehe`: `laut_scharf_feldstark_angespannt`, `laut_unscharf_feldstark_angespannt`, `leise_unscharf_feldduenn_angespannt`
- `zentrum_stabil`: `leise_scharf_feldduenn_getragen`

## Befund

- Staerkste Tragqualitaet: `leise_scharf_feldduenn_getragen` -> `zentrum_stabil` mit `0.7848`.
- Schwaechste Tragqualitaet: `laut_unscharf_feldstark_angespannt` -> `spannungsrand_kippnaehe` mit `0.6315`.

## Bewertung

Mini-DIO kann Sinnesaufnahme jetzt als passive Bedeutungsnaehe speichern: nicht als Rohdatenstrom, sondern als wiederkehrende Aufnahmeform mit Feldrolle.

Zusaetzlich erzeugt die Memory jetzt eine achsenabhaengige Rezeptor-Praeferenz. Sie ist keine Handlung und kein Gate. Sie beschreibt nur, ob Mini-DIO bei aehnlicher Aufnahme eher Hoeren, Sehen oder Fuehlen hochregeln, herunterregeln oder halten sollte.

Das ist die Grundlage fuer eine spaetere lernende Rezeptorschicht. Sie kann im naechsten Schritt nicht entscheiden, aber lesen: Diese Aufnahmeart fuehrt haeufig zu Zentrum, Bruecke, Offenheit oder Rand und legt eine bestimmte Sinneshaltung nahe.

Wie es weitergeht: Als naechstes sollte diese Memory ueber neue Welten reproduziert werden. Bleiben die Signaturen rollenstabil, oder entstehen neue Mischsignaturen?
