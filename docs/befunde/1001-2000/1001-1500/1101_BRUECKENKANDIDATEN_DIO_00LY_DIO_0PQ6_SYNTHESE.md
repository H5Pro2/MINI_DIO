# 1101 - Brueckenkandidaten dio_00ly und dio_0pq6

Diese Synthese ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Frage

Sind `dio_00ly` und `dio_0pq6` echte neue Brueckenkandidaten oder nur lokale Oberflaechenkontakte?

## Datengrundlage

- `1097_BRUECKENKANDIDAT_DIO_00LY_EINZELEREIGNISSE`
- `1098_BRUECKENKANDIDAT_DIO_00LY_TICKFENSTER`
- `1099_BRUECKENKANDIDAT_DIO_0PQ6_EINZELEREIGNISSE`
- `1100_BRUECKENKANDIDAT_DIO_0PQ6_TICKFENSTER`

## Kompakter Vergleich

| Familie | Lesart | Ereignisse | Welten | Gruppen | Spannung | Rekopplung | Strain | Delta Rekopplung | Delta Strain |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|
| `dio_00ly` | tragende Verarbeitung | 474 | 11 | feld_5m;zeit_1h | 0.0729 | 0.7284 | 0.1303 | 0.0214 | -0.0215 |
| `dio_00ly` | Kippnaehe | 12 | 6 | feld_5m;zeit_1h | 0.0934 | 0.6706 | 0.1646 | -0.0028 | 0.0013 |
| `dio_0pq6` | tragende Verarbeitung | 10 | 4 | feld_5m;zeit_1h | 0.0664 | 0.7266 | 0.1244 | 0.0221 | -0.0324 |
| `dio_0pq6` | Kippnaehe | 24 | 6 | feld_5m;zeit_1h | 0.0921 | 0.6769 | 0.1753 | -0.0154 | 0.0149 |

## Technische Lesart

`dio_00ly` wirkt wie ein breiter, haeufig getragener Brueckenkandidat.

Merkmale:

- sehr viele tragende Ereignisse,
- Sichtbarkeit in 5m- und 1h-Welten,
- tragende Lesart mit hoeherer Rekopplung und niedrigerem Strain,
- kippnahe Lesart bleibt vorhanden, aber deutlich kleiner.

Damit ist `dio_00ly` kein reines Einzelereignis. Die Familie wirkt als moeglicher neuer breit getragener Brueckenknoten.

`dio_0pq6` wirkt schmaler, aber differenzierter.

Merkmale:

- weniger Gesamtaktivitaet,
- kippnahe Ereignisse haeufiger als tragende,
- sehr klare Trennung: tragend ist rekoppelter und strainaermer, kippnah ist belasteter,
- Tickfenster zeigen nach tragenden Punkten teilweise schnelle Rueckkehr in Belastung.

Damit ist `dio_0pq6` kein stabiler breiter Knoten wie `dio_00ly`, sondern eher ein empfindlicher Umschalt- oder Kontaktkandidat.

## Befundgrenze

Diese Familien werden noch nicht als fertige Bedeutungen gesetzt.

Der Befund sagt nur:

```text
Beide Familien koennen reale Feldlesarten tragen.
Die aktuelle Bedeutung entsteht erst aus Weltfenster, Rezeptorhaltung, Feldfolge und Rueckkopplung.
```

## Bedeutung fuer das Bedeutungsnetz

Die bisherige Qualitaetskarte bleibt gueltig, aber sie wirkt nicht abgeschlossen.

`dio_00ly` und `dio_0pq6` zeigen, dass MINI_DIO neue Knoten am Rand oder in der Erweiterung der Karte ausbilden kann:

- `dio_00ly` als breiter getragener Brueckenkandidat,
- `dio_0pq6` als schmaler, empfindlicher Umschaltkandidat.

Das stuetzt die Lesart eines dynamischen Bedeutungsnetzes: stabile Rollen bleiben erhalten, neue Knoten koennen bei ausreichender Wiederkehr und Rueckkopplung nachreifen.

## Wie es weitergeht

Als naechstes sollte geprueft werden, ob `dio_00ly` und `dio_0pq6` in einer weiteren unabhaengigen Weltgruppe wieder auftauchen oder ob sie an die aktuelle Holdout-Gruppe gebunden bleiben.
