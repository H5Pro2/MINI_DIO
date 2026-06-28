# 1028 - MCM-Achsentypen Wiederkehrpruefung

Passive Gegenprobe, ob die in 1012 gelesenen Chart-/MCM-Typen in weiteren Welten wiederkehren.

## Kurzbefund

- Referenztypen aus 1012: 8
- Gepruefte Achsenfenster: 16
- Bekannte Referenztypen: 9
- Neue oder erweiterte Typen: 7

## Typen

| Typ | Status | Anzahl | Quellen | Welten | Bewegung | Return % | Range % | Druck | Rekopplung | Deutung |
|---|---|---:|---|---|---|---:|---:|---:|---:|---|
| getragene_expansion | known_reference_type | 3 | LONG2024_15M:3 | LONG2024_15M_BTC_STRESS_4000:2 <br> LONG2024_15M_SOL_STRESS_4000:1 | rekopplungs_uebergang:2 <br> druck_uebergang:1 | 25.290062 | 36.856573 | 0.056978 | 0.023351 | Expansion bleibt ueber das Fenster getragen. |
| abverkauf_mit_rekopplung | known_reference_type | 2 | LONG2024_5M:2 | LONG2024_5M_SOL_STRESS_4000:2 | rekopplungs_uebergang:2 | -10.002108 | 17.56247 | 0.053789 | 0.019196 | Abverkauf wird nicht nur als Fall gelesen, sondern mit Rekopplungsanteil getragen. |
| gerichtete_bewegung_mit_bruch | known_reference_type | 2 | LONG2024_15M:1 <br> LONG2024_5M:1 | LONG2024_15M_SOL_QUIET_4000:1 <br> LONG2024_5M_BTC_QUIET_4000:1 | bewegungsbruch_zone:2 | 10.594316 | 18.882155 | 0.068293 | 0.020462 | Richtung laeuft, aber das MCM-Feld liest Bruch oder Umordnung. |
| gerichtete_bewegung_mit_rekopplung | known_reference_type | 1 | LONG2024_15M:1 | LONG2024_15M_SOL_QUIET_4000:1 | rekopplungs_uebergang:1 | 19.822883 | 30.038966 | 0.052709 | 0.017809 | Richtung laeuft und koppelt im Feld wieder an. |
| konsolidierung_mit_rekopplung | known_reference_type | 1 | LONG2024_5M:1 | LONG2024_5M_BTC_QUIET_4000:1 | rekopplungs_uebergang:1 | 0.013527 | 5.812442 | 0.069053 | 0.023049 | Seitwaerts-/Ruhefenster traegt Rekopplung statt reiner Ruhe. |
| weite_volatilitaetszone | new_or_extended_type | 7 | LONG2024_5M:4 <br> LONG2024_15M:3 | LONG2024_15M_BTC_QUIET_4000:2 <br> LONG2024_5M_BTC_STRESS_4000:2 <br> LONG2024_5M_SOL_QUIET_4000:2 <br> LONG2024_15M_SOL_STRESS_4000:1 | rekopplungs_uebergang:4 <br> bewegungsbruch_zone:2 <br> druck_uebergang:1 | 0.966333 | 23.353875 | 0.05091 | 0.017819 | Das Fenster traegt breite Bewegung ohne eindeutige Richtung. |

## Einzelzuordnung

| Status | Typ | Quelle | Welt | Paar | Ticks | Chartzone | MCM-Bewegung | Fenster % | Range % |
|---|---|---|---|---|---|---|---|---:|---:|
| known_reference_type | abverkauf_mit_rekopplung | LONG2024_5M | LONG2024_5M_SOL_STRESS_4000 | `183drjy->1t5bcxp` | 2406-3426 | `abverkauf_getragen` | `rekopplungs_uebergang` | -9.208984 | 15.273437 |
| known_reference_type | abverkauf_mit_rekopplung | LONG2024_5M | LONG2024_5M_SOL_STRESS_4000 | `1t5bcxp->183drjy` | 2404-3477 | `abverkauf_getragen` | `rekopplungs_uebergang` | -10.795233 | 19.851504 |
| known_reference_type | gerichtete_bewegung_mit_bruch | LONG2024_15M | LONG2024_15M_SOL_QUIET_4000 | `183drjy->1t5bcxp` | 1671-3742 | `gerichtete_uebergangsbewegung` | `bewegungsbruch_zone` | 20.07336 | 31.890104 |
| known_reference_type | gerichtete_bewegung_mit_bruch | LONG2024_5M | LONG2024_5M_BTC_QUIET_4000 | `183drjy->1t5bcxp` | 1620-3871 | `gerichtete_uebergangsbewegung` | `bewegungsbruch_zone` | 1.115271 | 5.874207 |
| known_reference_type | gerichtete_bewegung_mit_rekopplung | LONG2024_15M | LONG2024_15M_SOL_QUIET_4000 | `1t5bcxp->183drjy` | 1689-3671 | `gerichtete_uebergangsbewegung` | `rekopplungs_uebergang` | 19.822883 | 30.038966 |
| known_reference_type | getragene_expansion | LONG2024_15M | LONG2024_15M_BTC_STRESS_4000 | `183drjy->1t5bcxp` | 524-3149 | `expansion_getragen` | `druck_uebergang` | 30.262088 | 36.633409 |
| known_reference_type | getragene_expansion | LONG2024_15M | LONG2024_15M_BTC_STRESS_4000 | `1t5bcxp->183drjy` | 441-3619 | `expansion_getragen` | `rekopplungs_uebergang` | 31.706961 | 37.083211 |
| known_reference_type | getragene_expansion | LONG2024_15M | LONG2024_15M_SOL_STRESS_4000 | `1t5bcxp->183drjy` | 763-1602 | `expansion_getragen` | `rekopplungs_uebergang` | 13.901137 | 36.853098 |
| known_reference_type | konsolidierung_mit_rekopplung | LONG2024_5M | LONG2024_5M_BTC_QUIET_4000 | `1t5bcxp->183drjy` | 1147-3872 | `konsolidierung_mit_spannung` | `rekopplungs_uebergang` | 0.013527 | 5.812442 |
| new_or_extended_type | weite_volatilitaetszone | LONG2024_15M | LONG2024_15M_BTC_QUIET_4000 | `183drjy->1t5bcxp` | 199-3845 | `weite_volatilitaetszone` | `druck_uebergang` | 5.734365 | 23.677599 |
| new_or_extended_type | weite_volatilitaetszone | LONG2024_15M | LONG2024_15M_BTC_QUIET_4000 | `1t5bcxp->183drjy` | 206-3867 | `weite_volatilitaetszone` | `rekopplungs_uebergang` | 5.556686 | 23.680007 |
| new_or_extended_type | weite_volatilitaetszone | LONG2024_15M | LONG2024_15M_SOL_STRESS_4000 | `183drjy->1t5bcxp` | 755-1599 | `weite_volatilitaetszone` | `bewegungsbruch_zone` | 12.701706 | 36.606731 |
| new_or_extended_type | weite_volatilitaetszone | LONG2024_5M | LONG2024_5M_BTC_STRESS_4000 | `183drjy->1t5bcxp` | 268-3972 | `weite_volatilitaetszone` | `bewegungsbruch_zone` | -10.489213 | 31.230536 |
| new_or_extended_type | weite_volatilitaetszone | LONG2024_5M | LONG2024_5M_BTC_STRESS_4000 | `1t5bcxp->183drjy` | 269-3975 | `weite_volatilitaetszone` | `rekopplungs_uebergang` | -10.538202 | 31.226834 |
| new_or_extended_type | weite_volatilitaetszone | LONG2024_5M | LONG2024_5M_SOL_QUIET_4000 | `183drjy->1t5bcxp` | 2023-3895 | `weite_volatilitaetszone` | `rekopplungs_uebergang` | 1.692088 | 8.508103 |
| new_or_extended_type | weite_volatilitaetszone | LONG2024_5M | LONG2024_5M_SOL_QUIET_4000 | `1t5bcxp->183drjy` | 1995-3898 | `weite_volatilitaetszone` | `rekopplungs_uebergang` | 2.106901 | 8.547315 |

## Befund

Die Pruefung trennt bekannte Referenztypen von neu entstehenden oder erweiterten Typen. Bekannte Typen sprechen fuer Wiederkehr der Feld-/Chart-Lesung. Neue Typen sind nicht automatisch Fehler; sie koennen echte Erweiterungen durch andere Weltspannung, Assetklasse oder Zeitebene sein.

## Wie es weitergeht

Als naechstes sollten die neuen oder erweiterten Typen getrennt gelesen werden: Welche entstehen durch andere Assetspannung, welche durch Zeitebene, und welche durch echte neue MCM-Uebergangsqualitaet.
