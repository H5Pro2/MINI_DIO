# 1044 - PAXG: Lupe auf `dio_14wj` als ruhige Traegerfamilie

## Zweck

Nach dem Gleichgruppenvergleich wurde `dio_14wj` isoliert.

Die Frage war:

```text
Ist `dio_14wj` nur eine Oberflaechenvariante von `dio_104t`,
oder traegt es in PAXG-5m eine eigene ruhige Rekopplungsrolle?
```

## Datengrundlage

Geprueft wurden:

- `PAXG2024_5M_10K`
- `PAXG2025_5M_10K`

Erzeugte Messdateien:

- `1044_PAXG_DIO14WJ_TRAEGERFAMILIE_LUPE.csv`
- `1044_PAXG_DIO14WJ_TRAEGERFAMILIE_UEBERGAENGE.csv`

Verglichen wurden die Familien:

- `dio_104t`
- `dio_14wj`

## Befund 1: Beide Familien liegen stabil, aber `dio_14wj` ist ruhiger

| Welt | Familie | Anzahl | Anteil | Rekopplung | Carry | Strain | Sinnes-MCM-Kopplung |
|---|---:|---:|---:|---:|---:|---:|---:|
| PAXG2024_5M_10K | `dio_104t` | 732 | 0.073244 | 0.730013 | 0.572476 | 0.149251 | 0.856988 |
| PAXG2024_5M_10K | `dio_14wj` | 530 | 0.053032 | 0.743973 | 0.582428 | 0.130787 | 0.874362 |
| PAXG2025_5M_10K | `dio_104t` | 860 | 0.086052 | 0.730299 | 0.575202 | 0.148628 | 0.857558 |
| PAXG2025_5M_10K | `dio_14wj` | 708 | 0.070843 | 0.743199 | 0.586935 | 0.131257 | 0.873902 |

Lesung:

`dio_14wj` ist in beiden PAXG-5m-Jahren stabiler im Sinne der inneren Feldqualitaet:

- mehr Rekopplung,
- mehr Carry,
- weniger Strain,
- staerkere Sinnes-MCM-Kopplung.

Das spricht gegen reine Oberflaechenvariante.

## Befund 2: `dio_14wj` traegt weniger Hoer- und Kontaktlast

| Welt | Familie | Hoer-Feld-Gap | Felt Pressure | adaptierter Feld-Input | Kontaktspannung |
|---|---:|---:|---:|---:|---:|
| PAXG2024_5M_10K | `dio_104t` | 0.044970 | 0.082173 | 0.075501 | 0.085971 |
| PAXG2024_5M_10K | `dio_14wj` | 0.010099 | 0.055095 | 0.034708 | 0.038828 |
| PAXG2025_5M_10K | `dio_104t` | 0.043262 | 0.080146 | 0.072791 | 0.082728 |
| PAXG2025_5M_10K | `dio_14wj` | 0.009458 | 0.054435 | 0.033377 | 0.037322 |

Lesung:

`dio_14wj` wirkt wie eine ruhigere Aufnahmeform:

- der Hoer-Feld-Gap ist deutlich niedriger,
- der gefuehlte Druck ist niedriger,
- die Feldaufnahme ist gedämpfter,
- die Kontaktspannung ist niedriger.

Damit ist `dio_14wj` nicht nur stabil, sondern reizärmer und rekoppelnder.

## Befund 3: `dio_14wj` bleibt in sich selbst stabil

Der haeufigste Uebergang mit `dio_14wj` ist:

| Uebergang | Effektpfad | Anzahl | Rekopplung-Delta | Strain-Delta | Carry-Delta |
|---|---|---:|---:|---:|---:|
| `dio_14wj -> dio_14wj` | stabil -> stabil | 294 | 0.001955 | -0.000695 | 0.002345 |

Lesung:

`dio_14wj` kann sich selbst ueber mehrere Ticks tragen.

Das ist wichtig: Die Familie erscheint nicht nur punktuell, sondern bildet eine eigene gehaltene Phase.

## Befund 4: `dio_104t -> dio_14wj` wirkt wie Beruhigungsuebergang

| Uebergang | Effektpfad | Anzahl | Rekopplung-Delta | Strain-Delta | Carry-Delta |
|---|---|---:|---:|---:|---:|
| `dio_104t -> dio_14wj` | stabil -> stabil | 150 | 0.010616 | -0.016744 | 0.011940 |
| `dio_14wj -> dio_104t` | stabil -> stabil | 69 | -0.011767 | 0.012854 | -0.011314 |

Lesung:

Der Weg von `dio_104t` nach `dio_14wj` verbessert im Mittel:

- Rekopplung steigt,
- Strain sinkt,
- Carry steigt.

Der Rueckweg von `dio_14wj` nach `dio_104t` zeigt die Gegenbewegung:

- Rekopplung sinkt,
- Strain steigt,
- Carry sinkt.

Das ist ein starkes Indiz, dass `dio_14wj` im PAXG-5m-Feld eine eigenstaendige Beruhigungs-/Rekopplungsrolle traegt.

## Schlussfolgerung

`dio_14wj` ist nach dieser Lupe keine beliebige Oberflaechenvariante von `dio_104t`.

Praeziser:

```text
`dio_104t` wirkt wie die breite PAXG-Grundfamilie.
`dio_14wj` wirkt wie eine ruhigere PAXG-5m-Rekopplungsfamilie.
```

Damit wird die bisherige PAXG-Lesung geschaerft:

```text
PAXG = gleiche Grundtopologie
PAXG-5m = ruhigere zweite Traegerfamilie
`dio_14wj` = moeglicher rekoppelnder Ruhetraeger
```

## Bedeutung fuer MINI_DIO

MINI_DIO bildet nicht nur eine globale Topfamilie.

Das Feld unterscheidet innerhalb derselben Topologie verschiedene Rollen:

- breite Grundfamilie,
- ruhige Traegerfamilie,
- Uebergangsfamilien,
- unruhigere Kontaktzonen.

Das ist fuer die weitere Forschung wichtig, weil Bedeutung nicht nur als einzelnes Symbol gelesen werden darf.

Eine Familie kann eine Rolle tragen.

Eine Rolle kann sich erst im Uebergang zeigen.

## Wie es weitergeht

Als naechstes sollte `dio_14wj` gegen PAXG-1h geprueft werden. Ziel: Klaeren, ob `dio_14wj` eine echte PAXG-5m-Rolle ist oder ob sie bei anderer Zeitauflösung in `dio_155c` beziehungsweise eine andere ruhigere Traegerfamilie uebergeht.
