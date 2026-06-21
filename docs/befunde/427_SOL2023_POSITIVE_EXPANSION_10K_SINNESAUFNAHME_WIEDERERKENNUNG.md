# 427 - Sol2023 Positive Expansion 10K Sinnesaufnahme Wiedererkennung

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
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 1519 | 0.5554 | 0.0000 | 0.1380 | 0.1051 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 1460 | 0.5779 | 0.0000 | 0.1321 | 0.0611 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 891 | 0.5238 | 0.0000 | 0.1552 | 0.1112 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 664 | 0.4576 | 0.0000 | 0.1856 | 0.1293 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 450 | 0.4798 | 0.0000 | 0.1702 | 0.1875 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 398 | 0.5820 | 0.0000 | 0.1312 | 0.0577 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 377 | 0.5318 | 0.0000 | 0.1551 | 0.1167 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 356 | 0.4605 | 0.0000 | 0.1770 | 0.2128 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 343 | 0.5596 | 0.0000 | 0.1362 | 0.0987 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 225 | 0.3583 | 0.0000 | 0.2219 | 0.2856 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1rxdw4p | einzelspur | 1 | 203 | 0.5846 | 0.0000 | 0.1305 | 0.0562 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1rxdw4p | einzelspur | 1 | 173 | 0.5636 | 0.0000 | 0.1356 | 0.0958 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 151 | 0.4176 | 0.0000 | 0.2001 | 0.2109 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 149 | 0.5381 | 0.0000 | 0.1506 | 0.1165 |
| fuehlen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 138 | 0.3834 | 0.0000 | 0.2146 | 0.2091 |
| feldinput | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 133 | 0.4570 | 0.0000 | 0.1773 | 0.2101 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 133 | 0.5240 | 0.0000 | 0.1551 | 0.1147 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 132 | 0.4699 | 0.0000 | 0.1731 | 0.1930 |

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
