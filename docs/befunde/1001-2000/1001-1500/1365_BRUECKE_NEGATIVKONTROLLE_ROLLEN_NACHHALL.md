# 1365 - Brueckenfunktion: Negativkontrolle Rollen-Nachhall

## Zweck

Diese Diagnose liest die Nachhallspur aus `1355` rollenbezogen.
Damit wird getrennt, ob Bruecke, Randdruck und Zentrumskontakt unterschiedlich weitertragen.

## Rollenbefund

| Rolle | Fenster | Preview weiter | Familie weiter | Rekopplung Delta | Strain Delta |
|---|---:|---:|---:|---:|---:|
| rueckbindung_in_normale_weltspannung | 17 | 12 | 13 | -0.001709 | 0.001794 |
| unklare_mikrophase | 3 | 2 | 1 | 0.003402 | -0.004912 |

## Interpretation

Die Nachhallspur ist rollenabhaengig zu lesen.
Preview-Gleichheit zeigt, ob ein lokaler Kontakt als gleiche MCM-Preview weiterliegt.
Familien-Gleichheit zeigt, ob die grobe `dio_*`-Familie weiterliegt.
Rekopplungs- und Straindelta zeigen, ob der Kontakt danach entlastet, stabilisiert oder belastet.

## Wie es weitergeht

Als naechstes sollte nur die staerkste Rollenlinie ausgewaehlt und gegen weitere Welten geprueft werden. Dadurch vermeiden wir Fragmentanalyse und testen gezielt, ob eine Feldfunktion reproduzierbar ist.
