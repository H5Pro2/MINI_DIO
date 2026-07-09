# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-21 14:07:35

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\_codex_sol_section_compare\SOL2024_5M_STRESS_4K`
- CSV: `docs\befunde\506_SOL2024_5M_STRESS_4K_SINNESACHSEN_EPISODENKARTE.csv`

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

### SOL2024_5M_STRESS_4K

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.2171 | 867 | 0.7208 | 0.1333 | 0.0619 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.2033 | 812 | 0.7142 | 0.1399 | 0.1080 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0999 | 399 | 0.7007 | 0.1568 | 0.1132 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0721 | 288 | 0.6744 | 0.1843 | 0.1253 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0636 | 254 | 0.6898 | 0.1718 | 0.1871 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0588 | 235 | 0.7132 | 0.1553 | 0.1160 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0516 | 206 | 0.6841 | 0.1780 | 0.2070 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0328 | 131 | 0.6444 | 0.2253 | 0.2803 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0205 | 82 | 0.6632 | 0.2043 | 0.2132 |
| fuehlen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0150 | 60 | 0.6450 | 0.2192 | 0.2242 |

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
