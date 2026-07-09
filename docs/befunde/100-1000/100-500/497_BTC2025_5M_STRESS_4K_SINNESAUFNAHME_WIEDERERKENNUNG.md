# 497 - Btc2025 5M Stress 4K Sinnesaufnahme Wiedererkennung

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
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 640 | 0.5749 | 0.0000 | 0.1316 | 0.0602 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 619 | 0.5494 | 0.0000 | 0.1392 | 0.1054 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 365 | 0.5225 | 0.0000 | 0.1543 | 0.1102 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 219 | 0.4554 | 0.0000 | 0.1849 | 0.1255 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 193 | 0.5303 | 0.0000 | 0.1552 | 0.1162 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 165 | 0.4545 | 0.0000 | 0.1781 | 0.2101 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 165 | 0.4687 | 0.0000 | 0.1725 | 0.1918 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 138 | 0.5489 | 0.0000 | 0.1368 | 0.0985 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 137 | 0.5657 | 0.0000 | 0.1346 | 0.0618 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 88 | 0.3562 | 0.0000 | 0.2227 | 0.2735 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1rxdw4p | einzelspur | 1 | 87 | 0.5610 | 0.0000 | 0.1363 | 0.0955 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1rxdw4p | einzelspur | 1 | 85 | 0.5823 | 0.0000 | 0.1306 | 0.0588 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 67 | 0.4005 | 0.0000 | 0.2046 | 0.2202 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 50 | 0.4762 | 0.0000 | 0.1678 | 0.1842 |
| feldinput | inner_effect_stable | dio_mcm_episode_1rxdw4p | einzelspur | 1 | 49 | 0.4530 | 0.0000 | 0.1786 | 0.2168 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 49 | 0.5105 | 0.0000 | 0.1553 | 0.1060 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_1rxdw4p | einzelspur | 1 | 45 | 0.4849 | 0.0000 | 0.1644 | 0.1798 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 44 | 0.5314 | 0.0000 | 0.1511 | 0.1175 |

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
