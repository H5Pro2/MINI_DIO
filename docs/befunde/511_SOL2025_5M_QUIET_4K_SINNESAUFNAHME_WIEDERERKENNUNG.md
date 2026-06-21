# 511 - Sol2025 5M Quiet 4K Sinnesaufnahme Wiedererkennung

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
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 885 | 0.5726 | 0.0000 | 0.1327 | 0.0631 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 825 | 0.5494 | 0.0000 | 0.1391 | 0.1035 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 441 | 0.5173 | 0.0000 | 0.1566 | 0.1143 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 299 | 0.4582 | 0.0000 | 0.1840 | 0.1301 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 255 | 0.4715 | 0.0000 | 0.1716 | 0.1869 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 215 | 0.4521 | 0.0000 | 0.1790 | 0.2131 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 188 | 0.5269 | 0.0000 | 0.1553 | 0.1170 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 128 | 0.3520 | 0.0000 | 0.2233 | 0.2747 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 110 | 0.4169 | 0.0000 | 0.1992 | 0.2020 |
| fuehlen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 85 | 0.3637 | 0.0000 | 0.2207 | 0.2295 |
| hoeren_hin | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 27 | 0.5254 | 0.0000 | 0.1549 | 0.0687 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 24 | 0.5724 | 0.0000 | 0.1353 | 0.0630 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 24 | 0.5537 | 0.0000 | 0.1387 | 0.1041 |
| feldinput | inner_effect_tipping | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 23 | 0.1822 | 0.0000 | 0.2977 | 0.4132 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1joiyc3 | einzelspur | 1 | 22 | 0.5577 | 0.0000 | 0.1312 | 0.0582 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1joiyc3 | einzelspur | 1 | 20 | 0.5095 | 0.0000 | 0.1498 | 0.1153 |
| ausgeglichen | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 18 | 0.4895 | 0.0000 | 0.1729 | 0.1246 |
| fuehlen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 17 | 0.4520 | 0.0000 | 0.1755 | 0.1905 |

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
