# 489 - Sol2025 1H Regulationsvorschlag

## Fragestellung

Welche Wahrnehmungsfaehigkeit liegt aus der passiven Sinnesaufnahme-Memory nahe, ohne daraus Handlung, Gate oder Strategie zu machen?

Gelesen wird:

- Input: `489_SOL2025_1H_PASSIVE_SINNESAUFNAHME_MEMORY.csv`

Wichtig: Diese Schicht ist kein aktiver Regler. Sie ist eine passive Regulationsvorschlagsschicht vor dem MCM-Feld.

## Kurzbefund

- Ausgewertete Intake-Spuren: 178.

## Vorschlagsfamilien

| Familie | Count |
|---|---:|
| aufnahme_entlasten | 114 |
| aufnahme_vertiefen | 64 |

## Dominante Vorschlaege

| Vorschlag | Count |
|---|---:|
| Abstand bilden | 67 |
| ruhig hinhoeren | 35 |
| Sehen schaerfen | 28 |
| Druck / Feldkontakt entlasten | 24 |
| leiser / weicher aufnehmen | 23 |
| Fokus halten / vertiefen | 1 |

## Staerkste Spuren

| Achse | Innenfeld | Qualitaet | Ereignisse | Dominanter Vorschlag | Fokus | Abstand | Weicher | Schaerfer | Kontaktentlastung | Hinhoeren |
|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | young_intake_trace | 296 | ruhig hinhoeren | 0.1406 | 0.1675 | 0.1537 | 0.2177 | 0.0688 | 0.7195 |
| sehen_fokus | inner_effect_stable | young_intake_trace | 281 | Sehen schaerfen | 0.4530 | 0.1953 | 0.1706 | 0.5909 | 0.0909 | 0.1320 |
| sehen_abstand | inner_effect_stable | young_intake_trace | 166 | Abstand bilden | 0.4324 | 0.4337 | 0.1876 | 0.3029 | 0.1012 | 0.1232 |
| sehen_abstand | inner_effect_carried_unrest | young_intake_trace | 119 | Abstand bilden | 0.4078 | 0.4715 | 0.2222 | 0.2806 | 0.1209 | 0.0987 |
| hoeren_leise | inner_effect_stable | young_intake_trace | 83 | leiser / weicher aufnehmen | 0.0897 | 0.2795 | 0.4707 | 0.1879 | 0.1526 | 0.3467 |
| hoeren_hin | inner_effect_stable | young_intake_trace | 80 | ruhig hinhoeren | 0.1145 | 0.1667 | 0.1531 | 0.2175 | 0.0681 | 0.7192 |
| ausgeglichen | inner_effect_stable | young_intake_trace | 79 | ruhig hinhoeren | 0.2282 | 0.2107 | 0.1842 | 0.2102 | 0.1018 | 0.2312 |
| sehen_fokus | inner_effect_stable | young_intake_trace | 73 | Sehen schaerfen | 0.4282 | 0.1931 | 0.1694 | 0.5911 | 0.0890 | 0.1322 |
| feldinput | inner_effect_stable | contact_loaded_intake | 64 | Druck / Feldkontakt entlasten | 0.1199 | 0.2857 | 0.2351 | 0.1791 | 0.3569 | 0.0770 |
| hoeren_hin | inner_effect_stable | young_intake_trace | 47 | ruhig hinhoeren | 0.1046 | 0.1727 | 0.1580 | 0.2106 | 0.0707 | 0.7116 |
| sehen_fokus | inner_effect_stable | young_intake_trace | 46 | Sehen schaerfen | 0.4206 | 0.1963 | 0.1720 | 0.5859 | 0.0902 | 0.1265 |
| hoeren_leise | inner_effect_carried_unrest | contact_loaded_intake | 35 | leiser / weicher aufnehmen | 0.0641 | 0.3062 | 0.4969 | 0.1646 | 0.1650 | 0.3210 |
| ausgeglichen | inner_effect_stable | young_intake_trace | 35 | ruhig hinhoeren | 0.2209 | 0.2125 | 0.1852 | 0.2079 | 0.1027 | 0.2287 |
| feldinput | inner_effect_carried_unrest | contact_loaded_intake | 30 | Druck / Feldkontakt entlasten | 0.0882 | 0.3747 | 0.3034 | 0.1466 | 0.4170 | 0.0413 |
| sehen_abstand | inner_effect_stable | young_intake_trace | 27 | Abstand bilden | 0.4166 | 0.4348 | 0.1894 | 0.3039 | 0.1019 | 0.1243 |
| hoeren_leise | inner_effect_stable | young_intake_trace | 25 | leiser / weicher aufnehmen | 0.0789 | 0.2706 | 0.4661 | 0.1834 | 0.1431 | 0.3418 |
| hoeren_hin | inner_effect_stable | young_intake_trace | 22 | ruhig hinhoeren | 0.1100 | 0.1674 | 0.1536 | 0.2205 | 0.0695 | 0.7225 |
| fuehlen_abstand | inner_effect_carried_unrest | contact_loaded_intake | 20 | Abstand bilden | 0.0903 | 0.5508 | 0.2780 | 0.1505 | 0.3788 | 0.0455 |
| hoeren_leise | inner_effect_stable | young_intake_trace | 20 | leiser / weicher aufnehmen | 0.0883 | 0.2538 | 0.4526 | 0.1952 | 0.1336 | 0.3547 |
| feldinput | inner_effect_carried_unrest | contact_loaded_intake | 18 | Druck / Feldkontakt entlasten | 0.0877 | 0.3672 | 0.2984 | 0.1477 | 0.4109 | 0.0424 |
| feldinput | inner_effect_stable | contact_loaded_intake | 18 | Druck / Feldkontakt entlasten | 0.1160 | 0.2836 | 0.2327 | 0.1809 | 0.3566 | 0.0790 |
| feldinput | inner_effect_stable | young_intake_trace | 17 | Druck / Feldkontakt entlasten | 0.1122 | 0.2887 | 0.2397 | 0.1767 | 0.3557 | 0.0744 |
| feldinput | inner_effect_tipping | contact_loaded_intake | 16 | Druck / Feldkontakt entlasten | 0.0484 | 0.5134 | 0.4075 | 0.1017 | 0.5136 | 0.0000 |
| sehen_abstand | inner_effect_carried_unrest | young_intake_trace | 16 | Abstand bilden | 0.3847 | 0.4981 | 0.2430 | 0.2680 | 0.1377 | 0.0848 |

## Interpretation

Die Schicht beschreibt keine Entscheidung. Sie liest nur, welche Wahrnehmungsfaehigkeit aus der bisherigen Aufnahmequalitaet naheliegt.

Damit bleibt die Trennung erhalten:

```text
Sinneskontakt -> passive Aufnahmequalitaet -> Regulationsvorschlag -> noch keine Handlung
```

Die Vorschlaege sind kontinuierliche Zugrichtungen. Sie sind keine Schwellen, keine Sperren und keine Anweisungen.

## Mechanische Grenze

- keine Handlung
- kein Entry
- kein Gate
- keine Strategie
- keine direkte Veraenderung des MCM-Feldes

Die Schicht bereitet nur vor, wie MINI_DIO spaeter lernen koennte, seine Wahrnehmung zu dosieren: Fokus oder Abstand, lauter oder leiser, schaerfer oder unschaerfer, mehr Kontakt oder Entlastung.

## Wie es weitergeht

Als naechstes sollte diese passive Vorschlagsschicht ueber mehrere Welten verglichen werden. Stabil wiederkehrende Vorschlaege koennen spaeter als lernbare Wahrnehmungsfaehigkeiten betrachtet werden, ohne das MCM-Feld direkt zu regeln.
