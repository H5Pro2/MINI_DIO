# MCM Bewegungsbruch Folgeformen

Stand: 2026-07-02

## Grundfrage

Wann wird aus `bewegungsbruch` Entlastung, und wann entsteht Nachlast, gebrochene Rekopplung oder ein gemischtes Fenster?

## Unterpruefung

Diese Diagnose vergleicht die Fensterlesarten aus der erweiterten Rohwelt-Fensterlupe.

## Eingabe

- `docs\befunde\1257_MCM_FELDPHASEN_ROHWELT_FENSTERLUPE_ERWEITERT.csv`

## Folgeformen

| Fensterlesart | Anzahl | Folgequalitaet | Bewegung | Loudness | Strain | Delta Rekopplung | Delta Strain | Expansion | Richtung | Dominante Welt |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| lastkontakt_entlastet | 811 | moderate_entlastung | bewegungsbruch | 0.6890 | 0.2796 | 0.0810 | -0.0992 | 3.9522 | 0.0859 | POS_EXPANSION_10K |
| rekopplung_bricht_in_last | 61 | schwache_entlastung | bewegungsbruch | 0.6966 | 0.2670 | 0.0237 | -0.0446 | 4.2334 | 0.0854 | SIDEWAYS_10K |
| gemischtes_fenster | 21 | nachlast_oder_bruch | bewegungsbruch | 0.2068 | 0.1430 | -0.0140 | 0.0063 | 3.6576 | 0.0767 | DOGE_5M_10K |
| rekopplung_vor_neuer_last | 9 | nachlast_oder_bruch | bewegungsbruch | 0.1875 | 0.1389 | -0.1148 | 0.1257 | 3.8289 | 0.0594 | POS_EXPANSION_10K |
| lastkontakt_bleibt | 1 | unklar | bewegungsbruch | 0.3011 | 0.2513 | 0.0078 | -0.0069 | 3.0085 | 0.3235 | POS_EXPANSION_10K |

## Befund

Die Hauptform `lastkontakt_entlastet` unterscheidet sich nicht dadurch, dass sie keinen Bewegungsbruch hat.

Der Unterschied liegt vor allem in der Folgequalitaet:

```text
Entlastung = Rekopplung steigt deutlich und Strain faellt deutlich.
Gegenform = dieselbe Rohweltklasse, aber schwacheres oder gebrochenes Folgeprofil.
```

Damit ist Bewegungsbruch die Rohweltbedingung, aber nicht die ganze Erklaerung.

## Bedeutung

Das MCM-Feld liest nicht nur die Aussenbewegung. Es liest, ob das Feld nach der Aussenbewegung wieder Anschluss findet.

## Wie es weitergeht

Als naechstes sollten die Gegenformen mit konkreten Tickfenstern markiert werden: Wo beginnt die Nachlast, und welche Feldrolle liegt direkt davor?
