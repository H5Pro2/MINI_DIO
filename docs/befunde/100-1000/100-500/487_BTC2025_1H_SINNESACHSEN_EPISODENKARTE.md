# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-21 12:16:17

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\_codex_asset_year_stability\BTC2025_1H`
- CSV: `docs\befunde\487_BTC2025_1H_SINNESACHSEN_EPISODENKARTE.csv`

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

### BTC2025_1H

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1610 | 321 | 0.7206 | 0.1329 | 0.0593 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1319 | 263 | 0.7132 | 0.1388 | 0.0970 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0707 | 141 | 0.7008 | 0.1541 | 0.1030 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0502 | 100 | 0.6612 | 0.1902 | 0.1315 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0486 | 97 | 0.7167 | 0.1514 | 0.1101 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0426 | 85 | 0.6868 | 0.1703 | 0.1797 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0336 | 67 | 0.6793 | 0.1791 | 0.2049 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0336 | 67 | 0.7197 | 0.1357 | 0.0625 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0326 | 65 | 0.7139 | 0.1363 | 0.0901 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1ahj81f | 0.0271 | 54 | 0.7023 | 0.1376 | 0.0868 |

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
