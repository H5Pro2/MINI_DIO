# Bewegungsarten Rohwelt-Segmente

Stand: 2026-06-20 08:30:52

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
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | nachher | 128 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0457 | 0.2022 | 0.2465 | 0.2185 | 0.8577 | 0.1931 | 0.6446 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | vorher | 128 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0656 | 0.2068 | 0.2495 | 0.2155 | 0.8665 | 0.1901 | 0.6480 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | wechsel | 64 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0737 | 0.2646 | 0.3705 | 0.2667 | 0.7920 | 0.2294 | 0.6203 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | nachher | 154 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0304 | 0.1699 | 0.2380 | 0.1943 | 0.8787 | 0.1797 | 0.6540 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | vorher | 154 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0583 | 0.1362 | 0.2184 | 0.1832 | 0.8856 | 0.1769 | 0.6541 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | wechsel | 77 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0998 | 0.0997 | 0.1376 | 0.1502 | 0.9125 | 0.1463 | 0.6795 |

## Ereignislupe

| Welt | Paar | Tick | Vorher | Wechsel | Nachher | dDruck | dRekopplung |
|---|---|---:|---|---|---|---:|---:|
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1620 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0221 | -0.0113 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1631 | bewegungsbruch | rekoppelnde_lage | rekoppelnde_lage | -0.0636 | 0.0022 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1637 | rekoppelnde_lage | druck_lage | rekoppelnde_lage | 0.0309 | -0.0133 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1646 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | 0.0148 | -0.0067 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1707 | offene_lage | rekoppelnde_lage | bewegungsbruch | 0.0440 | 0.0035 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1715 | rekoppelnde_lage | bewegungsbruch | gehaltene_form | -0.0701 | -0.0111 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1833 | rekoppelnde_lage | druck_lage | offene_lage | 0.1679 | -0.0403 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2133 | rekoppelnde_lage | offene_lage | offene_lage | -0.0256 | -0.0103 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2142 | rekoppelnde_lage | druck_lage | bewegungsbruch | -0.0591 | -0.0020 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2515 | rekoppelnde_lage | druck_lage | bewegungsbruch | 0.0481 | -0.0072 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2525 | rekoppelnde_lage | bewegungsbruch | rekoppelnde_lage | -0.0394 | 0.0017 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2567 | druck_lage | offene_lage | offene_lage | -0.1993 | 0.0233 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2762 | rekoppelnde_lage | druck_lage | bewegungsbruch | 0.1121 | -0.0399 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2816 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0473 | 0.0090 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2848 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.1456 | -0.0498 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3007 | rekoppelnde_lage | druck_lage | rekoppelnde_lage | -0.0945 | 0.0394 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3411 | offene_lage | bewegungsbruch | offene_lage | -0.0226 | 0.0178 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3420 | rekoppelnde_lage | offene_lage | offene_lage | -0.0003 | 0.0085 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3427 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0435 | 0.0182 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3436 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | -0.0968 | 0.0246 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3439 | rekoppelnde_lage | bewegungsbruch | bewegungsbruch | 0.0457 | -0.0168 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3481 | rekoppelnde_lage | druck_lage | offene_lage | -0.1260 | 0.0394 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3731 | gehaltene_form | gehaltene_form | druck_lage | 0.0827 | -0.0256 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3871 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0762 | 0.0470 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1147 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0294 | 0.0181 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1454 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0969 | 0.0203 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1619 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0200 | -0.0133 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1621 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0801 | -0.0114 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1635 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0882 | -0.0202 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1643 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0275 | -0.0032 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1653 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0185 | 0.0309 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1711 | bewegungsbruch | rekoppelnde_lage | rekoppelnde_lage | -0.0228 | 0.0016 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1832 | rekoppelnde_lage | rekoppelnde_lage | druck_lage | 0.1692 | -0.0354 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2113 | rekoppelnde_lage | rekoppelnde_lage | offene_lage | 0.0398 | -0.0131 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2136 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0794 | 0.0221 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2158 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0058 | 0.0198 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2523 | offene_lage | rekoppelnde_lage | bewegungsbruch | 0.0613 | -0.0182 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2526 | bewegungsbruch | rekoppelnde_lage | rekoppelnde_lage | -0.0638 | 0.0361 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2761 | rekoppelnde_lage | rekoppelnde_lage | druck_lage | 0.2044 | -0.0578 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2772 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0077 | 0.0110 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2817 | bewegungsbruch | rekoppelnde_lage | rekoppelnde_lage | -0.0691 | 0.0281 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2849 | rekoppelnde_lage | rekoppelnde_lage | druck_lage | 0.3002 | -0.0871 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2984 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0515 | -0.0029 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3009 | druck_lage | rekoppelnde_lage | rekoppelnde_lage | -0.1482 | 0.0554 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3393 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0135 | 0.0220 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3417 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0144 | -0.0047 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3423 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0473 | 0.0070 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3429 | rekoppelnde_lage | rekoppelnde_lage | gehaltene_form | 0.0476 | 0.0256 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3438 | offene_lage | rekoppelnde_lage | bewegungsbruch | 0.0629 | -0.0045 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3446 | rekoppelnde_lage | rekoppelnde_lage | gehaltene_form | 0.0802 | -0.0054 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3491 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0713 | 0.0273 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3867 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0017 | -0.0250 |
| LONG2024_5M_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3872 | bewegungsbruch | rekoppelnde_lage | rekoppelnde_lage | -0.0797 | 0.0410 |
| LONG2024_5M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 268 | bewegungsbruch | rekoppelnde_lage | rekoppelnde_lage | 0.0162 | -0.0061 |
| LONG2024_5M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 270 | rekoppelnde_lage | bewegungsbruch | bewegungsbruch | 0.0398 | -0.0054 |
| LONG2024_5M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 484 | druck_lage | druck_lage | offene_lage | -0.0869 | 0.0248 |
| LONG2024_5M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 486 | druck_lage | rekoppelnde_lage | rekoppelnde_lage | -0.1129 | 0.0158 |
| LONG2024_5M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 497 | druck_lage | bewegungsbruch | rekoppelnde_lage | -0.0853 | 0.0160 |
| LONG2024_5M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 682 | gehaltene_form | offene_lage | rekoppelnde_lage | 0.0153 | -0.0168 |
| LONG2024_5M_BTC_STRESS_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 729 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0287 | -0.0066 |

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
