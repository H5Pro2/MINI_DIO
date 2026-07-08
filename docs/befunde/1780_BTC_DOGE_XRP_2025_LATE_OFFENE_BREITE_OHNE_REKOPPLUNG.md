# 1780 - BTC/DOGE/XRP 2025 Late: offene Breite ohne Rekopplung

## Grundfrage

Nach der 1779-Prüfung blieb offen, ob BTC, DOGE oder XRP in späteren 2025-Fenstern ebenfalls `verteilt_rekoppelnd` werden können oder ob sie auch dort eher offene Rollenbreite bilden.

## Prüfung

Geprüft wurden die späten lokalen Anschlussfenster 5000-10000:

- BTC 2025: `5000-6000 -> 6000-7000` bis `8000-9000 -> 9000-10000`
- DOGE 2025: `5000-6000 -> 6000-7000` bis `8000-9000 -> 9000-10000`
- XRP 2025: `5000-6000 -> 6000-7000` bis `8000-9000 -> 9000-10000`

Die Messung nutzt dieselbe passive Real-Sleep-Real-Achse wie die vorherige Vier-Asset-Sequenz.

## Ergebnis

Es entstand kein `verteilt_rekoppelnd`.

Klassenverteilung:

| Klasse | Anzahl | Rollen | Kombinationen | Rekopplung | Nachhall |
|---|---:|---:|---:|---:|---:|
| `mittlere_uebergangsphase` | 2 | 3.0000 | 3.0000 | 0.688316 | 0.3000 |
| `verteilt_offen` | 10 | 6.8000 | 17.4000 | 0.686443 | 0.2782 |

XRP erreichte lokal sehr hohe Rollenbreite, zum Beispiel 12 Rollen und 32 Kombinationen im Fenster `8000-9000 -> 9000-10000`. Trotzdem blieb die Klasse `verteilt_offen`.

BTC und DOGE zeigten ebenfalls offene Rollenbreite und einzelne mittlere Übergangsphasen, aber keine rekoppelnde Breite.

## Interpretation

Der Befund stärkt die Trennung zwischen Rollenbreite und Rekopplungsqualität:

- Viele Rollen und Kombinationen reichen nicht aus.
- Breite kann offen bleiben, auch wenn sie stark ausgebaut ist.
- Rekoppelnde Breite braucht zusätzlich stärkere Rückbindung, mehr tragenden Nachhall und weniger offene Richtungswechsel.

Damit bleibt PAXG aus den bisherigen Prüfungen der stärkere rekoppelnde Vergleichspol. BTC, DOGE und XRP können in diesen späten Fenstern viel Rollenraum öffnen, aber dieser Rollenraum wird nicht ähnlich stark zusammengehalten.

## Grenze

Das ist keine endgültige Asset-Aussage. Der Befund gilt für die geprüften späten 2025-Fenster. Andere Jahre, Zeitmaße oder Weltabschnitte können anders ausfallen.

## Artefakte

- `reports/btc_doge_xrp_2025_late_lokale_realsleepreal_sequenz.csv`
- `reports/btc_doge_xrp_2025_late_lokale_realsleepreal_sequenz.md`
- `reports/btc_doge_xrp_2025_late_sequence_rawworld_contrast.csv`
- `reports/btc_doge_xrp_2025_late_sequence_rawworld_contrast.md`
- `reports/btc_doge_xrp_2025_late_sequence_rawworld_contrast_groups.csv`
- `reports/btc_doge_xrp_2025_late_asset_summary.csv`
- `reports/btc_doge_xrp_2025_late_asset_summary.md`

## Wie es weitergeht

Als nächstes sollte ein anderes Jahr oder ein anderes Zeitmaß für BTC/DOGE/XRP geprüft werden. Ziel ist zu klären, ob rekoppelnde Breite dort grundsätzlich möglich ist oder ob sie bisher besonders an PAXG-nahe Weltmilieus gebunden bleibt.
