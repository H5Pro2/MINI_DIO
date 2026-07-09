# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-07 11:24:08

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `docs\befunde\1676_ASSET_SHIFT_MEHRWELT_ACHSENREPORT.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| axis_assets_btc_2024_2000_to_4000 | btc_2024_5m_shift | kompakt_gebunden | kompakt | 1 | 0 | 0 | 0 | 0.6938 | 0.1405 | 1548 | 426 | 14 | 6 |
| axis_assets_btc_2024_4000_to_6000 | btc_2024_5m_shift | verteilt_rekoppelnd | verteilt | 5 | 10 | 4 | 6 | 0.6973 | 0.1516 | 1664 | 321 | 9 | 0 |
| axis_assets_btc_2024_6000_to_8000 | btc_2024_5m_shift | verteilt_rekoppelnd | verteilt | 6 | 15 | 8 | 7 | 0.6975 | 0.1552 | 1655 | 331 | 8 | 0 |
| axis_assets_doge_2024_2000_to_4000 | doge_2024_5m_shift | mittlere_uebergangsphase | mittel | 3 | 3 | 0 | 3 | 0.6929 | 0.1347 | 1504 | 468 | 22 | 0 |
| axis_assets_doge_2024_4000_to_6000 | doge_2024_5m_shift | verteilt_offen | verteilt | 5 | 10 | 4 | 6 | 0.6891 | 0.1141 | 1443 | 531 | 20 | 0 |
| axis_assets_doge_2024_6000_to_8000 | doge_2024_5m_shift | mittlere_uebergangsphase | mittel | 4 | 6 | 3 | 3 | 0.7018 | 0.1704 | 1749 | 237 | 8 | 0 |
| axis_assets_xrp_2024_2000_to_4000 | xrp_2024_5m_shift | mittlere_uebergangsphase | mittel | 3 | 3 | 0 | 3 | 0.6952 | 0.1443 | 1591 | 381 | 19 | 3 |
| axis_assets_xrp_2024_4000_to_6000 | xrp_2024_5m_shift | mittlere_uebergangsphase | mittel | 4 | 6 | 3 | 3 | 0.6946 | 0.1384 | 1562 | 413 | 18 | 1 |
| axis_assets_xrp_2024_6000_to_8000 | xrp_2024_5m_shift | mittlere_uebergangsphase | mittel | 4 | 6 | 4 | 2 | 0.7030 | 0.1745 | 1749 | 233 | 12 | 0 |
| axis_assets_paxg_2024_2000_to_4000 | paxg_2024_5m_shift | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 1 | 0.6984 | 0.1321 | 1577 | 407 | 10 | 0 |
| axis_assets_paxg_2024_4000_to_6000 | paxg_2024_5m_shift | mittlere_uebergangsphase | mittel | 4 | 6 | 0 | 6 | 0.7050 | 0.1578 | 1660 | 326 | 8 | 0 |
| axis_assets_paxg_2024_6000_to_8000 | paxg_2024_5m_shift | mittlere_uebergangsphase | mittel | 3 | 3 | 0 | 3 | 0.7035 | 0.1406 | 1690 | 298 | 6 | 0 |

## Klassenverteilung

- `kompakt_gebunden`: `1`
- `mittlere_uebergangsphase`: `8`
- `verteilt_offen`: `1`
- `verteilt_rekoppelnd`: `2`

## Befund

Der Report macht sichtbar, ob eine Weltphase kompakt gebunden, verteilt offen, verteilt rekoppelnd, nachhallend kompakt oder rand-/kippnah wirkt.

Die verschobenen Assetfenster zeigen klarer als der vorherige Startfenster-Vergleich:

- BTC 2024 5m wechselt von `kompakt_gebunden` zu zweimal `verteilt_rekoppelnd`.
- DOGE 2024 5m bildet eine mittlere Uebergangsphase, danach ein `verteilt_offen`-Fenster und danach wieder eine mittlere Uebergangsphase.
- XRP 2024 5m bleibt in diesen drei Fenstern durchgehend `mittlere_uebergangsphase`, aber mit veraenderter Cross-/Same-Verteilung.
- PAXG 2024 5m bleibt ebenfalls durchgehend `mittlere_uebergangsphase`, mit eher gleicher Ebene statt starker Cross-State-Bruecke.

Damit ist die Achsenklasse nicht einfach assetfest. MINI_DIO liest nicht nur "BTC", "DOGE", "XRP" oder "PAXG", sondern das jeweilige Feldmilieu eines konkreten Weltabschnitts. Besonders BTC zeigt, dass aus kompakter Bindung eine verteilte rekoppelnde Rollenflaeche entstehen kann. DOGE zeigt dagegen ein offenes verteiltes Zwischenfenster, das weniger stark rekoppelt und mehr Unruhe traegt.

Der Befund passt zur bisherigen MCM-Lesung: Bedeutung liegt nicht im Rohobjekt allein, sondern in der gewirkten Feldlage aus Weltphase, Sinnesaufnahme, Rollenbreite, Nachhall und Rekopplung.

Wichtig ist die gemeinsame Lesung:

```text
Rollenbreite allein reicht nicht.
Nachhall allein reicht nicht.
Topologie allein reicht nicht.
Erst die gemeinsame Achsenlage beschreibt das Feldmilieu.
```

## Grenze

Die Klassifikation ist eine passive Diagnose. Sie beschreibt Feldmilieu und Anschlussfaehigkeit, aber keine Richtung, keine Handlung und keine Strategie.
