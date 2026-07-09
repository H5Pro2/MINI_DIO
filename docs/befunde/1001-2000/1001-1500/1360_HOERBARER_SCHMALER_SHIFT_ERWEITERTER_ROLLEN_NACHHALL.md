# 1360 - Hoerbarer schmaler Shift: Erweiterter Rollen-Nachhall

## Zweck

Diese Diagnose liest die Nachhallspur aus `1355` rollenbezogen.
Damit wird getrennt, ob Bruecke, Randdruck und Zentrumskontakt unterschiedlich weitertragen.

## Rollenbefund

| Rolle | Fenster | Preview weiter | Familie weiter | Rekopplung Delta | Strain Delta |
|---|---:|---:|---:|---:|---:|
| brueckenuebergang_zum_lauten_kontakt | 10 | 8 | 4 | 0.001448 | -0.001295 |
| lauter_kontakt_bleibt_offen | 4 | 4 | 0 | -0.001737 | 0.003102 |
| offener_uebergang_zum_lauten_kontakt | 1 | 0 | 0 | -0.002341 | -0.000174 |
| randnaher_kontaktdruck | 8 | 5 | 2 | -0.263374 | -0.062453 |
| rueckbindung_in_normale_weltspannung | 4 | 3 | 4 | 0.002578 | -0.001953 |
| zentrumskontakt_mit_hoeranstieg | 7 | 7 | 4 | 0.001345 | -0.000733 |
| zentrumskontakt_wird_aktiviert | 2 | 1 | 0 | 0.002393 | 0.003518 |

## Interpretation

Die Nachhallspur ist rollenabhaengig zu lesen.
Preview-Gleichheit zeigt, ob ein lokaler Kontakt als gleiche MCM-Preview weiterliegt.
Familien-Gleichheit zeigt, ob die grobe `dio_*`-Familie weiterliegt.
Rekopplungs- und Straindelta zeigen, ob der Kontakt danach entlastet, stabilisiert oder belastet.
