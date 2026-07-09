# Sleep-Kombinationsphasen Scan

Stand: 2026-07-05 18:14:46

## Zweck

Diese Diagnose prueft, ob Sleep-Kombinationen bei veraenderter Sleep-Naehe stabil bleiben,
sich teilen oder neue Kombinationsinseln bilden.

Wichtig: Die Pruefung ist passiv. Sie erzeugt keine Handlung, keine Richtung, kein Gate und keine Motorik.

## Welt

- Daten: `data\kontrolliert_2024_negative_stress_test1_1000_5m_SOLUSDT.csv`
- Basis-Memory: `memory\sleep_combination_phase_scan\stress2024_sleep_combo_phase_scan\base_memory.json`

## Phasen

| Phase | activation_floor | Rollen | Kombinationen | geteilt mit Phase 1 | neu gegen Phase 1 | fehlt gegen Phase 1 | Jaccard | Lesung |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 0.75 | 1 | 0 | 0 | 0 | 0 | 1.0 | referenz_phase |
| 2 | 0.65 | 1 | 0 | 0 | 0 | 0 | 1.0 | sleep_combination_stable |
| 3 | 0.45 | 1 | 0 | 0 | 0 | 0 | 1.0 | sleep_combination_stable |

## Lesung

Die Sleep-Kombinationsnaehe blieb in dieser Phasenpruefung stabil. Es wurden keine neuen Kombinationsinseln gegen die Referenzphase sichtbar.

## Wie es weitergeht

Als naechstes sollte diese Phasenpruefung mit einer zweiten Welt wiederholt werden. Entscheidend ist, ob die weiche Sleep-Naehe immer neue Kombinationen erzeugt oder nur bei bestimmten Weltlagen.
