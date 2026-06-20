# Bewegungsarten Rohwelt-Segmente

Stand: 2026-06-20 08:18:08

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
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | nachher | 138 | 4 | rekoppelnde_lage | zentrum_stabil | 0.1073 | 0.2303 | 0.2462 | 0.2224 | 0.8658 | 0.1946 | 0.6454 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | vorher | 138 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0614 | 0.1832 | 0.2105 | 0.2027 | 0.8730 | 0.1851 | 0.6502 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | wechsel | 69 | 4 | druck_lage | offene_variante | 0.0518 | 0.2993 | 0.3666 | 0.2885 | 0.7998 | 0.2383 | 0.6164 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | nachher | 158 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0485 | 0.1886 | 0.2107 | 0.1978 | 0.8783 | 0.1826 | 0.6521 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | vorher | 158 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0470 | 0.1452 | 0.1669 | 0.1775 | 0.8893 | 0.1719 | 0.6572 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | wechsel | 79 | 4 | rekoppelnde_lage | zentrum_stabil | 0.1051 | 0.1094 | 0.1378 | 0.1570 | 0.9137 | 0.1514 | 0.6760 |

## Ereignislupe

| Welt | Paar | Tick | Vorher | Wechsel | Nachher | dDruck | dRekopplung |
|---|---|---:|---|---|---|---:|---:|
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 943 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0677 | 0.0266 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1536 | rekoppelnde_lage | druck_lage | rekoppelnde_lage | 0.0338 | -0.0187 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1546 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | -0.0383 | -0.0014 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1733 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0258 | 0.0087 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1746 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0130 | 0.0141 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1750 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | 0.0249 | 0.0026 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1900 | rekoppelnde_lage | bewegungsbruch | druck_lage | 0.0987 | -0.0195 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2114 | druck_lage | offene_lage | rekoppelnde_lage | -0.2073 | 0.0478 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2119 | gehaltene_form | rekoppelnde_lage | offene_lage | 0.0133 | -0.0376 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3385 | offene_lage | offene_lage | rekoppelnde_lage | -0.0214 | 0.0100 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3389 | rekoppelnde_lage | druck_lage | rekoppelnde_lage | 0.0803 | -0.0181 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3432 | offene_lage | druck_lage | offene_lage | -0.0585 | -0.0039 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3438 | offene_lage | bewegungsbruch | offene_lage | 0.0442 | -0.0243 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3444 | rekoppelnde_lage | druck_lage | rekoppelnde_lage | 0.0693 | -0.0150 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 940 | rekoppelnde_lage | rekoppelnde_lage | offene_lage | 0.1002 | -0.0245 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 944 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0138 | 0.0258 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1543 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0217 | 0.0007 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1721 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0354 | 0.0194 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1742 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0390 | 0.0043 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1748 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0256 | -0.0020 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1752 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0814 | 0.0499 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2102 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0317 | -0.0261 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2118 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | 0.0127 | -0.0254 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2882 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0235 | -0.0118 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3382 | rekoppelnde_lage | rekoppelnde_lage | offene_lage | 0.0556 | -0.0180 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3386 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0771 | 0.0300 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3413 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0915 | 0.0319 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3437 | rekoppelnde_lage | rekoppelnde_lage | bewegungsbruch | 0.0651 | -0.0318 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3442 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0701 | -0.0142 |
| LONG2025_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3446 | druck_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0688 | 0.0464 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2404 | rekoppelnde_lage | druck_lage | bewegungsbruch | 0.1216 | -0.0190 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2416 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | -0.0150 | 0.0137 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2427 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0114 | 0.0232 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2433 | bewegungsbruch | bewegungsbruch | rekoppelnde_lage | -0.0345 | -0.0072 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2449 | rekoppelnde_lage | druck_lage | bewegungsbruch | 0.0604 | 0.0026 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2826 | rekoppelnde_lage | gehaltene_form | offene_lage | -0.0209 | 0.0070 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2941 | rekoppelnde_lage | druck_lage | rekoppelnde_lage | 0.0955 | -0.0270 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3092 | offene_lage | offene_lage | rekoppelnde_lage | -0.0562 | 0.0265 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3096 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0400 | 0.0022 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3118 | bewegungsbruch | rekoppelnde_lage | rekoppelnde_lage | 0.0097 | 0.0020 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3120 | rekoppelnde_lage | druck_lage | druck_lage | 0.1597 | -0.0425 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3230 | druck_lage | offene_lage | rekoppelnde_lage | -0.0185 | -0.0060 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3232 | offene_lage | druck_lage | rekoppelnde_lage | -0.0131 | 0.0106 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3399 | rekoppelnde_lage | offene_lage | bewegungsbruch | 0.0318 | -0.0054 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3528 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0690 | 0.0222 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3924 | offene_lage | druck_lage | druck_lage | 0.2244 | -0.0568 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2125 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0200 | 0.0133 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2403 | rekoppelnde_lage | rekoppelnde_lage | druck_lage | 0.1572 | -0.0416 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2413 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0876 | -0.0038 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2417 | offene_lage | rekoppelnde_lage | offene_lage | -0.0502 | 0.0228 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2428 | rekoppelnde_lage | rekoppelnde_lage | offene_lage | 0.0097 | 0.0212 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2439 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0429 | -0.0110 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2650 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0072 | -0.0134 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2813 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0262 | 0.0355 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2939 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0745 | -0.0233 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3008 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0361 | 0.0119 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3080 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0414 | -0.0098 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3094 | offene_lage | offene_lage | rekoppelnde_lage | -0.0104 | -0.0024 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3098 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0030 | 0.0184 |
| LONG2025_5M_BTC_STRESS_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3119 | offene_lage | rekoppelnde_lage | druck_lage | 0.1563 | -0.0295 |

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
