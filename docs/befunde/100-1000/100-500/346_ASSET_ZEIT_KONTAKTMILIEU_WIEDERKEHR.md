# Kontaktmilieu Wiederkehr Und Drift

Stand: 2026-06-20 00:54:55

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
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 78 | 9 | 8 | offene_lage->offene_lage->offene_lage | 0.7949 | 0.0160 | 0.0832 | -0.0000 | 0.0182 | wiederkehrend_variabel |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 73 | 10 | 17 | offene_lage->offene_lage->offene_lage | 0.3425 | 0.0146 | 0.1176 | -0.0032 | 0.0207 | driftend |

## Signaturdetails

| Paar | Signatur | Events | Welten | Anteil | dDruck | dRekopplung |
|---|---|---:|---:|---:|---:|---:|
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | offene_lage->offene_lage->offene_lage | 62 | 9 | 0.7949 | 0.0103 | -0.0003 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | offene_lage->offene_lage->druck_lage | 5 | 5 | 0.0641 | 0.1439 | -0.0133 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | bewegungsbruch->offene_lage->offene_lage | 4 | 3 | 0.0513 | -0.0451 | 0.0118 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | druck_lage->offene_lage->offene_lage | 2 | 1 | 0.0256 | -0.0442 | 0.0170 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | offene_lage->offene_lage->bewegungsbruch | 2 | 2 | 0.0256 | 0.0978 | -0.0200 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | offene_lage->gehaltene_form->druck_lage | 1 | 1 | 0.0128 | -0.0444 | 0.0117 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | bewegungsbruch->offene_lage->druck_lage | 1 | 1 | 0.0128 | 0.1262 | -0.0011 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | druck_lage->gehaltene_form->offene_lage | 1 | 1 | 0.0128 | -0.1229 | 0.0305 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->offene_lage->offene_lage | 25 | 9 | 0.3425 | -0.0005 | -0.0035 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->druck_lage->offene_lage | 7 | 3 | 0.0959 | 0.0948 | -0.0166 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->bewegungsbruch->offene_lage | 6 | 5 | 0.0822 | 0.0037 | -0.0075 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->druck_lage->bewegungsbruch | 5 | 4 | 0.0685 | 0.0310 | -0.0063 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->druck_lage->druck_lage | 4 | 3 | 0.0548 | 0.2151 | -0.0187 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->druck_lage->gehaltene_form | 4 | 3 | 0.0548 | 0.1229 | -0.0112 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->druck_lage->druck_lage | 4 | 4 | 0.0548 | -0.0939 | 0.0063 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->bewegungsbruch->bewegungsbruch | 3 | 2 | 0.0411 | -0.0560 | 0.0094 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->offene_lage->offene_lage | 3 | 3 | 0.0411 | -0.1016 | 0.0298 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->offene_lage->druck_lage | 3 | 2 | 0.0411 | 0.2114 | -0.0365 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->offene_lage->offene_lage | 2 | 2 | 0.0274 | -0.1364 | 0.0223 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | gehaltene_form->offene_lage->offene_lage | 2 | 1 | 0.0274 | -0.1217 | 0.0144 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->bewegungsbruch->gehaltene_form | 1 | 1 | 0.0137 | -0.0378 | 0.0054 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->druck_lage->offene_lage | 1 | 1 | 0.0137 | -0.1630 | -0.0077 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->offene_lage->bewegungsbruch | 1 | 1 | 0.0137 | -0.1380 | 0.0647 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->druck_lage->bewegungsbruch | 1 | 1 | 0.0137 | 0.0061 | -0.0045 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->offene_lage->bewegungsbruch | 1 | 1 | 0.0137 | -0.0478 | 0.0010 |

## Befund

Stabile Milieus: 0
Variable wiederkehrende Milieus: 1

Ein wiederkehrendes Kontaktmilieu bedeutet hier nicht, dass die Feldbewegung mechanisch ausgeloest wird.
Es bedeutet: Die Feldbewegung erscheint in einem aehnlichen Rezeptor-/Innenfeld-Kontext wieder.

Das ist fuer MINI_DIO wichtig, weil dadurch Bedeutung nicht nur als Insel, sondern als Lagefolge gelesen werden kann.

## Wie es weitergeht

Als naechstes sollten stabile Milieus gegen laengere Welten geprueft werden.
Wenn sie dort stabil bleiben, koennen sie als passive Regulationswahrnehmung dokumentiert werden.
