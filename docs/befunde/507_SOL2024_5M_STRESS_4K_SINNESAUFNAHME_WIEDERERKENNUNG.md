# 507 - Sol2024 5M Stress 4K Sinnesaufnahme Wiedererkennung

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
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 867 | 0.5720 | 0.0000 | 0.1333 | 0.0619 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 812 | 0.5474 | 0.0000 | 0.1399 | 0.1080 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 399 | 0.5156 | 0.0000 | 0.1568 | 0.1132 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 288 | 0.4587 | 0.0000 | 0.1843 | 0.1253 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 254 | 0.4713 | 0.0000 | 0.1718 | 0.1871 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 235 | 0.5290 | 0.0000 | 0.1553 | 0.1160 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 206 | 0.4543 | 0.0000 | 0.1780 | 0.2070 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 131 | 0.3490 | 0.0000 | 0.2253 | 0.2803 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 82 | 0.4056 | 0.0000 | 0.2043 | 0.2132 |
| fuehlen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 60 | 0.3698 | 0.0000 | 0.2192 | 0.2242 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1joiyc3 | einzelspur | 1 | 52 | 0.5555 | 0.0000 | 0.1382 | 0.0657 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0mji3u6 | einzelspur | 1 | 35 | 0.5454 | 0.0000 | 0.1404 | 0.0993 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1joiyc3 | einzelspur | 1 | 31 | 0.5201 | 0.0000 | 0.1470 | 0.1117 |
| hoeren_hin | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 26 | 0.5221 | 0.0000 | 0.1558 | 0.0689 |
| feldinput | inner_effect_tipping | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 20 | 0.1773 | 0.0000 | 0.2997 | 0.4230 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1jx2k4i | einzelspur | 1 | 20 | 0.5550 | 0.0000 | 0.1359 | 0.0678 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1jx2k4i | einzelspur | 1 | 20 | 0.5211 | 0.0000 | 0.1458 | 0.0938 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0mji3u6 | einzelspur | 1 | 19 | 0.5175 | 0.0000 | 0.1525 | 0.1082 |

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
