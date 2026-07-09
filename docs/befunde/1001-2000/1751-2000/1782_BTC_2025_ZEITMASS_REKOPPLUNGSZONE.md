# 1782 - BTC 2025: zeitmaßnahe Rekopplungszone

## Grundfrage

Der vorherige Befund zeigte einen einzelnen `verteilt_rekoppelnd`-Treffer in BTC 2025 1h. Die offene Frage war, ob dieser Treffer nur lokal zufällig ist oder ob sich in der Umgebung eine zeitmaßnahe Rekopplungszone zeigt.

## Prüfung

Geprüft wurden:

- BTC 1h Nachbarschaft um `2000-3000 -> 3000-4000`
- BTC 30m ungefähr in derselben Weltphase
- BTC 15m ungefähr in derselben Weltphase

Die Fenster wurden passiv als Real-Sleep-Real-Achsen gelesen.

## Ergebnis

Es entstanden zwei `verteilt_rekoppelnd`-Treffer:

| Label | Zeitmaß | Rollen | Kombinationen | Rekopplung | Erfahrung | Nachhall |
|---|---|---:|---:|---:|---:|---:|
| `BTC_2025_1H_CORE_2000_3000` | 1h | 5 | 10 | 0.695555 | 0.4432 | 0.3512 |
| `BTC_2025_15M_ZONE_9000_10000` | 15m | 5 | 10 | 0.695155 | 0.4249 | 0.3388 |

Die 30m-Fenster derselben groben Phase bildeten keine rekoppelnde Breite. Sie blieben zwischen mittlerer Übergangsphase, verteilter Offenheit und kompakter Nachhallbindung.

## Klassenmittel

| Klasse | Anzahl | Rollen | Kombinationen | Rekopplung | Erfahrung | Nachhall |
|---|---:|---:|---:|---:|---:|---:|
| `kompakt_nachhallend` | 3 | 1.6667 | 0.6667 | 0.686713 | 0.6090 | 0.2799 |
| `mittlere_uebergangsphase` | 4 | 3.0000 | 3.0000 | 0.689719 | 0.5267 | 0.3079 |
| `verteilt_offen` | 2 | 6.0000 | 15.0000 | 0.693761 | 0.5733 | 0.3271 |
| `verteilt_rekoppelnd` | 2 | 5.0000 | 10.0000 | 0.695355 | 0.4341 | 0.3450 |

## Interpretation

Der Treffer ist nicht nur ein einzelner isolierter Punkt. BTC zeigt in derselben groben Weltphase sowohl im 1h- als auch im 15m-Zeitmaß rekoppelnde Breite.

Gleichzeitig ist die Zone nicht durchgehend:

- 1h enthält einen rekoppelnden Kern, davor offene Breite, danach Übergang.
- 30m enthält keine rekoppelnde Breite.
- 15m enthält erneut einen rekoppelnden Treffer, eingerahmt von kompakter Nachhallbindung und Übergang.

Damit wirkt die Rekopplung wie eine phasische Zone, nicht wie ein dauerhaft stabiler Block.

Die rekoppelnden Treffer tragen hier keine maximale Rollenanzahl. Sie tragen eine mittlere verteilte Breite mit höherer Rekopplung und höherem Nachhall. Das stützt weiter die Trennung:

```text
Mehr Rollen
  -> nicht automatisch rekoppelnd

mittlere Rollenbreite + Nachhall + Rückbindung
  -> rekoppelnde Breite möglich
```

## Grenze

Das ist eine passive Feldlesung. Sie beschreibt eine zeitmaßnahe Rekopplungszone in BTC 2025, aber keine Handlung, keine Richtung und keine Strategie.

## Artefakte

- `reports/btc_2025_zeitmass_rekopplungszone.csv`
- `reports/btc_2025_zeitmass_rekopplungszone.md`
- `reports/btc_2025_zeitmass_rekopplungszone_rawworld.csv`
- `reports/btc_2025_zeitmass_rekopplungszone_rawworld.md`
- `reports/btc_2025_zeitmass_rekopplungszone_rawworld_groups.csv`
