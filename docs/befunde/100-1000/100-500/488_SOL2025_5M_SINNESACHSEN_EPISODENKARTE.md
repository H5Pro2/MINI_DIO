# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-21 12:16:18

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\_codex_asset_year_stability\SOL2025_5M`
- CSV: `docs\befunde\488_SOL2025_5M_SINNESACHSEN_EPISODENKARTE.csv`

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

### SOL2025_5M

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1745 | 348 | 0.7177 | 0.1334 | 0.0642 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1605 | 320 | 0.7094 | 0.1410 | 0.1091 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0752 | 150 | 0.6978 | 0.1580 | 0.1163 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0632 | 126 | 0.6689 | 0.1879 | 0.1326 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1joiyc3 | 0.0542 | 108 | 0.7034 | 0.1389 | 0.0664 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0522 | 104 | 0.6889 | 0.1705 | 0.1846 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0446 | 89 | 0.6810 | 0.1798 | 0.2143 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0421 | 84 | 0.7107 | 0.1543 | 0.1197 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1joiyc3 | 0.0371 | 74 | 0.6925 | 0.1480 | 0.1123 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_1joiyc3 | 0.0306 | 61 | 0.6880 | 0.1574 | 0.1104 |

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
