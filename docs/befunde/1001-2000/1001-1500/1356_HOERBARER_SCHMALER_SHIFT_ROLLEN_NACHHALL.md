# 1356 - Hoerbarer schmaler Shift: Rollen-Nachhall

## Zweck

Diese Diagnose liest die Nachhallspur aus `1355` rollenbezogen.
Damit wird getrennt, ob Bruecke, Randdruck und Zentrumskontakt unterschiedlich weitertragen.

## Rollenbefund

| Rolle | Fenster | Preview weiter | Familie weiter | Rekopplung Delta | Strain Delta |
|---|---:|---:|---:|---:|---:|
| brueckenuebergang_zum_lauten_kontakt | 4 | 4 | 2 | 0.003469 | -0.003952 |
| lauter_kontakt_bleibt_offen | 1 | 1 | 0 | 0.002155 | 0.000469 |
| randnaher_kontaktdruck | 5 | 4 | 2 | -0.138072 | -0.036498 |
| zentrumskontakt_mit_hoeranstieg | 5 | 5 | 2 | 0.000913 | 0.000006 |
| zentrumskontakt_wird_aktiviert | 2 | 1 | 0 | 0.002393 | 0.003518 |

## Interpretation

Die Nachhallspur ist rollenabhaengig zu lesen.
Preview-Gleichheit zeigt, ob ein lokaler Kontakt als gleiche MCM-Preview weiterliegt.
Familien-Gleichheit zeigt, ob die grobe `dio_*`-Familie weiterliegt.
Rekopplungs- und Straindelta zeigen, ob der Kontakt danach entlastet, stabilisiert oder belastet.
