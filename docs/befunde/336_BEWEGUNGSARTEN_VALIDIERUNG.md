# Bewegungsarten Validierung

Stand: 2026-06-20 00:01:47

## Zweck

Diese Diagnose prueft, ob die bisher gefundenen Preview-Uebergangsklassen auch in Bedingungswelten auftreten.
Sie ist passiv: keine Handlung, kein Gate, keine aktive Regulation.

## Hierarchie

1. Grundfrage: Sind die Bewegungsarten robuste Feldbewegungen oder nur Artefakte einer Weltmatrix?
2. Unterpruefung: Stress-, Seitwaerts- und Expansionswelten gegen die bekannten Preview-Uebergangspaare pruefen.
3. Folgeschritt: stabile Bewegungsarten koennen spaeter als passive Regulationswahrnehmung gelesen werden.

## Klassenuebersicht

| Klasse | Paare | Events | Welten-Summe | Top-Paar | dDruck | dSchaerfe | dRekopplung |
|---|---:|---:|---:|---|---:|---:|---:|
| gemischte_feldbewegung | 10 | 53 | 37 | dio_mcm_episode_14wxqua->dio_mcm_episode_1y00xwb | 0.0011 | -0.0321 | -0.0069 |
| grundinsel_wechsel | 2 | 31 | 11 | dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | -0.0136 | 0.0351 | 0.0130 |
| druck_rueckfuehrung | 7 | 30 | 20 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 0.1243 | -0.0495 | -0.0642 |
| rekopplungsbogen | 7 | 26 | 23 | dio_mcm_episode_1yv9fvu->dio_mcm_episode_1so7ez5 | -0.0298 | 0.0516 | 0.0205 |
| offener_uebergang | 2 | 14 | 6 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | 0.0338 | -0.1973 | -0.0196 |
| schaerfungsuebergang | 2 | 13 | 8 | dio_mcm_episode_0vkdfwc->dio_mcm_episode_1t5bcxp | -0.0061 | 0.0830 | 0.0037 |

## Top-Uebergangspaare

| Paar | Klasse | Anzahl | Welten | dominante Welt | Rollenwechsel | dDruck | dSchaerfe | dRekopplung |
|---|---|---:|---:|---|---|---:|---:|---:|
| dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | grundinsel_wechsel | 19 | 6 | POS_EXPANSION_2023 (6/19) | zentrum_stabil->zentrum_stabil (16/19) | -0.0087 | 0.0117 | 0.0128 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | offener_uebergang | 12 | 4 | POS_EXPANSION_2023 (5/12) | zentrum_stabil->offene_variante (4/12) | 0.0329 | -0.1692 | -0.0196 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | grundinsel_wechsel | 12 | 5 | EXT_EXPANSION_2023 (4/12) | zentrum_stabil->zentrum_stabil (12/12) | -0.0185 | 0.0585 | 0.0132 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_rueckfuehrung | 12 | 5 | EXT_EXPANSION_2023 (4/12) | zentrum_stabil->zentrum_stabil (4/12) | 0.0557 | -0.1048 | -0.0299 |
| dio_mcm_episode_14wxqua->dio_mcm_episode_1y00xwb | gemischte_feldbewegung | 11 | 5 | NEG_STRESS_2024 (5/11) | zentrum_stabil->zentrum_stabil (7/11) | -0.0005 | 0.0251 | 0.0005 |
| dio_mcm_episode_0vkdfwc->dio_mcm_episode_1t5bcxp | schaerfungsuebergang | 11 | 6 | NEG_STRESS_2024 (3/11) | zentrum_stabil->zentrum_stabil (10/11) | 0.0023 | 0.0712 | 0.0037 |
| dio_mcm_episode_1y00xwb->dio_mcm_episode_0vkdfwc | gemischte_feldbewegung | 8 | 6 | NEG_STRESS_2024 (3/8) | zentrum_stabil->zentrum_stabil (6/8) | -0.0088 | -0.0090 | -0.0082 |
| dio_mcm_episode_04e9yp5->dio_mcm_episode_14wxqua | gemischte_feldbewegung | 7 | 4 | SIDEWAYS_2024 (3/7) | zentrum_stabil->zentrum_stabil (6/7) | -0.0006 | 0.0119 | -0.0007 |
| dio_mcm_episode_1yv9fvu->dio_mcm_episode_1so7ez5 | rekopplungsbogen | 6 | 5 | SIDEWAYS_2024 (2/6) | zentrum_stabil->zentrum_stabil (4/6) | -0.0180 | 0.0991 | 0.0121 |
| dio_mcm_episode_1so7ez5->dio_mcm_episode_02xikfk | gemischte_feldbewegung | 6 | 3 | NEG_STRESS_2024 (3/6) | zentrum_stabil->zentrum_stabil (5/6) | 0.0124 | -0.1198 | -0.0011 |
| dio_mcm_episode_17i4j9o->dio_mcm_episode_0y50lf3 | druck_rueckfuehrung | 5 | 2 | SIDEWAYS_2024 (4/5) | zentrum_stabil->zentrum_stabil (2/5) | 0.0479 | 0.1809 | -0.0229 |
| dio_mcm_episode_0y50lf3->dio_mcm_episode_17i4j9o | rekopplungsbogen | 4 | 2 | SIDEWAYS_2024 (3/4) | zentrum_stabil->zentrum_stabil (3/4) | -0.0425 | 0.0600 | 0.0285 |
| dio_mcm_episode_0magw2b->dio_mcm_episode_1yv9fvu | rekopplungsbogen | 4 | 4 | SIDEWAYS_2024 (1/4) | spannungsrand_kippnaehe->offene_variante (1/4) | -0.0466 | -0.1126 | 0.0296 |
| dio_mcm_episode_177kjvc->dio_mcm_episode_03xfov3 | gemischte_feldbewegung | 4 | 3 | NEG_STRESS_2023 (2/4) | zentrum_stabil->zentrum_stabil (3/4) | -0.0084 | 0.0593 | -0.0075 |
| dio_mcm_episode_03724m4->dio_mcm_episode_0y0oxs9 | druck_rueckfuehrung | 4 | 4 | SIDEWAYS_2026 (1/4) | zentrum_stabil->offene_variante (3/4) | 0.0496 | -0.0617 | -0.0267 |
| dio_mcm_episode_0y0oxs9->dio_mcm_episode_009px6q | gemischte_feldbewegung | 4 | 4 | SIDEWAYS_2026 (1/4) | zentrum_stabil->zentrum_stabil (3/4) | 0.0139 | -0.0152 | -0.0086 |
| dio_mcm_episode_009px6q->dio_mcm_episode_0y50lf3 | rekopplungsbogen | 4 | 4 | SIDEWAYS_2026 (1/4) | zentrum_stabil->zentrum_stabil (3/4) | -0.0144 | 0.0215 | 0.0158 |
| dio_mcm_episode_0wxdilw->dio_mcm_episode_0magw2b | gemischte_feldbewegung | 4 | 3 | NEG_STRESS_2024 (2/4) | zentrum_stabil->zentrum_stabil (3/4) | -0.0137 | -0.0668 | 0.0054 |
| dio_mcm_episode_0wxdilw->dio_mcm_episode_04e9yp5 | rekopplungsbogen | 3 | 3 | SIDEWAYS_2024 (1/3) | zentrum_stabil->zentrum_stabil (2/3) | -0.0318 | 0.1399 | 0.0251 |
| dio_mcm_episode_12zl3pt->dio_mcm_episode_177kjvc | gemischte_feldbewegung | 3 | 3 | SIDEWAYS_2024 (1/3) | zentrum_stabil->zentrum_stabil (3/3) | 0.0234 | 0.0118 | -0.0210 |
| dio_mcm_episode_0u1i1ff->dio_mcm_episode_03724m4 | rekopplungsbogen | 3 | 3 | SIDEWAYS_2026 (1/3) | zentrum_stabil->zentrum_stabil (3/3) | -0.0152 | 0.0667 | 0.0092 |
| dio_mcm_episode_1ur03vd->dio_mcm_episode_02xikfk | gemischte_feldbewegung | 3 | 3 | SIDEWAYS_2026 (1/3) | zentrum_stabil->zentrum_stabil (2/3) | -0.0254 | -0.0831 | -0.0111 |
| dio_mcm_episode_0ifxej6->dio_mcm_episode_0x7d4av | gemischte_feldbewegung | 3 | 3 | NEG_STRESS_2023 (1/3) | zentrum_stabil->zentrum_stabil (2/3) | 0.0191 | -0.1355 | -0.0164 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_0l5wut9 | druck_rueckfuehrung | 3 | 3 | NEG_STRESS_2023 (1/3) | zentrum_stabil->spannungsrand_kippnaehe (3/3) | 0.1797 | 0.0029 | -0.0910 |
| dio_mcm_episode_0y50lf3->dio_mcm_episode_19cadje | druck_rueckfuehrung | 2 | 2 | SIDEWAYS_2024 (1/2) | zentrum_stabil->spannungsrand_kippnaehe (2/2) | 0.2464 | 0.0049 | -0.1135 |
| dio_mcm_episode_0ixmssr->dio_mcm_episode_04e9yp5 | schaerfungsuebergang | 2 | 2 | SIDEWAYS_2024 (1/2) | zentrum_stabil->zentrum_stabil (2/2) | -0.0145 | 0.0948 | 0.0037 |
| dio_mcm_episode_0vq085e->dio_mcm_episode_085wm7v | rekopplungsbogen | 2 | 2 | SIDEWAYS_2024 (1/2) | offene_variante->zentrum_stabil (1/2) | -0.0399 | 0.0868 | 0.0233 |
| dio_mcm_episode_085wm7v->dio_mcm_episode_1yv9fvu | offener_uebergang | 2 | 2 | SIDEWAYS_2024 (1/2) | zentrum_stabil->offene_variante (1/2) | 0.0347 | -0.2254 | -0.0196 |
| dio_mcm_episode_14wxqua->dio_mcm_episode_0magw2b | druck_rueckfuehrung | 2 | 2 | SIDEWAYS_2024 (1/2) | zentrum_stabil->spannungsrand_kippnaehe (1/2) | 0.0896 | -0.2220 | -0.0598 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_19a388p | druck_rueckfuehrung | 2 | 2 | SIDEWAYS_2024 (1/2) | zentrum_stabil->spannungsrand_kippnaehe (2/2) | 0.2014 | -0.1470 | -0.1053 |

## Befund

Die Bewegungsarten bleiben als Arbeitsklassen lesbar, wenn sie in mehreren Bedingungswelten wiederkehren.
Wichtig ist nicht nur die Haeufigkeit, sondern ob Druck, Schaerfe und Rekopplung dieselbe Bewegungsrichtung tragen.

Wenn ein Paar nur lokal oder nur in einer Welt erscheint, wird es als lokale Kante behandelt.
Wenn ein Paar weltuebergreifend erscheint, ist es ein Kandidat fuer eine passive Feldbewegung.

## Wie es weitergeht

Als naechstes sollten die stabilsten validierten Bewegungsarten gegen ihre Rohwelt-Segmente gelegt werden.
Dann wird sichtbar, welche Weltbewegung eine Feldbewegung ausloest, ohne daraus schon Handlung abzuleiten.
