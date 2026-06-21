# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-21 11:09:49

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\_codex_kas_profile_stability\KAS2024_5M`
- CSV: `docs\befunde\481_KAS2024_5M_SINNESACHSEN_EPISODENKARTE.csv`

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

### KAS2024_5M

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1439 | 287 | 0.7183 | 0.1336 | 0.0619 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1389 | 277 | 0.7106 | 0.1423 | 0.1111 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1jx2k4i | 0.0772 | 154 | 0.7124 | 0.1347 | 0.0637 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1jx2k4i | 0.0687 | 137 | 0.7024 | 0.1429 | 0.1054 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0667 | 133 | 0.6989 | 0.1570 | 0.1166 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0592 | 118 | 0.6694 | 0.1872 | 0.1264 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0366 | 73 | 0.7109 | 0.1564 | 0.1188 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0341 | 68 | 0.6898 | 0.1693 | 0.1847 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0321 | 64 | 0.6850 | 0.1759 | 0.2098 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_1jx2k4i | 0.0291 | 58 | 0.6897 | 0.1586 | 0.1140 |

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
