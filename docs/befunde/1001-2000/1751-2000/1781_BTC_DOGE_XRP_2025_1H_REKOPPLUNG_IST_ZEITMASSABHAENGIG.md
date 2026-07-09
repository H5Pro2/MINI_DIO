# 1781 - BTC/DOGE/XRP 2025 1h: Rekopplung ist zeitmaßabhängig

## Grundfrage

Nach der späten 5m-Prüfung blieb BTC/DOGE/XRP ohne `verteilt_rekoppelnd`. Die nächste Unterprüfung war deshalb, ob ein anderes Zeitmaß dieselbe offene Breite zeigt oder ob rekoppelnde Breite dort doch entstehen kann.

## Prüfung

Geprüft wurden 1h-Fenster aus BTC, DOGE und XRP 2025:

- `0-1000 -> 1000-2000`
- `1000-2000 -> 2000-3000`
- `2000-3000 -> 3000-4000`
- `3000-4000 -> 4000-5000`

Die Auswertung nutzt dieselbe passive Real-Sleep-Real-Achse wie die 5m-Prüfungen.

## Ergebnis

Im 1h-Zeitmaß entsteht einmal `verteilt_rekoppelnd`:

| Label | Klasse | Rollen | Kombinationen | Rekopplung | Erfahrung | Nachhall |
|---|---|---:|---:|---:|---:|---:|
| `BTC_2025_1H_2000_3000` | `verteilt_rekoppelnd` | 5 | 10 | 0.695555 | 0.4432 | 0.3512 |

Gesamtverteilung:

| Klasse | Anzahl |
|---|---:|
| `kompakt_nachhallend` | 2 |
| `mittlere_uebergangsphase` | 5 |
| `verteilt_offen` | 4 |
| `verteilt_rekoppelnd` | 1 |

DOGE und XRP bleiben in dieser Prüfung zwischen Übergang, offener Breite und kompakter Nachhallbindung. BTC bildet im mittleren 1h-Abschnitt eine rekoppelnde Breite.

## Interpretation

Der Befund korrigiert die vorherige Arbeitsannahme:

```text
Rekoppelnde Breite ist nicht PAXG-exklusiv.
Sie ist aber phasen- und zeitmaßabhängig.
```

BTC 5m blieb in den geprüften späten Fenstern offen. BTC 1h bildet in einem mittleren Abschnitt dagegen `verteilt_rekoppelnd`. Das spricht dafür, dass das Feld nicht nur Assetqualität liest, sondern auch die zeitliche Form der Weltspur.

Wichtig ist die Präzisierung:

- PAXG bleibt in den bisherigen Prüfungen der stabilere rekoppelnde Vergleichspol.
- BTC kann rekoppelnde Breite ebenfalls ausbilden, aber bisher punktueller.
- DOGE/XRP zeigen in dieser 1h-Prüfung keine rekoppelnde Breite.

## Grenze

Das ist eine passive Diagnose. Sie beschreibt Feldmilieu und Anschlussqualität, keine Handlung und keine Asset-Regel.

## Artefakte

- `reports/btc_doge_xrp_2025_1h_lokale_realsleepreal_sequenz.csv`
- `reports/btc_doge_xrp_2025_1h_lokale_realsleepreal_sequenz.md`
- `reports/btc_doge_xrp_2025_1h_sequence_rawworld_contrast.csv`
- `reports/btc_doge_xrp_2025_1h_sequence_rawworld_contrast.md`
- `reports/btc_doge_xrp_2025_1h_sequence_rawworld_contrast_groups.csv`
- `reports/btc_doge_xrp_2025_1h_asset_summary.csv`
- `reports/btc_doge_xrp_2025_1h_asset_summary.md`

## Wie es weitergeht

Als nächstes sollte das BTC-1h-Rekopplungsfenster gegen Nachbarfenster und gegen 15m/30m geprüft werden. Ziel ist zu klären, ob dort eine stabile zeitmaßnahe Rekopplungszone liegt oder nur ein einzelner lokaler Treffer.
