# Kontaktmilieu Wiederkehr Und Drift

Stand: 2026-06-20 01:31:30

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
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 91 | 4 | 13 | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 0.6374 | 0.0097 | 0.0658 | -0.0038 | 0.0269 | wiederkehrend_stabil |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 80 | 4 | 36 | rekoppelnde_lage->offene_lage->rekoppelnde_lage | 0.1500 | 0.0087 | 0.0717 | -0.0055 | 0.0261 | lokal_offen |

## Signaturdetails

| Paar | Signatur | Events | Welten | Anteil | dDruck | dRekopplung |
|---|---|---:|---:|---:|---:|---:|
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 58 | 4 | 0.6374 | 0.0075 | -0.0003 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | offene_lage->rekoppelnde_lage->rekoppelnde_lage | 11 | 4 | 0.1209 | -0.0443 | 0.0153 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->offene_lage | 8 | 3 | 0.0879 | 0.0853 | -0.0349 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | bewegungsbruch->rekoppelnde_lage->rekoppelnde_lage | 4 | 2 | 0.0440 | -0.0485 | 0.0066 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | offene_lage->rekoppelnde_lage->druck_lage | 2 | 1 | 0.0220 | 0.1517 | -0.0674 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | bewegungsbruch->rekoppelnde_lage->druck_lage | 1 | 1 | 0.0110 | 0.0391 | -0.0287 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | gehaltene_form->rekoppelnde_lage->rekoppelnde_lage | 1 | 1 | 0.0110 | -0.0103 | -0.0002 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | offene_lage->rekoppelnde_lage->offene_lage | 1 | 1 | 0.0110 | -0.0216 | -0.0112 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->druck_lage | 1 | 1 | 0.0110 | 0.1748 | -0.0442 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | druck_lage->rekoppelnde_lage->rekoppelnde_lage | 1 | 1 | 0.0110 | -0.0909 | 0.0054 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->bewegungsbruch->bewegungsbruch | 1 | 1 | 0.0110 | 0.0080 | -0.0087 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->bewegungsbruch | 1 | 1 | 0.0110 | 0.0759 | -0.0249 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | bewegungsbruch->offene_lage->offene_lage | 1 | 1 | 0.0110 | -0.0378 | -0.0016 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->offene_lage->rekoppelnde_lage | 12 | 4 | 0.1500 | 0.0170 | -0.0077 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 9 | 4 | 0.1125 | -0.0249 | 0.0073 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->offene_lage->rekoppelnde_lage | 4 | 3 | 0.0500 | -0.0233 | 0.0051 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->bewegungsbruch->rekoppelnde_lage | 4 | 3 | 0.0500 | 0.0146 | 0.0122 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->offene_lage->bewegungsbruch | 3 | 3 | 0.0375 | 0.0585 | -0.0236 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->rekoppelnde_lage->offene_lage | 3 | 1 | 0.0375 | 0.0011 | 0.0043 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->offene_lage | 3 | 2 | 0.0375 | 0.1000 | -0.0257 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->rekoppelnde_lage->rekoppelnde_lage | 3 | 1 | 0.0375 | -0.0583 | 0.0233 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->offene_lage->rekoppelnde_lage | 3 | 3 | 0.0375 | -0.0569 | 0.0111 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->rekoppelnde_lage | 3 | 2 | 0.0375 | 0.0334 | -0.0144 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->bewegungsbruch | 2 | 1 | 0.0250 | 0.0666 | -0.0277 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->bewegungsbruch->rekoppelnde_lage | 2 | 2 | 0.0250 | -0.0330 | 0.0066 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | gehaltene_form->offene_lage->rekoppelnde_lage | 2 | 2 | 0.0250 | -0.0637 | -0.0045 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->rekoppelnde_lage->rekoppelnde_lage | 2 | 2 | 0.0250 | -0.0805 | 0.0173 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->bewegungsbruch->bewegungsbruch | 2 | 2 | 0.0250 | 0.0296 | -0.0087 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->bewegungsbruch->rekoppelnde_lage | 2 | 1 | 0.0250 | -0.0511 | 0.0001 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->druck_lage | 2 | 2 | 0.0250 | 0.1661 | -0.0567 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->rekoppelnde_lage->rekoppelnde_lage | 1 | 1 | 0.0125 | -0.1189 | 0.0347 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->druck_lage->bewegungsbruch | 1 | 1 | 0.0125 | -0.0181 | -0.0188 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->offene_lage->bewegungsbruch | 1 | 1 | 0.0125 | -0.0476 | 0.0219 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->druck_lage->druck_lage | 1 | 1 | 0.0125 | 0.0610 | -0.0310 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->rekoppelnde_lage->offene_lage | 1 | 1 | 0.0125 | 0.0369 | -0.0081 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->rekoppelnde_lage->druck_lage | 1 | 1 | 0.0125 | 0.0912 | -0.0035 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->offene_lage->druck_lage | 1 | 1 | 0.0125 | 0.0797 | 0.0061 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->gehaltene_form->offene_lage | 1 | 1 | 0.0125 | -0.0854 | 0.0053 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->bewegungsbruch->gehaltene_form | 1 | 1 | 0.0125 | 0.0344 | 0.0141 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->bewegungsbruch->offene_lage | 1 | 1 | 0.0125 | 0.0849 | -0.0477 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->bewegungsbruch->bewegungsbruch | 1 | 1 | 0.0125 | -0.0629 | 0.0287 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->offene_lage->offene_lage | 1 | 1 | 0.0125 | 0.0120 | 0.0034 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->druck_lage->rekoppelnde_lage | 1 | 1 | 0.0125 | -0.0711 | 0.0120 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->bewegungsbruch->druck_lage | 1 | 1 | 0.0125 | 0.0158 | -0.0190 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->rekoppelnde_lage->druck_lage | 1 | 1 | 0.0125 | 0.1574 | -0.0298 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->offene_lage->druck_lage | 1 | 1 | 0.0125 | 0.1379 | -0.1053 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->druck_lage->bewegungsbruch | 1 | 1 | 0.0125 | -0.0047 | -0.0389 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->offene_lage->offene_lage | 1 | 1 | 0.0125 | 0.2571 | -0.0811 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | gehaltene_form->druck_lage->druck_lage | 1 | 1 | 0.0125 | -0.1104 | -0.0038 |

## Befund

Stabile Milieus: 1
Variable wiederkehrende Milieus: 0

Ein wiederkehrendes Kontaktmilieu bedeutet hier nicht, dass die Feldbewegung mechanisch ausgeloest wird.
Es bedeutet: Die Feldbewegung erscheint in einem aehnlichen Rezeptor-/Innenfeld-Kontext wieder.

Das ist fuer MINI_DIO wichtig, weil dadurch Bedeutung nicht nur als Insel, sondern als Lagefolge gelesen werden kann.

## Wie es weitergeht

Als naechstes sollten stabile Milieus gegen laengere Welten geprueft werden.
Wenn sie dort stabil bleiben, koennen sie als passive Regulationswahrnehmung dokumentiert werden.
