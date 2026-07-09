# 423 - Sol2026 Sideways 10K Intake Memory Abgleich

## Fragestellung

Erkennt die passive Sinnesaufnahme-Memory in einer neuen Welt bereits bekannte Aufnahmefamilien wieder?

Verglichen wird:

- Basis: `409_PASSIVE_SINNESAUFNAHME_MEMORY.csv`
- Gegenwelt: `422_SOL2026_SIDEWAYS_10K_PASSIVE_SINNESAUFNAHME_MEMORY.csv`

## Kurzbefund

- Basis-Eintraege: 409.
- Gegenwelt-Eintraege: 292.
- Gemeinsame Intake-Keys: 125.
- Gleiche Memory-Qualitaet: 79.

## Vergleichszustaende

| Zustand | Count |
|---|---:|
| quality_reproduced | 79 |
| quality_shift_open | 37 |
| became_contact_loaded | 4 |
| drifted_lighter | 4 |
| drifted_heavier | 1 |

## Staerkste gemeinsame Spuren

| Intake-Key | Basis | Gegenwelt | Zustand | Probe Count | Balance Delta | Feldinput Delta |
|---|---|---|---|---:|---:|---:|
| feldinput|inner_effect_stable|dio_mcm_episode_0e7qvj1 | contact_loaded_intake | contact_loaded_intake | quality_reproduced | 553 | 0.0131 | 0.0015 |
| feldinput|inner_effect_carried_unrest|dio_mcm_episode_0e7qvj1 | contact_loaded_intake | contact_loaded_intake | quality_reproduced | 289 | 0.0181 | 0.0014 |
| hoeren_leise|inner_effect_carried_unrest|dio_mcm_episode_0e7qvj1 | contact_loaded_intake | contact_loaded_intake | quality_reproduced | 160 | 0.0143 | -0.0018 |
| fuehlen_abstand|inner_effect_carried_unrest|dio_mcm_episode_0e7qvj1 | contact_loaded_intake | contact_loaded_intake | quality_reproduced | 128 | 0.0261 | -0.0037 |
| sehen_fokus|inner_effect_stable|dio_mcm_episode_1rxdw4p | young_intake_trace | young_intake_trace | quality_reproduced | 109 | 0.0100 | 0.0126 |
| hoeren_hin|inner_effect_stable|dio_mcm_episode_1rxdw4p | young_intake_trace | young_intake_trace | quality_reproduced | 96 | 0.0522 | -0.0111 |
| sehen_fokus|inner_effect_stable|dio_mcm_episode_1hdpu9s | young_intake_trace | young_intake_trace | quality_reproduced | 94 | 0.0011 | 0.0057 |
| hoeren_hin|inner_effect_stable|dio_mcm_episode_1hdpu9s | young_intake_trace | young_intake_trace | quality_reproduced | 93 | 0.0048 | -0.0017 |
| hoeren_hin|inner_effect_stable|dio_mcm_episode_1joiyc3 | young_intake_trace | young_intake_trace | quality_reproduced | 75 | 0.0143 | -0.0069 |
| sehen_abstand|inner_effect_stable|dio_mcm_episode_1hdpu9s | young_intake_trace | young_intake_trace | quality_reproduced | 55 | 0.0015 | 0.0003 |
| feldinput|inner_effect_tipping|dio_mcm_episode_0e7qvj1 | contact_loaded_intake | contact_loaded_intake | quality_reproduced | 52 | 0.0036 | 0.0170 |
| feldinput|inner_effect_stable|dio_mcm_episode_1rxdw4p | contact_loaded_intake | contact_loaded_intake | quality_reproduced | 45 | 0.0529 | -0.0006 |
| hoeren_leise|inner_effect_stable|dio_mcm_episode_1rxdw4p | young_intake_trace | young_intake_trace | quality_reproduced | 35 | -0.0134 | 0.0265 |
| sehen_abstand|inner_effect_stable|dio_mcm_episode_1rxdw4p | young_intake_trace | young_intake_trace | quality_reproduced | 32 | 0.0049 | 0.0084 |
| feldinput|inner_effect_stable|dio_mcm_episode_1hdpu9s | contact_loaded_intake | contact_loaded_intake | quality_reproduced | 30 | 0.0085 | -0.0083 |
| sehen_abstand|inner_effect_carried_unrest|dio_mcm_episode_0db07p4 | young_intake_trace | young_intake_trace | quality_reproduced | 30 | -0.0248 | 0.0231 |
| hoeren_leise|inner_effect_stable|dio_mcm_episode_1hdpu9s | young_intake_trace | young_intake_trace | quality_reproduced | 27 | -0.0011 | 0.0080 |
| ausgeglichen|inner_effect_stable|dio_mcm_episode_1hdpu9s | young_intake_trace | young_intake_trace | quality_reproduced | 26 | 0.0023 | -0.0057 |
| feldinput|inner_effect_carried_unrest|dio_mcm_episode_1rxdw4p | contact_loaded_intake | contact_loaded_intake | quality_reproduced | 19 | 0.0465 | -0.0133 |
| sehen_abstand|inner_effect_carried_unrest|dio_mcm_episode_1hdpu9s | young_intake_trace | young_intake_trace | quality_reproduced | 19 | -0.0029 | 0.0254 |

## Interpretation

Die Gegenwelt erzeugt nicht nur neue Einzelspuren, sondern trifft einen Teil der bestehenden Intake-Familien wieder. Entscheidend ist, ob die Qualitaet gleich bleibt oder nur der gleiche Key unter anderer Last erscheint.

`quality_reproduced` bedeutet: dieselbe Aufnahmeachse, dieselbe Innenfeldlage und dieselbe MCM-Preview tragen auch in der neuen Welt dieselbe passive Memory-Qualitaet.

Das bleibt vor Handlung. Der Befund sagt nicht, was MINI_DIO tun soll, sondern welche Aufnahmeform im Innenfeld wiedererkennbar bleibt.

## Wie es weitergeht

Als naechstes sollte eine deutlich andere Gegenwelt laufen. Wenn dieselben ruhigen Spuren dort erhalten bleiben, spricht das fuer stabile Aufnahmefamilien. Wenn sie kippen, wird die Drift der Aufnahmequalitaet sichtbar.
