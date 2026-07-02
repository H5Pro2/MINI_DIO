# MCM Asset-Feldantwort auf Bewegungsbruch

Stand: 2026-07-02

## Grundfrage

Bleibt `bewegungsbruch -> lastkontakt_entlastet` ueber Assets gleich, oder bildet jedes Asset eine eigene MCM-Feldantwort?

## Unterpruefung

Diese Diagnose verdichtet die Rohwelt-Fensterlupe assetweise. Sie erzeugt keine Handlung und keine Strategie.

## Eingabe

- `docs\befunde\1251_MCM_FELDPHASEN_ROHWELT_FENSTERLUPE.csv`

## Profil

- Assetgruppen: `6`
- Antwortklassen: `{'entlastender_bruchkontakt': 6}`

## Assetantworten

| Asset | Fenster | Klasse | Bewegung | Lesart | Loudness | Strain | Delta Rekopplung | Delta Strain | Expansion | Richtung | Dominante Welt |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| SOL | 135 | entlastender_bruchkontakt | bewegungsbruch | lastkontakt_entlastet | 0.8092 | 0.3042 | 0.0923 | -0.1176 | 3.7406 | 0.0854 | POS_EXPANSION_10K |
| XRP | 43 | entlastender_bruchkontakt | bewegungsbruch | lastkontakt_entlastet | 0.7963 | 0.3068 | 0.0938 | -0.1176 | 4.6206 | 0.0822 | XRP_5M_10K |
| DOGE | 32 | entlastender_bruchkontakt | bewegungsbruch | lastkontakt_entlastet | 0.8024 | 0.3055 | 0.0892 | -0.1166 | 3.9992 | 0.1013 | DOGE_5M_10K |
| BTC | 24 | entlastender_bruchkontakt | bewegungsbruch | lastkontakt_entlastet | 0.7763 | 0.3025 | 0.0930 | -0.1198 | 4.5958 | 0.0893 | BTC_1H_2K |
| PAXG | 13 | entlastender_bruchkontakt | bewegungsbruch | lastkontakt_entlastet | 0.7851 | 0.3043 | 0.0955 | -0.1164 | 6.2655 | 0.0871 | PAXG_5M_10K |
| KAS | 9 | entlastender_bruchkontakt | bewegungsbruch | lastkontakt_entlastet | 0.7358 | 0.3026 | 0.0857 | -0.1123 | 6.7289 | 0.0857 | KAS_5M_2K |

## Befund

Die gekoppelte Rohwelt-Lupe zeigt eine gemeinsame Grundform: `bewegungsbruch` dominiert fast durchgehend.

Die Assetantwort unterscheidet sich aber in Staerke, Lautheit, Expansion und Entlastungsdelta.

Damit ist die aktuelle Lesart:

```text
gleiche Grundklasse, unterschiedliche Feldfaerbung
```

Das passt zur bisherigen MCM-Lesung: Die Topologie bleibt stabil, aber Welt- und Assetcharakter faerben die Feldantwort.

## Grenze

Diese Diagnose nutzt nur eindeutig gekoppelte Fenster aus `1251`. Nicht alle Segmentwelten sind enthalten.

## Wie es weitergeht

Als naechstes wird geprueft, ob die assetweise Feldfaerbung ueber neue Rohweltfenster reproduzierbar bleibt oder ob sie nur aus dieser Auswahl stammt.
