# MCM-Zentrumsachse: lokale Kontaktsegmente

## Zweck

Diese Datei liest konkrete Kontaktsegmente der staerksten Zentrumsachse.
Getrennt wird zwischen echtem Paarsegment und Einzelknoten-Kontakt.

## Sicherheitsgrenze

- passive Ruecklesung
- keine Handlung
- kein Gate
- keine Strategie

## Zusammenfassung

- Achse: `183drjy<->1t5bcxp`
- Kontaktsegmente gesamt: 1944
- Paarsegmente: 26
- Kontaktarten: `nur_b:1236 | nur_a:682 | paar_gemeinsam:26`
- Segmentlesung: `b_knoten_kontakt:1236 | a_knoten_kontakt:682 | paarsegment_rekoppelnd:16 | kontaktsegment_offen:7 | paarsegment_spannungswechsel:3`
- Welten: `SOL_2023_NEG_STRESS_10K_RECEPTOR:594 | SOL_2026_STABLE_5K_RECEPTOR:352 | SOL_2024_SIDEWAYS_5K_RECEPTOR:298 | SOL_2025_STRESS_5K_RECEPTOR:268 | BTC_2024_1H_RECEPTOR:76 | SOL_2024_1H_RECEPTOR:70`
- Paarsegmente Rekopplung: 0.0
- Paarsegmente Strain: 0.0
- Paarsegmente Pressure-Delta: 0.01684
- Paarsegmente Rekopplung-Delta: -0.007458

## Paarsegmente

| Welt | Tick | Quelle | Effekt | Klassen | Rekopplung | Strain | Pressure Delta | Rekopplung Delta | Lesung |
|---|---:|---|---|---|---:|---:|---:|---:|---|
| `-` | - | `542_MCM_FELDBEWEGUNGS_MEMORY_MEHRQUELLEN_UEBERGANGSRAUM.csv` | `recurrently_opening_strain` | `- / - / -` | 0.0 | 0.0 | 0.02074 | -0.023905 | `paarsegment_spannungswechsel` |
| `-` | - | `542_MCM_FELDBEWEGUNGS_MEMORY_MEHRQUELLEN_UEBERGANGSRAUM.csv` | `recurrently_reconnecting` | `- / - / -` | 0.0 | 0.0 | -0.016196 | 0.022663 | `kontaktsegment_offen` |
| `EXT_EXPANSION_2023` | 503 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `rekoppelnde_lage` | `rekoppelnde_lage / rekoppelnde_lage / rekoppelnde_lage` | 0.0 | 0.0 | 0.019712 | -0.0182 | `paarsegment_rekoppelnd` |
| `EXT_EXPANSION_2023` | 506 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `rekoppelnde_lage` | `rekoppelnde_lage / rekoppelnde_lage / rekoppelnde_lage` | 0.0 | 0.0 | 0.031329 | 0.014827 | `paarsegment_rekoppelnd` |
| `EXT_EXPANSION_2023` | 507 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `rekoppelnde_lage` | `rekoppelnde_lage / rekoppelnde_lage / bewegungsbruch` | 0.0 | 0.0 | 0.105197 | -0.012622 | `paarsegment_rekoppelnd` |
| `EXT_EXPANSION_2023` | 509 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `bewegungsbruch` | `rekoppelnde_lage / bewegungsbruch / rekoppelnde_lage` | 0.0 | 0.0 | -0.038149 | -0.005356 | `kontaktsegment_offen` |
| `EXT_EXPANSION_2023` | 514 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `rekoppelnde_lage` | `rekoppelnde_lage / rekoppelnde_lage / rekoppelnde_lage` | 0.0 | 0.0 | 0.044639 | -0.026322 | `paarsegment_rekoppelnd` |
| `EXT_EXPANSION_2023` | 515 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `rekoppelnde_lage` | `rekoppelnde_lage / rekoppelnde_lage / rekoppelnde_lage` | 0.0 | 0.0 | -0.014525 | -0.001924 | `paarsegment_rekoppelnd` |
| `EXT_EXPANSION_2023` | 517 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `rekoppelnde_lage` | `rekoppelnde_lage / rekoppelnde_lage / rekoppelnde_lage` | 0.0 | 0.0 | -0.046413 | 0.026433 | `paarsegment_rekoppelnd` |
| `EXT_EXPANSION_2023` | 526 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `druck_lage` | `rekoppelnde_lage / druck_lage / bewegungsbruch` | 0.0 | 0.0 | -0.076833 | -0.004621 | `kontaktsegment_offen` |
| `NEG_STRESS_2023` | 771 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `rekoppelnde_lage` | `rekoppelnde_lage / rekoppelnde_lage / rekoppelnde_lage` | 0.0 | 0.0 | -0.001943 | 0.025902 | `paarsegment_rekoppelnd` |
| `NEG_STRESS_2023` | 802 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `druck_lage` | `offene_lage / druck_lage / rekoppelnde_lage` | 0.0 | 0.0 | -0.015293 | 0.0206 | `kontaktsegment_offen` |
| `NEG_STRESS_2023` | 815 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `rekoppelnde_lage` | `rekoppelnde_lage / rekoppelnde_lage / rekoppelnde_lage` | 0.0 | 0.0 | 0.081003 | -0.007175 | `paarsegment_rekoppelnd` |
| `NEG_STRESS_2023` | 816 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `rekoppelnde_lage` | `rekoppelnde_lage / rekoppelnde_lage / rekoppelnde_lage` | 0.0 | 0.0 | 0.13052 | -0.029768 | `paarsegment_rekoppelnd` |
| `POS_EXPANSION_2023` | 571 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `rekoppelnde_lage` | `rekoppelnde_lage / rekoppelnde_lage / rekoppelnde_lage` | 0.0 | 0.0 | -0.030417 | -0.022347 | `paarsegment_rekoppelnd` |
| `POS_EXPANSION_2023` | 572 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `rekoppelnde_lage` | `rekoppelnde_lage / rekoppelnde_lage / rekoppelnde_lage` | 0.0 | 0.0 | -0.034707 | -0.025772 | `paarsegment_rekoppelnd` |
| `POS_EXPANSION_2023` | 576 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `rekoppelnde_lage` | `rekoppelnde_lage / rekoppelnde_lage / rekoppelnde_lage` | 0.0 | 0.0 | -0.054197 | 0.018725 | `paarsegment_rekoppelnd` |
| `POS_EXPANSION_2023` | 646 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `offene_lage` | `druck_lage / offene_lage / rekoppelnde_lage` | 0.0 | 0.0 | -0.141199 | 0.00712 | `kontaktsegment_offen` |
| `POS_EXPANSION_2023` | 651 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `rekoppelnde_lage` | `rekoppelnde_lage / rekoppelnde_lage / rekoppelnde_lage` | 0.0 | 0.0 | 0.185396 | -0.027456 | `paarsegment_rekoppelnd` |
| `POS_EXPANSION_2023` | 653 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `druck_lage` | `rekoppelnde_lage / druck_lage / bewegungsbruch` | 0.0 | 0.0 | 0.141314 | -0.042826 | `paarsegment_spannungswechsel` |
| `SIDEWAYS_2024` | 917 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `rekoppelnde_lage` | `rekoppelnde_lage / rekoppelnde_lage / rekoppelnde_lage` | 0.0 | 0.0 | -0.006888 | 0.00903 | `paarsegment_rekoppelnd` |
| `SIDEWAYS_2024` | 920 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `druck_lage` | `rekoppelnde_lage / druck_lage / rekoppelnde_lage` | 0.0 | 0.0 | 0.050905 | -0.03663 | `paarsegment_spannungswechsel` |
| `SIDEWAYS_2024` | 927 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `rekoppelnde_lage` | `rekoppelnde_lage / rekoppelnde_lage / rekoppelnde_lage` | 0.0 | 0.0 | 0.036541 | -0.001662 | `paarsegment_rekoppelnd` |
| `SIDEWAYS_2024` | 934 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `offene_lage` | `bewegungsbruch / offene_lage / bewegungsbruch` | 0.0 | 0.0 | -0.030912 | -0.014033 | `kontaktsegment_offen` |
| `SIDEWAYS_2026` | 905 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `rekoppelnde_lage` | `rekoppelnde_lage / rekoppelnde_lage / bewegungsbruch` | 0.0 | 0.0 | 0.101288 | -0.035123 | `paarsegment_rekoppelnd` |
| `SIDEWAYS_2026` | 906 | `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv` | `bewegungsbruch` | `rekoppelnde_lage / bewegungsbruch / rekoppelnde_lage` | 0.0 | 0.0 | -0.003065 | -0.003463 | `kontaktsegment_offen` |

## Befund

Paarsegmente zeigen, wo die Achse lokal wirklich gekoppelt auftritt.
Einzelknoten-Kontakte zeigen dagegen breite Feldnaehe ohne zwingende Achsenkopplung.

Arbeitsableitung:

```text
Die Zentrumsachse ist nicht nur ein globaler Name.
Sie besitzt lokale Kontaktsegmente, in denen Weltlage, MCM-Wirkung und Rollennaehe zusammenfallen.
```

## Wie es weitergeht

Als naechstes sollte geprueft werden, welche dieser Kontaktsegmente reproduzierbar wiederkehren und welche nur situationsbedingt auftreten.
