# Bewegungsarten Rohwelt-Segmente

Stand: 2026-06-20 00:54:33

## Zweck

Diese Diagnose legt validierte MCM-Preview-Bewegungen neben ihre lokalen Rohwelt- und Rezeptorsegmente.
Sie bleibt passiv: keine Handlung, kein Gate, keine aktive Regulation.

## Hierarchie

1. Grundfrage: Welche Welt-/Rezeptorlage begleitet eine passive Feldbewegung?
2. Unterpruefung: vor, waehrend und nach stabilen Uebergangspaaren vergleichen.
3. Folgeschritt: daraus passive Ausloesemilieus lesen, nicht Handlungsregeln.

## Phasenmatrix

| Paar | Phase | Samples | Welten | Segment | Rolle | Formstabilitaet | Formbruch | Energiebruch | Druck | Alignment | Strain | Rekopplung |
|---|---|---:|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | nachher | 146 | 10 | offene_lage | zentrum_stabil | 0.0325 | 0.1900 | 0.2270 | 0.2073 | 0.5672 | 0.1847 | 0.6462 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | vorher | 146 | 10 | offene_lage | zentrum_stabil | 0.0544 | 0.1780 | 0.2125 | 0.1926 | 0.5705 | 0.1794 | 0.6494 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | wechsel | 73 | 10 | offene_lage | zentrum_stabil | 0.0113 | 0.2381 | 0.3546 | 0.2884 | 0.5565 | 0.2279 | 0.6219 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | nachher | 156 | 9 | offene_lage | zentrum_stabil | 0.0527 | 0.1463 | 0.2148 | 0.1686 | 0.5715 | 0.1694 | 0.6546 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | vorher | 156 | 9 | offene_lage | zentrum_stabil | 0.0166 | 0.1166 | 0.1900 | 0.1526 | 0.5689 | 0.1638 | 0.6546 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | wechsel | 78 | 9 | offene_lage | zentrum_stabil | 0.0624 | 0.0978 | 0.1395 | 0.1226 | 0.5764 | 0.1382 | 0.6750 |

## Ereignislupe

| Welt | Paar | Tick | Vorher | Wechsel | Nachher | dDruck | dRekopplung |
|---|---|---:|---|---|---|---:|---:|
| BTC_2024_15M | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1193 | bewegungsbruch | offene_lage | offene_lage | -0.1929 | 0.0216 |
| BTC_2024_15M | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1175 | offene_lage | offene_lage | offene_lage | -0.0608 | -0.0053 |
| BTC_2024_15M | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1195 | offene_lage | offene_lage | offene_lage | -0.0119 | 0.0213 |
| BTC_2024_1H | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 446 | offene_lage | druck_lage | offene_lage | 0.2592 | -0.0073 |
| BTC_2024_1H | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 535 | offene_lage | druck_lage | druck_lage | 0.3060 | -0.0286 |
| BTC_2024_1H | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 729 | offene_lage | druck_lage | offene_lage | 0.2008 | -0.0403 |
| BTC_2024_1H | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 736 | offene_lage | bewegungsbruch | gehaltene_form | -0.0378 | 0.0054 |
| BTC_2024_1H | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 740 | offene_lage | druck_lage | gehaltene_form | 0.1277 | -0.0133 |
| BTC_2024_1H | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 782 | offene_lage | bewegungsbruch | bewegungsbruch | -0.1172 | 0.0236 |
| BTC_2024_1H | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1520 | offene_lage | druck_lage | druck_lage | 0.1308 | -0.0165 |
| BTC_2024_1H | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1699 | offene_lage | bewegungsbruch | bewegungsbruch | -0.0534 | 0.0169 |
| BTC_2024_1H | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1702 | bewegungsbruch | offene_lage | offene_lage | -0.0799 | 0.0230 |
| BTC_2024_1H | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1709 | druck_lage | offene_lage | offene_lage | -0.0483 | 0.0205 |
| BTC_2024_1H | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1718 | offene_lage | druck_lage | offene_lage | 0.0951 | -0.0327 |
| BTC_2024_1H | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1760 | offene_lage | offene_lage | offene_lage | -0.0121 | 0.0216 |
| BTC_2024_1H | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1765 | offene_lage | druck_lage | gehaltene_form | 0.1730 | -0.0094 |
| BTC_2024_1H | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1767 | druck_lage | druck_lage | druck_lage | -0.1242 | 0.0156 |
| BTC_2024_1H | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 442 | offene_lage | offene_lage | offene_lage | 0.0412 | -0.0003 |
| BTC_2024_1H | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 479 | offene_lage | offene_lage | offene_lage | 0.0484 | -0.0274 |
| BTC_2024_1H | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 727 | offene_lage | offene_lage | offene_lage | 0.1378 | -0.0311 |
| BTC_2024_1H | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 734 | offene_lage | offene_lage | druck_lage | 0.1906 | -0.0073 |
| BTC_2024_1H | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 738 | bewegungsbruch | offene_lage | offene_lage | 0.0646 | -0.0257 |
| BTC_2024_1H | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 777 | offene_lage | offene_lage | offene_lage | 0.0079 | 0.0141 |
| BTC_2024_1H | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 791 | offene_lage | offene_lage | offene_lage | 0.0224 | 0.0227 |
| BTC_2024_1H | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1701 | bewegungsbruch | offene_lage | offene_lage | -0.1134 | 0.0277 |
| BTC_2024_1H | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1703 | offene_lage | offene_lage | offene_lage | -0.0150 | 0.0089 |
| BTC_2024_1H | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1715 | offene_lage | offene_lage | offene_lage | 0.0263 | 0.0118 |
| BTC_2024_1H | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1754 | offene_lage | offene_lage | offene_lage | 0.1183 | -0.0063 |
| BTC_2024_1H | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1761 | offene_lage | offene_lage | offene_lage | -0.0525 | 0.0241 |
| BTC_2024_1H | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1766 | offene_lage | gehaltene_form | druck_lage | -0.0444 | 0.0117 |
| BTC_2024_30M | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 605 | offene_lage | druck_lage | offene_lage | 0.1219 | -0.0100 |
| BTC_2024_30M | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 623 | offene_lage | offene_lage | offene_lage | 0.0798 | 0.0053 |
| BTC_2024_30M | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 672 | offene_lage | bewegungsbruch | offene_lage | -0.0563 | -0.0058 |
| BTC_2024_30M | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 747 | offene_lage | offene_lage | offene_lage | 0.1637 | -0.0332 |
| BTC_2024_30M | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 811 | offene_lage | offene_lage | offene_lage | 0.0023 | 0.0070 |
| BTC_2024_30M | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 849 | offene_lage | druck_lage | druck_lage | 0.2512 | -0.0207 |
| BTC_2024_30M | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1043 | offene_lage | offene_lage | offene_lage | 0.0737 | -0.0248 |
| BTC_2024_30M | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1378 | druck_lage | druck_lage | offene_lage | -0.1630 | -0.0077 |
| BTC_2024_30M | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1394 | offene_lage | druck_lage | offene_lage | 0.0151 | -0.0048 |
| BTC_2024_30M | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1399 | offene_lage | offene_lage | offene_lage | -0.0134 | -0.0116 |
| BTC_2024_30M | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1483 | druck_lage | druck_lage | druck_lage | -0.0390 | 0.0080 |
| BTC_2024_30M | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1524 | druck_lage | offene_lage | offene_lage | -0.0909 | 0.0261 |
| BTC_2024_30M | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1526 | offene_lage | offene_lage | druck_lage | 0.0615 | -0.0171 |
| BTC_2024_30M | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 604 | offene_lage | offene_lage | druck_lage | 0.1521 | -0.0255 |
| BTC_2024_30M | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 625 | offene_lage | offene_lage | offene_lage | -0.0906 | 0.0104 |
| BTC_2024_30M | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 689 | bewegungsbruch | offene_lage | offene_lage | -0.1109 | 0.0186 |
| BTC_2024_30M | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 804 | offene_lage | offene_lage | offene_lage | 0.0502 | -0.0144 |
| BTC_2024_30M | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 824 | offene_lage | offene_lage | offene_lage | 0.0169 | -0.0029 |
| BTC_2024_30M | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 955 | offene_lage | offene_lage | offene_lage | -0.0705 | 0.0042 |
| BTC_2024_30M | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1371 | druck_lage | offene_lage | offene_lage | -0.1413 | 0.0284 |
| BTC_2024_30M | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1386 | offene_lage | offene_lage | offene_lage | 0.0355 | -0.0017 |
| BTC_2024_30M | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1397 | offene_lage | offene_lage | offene_lage | -0.0021 | -0.0043 |
| BTC_2024_30M | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1402 | offene_lage | offene_lage | offene_lage | -0.1196 | 0.0336 |
| BTC_2024_30M | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1505 | offene_lage | offene_lage | offene_lage | 0.0305 | 0.0130 |
| BTC_2024_30M | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1525 | druck_lage | offene_lage | offene_lage | 0.0529 | 0.0057 |
| BTC_2024_30M | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1552 | offene_lage | offene_lage | offene_lage | -0.0055 | -0.0007 |
| BTC_2024_5M | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1314 | offene_lage | druck_lage | gehaltene_form | 0.1302 | -0.0193 |
| BTC_2024_5M | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1799 | offene_lage | druck_lage | bewegungsbruch | 0.0927 | 0.0080 |
| BTC_2024_5M | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1815 | offene_lage | offene_lage | offene_lage | -0.0444 | 0.0036 |
| BTC_2024_5M | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1313 | offene_lage | offene_lage | druck_lage | 0.1744 | -0.0274 |

## Befund

Die Rohwelt-Segmentlupe beschreibt das Milieu einer Feldbewegung.
Sie sagt nicht: Wenn dieses Segment kommt, dann muss diese Bewegung folgen.

Fachlich wichtig ist die Trennung:

```text
Rohwelt/Rezeptorlage = Kontaktmilieu
MCM-Preview-Wechsel = passive Feldbewegung
```

Damit bleibt die Diagnose organisch: Weltkontakt wird gelesen, aber nicht als Regel gesetzt.

## Wie es weitergeht

Als naechstes sollten die besten Milieus auf Wiederkehr und Drift geprueft werden.
Dann wird sichtbar, ob eine Feldbewegung an eine konkrete Weltlage gebunden ist oder mehrere Milieus tragen kann.
