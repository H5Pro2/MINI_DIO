# Bewegungsarten Rohwelt-Segmente

Stand: 2026-06-20 01:31:29

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
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | nachher | 160 | 4 | rekoppelnde_lage | zentrum_stabil | -0.0064 | 0.1991 | 0.2482 | 0.2131 | 0.8724 | 0.1912 | 0.6446 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | vorher | 160 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0391 | 0.1816 | 0.2222 | 0.2044 | 0.8750 | 0.1855 | 0.6501 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | wechsel | 80 | 4 | offene_lage | zentrum_stabil | 0.0224 | 0.2514 | 0.3754 | 0.2719 | 0.8068 | 0.2305 | 0.6200 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | nachher | 182 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0178 | 0.1528 | 0.2143 | 0.1868 | 0.8821 | 0.1788 | 0.6527 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | vorher | 182 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0876 | 0.1347 | 0.2137 | 0.1772 | 0.8857 | 0.1743 | 0.6565 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | wechsel | 91 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0870 | 0.0946 | 0.1396 | 0.1518 | 0.9120 | 0.1491 | 0.6766 |

## Ereignislupe

| Welt | Paar | Tick | Vorher | Wechsel | Nachher | dDruck | dRekopplung |
|---|---|---:|---|---|---|---:|---:|
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 738 | druck_lage | rekoppelnde_lage | rekoppelnde_lage | -0.1189 | 0.0347 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 769 | offene_lage | offene_lage | rekoppelnde_lage | -0.0469 | -0.0014 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 780 | rekoppelnde_lage | druck_lage | bewegungsbruch | 0.1117 | -0.0303 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1614 | rekoppelnde_lage | offene_lage | bewegungsbruch | 0.0599 | -0.0244 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1625 | offene_lage | rekoppelnde_lage | offene_lage | 0.0247 | -0.0097 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1695 | rekoppelnde_lage | druck_lage | bewegungsbruch | 0.0215 | -0.0252 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2516 | bewegungsbruch | bewegungsbruch | rekoppelnde_lage | -0.0032 | 0.0010 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2518 | bewegungsbruch | druck_lage | bewegungsbruch | -0.0181 | -0.0188 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2574 | gehaltene_form | offene_lage | rekoppelnde_lage | -0.0651 | 0.0044 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2576 | offene_lage | rekoppelnde_lage | offene_lage | 0.0051 | 0.0080 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2582 | offene_lage | offene_lage | rekoppelnde_lage | 0.0047 | -0.0245 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2594 | rekoppelnde_lage | druck_lage | offene_lage | 0.1538 | -0.0389 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2648 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | 0.0867 | -0.0283 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2654 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | -0.0371 | -0.0024 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2673 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0762 | 0.0521 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2691 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | 0.0351 | 0.0002 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2693 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0654 | 0.0166 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2701 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0540 | 0.0225 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2839 | offene_lage | rekoppelnde_lage | offene_lage | -0.0264 | 0.0145 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2846 | rekoppelnde_lage | druck_lage | offene_lage | 0.1101 | -0.0254 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2855 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | 0.0183 | -0.0227 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2960 | bewegungsbruch | offene_lage | rekoppelnde_lage | 0.0146 | -0.0008 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3426 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | 0.0061 | 0.0059 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3428 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0554 | 0.0307 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3437 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | -0.0201 | -0.0008 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3581 | bewegungsbruch | offene_lage | bewegungsbruch | -0.0476 | 0.0219 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3822 | offene_lage | druck_lage | druck_lage | 0.0610 | -0.0310 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 723 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0042 | 0.0027 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 739 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0595 | 0.0217 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 775 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0358 | -0.0164 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1612 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0609 | 0.0230 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1618 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0214 | 0.0021 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1688 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0508 | -0.0056 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2510 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0683 | 0.0011 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2517 | bewegungsbruch | rekoppelnde_lage | druck_lage | 0.0391 | -0.0287 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2523 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0393 | -0.0098 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2575 | gehaltene_form | rekoppelnde_lage | rekoppelnde_lage | -0.0103 | -0.0002 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2581 | offene_lage | rekoppelnde_lage | offene_lage | -0.0216 | -0.0112 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2593 | rekoppelnde_lage | rekoppelnde_lage | druck_lage | 0.1748 | -0.0442 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2647 | rekoppelnde_lage | rekoppelnde_lage | offene_lage | 0.1103 | -0.0367 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2652 | rekoppelnde_lage | rekoppelnde_lage | offene_lage | 0.0972 | -0.0198 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2661 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0546 | -0.0097 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2674 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.1211 | 0.0585 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2692 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0134 | 0.0016 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2695 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0115 | 0.0048 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2703 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0390 | 0.0360 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2841 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0451 | 0.0356 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2853 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0640 | -0.0407 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2858 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0327 | 0.0144 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3305 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0642 | 0.0230 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3420 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0812 | 0.0074 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3427 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0202 | 0.0141 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3429 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0838 | 0.0032 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3447 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0077 | 0.0354 |
| LONG2025_15M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3816 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0118 | -0.0166 |
| LONG2025_15M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 896 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | -0.0225 | -0.0210 |
| LONG2025_15M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 901 | rekoppelnde_lage | offene_lage | bewegungsbruch | 0.0664 | -0.0249 |
| LONG2025_15M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 905 | rekoppelnde_lage | rekoppelnde_lage | offene_lage | 0.0369 | -0.0081 |
| LONG2025_15M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 917 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0266 | 0.0103 |
| LONG2025_15M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1174 | rekoppelnde_lage | bewegungsbruch | rekoppelnde_lage | -0.0062 | 0.0240 |

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
