# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 14:13:41

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\xrp_doge_2025_lokale_realsleepreal_achsen.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| XRP_2025_FOLLOW_0_1000 | XRP_2025_LOCAL | verteilt_offen | verteilt | 6 | 15 | 9 | 6 | 0.6892 | 0.7238 | 0.0346 | 0.4494 | 0.3101 | 977 | 17 | 0 | 0 |
| DOGE_2025_FOLLOW_0_1000 | DOGE_2025_LOCAL | mittlere_uebergangsphase | mittel | 4 | 6 | 4 | 2 | 0.6897 | 0.7195 | 0.0299 | 0.3812 | 0.3039 | 977 | 17 | 0 | 0 |

## Klassenverteilung

- `mittlere_uebergangsphase`: `1`
- `verteilt_offen`: `1`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_und_gewichte_differenzieren`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0299 | 0.0346 | 0.0048 |
| Erfahrung | 0.3812 | 0.4494 | 0.0681 |
| Gewicht carry | 0.3152 | 0.3292 | 0.0140 |
| Gewicht alignment | 0.2236 | 0.2260 | 0.0024 |
| Gewicht strain_relief | 0.2530 | 0.2607 | 0.0077 |
| Gewicht sensory | 0.1918 | 0.2005 | 0.0087 |

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
