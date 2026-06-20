# Bewegungsarten Rohwelt-Segmente

Stand: 2026-06-20 00:37:27

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
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | nachher | 320 | 6 | offene_lage | zentrum_stabil | 0.0519 | 0.2322 | 0.2327 | 0.2322 | 0.7106 | 0.1942 | 0.6455 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | vorher | 320 | 6 | offene_lage | zentrum_stabil | 0.0864 | 0.2471 | 0.2447 | 0.2353 | 0.7149 | 0.1945 | 0.6472 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | wechsel | 160 | 6 | druck_lage | zentrum_stabil | 0.0477 | 0.3219 | 0.3408 | 0.2978 | 0.6690 | 0.2338 | 0.6203 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | nachher | 430 | 6 | offene_lage | zentrum_stabil | 0.0303 | 0.1821 | 0.2062 | 0.1869 | 0.7128 | 0.1729 | 0.6575 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | vorher | 430 | 6 | offene_lage | zentrum_stabil | 0.0102 | 0.1554 | 0.1851 | 0.1756 | 0.7176 | 0.1676 | 0.6593 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | wechsel | 215 | 6 | offene_lage | zentrum_stabil | 0.0449 | 0.1238 | 0.1362 | 0.1462 | 0.7282 | 0.1420 | 0.6809 |

## Ereignislupe

| Welt | Paar | Tick | Vorher | Wechsel | Nachher | dDruck | dRekopplung |
|---|---|---:|---|---|---|---:|---:|
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1172 | offene_lage | druck_lage | bewegungsbruch | -0.0214 | 0.0013 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1191 | offene_lage | offene_lage | offene_lage | -0.0125 | 0.0026 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1195 | offene_lage | offene_lage | offene_lage | -0.0337 | 0.0133 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 3294 | offene_lage | offene_lage | offene_lage | -0.0141 | 0.0164 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 4566 | offene_lage | offene_lage | offene_lage | 0.0080 | 0.0058 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 4570 | offene_lage | bewegungsbruch | offene_lage | -0.1000 | 0.0182 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 4593 | offene_lage | offene_lage | offene_lage | -0.0460 | -0.0006 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 4612 | offene_lage | druck_lage | bewegungsbruch | 0.2308 | -0.0734 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 4713 | offene_lage | offene_lage | offene_lage | 0.0930 | -0.0098 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 4717 | offene_lage | bewegungsbruch | offene_lage | -0.0231 | 0.0030 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 4736 | bewegungsbruch | offene_lage | offene_lage | -0.1117 | 0.0324 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 4742 | offene_lage | druck_lage | bewegungsbruch | 0.0517 | -0.0019 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 4836 | offene_lage | offene_lage | offene_lage | -0.0763 | 0.0194 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 4993 | offene_lage | druck_lage | bewegungsbruch | -0.2165 | -0.0226 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 5089 | offene_lage | druck_lage | bewegungsbruch | -0.0074 | -0.0129 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 5098 | offene_lage | offene_lage | offene_lage | -0.0735 | 0.0034 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 5104 | offene_lage | druck_lage | druck_lage | 0.0575 | 0.0100 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 5121 | offene_lage | offene_lage | druck_lage | 0.1671 | -0.0186 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 5417 | druck_lage | druck_lage | druck_lage | 0.2052 | -0.0010 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 6085 | druck_lage | druck_lage | druck_lage | -0.0469 | 0.0051 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 6116 | offene_lage | offene_lage | druck_lage | 0.2739 | -0.0731 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 6147 | druck_lage | druck_lage | offene_lage | -0.0280 | 0.0041 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 7072 | druck_lage | druck_lage | druck_lage | -0.2237 | 0.0133 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 7107 | offene_lage | druck_lage | druck_lage | 0.1020 | 0.0151 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 7117 | offene_lage | offene_lage | offene_lage | -0.1232 | 0.0269 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 8714 | offene_lage | druck_lage | bewegungsbruch | -0.1862 | -0.0243 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 9051 | offene_lage | druck_lage | druck_lage | 0.1302 | -0.0293 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 9871 | druck_lage | druck_lage | offene_lage | -0.2313 | 0.0167 |
| EXPANSION_10K | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 9879 | offene_lage | bewegungsbruch | bewegungsbruch | -0.0033 | 0.0155 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1081 | offene_lage | offene_lage | offene_lage | -0.0304 | 0.0103 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1145 | offene_lage | offene_lage | offene_lage | 0.0001 | -0.0169 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1189 | offene_lage | offene_lage | offene_lage | 0.0686 | -0.0256 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1193 | offene_lage | offene_lage | offene_lage | 0.0140 | -0.0008 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1196 | offene_lage | offene_lage | offene_lage | -0.0347 | 0.0252 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1620 | offene_lage | offene_lage | offene_lage | -0.0028 | -0.0243 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3292 | offene_lage | offene_lage | offene_lage | -0.0435 | -0.0461 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3295 | offene_lage | offene_lage | offene_lage | 0.0112 | 0.0199 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 3828 | offene_lage | offene_lage | offene_lage | -0.0081 | 0.0292 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 4565 | offene_lage | offene_lage | offene_lage | -0.0103 | 0.0124 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 4567 | offene_lage | offene_lage | offene_lage | 0.0280 | -0.0044 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 4571 | offene_lage | offene_lage | offene_lage | -0.1600 | 0.0468 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 4611 | offene_lage | offene_lage | druck_lage | 0.1607 | -0.0704 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 4711 | offene_lage | offene_lage | offene_lage | 0.0334 | -0.0080 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 4716 | offene_lage | offene_lage | bewegungsbruch | -0.0352 | 0.0148 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 4718 | offene_lage | offene_lage | offene_lage | -0.0194 | -0.0028 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 4737 | offene_lage | offene_lage | offene_lage | -0.0661 | 0.0487 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 4814 | offene_lage | offene_lage | offene_lage | 0.1671 | -0.0084 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 4838 | offene_lage | offene_lage | offene_lage | -0.0178 | 0.0246 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 5083 | offene_lage | offene_lage | offene_lage | 0.0109 | 0.0222 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 5097 | offene_lage | offene_lage | offene_lage | -0.0354 | 0.0010 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 5099 | offene_lage | offene_lage | offene_lage | 0.0337 | 0.0139 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 5118 | offene_lage | gehaltene_form | offene_lage | 0.1101 | -0.0182 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 5336 | offene_lage | offene_lage | offene_lage | 0.0127 | 0.0024 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 6044 | offene_lage | offene_lage | offene_lage | 0.0760 | 0.0069 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 6115 | bewegungsbruch | offene_lage | offene_lage | 0.1286 | -0.0410 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 6141 | offene_lage | offene_lage | offene_lage | 0.0382 | -0.0351 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 6170 | offene_lage | offene_lage | offene_lage | 0.0171 | -0.0143 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 6329 | offene_lage | offene_lage | offene_lage | -0.0134 | 0.0090 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 7102 | offene_lage | offene_lage | offene_lage | -0.0072 | 0.0019 |
| EXPANSION_10K | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 7113 | offene_lage | gehaltene_form | gehaltene_form | 0.0918 | -0.0223 |

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
