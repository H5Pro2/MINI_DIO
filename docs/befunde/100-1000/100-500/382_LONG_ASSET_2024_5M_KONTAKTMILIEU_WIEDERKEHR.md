# Kontaktmilieu Wiederkehr Und Drift

Stand: 2026-06-20 08:30:52

## Zweck

Diese Diagnose prueft, ob die Kontaktmilieus um passive Feldbewegungen wiederkehren oder pro Welt driften.
Sie bleibt passiv: keine Handlung, kein Gate, keine aktive Regulation.

## Hierarchie

1. Grundfrage: Traegt dieselbe Feldbewegung ein wiederkehrendes Kontaktmilieu?
2. Unterpruefung: Vorher-Wechsel-Nachher-Signaturen pro Paar und Welt vergleichen.
3. Folgeschritt: stabile Milieus als passive Ausloesemilieus beobachten, nicht als Regeln verwenden.

## Paaruebersicht

| Paar | Events | Welten | Signaturen | Top-Signatur | Anteil | dDruck | Druck-Streuung | dRekopplung | Rekopplung-Streuung | Driftlabel |
|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 77 | 4 | 15 | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 0.5195 | 0.0111 | 0.0747 | -0.0001 | 0.0234 | wiederkehrend_variabel |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 64 | 4 | 30 | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 0.2031 | 0.0031 | 0.0737 | -0.0033 | 0.0206 | lokal_offen |

## Signaturdetails

| Paar | Signatur | Events | Welten | Anteil | dDruck | dRekopplung |
|---|---|---:|---:|---:|---:|---:|
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 40 | 4 | 0.5195 | 0.0113 | -0.0014 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | offene_lage->rekoppelnde_lage->rekoppelnde_lage | 9 | 3 | 0.1169 | -0.0407 | 0.0113 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | bewegungsbruch->rekoppelnde_lage->rekoppelnde_lage | 7 | 3 | 0.0909 | -0.0642 | 0.0170 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->druck_lage | 5 | 2 | 0.0649 | 0.1883 | -0.0450 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->offene_lage | 2 | 2 | 0.0260 | 0.0390 | -0.0124 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | offene_lage->rekoppelnde_lage->bewegungsbruch | 2 | 1 | 0.0260 | 0.0621 | -0.0113 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | druck_lage->rekoppelnde_lage->rekoppelnde_lage | 2 | 2 | 0.0260 | -0.1429 | 0.0458 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->gehaltene_form | 2 | 1 | 0.0260 | 0.0639 | 0.0101 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->offene_lage->rekoppelnde_lage | 2 | 1 | 0.0260 | 0.0438 | -0.0041 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->bewegungsbruch | 1 | 1 | 0.0130 | 0.1092 | -0.0284 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | offene_lage->offene_lage->rekoppelnde_lage | 1 | 1 | 0.0130 | -0.0768 | 0.0230 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | bewegungsbruch->rekoppelnde_lage->druck_lage | 1 | 1 | 0.0130 | 0.1225 | -0.0379 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | offene_lage->rekoppelnde_lage->offene_lage | 1 | 1 | 0.0130 | 0.0290 | 0.0058 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | bewegungsbruch->rekoppelnde_lage->offene_lage | 1 | 1 | 0.0130 | -0.0191 | 0.0134 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | gehaltene_form->rekoppelnde_lage->rekoppelnde_lage | 1 | 1 | 0.0130 | -0.0194 | 0.0178 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 13 | 4 | 0.2031 | -0.0083 | -0.0030 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->offene_lage->rekoppelnde_lage | 6 | 3 | 0.0938 | -0.0088 | -0.0017 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->bewegungsbruch | 6 | 3 | 0.0938 | 0.0472 | -0.0177 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->rekoppelnde_lage | 3 | 2 | 0.0469 | 0.0200 | -0.0004 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->offene_lage | 3 | 2 | 0.0469 | 0.0044 | 0.0029 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->offene_lage->offene_lage | 3 | 2 | 0.0469 | 0.0061 | -0.0028 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->bewegungsbruch->bewegungsbruch | 3 | 2 | 0.0469 | 0.0366 | -0.0052 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->rekoppelnde_lage->rekoppelnde_lage | 2 | 2 | 0.0312 | -0.0237 | -0.0019 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->bewegungsbruch->rekoppelnde_lage | 2 | 2 | 0.0312 | -0.0570 | -0.0013 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->druck_lage->druck_lage | 2 | 2 | 0.0312 | 0.1628 | -0.0336 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->offene_lage->rekoppelnde_lage | 2 | 1 | 0.0312 | 0.0161 | 0.0014 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->rekoppelnde_lage->bewegungsbruch | 1 | 1 | 0.0156 | 0.0440 | 0.0035 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->bewegungsbruch->gehaltene_form | 1 | 1 | 0.0156 | -0.0701 | -0.0111 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->offene_lage->offene_lage | 1 | 1 | 0.0156 | -0.1993 | 0.0233 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->bewegungsbruch->offene_lage | 1 | 1 | 0.0156 | -0.0226 | 0.0178 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | gehaltene_form->gehaltene_form->druck_lage | 1 | 1 | 0.0156 | 0.0828 | -0.0256 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->druck_lage->offene_lage | 1 | 1 | 0.0156 | -0.0869 | 0.0248 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->rekoppelnde_lage->rekoppelnde_lage | 1 | 1 | 0.0156 | -0.1129 | 0.0158 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->bewegungsbruch->rekoppelnde_lage | 1 | 1 | 0.0156 | -0.0853 | 0.0160 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | gehaltene_form->offene_lage->rekoppelnde_lage | 1 | 1 | 0.0156 | 0.0153 | -0.0168 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->offene_lage->bewegungsbruch | 1 | 1 | 0.0156 | 0.0566 | -0.0089 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->offene_lage->rekoppelnde_lage | 1 | 1 | 0.0156 | 0.0544 | -0.0178 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->druck_lage->bewegungsbruch | 1 | 1 | 0.0156 | 0.0509 | -0.0029 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->druck_lage->bewegungsbruch | 1 | 1 | 0.0156 | -0.0481 | 0.0431 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->bewegungsbruch->rekoppelnde_lage | 1 | 1 | 0.0156 | -0.0025 | 0.0128 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->rekoppelnde_lage->rekoppelnde_lage | 1 | 1 | 0.0156 | -0.0510 | 0.0069 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->rekoppelnde_lage->bewegungsbruch | 1 | 1 | 0.0156 | -0.0476 | 0.0071 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->bewegungsbruch->offene_lage | 1 | 1 | 0.0156 | -0.0356 | -0.0289 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->rekoppelnde_lage->offene_lage | 1 | 1 | 0.0156 | 0.0438 | 0.0087 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->bewegungsbruch->gehaltene_form | 1 | 1 | 0.0156 | 0.0899 | -0.0382 |

## Befund

Stabile Milieus: 0
Variable wiederkehrende Milieus: 1

Ein wiederkehrendes Kontaktmilieu bedeutet hier nicht, dass die Feldbewegung mechanisch ausgeloest wird.
Es bedeutet: Die Feldbewegung erscheint in einem aehnlichen Rezeptor-/Innenfeld-Kontext wieder.

Das ist fuer MINI_DIO wichtig, weil dadurch Bedeutung nicht nur als Insel, sondern als Lagefolge gelesen werden kann.

## Wie es weitergeht

Als naechstes sollten stabile Milieus gegen laengere Welten geprueft werden.
Wenn sie dort stabil bleiben, koennen sie als passive Regulationswahrnehmung dokumentiert werden.
