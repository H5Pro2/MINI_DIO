# Rohwelt-Ruecklesung vor Rekopplungsbindung

## Zweck

Diese Diagnose liest passiv zurueck, welche Weltspannung, Ton-/Energieform und sichtbare Form vor spaeterer Rekopplungsbindung lag.
Sie nutzt Episode-Dateien und betrachtet das Vorfenster vor rekoppelnden Zustandsmomenten.

## Methodische Grenze

- passive Diagnose
- keine Handlung
- kein Gate
- keine Strategie
- Der Zielzustand wird pro Lauf aus der jeweiligen Verteilung gelesen, nicht als feste globale Schwelle

## Befund

- Ausgewertete Laeufe: `32`
- Zielereignisse: `22170`
- Dominante sichtbare Vorformen: `offene_formaufnahme:32`
- Dominante Ton-/Energie-Vorformen: `gedaempfte_energie:32`
- Dominante Weltspannungs-Vorformen: `entlastete_weltspannung:32`

## Laufprofile

| Quelle | Events | Sicht davor | Ton davor | Spannung davor | Formstabilitaet | dForm | Energie-Ton | dTon | Feldaufnahme | dFeld | Ziel-Rekopplung | Ziel-Strain |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `adapted_state_negative_stress_2024_5m_10k` | 1990 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.018854 | -0.022947 | -0.030806 | -0.025293 | 0.100308 | -0.007222 | 0.734476 | 0.123719 |
| `adapted_state_sideways_2024_5m_10k` | 1990 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.021493 | -0.017923 | -0.02862 | -0.023693 | 0.101429 | -0.006657 | 0.73328 | 0.124067 |
| `adapted_state_negative_stress_2024_5m_10k` | 1989 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.01881 | -0.022991 | -0.030792 | -0.025279 | 0.100314 | -0.007216 | 0.73442 | 0.123766 |
| `adapted_state_sideways_2024_5m_10k` | 1989 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.021161 | -0.018255 | -0.028698 | -0.023771 | 0.101398 | -0.006688 | 0.733192 | 0.124276 |
| `adapted_state_positive_expansion_2023_5m_10k` | 1965 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.023971 | -0.019268 | -0.034371 | -0.026978 | 0.098941 | -0.008463 | 0.734917 | 0.123405 |
| `adapted_state_positive_expansion_2023_5m_10k` | 1965 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.023851 | -0.019388 | -0.033525 | -0.026133 | 0.099193 | -0.008212 | 0.734814 | 0.123576 |
| `field_quiet_candidates_btc2025` | 400 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.04602 | -0.023856 | -0.018354 | -0.010932 | 0.096929 | -0.006412 | 0.728707 | 0.126059 |
| `adapted_real_quiet_sol_2025_5m_2000` | 399 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.060006 | 0.000743 | -0.026431 | -0.017955 | 0.104276 | -0.004467 | 0.726529 | 0.127465 |
| `adapted_real_sequence_break_sol_2025_5m_2000` | 399 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.028426 | -0.018332 | -0.018971 | -0.012667 | 0.100135 | -0.005668 | 0.727733 | 0.127247 |
| `field_quiet_candidates_sol2025` | 399 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.060006 | 0.000743 | -0.026431 | -0.017955 | 0.104276 | -0.004467 | 0.726529 | 0.127465 |
| `adapted_real_sequence_break_sol_2025_5m_2000` | 398 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.028339 | -0.01842 | -0.018416 | -0.012112 | 0.099919 | -0.005883 | 0.727451 | 0.127523 |
| `field_quiet_candidates_btc2025` | 398 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.04427 | -0.025605 | -0.019053 | -0.01163 | 0.096189 | -0.007152 | 0.728408 | 0.126136 |
| `field_quiet_candidates_sol2025` | 398 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.029465 | -0.004069 | -0.029195 | -0.021952 | 0.104325 | -0.004969 | 0.725244 | 0.128178 |
| `adapted_real_quiet_sol_2025_5m_2000` | 397 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.057743 | -0.00152 | -0.025735 | -0.017258 | 0.10418 | -0.004564 | 0.726894 | 0.127229 |
| `field_quiet_candidates_btc2025` | 397 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.056613 | -0.016901 | -0.012059 | -0.006167 | 0.104406 | -0.000171 | 0.728981 | 0.125784 |
| `field_quiet_candidates_sol2025` | 397 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.057743 | -0.00152 | -0.025735 | -0.017258 | 0.10418 | -0.004564 | 0.726894 | 0.127229 |
| `field_quiet_candidates_sol2025` | 397 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.054241 | -0.004024 | -0.022145 | -0.015886 | 0.102607 | -0.004428 | 0.726557 | 0.125617 |
| `field_quiet_candidates_sol2025` | 397 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.054313 | -0.003953 | -0.021391 | -0.015132 | 0.102905 | -0.00413 | 0.726153 | 0.12579 |
| `field_quiet_candidates_btc2025` | 396 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.055927 | -0.017588 | -0.012877 | -0.006986 | 0.104054 | -0.000523 | 0.728792 | 0.126066 |
| `field_quiet_candidates_btc2025` | 396 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.036985 | -0.01573 | -0.015497 | -0.011036 | 0.096655 | -0.006735 | 0.727878 | 0.125655 |
| `field_quiet_candidates_btc2025` | 395 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.049972 | -0.019467 | -0.022752 | -0.014447 | 0.103239 | -0.001745 | 0.727898 | 0.126726 |
| `field_quiet_candidates_btc2025` | 395 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.021006 | -0.026086 | -0.016671 | -0.011684 | 0.10209 | -0.002822 | 0.727137 | 0.127226 |
| `field_quiet_candidates_btc2025` | 395 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.036079 | -0.016636 | -0.014461 | -0.01 | 0.096848 | -0.006542 | 0.727513 | 0.126024 |
| `field_quiet_candidates_sol2025` | 394 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.02881 | -0.004724 | -0.02914 | -0.021897 | 0.104603 | -0.004691 | 0.724951 | 0.128696 |
| `field_quiet_candidates_btc2025` | 393 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.051287 | -0.018151 | -0.02215 | -0.013846 | 0.103517 | -0.001467 | 0.727669 | 0.127135 |
| `field_quiet_candidates_sol2025` | 393 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.028115 | -0.014271 | -0.028421 | -0.021358 | 0.100287 | -0.006488 | 0.72819 | 0.127041 |
| `field_quiet_candidates_sol2025` | 392 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.024859 | -0.017527 | -0.027804 | -0.020742 | 0.100013 | -0.006761 | 0.727921 | 0.127516 |
| `field_quiet_candidates_sol2025` | 392 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.01871 | -0.02545 | -0.026536 | -0.019088 | 0.100865 | -0.006225 | 0.727983 | 0.126626 |
| `real_sequence_break_btc_2025_5m_2000` | 392 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.035034 | -0.012956 | -0.016619 | -0.011825 | 0.099536 | -0.006699 | 0.727549 | 0.126017 |
| `field_quiet_candidates_btc2025` | 391 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.021117 | -0.025975 | -0.017701 | -0.012713 | 0.10297 | -0.001942 | 0.726804 | 0.127132 |
| `field_quiet_candidates_sol2025` | 391 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.018317 | -0.025844 | -0.024907 | -0.017459 | 0.10113 | -0.005959 | 0.727676 | 0.127014 |
| `real_sequence_break_btc_2025_5m_2000` | 391 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.037373 | -0.010616 | -0.017337 | -0.012543 | 0.099542 | -0.006692 | 0.727174 | 0.126058 |

## Arbeitsableitung

```text
Spaetere Zielbindung (Rekopplungsbindung) entsteht nicht aus einem einzelnen Rohwert.
Ruecklesbar ist ein Vorfeld aus sichtbarer Formlage, tonaler Energieform und regulierter Feldaufnahme.
Die relativen Delta-Spalten zeigen, ob dieses Vorfeld gegen die jeweilige Weltbasis abweicht.
Damit liegt die Ursache nicht direkt in der Rohwelt, sondern in der Art, wie die Rohwelt vorher sinnlich aufgenommen wurde.
```

## Wie es weitergeht

Als naechstes sollten Rekopplungs- und Fragmentierungsruecklesung direkt nebeneinander gelegt werden.
Dann wird sichtbar, welche Vorwelt eher Bindung vorbereitet und welche eher Last/Fragmentierung vorbereitet.