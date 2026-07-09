# MCM Asset-Feldantwort Balanced

Stand: 2026-07-02

## Grundfrage

Bleibt die Asset-Feldantwort erhalten, wenn jedes Asset mit gleich vielen Rohweltfenstern gelesen wird?

## Unterpruefung

Pro Asset wurden `9` Fenster verwendet. Die Auswahl nimmt pro Asset die staerksten Rand-/Strain-Fenster aus der vorhandenen Rohweltlupe.

Diese Diagnose ist passiv und erzeugt keine Handlung.

## Eingabe

- `docs\befunde\1251_MCM_FELDPHASEN_ROHWELT_FENSTERLUPE.csv`

## Profil

- Assetgruppen: `6`
- Fenster pro Asset: `9`
- Antwortklassen: `{'entlastender_bruchkontakt': 3, 'stark_entlastender_bruchkontakt': 3}`

## Balancierte Assetantworten

| Asset | Fenster | Klasse | Bewegung | Lesart | Loudness | Strain | Delta Rekopplung | Delta Strain | Expansion | Richtung |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| BTC | 9 | entlastender_bruchkontakt | bewegungsbruch | lastkontakt_entlastet | 0.8079 | 0.3125 | 0.0958 | -0.1281 | 4.9070 | 0.1111 |
| DOGE | 9 | stark_entlastender_bruchkontakt | bewegungsbruch | lastkontakt_entlastet | 0.8139 | 0.3235 | 0.1018 | -0.1332 | 4.9217 | 0.1000 |
| KAS | 9 | entlastender_bruchkontakt | bewegungsbruch | lastkontakt_entlastet | 0.7358 | 0.3026 | 0.0857 | -0.1123 | 6.7289 | 0.0857 |
| PAXG | 9 | stark_entlastender_bruchkontakt | bewegungsbruch | lastkontakt_entlastet | 0.8096 | 0.3096 | 0.1009 | -0.1214 | 6.5495 | 0.0823 |
| SOL | 9 | stark_entlastender_bruchkontakt | bewegungsbruch | lastkontakt_entlastet | 0.9067 | 0.3338 | 0.1122 | -0.1424 | 3.8398 | 0.1147 |
| XRP | 9 | entlastender_bruchkontakt | bewegungsbruch | lastkontakt_entlastet | 0.8419 | 0.3257 | 0.0993 | -0.1271 | 5.4281 | 0.0508 |

## Befund

Auch bei gleicher Fensterzahl bleibt die gemeinsame Grundform sichtbar.

Die Assetfaerbung bleibt aber nicht identisch: Lautheit, Expansion und Entlastungsdelta unterscheiden sich weiter.

## Grenze

Die kleinste Assetgruppe bestimmt die strenge Gleichverteilung. Dadurch ist diese Diagnose methodisch sauberer, aber kleiner.

## Wie es weitergeht

Als naechstes sollte ein zweiter balancierter Lauf mit mehr Rohfenstern pro Asset erzeugt werden, statt nur aus der vorhandenen 1251-Auswahl zu ziehen.
