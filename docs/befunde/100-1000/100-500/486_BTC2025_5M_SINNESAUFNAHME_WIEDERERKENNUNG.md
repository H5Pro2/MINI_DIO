# 486 - Btc2025 5M Sinnesaufnahme Wiedererkennung

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
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 374 | 0.5639 | 0.0000 | 0.1342 | 0.0628 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 372 | 0.5406 | 0.0000 | 0.1412 | 0.1069 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 227 | 0.5126 | 0.0000 | 0.1567 | 0.1144 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 150 | 0.4414 | 0.0000 | 0.1896 | 0.1267 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 104 | 0.5233 | 0.0000 | 0.1563 | 0.1202 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 104 | 0.4607 | 0.0000 | 0.1747 | 0.1916 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 94 | 0.4404 | 0.0000 | 0.1829 | 0.2109 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1rxdw4p | einzelspur | 1 | 45 | 0.5514 | 0.0000 | 0.1371 | 0.1057 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 43 | 0.3878 | 0.0000 | 0.2076 | 0.2222 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 40 | 0.3338 | 0.0000 | 0.2300 | 0.2927 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1rxdw4p | einzelspur | 1 | 34 | 0.5686 | 0.0000 | 0.1358 | 0.0620 |
| feldinput | inner_effect_stable | dio_mcm_episode_1rxdw4p | einzelspur | 1 | 32 | 0.4585 | 0.0000 | 0.1737 | 0.2135 |
| fuehlen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 31 | 0.3520 | 0.0000 | 0.2248 | 0.2182 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0db07p4 | einzelspur | 1 | 19 | 0.5138 | 0.0000 | 0.1486 | 0.0944 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_1rxdw4p | einzelspur | 1 | 16 | 0.4632 | 0.0000 | 0.1731 | 0.1927 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1hdpu9s | einzelspur | 1 | 15 | 0.5778 | 0.0000 | 0.1291 | 0.0528 |
| feldinput | inner_effect_stable | dio_mcm_episode_0db07p4 | einzelspur | 1 | 12 | 0.4168 | 0.0000 | 0.1889 | 0.2109 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_1rxdw4p | einzelspur | 1 | 11 | 0.5369 | 0.0000 | 0.1505 | 0.1051 |

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
