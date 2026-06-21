# 481 - Kas2024 5M Sinnesaufnahme Wiedererkennung

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
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 287 | 0.5692 | 0.0000 | 0.1336 | 0.0619 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 277 | 0.5405 | 0.0000 | 0.1423 | 0.1111 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1jx2k4i | einzelspur | 1 | 154 | 0.5617 | 0.0000 | 0.1347 | 0.0637 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1jx2k4i | einzelspur | 1 | 137 | 0.5331 | 0.0000 | 0.1429 | 0.1054 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 133 | 0.5127 | 0.0000 | 0.1570 | 0.1166 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 118 | 0.4506 | 0.0000 | 0.1872 | 0.1264 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 73 | 0.5248 | 0.0000 | 0.1564 | 0.1188 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 68 | 0.4743 | 0.0000 | 0.1693 | 0.1847 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 64 | 0.4567 | 0.0000 | 0.1759 | 0.2098 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_1jx2k4i | einzelspur | 1 | 58 | 0.5026 | 0.0000 | 0.1586 | 0.1140 |
| feldinput | inner_effect_stable | dio_mcm_episode_1jx2k4i | einzelspur | 1 | 53 | 0.4480 | 0.0000 | 0.1784 | 0.2011 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_1jx2k4i | einzelspur | 1 | 43 | 0.4591 | 0.0000 | 0.1756 | 0.1876 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 42 | 0.3361 | 0.0000 | 0.2288 | 0.2907 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_1jx2k4i | einzelspur | 1 | 41 | 0.5224 | 0.0000 | 0.1529 | 0.1163 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 36 | 0.3841 | 0.0000 | 0.2119 | 0.2274 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_1jx2k4i | einzelspur | 1 | 24 | 0.3115 | 0.0000 | 0.2380 | 0.3067 |
| fuehlen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | einzelspur | 1 | 24 | 0.3829 | 0.0000 | 0.2132 | 0.2036 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0mji3u6 | einzelspur | 1 | 24 | 0.5600 | 0.0000 | 0.1327 | 0.0576 |

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
