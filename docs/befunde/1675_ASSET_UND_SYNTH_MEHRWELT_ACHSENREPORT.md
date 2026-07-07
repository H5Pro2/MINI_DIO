# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-07 11:01:34

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `docs\befunde\1675_ASSET_UND_SYNTH_MEHRWELT_ACHSENREPORT.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| axis_assets_btc_2024_0_to_2000 | btc_2024_5m | rand_kippnah | kompakt | 2 | 1 | 0 | 1 | 0.6912 | 0.1282 | 1472 | 497 | 23 | 2 |
| axis_assets_doge_2024_0_to_2000 | doge_2024_5m | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 1 | 0.6918 | 0.1255 | 1444 | 532 | 17 | 1 |
| axis_assets_xrp_2024_0_to_2000 | xrp_2024_5m | rand_kippnah | mittel | 4 | 6 | 3 | 3 | 0.6845 | 0.0888 | 1333 | 630 | 29 | 2 |
| axis_assets_paxg_2024_0_to_2000 | paxg_2024_5m | mittlere_uebergangsphase | mittel | 4 | 6 | 0 | 6 | 0.7005 | 0.1446 | 1613 | 364 | 14 | 3 |
| axis_synth_rand_kipp_0_to_2000 | synth_rand_kipp | rand_kippnah | verteilt | 7 | 19 | 14 | 3 | 0.7159 | 0.5605 | 1527 | 402 | 64 | 1 |

## Klassenverteilung

- `mittlere_uebergangsphase`: `2`
- `rand_kippnah`: `3`

## Befund

Der Report macht sichtbar, ob eine Weltphase kompakt gebunden, verteilt offen, verteilt rekoppelnd, nachhallend kompakt oder rand-/kippnah wirkt.

In dieser Asset-/Synth-Pruefung entstehen nur zwei Achsenklassen:

- `rand_kippnah`
- `mittlere_uebergangsphase`

BTC 2024 5m bleibt kompakt und rand-/kippnah. XRP 2024 5m liegt ebenfalls rand-/kippnah, aber mit mittlerer Rollenbreite. DOGE 2024 5m und PAXG 2024 5m werden als mittlere Uebergangsphasen gelesen.

Der synthetische Rand-/Kipp-Lauf ist der deutlichste Kontrast: Er ist verteilt, besitzt 7 Rollen und 19 Kombinationen, koppelt aber selektiv zurueck. Gleichzeitig ist sein Nachhall mit `0.5605` deutlich hoeher als bei den realen Assetfenstern. Das stuetzt die bisherige Lesung: Breite und Nachhall erzeugen nicht automatisch stabile Bindung. Entscheidend ist das gemeinsame Feldmilieu.

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

Als naechstes sollten laengere oder anders positionierte Assetfenster gegen denselben Report laufen. Ziel ist zu pruefen, ob `rand_kippnah` und `mittlere_uebergangsphase` assettypisch bleiben oder ob bei anderen Weltphasen wieder `kompakt_gebunden`, `kompakt_nachhallend`, `verteilt_offen` oder `verteilt_rekoppelnd` entstehen.
