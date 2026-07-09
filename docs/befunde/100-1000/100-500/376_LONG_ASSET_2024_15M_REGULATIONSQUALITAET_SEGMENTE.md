# Bewegungsarten Rohwelt-Segmente

Stand: 2026-06-20 08:30:48

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
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | nachher | 134 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0315 | 0.2334 | 0.2465 | 0.2256 | 0.8554 | 0.1970 | 0.6419 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | vorher | 134 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0372 | 0.1857 | 0.2094 | 0.2027 | 0.8721 | 0.1845 | 0.6513 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | wechsel | 67 | 4 | druck_lage | zentrum_stabil | 0.0833 | 0.2904 | 0.4183 | 0.3013 | 0.7685 | 0.2464 | 0.6116 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | nachher | 148 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0635 | 0.1698 | 0.2379 | 0.2015 | 0.8687 | 0.1839 | 0.6516 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | vorher | 148 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0464 | 0.1319 | 0.2154 | 0.1885 | 0.8875 | 0.1778 | 0.6554 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | wechsel | 74 | 4 | rekoppelnde_lage | zentrum_stabil | 0.1356 | 0.0918 | 0.1419 | 0.1537 | 0.9124 | 0.1514 | 0.6771 |

## Ereignislupe

| Welt | Paar | Tick | Vorher | Wechsel | Nachher | dDruck | dRekopplung |
|---|---|---:|---|---|---|---:|---:|
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 199 | rekoppelnde_lage | druck_lage | rekoppelnde_lage | -0.0024 | -0.0154 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 755 | rekoppelnde_lage | druck_lage | druck_lage | 0.0345 | 0.0089 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1690 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | -0.0215 | 0.0086 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1718 | rekoppelnde_lage | druck_lage | druck_lage | 0.1057 | -0.0203 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2133 | rekoppelnde_lage | druck_lage | offene_lage | -0.0659 | -0.0279 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2145 | offene_lage | offene_lage | rekoppelnde_lage | -0.0099 | -0.0048 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2273 | rekoppelnde_lage | bewegungsbruch | rekoppelnde_lage | -0.1213 | 0.0553 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2276 | rekoppelnde_lage | druck_lage | rekoppelnde_lage | 0.1179 | -0.0534 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2293 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0009 | 0.0117 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2296 | rekoppelnde_lage | druck_lage | rekoppelnde_lage | 0.0257 | -0.0097 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2307 | bewegungsbruch | bewegungsbruch | bewegungsbruch | -0.0087 | 0.0176 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2327 | rekoppelnde_lage | druck_lage | gehaltene_form | 0.1204 | -0.0284 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2532 | druck_lage | bewegungsbruch | offene_lage | -0.1048 | 0.0434 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2568 | rekoppelnde_lage | druck_lage | bewegungsbruch | 0.0636 | -0.0211 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2582 | rekoppelnde_lage | druck_lage | bewegungsbruch | 0.0503 | -0.0255 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2597 | rekoppelnde_lage | gehaltene_form | rekoppelnde_lage | 0.0473 | -0.0042 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2627 | offene_lage | offene_lage | rekoppelnde_lage | -0.0639 | 0.0305 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2689 | druck_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0971 | 0.0366 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2692 | rekoppelnde_lage | druck_lage | bewegungsbruch | 0.0244 | -0.0300 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2703 | rekoppelnde_lage | druck_lage | gehaltene_form | 0.0573 | -0.0077 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2709 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | -0.0214 | 0.0009 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2713 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | 0.0271 | -0.0115 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3047 | rekoppelnde_lage | gehaltene_form | gehaltene_form | 0.0777 | -0.0205 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3100 | rekoppelnde_lage | druck_lage | rekoppelnde_lage | 0.1372 | -0.0720 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3499 | rekoppelnde_lage | druck_lage | rekoppelnde_lage | 0.0686 | -0.0536 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3505 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0253 | -0.0111 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3508 | rekoppelnde_lage | bewegungsbruch | rekoppelnde_lage | 0.0259 | 0.0104 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3788 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | -0.0326 | -0.0252 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3804 | rekoppelnde_lage | offene_lage | offene_lage | 0.0388 | -0.0274 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3845 | rekoppelnde_lage | rekoppelnde_lage | offene_lage | 0.0434 | -0.0083 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 206 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0058 | -0.0035 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 749 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0211 | 0.0185 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1584 | rekoppelnde_lage | rekoppelnde_lage | druck_lage | 0.2298 | -0.0793 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1683 | rekoppelnde_lage | rekoppelnde_lage | bewegungsbruch | 0.0751 | 0.0031 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1691 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0856 | 0.0172 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2130 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.1715 | -0.0113 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2142 | rekoppelnde_lage | rekoppelnde_lage | offene_lage | 0.0734 | -0.0244 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2154 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0307 | 0.0199 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2274 | druck_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0281 | 0.0204 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2292 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0104 | -0.0258 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2295 | rekoppelnde_lage | rekoppelnde_lage | druck_lage | 0.0821 | -0.0141 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2298 | druck_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0885 | 0.0490 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2308 | rekoppelnde_lage | bewegungsbruch | rekoppelnde_lage | -0.0844 | 0.0322 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2547 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0297 | -0.0012 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2580 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.1222 | -0.0504 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2594 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0734 | 0.0099 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2598 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0137 | 0.0116 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2646 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0138 | 0.0048 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2690 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0533 | 0.0054 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2702 | rekoppelnde_lage | rekoppelnde_lage | druck_lage | 0.1028 | -0.0369 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2706 | gehaltene_form | rekoppelnde_lage | rekoppelnde_lage | -0.0397 | -0.0090 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2712 | rekoppelnde_lage | rekoppelnde_lage | offene_lage | 0.0348 | -0.0066 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2722 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0421 | 0.0122 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3021 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0292 | -0.0093 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3099 | rekoppelnde_lage | rekoppelnde_lage | druck_lage | 0.1073 | -0.0416 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3137 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0298 | 0.0127 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3498 | rekoppelnde_lage | rekoppelnde_lage | druck_lage | 0.1669 | -0.0831 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3504 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0007 | -0.0163 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3506 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0519 | -0.0237 |
| LONG2024_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3509 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0978 | 0.0263 |

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
