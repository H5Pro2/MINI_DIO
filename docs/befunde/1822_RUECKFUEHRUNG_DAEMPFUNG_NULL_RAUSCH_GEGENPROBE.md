# Wenn-Dann-Stress-Test: Rückführungsdämpfung

Stand: 2026-07-08 21:23:07

## Grundfrage

Wenn die Rückführung/Rekopplung im Feld gedämpft wird, kollabiert die Topologie oder bildet sie eine geordnete Variante?

Der Test verändert keine Laufmechanik und keine Memory. Er liest vorhandene Episoden und dämpft die Rekopplungsachse nur in der Auswertung.

## Eingriff

- Faktoren: `1.00, 0.90, 0.75, 0.50`
- `1.00` ist die Referenz.
- Kleinere Faktoren simulieren geringere Rückführungswirkung.
- Die Faktoren sind Teststufen, keine festen Regeln.

## Eingaben

- `debug/1398_holdout_smooth_control/dio_mini_lauf_1/episodes.csv`
- `debug/1402_holdout_noisy_drift/dio_mini_lauf_1/episodes.csv`
- `debug/1403_holdout_high_noisy_drift/dio_mini_lauf_1/episodes.csv`
- `debug/1404_holdout_combined_stress/dio_mini_lauf_1/episodes.csv`
- `debug/1526_null_shuffle_order/dio_mini_lauf_1/episodes.csv`
- `debug/1527_null_random_sign/dio_mini_lauf_1/episodes.csv`
- `debug/multiworld_axis_map/SYN_NULL_RANDOM_TO_SHUFFLE/real_a/dio_mini_lauf_1/episodes.csv`
- `debug/multiworld_axis_map/SYN_NULL_SHUFFLE_TO_RANDOM/real_a/dio_mini_lauf_1/episodes.csv`

## Gesamtbefund

- Zustände unter Dämpfung: `{'topologie_stabil_mit_daempfung': 9, 'geordnete_verschiebung': 15}`
- Familien-Wiedererkennbarkeit bei stärkster Dämpfung: `0.3333`
- mittlere Randverschiebung bei stärkster Dämpfung: `0.0000`
- mittlere Offenheitsverschiebung bei stärkster Dämpfung: `0.9470`

## Quellenvergleich

| Quelle | Faktor | Zustand | dominante Rolle | Zentrum | Rekopplung | Offen | Rand | Diffus | Familien-Stabilität |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|
| debug/1398_holdout_smooth_control/dio_mini_lauf_1/episodes.csv | 1.00 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.0050 | 0.9950 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/1398_holdout_smooth_control/dio_mini_lauf_1/episodes.csv | 0.90 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.0050 | 0.9950 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/1398_holdout_smooth_control/dio_mini_lauf_1/episodes.csv | 0.75 | `topologie_stabil_mit_daempfung` | `zentrum_stabil` | 0.9990 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.6667 |
| debug/1398_holdout_smooth_control/dio_mini_lauf_1/episodes.csv | 0.50 | `geordnete_verschiebung` | `offene_variante` | 0.0000 | 0.0000 | 0.9990 | 0.0000 | 0.0010 | 0.3333 |
| debug/1402_holdout_noisy_drift/dio_mini_lauf_1/episodes.csv | 1.00 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.0111 | 0.9889 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/1402_holdout_noisy_drift/dio_mini_lauf_1/episodes.csv | 0.90 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.0111 | 0.9889 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/1402_holdout_noisy_drift/dio_mini_lauf_1/episodes.csv | 0.75 | `geordnete_verschiebung` | `zentrum_stabil` | 0.9980 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.5333 |
| debug/1402_holdout_noisy_drift/dio_mini_lauf_1/episodes.csv | 0.50 | `geordnete_verschiebung` | `offene_variante` | 0.0000 | 0.0000 | 0.9980 | 0.0000 | 0.0020 | 0.3333 |
| debug/1403_holdout_high_noisy_drift/dio_mini_lauf_1/episodes.csv | 1.00 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.0121 | 0.9879 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/1403_holdout_high_noisy_drift/dio_mini_lauf_1/episodes.csv | 0.90 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.0121 | 0.9879 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/1403_holdout_high_noisy_drift/dio_mini_lauf_1/episodes.csv | 0.75 | `geordnete_verschiebung` | `zentrum_stabil` | 0.9970 | 0.0000 | 0.0010 | 0.0000 | 0.0000 | 0.5926 |
| debug/1403_holdout_high_noisy_drift/dio_mini_lauf_1/episodes.csv | 0.50 | `geordnete_verschiebung` | `offene_variante` | 0.0000 | 0.0000 | 0.9980 | 0.0000 | 0.0020 | 0.3333 |
| debug/1404_holdout_combined_stress/dio_mini_lauf_1/episodes.csv | 1.00 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.0181 | 0.9819 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/1404_holdout_combined_stress/dio_mini_lauf_1/episodes.csv | 0.90 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.0181 | 0.9819 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/1404_holdout_combined_stress/dio_mini_lauf_1/episodes.csv | 0.75 | `geordnete_verschiebung` | `zentrum_stabil` | 0.9909 | 0.0000 | 0.0060 | 0.0000 | 0.0000 | 0.4444 |
| debug/1404_holdout_combined_stress/dio_mini_lauf_1/episodes.csv | 0.50 | `geordnete_verschiebung` | `offene_variante` | 0.0000 | 0.0000 | 0.9970 | 0.0000 | 0.0030 | 0.3333 |
| debug/1526_null_shuffle_order/dio_mini_lauf_1/episodes.csv | 1.00 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.1566 | 0.7485 | 0.0543 | 0.0000 | 0.0000 | 1.0000 |
| debug/1526_null_shuffle_order/dio_mini_lauf_1/episodes.csv | 0.90 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.1566 | 0.7485 | 0.0543 | 0.0000 | 0.0000 | 1.0000 |
| debug/1526_null_shuffle_order/dio_mini_lauf_1/episodes.csv | 0.75 | `geordnete_verschiebung` | `zentrum_stabil` | 0.6533 | 0.0000 | 0.2473 | 0.0000 | 0.0000 | 0.3333 |
| debug/1526_null_shuffle_order/dio_mini_lauf_1/episodes.csv | 0.50 | `geordnete_verschiebung` | `offene_variante` | 0.0000 | 0.0000 | 0.8989 | 0.0000 | 0.1011 | 0.3333 |
| debug/1527_null_random_sign/dio_mini_lauf_1/episodes.csv | 1.00 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.1170 | 0.8003 | 0.0351 | 0.0000 | 0.0000 | 1.0000 |
| debug/1527_null_random_sign/dio_mini_lauf_1/episodes.csv | 0.90 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.1170 | 0.8003 | 0.0351 | 0.0000 | 0.0000 | 1.0000 |
| debug/1527_null_random_sign/dio_mini_lauf_1/episodes.csv | 0.75 | `geordnete_verschiebung` | `zentrum_stabil` | 0.7544 | 0.0000 | 0.1466 | 0.0000 | 0.0000 | 0.3333 |
| debug/1527_null_random_sign/dio_mini_lauf_1/episodes.csv | 0.50 | `geordnete_verschiebung` | `offene_variante` | 0.0000 | 0.0000 | 0.9006 | 0.0000 | 0.0994 | 0.3333 |
| debug/multiworld_axis_map/SYN_NULL_RANDOM_TO_SHUFFLE/real_a/dio_mini_lauf_1/episodes.csv | 1.00 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.1261 | 0.8734 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/multiworld_axis_map/SYN_NULL_RANDOM_TO_SHUFFLE/real_a/dio_mini_lauf_1/episodes.csv | 0.90 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.1261 | 0.8734 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/multiworld_axis_map/SYN_NULL_RANDOM_TO_SHUFFLE/real_a/dio_mini_lauf_1/episodes.csv | 0.75 | `geordnete_verschiebung` | `zentrum_stabil` | 0.8784 | 0.0000 | 0.0543 | 0.0000 | 0.0000 | 0.3333 |
| debug/multiworld_axis_map/SYN_NULL_RANDOM_TO_SHUFFLE/real_a/dio_mini_lauf_1/episodes.csv | 0.50 | `geordnete_verschiebung` | `offene_variante` | 0.0000 | 0.0000 | 0.9323 | 0.0000 | 0.0677 | 0.3333 |
| debug/multiworld_axis_map/SYN_NULL_SHUFFLE_TO_RANDOM/real_a/dio_mini_lauf_1/episodes.csv | 1.00 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.1115 | 0.8885 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/multiworld_axis_map/SYN_NULL_SHUFFLE_TO_RANDOM/real_a/dio_mini_lauf_1/episodes.csv | 0.90 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.1115 | 0.8885 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/multiworld_axis_map/SYN_NULL_SHUFFLE_TO_RANDOM/real_a/dio_mini_lauf_1/episodes.csv | 0.75 | `geordnete_verschiebung` | `zentrum_stabil` | 0.8722 | 0.0000 | 0.0698 | 0.0000 | 0.0000 | 0.3333 |
| debug/multiworld_axis_map/SYN_NULL_SHUFFLE_TO_RANDOM/real_a/dio_mini_lauf_1/episodes.csv | 0.50 | `geordnete_verschiebung` | `offene_variante` | 0.0000 | 0.0000 | 0.9415 | 0.0000 | 0.0585 | 0.3333 |

## Lesung

Dieser Test ist ein methodischer Stresstest, kein Beweis.

Ein starker Befund wäre: Kernfamilien bleiben teilweise wiedererkennbar, während Rollenanteile kontrolliert in Offenheit, Rand oder Diffusität driften.

Ein schwacher Befund wäre: Familienordnung verschwindet beliebig oder alle Quellen reagieren gleich, unabhängig von ihrer Ausgangsform.

## Ergebnisgrenze

- Der Eingriff ist aktuell eine Auswertungsdämpfung, keine echte erneute Laufberechnung.
- Dadurch zeigt der Test zuerst Sensitivität der Feldlesung, nicht vollständige Systemdynamik.
- Ein nächster härterer Test müsste denselben Faktor direkt in einem isolierten Testlauf anwenden.

## Wie es weitergeht

Als nächstes sollte derselbe Stress-Test gegen reale Asset-Fenster und eine Null-/Rauschwelt laufen. Wenn die Nullwelt anders reagiert und Kernfamilien in realen Welten teilweise wiedererkennbar bleiben, wird die Wenn-Dann-Prüfung belastbarer.
