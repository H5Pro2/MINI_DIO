# Befund 1215 - Reale Rollen-Phasenuebergaenge

## Grundfrage

Liegt `offene_variante` zeitlich vor `spannungsrand_kippnaehe`, oder sind beide Rollen unabhaengige Feldantworten?

## Weltuebersicht

| Welt | Segmente | Randsegmente | Rand nach Offen | Quote | Durchschnitt Offen-Dauer vor Rand |
|---|---:|---:|---:|---:|---:|
| SOL_2024_5M | 1110 | 34 | 30 | 0.8824 | 2.5000 |
| BTC_2024_5M | 1019 | 34 | 31 | 0.9118 | 2.2581 |
| KAS_2024_5M | 1084 | 37 | 34 | 0.9189 | 2.0882 |
| PAXG_2024_5M | 1094 | 32 | 25 | 0.7812 | 1.4800 |

## Wichtigste Uebergaenge

### SOL_2024_5M
- `offene_variante->zentrum_stabil`: `275`
- `zentrum_stabil->offene_variante`: `274`
- `offene_variante->rekopplungsnaehe`: `135`
- `rekopplungsnaehe->offene_variante`: `124`
- `rekopplungsnaehe->zentrum_stabil`: `121`
- `zentrum_stabil->rekopplungsnaehe`: `112`
- `spannungsrand_kippnaehe->offene_variante`: `30`
- `offene_variante->spannungsrand_kippnaehe`: `19`

### BTC_2024_5M
- `offene_variante->zentrum_stabil`: `253`
- `zentrum_stabil->offene_variante`: `251`
- `offene_variante->rekopplungsnaehe`: `124`
- `rekopplungsnaehe->offene_variante`: `113`
- `rekopplungsnaehe->zentrum_stabil`: `109`
- `zentrum_stabil->rekopplungsnaehe`: `100`
- `spannungsrand_kippnaehe->offene_variante`: `30`
- `offene_variante->spannungsrand_kippnaehe`: `18`

### KAS_2024_5M
- `offene_variante->zentrum_stabil`: `249`
- `zentrum_stabil->offene_variante`: `248`
- `offene_variante->rekopplungsnaehe`: `150`
- `rekopplungsnaehe->offene_variante`: `137`
- `rekopplungsnaehe->zentrum_stabil`: `118`
- `zentrum_stabil->rekopplungsnaehe`: `107`
- `spannungsrand_kippnaehe->offene_variante`: `34`
- `offene_variante->spannungsrand_kippnaehe`: `20`

### PAXG_2024_5M
- `zentrum_stabil->offene_variante`: `224`
- `offene_variante->zentrum_stabil`: `224`
- `offene_variante->rekopplungsnaehe`: `154`
- `rekopplungsnaehe->zentrum_stabil`: `152`
- `zentrum_stabil->rekopplungsnaehe`: `138`
- `rekopplungsnaehe->offene_variante`: `137`
- `spannungsrand_kippnaehe->offene_variante`: `26`
- `zentrum_stabil->spannungsrand_kippnaehe`: `17`

## Befund

- Direkte Uebergaenge `offene_variante -> spannungsrand_kippnaehe`: `67`
- Direkte Uebergaenge `spannungsrand_kippnaehe -> offene_variante`: `120`

Eine hohe Quote `Rand nach Offen` spricht fuer eine Feldphase: Offenheit kann als Vorraum vor Rand/Kipp auftreten.
Viele Rueckuebergaenge Rand/Kipp -> Offen sprechen dagegen fuer eine Pendelbewegung an der Rekopplungsgrenze.

## Ableitung

Wenn Rand/Kipp haeufig nach Offenheit kommt, ist Offenheit kein neutraler Zustand. Sie ist dann eine Vorphase, in der das Feld noch Uebergang halten kann.

Wenn Rand/Kipp ohne vorherige Offenheit kommt, entsteht die Randnaehe direkter aus Rohaufnahme, Lautheit und schwacher Rekopplung.

Wie es weitergeht: Die naechste Pruefung sollte die direkten `Offen -> Rand` und `Rand -> Offen` Segmente als kleine Zeitfenster plotten.
