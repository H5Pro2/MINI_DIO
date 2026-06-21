# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-21 14:07:33

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\_codex_sol_section_compare\SOL2024_5M_QUIET_4K`
- CSV: `docs\befunde\502_SOL2024_5M_QUIET_4K_SINNESACHSEN_EPISODENKARTE.csv`

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

### SOL2024_5M_QUIET_4K

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1728 | 690 | 0.7205 | 0.1314 | 0.0601 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1565 | 625 | 0.7143 | 0.1385 | 0.1061 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0836 | 334 | 0.7022 | 0.1565 | 0.1135 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0686 | 274 | 0.6748 | 0.1845 | 0.1279 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0508 | 203 | 0.7132 | 0.1552 | 0.1190 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0498 | 199 | 0.6907 | 0.1707 | 0.1831 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0496 | 198 | 0.6856 | 0.1773 | 0.2075 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0325 | 130 | 0.7223 | 0.1351 | 0.0638 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0315 | 126 | 0.7152 | 0.1362 | 0.0968 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0258 | 103 | 0.6443 | 0.2244 | 0.2798 |

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
