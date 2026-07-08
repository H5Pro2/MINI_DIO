# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 13:54:45

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\real_drift_asset_doge_xrp_2024_axis_map.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| REAL_DRIFT_DOGE_2024_A | DOGE_2024_DRIFT | kompakt_nachhallend | kompakt | 2 | 1 | 1 | 0 | 0.7024 | 0.7385 | 0.0361 | 0.7351 | 0.5660 | 4927 | 67 | 0 | 0 |
| REAL_DRIFT_XRP_2024_A | XRP_2024_DRIFT | kompakt_nachhallend | kompakt | 2 | 1 | 0 | 1 | 0.7033 | 0.7397 | 0.0363 | 0.7040 | 0.5664 | 4923 | 71 | 0 | 0 |

## Klassenverteilung

- `kompakt_nachhallend`: `2`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_aber_gewichte_noch_gleichfoermig`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0361 | 0.0363 | 0.0003 |
| Erfahrung | 0.7040 | 0.7351 | 0.0311 |
| Gewicht carry | 0.2990 | 0.2995 | 0.0005 |
| Gewicht alignment | 0.2204 | 0.2205 | 0.0001 |
| Gewicht strain_relief | 0.2703 | 0.2705 | 0.0001 |
| Gewicht sensory | 0.2097 | 0.2102 | 0.0005 |

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
