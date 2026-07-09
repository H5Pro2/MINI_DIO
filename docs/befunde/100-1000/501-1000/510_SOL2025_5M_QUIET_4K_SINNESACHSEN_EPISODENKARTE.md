# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-21 14:07:36

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\_codex_sol_section_compare\SOL2025_5M_QUIET_4K`
- CSV: `docs\befunde\510_SOL2025_5M_QUIET_4K_SINNESACHSEN_EPISODENKARTE.csv`

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

### SOL2025_5M_QUIET_4K

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.2216 | 885 | 0.7210 | 0.1327 | 0.0631 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.2066 | 825 | 0.7144 | 0.1391 | 0.1035 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1104 | 441 | 0.7025 | 0.1566 | 0.1143 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0749 | 299 | 0.6747 | 0.1840 | 0.1301 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0638 | 255 | 0.6898 | 0.1716 | 0.1869 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0538 | 215 | 0.6844 | 0.1790 | 0.2131 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0471 | 188 | 0.7115 | 0.1553 | 0.1170 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0320 | 128 | 0.6440 | 0.2233 | 0.2747 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0275 | 110 | 0.6666 | 0.1992 | 0.2020 |
| fuehlen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0213 | 85 | 0.6418 | 0.2207 | 0.2295 |

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
