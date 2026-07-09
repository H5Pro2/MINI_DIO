# Sleep-Kombinationsphasen Scan

Stand: 2026-07-05 18:14:04

## Zweck

Diese Diagnose prueft, ob Sleep-Kombinationen bei veraenderter Sleep-Naehe stabil bleiben,
sich teilen oder neue Kombinationsinseln bilden.

Wichtig: Die Pruefung ist passiv. Sie erzeugt keine Handlung, keine Richtung, kein Gate und keine Motorik.

## Welt

- Daten: `data\kontrolliert_sol_2024_5m_test1_2000_SOLUSDT.csv`
- Basis-Memory: `memory\sleep_combination_phase_scan\sol2024_sleep_combo_phase_scan\base_memory.json`

## Phasen

| Phase | activation_floor | Rollen | Kombinationen | geteilt mit Phase 1 | neu gegen Phase 1 | fehlt gegen Phase 1 | Jaccard | Lesung |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 0.75 | 3 | 3 | 3 | 0 | 0 | 1.0 | referenz_phase |
| 2 | 0.65 | 3 | 3 | 3 | 0 | 0 | 1.0 | sleep_combination_stable |
| 3 | 0.45 | 5 | 10 | 3 | 7 | 0 | 0.3 | sleep_combination_expanded |

## Lesung

Die Sleep-Kombinationsnaehe ist nicht starr. Weichere oder veraenderte Naehe kann neue Kombinationsinseln sichtbar machen, ohne dass daraus Handlung entsteht.
