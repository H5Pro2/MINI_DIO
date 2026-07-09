# 484 - Kas2024 1H Sinnesaufnahme Wiedererkennung

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
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 455 | 0.5665 | 0.0000 | 0.1343 | 0.0627 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 434 | 0.5421 | 0.0000 | 0.1408 | 0.1039 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 200 | 0.5090 | 0.0000 | 0.1584 | 0.1151 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 163 | 0.4442 | 0.0000 | 0.1887 | 0.1327 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 136 | 0.5250 | 0.0000 | 0.1557 | 0.1184 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 133 | 0.4687 | 0.0000 | 0.1727 | 0.1842 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 96 | 0.4423 | 0.0000 | 0.1829 | 0.2079 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 61 | 0.3262 | 0.0000 | 0.2329 | 0.2948 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 43 | 0.3992 | 0.0000 | 0.2050 | 0.2129 |
| fuehlen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 37 | 0.3518 | 0.0000 | 0.2264 | 0.2154 |
| feldinput | inner_effect_tipping | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 19 | 0.1738 | 0.0000 | 0.3020 | 0.4277 |
| hoeren_hin | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 10 | 0.5091 | 0.0000 | 0.1612 | 0.0825 |
| ausgeglichen | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 9 | 0.4876 | 0.0000 | 0.1707 | 0.1243 |
| fuehlen_abstand | inner_effect_tipping | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 9 | 0.1717 | 0.0000 | 0.3035 | 0.4035 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0198w46 | einzelspur | 1 | 8 | 0.5276 | 0.0000 | 0.1448 | 0.0636 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0mji3u6 | einzelspur | 1 | 7 | 0.5311 | 0.0000 | 0.1464 | 0.1196 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1jx2k4i | einzelspur | 1 | 7 | 0.4885 | 0.0000 | 0.1595 | 0.1087 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0mji3u6 | einzelspur | 1 | 6 | 0.5646 | 0.0000 | 0.1342 | 0.0621 |

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
