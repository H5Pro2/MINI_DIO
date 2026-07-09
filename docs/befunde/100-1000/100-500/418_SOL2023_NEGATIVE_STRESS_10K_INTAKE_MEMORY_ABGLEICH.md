# 418 - Sol2023 Negative Stress 10K Intake Memory Abgleich

## Fragestellung

Erkennt die passive Sinnesaufnahme-Memory in einer neuen Welt bereits bekannte Aufnahmefamilien wieder?

Verglichen wird:

- Basis: `409_PASSIVE_SINNESAUFNAHME_MEMORY.csv`
- Gegenwelt: `417_SOL2023_NEGATIVE_STRESS_10K_PASSIVE_SINNESAUFNAHME_MEMORY.csv`

## Kurzbefund

- Basis-Eintraege: 409.
- Gegenwelt-Eintraege: 348.
- Gemeinsame Intake-Keys: 135.
- Gleiche Memory-Qualitaet: 90.

## Vergleichszustaende

| Zustand | Count |
|---|---:|
| quality_reproduced | 90 |
| quality_shift_open | 38 |
| became_contact_loaded | 3 |
| drifted_heavier | 3 |
| drifted_lighter | 1 |

## Staerkste gemeinsame Spuren

| Intake-Key | Basis | Gegenwelt | Zustand | Probe Count | Balance Delta | Feldinput Delta |
|---|---|---|---|---:|---:|---:|
| feldinput|inner_effect_stable|dio_mcm_episode_0e7qvj1 | contact_loaded_intake | contact_loaded_intake | quality_reproduced | 430 | 0.0146 | -0.0016 |
| feldinput|inner_effect_carried_unrest|dio_mcm_episode_0e7qvj1 | contact_loaded_intake | contact_loaded_intake | quality_reproduced | 239 | 0.0166 | 0.0011 |
| hoeren_leise|inner_effect_carried_unrest|dio_mcm_episode_0e7qvj1 | contact_loaded_intake | contact_loaded_intake | quality_reproduced | 163 | 0.0185 | -0.0051 |
| hoeren_hin|inner_effect_stable|dio_mcm_episode_1hdpu9s | young_intake_trace | young_intake_trace | quality_reproduced | 150 | 0.0066 | -0.0031 |
| sehen_fokus|inner_effect_stable|dio_mcm_episode_1hdpu9s | young_intake_trace | young_intake_trace | quality_reproduced | 150 | -0.0044 | 0.0070 |
| fuehlen_abstand|inner_effect_carried_unrest|dio_mcm_episode_0e7qvj1 | contact_loaded_intake | contact_loaded_intake | quality_reproduced | 135 | 0.0252 | -0.0142 |
| feldinput|inner_effect_stable|dio_mcm_episode_1hdpu9s | contact_loaded_intake | contact_loaded_intake | quality_reproduced | 67 | 0.0171 | -0.0093 |
| ausgeglichen|inner_effect_stable|dio_mcm_episode_1hdpu9s | young_intake_trace | young_intake_trace | quality_reproduced | 61 | 0.0063 | -0.0075 |
| hoeren_leise|inner_effect_stable|dio_mcm_episode_1hdpu9s | young_intake_trace | young_intake_trace | quality_reproduced | 60 | -0.0034 | 0.0183 |
| sehen_abstand|inner_effect_stable|dio_mcm_episode_1hdpu9s | young_intake_trace | young_intake_trace | quality_reproduced | 51 | -0.0001 | 0.0006 |
| feldinput|inner_effect_tipping|dio_mcm_episode_0e7qvj1 | contact_loaded_intake | contact_loaded_intake | quality_reproduced | 40 | -0.0087 | 0.0100 |
| feldinput|inner_effect_stable|dio_mcm_episode_1jx2k4i | contact_loaded_intake | contact_loaded_intake | quality_reproduced | 31 | -0.0006 | 0.0067 |
| sehen_abstand|inner_effect_carried_unrest|dio_mcm_episode_1hdpu9s | young_intake_trace | young_intake_trace | quality_reproduced | 26 | -0.0186 | 0.0174 |
| hoeren_leise|inner_effect_stable|dio_mcm_episode_1jx2k4i | young_intake_trace | young_intake_trace | quality_reproduced | 21 | -0.0162 | 0.0034 |
| fuehlen_abstand|inner_effect_tipping|dio_mcm_episode_0e7qvj1 | contact_loaded_intake | contact_loaded_intake | quality_reproduced | 18 | -0.0238 | 0.0331 |
| feldinput|inner_effect_carried_unrest|dio_mcm_episode_1hdpu9s | contact_loaded_intake | contact_loaded_intake | quality_reproduced | 16 | -0.0100 | 0.0050 |
| sehen_fokus|inner_effect_stable|dio_mcm_episode_1ahj81f | young_intake_trace | young_intake_trace | quality_reproduced | 14 | -0.0125 | 0.0070 |
| feldinput|inner_effect_carried_unrest|dio_mcm_episode_1jx2k4i | contact_loaded_intake | contact_loaded_intake | quality_reproduced | 13 | -0.0222 | 0.0100 |
| hoeren_leise|inner_effect_carried_unrest|dio_mcm_episode_1hdpu9s | contact_loaded_intake | contact_loaded_intake | quality_reproduced | 13 | 0.0199 | 0.0099 |
| hoeren_hin|inner_effect_stable|dio_mcm_episode_1ahj81f | young_intake_trace | young_intake_trace | quality_reproduced | 11 | 0.0014 | -0.0112 |

## Interpretation

Die Gegenwelt erzeugt nicht nur neue Einzelspuren, sondern trifft einen Teil der bestehenden Intake-Familien wieder. Entscheidend ist, ob die Qualitaet gleich bleibt oder nur der gleiche Key unter anderer Last erscheint.

`quality_reproduced` bedeutet: dieselbe Aufnahmeachse, dieselbe Innenfeldlage und dieselbe MCM-Preview tragen auch in der neuen Welt dieselbe passive Memory-Qualitaet.

Das bleibt vor Handlung. Der Befund sagt nicht, was MINI_DIO tun soll, sondern welche Aufnahmeform im Innenfeld wiedererkennbar bleibt.

## Wie es weitergeht

Als naechstes sollte eine deutlich andere Gegenwelt laufen. Wenn dieselben ruhigen Spuren dort erhalten bleiben, spricht das fuer stabile Aufnahmefamilien. Wenn sie kippen, wird die Drift der Aufnahmequalitaet sichtbar.
