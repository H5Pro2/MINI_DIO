# Befund 1221 - Feldphasen-Matrix synthetische Extremwelten

## Grundfrage

Liegt `offene_variante` zeitlich vor `spannungsrand_kippnaehe`, oder sind beide Rollen unabhaengige Feldantworten?

## Weltuebersicht

| Welt | Segmente | Randsegmente | Rand nach Offen | Quote | Durchschnitt Offen-Dauer vor Rand |
|---|---:|---:|---:|---:|---:|
| HARMONIE | 117 | 3 | 2 | 0.6667 | 1.0000 |
| RAND_DOMINANZ | 679 | 28 | 25 | 0.8929 | 3.2400 |
| BRUCH_RAND | 640 | 7 | 3 | 0.4286 | 1.0000 |
| SEQ_ORIGINAL | 635 | 7 | 3 | 0.4286 | 1.0000 |
| SEQ_PERMUTIERT | 548 | 7 | 2 | 0.2857 | 1.0000 |
| SEQ_STARK_PERMUTIERT | 509 | 9 | 5 | 0.5556 | 2.0000 |
| SEQ_ZUFALLSNAH | 610 | 8 | 4 | 0.5000 | 1.5000 |
| ZEIT_KOMPAKT | 421 | 6 | 3 | 0.5000 | 1.3333 |
| ZEIT_GEDEHNT | 1010 | 8 | 5 | 0.6250 | 1.8000 |
| HARMONIE_KOMPAKT | 124 | 3 | 1 | 0.3333 | 1.0000 |
| HARMONIE_GEDEHNT | 117 | 2 | 1 | 0.5000 | 4.0000 |
| RAND_KOMPAKT | 469 | 20 | 16 | 0.8000 | 3.5000 |
| RAND_GEDEHNT | 1157 | 50 | 47 | 0.9400 | 3.5532 |

## Wichtigste Uebergaenge

### HARMONIE
- `rekopplungsnaehe->zentrum_stabil`: `36`
- `zentrum_stabil->offene_variante`: `24`
- `offene_variante->rekopplungsnaehe`: `20`
- `zentrum_stabil->rekopplungsnaehe`: `18`
- `offene_variante->zentrum_stabil`: `10`
- `zentrum_stabil->spannungsrand_kippnaehe`: `3`
- `spannungsrand_kippnaehe->offene_variante`: `3`
- `rekopplungsnaehe->offene_variante`: `2`

### RAND_DOMINANZ
- `rekopplungsnaehe->zentrum_stabil`: `132`
- `offene_variante->rekopplungsnaehe`: `129`
- `zentrum_stabil->offene_variante`: `109`
- `zentrum_stabil->rekopplungsnaehe`: `90`
- `offene_variante->zentrum_stabil`: `82`
- `rekopplungsnaehe->offene_variante`: `80`
- `spannungsrand_kippnaehe->offene_variante`: `28`
- `zentrum_stabil->spannungsrand_kippnaehe`: `14`

### BRUCH_RAND
- `zentrum_stabil->offene_variante`: `131`
- `offene_variante->zentrum_stabil`: `118`
- `offene_variante->rekopplungsnaehe`: `110`
- `rekopplungsnaehe->zentrum_stabil`: `97`
- `rekopplungsnaehe->offene_variante`: `91`
- `zentrum_stabil->rekopplungsnaehe`: `78`
- `zentrum_stabil->spannungsrand_kippnaehe`: `6`
- `spannungsrand_kippnaehe->offene_variante`: `6`

### SEQ_ORIGINAL
- `zentrum_stabil->offene_variante`: `130`
- `offene_variante->zentrum_stabil`: `118`
- `offene_variante->rekopplungsnaehe`: `107`
- `rekopplungsnaehe->zentrum_stabil`: `97`
- `rekopplungsnaehe->offene_variante`: `89`
- `zentrum_stabil->rekopplungsnaehe`: `79`
- `zentrum_stabil->spannungsrand_kippnaehe`: `6`
- `spannungsrand_kippnaehe->offene_variante`: `6`

### SEQ_PERMUTIERT
- `offene_variante->rekopplungsnaehe`: `108`
- `rekopplungsnaehe->offene_variante`: `105`
- `offene_variante->zentrum_stabil`: `90`
- `zentrum_stabil->offene_variante`: `85`
- `rekopplungsnaehe->zentrum_stabil`: `74`
- `zentrum_stabil->rekopplungsnaehe`: `71`
- `zentrum_stabil->spannungsrand_kippnaehe`: `7`
- `spannungsrand_kippnaehe->offene_variante`: `7`

### SEQ_STARK_PERMUTIERT
- `offene_variante->rekopplungsnaehe`: `106`
- `rekopplungsnaehe->offene_variante`: `105`
- `offene_variante->zentrum_stabil`: `77`
- `zentrum_stabil->offene_variante`: `69`
- `rekopplungsnaehe->zentrum_stabil`: `67`
- `zentrum_stabil->rekopplungsnaehe`: `66`
- `spannungsrand_kippnaehe->offene_variante`: `9`
- `zentrum_stabil->spannungsrand_kippnaehe`: `8`

### SEQ_ZUFALLSNAH
- `zentrum_stabil->offene_variante`: `125`
- `offene_variante->zentrum_stabil`: `112`
- `offene_variante->rekopplungsnaehe`: `101`
- `rekopplungsnaehe->zentrum_stabil`: `97`
- `rekopplungsnaehe->offene_variante`: `81`
- `zentrum_stabil->rekopplungsnaehe`: `77`
- `zentrum_stabil->spannungsrand_kippnaehe`: `7`
- `spannungsrand_kippnaehe->offene_variante`: `7`

### ZEIT_KOMPAKT
- `zentrum_stabil->offene_variante`: `83`
- `offene_variante->zentrum_stabil`: `75`
- `rekopplungsnaehe->zentrum_stabil`: `74`
- `offene_variante->rekopplungsnaehe`: `66`
- `zentrum_stabil->rekopplungsnaehe`: `59`
- `rekopplungsnaehe->offene_variante`: `51`
- `zentrum_stabil->spannungsrand_kippnaehe`: `6`
- `spannungsrand_kippnaehe->offene_variante`: `6`

### ZEIT_GEDEHNT
- `zentrum_stabil->offene_variante`: `203`
- `rekopplungsnaehe->zentrum_stabil`: `184`
- `offene_variante->zentrum_stabil`: `184`
- `zentrum_stabil->rekopplungsnaehe`: `157`
- `offene_variante->rekopplungsnaehe`: `146`
- `rekopplungsnaehe->offene_variante`: `119`
- `zentrum_stabil->spannungsrand_kippnaehe`: `8`
- `spannungsrand_kippnaehe->offene_variante`: `7`

### HARMONIE_KOMPAKT
- `rekopplungsnaehe->zentrum_stabil`: `35`
- `zentrum_stabil->offene_variante`: `23`
- `offene_variante->rekopplungsnaehe`: `21`
- `zentrum_stabil->rekopplungsnaehe`: `20`
- `offene_variante->zentrum_stabil`: `12`
- `rekopplungsnaehe->offene_variante`: `6`
- `zentrum_stabil->spannungsrand_kippnaehe`: `3`
- `spannungsrand_kippnaehe->offene_variante`: `3`

### HARMONIE_GEDEHNT
- `rekopplungsnaehe->zentrum_stabil`: `36`
- `zentrum_stabil->offene_variante`: `26`
- `zentrum_stabil->rekopplungsnaehe`: `19`
- `offene_variante->rekopplungsnaehe`: `18`
- `offene_variante->zentrum_stabil`: `12`
- `zentrum_stabil->spannungsrand_kippnaehe`: `2`
- `spannungsrand_kippnaehe->offene_variante`: `2`
- `rekopplungsnaehe->offene_variante`: `1`

### RAND_KOMPAKT
- `rekopplungsnaehe->zentrum_stabil`: `94`
- `zentrum_stabil->rekopplungsnaehe`: `79`
- `zentrum_stabil->offene_variante`: `74`
- `offene_variante->zentrum_stabil`: `68`
- `offene_variante->rekopplungsnaehe`: `66`
- `rekopplungsnaehe->offene_variante`: `47`
- `spannungsrand_kippnaehe->offene_variante`: `20`
- `zentrum_stabil->spannungsrand_kippnaehe`: `8`

### RAND_GEDEHNT
- `offene_variante->rekopplungsnaehe`: `256`
- `zentrum_stabil->offene_variante`: `199`
- `rekopplungsnaehe->zentrum_stabil`: `194`
- `rekopplungsnaehe->offene_variante`: `162`
- `offene_variante->zentrum_stabil`: `140`
- `zentrum_stabil->rekopplungsnaehe`: `105`
- `spannungsrand_kippnaehe->offene_variante`: `45`
- `zentrum_stabil->spannungsrand_kippnaehe`: `31`

## Befund

- Direkte Uebergaenge `offene_variante -> spannungsrand_kippnaehe`: `30`
- Direkte Uebergaenge `spannungsrand_kippnaehe -> offene_variante`: `149`

Eine hohe Quote `Rand nach Offen` spricht fuer eine Feldphase: Offenheit kann als Vorraum vor Rand/Kipp auftreten.
Viele Rueckuebergaenge Rand/Kipp -> Offen sprechen dagegen fuer eine Pendelbewegung an der Rekopplungsgrenze.

## Ableitung

Wenn Rand/Kipp haeufig nach Offenheit kommt, ist Offenheit kein neutraler Zustand. Sie ist dann eine Vorphase, in der das Feld noch Uebergang halten kann.

Wenn Rand/Kipp ohne vorherige Offenheit kommt, entsteht die Randnaehe direkter aus Rohaufnahme, Lautheit und schwacher Rekopplung.

Wie es weitergeht: Die naechste Pruefung sollte die direkten `Offen -> Rand` und `Rand -> Offen` Segmente als kleine Zeitfenster plotten.
