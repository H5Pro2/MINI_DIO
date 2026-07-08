# Wenn-Dann-Stress-Test: Rückführungsdämpfung

Stand: 2026-07-08 21:10:02

## Grundfrage

Wenn die Rückführung/Rekopplung im Feld gedämpft wird, kollabiert die Topologie oder bildet sie eine geordnete Variante?

Der Test verändert keine Laufmechanik und keine Memory. Er liest vorhandene Episoden und dämpft die Rekopplungsachse nur in der Auswertung.

## Eingriff

- Faktoren: `1.00, 0.90, 0.75, 0.50`
- `1.00` ist die Referenz.
- Kleinere Faktoren simulieren geringere Rückführungswirkung.
- Die Faktoren sind Teststufen, keine festen Regeln.

## Eingaben

- `debug/multiworld_axis_map/BTC_2025_1H_0_1000/real_a/dio_mini_lauf_1/episodes.csv`
- `debug/multiworld_axis_map/DOGE_2025_1H_0_1000/real_a/dio_mini_lauf_1/episodes.csv`
- `debug/multiworld_axis_map/XRP_2025_1H_0_1000/real_a/dio_mini_lauf_1/episodes.csv`
- `debug/multiworld_axis_map/SYN1788_BASE_TO_SHUFFLE/real_a/dio_mini_lauf_1/episodes.csv`
- `debug/multiworld_axis_map/SYN1773_A_0_1000/real_a/dio_mini_lauf_1/episodes.csv`

## Gesamtbefund

- Zustände unter Dämpfung: `{'topologie_stabil_mit_daempfung': 5, 'familienordnung_verliert_wiedererkennung': 3, 'topologie_kollabiert_in_rand_oder_diffus': 3, 'geordnete_verschiebung': 4}`
- Familien-Wiedererkennbarkeit bei stärkster Dämpfung: `0.2278`
- mittlere Randverschiebung bei stärkster Dämpfung: `0.0012`
- mittlere Offenheitsverschiebung bei stärkster Dämpfung: `0.8546`

## Quellenvergleich

| Quelle | Faktor | Zustand | dominante Rolle | Zentrum | Rekopplung | Offen | Rand | Diffus | Familien-Stabilität |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|
| debug/multiworld_axis_map/BTC_2025_1H_0_1000/real_a/dio_mini_lauf_1/episodes.csv | 1.00 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.3360 | 0.6268 | 0.0000 | 0.0010 | 0.0000 | 1.0000 |
| debug/multiworld_axis_map/BTC_2025_1H_0_1000/real_a/dio_mini_lauf_1/episodes.csv | 0.90 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.3360 | 0.6268 | 0.0000 | 0.0040 | 0.0000 | 0.7500 |
| debug/multiworld_axis_map/BTC_2025_1H_0_1000/real_a/dio_mini_lauf_1/episodes.csv | 0.75 | `familienordnung_verliert_wiedererkennung` | `zentrum_stabil` | 0.6408 | 0.0000 | 0.1197 | 0.0040 | 0.0000 | 0.1056 |
| debug/multiworld_axis_map/BTC_2025_1H_0_1000/real_a/dio_mini_lauf_1/episodes.csv | 0.50 | `topologie_kollabiert_in_rand_oder_diffus` | `offene_variante` | 0.0000 | 0.0000 | 0.7575 | 0.0040 | 0.2384 | 0.0833 |
| debug/multiworld_axis_map/DOGE_2025_1H_0_1000/real_a/dio_mini_lauf_1/episodes.csv | 1.00 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.3179 | 0.6479 | 0.0000 | 0.0020 | 0.0000 | 1.0000 |
| debug/multiworld_axis_map/DOGE_2025_1H_0_1000/real_a/dio_mini_lauf_1/episodes.csv | 0.90 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.3179 | 0.6479 | 0.0000 | 0.0040 | 0.0000 | 0.8333 |
| debug/multiworld_axis_map/DOGE_2025_1H_0_1000/real_a/dio_mini_lauf_1/episodes.csv | 0.75 | `familienordnung_verliert_wiedererkennung` | `zentrum_stabil` | 0.6328 | 0.0000 | 0.1388 | 0.0040 | 0.0000 | 0.1667 |
| debug/multiworld_axis_map/DOGE_2025_1H_0_1000/real_a/dio_mini_lauf_1/episodes.csv | 0.50 | `topologie_kollabiert_in_rand_oder_diffus` | `offene_variante` | 0.0000 | 0.0000 | 0.7716 | 0.0040 | 0.2243 | 0.1667 |
| debug/multiworld_axis_map/XRP_2025_1H_0_1000/real_a/dio_mini_lauf_1/episodes.csv | 1.00 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.3602 | 0.5966 | 0.0000 | 0.0020 | 0.0000 | 1.0000 |
| debug/multiworld_axis_map/XRP_2025_1H_0_1000/real_a/dio_mini_lauf_1/episodes.csv | 0.90 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.3602 | 0.5966 | 0.0000 | 0.0030 | 0.0000 | 0.8889 |
| debug/multiworld_axis_map/XRP_2025_1H_0_1000/real_a/dio_mini_lauf_1/episodes.csv | 0.75 | `familienordnung_verliert_wiedererkennung` | `zentrum_stabil` | 0.5694 | 0.0000 | 0.1771 | 0.0030 | 0.0000 | 0.2222 |
| debug/multiworld_axis_map/XRP_2025_1H_0_1000/real_a/dio_mini_lauf_1/episodes.csv | 0.50 | `topologie_kollabiert_in_rand_oder_diffus` | `offene_variante` | 0.0000 | 0.0000 | 0.7465 | 0.0030 | 0.2505 | 0.2222 |
| debug/multiworld_axis_map/SYN1788_BASE_TO_SHUFFLE/real_a/dio_mini_lauf_1/episodes.csv | 1.00 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.0092 | 0.9908 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/multiworld_axis_map/SYN1788_BASE_TO_SHUFFLE/real_a/dio_mini_lauf_1/episodes.csv | 0.90 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.0092 | 0.9908 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/multiworld_axis_map/SYN1788_BASE_TO_SHUFFLE/real_a/dio_mini_lauf_1/episodes.csv | 0.75 | `geordnete_verschiebung` | `zentrum_stabil` | 0.9953 | 0.0000 | 0.0031 | 0.0000 | 0.0000 | 0.4444 |
| debug/multiworld_axis_map/SYN1788_BASE_TO_SHUFFLE/real_a/dio_mini_lauf_1/episodes.csv | 0.50 | `geordnete_verschiebung` | `offene_variante` | 0.0000 | 0.0000 | 0.9983 | 0.0000 | 0.0017 | 0.3333 |
| debug/multiworld_axis_map/SYN1773_A_0_1000/real_a/dio_mini_lauf_1/episodes.csv | 1.00 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.0070 | 0.9930 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/multiworld_axis_map/SYN1773_A_0_1000/real_a/dio_mini_lauf_1/episodes.csv | 0.90 | `topologie_stabil_mit_daempfung` | `rekopplungsnaehe` | 0.0070 | 0.9930 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| debug/multiworld_axis_map/SYN1773_A_0_1000/real_a/dio_mini_lauf_1/episodes.csv | 0.75 | `geordnete_verschiebung` | `zentrum_stabil` | 0.9980 | 0.0000 | 0.0010 | 0.0000 | 0.0000 | 0.6190 |
| debug/multiworld_axis_map/SYN1773_A_0_1000/real_a/dio_mini_lauf_1/episodes.csv | 0.50 | `geordnete_verschiebung` | `offene_variante` | 0.0000 | 0.0000 | 0.9990 | 0.0000 | 0.0010 | 0.3333 |

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
