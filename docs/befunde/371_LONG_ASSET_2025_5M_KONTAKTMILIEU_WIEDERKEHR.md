# Kontaktmilieu Wiederkehr Und Drift

Stand: 2026-06-20 08:18:08

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
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 79 | 4 | 14 | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 0.6076 | 0.0203 | 0.0574 | -0.0051 | 0.0213 | wiederkehrend_stabil |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 69 | 4 | 26 | rekoppelnde_lage->druck_lage->bewegungsbruch | 0.1304 | 0.0197 | 0.0698 | -0.0047 | 0.0227 | lokal_offen |

## Signaturdetails

| Paar | Signatur | Events | Welten | Anteil | dDruck | dRekopplung |
|---|---|---:|---:|---:|---:|---:|
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 48 | 4 | 0.6076 | 0.0167 | -0.0040 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | offene_lage->rekoppelnde_lage->rekoppelnde_lage | 8 | 4 | 0.1013 | -0.0369 | 0.0085 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->offene_lage | 6 | 3 | 0.0759 | 0.0753 | -0.0114 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->druck_lage | 4 | 3 | 0.0506 | 0.1092 | -0.0343 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->bewegungsbruch | 3 | 2 | 0.0380 | 0.0551 | -0.0228 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | offene_lage->offene_lage->rekoppelnde_lage | 2 | 2 | 0.0253 | -0.0216 | -0.0012 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->offene_lage->rekoppelnde_lage | 1 | 1 | 0.0127 | 0.0127 | -0.0254 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | druck_lage->rekoppelnde_lage->rekoppelnde_lage | 1 | 1 | 0.0127 | -0.0688 | 0.0464 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | offene_lage->rekoppelnde_lage->offene_lage | 1 | 1 | 0.0127 | -0.0502 | 0.0228 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | offene_lage->rekoppelnde_lage->druck_lage | 1 | 1 | 0.0127 | 0.1563 | -0.0295 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->offene_lage->offene_lage | 1 | 1 | 0.0127 | 0.0036 | -0.0104 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | druck_lage->offene_lage->rekoppelnde_lage | 1 | 1 | 0.0127 | -0.1058 | 0.0406 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->gehaltene_form->druck_lage | 1 | 1 | 0.0127 | 0.1048 | -0.0199 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | offene_lage->rekoppelnde_lage->bewegungsbruch | 1 | 1 | 0.0127 | 0.0376 | -0.0278 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->bewegungsbruch | 9 | 3 | 0.1304 | 0.0804 | -0.0129 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->rekoppelnde_lage | 8 | 3 | 0.1159 | 0.0322 | -0.0133 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->offene_lage->rekoppelnde_lage | 6 | 3 | 0.0870 | 0.0195 | -0.0040 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 6 | 3 | 0.0870 | 0.0235 | -0.0006 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->bewegungsbruch->rekoppelnde_lage | 5 | 2 | 0.0725 | 0.0345 | -0.0206 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->rekoppelnde_lage->rekoppelnde_lage | 4 | 2 | 0.0580 | -0.0413 | 0.0186 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->offene_lage->rekoppelnde_lage | 3 | 3 | 0.0435 | -0.0961 | 0.0320 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->offene_lage->rekoppelnde_lage | 3 | 3 | 0.0435 | -0.0506 | 0.0119 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->rekoppelnde_lage->rekoppelnde_lage | 3 | 3 | 0.0435 | -0.0025 | 0.0023 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->druck_lage | 2 | 2 | 0.0290 | 0.1442 | -0.0302 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->druck_lage->rekoppelnde_lage | 2 | 2 | 0.0290 | 0.0002 | 0.0013 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->offene_lage->bewegungsbruch | 2 | 2 | 0.0290 | 0.0479 | -0.0080 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->rekoppelnde_lage->offene_lage | 2 | 2 | 0.0290 | 0.0316 | -0.0144 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->offene_lage | 2 | 2 | 0.0290 | 0.0306 | -0.0223 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->bewegungsbruch->druck_lage | 1 | 1 | 0.0145 | 0.0987 | -0.0195 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | gehaltene_form->rekoppelnde_lage->offene_lage | 1 | 1 | 0.0145 | 0.0133 | -0.0376 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->druck_lage->offene_lage | 1 | 1 | 0.0145 | -0.0585 | -0.0040 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->bewegungsbruch->offene_lage | 1 | 1 | 0.0145 | 0.0442 | -0.0243 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->bewegungsbruch->rekoppelnde_lage | 1 | 1 | 0.0145 | -0.0345 | -0.0072 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->gehaltene_form->offene_lage | 1 | 1 | 0.0145 | -0.0209 | 0.0070 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->druck_lage->druck_lage | 1 | 1 | 0.0145 | 0.2244 | -0.0568 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->druck_lage->rekoppelnde_lage | 1 | 1 | 0.0145 | 0.0512 | 0.0062 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->bewegungsbruch->offene_lage | 1 | 1 | 0.0145 | -0.0604 | -0.0211 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->bewegungsbruch->bewegungsbruch | 1 | 1 | 0.0145 | 0.0151 | 0.0161 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->rekoppelnde_lage->offene_lage | 1 | 1 | 0.0145 | -0.1255 | 0.0691 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->bewegungsbruch->rekoppelnde_lage | 1 | 1 | 0.0145 | -0.0990 | 0.0345 |

## Befund

Stabile Milieus: 1
Variable wiederkehrende Milieus: 0

Ein wiederkehrendes Kontaktmilieu bedeutet hier nicht, dass die Feldbewegung mechanisch ausgeloest wird.
Es bedeutet: Die Feldbewegung erscheint in einem aehnlichen Rezeptor-/Innenfeld-Kontext wieder.

Das ist fuer MINI_DIO wichtig, weil dadurch Bedeutung nicht nur als Insel, sondern als Lagefolge gelesen werden kann.

## Wie es weitergeht

Als naechstes sollten stabile Milieus gegen laengere Welten geprueft werden.
Wenn sie dort stabil bleiben, koennen sie als passive Regulationswahrnehmung dokumentiert werden.
