# 487 - Btc2025 1H Sinnesaufnahme Wiedererkennung

## Fragestellung

Kann MINI_DIO Aufnahmequalitaeten wiedererkennen, ohne daraus Handlung oder Regel zu machen?

Geprueft wird die kleinste passive Signatur:

```text
Aufnahmeachse + Innenfeldzustand + MCM-Preview
```

Wenn diese Signatur ueber mehrere Welten mit aehnlicher Feldwirkung wiederkehrt, ist sie eine passive Lernspur.

## Kurzbefund

- Wiederkehrende Signaturen mit mindestens drei Welten: 0.
- Reproduzierte ruhige Aufnahmen: 0.

## Staerkste Wiedererkennungen

| Achse | Innenfeld | Preview | Label | Welten | Count | Balance | Streuung | Strain | Feldinput |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 321 | 0.5728 | 0.0000 | 0.1329 | 0.0593 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 263 | 0.5501 | 0.0000 | 0.1388 | 0.0970 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 141 | 0.5209 | 0.0000 | 0.1541 | 0.1030 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 100 | 0.4381 | 0.0000 | 0.1902 | 0.1315 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 97 | 0.5378 | 0.0000 | 0.1514 | 0.1101 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 85 | 0.4716 | 0.0000 | 0.1703 | 0.1797 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 67 | 0.4489 | 0.0000 | 0.1791 | 0.2049 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 67 | 0.5683 | 0.0000 | 0.1357 | 0.0625 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 65 | 0.5551 | 0.0000 | 0.1363 | 0.0901 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1ahj81f | einzelspur | 1 | 54 | 0.5429 | 0.0000 | 0.1376 | 0.0868 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1q3us3f | einzelspur | 1 | 50 | 0.5813 | 0.0000 | 0.1321 | 0.0579 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1ahj81f | einzelspur | 1 | 42 | 0.5525 | 0.0000 | 0.1380 | 0.0687 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 37 | 0.3106 | 0.0000 | 0.2386 | 0.3153 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1q3us3f | einzelspur | 1 | 32 | 0.5618 | 0.0000 | 0.1350 | 0.1000 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 25 | 0.5293 | 0.0000 | 0.1522 | 0.1210 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 25 | 0.5228 | 0.0000 | 0.1540 | 0.1100 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 20 | 0.4881 | 0.0000 | 0.1665 | 0.1630 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_1q3us3f | einzelspur | 1 | 20 | 0.4804 | 0.0000 | 0.1688 | 0.1812 |

## Interpretation

Die staerksten Wiedererkennungen liegen nicht in beliebigen Rohwerten, sondern in wiederkehrenden Kombinationen aus Aufnahmeachse, Innenfeldzustand und MCM-Preview. Damit wird Aufnahmequalitaet als passive Spur lesbar.

`hoeren_hin + inner_effect_stable` bildet die ruhigste wiederkehrende Spur. `sehen_fokus + inner_effect_stable` liegt nahe daran und traegt Form stabiler. `feldinput` erscheint ebenfalls wiederkehrend, aber mit mehr Strain und Kontaktlast.

Das ist der wichtige Schnitt: MINI_DIO lernt hier nicht 'was zu tun ist'. MINI_DIO sammelt, welche Art von Weltaufnahme welche MCM-Feldwirkung wiederholt erzeugt.

## Mechanische Bedeutung

Diese Ebene ist der Uebergang von Diagnose zu passiver Lernspur:

```text
gleiche/aehnliche Weltlage
  -> gleiche Aufnahmeart
  -> aehnliche MCM-Feldwirkung
  -> wiedererkennbare Innenfeldspur
```

Sie bleibt vor Handlung, vor Gate und vor Strategie.

## Wie es weitergeht

Als naechstes sollte diese Wiedererkennung in eine kleine passive Intake-Memory ueberfuehrt werden: nicht zur Steuerung, sondern um zu speichern, welche Aufnahmeart in welcher Innenfeldlage wiederholt getragen oder belastet war.
