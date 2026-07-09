# 1376 - Randdruck: Negativkontrolle Rollen-Nachhall

## Zweck

Diese Diagnose liest die Nachhallspur aus `1375` rollenbezogen.
Damit wird getrennt, wie die Randdruck-Kontrollfenster weitertragen, wenn eine Randdruck-Komponente fehlt.

## Rollenbefund

| Rolle | Fenster | Preview weiter | Familie weiter | Rekopplung Delta | Strain Delta |
|---|---:|---:|---:|---:|---:|
| brueckenuebergang_zum_lauten_kontakt | 2 | 2 | 1 | 0.004998 | -0.004333 |
| lauter_kontakt_bleibt_offen | 4 | 4 | 0 | -0.001737 | 0.003102 |

## Interpretation

Die Nachhallspur ist rollenabhaengig zu lesen.
Preview-Gleichheit zeigt, ob ein lokaler Kontakt als gleiche MCM-Preview weiterliegt.
Familien-Gleichheit zeigt, ob die grobe `dio_*`-Familie weiterliegt.
Rekopplungs- und Straindelta zeigen, ob der Kontakt danach entlastet, stabilisiert oder belastet.
