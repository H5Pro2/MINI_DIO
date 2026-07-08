# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 14:23:24

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\xrp_doge_2025_lokale_realsleepreal_achsen_4.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| XRP_2025_FOLLOW_3000_4000 | XRP_2025_LOCAL_4 | mittlere_uebergangsphase | mittel | 4 | 6 | 3 | 1 | 0.6901 | 0.7313 | 0.0412 | 0.6007 | 0.3103 | 984 | 10 | 0 | 0 |
| DOGE_2025_FOLLOW_3000_4000 | DOGE_2025_LOCAL_4 | mittlere_uebergangsphase | mittel | 4 | 6 | 3 | 3 | 0.6891 | 0.7315 | 0.0424 | 0.6771 | 0.2984 | 979 | 15 | 0 | 0 |

## Klassenverteilung

- `mittlere_uebergangsphase`: `2`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_aber_gewichte_noch_gleichfoermig`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0412 | 0.0424 | 0.0012 |
| Erfahrung | 0.6007 | 0.6771 | 0.0764 |
| Gewicht carry | 0.2949 | 0.2976 | 0.0026 |
| Gewicht alignment | 0.2207 | 0.2211 | 0.0005 |
| Gewicht strain_relief | 0.2729 | 0.2729 | 0.0000 |
| Gewicht sensory | 0.2084 | 0.2115 | 0.0031 |

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
