# Rohwelt-Ruecklesung vor belasteter Fragmentierung

## Zweck

Diese Diagnose liest passiv zurueck, welche Weltspannung, Ton-/Energieform und sichtbare Form vor spaeterer belasteter Fragmentierung lag.
Sie nutzt Episode-Dateien und betrachtet das Vorfenster vor belasteten Fragmentierungszustandsmomenten.

## Methodische Grenze

- passive Diagnose
- keine Handlung
- kein Gate
- keine Strategie
- Der Zielzustand wird pro Lauf aus der jeweiligen Verteilung gelesen, nicht als feste globale Schwelle

## Befund

- Ausgewertete Laeufe: `24`
- Zielereignisse: `41`
- Dominante sichtbare Vorformen: `offene_formaufnahme:20 | sichtbar_stabile_form:4`
- Dominante Ton-/Energie-Vorformen: `gedaempfte_energie:20 | tonaler_wechsel:4`
- Dominante Weltspannungs-Vorformen: `entlastete_weltspannung:24`

## Laufprofile

| Quelle | Events | Sicht davor | Ton davor | Spannung davor | Formstabilitaet | dForm | Energie-Ton | dTon | Feldaufnahme | dFeld | Ziel-Rekopplung | Ziel-Strain |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `adapted_state_positive_expansion_2023_5m_10k` | 4 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.041378 | -0.001862 | 0.010135 | 0.017528 | 0.098105 | -0.009299 | 0.543078 | 0.337072 |
| `adapted_state_positive_expansion_2023_5m_10k` | 4 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.041378 | -0.001862 | 0.010135 | 0.017528 | 0.098105 | -0.009299 | 0.542406 | 0.336704 |
| `adapted_real_sequence_break_sol_2025_5m_2000` | 3 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | -0.009221 | -0.05598 | -0.101616 | -0.095312 | 0.074856 | -0.030946 | 0.542167 | 0.336723 |
| `adapted_real_sequence_break_sol_2025_5m_2000` | 3 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | -0.009221 | -0.05598 | -0.101616 | -0.095312 | 0.074856 | -0.030946 | 0.541723 | 0.336484 |
| `adapted_state_sideways_2024_5m_10k` | 3 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.200516 | 0.1611 | 0.02036 | 0.025287 | 0.099232 | -0.008854 | 0.540978 | 0.337572 |
| `adapted_state_sideways_2024_5m_10k` | 3 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.200516 | 0.1611 | 0.02036 | 0.025287 | 0.099232 | -0.008854 | 0.540409 | 0.337237 |
| `field_quiet_candidates_sol2025` | 2 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | -0.044688 | -0.078222 | -0.03644 | -0.029197 | 0.082975 | -0.026318 | 0.54006 | 0.338592 |
| `field_quiet_candidates_sol2025` | 2 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | -0.044688 | -0.078222 | -0.03644 | -0.029197 | 0.082975 | -0.026318 | 0.539836 | 0.338469 |
| `real_sequence_break_btc_2025_5m_2000` | 2 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | -0.019194 | -0.067184 | -0.088314 | -0.083519 | 0.089657 | -0.016578 | 0.543777 | 0.333859 |
| `adapted_real_quiet_sol_2025_5m_2000` | 1 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.046537 | -0.012726 | 0.13639 | 0.144866 | 0.109348 | 0.000604 | 0.530899 | 0.347875 |
| `adapted_real_quiet_sol_2025_5m_2000` | 1 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.046537 | -0.012726 | 0.13639 | 0.144866 | 0.109348 | 0.000604 | 0.530452 | 0.347629 |
| `adapted_state_negative_stress_2024_5m_10k` | 1 | `offene_formaufnahme` | `tonaler_wechsel` | `entlastete_weltspannung` | 0.173135 | 0.131334 | 0.020425 | 0.025938 | 0.131684 | 0.024153 | 0.53928 | 0.339596 |
| `adapted_state_negative_stress_2024_5m_10k` | 1 | `offene_formaufnahme` | `tonaler_wechsel` | `entlastete_weltspannung` | 0.173135 | 0.131334 | 0.020425 | 0.025938 | 0.131684 | 0.024153 | 0.538009 | 0.338866 |
| `field_quiet_candidates_btc2025` | 1 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | -0.174208 | -0.244084 | 0.058029 | 0.065452 | 0.104906 | 0.001565 | 0.539616 | 0.338224 |
| `field_quiet_candidates_btc2025` | 1 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | -0.174208 | -0.244084 | 0.058029 | 0.065452 | 0.104906 | 0.001565 | 0.539182 | 0.337983 |
| `field_quiet_candidates_sol2025` | 1 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.046537 | -0.012726 | 0.13639 | 0.144866 | 0.109348 | 0.000604 | 0.530899 | 0.347875 |
| `field_quiet_candidates_sol2025` | 1 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.046537 | -0.012726 | 0.13639 | 0.144866 | 0.109348 | 0.000604 | 0.530452 | 0.347629 |
| `field_quiet_candidates_sol2025` | 1 | `sichtbar_stabile_form` | `tonaler_wechsel` | `entlastete_weltspannung` | 0.472308 | 0.429922 | 0.123424 | 0.130487 | 0.102555 | -0.00422 | 0.552003 | 0.325097 |
| `field_quiet_candidates_sol2025` | 1 | `sichtbar_stabile_form` | `tonaler_wechsel` | `entlastete_weltspannung` | 0.472308 | 0.429922 | 0.123424 | 0.130487 | 0.102555 | -0.00422 | 0.551887 | 0.32505 |
| `field_quiet_candidates_sol2025` | 1 | `sichtbar_stabile_form` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.358375 | 0.300109 | 0.027111 | 0.03337 | 0.132294 | 0.025259 | 0.544261 | 0.330526 |
| `field_quiet_candidates_sol2025` | 1 | `sichtbar_stabile_form` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.358375 | 0.300109 | 0.027111 | 0.03337 | 0.132294 | 0.025259 | 0.543823 | 0.330303 |
| `field_quiet_candidates_sol2025` | 1 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.028605 | -0.015556 | 0.14141 | 0.148858 | 0.102795 | -0.004295 | 0.535475 | 0.340659 |
| `field_quiet_candidates_sol2025` | 1 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.028605 | -0.015556 | 0.14141 | 0.148858 | 0.102795 | -0.004295 | 0.535423 | 0.340632 |
| `real_sequence_break_btc_2025_5m_2000` | 1 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | -0.094108 | -0.142097 | 0.030084 | 0.034879 | 0.095549 | -0.010686 | 0.539906 | 0.336769 |

## Arbeitsableitung

```text
Spaetere Zielbindung (belastete Fragmentierung) entsteht nicht aus einem einzelnen Rohwert.
Ruecklesbar ist ein Vorfeld aus sichtbarer Formlage, tonaler Energieform und regulierter Feldaufnahme.
Die relativen Delta-Spalten zeigen, ob dieses Vorfeld gegen die jeweilige Weltbasis abweicht.
Damit liegt die Ursache nicht direkt in der Rohwelt, sondern in der Art, wie die Rohwelt vorher sinnlich aufgenommen wurde.
```

## Wie es weitergeht

Als naechstes sollten Rekopplungs- und Fragmentierungsruecklesung direkt nebeneinander gelegt werden.
Dann wird sichtbar, welche Vorwelt eher Bindung vorbereitet und welche eher Last/Fragmentierung vorbereitet.