# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-21 11:09:52

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\_codex_kas_profile_stability\KAS2024_1H`
- CSV: `docs\befunde\484_KAS2024_1H_SINNESACHSEN_EPISODENKARTE.csv`

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

### KAS2024_1H

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.2282 | 455 | 0.7164 | 0.1343 | 0.0627 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.2177 | 434 | 0.7090 | 0.1408 | 0.1039 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1003 | 200 | 0.6962 | 0.1584 | 0.1151 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0817 | 163 | 0.6660 | 0.1887 | 0.1327 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0682 | 136 | 0.7104 | 0.1557 | 0.1184 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0667 | 133 | 0.6874 | 0.1727 | 0.1842 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0481 | 96 | 0.6772 | 0.1829 | 0.2079 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0306 | 61 | 0.6328 | 0.2329 | 0.2948 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0216 | 43 | 0.6574 | 0.2050 | 0.2129 |
| fuehlen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0186 | 37 | 0.6321 | 0.2264 | 0.2154 |

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
