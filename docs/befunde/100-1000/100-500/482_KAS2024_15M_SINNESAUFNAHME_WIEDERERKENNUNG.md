# 482 - Kas2024 15M Sinnesaufnahme Wiedererkennung

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
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 418 | 0.5673 | 0.0000 | 0.1344 | 0.0637 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 390 | 0.5409 | 0.0000 | 0.1418 | 0.1087 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 198 | 0.5137 | 0.0000 | 0.1573 | 0.1151 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 127 | 0.5249 | 0.0000 | 0.1563 | 0.1215 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 127 | 0.4407 | 0.0000 | 0.1892 | 0.1389 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 117 | 0.4683 | 0.0000 | 0.1716 | 0.1881 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 102 | 0.4517 | 0.0000 | 0.1782 | 0.2048 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 62 | 0.3317 | 0.0000 | 0.2304 | 0.2940 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1jx2k4i | einzelspur | 1 | 60 | 0.5576 | 0.0000 | 0.1326 | 0.0629 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 54 | 0.4001 | 0.0000 | 0.2046 | 0.2114 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1jx2k4i | einzelspur | 1 | 46 | 0.5272 | 0.0000 | 0.1441 | 0.1044 |
| fuehlen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 32 | 0.3496 | 0.0000 | 0.2251 | 0.2360 |
| feldinput | inner_effect_stable | dio_mcm_episode_1jx2k4i | einzelspur | 1 | 17 | 0.4205 | 0.0000 | 0.1896 | 0.2095 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_1jx2k4i | einzelspur | 1 | 17 | 0.4812 | 0.0000 | 0.1661 | 0.1154 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_1jx2k4i | einzelspur | 1 | 12 | 0.2852 | 0.0000 | 0.2515 | 0.3168 |
| fuehlen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 12 | 0.4638 | 0.0000 | 0.1680 | 0.1613 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0mji3u6 | einzelspur | 1 | 11 | 0.5206 | 0.0000 | 0.1452 | 0.1137 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_1jx2k4i | einzelspur | 1 | 10 | 0.4442 | 0.0000 | 0.1838 | 0.1118 |

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
