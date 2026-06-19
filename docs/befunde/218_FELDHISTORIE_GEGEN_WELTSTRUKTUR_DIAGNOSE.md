# Feldhistorie gegen Weltstruktur - Diagnose

Stand: 2026-06-19 05:03:40

## Zweck

Diese Diagnose prueft passiv, ob aehnliche Rohweltverdichtung automatisch gleiche Rekopplungsrollen erzeugt.
Die Feldhistorie wird hier nur angenaehert: aus Feldlast, Memorylast und Rekopplungsverlust.

Hierarchie der Pruefung:

1. Grundfrage: Wirkt die Weltstruktur allein oder entscheidet die Feldgeschichte mit?
2. Unterpruefung: Aehnliche Weltverdichtung gegen Feldhistorielast, Rollenwechsel und Bindungskontrast legen.
3. Folgeschritt: Wenn aehnliche Weltstruktur unterschiedlich gelesen wird, Feldhistorie als eigene MCM-Dimension weiter pruefen.

## Ausgangswerte

| Welt | Rolle | Weltverdichtung | Feldhistorielast | Feldlast | Memorylast | Rekopplung | Kontrast |
|---|---|---:|---:|---:|---:|---:|---:|
| QUIET_2024_SIDEWAYS | reiz_aktiv_rekoppelnd | 1.0056 | 0.0271 | 0.0213 | 0.0532 | 0.639653 | -0.5529 |
| QUIET_2026_ANCHOR | reiz_aktiv_rekoppelnd | 1.0530 | 0.0270 | 0.0213 | 0.0532 | 0.639974 | -0.5830 |
| QUIET_2025_STRESS | reiz_aktiv_rekoppelnd | 1.8325 | 0.0038 | 0.0000 | 0.0106 | 0.639352 | -0.6129 |
| QUIET_2025_CORE | reiz_aktiv_rekoppelnd | 2.0029 | 0.0181 | 0.0106 | 0.0319 | 0.628376 | -0.4944 |
| QUIET_2024_REAL | reiz_aktiv_rekoppelnd | 4.0469 | 0.0292 | 0.0213 | 0.0532 | 0.630744 | -0.4875 |
| STRESS_2024_SIDEWAYS | reiz_aktiv_rekoppelnd | 4.6274 | 0.0429 | 0.0532 | 0.0532 | 0.629551 | -0.4669 |
| AUTO_STRESS_SEGMENT6 | uebergang_bindend | 7.8841 | 0.1463 | 0.1290 | 0.2473 | 0.606419 | -0.1357 |
| AUTO_STRESS_SEGMENT5_6 | uebergang_bindend | 8.8606 | 0.1600 | 0.1719 | 0.2344 | 0.606201 | -0.0917 |
| AUTO_STRESS_SEGMENT5 | uebergang_bindend | 11.3986 | 0.1750 | 0.2151 | 0.2258 | 0.607085 | -0.0642 |
| STRESS_2024_REAL | uebergang_bindend | 16.8929 | 0.1907 | 0.2340 | 0.2447 | 0.601652 | 0.0322 |
| STRESS_2023_TEST4 | last_memory_bindend | 17.0762 | 0.2052 | 0.2660 | 0.2447 | 0.596927 | 0.1294 |
| STRESS_2025_STRESS | last_memory_bindend | 19.0124 | 0.2076 | 0.2872 | 0.2234 | 0.594327 | 0.1203 |

## Aehnlichste Weltstruktur

| Paar | Rollen | Welt-Luecke | Feldhistorie-Luecke | Kontrast-Luecke | Rollenwechsel |
|---|---|---:|---:|---:|---|
| QUIET_2024_SIDEWAYS / QUIET_2026_ANCHOR | reiz_aktiv_rekoppelnd / reiz_aktiv_rekoppelnd | 0.0474 | 0.0001 | 0.0301 | nein |
| QUIET_2025_CORE / QUIET_2025_STRESS | reiz_aktiv_rekoppelnd / reiz_aktiv_rekoppelnd | 0.1704 | 0.0143 | 0.1185 | nein |
| STRESS_2023_TEST4 / STRESS_2024_REAL | last_memory_bindend / uebergang_bindend | 0.1833 | 0.0145 | 0.0972 | ja |
| QUIET_2024_REAL / STRESS_2024_SIDEWAYS | reiz_aktiv_rekoppelnd / reiz_aktiv_rekoppelnd | 0.5805 | 0.0137 | 0.0206 | nein |
| QUIET_2025_STRESS / QUIET_2026_ANCHOR | reiz_aktiv_rekoppelnd / reiz_aktiv_rekoppelnd | 0.7794 | 0.0233 | 0.0300 | nein |
| QUIET_2024_SIDEWAYS / QUIET_2025_STRESS | reiz_aktiv_rekoppelnd / reiz_aktiv_rekoppelnd | 0.8269 | 0.0233 | 0.0600 | nein |
| QUIET_2025_CORE / QUIET_2026_ANCHOR | reiz_aktiv_rekoppelnd / reiz_aktiv_rekoppelnd | 0.9499 | 0.0089 | 0.0886 | nein |
| AUTO_STRESS_SEGMENT5_6 / AUTO_STRESS_SEGMENT6 | uebergang_bindend / uebergang_bindend | 0.9765 | 0.0136 | 0.0440 | nein |
| QUIET_2024_SIDEWAYS / QUIET_2025_CORE | reiz_aktiv_rekoppelnd / reiz_aktiv_rekoppelnd | 0.9973 | 0.0090 | 0.0585 | nein |
| STRESS_2023_TEST4 / STRESS_2025_STRESS | last_memory_bindend / last_memory_bindend | 1.9361 | 0.0023 | 0.0091 | nein |
| QUIET_2024_REAL / QUIET_2025_CORE | reiz_aktiv_rekoppelnd / reiz_aktiv_rekoppelnd | 2.0440 | 0.0111 | 0.0069 | nein |
| STRESS_2024_REAL / STRESS_2025_STRESS | uebergang_bindend / last_memory_bindend | 2.1195 | 0.0169 | 0.0881 | ja |

## Staerkste Abweichung trotz Naehe

| Paar | Rollen | Welt-Luecke | Feldhistorie-Luecke | Kontrast-Luecke | Divergenz |
|---|---|---:|---:|---:|---:|
| STRESS_2023_TEST4 / STRESS_2024_REAL | last_memory_bindend / uebergang_bindend | 0.1833 | 0.0145 | 0.0972 | 0.1086 |
| AUTO_STRESS_SEGMENT6 / STRESS_2024_SIDEWAYS | uebergang_bindend / reiz_aktiv_rekoppelnd | 3.2566 | 0.1034 | 0.3312 | 0.0703 |
| QUIET_2024_REAL / AUTO_STRESS_SEGMENT6 | reiz_aktiv_rekoppelnd / uebergang_bindend | 3.8371 | 0.1171 | 0.3518 | 0.0662 |
| AUTO_STRESS_SEGMENT5_6 / STRESS_2024_SIDEWAYS | uebergang_bindend / reiz_aktiv_rekoppelnd | 4.2332 | 0.1171 | 0.3752 | 0.0628 |
| QUIET_2024_REAL / AUTO_STRESS_SEGMENT5_6 | reiz_aktiv_rekoppelnd / uebergang_bindend | 4.8137 | 0.1307 | 0.3958 | 0.0601 |
| QUIET_2025_STRESS / AUTO_STRESS_SEGMENT6 | reiz_aktiv_rekoppelnd / uebergang_bindend | 6.0516 | 0.1426 | 0.4772 | 0.0552 |
| QUIET_2025_STRESS / AUTO_STRESS_SEGMENT5_6 | reiz_aktiv_rekoppelnd / uebergang_bindend | 7.0281 | 0.1562 | 0.5212 | 0.0521 |
| QUIET_2025_CORE / AUTO_STRESS_SEGMENT6 | reiz_aktiv_rekoppelnd / uebergang_bindend | 5.8812 | 0.1282 | 0.3587 | 0.0485 |
| QUIET_2025_CORE / QUIET_2025_STRESS | reiz_aktiv_rekoppelnd / reiz_aktiv_rekoppelnd | 0.1704 | 0.0143 | 0.1185 | 0.0477 |
| QUIET_2025_CORE / AUTO_STRESS_SEGMENT5_6 | reiz_aktiv_rekoppelnd / uebergang_bindend | 6.8577 | 0.1419 | 0.4027 | 0.0462 |
| QUIET_2026_ANCHOR / AUTO_STRESS_SEGMENT6 | reiz_aktiv_rekoppelnd / uebergang_bindend | 6.8310 | 0.1193 | 0.4472 | 0.0454 |
| AUTO_STRESS_SEGMENT5 / STRESS_2024_SIDEWAYS | uebergang_bindend / reiz_aktiv_rekoppelnd | 6.7712 | 0.1321 | 0.4027 | 0.0454 |

## Diagnose-Lesart

- Wenn Weltverdichtung nahe liegt und Rolle gleich bleibt, spricht das fuer weltstrukturgetragene Ordnung.
- Wenn Weltverdichtung nahe liegt und Rolle kippt, spricht das fuer Feldhistorie, Memory oder Rekopplungsverlust als Mitursache.
- Wenn eine Stresswelt trotz aehnlicher Verdichtung aktiv-rekoppelnd bleibt, ist Stress nicht der Name einer festen Klasse, sondern einer moeglichen Feldwirkung.

## Wie es weitergeht

Als naechstes wird der Befund geschrieben.
Dort wird bewertet, ob MINI_DIO bereits eine feldhistorische Lesetiefe zeigt oder ob die aktuellen Werte nur Rohweltverdichtung abbilden.
