# 1513 - DOGE 2025 Randrollen-Stressgegenprüfung

## Zweck

Nach SOL und PAXG wurde eine lautere, offenere Gegenwelt geprüft:

`data/kontrolliert_doge_2025_5m_10k_DOGEUSDT.csv`

Der Lauf wurde frisch mit eigener Memory ausgeführt:

`debug/1513_real_doge2025_5m_10k_randrollen_stress_check`

Ziel war zu prüfen, ob die Geschwisterrollen `dio_0l7p` und `dio_14wj` unter einer rauschigeren DOGE-Welt stabil bleiben, verschwinden oder in Randspannung driften.

## Laufdaten

Ausgeführt wurden zwei Läufe mit `world_relative`:

```powershell
python -m mini_dio.run_mini --data data\kontrolliert_doge_2025_5m_10k_DOGEUSDT.csv --runs 2 --reset-memory --debug-root debug\1513_real_doge2025_5m_10k_randrollen_stress_check --world-label 1513_doge2025_5m_10k --sense-mode world_relative
```

## Ergebnis

Beide Läufe erzeugen praktisch dieselbe Innenfeldkarte.

| Kennwert | Lauf 1 | Lauf 2 |
| --- | ---: | ---: |
| Unique Symbols | 673 | 673 |
| Avg MCM Carry | 0.5368 | 0.5372 |
| Avg MCM Rekopplung | 0.7052 | 0.7048 |
| Avg MCM Strain | 0.1529 | 0.1526 |
| Avg Sensory Coupling | 0.8422 | 0.8418 |
| Stable Inner Effect | 0.8018 | 0.8012 |
| Carried Unrest | 0.1915 | 0.1921 |
| Strained | 0.0007 | 0.0006 |
| Tipping | 0.0060 | 0.0061 |

Die Reproduktion ist damit sehr eng:

```text
DOGE 2025 5m bleibt offener und unruhiger als PAXG,
aber es entsteht kein Randkollaps.
```

## Rollenprofil

Die beiden Zielrollen tauchen wieder sichtbar auf:

| Familie | Lauf 1 Count | Lauf 2 Count | Lesung |
| --- | ---: | ---: | --- |
| `dio_0l7p` | 394 | 788 | fokussierte Rekopplungs-/Wechselnähe |
| `dio_14wj` | 243 | 486 | ruhige sensorische Rekopplungsnähe |

Der höhere Count in Lauf 2 entsteht durch die kumulative Memory-Zählung über beide Läufe. Die Top-Symbol-Lesung pro Lauf bleibt gleich:

- `dio_0l7pvdk`: 394
- `dio_14wjmk5`: 243

## Deutung

DOGE bestätigt die Geschwisterrollen.

`dio_0l7p` bleibt stärker sichtbar als `dio_14wj`, ähnlich wie in SOL.

`dio_14wj` verschwindet aber nicht und kippt nicht in instabile Randspannung. Es bleibt eine wiedererkennbare ruhige Rekopplungsrolle, nur weniger dominant als in PAXG.

Damit ergibt sich eine präzisere Asset-Färbung:

| Welt | Wirkung auf `dio_14wj` |
| --- | --- |
| PAXG | stärker, häufiger, nachhallender |
| SOL | stabil, aber weniger dominant |
| DOGE | stabil, aber durch mehr offene Unruhe schwächer gewichtet |

## MCM-Deutung

Der Befund stärkt den Rollenatlas:

Eine Feldrolle kann ihre Grundqualität behalten, obwohl die Welt lauter, offener oder unruhiger wird.

DOGE erhöht nicht automatisch Randspannung. Die Rezeptoraufnahme hält die Weltspannung so weit geordnet, dass das Feld weiterhin überwiegend stabil rekoppelt.

Wichtig ist die Trennung:

```text
Welt wird unruhiger.
Feldrolle bleibt lesbar.
Gewichtung verändert sich.
Topologie bricht nicht.
```

## Grenze

Dieser Lauf beweist nicht, dass `dio_14wj` unter jeder Stresswelt stabil bleibt.

Er zeigt aber: Eine rauschigere DOGE-Welt reicht bisher nicht aus, um die Rolle in Randspannung zu drücken oder zu löschen.
