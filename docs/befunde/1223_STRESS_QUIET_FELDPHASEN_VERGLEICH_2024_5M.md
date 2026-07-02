# Stress Quiet Feldphasen Vergleich 2024 5m

## Grundfrage

Liegt `offene_variante` zeitlich vor `spannungsrand_kippnaehe`, oder sind beide Rollen unabhaengige Feldantworten?

## Weltuebersicht

| Welt | Segmente | Randsegmente | Rand nach Offen | Quote | Durchschnitt Offen-Dauer vor Rand |
|---|---:|---:|---:|---:|---:|
| SOL_QUIET_2024_5M | 434 | 201 | 201 | 1.0000 | 17.3035 |
| SOL_STRESS_2024_5M | 424 | 204 | 204 | 1.0000 | 17.5784 |
| BTC_QUIET_2024_5M | 437 | 196 | 196 | 1.0000 | 17.1071 |
| BTC_STRESS_2024_5M | 527 | 220 | 220 | 1.0000 | 13.4455 |

## Wichtigste Uebergaenge

### SOL_QUIET_2024_5M
- `spannungsrand_kippnaehe->offene_variante`: `201`
- `offene_variante->spannungsrand_kippnaehe`: `200`
- `offene_variante->rekopplungsnaehe`: `16`
- `rekopplungsnaehe->offene_variante`: `15`
- `rekopplungsnaehe->spannungsrand_kippnaehe`: `1`

### SOL_STRESS_2024_5M
- `spannungsrand_kippnaehe->offene_variante`: `204`
- `offene_variante->spannungsrand_kippnaehe`: `203`
- `offene_variante->rekopplungsnaehe`: `8`
- `rekopplungsnaehe->offene_variante`: `7`
- `rekopplungsnaehe->spannungsrand_kippnaehe`: `1`

### BTC_QUIET_2024_5M
- `spannungsrand_kippnaehe->offene_variante`: `196`
- `offene_variante->spannungsrand_kippnaehe`: `192`
- `offene_variante->rekopplungsnaehe`: `24`
- `rekopplungsnaehe->offene_variante`: `20`
- `rekopplungsnaehe->spannungsrand_kippnaehe`: `4`

### BTC_STRESS_2024_5M
- `spannungsrand_kippnaehe->offene_variante`: `220`
- `offene_variante->spannungsrand_kippnaehe`: `212`
- `offene_variante->rekopplungsnaehe`: `46`
- `rekopplungsnaehe->offene_variante`: `38`
- `rekopplungsnaehe->spannungsrand_kippnaehe`: `8`
- `offene_variante->zentrum_stabil`: `1`
- `zentrum_stabil->offene_variante`: `1`

## Befund

- Direkte Uebergaenge `offene_variante -> spannungsrand_kippnaehe`: `807`
- Direkte Uebergaenge `spannungsrand_kippnaehe -> offene_variante`: `821`

Eine hohe Quote `Rand nach Offen` spricht fuer eine Feldphase: Offenheit kann als Vorraum vor Rand/Kipp auftreten.
Viele Rueckuebergaenge Rand/Kipp -> Offen sprechen dagegen fuer eine Pendelbewegung an der Rekopplungsgrenze.

## Ableitung

Wenn Rand/Kipp haeufig nach Offenheit kommt, ist Offenheit kein neutraler Zustand. Sie ist dann eine Vorphase, in der das Feld noch Uebergang halten kann.

Wenn Rand/Kipp ohne vorherige Offenheit kommt, entsteht die Randnaehe direkter aus Rohaufnahme, Lautheit und schwacher Rekopplung.

Wie es weitergeht: Die naechste Pruefung sollte die direkten `Offen -> Rand` und `Rand -> Offen` Segmente als kleine Zeitfenster plotten.
