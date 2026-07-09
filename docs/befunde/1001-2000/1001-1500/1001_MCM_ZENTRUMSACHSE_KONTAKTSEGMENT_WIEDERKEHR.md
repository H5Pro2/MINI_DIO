# MCM-Zentrumsachse: Kontaktsegment-Wiederkehr

## Zweck

Diese Datei prueft, welche lokalen Achsen-Kontaktsegmente wiederkehren und welche nur situationsbedingt auftreten.

## Sicherheitsgrenze

- passive Ruecklesung
- keine Handlung
- kein Gate
- keine Strategie

## Wiederkehrstatus

| Status | Anzahl |
|---|---:|
| `situationssegment` | 8 |
| `lokal_wiederholt` | 2 |
| `wiederkehrend_rekoppelnd` | 1 |

## Signaturen

| Signatur | Anzahl | Welten | Pressure Delta | Rekopplung Delta | Lesung |
|---|---:|---:|---:|---:|---|
| `rekoppelnde_lage / rekoppelnde_lage / rekoppelnde_lage / rekoppelnde_lage / paarsegment_rekoppelnd` | 14 | 4 | 0.024289 | -0.004694 | `wiederkehrend_rekoppelnd` |
| `bewegungsbruch / rekoppelnde_lage / bewegungsbruch / rekoppelnde_lage / kontaktsegment_offen` | 2 | 2 | -0.020607 | -0.00441 | `lokal_wiederholt` |
| `rekoppelnde_lage / rekoppelnde_lage / rekoppelnde_lage / bewegungsbruch / paarsegment_rekoppelnd` | 2 | 2 | 0.103243 | -0.023873 | `lokal_wiederholt` |
| `druck_lage / offene_lage / druck_lage / rekoppelnde_lage / kontaktsegment_offen` | 1 | 1 | -0.015293 | 0.0206 | `situationssegment` |
| `druck_lage / rekoppelnde_lage / druck_lage / bewegungsbruch / kontaktsegment_offen` | 1 | 1 | -0.076833 | -0.004621 | `situationssegment` |
| `druck_lage / rekoppelnde_lage / druck_lage / bewegungsbruch / paarsegment_spannungswechsel` | 1 | 1 | 0.141314 | -0.042826 | `situationssegment` |
| `druck_lage / rekoppelnde_lage / druck_lage / rekoppelnde_lage / paarsegment_spannungswechsel` | 1 | 1 | 0.050905 | -0.03663 | `situationssegment` |
| `offene_lage / bewegungsbruch / offene_lage / bewegungsbruch / kontaktsegment_offen` | 1 | 1 | -0.030912 | -0.014033 | `situationssegment` |
| `offene_lage / druck_lage / offene_lage / rekoppelnde_lage / kontaktsegment_offen` | 1 | 1 | -0.141199 | 0.00712 | `situationssegment` |
| `recurrently_opening_strain / - / - / - / paarsegment_spannungswechsel` | 1 | 1 | 0.02074 | -0.023905 | `situationssegment` |
| `recurrently_reconnecting / - / - / - / kontaktsegment_offen` | 1 | 1 | -0.016196 | 0.022663 | `situationssegment` |

## Befund

Wiederkehrende Kontaktsegmente sind keine neuen Regeln.
Sie markieren nur, welche lokale Achsenberuehrung in mehreren Welten erneut als Feldwirkung erscheint.

Arbeitsableitung:

```text
Aus einer lokalen Achsenberuehrung wird erst dann eine tragendere Bedeutungsnaehe,
wenn aehnliche Kontaktqualitaet ueber mehrere Weltlagen erneut erscheint.
```

## Wie es weitergeht

Als naechstes sollte die staerkste wiederkehrende Signatur gegen Nachbarschaft und Feldmitte gelesen werden.
