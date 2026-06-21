# 488 - Sol2025 5M Regulationsvorschlag

## Fragestellung

Welche Wahrnehmungsfaehigkeit liegt aus der passiven Sinnesaufnahme-Memory nahe, ohne daraus Handlung, Gate oder Strategie zu machen?

Gelesen wird:

- Input: `488_SOL2025_5M_PASSIVE_SINNESAUFNAHME_MEMORY.csv`

Wichtig: Diese Schicht ist kein aktiver Regler. Sie ist eine passive Regulationsvorschlagsschicht vor dem MCM-Feld.

## Kurzbefund

- Ausgewertete Intake-Spuren: 132.

## Vorschlagsfamilien

| Familie | Count |
|---|---:|
| aufnahme_entlasten | 85 |
| aufnahme_vertiefen | 47 |

## Dominante Vorschlaege

| Vorschlag | Count |
|---|---:|
| Abstand bilden | 52 |
| Sehen schaerfen | 24 |
| ruhig hinhoeren | 22 |
| leiser / weicher aufnehmen | 17 |
| Druck / Feldkontakt entlasten | 16 |
| Fokus halten / vertiefen | 1 |

## Staerkste Spuren

| Achse | Innenfeld | Qualitaet | Ereignisse | Dominanter Vorschlag | Fokus | Abstand | Weicher | Schaerfer | Kontaktentlastung | Hinhoeren |
|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | young_intake_trace | 348 | ruhig hinhoeren | 0.1466 | 0.1673 | 0.1532 | 0.2175 | 0.0687 | 0.7192 |
| sehen_fokus | inner_effect_stable | young_intake_trace | 320 | Sehen schaerfen | 0.4564 | 0.2011 | 0.1746 | 0.5894 | 0.0952 | 0.1303 |
| sehen_abstand | inner_effect_stable | young_intake_trace | 150 | Abstand bilden | 0.4298 | 0.4368 | 0.1899 | 0.3022 | 0.1035 | 0.1224 |
| sehen_abstand | inner_effect_carried_unrest | young_intake_trace | 126 | Abstand bilden | 0.4117 | 0.4685 | 0.2193 | 0.2842 | 0.1199 | 0.1026 |
| hoeren_hin | inner_effect_stable | young_intake_trace | 108 | ruhig hinhoeren | 0.1107 | 0.1744 | 0.1597 | 0.2091 | 0.0712 | 0.7100 |
| hoeren_leise | inner_effect_stable | young_intake_trace | 104 | leiser / weicher aufnehmen | 0.0953 | 0.2680 | 0.4625 | 0.1916 | 0.1441 | 0.3507 |
| feldinput | inner_effect_stable | contact_loaded_intake | 89 | Druck / Feldkontakt entlasten | 0.1217 | 0.2932 | 0.2399 | 0.1776 | 0.3628 | 0.0754 |
| ausgeglichen | inner_effect_stable | young_intake_trace | 84 | ruhig hinhoeren | 0.2273 | 0.2144 | 0.1865 | 0.2085 | 0.1044 | 0.2294 |
| sehen_fokus | inner_effect_stable | young_intake_trace | 74 | Sehen schaerfen | 0.4181 | 0.2101 | 0.1829 | 0.5790 | 0.0987 | 0.1189 |
| sehen_abstand | inner_effect_stable | young_intake_trace | 61 | Abstand bilden | 0.4148 | 0.4348 | 0.1891 | 0.2970 | 0.1001 | 0.1167 |
| feldinput | inner_effect_carried_unrest | contact_loaded_intake | 51 | Druck / Feldkontakt entlasten | 0.0948 | 0.3547 | 0.2904 | 0.1514 | 0.4013 | 0.0466 |
| sehen_abstand | inner_effect_carried_unrest | young_intake_trace | 41 | Abstand bilden | 0.3995 | 0.4691 | 0.2196 | 0.2819 | 0.1199 | 0.1001 |
| hoeren_leise | inner_effect_carried_unrest | contact_loaded_intake | 41 | leiser / weicher aufnehmen | 0.0688 | 0.2979 | 0.4898 | 0.1693 | 0.1602 | 0.3262 |
| fuehlen_abstand | inner_effect_carried_unrest | contact_loaded_intake | 36 | Abstand bilden | 0.0883 | 0.5752 | 0.2951 | 0.1458 | 0.3973 | 0.0404 |
| hoeren_leise | inner_effect_stable | young_intake_trace | 23 | leiser / weicher aufnehmen | 0.0747 | 0.2855 | 0.4774 | 0.1788 | 0.1533 | 0.3366 |
| hoeren_hin | inner_effect_stable | young_intake_trace | 23 | ruhig hinhoeren | 0.1103 | 0.1605 | 0.1474 | 0.2206 | 0.0646 | 0.7227 |
| hoeren_leise | inner_effect_carried_unrest | young_intake_trace | 19 | leiser / weicher aufnehmen | 0.0675 | 0.2969 | 0.4909 | 0.1708 | 0.1571 | 0.3279 |
| ausgeglichen | inner_effect_stable | young_intake_trace | 16 | ruhig hinhoeren | 0.2144 | 0.2124 | 0.1857 | 0.2030 | 0.1009 | 0.2233 |
| feldinput | inner_effect_stable | contact_loaded_intake | 15 | Druck / Feldkontakt entlasten | 0.1029 | 0.3007 | 0.2477 | 0.1660 | 0.3643 | 0.0626 |
| sehen_fokus | inner_effect_stable | young_intake_trace | 13 | Sehen schaerfen | 0.4246 | 0.1941 | 0.1681 | 0.5953 | 0.0923 | 0.1369 |
| feldinput | inner_effect_carried_unrest | contact_loaded_intake | 12 | Druck / Feldkontakt entlasten | 0.0842 | 0.3645 | 0.2982 | 0.1444 | 0.4071 | 0.0388 |
| feldinput | inner_effect_stable | contact_loaded_intake | 12 | Druck / Feldkontakt entlasten | 0.1069 | 0.3118 | 0.2521 | 0.1712 | 0.3766 | 0.0683 |
| fuehlen_abstand | inner_effect_carried_unrest | young_intake_trace | 12 | Abstand bilden | 0.0978 | 0.5124 | 0.2560 | 0.1604 | 0.3459 | 0.0564 |
| sehen_fokus | inner_effect_stable | young_intake_trace | 11 | Sehen schaerfen | 0.4044 | 0.2178 | 0.1903 | 0.5718 | 0.1019 | 0.1110 |

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
