# 408 - Sinnesaufnahme Wiedererkennung

## Fragestellung

Kann MINI_DIO Aufnahmequalitaeten wiedererkennen, ohne daraus Handlung oder Regel zu machen?

Geprueft wird die kleinste passive Signatur:

```text
Aufnahmeachse + Innenfeldzustand + MCM-Preview
```

Wenn diese Signatur ueber mehrere Welten mit aehnlicher Feldwirkung wiederkehrt, ist sie eine passive Lernspur.

## Kurzbefund

- Wiederkehrende Signaturen mit mindestens drei Welten: 51.
- Reproduzierte ruhige Aufnahmen: 6.

## Staerkste Wiedererkennungen

| Achse | Innenfeld | Preview | Label | Welten | Count | Balance | Streuung | Strain | Feldinput |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | reproduzierte_ruhige_aufnahme | 4 | 1411 | 0.5689 | 0.0023 | 0.1336 | 0.0622 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | reproduzierte_ruhige_aufnahme | 4 | 1294 | 0.5432 | 0.0036 | 0.1408 | 0.1053 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | wiederkehrend_tragend | 4 | 624 | 0.5129 | 0.0045 | 0.1571 | 0.1130 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | wiederkehrend_offen | 4 | 507 | 0.4454 | 0.0044 | 0.1884 | 0.1310 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | reproduzierte_ruhige_aufnahme | 4 | 390 | 0.5285 | 0.0054 | 0.1545 | 0.1167 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | wiederkehrend_offen | 4 | 390 | 0.4712 | 0.0020 | 0.1710 | 0.1834 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | wiederkehrend_kontaktlastig | 4 | 316 | 0.4481 | 0.0051 | 0.1798 | 0.2095 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | wiederkehrend_kontaktlastig | 4 | 191 | 0.3331 | 0.0156 | 0.2303 | 0.2899 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1jx2k4i | reproduzierte_ruhige_aufnahme | 4 | 156 | 0.5319 | 0.0120 | 0.1432 | 0.1037 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | wiederkehrend_kontaktlastig | 4 | 138 | 0.4013 | 0.0122 | 0.2042 | 0.2125 |
| fuehlen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | wiederkehrend_kontaktlastig | 4 | 114 | 0.3564 | 0.0187 | 0.2239 | 0.2224 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_1jx2k4i | wiederkehrend_tragend | 4 | 65 | 0.4976 | 0.0151 | 0.1607 | 0.1150 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0mji3u6 | reproduzierte_ruhige_aufnahme | 4 | 49 | 0.5616 | 0.0044 | 0.1322 | 0.0595 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_1jx2k4i | wiederkehrend_tragend | 4 | 46 | 0.5193 | 0.0120 | 0.1536 | 0.1171 |
| feldinput | inner_effect_tipping | dio_mcm_episode_0e7qvj1 | wiederkehrend_kontaktlastig | 4 | 38 | 0.1742 | 0.0056 | 0.3014 | 0.4232 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0mji3u6 | reproduzierte_ruhige_aufnahme | 4 | 35 | 0.5362 | 0.0037 | 0.1432 | 0.1060 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0mji3u6 | wiederkehrend_offen | 4 | 28 | 0.4375 | 0.0107 | 0.1919 | 0.1293 |
| fuehlen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | wiederkehrend_offen | 4 | 22 | 0.4632 | 0.0144 | 0.1697 | 0.1628 |

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
