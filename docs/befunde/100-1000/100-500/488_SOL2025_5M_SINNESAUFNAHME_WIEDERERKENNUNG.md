# 488 - Sol2025 5M Sinnesaufnahme Wiedererkennung

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
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 348 | 0.5682 | 0.0000 | 0.1334 | 0.0642 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 320 | 0.5412 | 0.0000 | 0.1410 | 0.1091 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 150 | 0.5108 | 0.0000 | 0.1580 | 0.1163 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 126 | 0.4479 | 0.0000 | 0.1879 | 0.1326 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1joiyc3 | einzelspur | 1 | 108 | 0.5479 | 0.0000 | 0.1389 | 0.0664 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 104 | 0.4723 | 0.0000 | 0.1705 | 0.1846 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 89 | 0.4476 | 0.0000 | 0.1798 | 0.2143 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 84 | 0.5265 | 0.0000 | 0.1543 | 0.1197 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1joiyc3 | einzelspur | 1 | 74 | 0.5165 | 0.0000 | 0.1480 | 0.1123 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_1joiyc3 | einzelspur | 1 | 61 | 0.5030 | 0.0000 | 0.1574 | 0.1104 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 51 | 0.3551 | 0.0000 | 0.2223 | 0.2649 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 41 | 0.4161 | 0.0000 | 0.1980 | 0.2013 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_1joiyc3 | einzelspur | 1 | 41 | 0.4447 | 0.0000 | 0.1873 | 0.1328 |
| fuehlen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 36 | 0.3349 | 0.0000 | 0.2327 | 0.2530 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 23 | 0.5792 | 0.0000 | 0.1284 | 0.0591 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_1joiyc3 | einzelspur | 1 | 23 | 0.4370 | 0.0000 | 0.1827 | 0.1957 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_1joiyc3 | einzelspur | 1 | 19 | 0.4055 | 0.0000 | 0.2009 | 0.1944 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_1joiyc3 | einzelspur | 1 | 16 | 0.5179 | 0.0000 | 0.1534 | 0.1137 |

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
