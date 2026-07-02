# Real/Synthetisch Rollenprofil Vergleich

## Grundfrage

Liegen reale Rand/Kipp-Rollen naeher an Hoerlast, Formbruch oder gekoppelter Feldlast?

Diese Diagnose vergleicht aggregierte Rollenprofile aus synthetischen und realen Segmentdateien. Sie ist passiv und erzeugt keine Runtime-Regel.

## Rollenprofile

| Quelle | Welt | Rolle | Daueranteil | Rohfeld | Lautheit | Schaerfe | Rekopplung | Strain | Signatur |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| REAL_5M | BTC_QUIET_CURRENT | offene_variante | 0.3458 | 0.1660 | 0.2806 | 0.6151 | 0.6713 | 0.1732 | gemischte_feldlage |
| REAL_5M | BTC_QUIET_CURRENT | rekopplungsnaehe | 0.1412 | 0.1092 | 0.1819 | 0.6671 | 0.7056 | 0.1428 | gemischte_feldlage |
| REAL_5M | BTC_QUIET_CURRENT | spannungsrand_kippnaehe | 0.0165 | 0.4078 | 0.7147 | 0.5824 | 0.5827 | 0.2834 | gekoppelte_feldlast |
| REAL_5M | BTC_QUIET_CURRENT | zentrum_stabil | 0.4965 | 0.0904 | 0.1487 | 0.6866 | 0.7214 | 0.1381 | rekopplung_zentrumsnah |
| REAL_5M | BTC_STRESS_CURRENT | offene_variante | 0.3435 | 0.1735 | 0.2937 | 0.6215 | 0.6709 | 0.1739 | gemischte_feldlage |
| REAL_5M | BTC_STRESS_CURRENT | rekopplungsnaehe | 0.1237 | 0.1087 | 0.1801 | 0.6733 | 0.7060 | 0.1409 | gemischte_feldlage |
| REAL_5M | BTC_STRESS_CURRENT | spannungsrand_kippnaehe | 0.0193 | 0.3681 | 0.6358 | 0.5435 | 0.5882 | 0.2745 | gekoppelte_feldlast |
| REAL_5M | BTC_STRESS_CURRENT | zentrum_stabil | 0.5135 | 0.0917 | 0.1528 | 0.6932 | 0.7222 | 0.1382 | rekopplung_zentrumsnah |
| REAL_5M | SOL_QUIET_CURRENT | offene_variante | 0.3678 | 0.1681 | 0.2860 | 0.6119 | 0.6719 | 0.1734 | gemischte_feldlage |
| REAL_5M | SOL_QUIET_CURRENT | rekopplungsnaehe | 0.1480 | 0.1098 | 0.1816 | 0.6593 | 0.7052 | 0.1448 | gemischte_feldlage |
| REAL_5M | SOL_QUIET_CURRENT | spannungsrand_kippnaehe | 0.0155 | 0.3996 | 0.7011 | 0.5641 | 0.5829 | 0.2831 | gekoppelte_feldlast |
| REAL_5M | SOL_QUIET_CURRENT | zentrum_stabil | 0.4687 | 0.0899 | 0.1470 | 0.6814 | 0.7208 | 0.1378 | rekopplung_zentrumsnah |
| REAL_5M | SOL_STRESS_CURRENT | offene_variante | 0.3630 | 0.1676 | 0.2857 | 0.6102 | 0.6713 | 0.1743 | gemischte_feldlage |
| REAL_5M | SOL_STRESS_CURRENT | rekopplungsnaehe | 0.1435 | 0.1060 | 0.1744 | 0.6594 | 0.7052 | 0.1431 | gemischte_feldlage |
| REAL_5M | SOL_STRESS_CURRENT | spannungsrand_kippnaehe | 0.0190 | 0.3802 | 0.6616 | 0.5490 | 0.5864 | 0.2787 | gekoppelte_feldlast |
| REAL_5M | SOL_STRESS_CURRENT | zentrum_stabil | 0.4745 | 0.0908 | 0.1485 | 0.6812 | 0.7209 | 0.1387 | rekopplung_zentrumsnah |
| SYNTH_AXES | SYNTH_DESYNC_AXES | offene_variante | 0.0182 | 0.1714 | 0.2981 | 0.7954 | 0.6831 | 0.1644 | gemischte_feldlage |
| SYNTH_AXES | SYNTH_DESYNC_AXES | rekopplungsnaehe | 0.0198 | 0.1367 | 0.2393 | 0.8106 | 0.7112 | 0.1439 | rekopplung_zentrumsnah |
| SYNTH_AXES | SYNTH_DESYNC_AXES | spannungsrand_kippnaehe | 0.0173 | 0.4870 | 0.8219 | 0.7405 | 0.6193 | 0.2820 | hoerlast_bei_lesbarer_form |
| SYNTH_AXES | SYNTH_DESYNC_AXES | zentrum_stabil | 0.9447 | 0.0292 | 0.0396 | 0.8368 | 0.7574 | 0.1220 | rekopplung_zentrumsnah |
| SYNTH_AXES | SYNTH_RAND_KIPP | offene_variante | 0.1155 | 0.1749 | 0.3034 | 0.5802 | 0.6736 | 0.1793 | gemischte_feldlage |
| SYNTH_AXES | SYNTH_RAND_KIPP | rekopplungsnaehe | 0.0541 | 0.0950 | 0.1459 | 0.5953 | 0.7031 | 0.1535 | ruhige_feldnaehe |
| SYNTH_AXES | SYNTH_RAND_KIPP | spannungsrand_kippnaehe | 0.0024 | 0.3798 | 0.6664 | 0.5797 | 0.6079 | 0.2716 | gekoppelte_feldlast |
| SYNTH_AXES | SYNTH_RAND_KIPP | zentrum_stabil | 0.8279 | 0.0385 | 0.0554 | 0.8015 | 0.7493 | 0.1244 | rekopplung_zentrumsnah |
| SYNTH_AXES | SYNTH_VISUAL_CHAOTIC_HEARING_STABLE | offene_variante | 0.0031 | 0.0740 | 0.1171 | 0.7336 | 0.6781 | 0.1491 | ruhige_feldnaehe |
| SYNTH_AXES | SYNTH_VISUAL_CHAOTIC_HEARING_STABLE | rekopplungsnaehe | 0.0017 | 0.0188 | 0.0131 | 0.7971 | 0.7233 | 0.0961 | rekopplung_zentrumsnah |
| SYNTH_AXES | SYNTH_VISUAL_CHAOTIC_HEARING_STABLE | zentrum_stabil | 0.9952 | 0.0167 | 0.0123 | 0.8397 | 0.7593 | 0.1182 | rekopplung_zentrumsnah |
| SYNTH_AXES | SYNTH_VISUAL_STABLE_HEARING_CHAOTIC | offene_variante | 0.0231 | 0.3502 | 0.5928 | 0.7614 | 0.6553 | 0.2278 | gemischte_feldlage |
| SYNTH_AXES | SYNTH_VISUAL_STABLE_HEARING_CHAOTIC | rekopplungsnaehe | 0.0073 | 0.1460 | 0.2491 | 0.7946 | 0.7114 | 0.1396 | rekopplung_zentrumsnah |
| SYNTH_AXES | SYNTH_VISUAL_STABLE_HEARING_CHAOTIC | spannungsrand_kippnaehe | 0.0306 | 0.4957 | 0.8361 | 0.7397 | 0.6180 | 0.2844 | hoerlast_bei_lesbarer_form |
| SYNTH_AXES | SYNTH_VISUAL_STABLE_HEARING_CHAOTIC | zentrum_stabil | 0.9390 | 0.0270 | 0.0385 | 0.8372 | 0.7611 | 0.1221 | rekopplung_zentrumsnah |

## Staerkste Rand/Kipp-Lautheit

- `SYNTH_AXES` / `SYNTH_VISUAL_STABLE_HEARING_CHAOTIC`: Lautheit `0.8361`, Rohfeld `0.4957`, Schaerfe `0.7397`, Rekopplung `0.6180`, Strain `0.2844`, Signatur `hoerlast_bei_lesbarer_form`
- `SYNTH_AXES` / `SYNTH_DESYNC_AXES`: Lautheit `0.8219`, Rohfeld `0.4870`, Schaerfe `0.7405`, Rekopplung `0.6193`, Strain `0.2820`, Signatur `hoerlast_bei_lesbarer_form`
- `REAL_5M` / `BTC_QUIET_CURRENT`: Lautheit `0.7147`, Rohfeld `0.4078`, Schaerfe `0.5824`, Rekopplung `0.5827`, Strain `0.2834`, Signatur `gekoppelte_feldlast`
- `REAL_5M` / `SOL_QUIET_CURRENT`: Lautheit `0.7011`, Rohfeld `0.3996`, Schaerfe `0.5641`, Rekopplung `0.5829`, Strain `0.2831`, Signatur `gekoppelte_feldlast`
- `SYNTH_AXES` / `SYNTH_RAND_KIPP`: Lautheit `0.6664`, Rohfeld `0.3798`, Schaerfe `0.5797`, Rekopplung `0.6079`, Strain `0.2716`, Signatur `gekoppelte_feldlast`
- `REAL_5M` / `SOL_STRESS_CURRENT`: Lautheit `0.6616`, Rohfeld `0.3802`, Schaerfe `0.5490`, Rekopplung `0.5864`, Strain `0.2787`, Signatur `gekoppelte_feldlast`

## Staerkster Rand/Kipp-Strain

- `SYNTH_AXES` / `SYNTH_VISUAL_STABLE_HEARING_CHAOTIC`: Strain `0.2844`, Lautheit `0.8361`, Rohfeld `0.4957`, Schaerfe `0.7397`, Signatur `hoerlast_bei_lesbarer_form`
- `REAL_5M` / `BTC_QUIET_CURRENT`: Strain `0.2834`, Lautheit `0.7147`, Rohfeld `0.4078`, Schaerfe `0.5824`, Signatur `gekoppelte_feldlast`
- `REAL_5M` / `SOL_QUIET_CURRENT`: Strain `0.2831`, Lautheit `0.7011`, Rohfeld `0.3996`, Schaerfe `0.5641`, Signatur `gekoppelte_feldlast`
- `SYNTH_AXES` / `SYNTH_DESYNC_AXES`: Strain `0.2820`, Lautheit `0.8219`, Rohfeld `0.4870`, Schaerfe `0.7405`, Signatur `hoerlast_bei_lesbarer_form`
- `REAL_5M` / `SOL_STRESS_CURRENT`: Strain `0.2787`, Lautheit `0.6616`, Rohfeld `0.3802`, Schaerfe `0.5490`, Signatur `gekoppelte_feldlast`
- `REAL_5M` / `BTC_STRESS_CURRENT`: Strain `0.2745`, Lautheit `0.6358`, Rohfeld `0.3681`, Schaerfe `0.5435`, Signatur `gekoppelte_feldlast`

## Ableitung

Wenn Rand/Kipp hohe Lautheit, hohes Rohfeld, sinkende Rekopplung und hohen Strain gemeinsam zeigt, ist die Rolle als gekoppelte Feldlast zu lesen.

Wenn Lautheit hoch bleibt, die visuelle Schaerfe aber ebenfalls hoch bleibt, spricht das fuer Hoerlast bei lesbarer Form.

Wenn visuelle Schaerfe niedrig ist, aber Lautheit nicht stark steigt, spricht das eher fuer Formbruch ohne starke Hoerlast.

## Wie es weitergeht

Als naechstes sollten die realen `gekoppelte_feldlast`-Fenster gegen die Rohweltsequenz gelesen werden. Ziel ist zu sehen, ob diese Rolle an Bewegungsbruch, Expansion oder Rekopplungsversuch gebunden ist.
