# 2038 - Feldfunktionswechsel Vorphasen-Klassen

## Zweck

Diese Diagnose verdichtet die Rohweltfenster vor Feldfunktionswechseln zu passiven Vorphasen-Klassen.

Geprüft wird, ob vor Öffnung und Rekopplung wiederkehrende Welt-, Sinnes- und Feldkontaktprofile sichtbar sind.

## Eingaben

- `lb48`
- `lb96`
- `lb144`

## Zusammenfassung

| Lookback | Gruppe | Kette | Ereignisse | dominante Rohphase | dominante Sinnesphase | dominanter Feldkontakt | MCM carry/strain/rekopplung |
|---|---|---|---:|---|---|---|---:|
| `lb144` | `oberflaeche_rekoppelt` | `long_btc_sol` | 41 | `weite_unruhige_vorphase_fallend` (0.39) | `sicht_zerfaellt_wechselnd_mittel` (0.22) | `offene_rekopplung` (0.66) | 0.410/0.231/0.616 |
| `lb144` | `oberflaeche_rekoppelt` | `multiasset` | 39 | `weite_unruhige_vorphase_steigend` (0.41) | `sicht_stabil_gedaempft_leise` (0.21) | `tragende_rekopplung` (0.59) | 0.425/0.210/0.633 |
| `lb144` | `oberflaeche_rekoppelt_spaet` | `long_btc_sol` | 22 | `enge_unruhige_vorphase_fallend` (0.23) | `sicht_zerfaellt_hoch_schwingend_laut` (0.50) | `offene_rekopplung` (0.95) | 0.378/0.268/0.590 |
| `lb144` | `oberflaeche_rekoppelt_spaet` | `multiasset` | 24 | `weite_unruhige_vorphase_fallend` (0.38) | `sicht_zerfaellt_hoch_schwingend_laut` (0.54) | `offene_rekopplung` (0.83) | 0.375/0.270/0.590 |
| `lb144` | `rekopplung_oeffnet` | `long_btc_sol` | 112 | `enge_unruhige_vorphase_fallend` (0.29) | `sicht_zerfaellt_hoch_schwingend_laut` (0.61) | `spannungsnahe_oeffnung` (0.69) | 0.370/0.286/0.581 |
| `lb144` | `rekopplung_oeffnet` | `multiasset` | 66 | `weite_unruhige_vorphase_steigend` (0.32) | `sicht_zerfaellt_hoch_schwingend_laut` (0.62) | `spannungsnahe_oeffnung` (0.76) | 0.367/0.287/0.581 |
| `lb48` | `oberflaeche_rekoppelt` | `long_btc_sol` | 41 | `weite_unruhige_vorphase_fallend` (0.29) | `sicht_zerfaellt_wechselnd_mittel` (0.22) | `offene_rekopplung` (0.66) | 0.410/0.231/0.616 |
| `lb48` | `oberflaeche_rekoppelt` | `multiasset` | 39 | `enge_unruhige_vorphase_steigend` (0.33) | `sicht_stabil_gedaempft_leise` (0.21) | `tragende_rekopplung` (0.59) | 0.425/0.210/0.633 |
| `lb48` | `oberflaeche_rekoppelt_spaet` | `long_btc_sol` | 22 | `enge_unruhige_vorphase_steigend` (0.41) | `sicht_zerfaellt_hoch_schwingend_laut` (0.50) | `offene_rekopplung` (0.95) | 0.378/0.268/0.590 |
| `lb48` | `oberflaeche_rekoppelt_spaet` | `multiasset` | 24 | `weite_unruhige_vorphase_fallend` (0.33) | `sicht_zerfaellt_hoch_schwingend_laut` (0.54) | `offene_rekopplung` (0.83) | 0.375/0.270/0.590 |
| `lb48` | `rekopplung_oeffnet` | `long_btc_sol` | 112 | `enge_unruhige_vorphase_steigend` (0.31) | `sicht_zerfaellt_hoch_schwingend_laut` (0.61) | `spannungsnahe_oeffnung` (0.69) | 0.370/0.286/0.581 |
| `lb48` | `rekopplung_oeffnet` | `multiasset` | 66 | `weite_unruhige_vorphase_fallend` (0.26) | `sicht_zerfaellt_hoch_schwingend_laut` (0.62) | `spannungsnahe_oeffnung` (0.76) | 0.367/0.287/0.581 |
| `lb96` | `oberflaeche_rekoppelt` | `long_btc_sol` | 41 | `weite_unruhige_vorphase_fallend` (0.39) | `sicht_zerfaellt_wechselnd_mittel` (0.22) | `offene_rekopplung` (0.66) | 0.410/0.231/0.616 |
| `lb96` | `oberflaeche_rekoppelt` | `multiasset` | 39 | `enge_unruhige_vorphase_steigend` (0.33) | `sicht_stabil_gedaempft_leise` (0.21) | `tragende_rekopplung` (0.59) | 0.425/0.210/0.633 |
| `lb96` | `oberflaeche_rekoppelt_spaet` | `long_btc_sol` | 22 | `enge_unruhige_vorphase_fallend` (0.27) | `sicht_zerfaellt_hoch_schwingend_laut` (0.50) | `offene_rekopplung` (0.95) | 0.378/0.268/0.590 |
| `lb96` | `oberflaeche_rekoppelt_spaet` | `multiasset` | 24 | `weite_unruhige_vorphase_fallend` (0.33) | `sicht_zerfaellt_hoch_schwingend_laut` (0.54) | `offene_rekopplung` (0.83) | 0.375/0.270/0.590 |
| `lb96` | `rekopplung_oeffnet` | `long_btc_sol` | 112 | `enge_unruhige_vorphase_fallend` (0.33) | `sicht_zerfaellt_hoch_schwingend_laut` (0.61) | `spannungsnahe_oeffnung` (0.69) | 0.370/0.286/0.581 |
| `lb96` | `rekopplung_oeffnet` | `multiasset` | 66 | `weite_unruhige_vorphase_fallend` (0.26) | `sicht_zerfaellt_hoch_schwingend_laut` (0.62) | `spannungsnahe_oeffnung` (0.76) | 0.367/0.287/0.581 |

## Lesung

Die Vorphasen-Klassen trennen drei Ebenen:

- Rohweltbewegung: wie breit, unruhig oder gerichtet das vorherige Fenster ist
- Sinnesprofil: ob Sehen/Hören stabil, wechselnd, hoch schwingend oder gedämpft wirken
- Feldkontakt: ob der Kontakt tragend rekoppelt oder spannungsnah öffnet

Damit wird der Rollenwechsel nicht als isolierter Moment gelesen, sondern als Kontaktpunkt nach einer passiven Vorphase.

## Bedeutung für DIO

DIO kann daraus später eine organische Vorwahrnehmung entwickeln: nicht handeln, sondern merken, welche Vorphase typischerweise zu Öffnung oder Rekopplung führt.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob diese Vorphasen-Klassen über weitere Weltkörper stabil bleiben oder ob Asset-spezifische Vorphasen entstehen.
