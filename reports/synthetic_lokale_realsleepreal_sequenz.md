# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 14:48:37

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\synthetic_lokale_realsleepreal_sequenz.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SYN_HARMONIE_FOLLOW_0_1000 | SYN_HARMONIE_SEQ | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7512 | 0.7512 | 0.0000 | 0.0000 | 0.7475 | 994 | 0 | 0 | 0 |
| SYN_HARMONIE_FOLLOW_1000_2000 | SYN_HARMONIE_SEQ | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7505 | 0.7505 | 0.0000 | 0.0000 | 0.7651 | 994 | 0 | 0 | 0 |
| SYN_HARMONIE_FOLLOW_2000_3000 | SYN_HARMONIE_SEQ | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7518 | 0.7518 | 0.0000 | 0.0000 | 0.7658 | 994 | 0 | 0 | 0 |
| SYN_HARMONIE_FOLLOW_3000_4000 | SYN_HARMONIE_SEQ | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7549 | 0.7549 | 0.0000 | 0.0000 | 0.7935 | 994 | 0 | 0 | 0 |
| SYN_BRUCH_RAND_FOLLOW_0_1000 | SYN_BRUCH_RAND_SEQ | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 0 | 0.7441 | 0.7672 | 0.0232 | 0.0611 | 0.6966 | 993 | 1 | 0 | 0 |
| SYN_BRUCH_RAND_FOLLOW_1000_2000 | SYN_BRUCH_RAND_SEQ | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7100 | 0.7100 | 0.0000 | 0.0000 | 0.3874 | 994 | 0 | 0 | 0 |
| SYN_BRUCH_RAND_FOLLOW_2000_3000 | SYN_BRUCH_RAND_SEQ | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7482 | 0.7482 | 0.0000 | 0.0000 | 0.7196 | 994 | 0 | 0 | 0 |
| SYN_BRUCH_RAND_FOLLOW_3000_4000 | SYN_BRUCH_RAND_SEQ | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 0 | 0.7518 | 0.7561 | 0.0042 | 0.0105 | 0.7670 | 993 | 1 | 0 | 0 |
| SYN_RAND_DOM_FOLLOW_0_1000 | SYN_RAND_DOM_SEQ | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7252 | 0.7252 | 0.0000 | 0.0000 | 0.5703 | 994 | 0 | 0 | 0 |
| SYN_RAND_DOM_FOLLOW_1000_2000 | SYN_RAND_DOM_SEQ | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7248 | 0.7248 | 0.0000 | 0.0000 | 0.4943 | 994 | 0 | 0 | 0 |
| SYN_RAND_DOM_FOLLOW_2000_3000 | SYN_RAND_DOM_SEQ | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 0 | 0.7448 | 0.7808 | 0.0360 | 0.0999 | 0.6946 | 993 | 1 | 0 | 0 |
| SYN_RAND_DOM_FOLLOW_3000_4000 | SYN_RAND_DOM_SEQ | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 0 | 0.7335 | 0.7571 | 0.0236 | 0.0658 | 0.6315 | 992 | 2 | 0 | 0 |

## Klassenverteilung

- `kompakt_nachhallend`: `8`
- `mittlere_uebergangsphase`: `4`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_und_gewichte_differenzieren`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0000 | 0.0360 | 0.0360 |
| Erfahrung | 0.0000 | 0.0999 | 0.0999 |
| Gewicht carry | 0.3034 | 0.4200 | 0.1166 |
| Gewicht alignment | 0.2215 | 0.2400 | 0.0185 |
| Gewicht strain_relief | 0.2000 | 0.2674 | 0.0674 |
| Gewicht sensory | 0.1400 | 0.2077 | 0.0677 |

## Befund

Der Report macht sichtbar, ob eine Weltphase kompakt gebunden, verteilt offen, verteilt rekoppelnd, nachhallend kompakt oder rand-/kippnah wirkt.

Wichtig ist die gemeinsame Lesung:

```text
Rollenbreite allein reicht nicht.
Nachhall allein reicht nicht.
Topologie allein reicht nicht.
Erst die gemeinsame Achsenlage beschreibt das Feldmilieu.
```

Die adaptive Rekopplung wird als passive Zusatzlesung ausgewiesen. Sie zeigt, ob Erfahrung die Rueckfuehrung gegenueber der statischen Referenz anhebt, daempft oder nahe am Grundwert haelt.

Wenn die adaptiven Gewichte nur sehr wenig streuen, ist die Schicht technisch aktiv, aber noch nicht stark welt- oder familienselektiv. Dann liegt die naechste Arbeit nicht in mehr Daten, sondern in genauerer Erfahrungskopplung pro Feldrolle.

## Grenze

Die Klassifikation ist eine passive Diagnose. Sie beschreibt Feldmilieu und Anschlussfaehigkeit, aber keine Richtung, keine Handlung und keine Strategie.

## Wie es weitergeht

Als naechstes sollte dieser Report auf neue Assets oder neue synthetische Kontrollwelten angewendet werden. Ziel ist zu pruefen, ob die Achsenklassen stabil bleiben oder neue Feldmilieus entstehen.
