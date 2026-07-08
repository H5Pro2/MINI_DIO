# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 17:38:53

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\synthetic_1788_role_mosaic_afterimage_axis_probe.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SYN1788_BASE_TO_FOLLOW | synthetic_role_mosaic_afterimage | kompakt_nachhallend | kompakt | 2 | 1 | 0 | 1 | 0.7511 | 0.7663 | 0.0152 | 0.0239 | 0.8003 | 3594 | 0 | 0 | 0 |
| SYN1788_BASE_TO_SHUFFLE | synthetic_role_mosaic_afterimage_control | kompakt_nachhallend | kompakt | 2 | 1 | 0 | 1 | 0.7511 | 0.7663 | 0.0152 | 0.0239 | 0.8003 | 3594 | 0 | 0 | 0 |

## Klassenverteilung

- `kompakt_nachhallend`: `2`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_aber_gewichte_noch_gleichfoermig`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0152 | 0.0152 | 0.0000 |
| Erfahrung | 0.0239 | 0.0239 | 0.0000 |
| Gewicht carry | 0.3692 | 0.3692 | 0.0000 |
| Gewicht alignment | 0.2296 | 0.2296 | 0.0000 |
| Gewicht strain_relief | 0.2286 | 0.2286 | 0.0000 |
| Gewicht sensory | 0.1726 | 0.1726 | 0.0000 |

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
