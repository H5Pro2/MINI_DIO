# Aktuelle Rezeptorschicht - Stress/Quiet Feldphasen 1h

## Grundfrage

Liegt `offene_variante` zeitlich vor `spannungsrand_kippnaehe`, oder sind beide Rollen unabhaengige Feldantworten?

## Weltuebersicht

| Welt | Segmente | Randsegmente | Rand nach Offen | Quote | Durchschnitt Offen-Dauer vor Rand |
|---|---:|---:|---:|---:|---:|
| SOL_QUIET_1H | 1950 | 76 | 65 | 0.8553 | 2.3538 |
| SOL_STRESS_1H | 2013 | 85 | 76 | 0.8941 | 1.7368 |
| BTC_QUIET_1H | 1847 | 70 | 56 | 0.8000 | 1.9286 |
| BTC_STRESS_1H | 1866 | 82 | 65 | 0.7927 | 2.4923 |

## Wichtigste Uebergaenge

### SOL_QUIET_1H
- `offene_variante->zentrum_stabil`: `455`
- `zentrum_stabil->offene_variante`: `445`
- `rekopplungsnaehe->zentrum_stabil`: `260`
- `zentrum_stabil->rekopplungsnaehe`: `237`
- `offene_variante->rekopplungsnaehe`: `216`
- `rekopplungsnaehe->offene_variante`: `184`
- `spannungsrand_kippnaehe->offene_variante`: `64`
- `zentrum_stabil->spannungsrand_kippnaehe`: `35`

### SOL_STRESS_1H
- `zentrum_stabil->offene_variante`: `464`
- `offene_variante->zentrum_stabil`: `443`
- `rekopplungsnaehe->zentrum_stabil`: `288`
- `offene_variante->rekopplungsnaehe`: `241`
- `zentrum_stabil->rekopplungsnaehe`: `228`
- `rekopplungsnaehe->offene_variante`: `178`
- `spannungsrand_kippnaehe->offene_variante`: `75`
- `zentrum_stabil->spannungsrand_kippnaehe`: `42`

### BTC_QUIET_1H
- `zentrum_stabil->offene_variante`: `464`
- `offene_variante->zentrum_stabil`: `449`
- `rekopplungsnaehe->zentrum_stabil`: `253`
- `zentrum_stabil->rekopplungsnaehe`: `208`
- `offene_variante->rekopplungsnaehe`: `193`
- `rekopplungsnaehe->offene_variante`: `139`
- `spannungsrand_kippnaehe->offene_variante`: `57`
- `zentrum_stabil->spannungsrand_kippnaehe`: `39`

### BTC_STRESS_1H
- `zentrum_stabil->offene_variante`: `437`
- `offene_variante->zentrum_stabil`: `436`
- `rekopplungsnaehe->zentrum_stabil`: `245`
- `zentrum_stabil->rekopplungsnaehe`: `214`
- `offene_variante->rekopplungsnaehe`: `204`
- `rekopplungsnaehe->offene_variante`: `165`
- `spannungsrand_kippnaehe->offene_variante`: `68`
- `zentrum_stabil->spannungsrand_kippnaehe`: `37`

## Befund

- Direkte Uebergaenge `offene_variante -> spannungsrand_kippnaehe`: `105`
- Direkte Uebergaenge `spannungsrand_kippnaehe -> offene_variante`: `264`

Eine hohe Quote `Rand nach Offen` spricht fuer eine Feldphase: Offenheit kann als Vorraum vor Rand/Kipp auftreten.
Viele Rueckuebergaenge Rand/Kipp -> Offen sprechen dagegen fuer eine Pendelbewegung an der Rekopplungsgrenze.

## Ableitung

Wenn Rand/Kipp haeufig nach Offenheit kommt, ist Offenheit kein neutraler Zustand. Sie ist dann eine Vorphase, in der das Feld noch Uebergang halten kann.

Wenn Rand/Kipp ohne vorherige Offenheit kommt, entsteht die Randnaehe direkter aus Rohaufnahme, Lautheit und schwacher Rekopplung.
