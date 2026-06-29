# Passive Rezeptor-Regulationskarte

## Zweck

Diese Datei verdichtet die Rohwelt-Ruecklesungen zu einer passiven Rezeptor-Regulationskarte.
Sie liest, welche Sinnesachsen eher Bindungsnaehe oder Fragmentierungsnaehe anzeigen.

## Sicherheitsgrenze

- passive Lesekarte
- keine Handlung
- kein Gate
- keine Strategie
- keine harte Regulation

## Karte

| Sinnesachse | Rezeptorachse | Metrik | Gruppe 1 Delta | Gruppe 2 Delta | Mittel | Leseklasse | Deutung |
|---|---|---|---:|---:|---:|---|---|
| `hoeren` | `tonale_energie` | `delta_energy_tone_vs_world` | 0.041169 | 0.065663 | 0.053416 | `fragmentierungsnaehe_stabil` | Achse liegt in beiden Gruppen klar hoeher vor Fragmentierung. |
| `sehen` | `formstabilitaet` | `delta_seen_stability_vs_world` | 0.005067 | 0.056655 | 0.030861 | `fragmentierungsnaehe_schwach` | Achse zeigt gleiche Richtung, aber mindestens eine Gruppe ist schwach. |
| `hoeren` | `lautheit` | `delta_loudness_vs_world` | 0.047788 | 0.002991 | 0.025389 | `fragmentierungsnaehe_schwach` | Achse zeigt gleiche Richtung, aber mindestens eine Gruppe ist schwach. |
| `hoeren` | `tonaler_wechsel` | `delta_energy_shift_abs_vs_world` | 0.03039 | -0.005326 | 0.012532 | `weltabhaengig_oder_widerspruechlich` | Achse kippt zwischen Weltgruppen oder ist nicht stabil trennend. |
| `rezeptor` | `feldaufnahme` | `delta_adapted_field_intake_vs_world` | 0.021916 | 0.001425 | 0.011671 | `fragmentierungsnaehe_schwach` | Achse zeigt gleiche Richtung, aber mindestens eine Gruppe ist schwach. |
| `mcm_feld` | `feldspannung` | `delta_mcm_tension_vs_world` | 0.021916 | 0.001425 | 0.011671 | `fragmentierungsnaehe_schwach` | Achse zeigt gleiche Richtung, aber mindestens eine Gruppe ist schwach. |
| `fuehlen` | `druck` | `delta_felt_pressure_vs_world` | 0.023754 | -0.000926 | 0.011414 | `weltabhaengig_oder_widerspruechlich` | Achse kippt zwischen Weltgruppen oder ist nicht stabil trennend. |
| `sehen` | `formwechsel` | `delta_seen_change_vs_world` | -0.011835 | 0.027526 | 0.007845 | `weltabhaengig_oder_widerspruechlich` | Achse kippt zwischen Weltgruppen oder ist nicht stabil trennend. |
| `sehen` | `schaerfe` | `delta_visual_sharpness_vs_world` | -0.028146 | 0.022933 | -0.002607 | `weltabhaengig_oder_widerspruechlich` | Achse kippt zwischen Weltgruppen oder ist nicht stabil trennend. |

## Befund

- Stabile Fragmentierungsnaehe: `tonale_energie`
- Schwache Fragmentierungsnaehe: `lautheit, formstabilitaet, feldaufnahme, feldspannung`
- Schwache Bindungsnaehe: `-`
- Weltabhaengig / nicht stabil: `tonaler_wechsel, formwechsel, schaerfe, druck`

## Arbeitsableitung

```text
Die bisher robusteste passive Regulationsachse liegt im Hoeren:
tonale Energie zeigt in beiden Weltgruppen Fragmentierungsnaehe.
Andere Achsen bleiben wichtig, aber kontextabhaengiger.
```

Das ist keine Steuerung.
Es ist eine Lesung darueber, welche Aufnahmeform das Feld spaeter eher bindet oder belastet.

## Wie es weitergeht

Als naechstes sollte diese Karte gegen weitere Sinnes-/Feldrollen gelegt werden.
Ziel: pruefen, ob tonale Energie wirklich als fruehe Fragmentierungsnaehe wirkt oder nur in den bisher geprueften Welten dominant war.