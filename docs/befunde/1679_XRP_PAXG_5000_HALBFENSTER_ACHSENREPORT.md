# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-07 12:20:58

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `docs\befunde\1679_XRP_PAXG_5000_HALBFENSTER_ACHSENREPORT.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| axis_xrp_2024_5000_halves | xrp_2024_5m_5000_halves | rand_kippnah | mittel | 4 | 6 | 3 | 3 | 0.6912 | 0.1086 | 3306 | 1621 | 64 | 3 |
| axis_paxg_2024_5000_halves | paxg_2024_5m_5000_halves | rand_kippnah | mittel | 4 | 6 | 0 | 6 | 0.7067 | 0.1643 | 4026 | 939 | 26 | 3 |

## Klassenverteilung

- `rand_kippnah`: `2`

## Befund

Der Report macht sichtbar, ob eine Weltphase kompakt gebunden, verteilt offen, verteilt rekoppelnd, nachhallend kompakt oder rand-/kippnah wirkt.

Diese Pruefung nutzt dieselbe Halbfensterlogik wie Report 1678:

```text
0-5000 -> 5000-10000
```

Auch XRP und PAXG werden bei laengerer Lesetiefe `rand_kippnah`.

Damit erweitert sich der Befund:

- BTC 2024 5m: `rand_kippnah`
- DOGE 2024 5m: `rand_kippnah`
- XRP 2024 5m: `rand_kippnah`
- PAXG 2024 5m: `rand_kippnah`

Die Unterschiede liegen nicht im groben Achsenlabel, sondern in der inneren Zusammensetzung:

- XRP bleibt unruhiger: `tragend_unruhig=1621`, `kippend=64`, niedrigerer Nachhall `0.1086`.
- PAXG wirkt stabiler und same-state-lastiger: `stabil=4026`, `kippend=26`, `same_state=6`, Nachhall `0.1643`.

Das bestaetigt die Trennung zwischen:

```text
gemeinsamer Feldklasse
und
asset-/weltphasenspezifischer Binnenqualitaet
```

Vorlaeufige Lesung: 5000er-Halbfenster bringen bei den bisher geprueften 2024-5m-Assets ein gemeinsames Rand-/Kippmilieu hervor. Die Binnenqualitaet unterscheidet sich jedoch deutlich. Damit ist `rand_kippnah` keine simple Gleichmachung, sondern eine gemeinsame uebergeordnete Lage mit unterschiedlichen inneren Auspraegungen.

Wichtig ist die gemeinsame Lesung:

```text
Rollenbreite allein reicht nicht.
Nachhall allein reicht nicht.
Topologie allein reicht nicht.
Erst die gemeinsame Achsenlage beschreibt das Feldmilieu.
```

## Grenze

Die Klassifikation ist eine passive Diagnose. Sie beschreibt Feldmilieu und Anschlussfaehigkeit, aber keine Richtung, keine Handlung und keine Strategie.

## Wie es weitergeht

Als naechstes sollte ein zusammenfassender Vier-Asset-Halbfensterbefund erstellt werden. Ziel ist, BTC, DOGE, XRP und PAXG nebeneinander zu lesen: gemeinsame Rand-/Kippklasse, aber unterschiedliche Binnenqualitaet.
