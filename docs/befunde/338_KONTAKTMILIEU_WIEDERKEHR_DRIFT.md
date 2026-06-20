# Kontaktmilieu Wiederkehr Und Drift

Stand: 2026-06-20 00:16:04

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
| dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | 19 | 6 | 13 | rekoppelnde_lage->offene_lage->rekoppelnde_lage | 0.1579 | -0.0141 | 0.0624 | 0.0038 | 0.0184 | lokal_offen |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 12 | 5 | 7 | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 0.3333 | -0.0001 | 0.0766 | -0.0102 | 0.0192 | lokal_offen |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | 12 | 4 | 11 | offene_lage->druck_lage->offene_lage | 0.1667 | -0.0204 | 0.0552 | 0.0071 | 0.0168 | lokal_offen |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 12 | 5 | 2 | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 0.8333 | 0.0362 | 0.0685 | -0.0059 | 0.0206 | wiederkehrend_stabil |

## Signaturdetails

| Paar | Signatur | Events | Welten | Anteil | dDruck | dRekopplung |
|---|---|---:|---:|---:|---:|---:|
| dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->offene_lage->rekoppelnde_lage | 3 | 3 | 0.1579 | 0.0124 | -0.0071 |
| dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | bewegungsbruch->rekoppelnde_lage->rekoppelnde_lage | 3 | 2 | 0.1579 | -0.0664 | 0.0073 |
| dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | offene_lage->rekoppelnde_lage->rekoppelnde_lage | 2 | 1 | 0.1053 | -0.0655 | 0.0265 |
| dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | offene_lage->bewegungsbruch->bewegungsbruch | 2 | 2 | 0.1053 | -0.0065 | 0.0054 |
| dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | offene_lage->offene_lage->rekoppelnde_lage | 1 | 1 | 0.0526 | 0.0249 | -0.0162 |
| dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | offene_lage->rekoppelnde_lage->bewegungsbruch | 1 | 1 | 0.0526 | 0.0133 | -0.0138 |
| dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->rekoppelnde_lage->offene_lage | 1 | 1 | 0.0526 | -0.0040 | 0.0177 |
| dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | offene_lage->offene_lage->offene_lage | 1 | 1 | 0.0526 | -0.0161 | 0.0137 |
| dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->rekoppelnde_lage->bewegungsbruch | 1 | 1 | 0.0526 | 0.0701 | 0.0003 |
| dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | druck_lage->offene_lage->offene_lage | 1 | 1 | 0.0526 | -0.1343 | 0.0274 |
| dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->rekoppelnde_lage->druck_lage | 1 | 1 | 0.0526 | 0.1390 | -0.0361 |
| dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | gehaltene_form->rekoppelnde_lage->rekoppelnde_lage | 1 | 1 | 0.0526 | -0.0605 | 0.0156 |
| dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 1 | 1 | 0.0526 | 0.0058 | -0.0016 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 4 | 3 | 0.3333 | 0.0282 | -0.0107 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->bewegungsbruch->rekoppelnde_lage | 2 | 2 | 0.1667 | -0.0206 | -0.0044 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->bewegungsbruch | 2 | 2 | 0.1667 | 0.0322 | -0.0237 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->druck_lage->rekoppelnde_lage | 1 | 1 | 0.0833 | -0.0153 | 0.0206 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->offene_lage->rekoppelnde_lage | 1 | 1 | 0.0833 | -0.1412 | 0.0071 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->rekoppelnde_lage | 1 | 1 | 0.0833 | 0.0509 | -0.0366 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->offene_lage->bewegungsbruch | 1 | 1 | 0.0833 | -0.0309 | -0.0140 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | offene_lage->druck_lage->offene_lage | 2 | 2 | 0.1667 | -0.0295 | 0.0008 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | druck_lage->rekoppelnde_lage->bewegungsbruch | 1 | 1 | 0.0833 | -0.0694 | 0.0151 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | gehaltene_form->druck_lage->bewegungsbruch | 1 | 1 | 0.0833 | 0.0640 | -0.0030 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | druck_lage->bewegungsbruch->offene_lage | 1 | 1 | 0.0833 | -0.1013 | 0.0320 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | druck_lage->offene_lage->bewegungsbruch | 1 | 1 | 0.0833 | -0.1012 | -0.0013 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | bewegungsbruch->gehaltene_form->gehaltene_form | 1 | 1 | 0.0833 | -0.0237 | 0.0114 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 1 | 1 | 0.0833 | 0.0163 | 0.0078 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | rekoppelnde_lage->druck_lage->bewegungsbruch | 1 | 1 | 0.0833 | 0.0421 | -0.0204 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | offene_lage->offene_lage->offene_lage | 1 | 1 | 0.0833 | 0.0660 | 0.0080 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | rekoppelnde_lage->bewegungsbruch->rekoppelnde_lage | 1 | 1 | 0.0833 | -0.0328 | 0.0112 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | bewegungsbruch->druck_lage->rekoppelnde_lage | 1 | 1 | 0.0833 | -0.0458 | 0.0234 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 10 | 4 | 0.8333 | 0.0227 | -0.0023 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->bewegungsbruch | 2 | 2 | 0.1667 | 0.1032 | -0.0239 |

## Befund

Stabile Milieus: 1
Variable wiederkehrende Milieus: 0

Ein wiederkehrendes Kontaktmilieu bedeutet hier nicht, dass die Feldbewegung mechanisch ausgeloest wird.
Es bedeutet: Die Feldbewegung erscheint in einem aehnlichen Rezeptor-/Innenfeld-Kontext wieder.

Das ist fuer MINI_DIO wichtig, weil dadurch Bedeutung nicht nur als Insel, sondern als Lagefolge gelesen werden kann.

## Wie es weitergeht

Als naechstes sollten stabile Milieus gegen laengere Welten geprueft werden.
Wenn sie dort stabil bleiben, koennen sie als passive Regulationswahrnehmung dokumentiert werden.
