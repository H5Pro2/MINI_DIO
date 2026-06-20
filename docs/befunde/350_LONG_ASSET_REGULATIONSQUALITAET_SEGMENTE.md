# Bewegungsarten Rohwelt-Segmente

Stand: 2026-06-20 01:12:47

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
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | nachher | 228 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0351 | 0.2202 | 0.2309 | 0.2241 | 0.8569 | 0.1955 | 0.6429 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | vorher | 228 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0332 | 0.2112 | 0.2329 | 0.2124 | 0.8698 | 0.1883 | 0.6491 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | wechsel | 114 | 4 | druck_lage | offene_variante | 0.0052 | 0.3153 | 0.3759 | 0.2901 | 0.7906 | 0.2374 | 0.6158 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | nachher | 262 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0142 | 0.1616 | 0.2206 | 0.1935 | 0.8787 | 0.1812 | 0.6524 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | vorher | 262 | 4 | rekoppelnde_lage | zentrum_stabil | -0.0241 | 0.1406 | 0.1798 | 0.1796 | 0.8898 | 0.1725 | 0.6567 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | wechsel | 131 | 4 | rekoppelnde_lage | zentrum_stabil | -0.0029 | 0.0943 | 0.1359 | 0.1504 | 0.9173 | 0.1467 | 0.6785 |

## Ereignislupe

| Welt | Paar | Tick | Vorher | Wechsel | Nachher | dDruck | dRekopplung |
|---|---|---:|---|---|---|---:|---:|
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 410 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.1118 | 0.0458 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 425 | rekoppelnde_lage | druck_lage | rekoppelnde_lage | 0.0574 | -0.0148 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 433 | rekoppelnde_lage | druck_lage | offene_lage | 0.0990 | -0.0406 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 526 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | 0.0502 | -0.0266 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 588 | rekoppelnde_lage | druck_lage | rekoppelnde_lage | 0.0066 | -0.0076 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 591 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0494 | -0.0177 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 593 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | -0.0123 | -0.0022 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1013 | rekoppelnde_lage | offene_lage | offene_lage | -0.0073 | 0.0021 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1028 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0900 | -0.0167 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1034 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0216 | -0.0047 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1084 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | 0.0122 | 0.0139 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1175 | rekoppelnde_lage | druck_lage | rekoppelnde_lage | -0.0860 | -0.0126 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1262 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0399 | -0.0323 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1270 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0798 | 0.0356 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1558 | rekoppelnde_lage | druck_lage | rekoppelnde_lage | 0.0362 | -0.0261 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1901 | rekoppelnde_lage | bewegungsbruch | rekoppelnde_lage | 0.0932 | -0.0269 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1915 | rekoppelnde_lage | druck_lage | bewegungsbruch | 0.0728 | -0.0358 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1936 | offene_lage | bewegungsbruch | rekoppelnde_lage | -0.0633 | 0.0033 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1941 | rekoppelnde_lage | rekoppelnde_lage | bewegungsbruch | 0.0767 | -0.0344 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2314 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | 0.0026 | 0.0152 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2343 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | -0.0044 | 0.0036 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2351 | rekoppelnde_lage | druck_lage | offene_lage | 0.0733 | -0.0157 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2379 | druck_lage | druck_lage | rekoppelnde_lage | -0.1580 | 0.0407 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2633 | rekoppelnde_lage | druck_lage | offene_lage | 0.0444 | -0.0458 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2809 | bewegungsbruch | rekoppelnde_lage | rekoppelnde_lage | -0.0736 | 0.0392 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2869 | rekoppelnde_lage | bewegungsbruch | rekoppelnde_lage | -0.1126 | 0.0141 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3194 | druck_lage | gehaltene_form | druck_lage | -0.0804 | 0.0038 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3205 | rekoppelnde_lage | druck_lage | bewegungsbruch | 0.1228 | -0.0030 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3208 | bewegungsbruch | offene_lage | rekoppelnde_lage | -0.0726 | -0.0051 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3217 | rekoppelnde_lage | offene_lage | bewegungsbruch | 0.0222 | 0.0058 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3229 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0056 | 0.0047 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3267 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0431 | -0.0070 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3436 | rekoppelnde_lage | druck_lage | bewegungsbruch | 0.1021 | -0.0272 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3539 | bewegungsbruch | bewegungsbruch | offene_lage | -0.0281 | -0.0057 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3868 | offene_lage | bewegungsbruch | rekoppelnde_lage | 0.0523 | -0.0202 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3882 | rekoppelnde_lage | offene_lage | bewegungsbruch | 0.0424 | -0.0290 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3910 | rekoppelnde_lage | druck_lage | offene_lage | 0.0951 | -0.0334 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 401 | rekoppelnde_lage | rekoppelnde_lage | offene_lage | 0.0726 | -0.0245 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 411 | druck_lage | rekoppelnde_lage | rekoppelnde_lage | -0.1033 | 0.0257 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 432 | rekoppelnde_lage | rekoppelnde_lage | druck_lage | 0.1898 | -0.0660 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 524 | rekoppelnde_lage | rekoppelnde_lage | offene_lage | 0.1459 | -0.0564 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 587 | rekoppelnde_lage | rekoppelnde_lage | druck_lage | 0.1389 | -0.0378 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 590 | druck_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0948 | 0.0136 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 592 | rekoppelnde_lage | rekoppelnde_lage | offene_lage | 0.0558 | -0.0156 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1001 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0027 | -0.0044 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1027 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0667 | -0.0114 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1033 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0188 | 0.0047 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1035 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0267 | -0.0158 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1076 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0594 | 0.0202 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1085 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0174 | 0.0185 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1161 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0573 | 0.0152 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1261 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0419 | -0.0335 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1263 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0185 | -0.0184 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1271 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0306 | 0.0125 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1557 | rekoppelnde_lage | rekoppelnde_lage | druck_lage | 0.1062 | -0.0618 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1586 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0131 | 0.0047 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1899 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0208 | -0.0225 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1907 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0523 | 0.0279 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1924 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0546 | 0.0512 |
| LONG_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1939 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0136 | -0.0067 |

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
