# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-20 16:55:12

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\intake_memory_probe_sol2023_positive_expansion_10k`
- CSV: `docs\befunde\425_SOL2023_POSITIVE_EXPANSION_10K_SINNESACHSEN_EPISODENKARTE.csv`

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

### SOL_2023_POSITIVE_EXPANSION_10K

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1520 | 1519 | 0.7197 | 0.1380 | 0.1051 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1461 | 1460 | 0.7253 | 0.1321 | 0.0611 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0892 | 891 | 0.7067 | 0.1552 | 0.1112 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0664 | 664 | 0.6756 | 0.1856 | 0.1293 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0450 | 450 | 0.6969 | 0.1702 | 0.1875 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0398 | 398 | 0.7276 | 0.1312 | 0.0577 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0377 | 377 | 0.7161 | 0.1551 | 0.1167 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0356 | 356 | 0.6907 | 0.1770 | 0.2128 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0343 | 343 | 0.7204 | 0.1362 | 0.0987 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0225 | 225 | 0.6516 | 0.2219 | 0.2856 |

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
