# Synthetische Sinnesachsen-Stress Feldphasen

## Grundfrage

Liegt `offene_variante` zeitlich vor `spannungsrand_kippnaehe`, oder sind beide Rollen unabhaengige Feldantworten?

## Weltuebersicht

| Welt | Segmente | Randsegmente | Rand nach Offen | Quote | Durchschnitt Offen-Dauer vor Rand |
|---|---:|---:|---:|---:|---:|
| SYNTH_DESYNC_AXES | 655 | 146 | 28 | 0.1918 | 1.3214 |
| SYNTH_RAND_KIPP | 1257 | 21 | 19 | 0.9048 | 2.0526 |
| SYNTH_VISUAL_CHAOTIC_HEARING_STABLE | 34 | 0 | 0 | 0.0000 | 0.0000 |
| SYNTH_VISUAL_STABLE_HEARING_CHAOTIC | 787 | 224 | 136 | 0.6071 | 1.0588 |

## Wichtigste Uebergaenge

### SYNTH_DESYNC_AXES
- `zentrum_stabil->spannungsrand_kippnaehe`: `135`
- `rekopplungsnaehe->zentrum_stabil`: `118`
- `spannungsrand_kippnaehe->zentrum_stabil`: `106`
- `zentrum_stabil->rekopplungsnaehe`: `77`
- `zentrum_stabil->offene_variante`: `61`
- `offene_variante->zentrum_stabil`: `50`
- `offene_variante->rekopplungsnaehe`: `44`
- `spannungsrand_kippnaehe->offene_variante`: `25`

### SYNTH_RAND_KIPP
- `offene_variante->rekopplungsnaehe`: `270`
- `zentrum_stabil->offene_variante`: `259`
- `rekopplungsnaehe->zentrum_stabil`: `249`
- `offene_variante->zentrum_stabil`: `158`
- `rekopplungsnaehe->offene_variante`: `149`
- `zentrum_stabil->rekopplungsnaehe`: `129`
- `zentrum_stabil->spannungsrand_kippnaehe`: `19`
- `spannungsrand_kippnaehe->offene_variante`: `19`

### SYNTH_VISUAL_CHAOTIC_HEARING_STABLE
- `rekopplungsnaehe->zentrum_stabil`: `10`
- `zentrum_stabil->offene_variante`: `10`
- `offene_variante->rekopplungsnaehe`: `8`
- `offene_variante->zentrum_stabil`: `3`
- `zentrum_stabil->rekopplungsnaehe`: `2`

### SYNTH_VISUAL_STABLE_HEARING_CHAOTIC
- `zentrum_stabil->spannungsrand_kippnaehe`: `222`
- `spannungsrand_kippnaehe->zentrum_stabil`: `181`
- `offene_variante->zentrum_stabil`: `143`
- `zentrum_stabil->offene_variante`: `128`
- `rekopplungsnaehe->zentrum_stabil`: `38`
- `spannungsrand_kippnaehe->rekopplungsnaehe`: `24`
- `spannungsrand_kippnaehe->offene_variante`: `19`
- `offene_variante->rekopplungsnaehe`: `11`

## Befund

- Direkte Uebergaenge `offene_variante -> spannungsrand_kippnaehe`: `6`
- Direkte Uebergaenge `spannungsrand_kippnaehe -> offene_variante`: `63`

Eine hohe Quote `Rand nach Offen` spricht fuer eine Feldphase: Offenheit kann als Vorraum vor Rand/Kipp auftreten.
Viele Rueckuebergaenge Rand/Kipp -> Offen sprechen dagegen fuer eine Pendelbewegung an der Rekopplungsgrenze.

## Ableitung

Wenn Rand/Kipp haeufig nach Offenheit kommt, ist Offenheit kein neutraler Zustand. Sie ist dann eine Vorphase, in der das Feld noch Uebergang halten kann.

Wenn Rand/Kipp ohne vorherige Offenheit kommt, entsteht die Randnaehe direkter aus Rohaufnahme, Lautheit und schwacher Rekopplung.

Wie es weitergeht: Die naechste Pruefung sollte die direkten `Offen -> Rand` und `Rand -> Offen` Segmente als kleine Zeitfenster plotten.
