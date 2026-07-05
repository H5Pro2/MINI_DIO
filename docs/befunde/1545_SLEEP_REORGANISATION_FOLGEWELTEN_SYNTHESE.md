# Sleep-Reorganisation Folgewelten Synthese

Stand: 2026-07-05

## Zweck

Diese Synthese ordnet die ersten Real-Sleep-Real-Pruefungen ein.

Geprueft wurde:

- Real A: SOL-2024-5m-Welt,
- Sleep: entkoppeltes MCM-Feldmilieu aus gespeicherten Feldepisoden,
- Real B: gleiche Welt, verwandte SOL-Folgewelt oder BTC-Assetgegenpruefung.

Die Sleep-Phase schreibt nur eine passive Reorganisationsspur:

```text
passive_sleep_reorganization_memory
```

Diese Spur markiert beruehrte bestehende Rollen. Sie erzeugt keine neue Weltbedeutung, kein Gate, keine Richtung und keine Handlung.

## Ergebnisuebersicht

| Pruefung | Real B Welt | Top-Syntax | Top-Familien | MCM-Tragqualitaet | MCM-Rekopplung | Lesung |
|---|---|---:|---:|---:|---:|---|
| 1541 Baseline | gleiche SOL-Welt | 1.000000 | 1.000000 | 0.510684 | 0.692524 | Wiederholung bleibt stabil |
| 1543 SOL-Folgewelt | SOL Bridge 2024 | 0.600000 | 1.000000 | 0.497263 | 0.686759 | Familien bleiben, Oberflaeche verschiebt |
| 1544 BTC-Gegenpruefung | BTC 2024 | 0.777778 | 0.777778 | 0.513118 | 0.695028 | assetuebergreifende Teilankopplung |

## Schlafspur

In allen drei Pruefungen beruehrte Sleep dieselben drei bestehenden MCM-Episodenrollen:

```text
dio_mcm_episode_1k2bqha
dio_mcm_episode_0e7qvj1
dio_mcm_episode_1wra2fc
```

Der Sleep-Zustand blieb:

```text
sleep_rekopplung
```

Die Reorganisationsspur wurde als:

```text
sleep_focused_role_touch
```

gelesen.

## Fachliche Lesung

Der aktuelle Befund zeigt noch nicht:

```text
MINI_DIO bildet im Schlaf eigenstaendig neue Kontexte.
```

Der aktuelle Befund zeigt aber:

```text
Sleep kann bestehende Feldrollen offline wieder beruehren.
Diese Rollen bleiben bei erneuter Weltberuehrung anschlussfaehig.
Die Anschlussfaehigkeit ist je nach Folgewelt unterschiedlich.
```

Die SOL-Folgewelt behielt alle Top-Familien, aber nicht alle Oberflaechensymbole. Das spricht fuer:

```text
gleiche Bedeutungsfamilie, veraenderte Oberflaeche
```

Die BTC-Gegenpruefung behielt 7 von 8 Top-Familien und zeigte leicht hoehere Tragqualitaet, Rekopplung und Sinneskopplung. Das spricht vorsichtig fuer:

```text
assetuebergreifende Feldnaehe
```

Es ist aber noch kein Beweis, dass Sleep diese Naehe verursacht. Die Sleep-Spur wird aktuell gespeichert, aber noch nicht als aktive Leseschicht verwendet.

## Grenze

Die aktuelle Stufe trennt sauber:

```text
Offline-Beruehrung alter Rollen
von
neuer Schlaf-Kontextbildung
```

Neue Kontextbildung waere erst dann belastbar, wenn:

1. Sleep alte Rollen anders kombiniert,
2. diese Kombination als eigene passive Spur stabil bleibt,
3. sie spaeter in realer Weltlage wieder auftaucht,
4. und sie sich von normaler Wiederholung unterscheiden laesst.

## Wie es weitergeht

Als naechstes wird eine Leseschicht gebaut, die `passive_sleep_reorganization_memory` im naechsten Real-Lauf nur passiv mitliest.

Ziel:

```text
Tauchen im Schlaf beruehrte Rollen im Real-Lauf wieder auf?
Werden sie klarer, driftender oder bleiben sie neutral?
```

Erst danach kann sinnvoll geprueft werden, ob Sleep mehr ist als Rollenmarkierung.
