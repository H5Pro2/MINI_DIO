# 1785 - BTC/PAXG: Rekopplungssignatur im Vergleich

## Grundfrage

Nach der BTC-Zonenmatrix aus 1784 war offen, ob BTC und PAXG dieselbe rekoppelnde Feldfunktion tragen oder ob PAXG eine eigene Bindungsform bildet.

## Prüfung

Verglichen wurden vorhandene passive Reports:

- BTC 2025: `verteilt_rekoppelnd` aus der BTC-Rekopplungszonen-Matrix
- PAXG: `verteilt_rekoppelnd` aus 5m-Fenstern 2024/2025
- PAXG: offene Breite als Gegenfolie

PAXG wurde über die vorhandene `count`-Spalte gewichtet. BTC wurde aus der Gesamtzeile der BTC-Matrix gelesen, damit keine Phasen- und Zeitmaßwerte doppelt gezählt werden.

## Ergebnis

| Gruppe | n | Rollen | Kombinationen | Cross | Same | Rekopplung | Erfahrung | Nachhall |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC `verteilt_rekoppelnd` | 3 | 5.3333 | 11.6667 | 4.3333 | 5.0000 | 0.695374 | 0.4344 | 0.3456 |
| PAXG `verteilt_rekoppelnd` | 4 | 7.2500 | 17.5000 | 9.0000 | 5.0000 | 0.704916 | 0.2515 | 0.3757 |
| PAXG offene Breite | 11 | 6.8182 | 17.9091 | 9.5455 | 6.4545 | 0.691200 | 0.4680 | 0.3045 |

## Interpretation

BTC und PAXG teilen die Grundform `verteilt_rekoppelnd`: erhöhte Rückbindung und erhöhter Nachhall gegenüber offener Breite.

Der Unterschied liegt in der Ausprägung:

```text
BTC
  -> enger, phasischer, zeitmaßabhängiger

PAXG
  -> breiter, stärker rekoppelnd, stärker nachhallend
```

PAXG zeigt mehr Rollen, mehr Kombinationen und deutlich mehr Cross-State-Kopplung. BTC zeigt dagegen eine engere Rekopplungszone mit hoher Stabilität. Damit wirkt PAXG nicht wie eine andere Topologie, sondern wie eine breiter öffnende Form derselben rekoppelnden Feldfunktion.

## Bedeutung für MINI_DIO

Der Befund stärkt die Lesart, dass MINI_DIO nicht nur Rollenanzahl bildet, sondern Feldfunktionen differenziert:

- offene Breite
- rekoppelnde Breite
- kompakte Nachhallbindung
- phasische Zeitmaßbindung

Wichtig ist: Rekopplung ist nicht einfach "viel Struktur". Sie entsteht, wenn Rollenbreite, Nachhall und Rückbindung gemeinsam tragend werden.

## Grenze

Das ist eine passive Diagnose. Sie beschreibt keine Handlung, keine Richtung und keine feste Regel. Der Befund sagt nur: In den geprüften Fenstern tragen BTC und PAXG eine ähnliche rekoppelnde Funktion, aber mit unterschiedlicher Breite und unterschiedlicher Zeitmaßbindung.

## Artefakte

- `reports/btc_paxg_rekopplungssignatur_vergleich.csv`
- `reports/btc_paxg_rekopplungssignatur_vergleich.md`

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob diese rekoppelnde Feldfunktion auch bei einem weiteren Asset oder einer synthetischen Kontrollwelt auftaucht. Ziel ist zu trennen, ob Rekopplung assetübergreifend stabil ist oder nur bei bestimmten Weltspannungen entsteht.
