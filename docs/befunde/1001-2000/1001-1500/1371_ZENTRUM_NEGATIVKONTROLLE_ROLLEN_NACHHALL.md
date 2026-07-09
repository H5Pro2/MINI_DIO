# 1371 - Zentrumskontakt: Negativkontrolle Rollen-Nachhall

## Zweck

Diese Diagnose liest die Nachhallspur aus `1370` rollenbezogen.
Damit wird getrennt, wie die Kontrollfenster weitertragen, wenn die volle Zentrumslagefolge fehlt.

## Rollenbefund

| Rolle | Fenster | Preview weiter | Familie weiter | Rekopplung Delta | Strain Delta |
|---|---:|---:|---:|---:|---:|
| brueckenuebergang_zum_lauten_kontakt | 7 | 4 | 4 | -0.000385 | -0.000615 |
| lauter_kontakt_bleibt_offen | 1 | 1 | 1 | -0.001150 | -0.002441 |
| offener_uebergang_zum_lauten_kontakt | 4 | 2 | 4 | 0.003156 | -0.003601 |
| rueckbindung_in_normale_weltspannung | 7 | 6 | 6 | -0.003639 | 0.003743 |

## Interpretation

Die Nachhallspur ist rollenabhaengig zu lesen.
Preview-Gleichheit zeigt, ob ein lokaler Kontakt als gleiche MCM-Preview weiterliegt.
Familien-Gleichheit zeigt, ob die grobe `dio_*`-Familie weiterliegt.
Rekopplungs- und Straindelta zeigen, ob der Kontakt danach entlastet, stabilisiert oder belastet.
