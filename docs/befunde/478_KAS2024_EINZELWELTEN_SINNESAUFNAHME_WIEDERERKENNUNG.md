# 478 - Kas2024 Einzelwelten Sinnesaufnahme Wiedererkennung

## Fragestellung

Kann MINI_DIO Aufnahmequalitaeten wiedererkennen, ohne daraus Handlung oder Regel zu machen?

Geprueft wird die kleinste passive Signatur:

```text
Aufnahmeachse + Innenfeldzustand + MCM-Preview
```

Wenn diese Signatur ueber mehrere Welten mit aehnlicher Feldwirkung wiederkehrt, ist sie eine passive Lernspur.

## Kurzbefund

- Wiederkehrende Signaturen mit mindestens drei Welten: 50.
- Reproduzierte ruhige Aufnahmen: 7.

## Staerkste Wiedererkennungen

| Achse | Innenfeld | Preview | Label | Welten | Count | Balance | Streuung | Strain | Feldinput |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | reproduzierte_ruhige_aufnahme | 4 | 1590 | 0.5675 | 0.0009 | 0.1341 | 0.0631 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | reproduzierte_ruhige_aufnahme | 4 | 1505 | 0.5405 | 0.0014 | 0.1417 | 0.1073 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | wiederkehrend_tragend | 4 | 721 | 0.5117 | 0.0018 | 0.1576 | 0.1150 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | wiederkehrend_offen | 4 | 567 | 0.4418 | 0.0060 | 0.1897 | 0.1344 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | reproduzierte_ruhige_aufnahme | 4 | 480 | 0.5251 | 0.0002 | 0.1556 | 0.1194 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | wiederkehrend_offen | 4 | 434 | 0.4688 | 0.0026 | 0.1718 | 0.1874 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | wiederkehrend_kontaktlastig | 4 | 389 | 0.4472 | 0.0058 | 0.1800 | 0.2089 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1jx2k4i | reproduzierte_ruhige_aufnahme | 4 | 241 | 0.5573 | 0.0098 | 0.1351 | 0.0639 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | wiederkehrend_kontaktlastig | 4 | 227 | 0.3304 | 0.0034 | 0.2311 | 0.2940 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1jx2k4i | reproduzierte_ruhige_aufnahme | 4 | 207 | 0.5278 | 0.0111 | 0.1444 | 0.1064 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | wiederkehrend_kontaktlastig | 4 | 171 | 0.3980 | 0.0077 | 0.2055 | 0.2140 |
| fuehlen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | wiederkehrend_kontaktlastig | 4 | 122 | 0.3559 | 0.0135 | 0.2237 | 0.2249 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_1jx2k4i | wiederkehrend_tragend | 4 | 88 | 0.4931 | 0.0146 | 0.1620 | 0.1134 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_1jx2k4i | reproduzierte_ruhige_aufnahme | 4 | 55 | 0.5202 | 0.0111 | 0.1526 | 0.1168 |
| feldinput | inner_effect_tipping | dio_mcm_episode_0e7qvj1 | wiederkehrend_kontaktlastig | 4 | 43 | 0.1737 | 0.0066 | 0.3013 | 0.4267 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_1jx2k4i | wiederkehrend_offen | 4 | 40 | 0.4388 | 0.0229 | 0.1892 | 0.1239 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0mji3u6 | reproduzierte_ruhige_aufnahme | 4 | 35 | 0.5294 | 0.0064 | 0.1453 | 0.1090 |
| hoeren_hin | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | wiederkehrend_tragend | 4 | 28 | 0.5072 | 0.0174 | 0.1627 | 0.0807 |

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
