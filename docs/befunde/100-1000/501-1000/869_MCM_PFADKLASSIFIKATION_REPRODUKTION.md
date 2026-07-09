# MCM-Pfadklassifikation Reproduktion

## Zweck

Diese Notiz vergleicht die erste Pfadklassifikation `864` mit einer weiteren Weltgruppe `868`.
Ziel ist nicht, einzelne Token-Namen zu beweisen, sondern zu pruefen, ob die Feldrollen der MCM-Verdichtung reproduzierbar bleiben.

## Datengrundlage

- Basisvergleich: `864_MCM_PFADKLASSIFIKATION.csv`
- Weitere Weltgruppe: `868_MCM_PFADKLASSIFIKATION_WEITERE_WELTGRUPPE.csv`
- Weitere Weltgruppe gebildet aus sieben Episode-Welten:
  - `SOL2024`
  - `BTC2024`
  - `KAS2024`
  - `PAXG2024`
  - `QUIET2026`
  - `STRESS2025`
  - `EXPANSION2023`

## Pfadklassenvergleich

| Pfadklasse | 864 | 868 | Differenz |
|---|---:|---:|---:|
| stabile_insel | 14 | 11 | -3 |
| rekoppelnder_pfad | 41 | 24 | -17 |
| offener_driftpfad | 27 | 16 | -11 |
| randpfad | 3 | 3 | 0 |
| brueckenpfad | 18 | 19 | +1 |
| junge_oberflaeche | 30 | 29 | -1 |
| gemischter_pfad | 9 | 1 | -8 |

## Befund

Die zweite Weltgruppe veraendert die absolute Anzahl gemeinsamer Tokens, aber die Rollenordnung bleibt erkennbar.

Stabil:

- `randpfad` bleibt bei `3`.
- `brueckenpfad` bleibt nahezu gleich (`18` zu `19`).
- `junge_oberflaeche` bleibt nahezu gleich (`30` zu `29`).
- `stabile_insel` bleibt in derselben Groessenordnung (`14` zu `11`).

Veraendert:

- `rekoppelnder_pfad` faellt von `41` auf `24`.
- `offener_driftpfad` faellt von `27` auf `16`.
- `gemischter_pfad` faellt von `9` auf `1`.

Das spricht nicht gegen die Topologie. Es zeigt eher, dass die zweite Weltgruppe weniger gemischte oder offene Zwischenlagen erzeugt und staerker in klare Bruecken-, Oberflaechen- und stabile Rollen faellt.

## Bedeutung

Die Reproduktion bestaetigt nicht jeden einzelnen Token als feste Bedeutung.
Sie bestaetigt staerker die Rollenstruktur:

- stabile Inseln,
- rekoppelnde Pfade,
- offene Driftpfade,
- Randpfade,
- Brueckenpfade,
- junge Oberflaechen.

Damit wird die bisherige Lesart praeziser:

```text
MINI_DIO reproduziert nicht einfach Namen.
MINI_DIO reproduziert Feldrollen.
```

Die konkrete Symboloberflaeche bleibt weltabhaengig.
Die darunterliegende MCM-Ordnung wirkt dagegen deutlich stabiler.

## Einordnung

Das ist ein wichtiger Unterschied zur reinen Mustererkennung.
Ein reines Musterregister wuerde vor allem fragen:

```text
Kommt derselbe Name wieder?
```

Die MCM-Lesart fragt:

```text
Kommt dieselbe Feldrolle wieder?
Bleibt eine Insel Insel?
Bleibt Rand selten?
Bleibt Bruecke als Uebergang aktiv?
Entsteht Drift nur in bestimmten offenen Bereichen?
```

Die aktuelle Pruefung spricht dafuer, dass MINI_DIO eine reproduzierbare Rollenordnung ausbildet, ohne dass die Tokenoberflaeche starr identisch bleiben muss.

## Wie es weitergeht

Als naechstes sollte die zweite Pfadklassifikation nicht weiter global gelesen werden, sondern an den stabilsten Rollen geprueft werden:

1. Welche Brueckenpfade bleiben ueber beide Gruppen aktiv?
2. Welche Randpfade bleiben randnah?
3. Welche jungen Oberflaechen reifen in Folgepruefungen nach?
4. Welche rekoppelnden Pfade sind echte Innenordnung und welche nur Weltgruppeneffekt?
