# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-21 12:16:19

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\_codex_asset_year_stability\SOL2025_1H`
- CSV: `docs\befunde\489_SOL2025_1H_SINNESACHSEN_EPISODENKARTE.csv`

## Methode

Pro Welt werden die Achsen weltrelativ normalisiert. Eine Achse gilt lokal dominant, wenn sie in dieser Welt deutlich ueber ihrem eigenen Durchschnitt liegt.

Gelesene Achsen:

- `sehen_fokus`
- `sehen_abstand`
- `hoeren_hin`
- `hoeren_leise`
- `fuehlen_abstand`
- `feldinput`
- `ausgeglichen`

## Top-Befunde je Welt

### SOL2025_1H

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1484 | 296 | 0.7190 | 0.1349 | 0.0638 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1409 | 281 | 0.7113 | 0.1389 | 0.1022 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0832 | 166 | 0.6989 | 0.1565 | 0.1129 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0597 | 119 | 0.6631 | 0.1907 | 0.1332 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0416 | 83 | 0.6854 | 0.1754 | 0.1977 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0401 | 80 | 0.7182 | 0.1342 | 0.0628 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0396 | 79 | 0.7139 | 0.1539 | 0.1152 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0366 | 73 | 0.7118 | 0.1390 | 0.0987 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0321 | 64 | 0.6822 | 0.1779 | 0.2044 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1ahj81f | 0.0236 | 47 | 0.7068 | 0.1371 | 0.0662 |

## Erste Lesart

Die Weltmittelwerte waren eng. Lokal entstehen aber unterscheidbare Achsenlagen. Entscheidend ist nicht, dass eine Welt insgesamt lauter oder visueller ist, sondern welche Achse in konkreten Episoden hervorsticht und ob diese Episode rekoppelt oder belastet.

Damit verschiebt sich die naechste Pruefung von globaler Regulation zu episodischer Kopplung:

```text
Welche Achsenlage wurde vom Feld getragen?
Welche Achsenlage erzeugte Strain?
Welche Achsenlage blieb nur offen oder ausgeglichen?
```

## Wie es weitergeht

Als naechstes wird aus dieser Karte eine kleine Rekopplungsanalyse abgeleitet: Welche Achsenlage hat pro Welt die beste Rekopplung bei niedriger Belastung?
