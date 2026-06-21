# 483 - Kas2024 30M Sinnesaufnahme Wiedererkennung

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
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 430 | 0.5677 | 0.0000 | 0.1342 | 0.0638 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 404 | 0.5385 | 0.0000 | 0.1421 | 0.1069 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 190 | 0.5117 | 0.0000 | 0.1574 | 0.1138 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 159 | 0.4337 | 0.0000 | 0.1930 | 0.1386 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 144 | 0.5254 | 0.0000 | 0.1543 | 0.1189 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 127 | 0.4424 | 0.0000 | 0.1812 | 0.2126 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 116 | 0.4660 | 0.0000 | 0.1725 | 0.1918 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 62 | 0.3293 | 0.0000 | 0.2318 | 0.2953 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 38 | 0.4068 | 0.0000 | 0.2015 | 0.2062 |
| fuehlen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 29 | 0.3459 | 0.0000 | 0.2275 | 0.2425 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1jx2k4i | einzelspur | 1 | 22 | 0.5277 | 0.0000 | 0.1441 | 0.0665 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1jx2k4i | einzelspur | 1 | 17 | 0.5027 | 0.0000 | 0.1509 | 0.1198 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 15 | 0.5714 | 0.0000 | 0.1310 | 0.0831 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 13 | 0.5616 | 0.0000 | 0.1427 | 0.0718 |
| feldinput | inner_effect_tipping | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 12 | 0.1812 | 0.0000 | 0.2980 | 0.4148 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_1jx2k4i | einzelspur | 1 | 11 | 0.4712 | 0.0000 | 0.1698 | 0.1049 |
| sehen_fokus | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 10 | 0.4711 | 0.0000 | 0.1790 | 0.1324 |
| ausgeglichen | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 9 | 0.4876 | 0.0000 | 0.1716 | 0.1239 |

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
