# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 14:00:08

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\real_drift_asset_doge_xrp_2025_axis_map.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| REAL_DRIFT_DOGE_2025_A | DOGE_2025_DRIFT | kompakt_nachhallend | kompakt | 2 | 1 | 0 | 1 | 0.7021 | 0.7368 | 0.0347 | 0.7119 | 0.5680 | 4949 | 45 | 0 | 0 |
| REAL_DRIFT_XRP_2025_A | XRP_2025_DRIFT | mittlere_uebergangsphase | mittel | 4 | 6 | 4 | 2 | 0.7025 | 0.7389 | 0.0364 | 0.7667 | 0.5677 | 4941 | 53 | 0 | 0 |

## Klassenverteilung

- `kompakt_nachhallend`: `1`
- `mittlere_uebergangsphase`: `1`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_aber_gewichte_noch_gleichfoermig`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0347 | 0.0364 | 0.0017 |
| Erfahrung | 0.7119 | 0.7667 | 0.0547 |
| Gewicht carry | 0.2984 | 0.3032 | 0.0048 |
| Gewicht alignment | 0.2201 | 0.2211 | 0.0010 |
| Gewicht strain_relief | 0.2679 | 0.2706 | 0.0027 |
| Gewicht sensory | 0.2078 | 0.2109 | 0.0031 |

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
