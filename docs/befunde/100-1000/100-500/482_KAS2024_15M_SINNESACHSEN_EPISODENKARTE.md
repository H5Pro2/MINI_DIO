# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-21 11:09:50

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\_codex_kas_profile_stability\KAS2024_15M`
- CSV: `docs\befunde\482_KAS2024_15M_SINNESACHSEN_EPISODENKARTE.csv`

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

### KAS2024_15M

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.2096 | 418 | 0.7176 | 0.1344 | 0.0637 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1956 | 390 | 0.7099 | 0.1418 | 0.1087 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0993 | 198 | 0.6998 | 0.1573 | 0.1151 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0637 | 127 | 0.7115 | 0.1563 | 0.1215 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0637 | 127 | 0.6646 | 0.1892 | 0.1389 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0587 | 117 | 0.6869 | 0.1716 | 0.1881 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0512 | 102 | 0.6810 | 0.1782 | 0.2048 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0311 | 62 | 0.6356 | 0.2304 | 0.2940 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1jx2k4i | 0.0301 | 60 | 0.7059 | 0.1326 | 0.0629 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0271 | 54 | 0.6576 | 0.2046 | 0.2114 |

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
