# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-21 14:07:37

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\_codex_sol_section_compare\SOL2025_5M_STRESS_4K`
- CSV: `docs\befunde\514_SOL2025_5M_STRESS_4K_SINNESACHSEN_EPISODENKARTE.csv`

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

### SOL2025_5M_STRESS_4K

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1522 | 608 | 0.7220 | 0.1327 | 0.0607 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1365 | 545 | 0.7155 | 0.1393 | 0.1046 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0766 | 306 | 0.7030 | 0.1556 | 0.1118 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0679 | 271 | 0.7214 | 0.1325 | 0.0598 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0608 | 243 | 0.7150 | 0.1373 | 0.0991 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0486 | 194 | 0.6746 | 0.1846 | 0.1249 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0448 | 179 | 0.6948 | 0.1675 | 0.1795 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0411 | 164 | 0.7144 | 0.1544 | 0.1153 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0320 | 128 | 0.6997 | 0.1573 | 0.1131 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0315 | 126 | 0.6848 | 0.1781 | 0.2099 |

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
