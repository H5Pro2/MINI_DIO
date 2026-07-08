# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 14:17:39

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\xrp_doge_2025_lokale_realsleepreal_achsen_2.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| XRP_2025_FOLLOW_1000_2000 | XRP_2025_LOCAL_2 | verteilt_offen | verteilt | 6 | 13 | 7 | 6 | 0.6907 | 0.7246 | 0.0340 | 0.5025 | 0.3206 | 977 | 17 | 0 | 0 |
| DOGE_2025_FOLLOW_1000_2000 | DOGE_2025_LOCAL_2 | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.6897 | 0.7319 | 0.0422 | 0.5395 | 0.3191 | 979 | 15 | 0 | 0 |

## Klassenverteilung

- `kompakt_nachhallend`: `1`
- `verteilt_offen`: `1`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_und_gewichte_differenzieren`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0340 | 0.0422 | 0.0083 |
| Erfahrung | 0.5025 | 0.5395 | 0.0369 |
| Gewicht carry | 0.2942 | 0.3170 | 0.0229 |
| Gewicht alignment | 0.2207 | 0.2241 | 0.0033 |
| Gewicht strain_relief | 0.2599 | 0.2734 | 0.0135 |
| Gewicht sensory | 0.1990 | 0.2117 | 0.0127 |

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
