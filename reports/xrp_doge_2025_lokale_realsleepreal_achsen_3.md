# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 14:20:13

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\xrp_doge_2025_lokale_realsleepreal_achsen_3.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| XRP_2025_FOLLOW_2000_3000 | XRP_2025_LOCAL_3 | verteilt_offen | verteilt | 5 | 10 | 4 | 3 | 0.6923 | 0.7273 | 0.0350 | 0.4387 | 0.3075 | 982 | 12 | 0 | 0 |
| DOGE_2025_FOLLOW_2000_3000 | DOGE_2025_LOCAL_3 | verteilt_offen | verteilt | 6 | 15 | 8 | 7 | 0.6885 | 0.7278 | 0.0394 | 0.4578 | 0.2843 | 977 | 17 | 0 | 0 |

## Klassenverteilung

- `verteilt_offen`: `2`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_und_gewichte_differenzieren`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0350 | 0.0394 | 0.0044 |
| Erfahrung | 0.4387 | 0.4578 | 0.0191 |
| Gewicht carry | 0.3038 | 0.3157 | 0.0119 |
| Gewicht alignment | 0.2222 | 0.2238 | 0.0017 |
| Gewicht strain_relief | 0.2602 | 0.2672 | 0.0070 |
| Gewicht sensory | 0.2003 | 0.2068 | 0.0066 |

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
