# MCM-Zentrumsachse: Signatur, Nachbarschaft und Feldmitte

## Zweck

Diese Datei liest die staerkste wiederkehrende Kontaktsegment-Signatur gegen Nachbarschaft und Feldmitte.

## Sicherheitsgrenze

- passive Ruecklesung
- keine Handlung
- kein Gate
- keine Strategie

## Achsenprofil

- Achse: `183drjy<->1t5bcxp`
- Signatur: `rekoppelnde_lage / rekoppelnde_lage / rekoppelnde_lage / rekoppelnde_lage / paarsegment_rekoppelnd`
- Wiederkehr: 14 Kontakte ueber 4 Welten
- Signatur-Welten: `EXT_EXPANSION_2023:5 | POS_EXPANSION_2023:4 | NEG_STRESS_2023:3 | SIDEWAYS_2024:2`
- Pressure-Delta: 0.024289
- Rekopplung-Delta: -0.004694

## Knotenprofile

| Knoten | Klasse | Zone | Rolle | Top Previous | Top Next | Rekopplung | Strain |
|---|---|---|---|---|---|---:|---:|
| `183drjy` | `nichtbruecke_rekopplungsfeld:2` | `rekopplungszone:2` | `zentrum_stabil:2` | `1t5bcxp:2` | `1t5bcxp:2` | 0.658507 | 0.170051 |
| `1t5bcxp` | `nichtbruecke_zentrum_schwach:2` | `stabile_bedeutungsinsel:1 \| rekopplungszone:1` | `zentrum_stabil:2` | `183drjy:2` | `183drjy:2` | 0.648956 | 0.183806 |

## Gemeinsame Feldnaehe

- Rollenbelege: `spannungsrand_kippnaehe:136 | zentrum_stabil:72 | offene_variante:4`
- Zonenbelege: `junge_spur:92 | nichtbruecke_randspannung:70 | rekopplungszone:60 | randnahe_verdichtung:48 | nichtbruecke_zentrum_schwach:24`
- Lesung: `rekopplungsfeld_zu_stabiler_bedeutungsinsel`

## Befund

Die dominante rekoppelnde Kontaktsegment-Signatur verbindet keine starre Kante,
sondern ein Rekopplungsfeld mit einer zentrumsnahen stabilen Bedeutungsinsel.

Arbeitsableitung:

```text
Die Achse wirkt wie eine lokale Mitte-Nachbarschaft:
ein Knoten traegt Rekopplungsfeld, der andere traegt zentrumsnahe Stabilitaet.
```

## Wie es weitergeht

Als naechstes sollte diese Mitte-Nachbarschaft gegen neue Folgewelten geprueft werden: bleibt die Beziehung erhalten oder verlagert sie sich erneut?
