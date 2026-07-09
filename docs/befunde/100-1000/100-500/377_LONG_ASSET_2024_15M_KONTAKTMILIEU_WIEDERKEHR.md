# Kontaktmilieu Wiederkehr Und Drift

Stand: 2026-06-20 08:30:49

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
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 74 | 4 | 12 | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 0.5405 | 0.0130 | 0.0730 | -0.0038 | 0.0293 | wiederkehrend_variabel |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 67 | 4 | 29 | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 0.1642 | 0.0228 | 0.0736 | -0.0094 | 0.0263 | lokal_offen |

## Signaturdetails

| Paar | Signatur | Events | Welten | Anteil | dDruck | dRekopplung |
|---|---|---:|---:|---:|---:|---:|
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 40 | 4 | 0.5405 | 0.0104 | -0.0013 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | offene_lage->rekoppelnde_lage->rekoppelnde_lage | 10 | 4 | 0.1351 | -0.0636 | 0.0145 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->druck_lage | 7 | 3 | 0.0946 | 0.1404 | -0.0505 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->offene_lage | 4 | 2 | 0.0541 | 0.0547 | -0.0029 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | druck_lage->rekoppelnde_lage->rekoppelnde_lage | 3 | 2 | 0.0405 | -0.0790 | 0.0495 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->bewegungsbruch | 2 | 2 | 0.0270 | 0.0750 | -0.0195 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | bewegungsbruch->rekoppelnde_lage->druck_lage | 2 | 2 | 0.0270 | 0.0801 | -0.0604 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | bewegungsbruch->rekoppelnde_lage->rekoppelnde_lage | 2 | 1 | 0.0270 | -0.0396 | 0.0152 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->bewegungsbruch->rekoppelnde_lage | 1 | 1 | 0.0135 | -0.0844 | 0.0322 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | gehaltene_form->rekoppelnde_lage->rekoppelnde_lage | 1 | 1 | 0.0135 | -0.0397 | -0.0090 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | gehaltene_form->gehaltene_form->rekoppelnde_lage | 1 | 1 | 0.0135 | -0.0101 | -0.0122 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | offene_lage->rekoppelnde_lage->druck_lage | 1 | 1 | 0.0135 | 0.1220 | -0.0417 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 11 | 4 | 0.1642 | -0.0329 | 0.0077 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->rekoppelnde_lage | 7 | 2 | 0.1045 | 0.0596 | -0.0362 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->bewegungsbruch | 7 | 2 | 0.1045 | 0.0762 | -0.0241 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->offene_lage->rekoppelnde_lage | 5 | 2 | 0.0746 | 0.0114 | -0.0117 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->offene_lage | 4 | 3 | 0.0597 | 0.0508 | -0.0232 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->bewegungsbruch->rekoppelnde_lage | 3 | 2 | 0.0448 | -0.0306 | 0.0260 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->gehaltene_form | 3 | 2 | 0.0448 | 0.0848 | -0.0202 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->druck_lage | 2 | 1 | 0.0299 | 0.0701 | -0.0057 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->offene_lage->rekoppelnde_lage | 2 | 1 | 0.0299 | -0.0369 | 0.0129 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->offene_lage->offene_lage | 2 | 2 | 0.0299 | 0.0340 | -0.0228 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->druck_lage->rekoppelnde_lage | 2 | 2 | 0.0299 | -0.0009 | -0.0059 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->bewegungsbruch->rekoppelnde_lage | 2 | 1 | 0.0299 | -0.0362 | -0.0177 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->bewegungsbruch->bewegungsbruch | 1 | 1 | 0.0149 | -0.0087 | 0.0176 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->bewegungsbruch->offene_lage | 1 | 1 | 0.0149 | -0.1048 | 0.0434 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->gehaltene_form->rekoppelnde_lage | 1 | 1 | 0.0149 | 0.0473 | -0.0042 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->rekoppelnde_lage->rekoppelnde_lage | 1 | 1 | 0.0149 | -0.0971 | 0.0366 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->gehaltene_form->gehaltene_form | 1 | 1 | 0.0149 | 0.0777 | -0.0205 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->rekoppelnde_lage->offene_lage | 1 | 1 | 0.0149 | 0.0434 | -0.0083 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->offene_lage->druck_lage | 1 | 1 | 0.0149 | 0.1873 | -0.0441 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->rekoppelnde_lage->druck_lage | 1 | 1 | 0.0149 | 0.0204 | -0.0036 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->druck_lage->offene_lage | 1 | 1 | 0.0149 | -0.1214 | 0.0429 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->offene_lage->bewegungsbruch | 1 | 1 | 0.0149 | -0.1218 | 0.0031 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->rekoppelnde_lage->rekoppelnde_lage | 1 | 1 | 0.0149 | 0.0294 | 0.0310 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->druck_lage->druck_lage | 1 | 1 | 0.0149 | 0.0516 | -0.0072 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | gehaltene_form->rekoppelnde_lage->rekoppelnde_lage | 1 | 1 | 0.0149 | 0.0019 | -0.0136 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->druck_lage->bewegungsbruch | 1 | 1 | 0.0149 | 0.0896 | -0.0417 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | gehaltene_form->druck_lage->druck_lage | 1 | 1 | 0.0149 | 0.1713 | -0.0451 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->offene_lage->rekoppelnde_lage | 1 | 1 | 0.0149 | 0.1268 | -0.0471 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->offene_lage->bewegungsbruch | 1 | 1 | 0.0149 | 0.0653 | -0.0214 |

## Befund

Stabile Milieus: 0
Variable wiederkehrende Milieus: 1

Ein wiederkehrendes Kontaktmilieu bedeutet hier nicht, dass die Feldbewegung mechanisch ausgeloest wird.
Es bedeutet: Die Feldbewegung erscheint in einem aehnlichen Rezeptor-/Innenfeld-Kontext wieder.

Das ist fuer MINI_DIO wichtig, weil dadurch Bedeutung nicht nur als Insel, sondern als Lagefolge gelesen werden kann.

## Wie es weitergeht

Als naechstes sollten stabile Milieus gegen laengere Welten geprueft werden.
Wenn sie dort stabil bleiben, koennen sie als passive Regulationswahrnehmung dokumentiert werden.
