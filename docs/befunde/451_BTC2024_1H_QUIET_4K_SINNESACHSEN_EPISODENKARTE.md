# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-20 23:53:23

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\intake_memory_probe_btc2024_1h_quiet_4k\dio_mini_lauf_1`
- CSV: `docs\befunde\451_BTC2024_1H_QUIET_4K_SINNESACHSEN_EPISODENKARTE.csv`

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

### BTC_2024_1H_QUIET_4K

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1600 | 639 | 0.7246 | 0.1339 | 0.0612 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1542 | 616 | 0.7170 | 0.1383 | 0.1013 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0836 | 334 | 0.7030 | 0.1568 | 0.1148 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0608 | 243 | 0.7223 | 0.1322 | 0.0612 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0553 | 221 | 0.7159 | 0.1532 | 0.1171 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0541 | 216 | 0.6724 | 0.1857 | 0.1351 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0471 | 188 | 0.6957 | 0.1685 | 0.1809 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0463 | 185 | 0.7119 | 0.1406 | 0.1034 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0406 | 162 | 0.6871 | 0.1771 | 0.2088 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0248 | 99 | 0.7130 | 0.1505 | 0.1181 |

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
