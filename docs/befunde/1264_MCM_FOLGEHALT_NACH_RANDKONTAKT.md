# MCM Folgehalt nach Randkontakt

Stand: 2026-07-02

## Grundfrage

Wie lange traegt eine Folgeordnung nach `spannungsrand_kippnaehe`, bevor das Feld erneut in Rand/Kipp naehe zurueckfaellt?

## Unterpruefung

Diese Diagnose liest Segmentfolgen aus vorhandenen Feldphasen. Sie modelliert keine neue Regulation und setzt keine Handlungsschwelle.

## Profil

- Randkontakte gelesen: `2962`
- Folgearten: `{'offene_variante_entlastend_gehalten': 1447, 'offenheit_kurz_getragen_dann_rueckfall': 874, 'zentrum_stabil_entlastend_gehalten': 249, 'rekopplungsnaehe_entlastend_gehalten': 206, 'zentrum_kurz_getragen_dann_rueckfall': 181, 'offene_variante_gemischt_gehalten': 4, 'rekopplung_kurz_getragen_dann_rueckfall': 1}`
- direkte Folgerollen: `{'offene_variante': 2325, 'zentrum_stabil': 430, 'rekopplungsnaehe': 207}`
- staerkste Welten nach Anzahl: `{'SYNTH_VISUAL_STABLE_HEARING_CHAOTIC': 224, 'BTC_STRESS_2024_5M': 220, 'SOL_STRESS_2024_5M': 204, 'SOL_QUIET_2024_5M': 201, 'BTC_QUIET_2024_5M': 196, 'XRP_5M_10K': 162, 'POS_EXPANSION_10K': 157, 'NEG_STRESS_10K': 152, 'SYNTH_DESYNC_AXES': 146, 'DOGE_5M_10K': 139}`

## Mittelwerte nach Folgeart

| Folgeart | Anzahl | Folge-Dauer | Delta Rekopplung | Delta Strain | Rand-Lautheit | Rand-Strain |
|---|---:|---:|---:|---:|---:|---:|
| offene_variante_entlastend_gehalten | 1447 | 3.9710 | 0.0737 | -0.0958 | 0.6649 | 0.2789 |
| offenheit_kurz_getragen_dann_rueckfall | 874 | 14.1911 | 0.0545 | -0.0939 | 0.0964 | 0.2853 |
| zentrum_stabil_entlastend_gehalten | 249 | 2.3293 | 0.1159 | -0.1314 | 0.7607 | 0.2775 |
| rekopplungsnaehe_entlastend_gehalten | 206 | 1.1942 | 0.1032 | -0.1136 | 0.7195 | 0.2723 |
| zentrum_kurz_getragen_dann_rueckfall | 181 | 6.8950 | 0.1134 | -0.1366 | 0.8002 | 0.2774 |
| offene_variante_gemischt_gehalten | 4 | 1.5000 | -0.0098 | -0.0290 | 0.6858 | 0.2616 |
| rekopplung_kurz_getragen_dann_rueckfall | 1 | 2.0000 | 0.1133 | -0.1357 | 0.7510 | 0.2725 |

## Beispiel-Fenster

| Folgeart | Welt | Rand Tick | Folge | Folge-Dauer | Danach | Delta Rekopplung | Delta Strain |
|---|---|---:|---|---:|---|---:|---:|
| offene_variante_entlastend_gehalten | BRUCH_RAND | 700 | offene_variante | 3 | zentrum_stabil | 0.0869 | -0.1548 |
| offene_variante_entlastend_gehalten | BRUCH_RAND | 1400 | offene_variante | 4 | rekopplungsnaehe | 0.1038 | -0.1385 |
| offene_variante_entlastend_gehalten | BRUCH_RAND | 3500 | offene_variante | 3 | zentrum_stabil | 0.0605 | -0.0791 |
| offene_variante_entlastend_gehalten | BRUCH_RAND | 4200 | offene_variante | 2 | rekopplungsnaehe | 0.0778 | -0.1002 |
| offene_variante_entlastend_gehalten | BRUCH_RAND | 4900 | offene_variante | 2 | zentrum_stabil | 0.0583 | -0.0938 |
| offene_variante_entlastend_gehalten | BRUCH_RAND | 5400 | offene_variante | 3 | zentrum_stabil | 0.0745 | -0.0933 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 59 | offene_variante | 11 | rekopplungsnaehe | 0.0907 | -0.1209 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 79 | offene_variante | 1 | rekopplungsnaehe | 0.0880 | -0.1078 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 97 | offene_variante | 6 | rekopplungsnaehe | 0.0996 | -0.1333 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 166 | offene_variante | 1 | zentrum_stabil | 0.0908 | -0.0850 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 204 | offene_variante | 4 | rekopplungsnaehe | 0.0900 | -0.1073 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 213 | offene_variante | 2 | rekopplungsnaehe | 0.0891 | -0.1183 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 236 | offene_variante | 9 | rekopplungsnaehe | 0.0531 | -0.0746 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 254 | offene_variante | 3 | rekopplungsnaehe | 0.0327 | -0.0532 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 286 | offene_variante | 3 | zentrum_stabil | 0.0879 | -0.1099 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 350 | offene_variante | 9 | zentrum_stabil | 0.1005 | -0.1240 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 424 | offene_variante | 8 | zentrum_stabil | 0.1164 | -0.1467 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 446 | offene_variante | 9 | zentrum_stabil | 0.0744 | -0.0988 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 652 | offene_variante | 2 | zentrum_stabil | 0.0839 | -0.1040 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 708 | offene_variante | 2 | zentrum_stabil | 0.0848 | -0.0997 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 938 | offene_variante | 4 | zentrum_stabil | 0.1001 | -0.1328 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 987 | offene_variante | 2 | zentrum_stabil | 0.0681 | -0.0862 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 1022 | offene_variante | 3 | zentrum_stabil | 0.0466 | -0.0712 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 1045 | offene_variante | 1 | rekopplungsnaehe | 0.0839 | -0.1026 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 1066 | offene_variante | 2 | zentrum_stabil | 0.0812 | -0.0926 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 1080 | offene_variante | 2 | zentrum_stabil | 0.0869 | -0.1092 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 1141 | offene_variante | 3 | zentrum_stabil | 0.0618 | -0.0783 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 1233 | offene_variante | 1 | zentrum_stabil | 0.0839 | -0.0850 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 1313 | offene_variante | 1 | zentrum_stabil | 0.0922 | -0.1184 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 1359 | offene_variante | 5 | rekopplungsnaehe | 0.0717 | -0.0990 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 1369 | offene_variante | 3 | zentrum_stabil | 0.0638 | -0.0784 |
| offene_variante_entlastend_gehalten | BTC_1H_2K | 1399 | offene_variante | 6 | rekopplungsnaehe | 0.0578 | -0.0898 |

## Befund

Randkontakt ist kein Endzustand. Entscheidend ist die Folgebewegung des Feldes.

Die Diagnose trennt drei passive Lesarten:

```text
1. Rand bleibt oder kehrt schnell zurueck.
2. Zentrum/Rekopplung/Offenheit erscheint, haelt aber nur kurz.
3. Folgeordnung entlastet und bleibt vorerst ohne direkten Rueckfall sichtbar.
```

Damit wird die Aussage aus 1262-1263 konkretisiert: Ordnung braucht Folgehalt.

## Wie es weitergeht

Als naechstes sollte dieser Folgehalt mit Rohweltfenstern gekoppelt werden: Welche Weltspannung erzeugt kurzen Rueckfall, welche Weltspannung laesst Folgeordnung tragen?
