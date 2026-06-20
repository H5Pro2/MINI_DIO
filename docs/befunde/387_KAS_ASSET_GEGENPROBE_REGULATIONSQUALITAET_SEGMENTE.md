# Bewegungsarten Rohwelt-Segmente

Stand: 2026-06-20 08:38:21

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
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | nachher | 18 | 2 | rekoppelnde_lage | zentrum_stabil | 0.0637 | 0.2575 | 0.3419 | 0.2606 | 0.8292 | 0.2164 | 0.6309 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | vorher | 18 | 2 | rekoppelnde_lage | zentrum_stabil | 0.0707 | 0.1811 | 0.2252 | 0.1966 | 0.8869 | 0.1841 | 0.6498 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | wechsel | 9 | 2 | druck_lage | offene_variante | 0.1785 | 0.2312 | 0.4988 | 0.3290 | 0.7184 | 0.2647 | 0.6020 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | nachher | 14 | 2 | rekoppelnde_lage | zentrum_stabil | 0.1179 | 0.0913 | 0.2650 | 0.1835 | 0.8748 | 0.1837 | 0.6498 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | vorher | 14 | 2 | rekoppelnde_lage | zentrum_stabil | 0.1372 | 0.0757 | 0.1961 | 0.1529 | 0.9097 | 0.1674 | 0.6599 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | wechsel | 7 | 2 | rekoppelnde_lage | zentrum_stabil | 0.1624 | 0.0647 | 0.1201 | 0.1247 | 0.9343 | 0.1442 | 0.6757 |

## Ereignislupe

| Welt | Paar | Tick | Vorher | Wechsel | Nachher | dDruck | dRekopplung |
|---|---|---:|---|---|---|---:|---:|
| KAS2024_15M_ASSET_PROBE | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1970 | rekoppelnde_lage | druck_lage | bewegungsbruch | 0.0656 | -0.0008 |
| KAS2024_15M_ASSET_PROBE | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1982 | offene_lage | druck_lage | rekoppelnde_lage | -0.0219 | -0.0046 |
| KAS2024_15M_ASSET_PROBE | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1975 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0215 | 0.0077 |
| KAS2024_1H_ASSET_PROBE | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 447 | rekoppelnde_lage | offene_lage | druck_lage | 0.1978 | -0.0476 |
| KAS2024_1H_ASSET_PROBE | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 505 | rekoppelnde_lage | druck_lage | rekoppelnde_lage | 0.1115 | -0.0282 |
| KAS2024_1H_ASSET_PROBE | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 849 | rekoppelnde_lage | bewegungsbruch | rekoppelnde_lage | -0.0621 | 0.0088 |
| KAS2024_1H_ASSET_PROBE | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 907 | bewegungsbruch | bewegungsbruch | bewegungsbruch | -0.0767 | -0.0043 |
| KAS2024_1H_ASSET_PROBE | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1512 | offene_lage | druck_lage | rekoppelnde_lage | 0.0719 | -0.0251 |
| KAS2024_1H_ASSET_PROBE | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1642 | rekoppelnde_lage | offene_lage | bewegungsbruch | 0.1956 | -0.0501 |
| KAS2024_1H_ASSET_PROBE | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 1665 | rekoppelnde_lage | druck_lage | bewegungsbruch | 0.0941 | -0.0181 |
| KAS2024_1H_ASSET_PROBE | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 444 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0154 | -0.0224 |
| KAS2024_1H_ASSET_PROBE | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 503 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.1213 | -0.0378 |
| KAS2024_1H_ASSET_PROBE | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 822 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0191 | -0.0011 |
| KAS2024_1H_ASSET_PROBE | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 859 | offene_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0485 | 0.0155 |
| KAS2024_1H_ASSET_PROBE | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1641 | rekoppelnde_lage | rekoppelnde_lage | offene_lage | 0.1274 | -0.0329 |
| KAS2024_1H_ASSET_PROBE | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 1656 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | 0.0012 | 0.0007 |

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
