# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-20 15:53:02

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\intake_memory_probe_sol2026_sideways_10k`
- CSV: `docs\befunde\419_SOL2026_SIDEWAYS_10K_SINNESACHSEN_EPISODENKARTE.csv`

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

### SOL_2026_SIDEWAYS_10K

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1988 | 1987 | 0.7268 | 0.1324 | 0.0612 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1853 | 1852 | 0.7209 | 0.1378 | 0.1019 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0907 | 906 | 0.7089 | 0.1554 | 0.1129 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0646 | 646 | 0.6960 | 0.1700 | 0.1871 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0584 | 584 | 0.7176 | 0.1536 | 0.1162 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0553 | 553 | 0.6905 | 0.1765 | 0.2109 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0530 | 530 | 0.6824 | 0.1816 | 0.1278 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0289 | 289 | 0.6488 | 0.2248 | 0.2913 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0160 | 160 | 0.6693 | 0.2010 | 0.2106 |
| fuehlen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0128 | 128 | 0.6519 | 0.2146 | 0.2187 |

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
