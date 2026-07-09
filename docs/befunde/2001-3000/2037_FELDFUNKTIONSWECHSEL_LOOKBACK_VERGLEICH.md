# 2037 - Feldfunktionswechsel Lookback-Vergleich

## Zweck

Dieser Bericht vergleicht die Rohweltfenster-Lupe mit mehreren Lookback-Längen.

Geprüft wird, ob Öffnung und Rekopplung nur direkt am Signaturmoment sichtbar sind oder bereits in einem längeren Weltfenster unterscheidbare Profile tragen.

## Eingaben

- `lb48`
- `lb96`
- `lb144`

## Vergleich

| Gruppe | Kette | Range 48/96/144 | Wechsel 48/96/144 | MCM 48 | MCM 144 | Wachstum Range/Wechsel | MCM-Delta |
|---|---|---:|---:|---:|---:|---:|---:|
| `oberflaeche_rekoppelt` | `long_btc_sol` | 5.697 / 6.424 / 7.417 | 23.37 / 48.05 / 72.80 | 0.410/0.231/0.616 | 0.410/0.231/0.616 | 1.720/49.44 | 0.000/0.000/0.000 |
| `oberflaeche_rekoppelt` | `multiasset` | 5.102 / 6.129 / 7.665 | 22.59 / 44.13 / 64.67 | 0.425/0.210/0.633 | 0.425/0.210/0.633 | 2.563/42.08 | 0.000/0.000/0.000 |
| `oberflaeche_rekoppelt_spaet` | `long_btc_sol` | 2.376 / 3.662 / 4.394 | 22.32 / 47.05 / 72.73 | 0.378/0.268/0.590 | 0.378/0.268/0.590 | 2.018/50.41 | 0.000/0.000/0.000 |
| `oberflaeche_rekoppelt_spaet` | `multiasset` | 4.288 / 5.471 / 6.409 | 21.50 / 43.33 / 62.21 | 0.375/0.270/0.590 | 0.375/0.270/0.590 | 2.121/40.71 | 0.000/0.000/0.000 |
| `rekopplung_oeffnet` | `long_btc_sol` | 2.340 / 3.377 / 4.221 | 23.48 / 47.30 / 70.59 | 0.370/0.286/0.581 | 0.370/0.286/0.581 | 1.882/47.11 | 0.000/0.000/0.000 |
| `rekopplung_oeffnet` | `multiasset` | 3.231 / 4.587 / 6.465 | 21.18 / 44.20 / 65.00 | 0.367/0.287/0.581 | 0.367/0.287/0.581 | 3.234/43.82 | 0.000/0.000/0.000 |

## Befund

Die Rohwelt wird mit längerem Lookback erwartbar breiter: Range und Richtungswechsel steigen deutlich.

Die MCM-Werte der Gruppen bleiben dagegen praktisch stabil, weil sie am Signaturmoment gemessen werden. Damit sind Öffnung und Rekopplung nicht nur Ergebnis eines beliebig längeren Fensters, sondern an konkrete Feldzustände am Kontaktpunkt gebunden.

Wichtig ist die Trennung:

- längerer Lookback zeigt mehr Vorgeschichte und Weltunruhe
- der eigentliche Rollenwechsel bleibt im MCM-Profil unterscheidbar

## Lesung für DIO

DIO braucht keine harte Vorhersage aus langer Historie.

Sinnvoller ist eine zweistufige Feldlesung: Vorgeschichte als Weltphase lesen, den Rollenwechsel aber am aktuellen Feldkontakt prüfen.
