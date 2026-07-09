# MCM Asset-Feldantwort Balanced

Stand: 2026-07-02

## Grundfrage

Bleibt die Asset-Feldantwort erhalten, wenn jedes Asset mit gleich vielen Rohweltfenstern gelesen wird?

## Unterpruefung

Pro Asset wurden `36` Fenster verwendet. Die Auswahl nimmt pro Asset die staerksten Rand-/Strain-Fenster aus der vorhandenen Rohweltlupe.

Diese Diagnose ist passiv und erzeugt keine Handlung.

## Eingabe

- `docs\befunde\1257_MCM_FELDPHASEN_ROHWELT_FENSTERLUPE_ERWEITERT.csv`

## Profil

- Assetgruppen: `6`
- Fenster pro Asset: `36`
- Antwortklassen: `{'entlastender_bruchkontakt': 6}`

## Balancierte Assetantworten

| Asset | Fenster | Klasse | Bewegung | Lesart | Loudness | Strain | Delta Rekopplung | Delta Strain | Expansion | Richtung |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| BTC | 36 | entlastender_bruchkontakt | bewegungsbruch | lastkontakt_entlastet | 0.7614 | 0.2963 | 0.0915 | -0.1168 | 4.5235 | 0.0846 |
| DOGE | 36 | entlastender_bruchkontakt | bewegungsbruch | lastkontakt_entlastet | 0.7871 | 0.3036 | 0.0875 | -0.1146 | 4.0192 | 0.0981 |
| KAS | 36 | entlastender_bruchkontakt | bewegungsbruch | lastkontakt_entlastet | 0.6556 | 0.2747 | 0.0773 | -0.0975 | 4.4266 | 0.0770 |
| PAXG | 36 | entlastender_bruchkontakt | bewegungsbruch | lastkontakt_entlastet | 0.7570 | 0.2884 | 0.0832 | -0.1032 | 5.5995 | 0.0769 |
| SOL | 36 | entlastender_bruchkontakt | bewegungsbruch | lastkontakt_entlastet | 0.8747 | 0.3223 | 0.0974 | -0.1272 | 4.3092 | 0.1063 |
| XRP | 36 | entlastender_bruchkontakt | bewegungsbruch | lastkontakt_entlastet | 0.7994 | 0.3097 | 0.0976 | -0.1222 | 4.7843 | 0.0809 |

## Befund

Auch bei gleicher Fensterzahl bleibt die gemeinsame Grundform sichtbar.

Die Assetfaerbung bleibt aber nicht identisch: Lautheit, Expansion und Entlastungsdelta unterscheiden sich weiter.

## Grenze

Die kleinste Assetgruppe bestimmt die strenge Gleichverteilung. Dadurch ist diese Diagnose methodisch sauberer, aber kleiner.
