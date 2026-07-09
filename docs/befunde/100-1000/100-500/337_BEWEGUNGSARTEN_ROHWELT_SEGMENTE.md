# Bewegungsarten Rohwelt-Segmente

Stand: 2026-06-20 00:10:56

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
| dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | nachher | 38 | 6 | rekoppelnde_lage | zentrum_stabil | 0.0331 | 0.2704 | 0.2112 | 0.2184 | 0.8388 | 0.1964 | 0.6398 |
| dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | vorher | 38 | 6 | rekoppelnde_lage | zentrum_stabil | 0.0558 | 0.2496 | 0.2017 | 0.2325 | 0.8321 | 0.2041 | 0.6361 |
| dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | wechsel | 19 | 6 | rekoppelnde_lage | zentrum_stabil | 0.0634 | 0.2480 | 0.1910 | 0.2154 | 0.8930 | 0.1840 | 0.6533 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | nachher | 24 | 5 | rekoppelnde_lage | zentrum_stabil | 0.0212 | 0.1516 | 0.2116 | 0.2002 | 0.8713 | 0.1908 | 0.6441 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | vorher | 24 | 5 | rekoppelnde_lage | zentrum_stabil | 0.0865 | 0.1441 | 0.2455 | 0.2002 | 0.8679 | 0.1822 | 0.6543 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | wechsel | 12 | 5 | druck_lage | offene_variante | 0.0771 | 0.2177 | 0.4535 | 0.2987 | 0.7873 | 0.2425 | 0.6149 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | nachher | 24 | 4 | rekoppelnde_lage | zentrum_stabil | 0.1032 | 0.2828 | 0.1966 | 0.2418 | 0.8205 | 0.2058 | 0.6370 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | vorher | 24 | 4 | offene_lage | zentrum_stabil | 0.3697 | 0.2598 | 0.2661 | 0.2622 | 0.7930 | 0.2222 | 0.6298 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | wechsel | 12 | 4 | druck_lage | offene_variante | 0.2782 | 0.4588 | 0.3178 | 0.3086 | 0.7023 | 0.2476 | 0.6124 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | nachher | 24 | 5 | rekoppelnde_lage | zentrum_stabil | 0.1646 | 0.1259 | 0.2545 | 0.2008 | 0.8723 | 0.1902 | 0.6469 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | vorher | 24 | 5 | rekoppelnde_lage | zentrum_stabil | 0.0460 | 0.1135 | 0.1373 | 0.1647 | 0.8939 | 0.1734 | 0.6528 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | wechsel | 12 | 5 | rekoppelnde_lage | zentrum_stabil | 0.1009 | 0.0779 | 0.1203 | 0.1450 | 0.8996 | 0.1505 | 0.6721 |

## Ereignislupe

| Welt | Paar | Tick | Vorher | Wechsel | Nachher | dDruck | dRekopplung |
|---|---|---:|---|---|---|---:|---:|
| EXT_EXPANSION_2023 | dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | 394 | offene_lage | offene_lage | rekoppelnde_lage | 0.0249 | -0.0162 |
| EXT_EXPANSION_2023 | dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | 397 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | -0.0360 | -0.0023 |
| EXT_EXPANSION_2023 | dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | 660 | offene_lage | rekoppelnde_lage | bewegungsbruch | 0.0133 | -0.0138 |
| EXT_EXPANSION_2023 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 506 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0313 | 0.0148 |
| EXT_EXPANSION_2023 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 509 | rekoppelnde_lage | bewegungsbruch | rekoppelnde_lage | -0.0381 | -0.0054 |
| EXT_EXPANSION_2023 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 515 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0145 | -0.0019 |
| EXT_EXPANSION_2023 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 526 | rekoppelnde_lage | druck_lage | bewegungsbruch | -0.0768 | -0.0046 |
| EXT_EXPANSION_2023 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | 396 | offene_lage | druck_lage | offene_lage | -0.0170 | -0.0256 |
| EXT_EXPANSION_2023 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | 398 | druck_lage | rekoppelnde_lage | bewegungsbruch | -0.0694 | 0.0151 |
| EXT_EXPANSION_2023 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | 655 | gehaltene_form | druck_lage | bewegungsbruch | 0.0640 | -0.0030 |
| EXT_EXPANSION_2023 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 503 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0197 | -0.0182 |
| EXT_EXPANSION_2023 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 507 | rekoppelnde_lage | rekoppelnde_lage | bewegungsbruch | 0.1052 | -0.0126 |
| EXT_EXPANSION_2023 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 514 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0446 | -0.0263 |
| EXT_EXPANSION_2023 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 517 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0464 | 0.0264 |
| NEG_STRESS_2023 | dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | 264 | rekoppelnde_lage | rekoppelnde_lage | offene_lage | -0.0040 | 0.0177 |
| NEG_STRESS_2023 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 802 | offene_lage | druck_lage | rekoppelnde_lage | -0.0153 | 0.0206 |
| NEG_STRESS_2023 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 816 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.1305 | -0.0298 |
| NEG_STRESS_2023 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 771 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0019 | 0.0259 |
| NEG_STRESS_2023 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 815 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0810 | -0.0072 |
| NEG_STRESS_2024 | dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | 700 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0843 | 0.0409 |
| NEG_STRESS_2024 | dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | 763 | offene_lage | offene_lage | offene_lage | -0.0161 | 0.0137 |
| NEG_STRESS_2024 | dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | 961 | rekoppelnde_lage | rekoppelnde_lage | bewegungsbruch | 0.0701 | 0.0003 |
| NEG_STRESS_2024 | dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | 974 | druck_lage | offene_lage | offene_lage | -0.1343 | 0.0274 |
| NEG_STRESS_2024 | dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | 977 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0467 | 0.0122 |
| NEG_STRESS_2024 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | 760 | druck_lage | bewegungsbruch | offene_lage | -0.1013 | 0.0320 |
| NEG_STRESS_2024 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | 973 | offene_lage | druck_lage | offene_lage | -0.0421 | 0.0272 |
| NEG_STRESS_2024 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | 975 | druck_lage | offene_lage | bewegungsbruch | -0.1012 | -0.0013 |
| POS_EXPANSION_2023 | dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | 228 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | 0.0762 | -0.0152 |
| POS_EXPANSION_2023 | dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | 247 | bewegungsbruch | rekoppelnde_lage | rekoppelnde_lage | -0.0720 | -0.0199 |
| POS_EXPANSION_2023 | dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | 328 | rekoppelnde_lage | rekoppelnde_lage | druck_lage | 0.1390 | -0.0361 |
| POS_EXPANSION_2023 | dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | 332 | bewegungsbruch | rekoppelnde_lage | rekoppelnde_lage | -0.0792 | 0.0234 |
| POS_EXPANSION_2023 | dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | 341 | offene_lage | bewegungsbruch | bewegungsbruch | -0.0197 | 0.0092 |
| POS_EXPANSION_2023 | dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | 356 | gehaltene_form | rekoppelnde_lage | rekoppelnde_lage | -0.0605 | 0.0156 |
| POS_EXPANSION_2023 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 572 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0347 | -0.0258 |
| POS_EXPANSION_2023 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 646 | druck_lage | offene_lage | rekoppelnde_lage | -0.1412 | 0.0071 |
| POS_EXPANSION_2023 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 653 | rekoppelnde_lage | druck_lage | bewegungsbruch | 0.1413 | -0.0428 |
| POS_EXPANSION_2023 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | 235 | bewegungsbruch | gehaltene_form | gehaltene_form | -0.0237 | 0.0114 |
| POS_EXPANSION_2023 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | 326 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0163 | 0.0078 |
| POS_EXPANSION_2023 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | 329 | rekoppelnde_lage | druck_lage | bewegungsbruch | 0.0421 | -0.0204 |
| POS_EXPANSION_2023 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | 339 | offene_lage | offene_lage | offene_lage | 0.0660 | 0.0079 |
| POS_EXPANSION_2023 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | 355 | rekoppelnde_lage | bewegungsbruch | rekoppelnde_lage | -0.0328 | 0.0112 |
| POS_EXPANSION_2023 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 571 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0304 | -0.0223 |
| POS_EXPANSION_2023 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 576 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0542 | 0.0187 |
| POS_EXPANSION_2023 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 651 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.1854 | -0.0275 |
| SIDEWAYS_2024 | dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | 608 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0058 | -0.0016 |
| SIDEWAYS_2024 | dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | 636 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | -0.0030 | -0.0038 |
| SIDEWAYS_2024 | dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | 665 | bewegungsbruch | rekoppelnde_lage | rekoppelnde_lage | -0.0481 | 0.0184 |
| SIDEWAYS_2024 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 920 | rekoppelnde_lage | druck_lage | rekoppelnde_lage | 0.0509 | -0.0366 |
| SIDEWAYS_2024 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 934 | bewegungsbruch | offene_lage | bewegungsbruch | -0.0309 | -0.0140 |
| SIDEWAYS_2024 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | 661 | bewegungsbruch | druck_lage | rekoppelnde_lage | -0.0458 | 0.0234 |
| SIDEWAYS_2024 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 917 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0069 | 0.0090 |
| SIDEWAYS_2024 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 927 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0365 | -0.0017 |
| SIDEWAYS_2026 | dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | 434 | offene_lage | bewegungsbruch | bewegungsbruch | 0.0067 | 0.0015 |
| SIDEWAYS_2026 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 906 | rekoppelnde_lage | bewegungsbruch | rekoppelnde_lage | -0.0031 | -0.0035 |
| SIDEWAYS_2026 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 905 | rekoppelnde_lage | rekoppelnde_lage | bewegungsbruch | 0.1013 | -0.0351 |

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
