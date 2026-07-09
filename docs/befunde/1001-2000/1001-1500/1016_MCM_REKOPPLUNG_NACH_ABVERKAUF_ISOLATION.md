# 1016 - MCM-Achsentypen Wiederkehrpruefung

Passive Gegenprobe, ob die in 1012 gelesenen Chart-/MCM-Typen in weiteren Welten wiederkehren.

## Kurzbefund

- Referenztypen aus 1012: 8
- Gepruefte Achsenfenster: 40
- Bekannte Referenztypen: 23
- Neue oder erweiterte Typen: 17

## Typen

| Typ | Status | Anzahl | Quellen | Welten | Bewegung | Return % | Range % | Druck | Rekopplung | Deutung |
|---|---|---:|---|---|---|---:|---:|---:|---:|---|
| abverkauf_mit_rekopplung | known_reference_type | 7 | LONG_2025_15M:3 <br> LONG_2024_5M:2 <br> LONG_2025_1H:1 <br> LONG_2025_5M:1 | LONG2024_5M_SOL_STRESS_4000:2 <br> LONG2025_SOL_STRESS_4000:1 <br> LONG2025_15M_BTC_QUIET_4000:1 <br> LONG2025_15M_BTC_STRESS_4000:1 <br> LONG2025_15M_SOL_STRESS_4000:1 <br> LONG2025_5M_BTC_STRESS_4000:1 | rekopplungs_uebergang:7 | -16.343053 | 26.165717 | 0.051619 | 0.019111 | Abverkauf wird nicht nur als Fall gelesen, sondern mit Rekopplungsanteil getragen. |
| getragene_expansion | known_reference_type | 5 | LONG_2024_15M:3 <br> LONG_2025_1H:2 | LONG2025_BTC_STRESS_4000:2 <br> LONG2024_15M_BTC_STRESS_4000:2 <br> LONG2024_15M_SOL_STRESS_4000:1 | rekopplungs_uebergang:3 <br> bewegungsbruch_zone:1 <br> druck_uebergang:1 | 24.055575 | 35.201744 | 0.059705 | 0.021734 | Expansion bleibt ueber das Fenster getragen. |
| gerichtete_bewegung_mit_bruch | known_reference_type | 4 | LONG_2025_1H:1 <br> LONG_2025_5M:1 <br> LONG_2024_15M:1 <br> LONG_2024_5M:1 | LONG2025_SOL_STRESS_4000:1 <br> LONG2025_5M_BTC_STRESS_4000:1 <br> LONG2024_15M_SOL_QUIET_4000:1 <br> LONG2024_5M_BTC_QUIET_4000:1 | bewegungsbruch_zone:4 | -7.005688 | 27.087858 | 0.063247 | 0.018472 | Richtung laeuft, aber das MCM-Feld liest Bruch oder Umordnung. |
| gerichtete_bewegung_mit_rekopplung | known_reference_type | 4 | LONG_2025_5M:2 <br> LONG_2025_15M:1 <br> LONG_2024_15M:1 | LONG2025_5M_BTC_QUIET_4000:2 <br> LONG2025_15M_BTC_QUIET_4000:1 <br> LONG2024_15M_SOL_QUIET_4000:1 | rekopplungs_uebergang:4 | 4.737651 | 12.69461 | 0.052582 | 0.019147 | Richtung laeuft und koppelt im Feld wieder an. |
| abverkauf_mit_bruch | known_reference_type | 2 | LONG_2025_15M:1 <br> LONG_2025_5M:1 | LONG2025_15M_SOL_STRESS_4000:1 <br> LONG2025_5M_SOL_STRESS_4000:1 | bewegungsbruch_zone:2 | -26.952207 | 36.754031 | 0.064318 | 0.021888 | Abverkauf wird als Bewegungsbruch oder Druckbruch gelesen. |
| konsolidierung_mit_rekopplung | known_reference_type | 1 | LONG_2024_5M:1 | LONG2024_5M_BTC_QUIET_4000:1 | rekopplungs_uebergang:1 | 0.013527 | 5.812442 | 0.069053 | 0.023049 | Seitwaerts-/Ruhefenster traegt Rekopplung statt reiner Ruhe. |
| weite_volatilitaetszone | new_or_extended_type | 17 | LONG_2025_1H:4 <br> LONG_2024_5M:4 <br> LONG_2025_15M:3 <br> LONG_2025_5M:3 <br> LONG_2024_15M:3 | LONG2025_BTC_QUIET_4000:2 <br> LONG2025_SOL_QUIET_4000:2 <br> LONG2025_15M_SOL_QUIET_4000:2 <br> LONG2025_5M_SOL_QUIET_4000:2 <br> LONG2024_15M_BTC_QUIET_4000:2 <br> LONG2024_5M_BTC_STRESS_4000:2 <br> LONG2024_5M_SOL_QUIET_4000:2 <br> LONG2025_15M_BTC_STRESS_4000:1 | rekopplungs_uebergang:10 <br> bewegungsbruch_zone:6 <br> druck_uebergang:1 | 2.772644 | 29.38524 | 0.050974 | 0.018031 | Das Fenster traegt breite Bewegung ohne eindeutige Richtung. |

## Einzelzuordnung

| Status | Typ | Quelle | Welt | Paar | Ticks | Chartzone | MCM-Bewegung | Fenster % | Range % |
|---|---|---|---|---|---|---|---|---:|---:|
| known_reference_type | abverkauf_mit_bruch | LONG_2025_15M | LONG2025_15M_SOL_STRESS_4000 | `183drjy->1t5bcxp` | 134-3979 | `abverkauf_getragen` | `bewegungsbruch_zone` | -36.805556 | 42.974387 |
| known_reference_type | abverkauf_mit_bruch | LONG_2025_5M | LONG2025_5M_SOL_STRESS_4000 | `183drjy->1t5bcxp` | 473-3976 | `abverkauf_getragen` | `bewegungsbruch_zone` | -17.098858 | 30.533676 |
| known_reference_type | abverkauf_mit_rekopplung | LONG_2024_5M | LONG2024_5M_SOL_STRESS_4000 | `183drjy->1t5bcxp` | 2406-3426 | `abverkauf_getragen` | `rekopplungs_uebergang` | -9.208984 | 15.273437 |
| known_reference_type | abverkauf_mit_rekopplung | LONG_2024_5M | LONG2024_5M_SOL_STRESS_4000 | `1t5bcxp->183drjy` | 2404-3477 | `abverkauf_getragen` | `rekopplungs_uebergang` | -10.795233 | 19.851504 |
| known_reference_type | abverkauf_mit_rekopplung | LONG_2025_15M | LONG2025_15M_BTC_QUIET_4000 | `1t5bcxp->183drjy` | 723-3816 | `abverkauf_getragen` | `rekopplungs_uebergang` | -3.810866 | 10.623678 |
| known_reference_type | abverkauf_mit_rekopplung | LONG_2025_15M | LONG2025_15M_BTC_STRESS_4000 | `1t5bcxp->183drjy` | 894-3647 | `abverkauf_getragen` | `rekopplungs_uebergang` | -10.193232 | 22.125853 |
| known_reference_type | abverkauf_mit_rekopplung | LONG_2025_15M | LONG2025_15M_SOL_STRESS_4000 | `1t5bcxp->183drjy` | 132-3955 | `abverkauf_getragen` | `rekopplungs_uebergang` | -36.414755 | 42.869996 |
| known_reference_type | abverkauf_mit_rekopplung | LONG_2025_5M | LONG2025_5M_BTC_STRESS_4000 | `1t5bcxp->183drjy` | 2125-3952 | `abverkauf_getragen` | `rekopplungs_uebergang` | -6.169117 | 10.763185 |
| known_reference_type | abverkauf_mit_rekopplung | LONG_2025_1H | LONG2025_SOL_STRESS_4000 | `1t5bcxp->183drjy` | 322-2431 | `abverkauf_getragen` | `rekopplungs_uebergang` | -37.809187 | 61.652364 |
| known_reference_type | gerichtete_bewegung_mit_bruch | LONG_2024_15M | LONG2024_15M_SOL_QUIET_4000 | `183drjy->1t5bcxp` | 1671-3742 | `gerichtete_uebergangsbewegung` | `bewegungsbruch_zone` | 20.07336 | 31.890104 |
| known_reference_type | gerichtete_bewegung_mit_bruch | LONG_2024_5M | LONG2024_5M_BTC_QUIET_4000 | `183drjy->1t5bcxp` | 1620-3871 | `gerichtete_uebergangsbewegung` | `bewegungsbruch_zone` | 1.115271 | 5.874207 |
| known_reference_type | gerichtete_bewegung_mit_bruch | LONG_2025_5M | LONG2025_5M_BTC_STRESS_4000 | `183drjy->1t5bcxp` | 2404-3924 | `gerichtete_uebergangsbewegung` | `bewegungsbruch_zone` | -5.889823 | 8.950316 |
| known_reference_type | gerichtete_bewegung_mit_bruch | LONG_2025_1H | LONG2025_SOL_STRESS_4000 | `183drjy->1t5bcxp` | 327-3766 | `gerichtete_uebergangsbewegung` | `bewegungsbruch_zone` | -43.321558 | 61.636807 |
| known_reference_type | gerichtete_bewegung_mit_rekopplung | LONG_2024_15M | LONG2024_15M_SOL_QUIET_4000 | `1t5bcxp->183drjy` | 1689-3671 | `gerichtete_uebergangsbewegung` | `rekopplungs_uebergang` | 19.822883 | 30.038966 |
| known_reference_type | gerichtete_bewegung_mit_rekopplung | LONG_2025_15M | LONG2025_15M_BTC_QUIET_4000 | `183drjy->1t5bcxp` | 738-3822 | `gerichtete_uebergangsbewegung` | `rekopplungs_uebergang` | -4.169846 | 10.629993 |
| known_reference_type | gerichtete_bewegung_mit_rekopplung | LONG_2025_5M | LONG2025_5M_BTC_QUIET_4000 | `183drjy->1t5bcxp` | 943-3444 | `gerichtete_uebergangsbewegung` | `rekopplungs_uebergang` | 1.593614 | 5.054458 |
| known_reference_type | gerichtete_bewegung_mit_rekopplung | LONG_2025_5M | LONG2025_5M_BTC_QUIET_4000 | `1t5bcxp->183drjy` | 940-3446 | `gerichtete_uebergangsbewegung` | `rekopplungs_uebergang` | 1.703952 | 5.055021 |
| known_reference_type | getragene_expansion | LONG_2024_15M | LONG2024_15M_BTC_STRESS_4000 | `183drjy->1t5bcxp` | 524-3149 | `expansion_getragen` | `druck_uebergang` | 30.262088 | 36.633409 |
| known_reference_type | getragene_expansion | LONG_2024_15M | LONG2024_15M_BTC_STRESS_4000 | `1t5bcxp->183drjy` | 441-3619 | `expansion_getragen` | `rekopplungs_uebergang` | 31.706961 | 37.083211 |
| known_reference_type | getragene_expansion | LONG_2024_15M | LONG2024_15M_SOL_STRESS_4000 | `1t5bcxp->183drjy` | 763-1602 | `expansion_getragen` | `rekopplungs_uebergang` | 13.901137 | 36.853098 |
| known_reference_type | getragene_expansion | LONG_2025_1H | LONG2025_BTC_STRESS_4000 | `183drjy->1t5bcxp` | 1236-2768 | `expansion_getragen` | `bewegungsbruch_zone` | 18.94883 | 32.324571 |
| known_reference_type | getragene_expansion | LONG_2025_1H | LONG2025_BTC_STRESS_4000 | `1t5bcxp->183drjy` | 1177-2804 | `expansion_getragen` | `rekopplungs_uebergang` | 25.458857 | 33.114433 |
| known_reference_type | konsolidierung_mit_rekopplung | LONG_2024_5M | LONG2024_5M_BTC_QUIET_4000 | `1t5bcxp->183drjy` | 1147-3872 | `konsolidierung_mit_spannung` | `rekopplungs_uebergang` | 0.013527 | 5.812442 |
| new_or_extended_type | weite_volatilitaetszone | LONG_2024_15M | LONG2024_15M_BTC_QUIET_4000 | `183drjy->1t5bcxp` | 199-3845 | `weite_volatilitaetszone` | `druck_uebergang` | 5.734365 | 23.677599 |
| new_or_extended_type | weite_volatilitaetszone | LONG_2024_15M | LONG2024_15M_BTC_QUIET_4000 | `1t5bcxp->183drjy` | 206-3867 | `weite_volatilitaetszone` | `rekopplungs_uebergang` | 5.556686 | 23.680007 |
| new_or_extended_type | weite_volatilitaetszone | LONG_2024_15M | LONG2024_15M_SOL_STRESS_4000 | `183drjy->1t5bcxp` | 755-1599 | `weite_volatilitaetszone` | `bewegungsbruch_zone` | 12.701706 | 36.606731 |
| new_or_extended_type | weite_volatilitaetszone | LONG_2024_5M | LONG2024_5M_BTC_STRESS_4000 | `183drjy->1t5bcxp` | 268-3972 | `weite_volatilitaetszone` | `bewegungsbruch_zone` | -10.489213 | 31.230536 |
| new_or_extended_type | weite_volatilitaetszone | LONG_2024_5M | LONG2024_5M_BTC_STRESS_4000 | `1t5bcxp->183drjy` | 269-3975 | `weite_volatilitaetszone` | `rekopplungs_uebergang` | -10.538202 | 31.226834 |
| new_or_extended_type | weite_volatilitaetszone | LONG_2024_5M | LONG2024_5M_SOL_QUIET_4000 | `183drjy->1t5bcxp` | 2023-3895 | `weite_volatilitaetszone` | `rekopplungs_uebergang` | 1.692088 | 8.508103 |
| new_or_extended_type | weite_volatilitaetszone | LONG_2024_5M | LONG2024_5M_SOL_QUIET_4000 | `1t5bcxp->183drjy` | 1995-3898 | `weite_volatilitaetszone` | `rekopplungs_uebergang` | 2.106901 | 8.547315 |
| new_or_extended_type | weite_volatilitaetszone | LONG_2025_15M | LONG2025_15M_BTC_STRESS_4000 | `183drjy->1t5bcxp` | 896-3025 | `weite_volatilitaetszone` | `rekopplungs_uebergang` | -7.449022 | 22.072909 |
| new_or_extended_type | weite_volatilitaetszone | LONG_2025_15M | LONG2025_15M_SOL_QUIET_4000 | `183drjy->1t5bcxp` | 442-3921 | `weite_volatilitaetszone` | `bewegungsbruch_zone` | 5.812744 | 27.730819 |
| new_or_extended_type | weite_volatilitaetszone | LONG_2025_15M | LONG2025_15M_SOL_QUIET_4000 | `1t5bcxp->183drjy` | 440-3969 | `weite_volatilitaetszone` | `rekopplungs_uebergang` | 3.89161 | 27.848515 |
| new_or_extended_type | weite_volatilitaetszone | LONG_2025_5M | LONG2025_5M_SOL_QUIET_4000 | `183drjy->1t5bcxp` | 1792-3653 | `weite_volatilitaetszone` | `bewegungsbruch_zone` | -1.888056 | 8.422603 |
| new_or_extended_type | weite_volatilitaetszone | LONG_2025_5M | LONG2025_5M_SOL_QUIET_4000 | `1t5bcxp->183drjy` | 1787-3643 | `weite_volatilitaetszone` | `rekopplungs_uebergang` | -1.28764 | 8.436725 |
| new_or_extended_type | weite_volatilitaetszone | LONG_2025_5M | LONG2025_5M_SOL_STRESS_4000 | `1t5bcxp->183drjy` | 490-3493 | `weite_volatilitaetszone` | `rekopplungs_uebergang` | -9.80706 | 30.674847 |
| new_or_extended_type | weite_volatilitaetszone | LONG_2025_1H | LONG2025_BTC_QUIET_4000 | `183drjy->1t5bcxp` | 1002-3651 | `weite_volatilitaetszone` | `bewegungsbruch_zone` | 3.835077 | 24.989538 |
| new_or_extended_type | weite_volatilitaetszone | LONG_2025_1H | LONG2025_BTC_QUIET_4000 | `1t5bcxp->183drjy` | 999-3655 | `weite_volatilitaetszone` | `rekopplungs_uebergang` | 3.983749 | 24.917756 |
| new_or_extended_type | weite_volatilitaetszone | LONG_2025_1H | LONG2025_SOL_QUIET_4000 | `183drjy->1t5bcxp` | 661-3909 | `weite_volatilitaetszone` | `bewegungsbruch_zone` | 16.748203 | 77.012744 |
| new_or_extended_type | weite_volatilitaetszone | LONG_2025_1H | LONG2025_SOL_QUIET_4000 | `1t5bcxp->183drjy` | 577-3911 | `weite_volatilitaetszone` | `rekopplungs_uebergang` | 26.531015 | 83.965495 |

## Befund

Die Pruefung trennt bekannte Referenztypen von neu entstehenden oder erweiterten Typen. Bekannte Typen sprechen fuer Wiederkehr der Feld-/Chart-Lesung. Neue Typen sind nicht automatisch Fehler; sie koennen echte Erweiterungen durch andere Weltspannung, Assetklasse oder Zeitebene sein.

## Wie es weitergeht

Als naechstes sollten die neuen oder erweiterten Typen getrennt gelesen werden: Welche entstehen durch andere Assetspannung, welche durch Zeitebene, und welche durch echte neue MCM-Uebergangsqualitaet.
