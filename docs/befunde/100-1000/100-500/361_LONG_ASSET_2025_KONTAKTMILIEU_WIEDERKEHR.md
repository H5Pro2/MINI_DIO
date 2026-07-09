# Kontaktmilieu Wiederkehr Und Drift

Stand: 2026-06-20 01:25:27

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
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 103 | 4 | 17 | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 0.5534 | 0.0035 | 0.0734 | 0.0011 | 0.0274 | wiederkehrend_variabel |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 97 | 4 | 36 | rekoppelnde_lage->bewegungsbruch->rekoppelnde_lage | 0.1340 | -0.0021 | 0.0791 | 0.0008 | 0.0240 | lokal_offen |

## Signaturdetails

| Paar | Signatur | Events | Welten | Anteil | dDruck | dRekopplung |
|---|---|---:|---:|---:|---:|---:|
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 57 | 4 | 0.5534 | -0.0010 | 0.0050 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | bewegungsbruch->rekoppelnde_lage->rekoppelnde_lage | 10 | 3 | 0.0971 | -0.0710 | 0.0229 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | offene_lage->rekoppelnde_lage->rekoppelnde_lage | 10 | 3 | 0.0971 | -0.0226 | 0.0118 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->offene_lage | 6 | 4 | 0.0583 | 0.0590 | -0.0200 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->druck_lage | 5 | 2 | 0.0485 | 0.1790 | -0.0580 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | offene_lage->rekoppelnde_lage->offene_lage | 3 | 1 | 0.0291 | -0.0056 | -0.0023 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->rekoppelnde_lage->bewegungsbruch | 2 | 2 | 0.0194 | 0.1072 | -0.0408 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | gehaltene_form->rekoppelnde_lage->druck_lage | 1 | 1 | 0.0097 | 0.2327 | -0.0864 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | gehaltene_form->offene_lage->rekoppelnde_lage | 1 | 1 | 0.0097 | -0.0603 | 0.0346 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | druck_lage->rekoppelnde_lage->offene_lage | 1 | 1 | 0.0097 | -0.0376 | -0.0035 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | bewegungsbruch->rekoppelnde_lage->offene_lage | 1 | 1 | 0.0097 | -0.0760 | 0.0123 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | gehaltene_form->rekoppelnde_lage->rekoppelnde_lage | 1 | 1 | 0.0097 | -0.0775 | -0.0126 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | offene_lage->rekoppelnde_lage->gehaltene_form | 1 | 1 | 0.0097 | -0.0487 | 0.0202 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | bewegungsbruch->rekoppelnde_lage->druck_lage | 1 | 1 | 0.0097 | 0.1194 | -0.0276 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | druck_lage->gehaltene_form->rekoppelnde_lage | 1 | 1 | 0.0097 | -0.0601 | 0.0104 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | druck_lage->rekoppelnde_lage->rekoppelnde_lage | 1 | 1 | 0.0097 | -0.1119 | 0.0387 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | rekoppelnde_lage->bewegungsbruch->rekoppelnde_lage | 1 | 1 | 0.0097 | 0.0220 | -0.0071 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->bewegungsbruch->rekoppelnde_lage | 13 | 4 | 0.1340 | -0.0271 | -0.0022 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | 10 | 4 | 0.1031 | -0.0329 | 0.0074 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->rekoppelnde_lage | 6 | 3 | 0.0619 | 0.0180 | -0.0041 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->bewegungsbruch | 6 | 3 | 0.0619 | 0.0634 | -0.0168 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->offene_lage | 6 | 4 | 0.0619 | 0.0557 | -0.0139 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->offene_lage->rekoppelnde_lage | 5 | 3 | 0.0515 | -0.0221 | 0.0055 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->druck_lage | 5 | 2 | 0.0515 | 0.1615 | -0.0450 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->bewegungsbruch->rekoppelnde_lage | 4 | 4 | 0.0412 | -0.0700 | 0.0089 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->rekoppelnde_lage->rekoppelnde_lage | 4 | 3 | 0.0412 | -0.0495 | 0.0217 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->bewegungsbruch->offene_lage | 3 | 2 | 0.0309 | -0.0232 | 0.0066 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->offene_lage->rekoppelnde_lage | 3 | 1 | 0.0309 | -0.0419 | 0.0146 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->druck_lage->offene_lage | 2 | 2 | 0.0206 | 0.0147 | -0.0057 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->druck_lage->gehaltene_form | 2 | 2 | 0.0206 | 0.0943 | 0.0059 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->druck_lage->bewegungsbruch | 2 | 2 | 0.0206 | 0.0059 | 0.0088 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->rekoppelnde_lage->offene_lage | 2 | 1 | 0.0206 | 0.0285 | -0.0101 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->bewegungsbruch->rekoppelnde_lage | 2 | 2 | 0.0206 | -0.0363 | 0.0245 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->rekoppelnde_lage->offene_lage | 2 | 2 | 0.0206 | -0.0393 | 0.0069 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->offene_lage->bewegungsbruch | 2 | 2 | 0.0206 | 0.0338 | -0.0089 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | gehaltene_form->rekoppelnde_lage->rekoppelnde_lage | 1 | 1 | 0.0103 | -0.1229 | 0.0522 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->rekoppelnde_lage->offene_lage | 1 | 1 | 0.0103 | -0.0171 | -0.0079 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->bewegungsbruch->offene_lage | 1 | 1 | 0.0103 | -0.0182 | 0.0325 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->druck_lage->bewegungsbruch | 1 | 1 | 0.0103 | -0.1280 | 0.0583 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->druck_lage->bewegungsbruch | 1 | 1 | 0.0103 | 0.0024 | -0.0047 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->offene_lage->rekoppelnde_lage | 1 | 1 | 0.0103 | -0.0981 | 0.0471 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->bewegungsbruch->gehaltene_form | 1 | 1 | 0.0103 | 0.1273 | -0.0233 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->offene_lage->druck_lage | 1 | 1 | 0.0103 | 0.0493 | -0.0351 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->druck_lage->offene_lage | 1 | 1 | 0.0103 | -0.0897 | 0.0122 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->rekoppelnde_lage->offene_lage | 1 | 1 | 0.0103 | -0.1288 | 0.0240 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_lage->bewegungsbruch->rekoppelnde_lage | 1 | 1 | 0.0103 | -0.1791 | 0.0444 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->druck_lage->druck_lage | 1 | 1 | 0.0103 | -0.0968 | 0.0031 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->druck_lage->rekoppelnde_lage | 1 | 1 | 0.0103 | -0.0665 | 0.0443 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->bewegungsbruch->druck_lage | 1 | 1 | 0.0103 | 0.0204 | 0.0062 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | offene_lage->druck_lage->druck_lage | 1 | 1 | 0.0103 | 0.1716 | -0.0293 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | gehaltene_form->druck_lage->bewegungsbruch | 1 | 1 | 0.0103 | -0.0308 | -0.0041 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | rekoppelnde_lage->rekoppelnde_lage->bewegungsbruch | 1 | 1 | 0.0103 | 0.0982 | -0.0277 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | bewegungsbruch->rekoppelnde_lage->rekoppelnde_lage | 1 | 1 | 0.0103 | -0.0678 | 0.0169 |

## Befund

Stabile Milieus: 0
Variable wiederkehrende Milieus: 1

Ein wiederkehrendes Kontaktmilieu bedeutet hier nicht, dass die Feldbewegung mechanisch ausgeloest wird.
Es bedeutet: Die Feldbewegung erscheint in einem aehnlichen Rezeptor-/Innenfeld-Kontext wieder.

Das ist fuer MINI_DIO wichtig, weil dadurch Bedeutung nicht nur als Insel, sondern als Lagefolge gelesen werden kann.

## Wie es weitergeht

Als naechstes sollten stabile Milieus gegen laengere Welten geprueft werden.
Wenn sie dort stabil bleiben, koennen sie als passive Regulationswahrnehmung dokumentiert werden.
