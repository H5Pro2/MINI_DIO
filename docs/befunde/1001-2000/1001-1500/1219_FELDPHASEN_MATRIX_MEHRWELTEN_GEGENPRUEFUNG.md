# Befund 1219 - Feldphasen-Matrix Mehrwelten-Gegenpruefung

## Grundfrage

Liegt `offene_variante` zeitlich vor `spannungsrand_kippnaehe`, oder sind beide Rollen unabhaengige Feldantworten?

## Weltuebersicht

| Welt | Segmente | Randsegmente | Rand nach Offen | Quote | Durchschnitt Offen-Dauer vor Rand |
|---|---:|---:|---:|---:|---:|
| SOL_5M_2K | 1110 | 34 | 30 | 0.8824 | 2.5000 |
| BTC_5M_2K | 1019 | 34 | 31 | 0.9118 | 2.2581 |
| KAS_5M_2K | 1086 | 37 | 34 | 0.9189 | 2.0882 |
| PAXG_5M_10K | 4476 | 87 | 67 | 0.7701 | 1.4627 |
| DOGE_5M_10K | 4369 | 139 | 115 | 0.8273 | 1.9478 |
| XRP_5M_10K | 4270 | 162 | 122 | 0.7531 | 1.8443 |
| SOL_1H_2K | 1060 | 45 | 38 | 0.8444 | 1.9737 |
| BTC_1H_2K | 990 | 46 | 38 | 0.8261 | 1.9737 |
| NEG_STRESS_10K | 4302 | 152 | 128 | 0.8421 | 1.9219 |
| POS_EXPANSION_10K | 4581 | 157 | 130 | 0.8280 | 1.7154 |
| SIDEWAYS_10K | 4619 | 128 | 100 | 0.7812 | 1.8000 |

## Wichtigste Uebergaenge

### SOL_5M_2K
- `offene_variante->zentrum_stabil`: `275`
- `zentrum_stabil->offene_variante`: `274`
- `offene_variante->rekopplungsnaehe`: `135`
- `rekopplungsnaehe->offene_variante`: `124`
- `rekopplungsnaehe->zentrum_stabil`: `121`
- `zentrum_stabil->rekopplungsnaehe`: `112`
- `spannungsrand_kippnaehe->offene_variante`: `30`
- `offene_variante->spannungsrand_kippnaehe`: `19`

### BTC_5M_2K
- `offene_variante->zentrum_stabil`: `253`
- `zentrum_stabil->offene_variante`: `251`
- `offene_variante->rekopplungsnaehe`: `124`
- `rekopplungsnaehe->offene_variante`: `113`
- `rekopplungsnaehe->zentrum_stabil`: `109`
- `zentrum_stabil->rekopplungsnaehe`: `100`
- `spannungsrand_kippnaehe->offene_variante`: `30`
- `offene_variante->spannungsrand_kippnaehe`: `18`

### KAS_5M_2K
- `offene_variante->zentrum_stabil`: `249`
- `zentrum_stabil->offene_variante`: `248`
- `offene_variante->rekopplungsnaehe`: `151`
- `rekopplungsnaehe->offene_variante`: `138`
- `rekopplungsnaehe->zentrum_stabil`: `118`
- `zentrum_stabil->rekopplungsnaehe`: `107`
- `spannungsrand_kippnaehe->offene_variante`: `34`
- `offene_variante->spannungsrand_kippnaehe`: `20`

### PAXG_5M_10K
- `zentrum_stabil->offene_variante`: `1050`
- `offene_variante->zentrum_stabil`: `1004`
- `rekopplungsnaehe->zentrum_stabil`: `823`
- `zentrum_stabil->rekopplungsnaehe`: `734`
- `offene_variante->rekopplungsnaehe`: `388`
- `rekopplungsnaehe->offene_variante`: `302`
- `spannungsrand_kippnaehe->offene_variante`: `62`
- `zentrum_stabil->spannungsrand_kippnaehe`: `56`

### DOGE_5M_10K
- `zentrum_stabil->offene_variante`: `1072`
- `offene_variante->zentrum_stabil`: `1035`
- `rekopplungsnaehe->zentrum_stabil`: `693`
- `zentrum_stabil->rekopplungsnaehe`: `596`
- `offene_variante->rekopplungsnaehe`: `394`
- `rekopplungsnaehe->offene_variante`: `300`
- `spannungsrand_kippnaehe->offene_variante`: `109`
- `zentrum_stabil->spannungsrand_kippnaehe`: `73`

### XRP_5M_10K
- `zentrum_stabil->offene_variante`: `1041`
- `offene_variante->zentrum_stabil`: `1025`
- `rekopplungsnaehe->zentrum_stabil`: `670`
- `zentrum_stabil->rekopplungsnaehe`: `573`
- `offene_variante->rekopplungsnaehe`: `370`
- `rekopplungsnaehe->offene_variante`: `266`
- `spannungsrand_kippnaehe->offene_variante`: `126`
- `zentrum_stabil->spannungsrand_kippnaehe`: `100`

### SOL_1H_2K
- `zentrum_stabil->offene_variante`: `233`
- `offene_variante->zentrum_stabil`: `229`
- `offene_variante->rekopplungsnaehe`: `145`
- `rekopplungsnaehe->zentrum_stabil`: `129`
- `rekopplungsnaehe->offene_variante`: `123`
- `zentrum_stabil->rekopplungsnaehe`: `110`
- `spannungsrand_kippnaehe->offene_variante`: `40`
- `offene_variante->spannungsrand_kippnaehe`: `23`

### BTC_1H_2K
- `offene_variante->zentrum_stabil`: `245`
- `zentrum_stabil->offene_variante`: `215`
- `zentrum_stabil->rekopplungsnaehe`: `125`
- `rekopplungsnaehe->zentrum_stabil`: `115`
- `rekopplungsnaehe->offene_variante`: `103`
- `offene_variante->rekopplungsnaehe`: `94`
- `spannungsrand_kippnaehe->offene_variante`: `39`
- `zentrum_stabil->spannungsrand_kippnaehe`: `22`

### NEG_STRESS_10K
- `offene_variante->zentrum_stabil`: `1048`
- `zentrum_stabil->offene_variante`: `1042`
- `rekopplungsnaehe->zentrum_stabil`: `647`
- `zentrum_stabil->rekopplungsnaehe`: `573`
- `offene_variante->rekopplungsnaehe`: `374`
- `rekopplungsnaehe->offene_variante`: `313`
- `spannungsrand_kippnaehe->offene_variante`: `114`
- `zentrum_stabil->spannungsrand_kippnaehe`: `95`

### POS_EXPANSION_10K
- `zentrum_stabil->offene_variante`: `1123`
- `offene_variante->zentrum_stabil`: `1091`
- `rekopplungsnaehe->zentrum_stabil`: `728`
- `zentrum_stabil->rekopplungsnaehe`: `617`
- `offene_variante->rekopplungsnaehe`: `411`
- `rekopplungsnaehe->offene_variante`: `296`
- `spannungsrand_kippnaehe->offene_variante`: `131`
- `zentrum_stabil->spannungsrand_kippnaehe`: `89`

### SIDEWAYS_10K
- `zentrum_stabil->offene_variante`: `1104`
- `offene_variante->zentrum_stabil`: `1061`
- `rekopplungsnaehe->zentrum_stabil`: `753`
- `zentrum_stabil->rekopplungsnaehe`: `648`
- `offene_variante->rekopplungsnaehe`: `449`
- `rekopplungsnaehe->offene_variante`: `347`
- `spannungsrand_kippnaehe->offene_variante`: `102`
- `zentrum_stabil->spannungsrand_kippnaehe`: `68`

## Befund

- Direkte Uebergaenge `offene_variante -> spannungsrand_kippnaehe`: `355`
- Direkte Uebergaenge `spannungsrand_kippnaehe -> offene_variante`: `817`

Eine hohe Quote `Rand nach Offen` spricht fuer eine Feldphase: Offenheit kann als Vorraum vor Rand/Kipp auftreten.
Viele Rueckuebergaenge Rand/Kipp -> Offen sprechen dagegen fuer eine Pendelbewegung an der Rekopplungsgrenze.

## Ableitung

Wenn Rand/Kipp haeufig nach Offenheit kommt, ist Offenheit kein neutraler Zustand. Sie ist dann eine Vorphase, in der das Feld noch Uebergang halten kann.

Wenn Rand/Kipp ohne vorherige Offenheit kommt, entsteht die Randnaehe direkter aus Rohaufnahme, Lautheit und schwacher Rekopplung.

Wie es weitergeht: Die naechste Pruefung sollte die direkten `Offen -> Rand` und `Rand -> Offen` Segmente als kleine Zeitfenster plotten.
