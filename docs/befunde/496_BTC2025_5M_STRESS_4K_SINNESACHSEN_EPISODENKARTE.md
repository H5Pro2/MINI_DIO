# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-21 13:02:58

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\_codex_btc2025_section_shift\BTC2025_5M_STRESS_4K`
- CSV: `docs\befunde\496_BTC2025_5M_STRESS_4K_SINNESACHSEN_EPISODENKARTE.csv`

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

### BTC2025_5M_STRESS_4K

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1602 | 640 | 0.7215 | 0.1316 | 0.0602 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1550 | 619 | 0.7150 | 0.1392 | 0.1054 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0914 | 365 | 0.7044 | 0.1543 | 0.1102 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0548 | 219 | 0.6717 | 0.1849 | 0.1255 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0483 | 193 | 0.7145 | 0.1552 | 0.1162 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0413 | 165 | 0.6851 | 0.1781 | 0.2101 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0413 | 165 | 0.6891 | 0.1725 | 0.1918 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0346 | 138 | 0.7103 | 0.1368 | 0.0985 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0343 | 137 | 0.7158 | 0.1346 | 0.0618 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0220 | 88 | 0.6473 | 0.2227 | 0.2735 |

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
