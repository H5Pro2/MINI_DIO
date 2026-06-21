# 411 - Btc2024 5M Quiet Sinnesaufnahme Wiedererkennung

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
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 695 | 0.5709 | 0.0000 | 0.1337 | 0.0626 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 685 | 0.5495 | 0.0000 | 0.1388 | 0.1028 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 363 | 0.5181 | 0.0000 | 0.1558 | 0.1110 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 281 | 0.4601 | 0.0000 | 0.1833 | 0.1222 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 203 | 0.4707 | 0.0000 | 0.1723 | 0.1898 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 179 | 0.4563 | 0.0000 | 0.1767 | 0.2083 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 168 | 0.5314 | 0.0000 | 0.1536 | 0.1149 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 96 | 0.5635 | 0.0000 | 0.1363 | 0.0626 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 91 | 0.3335 | 0.0000 | 0.2298 | 0.2961 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 85 | 0.5408 | 0.0000 | 0.1392 | 0.1039 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 64 | 0.4158 | 0.0000 | 0.1992 | 0.1987 |
| fuehlen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 60 | 0.3788 | 0.0000 | 0.2137 | 0.2100 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1rxdw4p | einzelspur | 1 | 55 | 0.5628 | 0.0000 | 0.1337 | 0.0965 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1rxdw4p | einzelspur | 1 | 45 | 0.5824 | 0.0000 | 0.1292 | 0.0581 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 36 | 0.5182 | 0.0000 | 0.1516 | 0.1057 |
| feldinput | inner_effect_stable | dio_mcm_episode_1rxdw4p | einzelspur | 1 | 33 | 0.4509 | 0.0000 | 0.1792 | 0.2203 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 23 | 0.5226 | 0.0000 | 0.1547 | 0.1211 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_1rxdw4p | einzelspur | 1 | 23 | 0.5368 | 0.0000 | 0.1504 | 0.1177 |

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
