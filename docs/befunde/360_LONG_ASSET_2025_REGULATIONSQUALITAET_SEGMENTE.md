# Bewegungsarten Rohwelt-Segmente

Stand: 2026-06-20 01:25:26

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
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | nachher | 194 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0631 | 0.2166 | 0.2301 | 0.2199 | 0.8566 | 0.1915 | 0.6465 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | vorher | 194 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0706 | 0.2182 | 0.2314 | 0.2220 | 0.8559 | 0.1943 | 0.6457 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | wechsel | 97 | 4 | druck_lage | offene_variante | -0.0113 | 0.3281 | 0.3862 | 0.3034 | 0.7960 | 0.2406 | 0.6152 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | nachher | 226 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0768 | 0.1495 | 0.1936 | 0.1854 | 0.8776 | 0.1766 | 0.6567 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | vorher | 226 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0582 | 0.1507 | 0.1806 | 0.1848 | 0.8833 | 0.1761 | 0.6557 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | wechsel | 113 | 4 | rekoppelnde_lage | zentrum_stabil | 0.0828 | 0.1071 | 0.1191 | 0.1529 | 0.9069 | 0.1490 | 0.6782 |

## Ereignislupe

| Welt | Paar | Tick | Vorher | Wechsel | Nachher | dDruck | dRekopplung |
|---|---|---:|---|---|---|---:|---:|
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1002 | rekoppelnde_lage | druck_lage | rekoppelnde_lage | -0.0243 | 0.0073 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1030 | gehaltene_form | rekoppelnde_lage | rekoppelnde_lage | -0.1229 | 0.0522 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1037 | rekoppelnde_lage | druck_lage | bewegungsbruch | 0.0893 | -0.0301 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1053 | offene_lage | druck_lage | offene_lage | 0.0328 | -0.0058 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1103 | rekoppelnde_lage | bewegungsbruch | rekoppelnde_lage | 0.0038 | -0.0140 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1143 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0291 | 0.0168 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1158 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | 0.0013 | 0.0070 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1161 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0143 | -0.0187 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1206 | rekoppelnde_lage | druck_lage | offene_lage | 0.0949 | -0.0292 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1226 | rekoppelnde_lage | bewegungsbruch | rekoppelnde_lage | -0.0281 | 0.0040 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1238 | rekoppelnde_lage | druck_lage | rekoppelnde_lage | 0.0176 | -0.0084 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1245 | bewegungsbruch | rekoppelnde_lage | offene_lage | -0.0171 | -0.0079 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1287 | rekoppelnde_lage | druck_lage | gehaltene_form | 0.1037 | -0.0015 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1293 | rekoppelnde_lage | druck_lage | druck_lage | 0.2871 | -0.0857 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1534 | rekoppelnde_lage | druck_lage | druck_lage | 0.1075 | -0.0417 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1585 | rekoppelnde_lage | bewegungsbruch | offene_lage | -0.0406 | 0.0004 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1601 | rekoppelnde_lage | druck_lage | bewegungsbruch | 0.0703 | -0.0035 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2092 | offene_lage | bewegungsbruch | rekoppelnde_lage | -0.0270 | 0.0222 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2099 | rekoppelnde_lage | bewegungsbruch | rekoppelnde_lage | -0.0102 | -0.0100 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2413 | rekoppelnde_lage | druck_lage | bewegungsbruch | 0.1026 | -0.0568 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2433 | rekoppelnde_lage | druck_lage | rekoppelnde_lage | 0.0806 | -0.0220 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2449 | rekoppelnde_lage | bewegungsbruch | rekoppelnde_lage | -0.0035 | 0.0192 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2541 | offene_lage | bewegungsbruch | offene_lage | -0.0182 | 0.0325 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2961 | rekoppelnde_lage | druck_lage | rekoppelnde_lage | 0.0160 | -0.0197 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3054 | druck_lage | druck_lage | bewegungsbruch | -0.1280 | 0.0583 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3069 | offene_lage | druck_lage | bewegungsbruch | 0.0024 | -0.0047 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3094 | bewegungsbruch | druck_lage | bewegungsbruch | -0.0084 | 0.0217 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3100 | rekoppelnde_lage | offene_lage | rekoppelnde_lage | -0.0180 | 0.0019 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3559 | bewegungsbruch | offene_lage | rekoppelnde_lage | -0.0981 | 0.0471 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3563 | rekoppelnde_lage | bewegungsbruch | rekoppelnde_lage | -0.0678 | 0.0030 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3651 | rekoppelnde_lage | bewegungsbruch | offene_lage | 0.0393 | -0.0005 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 999 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0527 | -0.0056 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1008 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0021 | 0.0214 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1031 | bewegungsbruch | rekoppelnde_lage | rekoppelnde_lage | -0.1005 | 0.0499 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1044 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0319 | -0.0205 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1096 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0282 | 0.0083 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1139 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0067 | -0.0175 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1144 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0426 | 0.0337 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1160 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0466 | 0.0124 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1193 | bewegungsbruch | rekoppelnde_lage | rekoppelnde_lage | -0.0987 | -0.0102 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1216 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0250 | -0.0023 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1234 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0189 | 0.0127 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1241 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0230 | 0.0026 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1280 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0202 | 0.0066 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1292 | gehaltene_form | rekoppelnde_lage | druck_lage | 0.2327 | -0.0864 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1533 | rekoppelnde_lage | rekoppelnde_lage | druck_lage | 0.2175 | -0.0709 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1555 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0666 | -0.0247 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1590 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0465 | -0.0028 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1616 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0326 | -0.0178 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2098 | rekoppelnde_lage | rekoppelnde_lage | bewegungsbruch | 0.0700 | -0.0283 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2412 | rekoppelnde_lage | rekoppelnde_lage | druck_lage | 0.2467 | -0.0990 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2432 | rekoppelnde_lage | rekoppelnde_lage | druck_lage | 0.1024 | -0.0437 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2438 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0143 | 0.0318 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2461 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0028 | 0.0018 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2542 | gehaltene_form | offene_lage | rekoppelnde_lage | -0.0603 | 0.0346 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2946 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0316 | -0.0074 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3021 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0036 | -0.0125 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3063 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0120 | 0.0165 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3090 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0596 | 0.0013 |
| LONG2025_BTC_QUIET_4000 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3099 | rekoppelnde_lage | rekoppelnde_lage | offene_lage | 0.0229 | -0.0226 |

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
