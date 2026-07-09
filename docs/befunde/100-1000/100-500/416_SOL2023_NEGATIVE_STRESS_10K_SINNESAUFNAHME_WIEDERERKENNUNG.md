# 416 - Sol2023 Negative Stress 10K Sinnesaufnahme Wiedererkennung

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
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 1724 | 0.5772 | 0.0000 | 0.1327 | 0.0611 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 1614 | 0.5536 | 0.0000 | 0.1391 | 0.1041 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 995 | 0.5235 | 0.0000 | 0.1557 | 0.1136 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 635 | 0.4571 | 0.0000 | 0.1858 | 0.1285 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 522 | 0.4784 | 0.0000 | 0.1703 | 0.1859 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 460 | 0.5340 | 0.0000 | 0.1542 | 0.1147 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 430 | 0.4628 | 0.0000 | 0.1764 | 0.2079 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 239 | 0.3497 | 0.0000 | 0.2249 | 0.2910 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0gqol8d | einzelspur | 1 | 192 | 0.5826 | 0.0000 | 0.1332 | 0.0578 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 163 | 0.4198 | 0.0000 | 0.1990 | 0.2074 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 150 | 0.5777 | 0.0000 | 0.1329 | 0.0585 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 150 | 0.5514 | 0.0000 | 0.1389 | 0.0998 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0gqol8d | einzelspur | 1 | 140 | 0.5700 | 0.0000 | 0.1346 | 0.0944 |
| fuehlen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 135 | 0.3816 | 0.0000 | 0.2149 | 0.2082 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1jwnjz4 | einzelspur | 1 | 111 | 0.5833 | 0.0000 | 0.1343 | 0.0598 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1jx2k4i | einzelspur | 1 | 105 | 0.5595 | 0.0000 | 0.1357 | 0.0603 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1jx2k4i | einzelspur | 1 | 96 | 0.5338 | 0.0000 | 0.1432 | 0.1004 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1jwnjz4 | einzelspur | 1 | 83 | 0.5644 | 0.0000 | 0.1365 | 0.0980 |

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
