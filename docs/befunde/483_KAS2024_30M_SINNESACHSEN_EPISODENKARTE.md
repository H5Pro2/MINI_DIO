# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-21 11:09:51

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\_codex_kas_profile_stability\KAS2024_30M`
- CSV: `docs\befunde\483_KAS2024_30M_SINNESACHSEN_EPISODENKARTE.csv`

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

### KAS2024_30M

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.2156 | 430 | 0.7179 | 0.1342 | 0.0638 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.2026 | 404 | 0.7073 | 0.1421 | 0.1069 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0953 | 190 | 0.6976 | 0.1574 | 0.1138 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0797 | 159 | 0.6614 | 0.1930 | 0.1386 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0722 | 144 | 0.7094 | 0.1543 | 0.1189 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0637 | 127 | 0.6768 | 0.1812 | 0.2126 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0582 | 116 | 0.6865 | 0.1725 | 0.1918 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0311 | 62 | 0.6349 | 0.2318 | 0.2953 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0191 | 38 | 0.6598 | 0.2015 | 0.2062 |
| fuehlen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0145 | 29 | 0.6340 | 0.2275 | 0.2425 |

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
