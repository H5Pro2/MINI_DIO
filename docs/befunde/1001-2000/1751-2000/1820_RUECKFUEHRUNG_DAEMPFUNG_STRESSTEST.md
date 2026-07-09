# Wenn-Dann-Stress-Test: Rückführungsdämpfung

Stand: 2026-07-08 21:10:03

## Grundfrage

Wenn die Rückführung/Rekopplung im Feld gedämpft wird, kollabiert die Topologie oder bildet sie eine geordnete Variante?

Der Test verändert keine Laufmechanik und keine Memory. Er liest vorhandene Episoden und dämpft die Rekopplungsachse nur in der Auswertung.

## Eingriff

- Faktoren: `1.00, 0.90, 0.75, 0.50`
- `1.00` ist die Referenz.
- Kleinere Faktoren simulieren geringere Rückführungswirkung.
- Die Faktoren sind Teststufen, keine festen Regeln.

## Eingaben

- `debug/multiworld_axis_map/SYN1788_BASE_TO_FOLLOW/real_a/dio_mini_lauf_1/episodes.csv`
- `debug/multiworld_axis_map/SYN1788_BASE_TO_FOLLOW/real_b/dio_mini_lauf_2/episodes.csv`
- `debug/multiworld_axis_map/SYN1788_BASE_TO_SHUFFLE/real_a/dio_mini_lauf_1/episodes.csv`
- `debug/multiworld_axis_map/SYN1788_BASE_TO_SHUFFLE/real_b/dio_mini_lauf_2/episodes.csv`

## Gesamtbefund

- Zustände unter Dämpfung: `{'topologie_stabil_mit_daempfung': 4, 'geordnete_verschiebung': 8}`
- Familien-Wiedererkennbarkeit bei stärkster Dämpfung: `0.3333`
- mittlere Randverschiebung bei stärkster Dämpfung: `0.0000`
- mittlere Offenheitsverschiebung bei stärkster Dämpfung: `0.9965`

## Quellenvergleich

| Quelle | Faktor | Zustand | dominante Rolle | Zentrum | Rekopplung | Offen | Rand | Diffus | Familien-Stabilität |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|
| debug/multiworld_axis_map/SYN1788_BASE_TO_FOLLOW/real_a/dio_mini_lauf_1/episodes.csv | 1.00 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.0092 | 0.9908 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/multiworld_axis_map/SYN1788_BASE_TO_FOLLOW/real_a/dio_mini_lauf_1/episodes.csv | 0.90 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.0092 | 0.9908 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/multiworld_axis_map/SYN1788_BASE_TO_FOLLOW/real_a/dio_mini_lauf_1/episodes.csv | 0.75 | `geordnete_verschiebung` | `zentrum_stabil` | 0.9953 | 0.0000 | 0.0031 | 0.0000 | 0.0000 | 0.4444 |
| debug/multiworld_axis_map/SYN1788_BASE_TO_FOLLOW/real_a/dio_mini_lauf_1/episodes.csv | 0.50 | `geordnete_verschiebung` | `offene_variante` | 0.0000 | 0.0000 | 0.9983 | 0.0000 | 0.0017 | 0.3333 |
| debug/multiworld_axis_map/SYN1788_BASE_TO_FOLLOW/real_b/dio_mini_lauf_2/episodes.csv | 1.00 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.0095 | 0.9905 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/multiworld_axis_map/SYN1788_BASE_TO_FOLLOW/real_b/dio_mini_lauf_2/episodes.csv | 0.90 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.0095 | 0.9905 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/multiworld_axis_map/SYN1788_BASE_TO_FOLLOW/real_b/dio_mini_lauf_2/episodes.csv | 0.75 | `geordnete_verschiebung` | `zentrum_stabil` | 0.9930 | 0.0000 | 0.0047 | 0.0000 | 0.0000 | 0.4848 |
| debug/multiworld_axis_map/SYN1788_BASE_TO_FOLLOW/real_b/dio_mini_lauf_2/episodes.csv | 0.50 | `geordnete_verschiebung` | `offene_variante` | 0.0000 | 0.0000 | 0.9978 | 0.0000 | 0.0022 | 0.3333 |
| debug/multiworld_axis_map/SYN1788_BASE_TO_SHUFFLE/real_a/dio_mini_lauf_1/episodes.csv | 1.00 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.0092 | 0.9908 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/multiworld_axis_map/SYN1788_BASE_TO_SHUFFLE/real_a/dio_mini_lauf_1/episodes.csv | 0.90 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.0092 | 0.9908 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/multiworld_axis_map/SYN1788_BASE_TO_SHUFFLE/real_a/dio_mini_lauf_1/episodes.csv | 0.75 | `geordnete_verschiebung` | `zentrum_stabil` | 0.9953 | 0.0000 | 0.0031 | 0.0000 | 0.0000 | 0.4444 |
| debug/multiworld_axis_map/SYN1788_BASE_TO_SHUFFLE/real_a/dio_mini_lauf_1/episodes.csv | 0.50 | `geordnete_verschiebung` | `offene_variante` | 0.0000 | 0.0000 | 0.9983 | 0.0000 | 0.0017 | 0.3333 |
| debug/multiworld_axis_map/SYN1788_BASE_TO_SHUFFLE/real_b/dio_mini_lauf_2/episodes.csv | 1.00 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.0184 | 0.9814 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/multiworld_axis_map/SYN1788_BASE_TO_SHUFFLE/real_b/dio_mini_lauf_2/episodes.csv | 0.90 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.0184 | 0.9814 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/multiworld_axis_map/SYN1788_BASE_TO_SHUFFLE/real_b/dio_mini_lauf_2/episodes.csv | 0.75 | `geordnete_verschiebung` | `zentrum_stabil` | 0.9844 | 0.0000 | 0.0072 | 0.0000 | 0.0000 | 0.3810 |
| debug/multiworld_axis_map/SYN1788_BASE_TO_SHUFFLE/real_b/dio_mini_lauf_2/episodes.csv | 0.50 | `geordnete_verschiebung` | `offene_variante` | 0.0000 | 0.0000 | 0.9917 | 0.0000 | 0.0083 | 0.3333 |

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
