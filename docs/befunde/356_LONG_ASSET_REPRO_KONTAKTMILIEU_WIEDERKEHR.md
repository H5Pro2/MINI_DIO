# Kontaktmilieu Wiederkehr Und Drift

Stand: 2026-06-20 01:19:48

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
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 106 | 3 | 12 | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 0.6132 | 0.0176 | 0.0732 | -0.0059 | 0.0279 | wiederkehrend_variabel |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 94 | 4 | 33 | rekoppelnde_lage->druck_lage->rekoppelnde_lage | 0.1277 | 0.0104 | 0.0728 | -0.0069 | 0.0244 | lokal_offen |

## Signaturdetails

| Paar | Signatur | Events | Welten | Anteil | dDruck | dRekopplung |
|---|---|---:|---:|---:|---:|---:|
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 65 | 3 | 0.6132 | 0.0118 | -0.0025 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | offene_lage->rekoppelnde_lage->rekoppelnde_lage | 13 | 3 | 0.1226 | -0.0421 | 0.0105 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->druck_lage | 8 | 3 | 0.0755 | 0.1587 | -0.0590 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->offene_lage | 7 | 3 | 0.0660 | 0.0861 | -0.0332 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | druck_lage->rekoppelnde_lage->rekoppelnde_lage | 3 | 2 | 0.0283 | -0.0957 | 0.0207 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->bewegungsbruch | 2 | 2 | 0.0189 | 0.0583 | -0.0264 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | druck_lage->rekoppelnde_lage->offene_lage | 2 | 2 | 0.0189 | -0.0855 | 0.0319 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->offene_lage->rekoppelnde_lage | 2 | 2 | 0.0189 | -0.0242 | 0.0259 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | offene_lage->rekoppelnde_lage->druck_lage | 1 | 1 | 0.0094 | 0.0582 | -0.0171 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | bewegungsbruch->rekoppelnde_lage->bewegungsbruch | 1 | 1 | 0.0094 | -0.0040 | -0.0025 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | bewegungsbruch->rekoppelnde_lage->rekoppelnde_lage | 1 | 1 | 0.0094 | -0.0302 | 0.0063 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->offene_lage->druck_lage | 1 | 1 | 0.0094 | 0.1315 | -0.0118 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->rekoppelnde_lage | 12 | 3 | 0.1277 | 0.0178 | -0.0140 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 11 | 3 | 0.1170 | 0.0037 | 0.0006 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->offene_lage->rekoppelnde_lage | 9 | 3 | 0.0957 | -0.0054 | 0.0040 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->bewegungsbruch | 8 | 3 | 0.0851 | 0.0815 | -0.0239 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->offene_lage | 7 | 2 | 0.0745 | 0.0883 | -0.0311 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->rekoppelnde_lage->rekoppelnde_lage | 5 | 3 | 0.0532 | -0.0348 | 0.0070 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->bewegungsbruch->rekoppelnde_lage | 5 | 3 | 0.0532 | -0.0196 | -0.0036 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->bewegungsbruch->rekoppelnde_lage | 4 | 3 | 0.0426 | 0.0079 | -0.0026 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->offene_lage->bewegungsbruch | 4 | 2 | 0.0426 | 0.0561 | -0.0198 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->druck_lage | 3 | 1 | 0.0319 | 0.0973 | -0.0280 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->rekoppelnde_lage->bewegungsbruch | 2 | 2 | 0.0213 | 0.0688 | -0.0189 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->bewegungsbruch->offene_lage | 2 | 2 | 0.0213 | -0.0868 | 0.0034 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->rekoppelnde_lage->offene_lage | 2 | 2 | 0.0213 | 0.0786 | -0.0269 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->offene_lage->offene_lage | 1 | 1 | 0.0106 | -0.0073 | 0.0021 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->druck_lage->rekoppelnde_lage | 1 | 1 | 0.0106 | -0.1580 | 0.0407 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->rekoppelnde_lage->rekoppelnde_lage | 1 | 1 | 0.0106 | -0.0736 | 0.0392 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->gehaltene_form->druck_lage | 1 | 1 | 0.0106 | -0.0804 | 0.0038 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->offene_lage->rekoppelnde_lage | 1 | 1 | 0.0106 | -0.0726 | -0.0051 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->druck_lage->offene_lage | 1 | 1 | 0.0106 | -0.0037 | -0.0266 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->bewegungsbruch->gehaltene_form | 1 | 1 | 0.0106 | -0.0715 | 0.0204 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->bewegungsbruch->offene_lage | 1 | 1 | 0.0106 | -0.0051 | -0.0110 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->offene_lage->rekoppelnde_lage | 1 | 1 | 0.0106 | -0.0649 | 0.0138 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->bewegungsbruch->rekoppelnde_lage | 1 | 1 | 0.0106 | -0.1652 | 0.0495 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->druck_lage->offene_lage | 1 | 1 | 0.0106 | -0.0270 | 0.0146 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->rekoppelnde_lage->offene_lage | 1 | 1 | 0.0106 | -0.0900 | 0.0262 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->gehaltene_form | 1 | 1 | 0.0106 | 0.0364 | -0.0226 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->druck_lage->druck_lage | 1 | 1 | 0.0106 | -0.0161 | -0.0099 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->bewegungsbruch->rekoppelnde_lage | 1 | 1 | 0.0106 | -0.1031 | 0.0328 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->bewegungsbruch->bewegungsbruch | 1 | 1 | 0.0106 | 0.0068 | -0.0189 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->bewegungsbruch->offene_lage | 1 | 1 | 0.0106 | -0.0688 | -0.0170 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->druck_lage->rekoppelnde_lage | 1 | 1 | 0.0106 | -0.0114 | 0.0092 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->druck_lage->gehaltene_form | 1 | 1 | 0.0106 | -0.0564 | 0.0452 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->bewegungsbruch->druck_lage | 1 | 1 | 0.0106 | 0.1402 | -0.0588 |

## Befund

Stabile Milieus: 0
Variable wiederkehrende Milieus: 1

Ein wiederkehrendes Kontaktmilieu bedeutet hier nicht, dass die Feldbewegung mechanisch ausgeloest wird.
Es bedeutet: Die Feldbewegung erscheint in einem aehnlichen Rezeptor-/Innenfeld-Kontext wieder.

Das ist fuer MINI_DIO wichtig, weil dadurch Bedeutung nicht nur als Insel, sondern als Lagefolge gelesen werden kann.

## Wie es weitergeht

Als naechstes sollten stabile Milieus gegen laengere Welten geprueft werden.
Wenn sie dort stabil bleiben, koennen sie als passive Regulationswahrnehmung dokumentiert werden.
